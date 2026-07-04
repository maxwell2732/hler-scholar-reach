# File map — where the canonical rules live

To avoid duplicating content, this skill keeps a single canonical copy
of every rule file at the **repository root** of hler-scholar-reach.
This directory intentionally contains only this map.

| What | Canonical location (repo root) |
|---|---|
| Stage instructions (0–9) | `prompts/00-intake.md` … `prompts/09-integrity-review.md` |
| Human Gates (1–4) | `gates/gate-01-scientific-integrity.md` … `gates/gate-04-final-approval.md` |
| Artifact type rules | `references/artifact-types.md` |
| Audience taxonomy | `references/audience-taxonomy.md` |
| Channel profiles | `references/channel-profiles.md` |
| Claim language guide | `references/claim-language-guide.md` |
| Academic integrity rules | `references/academic-integrity.md` |
| Bilingual localization guide | `references/bilingual-localization.md` |
| Output templates | `templates/` |
| Scanner script | `.claude/skills/scholar-reach/scripts/check_claims.py` (lives with the skill) |

If you copy this skill into another project standalone, copy the
`prompts/`, `gates/`, `references/`, and `templates/` directories into
this skill directory and the workflow will find them relative to
SKILL.md.
