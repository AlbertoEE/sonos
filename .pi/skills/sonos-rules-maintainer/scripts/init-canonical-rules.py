#!/usr/bin/env python3
"""Promote generated Sonos rule modules to canonical modular source of truth."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

RULES_MD = Path("vaults/system/rules.md")
RULES_DIR = Path("vaults/system/rules")
META_DIR = RULES_DIR / "_meta"
PATCH_DIR = Path("vaults/system/rules-patches")
VERSION = "Alpha 0.1.0"
TODAY = date.today().isoformat()
GENERATOR_MARKER = "generated_by: sonos-rules-modularizer"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.S)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for raw in m.group(1).splitlines():
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fm[key.strip()] = value.strip().strip('"')
    return fm, text[m.end():].lstrip("\n")


def make_frontmatter(old: dict[str, str]) -> str:
    title = old.get("title", "Untitled").replace('"', '\\"')
    source_section = old.get("source_section", title).replace('"', '\\"')
    return (
        "---\n"
        f"title: \"{title}\"\n"
        "rules_status: canonical\n"
        f"source_section: \"{source_section}\"\n"
        f"version_introduced: \"{VERSION}\"\n"
        f"last_reviewed: \"{TODAY}\"\n"
        "---\n\n"
    )


def parse_master_headings(master: Path) -> tuple[str, dict[int, tuple[int, str]]]:
    text = master.read_text(encoding="utf-8")
    lines = text.splitlines()
    heading_by_line: dict[int, tuple[int, str]] = {}
    first_numbered_idx: int | None = None

    for idx, line in enumerate(lines, start=1):
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        heading = m.group(2).strip()
        heading_by_line[idx] = (level, heading)
        if first_numbered_idx is None and re.match(r"\d+(?:\.\d+)*\.?\s+", heading):
            first_numbered_idx = idx - 1

    title_page = "\n".join(lines[: first_numbered_idx or 0]).rstrip() + "\n"
    return title_page, heading_by_line


def module_files(rules_dir: Path) -> list[Path]:
    excluded = {rules_dir / "index.md", rules_dir / "glossary.md"}
    return sorted(
        p
        for p in rules_dir.rglob("*.md")
        if p not in excluded and "_meta" not in p.parts
    )


def collect_modules(rules_dir: Path, heading_by_line: dict[int, tuple[int, str]]) -> list[dict[str, object]]:
    modules: list[dict[str, object]] = []
    for path in module_files(rules_dir):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        start = int(fm.get("source_start_line", "999999"))
        level, heading = heading_by_line.get(start, (1, fm.get("source_section", fm.get("title", path.stem))))
        modules.append(
            {
                "path": path,
                "rel": path.relative_to(rules_dir).as_posix(),
                "start": start,
                "level": level,
                "heading": heading,
                "frontmatter": fm,
                "body": body,
                "is_generated": GENERATOR_MARKER in text,
            }
        )
    return sorted(modules, key=lambda m: int(m["start"]))


def manifest_content(modules: list[dict[str, object]]) -> str:
    lines = [
        "# Canonical print order for Sonos modular rules.",
        "# Edit this when adding, removing, or reordering rule modules.",
        "modules:",
    ]
    for module in modules:
        heading = str(module["heading"]).replace('"', '\\"')
        lines.append(f"  - path: \"{module['rel']}\"")
        lines.append(f"    level: {module['level']}")
        lines.append(f"    heading: \"{heading}\"")
    lines.append("")
    return "\n".join(lines)


def version_content() -> str:
    return (
        f"current_version: \"{VERSION}\"\n"
        f"updated: \"{TODAY}\"\n"
        "source_of_truth: \"vaults/system/rules/\"\n"
        "printable: \"vaults/system/rules.md\"\n"
    )


def changelog_content() -> str:
    return (
        "# Sonos Rules Changelog\n\n"
        f"## {VERSION} — {TODAY}\n\n"
        "- Promoted modular rules to canonical source of truth.\n"
        "- `vaults/system/rules.md` is now generated for printable use.\n"
        "- Added manifest, version metadata, and patch history workflow.\n"
    )


def patch_content(modules: list[dict[str, object]]) -> str:
    affected = "\n".join(f"  - vaults/system/rules/{m['rel']}" for m in modules)
    return (
        "---\n"
        "type: rules_patch\n"
        f"version: \"{VERSION}\"\n"
        f"date: {TODAY}\n"
        "status: applied\n"
        "affected_files:\n"
        f"{affected}\n"
        "  - vaults/system/rules/_meta/manifest.yml\n"
        "  - vaults/system/rules/_meta/version.yml\n"
        "  - vaults/system/rules/_meta/changelog.md\n"
        "  - vaults/system/rules.md\n"
        "---\n\n"
        f"# {VERSION} — Canonical Modular Rules\n\n"
        "## Intent\n\n"
        "Make modular rule files the source of truth so future AI-assisted rule changes can be small, contextual, and versioned. Keep `vaults/system/rules.md` as the generated printable document.\n\n"
        "## Changes\n\n"
        "- Promoted generated modules in `vaults/system/rules/` to canonical editable rules.\n"
        "- Added `_meta/manifest.yml` to define printable order and heading levels.\n"
        "- Added `_meta/version.yml` and `_meta/changelog.md`.\n"
        "- Added patch history folder `vaults/system/rules-patches/`.\n\n"
        "## Design Notes\n\n"
        "This is a workflow patch, not a mechanical rules change. No game mechanics were intentionally changed.\n\n"
        "## Follow-ups\n\n"
        "- [ ] Use `sonos-rules-maintainer` for future changes instead of editing the printable master file.\n"
    )


def index_content(modules: list[dict[str, object]]) -> str:
    labels = {
        "core": "Core system",
        "character": "Cantores / character rules",
        "instrument": "Instrumento Vital",
        "combat": "Combat",
        "negotiation": "Negotiation",
    }
    lines = [
        "---",
        "title: \"Sonos Rules Index\"",
        "generated_by: sonos-rules-maintainer",
        "do_not_edit: true",
        "---",
        "",
        "# Sonos Rules Index",
        "",
        "AI-facing index for the canonical modular Sonos rules.",
        "The modular files are the source of truth; `vaults/system/rules.md` is compiled from them.",
        "",
    ]
    current = None
    for module in modules:
        rel = str(module["rel"])
        folder = rel.split("/", 1)[0]
        if folder != current:
            if current is not None:
                lines.append("")
            current = folder
            lines.extend([f"## {labels.get(folder, folder.title())}", ""])
        title = str(module["heading"])
        display = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", title)
        lines.append(f"- [{display}]({rel}) — print heading `{title}`")
    lines.append("")
    return "\n".join(lines)


def write(path: Path, content: str, dry_run: bool, force: bool = True) -> None:
    if dry_run:
        print(f"PLAN: write {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        print(f"SKIP: exists {path}")
        return
    old = path.read_text(encoding="utf-8") if path.exists() else None
    path.write_text(content, encoding="utf-8")
    print(("UNCHANGED" if old == content else "WROTE") + f": {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Promote generated Sonos rules modules to canonical source of truth")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not RULES_MD.exists():
        print(f"ERROR: missing {RULES_MD}", file=sys.stderr)
        return 1
    if not RULES_DIR.exists():
        print(f"ERROR: missing {RULES_DIR}", file=sys.stderr)
        return 1

    title_page, heading_by_line = parse_master_headings(RULES_MD)
    modules = collect_modules(RULES_DIR, heading_by_line)
    generated_count = sum(1 for m in modules if m["is_generated"])

    print(f"Modules found: {len(modules)}")
    print(f"Generated modules promotable: {generated_count}")
    print(f"Version: {VERSION}")

    write(META_DIR / "title-page.md", title_page, args.dry_run)
    write(META_DIR / "manifest.yml", manifest_content(modules), args.dry_run)
    write(META_DIR / "version.yml", version_content(), args.dry_run)
    write(META_DIR / "changelog.md", changelog_content(), args.dry_run, force=False)
    write(PATCH_DIR / f"{TODAY}-alpha-0.1.0-canonical-modular-rules.md", patch_content(modules), args.dry_run, force=False)
    write(RULES_DIR / "index.md", index_content(modules), args.dry_run)

    for module in modules:
        path = Path(module["path"])
        if not module["is_generated"] and not args.dry_run:
            print(f"SKIP non-generated module: {path}")
            continue
        content = make_frontmatter(module["frontmatter"]) + str(module["body"]).rstrip() + "\n"
        write(path, content, args.dry_run)

    print("Done." if not args.dry_run else "Dry run complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
