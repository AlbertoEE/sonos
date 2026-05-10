# Pi migration

This directory contains Pi-native copies of the existing Claude Code resources.

- `prompts/*.md` are migrated from `.claude/commands/*.md` and are available as slash prompt templates, e.g. `/crear-boss`, `/idea`, `/revisar-ideas`.
- `skills/sonos-dm-interviewer/SKILL.md` is migrated from `.claude/agents/sonos-dm-interviewer.md` and is available as `/skill:sonos-dm-interviewer`.
- `.claude/` is intentionally left untouched.

After editing these files, run `/reload` inside Pi.
