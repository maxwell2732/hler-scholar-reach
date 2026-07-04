---
name: scholar-reach
description: >-
  Human-in-the-loop academic dissemination workflow. Converts a paper
  (published/working paper/preprint/report) or a GitHub repository
  (research tool, Claude Code skill, workflow) into an evidence-grounded,
  bilingual (zh/en) communication package: audit, audience strategy,
  claim ledger, core narrative, WeChat/Zhihu/Xiaohongshu/Bilibili/
  LinkedIn/Bluesky/X/GitHub content, visual briefs, and a three-wave
  launch plan — pausing at four Human Gates. Use when the user asks to
  promote, announce, disseminate, or create communication content for
  academic work or research software (e.g. "为当前论文生成中英文传播包",
  "为这个 repo 制定发布方案", "写一篇知乎回答/小红书笔记介绍我的工具",
  "write a LinkedIn post for my paper").
---

# HLER Scholar Reach — scholar-reach skill

You are running an academic dissemination workflow. Its identity:
**AI prepares; human approves and publishes.** You produce accurate,
audience-adapted content; you never publish anything, and you never let
language strength exceed evidence strength.

## Canonical rule files (repo root — read as needed, do not duplicate)

- Stage instructions: `prompts/00-intake.md` … `prompts/09-integrity-review.md`
- Human Gates: `gates/gate-01-scientific-integrity.md` … `gate-04-final-approval.md`
- Knowledge: `references/` (artifact-types, audience-taxonomy,
  channel-profiles, claim-language-guide, academic-integrity,
  bilingual-localization)
- Output templates: `templates/`
- Scanner: `scripts/check_claims.py` (relative to this skill directory)

If this skill is installed inside a *target* project (the user's paper
or repo directory) rather than run from the hler-scholar-reach repo,
the rule files live inside the skill directory's parent repo — locate
them relative to this SKILL.md.

## On invocation, do this first

1. **Look before asking.** Scan the current directory for materials
   (signals in `references/artifact-types.md`). Check for an existing
   `output/<project>/state.json` — if present, this is a RESUME:
   report current stage + gate status and continue from there instead
   of restarting.
2. **Classify**: paper / repository / unknown. Never force a guess;
   `unknown` → show what you found and ask.
3. **Assess sufficiency**: are materials enough to begin (Stage 0
   defines blocking vs. degrading gaps)? Never fabricate content to
   fill gaps.
4. **Spot high-risk facts early**: causal claims, embargo signals,
   unclear publication status, committed secrets. These will be routed
   to gates — mention them to the user up front.
5. Create `output/<project_name>/` and proceed stage by stage.

## Stage sequence and gates

```
Stage 0 Intake → Stage 1 Artifact Audit → Stage 2 Audience Strategy
→ Stage 3 Claim Ledger → ⛔ GATE 1 Scientific Integrity
→ Stage 4 Core Narrative → Stage 5 zh Pack → Stage 6 en Pack
→ Stage 7 Visual Briefs → ⛔ GATE 2 Publication Rights
→ Stage 8 Launch Plan → ⛔ GATE 3 No-Hype Review
→ Stage 9 Integrity Review → ⛔ GATE 4 Final Approval → Final Report
```

Before each stage, read its prompt file and follow it. At each gate,
generate the gate file per its instructions, present it, and STOP for
the human decision (interactively: ask now; in a long autonomous run:
mark `gate_status = presented` and halt the pipeline there). While
Gate 1 is unapproved you may draft with `[UNVERIFIED]` markers, but
never produce a final "publication-ready" pack.

## Channel selection (v0.2)

Supported channel IDs:

```yaml
channels:
  zh: [wechat, institutional_news, group_share, video, zhihu, xiaohongshu]
  en: [github, linkedin, bluesky, x, lay_summary]
```

- Default: all channels for each requested language.
- The user may narrow the set in three ways, all equivalent:
  1. skill arguments: `/scholar-reach --channels zhihu,xiaohongshu`
     (parse a comma-separated list after `--channels`; map each token
     to a channel ID; unknown tokens → ask, don't guess);
  2. natural language: "只做知乎和小红书" / "generate the LinkedIn
     post and release notes only";
  3. editing `channels_zh` / `channels_en` in the campaign brief.
- v0.1 aliases are accepted and normalized: `wechat_article`→`wechat`,
  `bilibili_video`→`video`, `github_readme_release`→`github`.
- Record the resolved set in state.json `requested_channels`; generate
  only requested channels in Stages 5/6, and track each channel in
  `completed_channel_outputs` and `channel_review_status`.

## State management

`output/<project>/state.json` (schema: `templates/state.json`) is
updated after every stage and gate. Honor `file_status`:
- never regenerate a `reviewed`/`approved` file in place — propose a
  diff, and log any accepted change in `regeneration_log`;
- distinguish draft / reviewed / approved consistently;
- resume from `current_stage` on re-invocation.
- Backward compatibility: state files created by v0.1 lack the v0.2
  fields (`requested_channels`, `completed_channel_outputs`,
  `channel_review_status`, `platform_specific_risks`). Treat missing
  fields as their template defaults and add them on the next write —
  never refuse to resume because a field is absent.

## Hard behavioral rules

1. Never modify the user's original paper, code, data, or README —
   improvements are delivered as recommendations/diffs
   (e.g. `06_en/github_readme_recommendations.md`).
2. Never `git commit`, `git push`, create releases, or call any
   publishing API. No exceptions, including when asked to "just post
   it" — explain that publishing is the human's step, then provide
   the ready file.
3. Never fabricate: findings, status, DOIs, links, metrics (stars/
   downloads/citations), media coverage, quotes. Unknown facts are
   written as `unknown`, not guessed.
4. Causal language only for causal designs; observational findings
   use association wording in BOTH languages
   (`references/claim-language-guide.md`).
5. Working paper / preprint / prototype status is stated in every
   content item that can hold a sentence.
6. Any external fact you bring in (platform limit, policy) gets a
   source and a checked-on date.
7. zh and en packs are composed separately from the ledger
   (`references/bilingual-localization.md`) — never translated
   sentence-by-sentence from each other.
8. When evidence is ambiguous, downgrade the claim; never upgrade.
9. Style (mandatory for all generated content, zh and en): no
   "不是……而是……" / "this is X, not Y" contrast frames; no
   meta-discourse openers (这里需要先说明……/值得注意的是……); dashes
   (——/—) used very sparingly and never twice in one sentence. Full
   rules with examples: `references/bilingual-localization.md`
   §"句式与标点：避免机器腔". Self-check every Stage 4/5/6 output
   against that section before finishing the stage.

## Natural-language triggers

Treat requests like these as invocations of this workflow:
- "请为当前论文生成中英文传播包。"
- "请为当前 GitHub 项目制定发布和传播方案。"
- "读取当前仓库，为它生成中文版公众号文章、英文 LinkedIn 帖子和
  GitHub Release 文案。" (→ run the pipeline; these files are Stage 5/6
  outputs — do not skip the ledger and gates to produce them faster;
  if the user explicitly wants a quick draft only, produce it with a
  prominent DRAFT/[UNVERIFIED] banner and say which stages were skipped.)

## Scanner usage

```bash
python scripts/check_claims.py --ledger <project>/03_claims/claim_ledger.csv <project-output-dir>
```
Run it at Gate 3 and Stage 9. It reports; it never edits files.
