---
name: sonos-rules-maintainer
description: Maintain Sonos rules through versioned patches using modular rule files as the source of truth, then compile the printable vaults/system/rules.md. Use when modifying, clarifying, adding, versioning, or publishing Sonos TTRPG rules.
---

# Sonos Rules Maintainer

You maintain the Sonos rules as a living ruleset.

The new policy is:

```text
vaults/system/rules/     # canonical modular source of truth
vaults/system/rules.md   # generated printable document
```

Do **not** edit the printable `vaults/system/rules.md` by hand. Edit modular rule files, record a patch, then compile.

## Replaces / supersedes

This skill supersedes `sonos-rules-modularizer` for normal ongoing work.

`sonos-rules-modularizer` is now only a bootstrap/emergency import tool for splitting an old monolithic master file. Normal workflow should use this skill.

## Required files

Canonical rules metadata:

```text
vaults/system/rules/_meta/title-page.md
vaults/system/rules/_meta/manifest.yml
vaults/system/rules/_meta/version.yml
vaults/system/rules/_meta/changelog.md
```

Patch history:

```text
vaults/system/rules-patches/
```

Compiler:

```text
.pi/skills/sonos-rules-maintainer/scripts/compile-rules.py
```

Migration/bootstrap:

```text
.pi/skills/sonos-rules-maintainer/scripts/init-canonical-rules.py
```

## Core workflow

When the user asks to change rules:

1. **Understand intent**
   - Restate the desired change.
   - Ask clarifying questions only if the rule would be ambiguous.

2. **Locate affected modules**
   - Start with `vaults/system/rules/index.md` and `_meta/manifest.yml`.
   - Read only relevant modular files.
   - Do not load `vaults/system/rules.md` unless debugging compilation or checking legacy text.

3. **Draft a patch**
   - Decide version bump:
     - Patch: wording, clarification, small balance tweak.
     - Minor: new subsystem, new rule family, meaningful mechanic.
     - Major: incompatible redesign.
   - Summarize intent, affected files, rule changes, and balance/design notes.

4. **Apply edits to modular files**
   - Edit canonical modules in `vaults/system/rules/`.
   - Add new module files only if needed.
   - If adding a module, also update `_meta/manifest.yml` in the desired print order.

5. **Record versioned patch**
   - Create a patch note in `vaults/system/rules-patches/`.
   - Update `_meta/version.yml`.
   - Append to `_meta/changelog.md`.

6. **Compile printable rules**
   - Run:

```bash
python3 .pi/skills/sonos-rules-maintainer/scripts/compile-rules.py
```

7. **Validate**
   - Check the changed files.
   - Ensure `vaults/system/rules.md` was generated, not hand-edited.
   - If cards are affected, consider whether card files or prompts/skills need updates.

## Version format

Use alpha semver style:

```text
Alpha 0.1.0
Alpha 0.1.1  # small clarification or balance patch
Alpha 0.2.0  # new subsystem or meaningful mechanic
Alpha 1.0.0  # stable release
```

`version.yml` shape:

```yaml
current_version: "Alpha 0.1.0"
updated: "2026-05-10"
source_of_truth: "vaults/system/rules/"
printable: "vaults/system/rules.md"
```

## Patch note format

Create patch files named:

```text
YYYY-MM-DD-alpha-X.Y.Z-short-slug.md
```

Use this content:

```markdown
---
type: rules_patch
version: "Alpha X.Y.Z"
date: YYYY-MM-DD
status: applied
affected_files:
  - vaults/system/rules/...
---

# Alpha X.Y.Z — [Title]

## Intent

[What the user wanted and why.]

## Changes

- [Concrete rule change]
- [Concrete rule change]

## Design Notes

[Balance / interaction notes.]

## Follow-ups

- [ ] [Optional unresolved question]
```

## Compiler behavior

`compile-rules.py` reads:

```text
vaults/system/rules/_meta/title-page.md
vaults/system/rules/_meta/manifest.yml
```

Then writes:

```text
vaults/system/rules.md
```

It strips YAML frontmatter from modules and reconstructs heading levels from the manifest, so the printable document remains readable and printable.

## Adding new rule modules

If adding a new module:

1. Create file in the correct folder.
2. Add frontmatter:

```yaml
---
title: "Rule Title"
rules_status: canonical
version_introduced: "Alpha X.Y.Z"
last_reviewed: "YYYY-MM-DD"
---
```

3. Start body with `# Rule Title`.
4. Add it to `_meta/manifest.yml` in print order:

```yaml
  - path: "combat/new-rule.md"
    level: 2
    heading: "3.7 New Rule"
```

5. Compile.

## Rules for AI edits

- Do not invent hidden rules.
- If the user gives a design thought, convert it into clear procedure.
- Keep wording table-friendly.
- Prefer small localized changes over sweeping rewrites.
- Preserve Spanish terminology used by the rules.
- If a change affects several systems, mention all affected modules.
- If a rule has unresolved edge cases, write them as follow-up questions in the patch note.

## When to update ontology / audits

After a meaningful rules patch, consider updating:

```text
infranodus/rules-ontology.md
documentation/rules-critical-audit.md
```

Do not regenerate the ontology blindly. Treat it as curated: append/edit deliberately.

## Useful commands

Initialize canonical modular rules from the current generated modules:

```bash
python3 .pi/skills/sonos-rules-maintainer/scripts/init-canonical-rules.py --dry-run
python3 .pi/skills/sonos-rules-maintainer/scripts/init-canonical-rules.py
```

Compile printable rules:

```bash
python3 .pi/skills/sonos-rules-maintainer/scripts/compile-rules.py --dry-run
python3 .pi/skills/sonos-rules-maintainer/scripts/compile-rules.py
```
