# Audience Taxonomy (v0.1)

Segment IDs used in campaign-brief.yaml and the Audience–Message Matrix.
For each selected segment, Stage 2 must fill all eight matrix fields
(who / cares about / may misunderstand / emphasize / don't emphasize /
content forms / channels / CTA).

## Paper audiences

| ID | Segment | Typical core question | Common misunderstanding risk |
|---|---|---|---|
| `same_field_scholars` | 同领域学者 | Is the identification/design credible? What's new vs. the literature? | Overreading effect sizes; assuming causality from association |
| `adjacent_field_scholars` | 邻近领域学者 | Can I use this finding/method in my area? | Missing field-specific caveats and data limitations |
| `graduate_students` | 研究生 | How was this done? Can I learn/replicate the method? | Treating one study as settled knowledge |
| `policy_researchers` | 政策研究者 | What does this imply for intervention/regulation? | Jumping from association to policy causality |
| `general_public` | 普通公众 | Does this affect my life? What should I do? | Personal health/behavior advice from population-level findings |
| `science_media` | 科研媒体 | What's the headline? Is there a human story? | Hype amplification; dropping limitations |
| `potential_collaborators` | 潜在合作者 | Is there a data/method/team fit with my work? | Overestimating data availability |

## Repository audiences

| ID | Segment | Typical core question | Common misunderstanding risk |
|---|---|---|---|
| `target_discipline_researchers` | 目标学科研究者 | Does this solve my actual workflow problem? Is it trustworthy? | Assuming maturity/validation beyond actual status |
| `graduate_students` | 研究生 | Can I use this in my thesis? How steep is the learning curve? | Blind trust in automated output |
| `teachers` | 教师 | Can I teach with it? Is it stable for a semester? | Assuming long-term maintenance guarantees |
| `ai_workflow_developers` | AI workflow 开发者 | What's the design? What can I reuse or extend? | Judging by novelty rather than fit |
| `open_source_contributors` | 开源贡献者 | Where can I help? Is the project welcoming and organized? | Unclear scope → misdirected PRs |
| `potential_users` | 潜在用户（泛） | What is this and is it for me, in 30 seconds? | Wrong expectations about what the tool automates |

## General rules

1. Never target `general_public` or `science_media` with content that
   has not passed Gate 1 (scientific integrity) — these segments have
   the least ability to self-correct overclaiming.
2. Each segment gets ONE primary CTA. Multiple CTAs dilute all of them.
3. "What NOT to emphasize" is mandatory — it prevents each segment's
   characteristic misreading, listed in the tables above.
4. If the user's goals (campaign brief) and the chosen segments
   conflict (e.g. goal=software_adoption but no user segment selected),
   flag the mismatch instead of silently fixing it.
