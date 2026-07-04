# Claim Language Guide

The core rule: **the strength of the language must not exceed the
strength of the evidence.** This guide maps claim types to allowed and
prohibited phrasing in both languages. Stage 3 (claim ledger) applies
it claim by claim; Gate 3 (no-hype) and Stage 9 (integrity review)
enforce it across all generated content.

## Claim types

| claim_type | Evidence basis | Default confidence ceiling |
|---|---|---|
| `descriptive` | Counts, distributions, sample characteristics | high |
| `observational_association` | Non-experimental correlation/regression | medium |
| `causal_experimental` | RCT / randomized design | high (within design limits) |
| `causal_quasi_experimental` | DiD, IV, RDD, natural experiments | medium-high, assumption-dependent |
| `causal_genetic` | MR, twin/family designs | medium, assumption-dependent |
| `mechanism_supported` | Direct mechanistic evidence in this work | medium |
| `mechanism_hypothesized` | Proposed, not tested here | low — must be labeled speculation |
| `software_capability` | Feature demonstrated/tested in the repo | high for demonstrated, else downgrade |
| `software_design_goal` | Intended but not yet achieved/validated | must be labeled as goal, not capability |
| `adoption_metric` | User-supplied number with date | exact number + date only |
| `publication_status` | Journal/venue records or user statement | exact status vocabulary only |

## Language mapping

### observational_association

- EN allowed: *was associated with; was linked to; correlated with;
  respondents with X reported higher Y*
- EN prohibited: *caused; led to; prevented; reduces (as causal);
  improves (as causal); proves; shows that X makes Y*
- ZH allowed：与……相关；与……存在关联；X 较高的群体报告了更高的 Y
- ZH prohibited：导致；引起；预防；改善（因果义）；证明；使得

### causal_experimental

- EN allowed: *increased/decreased (in the trial); the intervention
  raised Y by ...; caused (if the design supports it)*
- Still prohibited: *proves; guarantees; will work for everyone;
  solves*
- ZH allowed：干预使 Y 提高了……；实验组相比对照组……
- ZH prohibited：彻底解决；完全证明；对所有人有效

### causal_quasi_experimental / causal_genetic

- EN allowed: *provides causal evidence that ... under [assumptions];
  consistent with a causal effect of X on Y*
- Must carry the identifying assumption in `qualifications`.
- ZH allowed：在……假设下提供了因果证据；结果与 X 对 Y 的因果效应一致
- Prohibited: unconditional causal statements without the assumption.

### mechanism_hypothesized

- EN allowed: *one possible explanation is ...; the authors hypothesize ...*
- EN prohibited: *the mechanism is ...; X works by ...*
- ZH allowed：一种可能的解释是……；作者推测……
- ZH prohibited：其机制是……；X 通过……起作用

### software_capability vs software_design_goal

- Capability (demonstrated): *clean-panel flags duplicate IDs and
  produces an audit log* — only if this is shown in tests/examples.
- Design goal: EN *is designed to / aims to / intended for*;
  ZH：旨在……；目标是……；设计用于……
- Prohibited for prototypes: *production-ready; battle-tested;
  widely adopted; enterprise-grade*; ZH：成熟稳定；广泛使用；
  经过大规模验证。

### publication_status

- Working paper: EN *working paper (not yet peer-reviewed)*;
  ZH：工作论文（尚未经过同行评审）。
- Preprint: EN *preprint on <server> (not yet peer-reviewed)*;
  ZH：预印本（发布于 <平台>，尚未经过同行评审）。
- Never: "published in", "研究发表于《...》" unless status=published
  or online_first (with "online first" stated).

## Universal prohibited vocabulary (any claim type)

EN: groundbreaking, revolutionary, unprecedented, first-ever,
game-changing, transformative, solves, proves, prevents, guarantees,
world-leading, paradigm-shifting.

ZH: 颠覆性、革命性、全球首个、国际领先、填补国际空白、彻底解决、
完全证明、杜绝、保证、必然导致、重大突破（无第三方依据时）。

Exception process: if the user insists one of these is factually
supported (e.g. a genuinely registered "first"), it requires (a) a
citable source in the manifest, and (b) explicit human approval in
Gate 3. The scanner still reports it; the human overrides it.

## Conservative fallback

When evidence for a claim's type or strength is unclear:

1. Downgrade one level (causal → association; capability → design goal).
2. Add `[UNVERIFIED]` and set `human_approval_required = yes`.
3. Never resolve ambiguity in the direction of the stronger claim.
