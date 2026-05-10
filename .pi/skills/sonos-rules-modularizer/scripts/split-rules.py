#!/usr/bin/env python3
"""Split Sonos master rules into AI-facing markdown modules.

Source of truth: vaults/system/rules.md
Generated output: vaults/system/rules/
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_SOURCE = Path("vaults/system/rules.md")
DEFAULT_OUTPUT = Path("vaults/system/rules")
GENERATOR = "sonos-rules-modularizer"
MARKER = f"generated_by: {GENERATOR}"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
NUMBERED_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+(.+)$")
LETTERED_INSTRUMENT_RE = re.compile(r"^[ABC]\)\s+(Pulsos|Rudimentos|Fundamentos)$", re.IGNORECASE)

# Terms for a non-definitional starter glossary. The script does not invent definitions.
GLOSSARY_TERMS = [
    "Sonos",
    "Cantor",
    "Atributos",
    "Ritmo",
    "Melodía",
    "Armonía",
    "Disonancia",
    "Síncopa",
    "Tempo",
    "Habilidades",
    "Perks",
    "Vitalidad",
    "Silencio",
    "Resonancia",
    "Auralium",
    "Instrumento Vital",
    "Pulso",
    "Pulsos",
    "Rudimento",
    "Rudimentos",
    "Fundamento",
    "Fundamentos",
    "Desafinación",
    "Iniciativa",
    "Resintonía",
    "Malicia",
    "Tensión",
    "Estados",
    "Negociación",
    "PNJ",
    "Actitud",
    "Motivación",
    "Escollo",
    "Oferta",
]

FOLDER_LABELS = {
    "core": "Core system",
    "character": "Cantores / character rules",
    "instrument": "Instrumento Vital",
    "combat": "Combat",
    "negotiation": "Negotiation",
    "misc": "Miscellaneous",
}


@dataclass(frozen=True)
class Heading:
    line_index: int
    level: int
    raw_title: str
    clean_title: str
    number: str | None
    text_after_number: str
    folder: str
    is_module: bool


@dataclass(frozen=True)
class Module:
    heading: Heading
    end_line_index: int
    rel_path: Path
    display_title: str
    content: str


def strip_markdown_inline(text: str) -> str:
    text = text.strip()
    # Strip repeated wrapping emphasis used in headings, e.g. **Title**, *Title*.
    changed = True
    while changed:
        changed = False
        for token in ("***", "**", "*"):
            if text.startswith(token) and text.endswith(token) and len(text) >= 2 * len(token):
                text = text[len(token) : -len(token)].strip()
                changed = True
    return text


def strip_number_prefix(title: str) -> str:
    title = strip_markdown_inline(title)
    m = NUMBERED_RE.match(title)
    if m:
        return m.group(2).strip()
    m = re.match(r"^[ABC]\)\s+(.+)$", title)
    if m:
        return m.group(1).strip()
    return title


def slugify(text: str) -> str:
    text = strip_number_prefix(text).lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "section"


def parse_number(title: str) -> tuple[str | None, str]:
    clean = strip_markdown_inline(title)
    m = NUMBERED_RE.match(clean)
    if not m:
        return None, clean
    return m.group(1), m.group(2).strip()


def folder_for(number: str | None, current_number: str | None) -> str:
    effective = number or current_number or ""
    if effective.startswith("1"):
        return "core"
    if effective.startswith("2.4"):
        return "instrument"
    if effective.startswith("2"):
        return "character"
    if effective.startswith("3"):
        return "combat"
    if effective.startswith("4"):
        return "negotiation"
    return "misc"


def is_module_heading(level: int, clean_title: str, number: str | None, current_top: str | None) -> bool:
    # Ignore the title/cover page before the numbered rules begin.
    if current_top is None and number is None:
        return False
    if number is not None and level <= 3:
        return True
    # Useful unnumbered AI reference targets below numbered sections.
    if current_top is not None and level <= 3:
        return True
    # Split the three Instrumento Vital damage primitives even though they are h4.
    if current_top is not None and LETTERED_INSTRUMENT_RE.match(clean_title):
        return True
    return False


def parse_headings(lines: list[str]) -> list[Heading]:
    headings: list[Heading] = []
    current_top: str | None = None
    current_number: str | None = None

    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        raw_title = m.group(2).strip()
        clean_title = strip_markdown_inline(raw_title)
        number, text_after_number = parse_number(clean_title)

        if number:
            current_number = number
            if level == 1:
                current_top = number.split(".")[0]

        module = is_module_heading(level, clean_title, number, current_top)
        folder = folder_for(number, current_number)
        headings.append(
            Heading(
                line_index=i,
                level=level,
                raw_title=raw_title,
                clean_title=clean_title,
                number=number,
                text_after_number=text_after_number,
                folder=folder,
                is_module=module,
            )
        )
    return headings


def adjust_section_markdown(section_lines: list[str], start_level: int, display_title: str) -> str:
    """Normalize the first heading to h1 and shift nested headings accordingly."""
    out: list[str] = []
    first_heading_done = False

    for line in section_lines:
        m = HEADING_RE.match(line)
        if not m:
            out.append(line)
            continue

        level = len(m.group(1))
        title = strip_markdown_inline(m.group(2).strip())
        if not first_heading_done:
            out.append(f"# {display_title}")
            first_heading_done = True
            continue

        new_level = max(2, level - start_level + 1)
        new_level = min(new_level, 6)
        out.append(f"{'#' * new_level} {title}")

    return "\n".join(out).rstrip() + "\n"


def frontmatter(module: Module, source: Path) -> str:
    heading = module.heading
    source_section = heading.clean_title.replace('"', '\\"')
    title = module.display_title.replace('"', '\\"')
    return (
        "---\n"
        f"title: \"{title}\"\n"
        f"generated_from: {source.as_posix()}\n"
        f"generated_by: {GENERATOR}\n"
        f"source_section: \"{source_section}\"\n"
        f"source_start_line: {heading.line_index + 1}\n"
        f"source_end_line: {module.end_line_index}\n"
        "do_not_edit: true\n"
        "---\n\n"
    )


def build_modules(lines: list[str], headings: list[Heading], source: Path) -> list[Module]:
    module_headings = [h for h in headings if h.is_module]
    used_paths: dict[Path, int] = {}
    modules: list[Module] = []

    for idx, heading in enumerate(module_headings):
        start = heading.line_index
        end = module_headings[idx + 1].line_index if idx + 1 < len(module_headings) else len(lines)
        section_lines = lines[start:end]
        display_title = strip_number_prefix(heading.clean_title)
        slug = slugify(heading.clean_title)
        rel_path = Path(heading.folder) / f"{slug}.md"

        if rel_path in used_paths:
            used_paths[rel_path] += 1
            rel_path = rel_path.with_name(f"{rel_path.stem}-{used_paths[rel_path]}{rel_path.suffix}")
        else:
            used_paths[rel_path] = 1

        body = adjust_section_markdown(section_lines, heading.level, display_title)
        module = Module(
            heading=heading,
            end_line_index=end,
            rel_path=rel_path,
            display_title=display_title,
            content="",  # filled below after frontmatter can reference the module
        )
        full_content = frontmatter(module, source) + body
        modules.append(
            Module(
                heading=heading,
                end_line_index=end,
                rel_path=rel_path,
                display_title=display_title,
                content=full_content,
            )
        )
    return modules


def module_sort_key(module: Module) -> tuple[int, int, str]:
    folder_order = {"core": 1, "character": 2, "instrument": 3, "combat": 4, "negotiation": 5, "misc": 9}
    return (folder_order.get(module.heading.folder, 99), module.heading.line_index, module.rel_path.as_posix())


def make_index(modules: list[Module], source: Path) -> str:
    lines = [
        "---",
        "title: \"Sonos Rules Index\"",
        f"generated_from: {source.as_posix()}",
        f"generated_by: {GENERATOR}",
        "do_not_edit: true",
        "---",
        "",
        "# Sonos Rules Index",
        "",
        "This is the AI-facing index generated from `vaults/system/rules.md`.",
        "The master rules file remains the source of truth.",
        "",
        "Use this index to load only the rule modules needed for a task instead of loading the entire master file.",
        "",
    ]

    current_folder: str | None = None
    for module in sorted(modules, key=module_sort_key):
        folder = module.heading.folder
        if folder != current_folder:
            if current_folder is not None:
                lines.append("")
            current_folder = folder
            lines.extend([f"## {FOLDER_LABELS.get(folder, folder.title())}", ""])
        section = module.heading.clean_title
        lines.append(f"- [{module.display_title}]({module.rel_path.as_posix()}) — source section `{section}`")
    lines.append("")
    lines.extend(
        [
            "## Suggested AI Loading Patterns",
            "",
            "- **Rules lookup:** start here, then read only the linked modules relevant to the question.",
            "- **Combat:** read `combat/` plus relevant resources from `character/` or `instrument/`.",
            "- **Cards / abilities:** read `instrument/pulsos.md`, `instrument/rudimentos.md`, `instrument/fundamentos.md`, and relevant combat/action modules.",
            "- **Negotiation:** read `negotiation/` only unless the scene invokes combat or resources.",
            "- **Glossary:** read `glossary.md` to locate terms, then open the linked modules.",
            "",
        ]
    )
    return "\n".join(lines)


def find_term_modules(term: str, modules: Iterable[Module]) -> list[Module]:
    pattern = re.compile(re.escape(term), re.IGNORECASE)
    return [m for m in modules if pattern.search(m.content)]


def make_glossary(modules: list[Module], source: Path) -> str:
    lines = [
        "---",
        "title: \"Sonos Rules Glossary\"",
        f"generated_from: {source.as_posix()}",
        f"generated_by: {GENERATOR}",
        "do_not_edit: true",
        "---",
        "",
        "# Sonos Rules Glossary",
        "",
        "Starter glossary generated from known Sonos terms.",
        "Definitions are intentionally not invented here; each entry points to modules where the term appears.",
        "",
    ]
    for term in GLOSSARY_TERMS:
        found = find_term_modules(term, modules)
        if found:
            links = ", ".join(f"[{m.display_title}]({m.rel_path.as_posix()})" for m in found[:6])
            if len(found) > 6:
                links += f", +{len(found) - 6} more"
        else:
            links = "not found in generated modules"
        lines.append(f"- **{term}** — Appears in: {links}.")
    lines.append("")
    return "\n".join(lines)


def can_overwrite(path: Path) -> bool:
    if not path.exists():
        return True
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False
    return MARKER in text


def write_generated(path: Path, content: str) -> bool:
    if not can_overwrite(path):
        raise RuntimeError(f"Refusing to overwrite non-generated file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def run(args: argparse.Namespace) -> int:
    source = Path(args.source)
    output = Path(args.output)
    if not source.exists():
        print(f"ERROR: source file not found: {source}", file=sys.stderr)
        return 1

    raw_text = source.read_text(encoding="utf-8")
    lines = raw_text.splitlines()
    headings = parse_headings(lines)
    modules = build_modules(lines, headings, source)
    index_content = make_index(modules, source)
    glossary_content = make_glossary(modules, source)

    planned = [(output / "index.md", index_content), (output / "glossary.md", glossary_content)]
    planned.extend((output / m.rel_path, m.content) for m in sorted(modules, key=module_sort_key))

    print(f"Source: {source}")
    print(f"Output: {output}")
    print(f"Detected headings: {len(headings)}")
    print(f"Generated modules planned: {len(modules)}")
    print("")

    if args.dry_run:
        print("DRY RUN — no files written")
        for path, _ in planned:
            print(f"PLAN: {path}")
        return 0

    written = 0
    unchanged = 0
    for path, content in planned:
        changed = write_generated(path, content)
        if changed:
            written += 1
            print(f"WROTE: {path}")
        else:
            unchanged += 1
            print(f"UNCHANGED: {path}")

    print("")
    print(f"Done. Written/updated: {written}; unchanged: {unchanged}; total files: {len(planned)}")
    print("Original master file was not modified.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Split Sonos master rules into generated markdown modules.")
    parser.add_argument("--source", default=DEFAULT_SOURCE.as_posix(), help="Master rules markdown file")
    parser.add_argument("--output", default=DEFAULT_OUTPUT.as_posix(), help="Generated rules directory")
    parser.add_argument("--dry-run", action="store_true", help="Print planned files without writing")
    parser.add_argument("--force-bootstrap", action="store_true", help="Allow overwriting canonical modular workflow output")
    args = parser.parse_args()

    canonical_manifest = Path(args.output) / "_meta" / "manifest.yml"
    if canonical_manifest.exists() and not args.force_bootstrap:
        print(
            f"ERROR: canonical rules manifest exists at {canonical_manifest}.\n"
            "This splitter is now a legacy/bootstrap tool. Use sonos-rules-maintainer for normal rule edits,\n"
            "or rerun with --force-bootstrap only if you intentionally want to re-split from rules.md.",
            file=sys.stderr,
        )
        return 2

    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
