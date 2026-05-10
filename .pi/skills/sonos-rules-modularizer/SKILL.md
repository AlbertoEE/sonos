---
name: sonos-rules-modularizer
description: Legacy/bootstrap splitter for Sonos rules. Splits vaults/system/rules.md into modules only when recovering or importing an old monolithic rules file. Do not use for normal ongoing rule edits after canonical modular migration; use sonos-rules-maintainer instead.
---

# Sonos Rules Modularizer

This is a **legacy/bootstrap** skill for splitting an old monolithic Sonos rules document into modules.

Current canonical policy is:

```text
vaults/system/rules/     # source of truth
vaults/system/rules.md   # generated printable document
```

For normal ongoing edits, use `sonos-rules-maintainer`, not this skill.

## Core Policy

- Do **not** run this in normal workflow if `vaults/system/rules/_meta/manifest.yml` exists.
- Treat this as an import/recovery tool only.
- Normal rule changes must edit canonical modules and compile with `sonos-rules-maintainer`.
- Running this against canonical modules may overwrite curated frontmatter and patch workflow metadata.

## When to Use

Use this skill only when:

- importing an old monolithic `vaults/system/rules.md` into modules;
- recovering modular files from the printable document;
- explicitly bootstrapping a fresh repo before `sonos-rules-maintainer` is initialized.

Do not use it for rules questions, design tasks, or normal updates.

## Files

```text
.pi/skills/sonos-rules-modularizer/
├── SKILL.md
└── scripts/
    └── split-rules.py
```

## Workflow

### 1. Dry run first

Always preview the split before writing files:

```bash
python3 .pi/skills/sonos-rules-modularizer/scripts/split-rules.py --dry-run
```

Check that the generated paths look sensible.

### 2. Generate modules

```bash
python3 .pi/skills/sonos-rules-modularizer/scripts/split-rules.py
```

This creates or updates:

```text
vaults/system/rules/index.md
vaults/system/rules/glossary.md
vaults/system/rules/core/*.md
vaults/system/rules/character/*.md
vaults/system/rules/instrument/*.md
vaults/system/rules/combat/*.md
vaults/system/rules/negotiation/*.md
```

### 3. Validate

After generation, inspect:

```bash
find vaults/system/rules -type f -name '*.md' | sort
```

Verify:

- this was an intentional bootstrap/recovery operation;
- canonical `_meta/manifest.yml` was not accidentally overwritten;
- `vaults/system/rules/index.md` links to each module;
- no handwritten file was overwritten.

## Generated Module Conventions

Legacy generated modules used `generated_by: sonos-rules-modularizer` and `do_not_edit: true` frontmatter. After canonical migration, normal modules instead use `rules_status: canonical` and are maintained by `sonos-rules-maintainer`.

The body is normalized so the module starts with a level-1 heading, with nested headings adjusted relative to it.

## Folder Mapping

The splitter maps the current numbered structure approximately like this:

- `1.*` → `core/`
- `2.1`, `2.2`, `2.3` → `character/`
- `2.4.*` → `instrument/`
- `3.*` → `combat/`
- `4.*` → `negotiation/`

Some unnumbered subsections, such as `Subidas de Tensión`, `Estados Negativos`, or negotiation motivations, are also split into their own modules when they are useful AI reference targets.

## InfraNodus / Ontology Follow-Up

Useful upstream InfraNodus skills found:

- `skill-llm-wiki`: useful as broad inspiration for markdown knowledge-base workflows, but too broad to be the main splitter.
- `skill-ontology-creator`: useful after modularization to create `infranodus/rules-ontology.md` and analyze overloaded concepts, isolated mechanics, weak links, and missing glossary entries.
- `critical-perspective` / `shifting-perspective`: useful later for design review, not required for deterministic splitting.

Suggested second-pass workflow after modules exist:

1. Read all generated `vaults/system/rules/**/*.md` files.
2. Use `ontology-creator` to generate an append-only rules ontology.
3. Save it as `infranodus/rules-ontology.md`.
4. Use InfraNodus to inspect clusters, gaps, bridge concepts, and overloaded terms.
5. Use the findings to improve the master rules or create more targeted Sonos skills.

## How Future Sonos Skills Should Use the Output

Do not tell future skills to read the whole master rules file by default. Instead, reference the generated index and relevant modules.

Examples:

- Combat questions: read `vaults/system/rules/combat/*.md` and relevant resources from `character/` or `instrument/`.
- Card design: read `instrument/pulsos.md`, `instrument/rudimentos.md`, `instrument/fundamentos.md`, `character/recursos-de-un-cantor.md`, and combat action economy files.
- Negotiation scenes: read `negotiation/*.md` only.
- Glossary checks: read `vaults/system/rules/glossary.md` plus the module where the term appears.
