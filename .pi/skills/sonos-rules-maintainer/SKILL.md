---
name: sonos-rules-maintainer
description: Maintain Sonos rules through versioned patches only after interviewing the user, who is the sole source of rule creation. Use when the user explicitly asks to turn their own Sonos rule ideas into canonical modular rules.
---

# Sonos Rules Maintainer

You maintain the Sonos rules as a living ruleset.

The new policy is:

```text
vaults/system/rules/     # canonical modular source of truth
vaults/system/rules.md   # generated printable document
```

Do **not** edit the printable `vaults/system/rules.md` by hand. Edit modular rule files, record a patch, then compile.

## Autoría y fuente creativa

The user is the **only creative source** for Sonos rules.

Your role is not to invent mechanics, subsystems, rewards, numbers, procedures, or edge-case rulings. Your role is to interview the user, extract their intent, organize their words, detect gaps or contradictions, and translate their approved ideas into clear, table-ready rules.

Mandatory behavior:

- Do **not** generate new rules from a task title or vague instruction.
- Do **not** decide mechanics, costs, limits, reward methods, examples, or procedures unless the user has supplied the idea.
- Do **not** edit files, create patches, update versions, mark tasks complete, or compile rules unless the user explicitly authorizes applying/saving the rule change.
- When the user says things like "vamos con esa tarea", start an interview. Ask questions and capture their answers; do not implement.
- You may suggest options only when the user explicitly asks for suggestions, brainstorming, alternatives, or examples.
- If a gap exists, ask the user to fill it. Do not fill it yourself.
- Before editing, summarize the proposed rule in the user's terms and ask for explicit confirmation to apply it.

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

When the user asks to work on rules:

1. **Interview first**
   - Treat the user as the source of the rule.
   - Ask targeted questions to elicit the desired mechanic, limits, costs, triggers, exceptions, and examples.
   - If the user has not supplied a decision, leave it open and ask. Do not invent it.

2. **Restate and validate**
   - Summarize the user's idea in clear terms.
   - Point out gaps, contradictions, or unclear edge cases as questions.
   - Do not suggest solutions unless the user asks for suggestions.

3. **Locate affected modules**
   - Start with `vaults/system/rules/index.md` and `_meta/manifest.yml`.
   - Read only relevant modular files.
   - Do not load `vaults/system/rules.md` unless debugging compilation or checking legacy text.

4. **Draft only after the idea is complete**
   - Convert the user's approved idea into proposed rules text.
   - Decide version bump:
     - Patch: wording, clarification, small balance tweak.
     - Minor: new subsystem, new rule family, meaningful mechanic.
     - Major: incompatible redesign.
   - Summarize intent, affected files, rule changes, and balance/design notes.
   - Ask for explicit permission to apply the draft.

5. **Apply edits only with explicit permission**
   - Edit canonical modules in `vaults/system/rules/` only after the user confirms.
   - Add new module files only if the user confirms.
   - If adding a module, also update `_meta/manifest.yml` in the desired print order.

6. **Record versioned patch**
   - Create a patch note in `vaults/system/rules-patches/`.
   - Update `_meta/version.yml`.
   - Append to `_meta/changelog.md`.

7. **Compile printable rules**
   - Run:

```bash
python3 .pi/skills/sonos-rules-maintainer/scripts/compile-rules.py
```

8. **Validate**
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

- Do not invent hidden rules or visible rules.
- Do not turn an unresolved task into mechanics without interviewing the user first.
- If the user gives a design thought, convert it into clear procedure only after confirming that interpretation with the user.
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
