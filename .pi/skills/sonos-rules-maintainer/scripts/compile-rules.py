#!/usr/bin/env python3
"""Compile canonical modular Sonos rules into printable vaults/system/rules.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RULES_DIR = Path("vaults/system/rules")
MANIFEST = RULES_DIR / "_meta" / "manifest.yml"
TITLE_PAGE = RULES_DIR / "_meta" / "title-page.md"
OUTPUT = Path("vaults/system/rules.md")

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n?", re.S)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1).lstrip("\n")


def parse_manifest(path: Path) -> list[dict[str, str | int]]:
    if not path.exists():
        raise FileNotFoundError(f"Manifest not found: {path}")

    entries: list[dict[str, str | int]] = []
    current: dict[str, str | int] | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "modules:":
            continue
        if stripped.startswith("- path:"):
            if current:
                entries.append(current)
            value = stripped.split(":", 1)[1].strip().strip('"')
            current = {"path": value}
            continue
        if current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            value = value.strip().strip('"')
            if key == "level":
                current[key] = int(value)
            else:
                current[key] = value

    if current:
        entries.append(current)

    for entry in entries:
        if "path" not in entry or "level" not in entry or "heading" not in entry:
            raise ValueError(f"Malformed manifest entry: {entry}")
    return entries


def rewrite_module_headings(text: str, level: int, heading: str) -> str:
    lines = strip_frontmatter(text).splitlines()
    out: list[str] = []
    first_heading_seen = False

    for line in lines:
        m = HEADING_RE.match(line)
        if not m:
            out.append(line)
            continue

        old_level = len(m.group(1))
        title = m.group(2).strip()
        if not first_heading_seen:
            out.append(f"{'#' * level} {heading}")
            first_heading_seen = True
            continue

        # Module files are authored with H1 as their local root. Shift nested headings
        # back into printable-document depth.
        new_level = min(6, max(1, level + old_level - 1))
        out.append(f"{'#' * new_level} {title}")

    if not first_heading_seen:
        out.insert(0, f"{'#' * level} {heading}")

    return "\n".join(out).rstrip() + "\n"


def build_document(rules_dir: Path, title_page: Path, entries: list[dict[str, str | int]]) -> str:
    parts: list[str] = []
    if title_page.exists():
        parts.append(title_page.read_text(encoding="utf-8").rstrip())

    for entry in entries:
        module_path = rules_dir / str(entry["path"])
        if not module_path.exists():
            raise FileNotFoundError(f"Module listed in manifest not found: {module_path}")
        module_text = module_path.read_text(encoding="utf-8")
        parts.append(rewrite_module_headings(module_text, int(entry["level"]), str(entry["heading"])).rstrip())

    return "\n\n".join(part for part in parts if part).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile modular Sonos rules into printable rules.md")
    parser.add_argument("--rules-dir", default=RULES_DIR.as_posix())
    parser.add_argument("--manifest", default=MANIFEST.as_posix())
    parser.add_argument("--title-page", default=TITLE_PAGE.as_posix())
    parser.add_argument("--output", default=OUTPUT.as_posix())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rules_dir = Path(args.rules_dir)
    manifest = Path(args.manifest)
    title_page = Path(args.title_page)
    output = Path(args.output)

    try:
        entries = parse_manifest(manifest)
        document = build_document(rules_dir, title_page, entries)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Manifest: {manifest}")
    print(f"Modules: {len(entries)}")
    print(f"Output: {output}")

    if args.dry_run:
        print("DRY RUN — no files written")
        print(f"Compiled characters: {len(document)}")
        return 0

    old = output.read_text(encoding="utf-8") if output.exists() else None
    output.write_text(document, encoding="utf-8")
    if old == document:
        print("UNCHANGED: printable rules already up to date")
    else:
        print("WROTE: printable rules regenerated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
