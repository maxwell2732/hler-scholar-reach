# AGENTS.md - Codex Support Entry

## Repository Purpose

HLER Scholar Reach is a human-in-the-loop scholarly communication workflow.
It converts papers, working papers, research reports, and research-software
repositories into evidence-grounded bilingual communication packages.

The core rule is:

**AI prepares; human approves and publishes.**

Codex should help audit materials, organize claims, draft communication
assets, and improve the workflow. It must not publish content or strengthen
claims beyond the evidence.

## Canonical Workflow

Follow the same stage sequence as the Claude skill in
`.claude/skills/scholar-reach/SKILL.md`:

1. Stage 0: Intake
2. Stage 1: Artifact Audit
3. Stage 2: Audience Strategy
4. Stage 3: Claim Ledger
5. Gate 1: Scientific Integrity
6. Stage 4: Core Narrative
7. Stage 5: Chinese Content Pack
8. Stage 6: English Content Pack
9. Stage 7: Visual Asset Briefs
10. Gate 2: Publication Rights
11. Stage 8: Launch Plan
12. Gate 3: No-Hype Review
13. Stage 9: Integrity Review
14. Gate 4: Final Approval

Before running or modifying a stage, read the corresponding prompt in
`prompts/`. Before applying a gate, read the corresponding file in `gates/`.
Use `references/` for long-lived rules and `templates/` for output shape.

## Codex Operating Rules

- Preserve scientific integrity. Do not fabricate findings, DOIs, citations,
  stars, forks, downloads, testimonials, media coverage, or publication status.
- Keep causal wording aligned with the study design. Observational evidence
  must use association wording in both Chinese and English.
- Treat unknown facts as `unknown`; do not infer them for convenience.
- Do not modify a user's original paper, data, source manuscript, or target
  project README while generating a communication package. Put recommendations,
  diffs, and campaign files under `output/<project>/`.
- Do not run `git commit`, `git push`, create a GitHub release, or call any
  publishing API unless the user explicitly asks for repository maintenance
  work unrelated to publishing the generated campaign.
- Generated campaign content belongs in `output/<project>/` and is ignored by
  git by default.
- Respect reviewed and approved files in `output/<project>/state.json`. Do not
  overwrite them in place; propose a diff or create a new draft.

## Writing Style

For generated communication content in Chinese or English:

- Avoid the contrast frame "not X but Y" and its Chinese equivalent.
- Avoid meta-discourse openers such as "it is worth noting" or
  "here we need to explain first".
- Use dashes sparingly. Never use more than one dash in a sentence.
- Compose Chinese and English outputs separately from the claim ledger instead
  of translating sentence by sentence.

See `references/bilingual-localization.md` for the full style rules.

## Supported Channels

Chinese channel IDs:

- `wechat`
- `institutional_news`
- `group_share`
- `video`
- `zhihu`
- `xiaohongshu`

English channel IDs:

- `github`
- `linkedin`
- `bluesky`
- `x`
- `lay_summary`

If a user narrows channels in natural language, map their request to these IDs
and record the resolved set in `output/<project>/state.json`.

## Tests

Run these checks after structural, template, or scanner changes:

```bash
bash tests/test-structure.sh
python tests/test-claim-consistency.py
```

On Windows, use a shell that can run the Bash script, such as Git Bash or WSL.
The Python scanner uses only the standard library.

## Repository Maintenance Notes

- Keep `.claude/skills/scholar-reach/SKILL.md` and this file behaviorally
  consistent when workflow rules change.
- Keep README, README_EN, LICENSE, and CITATION.cff author and repository
  metadata consistent.
- Do not commit private source materials under `papers/`.
