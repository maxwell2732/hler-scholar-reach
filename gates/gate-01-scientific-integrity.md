# Human Gate 1 — Scientific Integrity / 科学诚信确认

**When**: immediately after Stage 3 (claim ledger). The workflow
PAUSES here. / 完成 claim ledger 后立即触发，工作流在此暂停。

**Rule while pending**: drafts may continue with visible
`[UNVERIFIED]` markers, but NO "publication-ready" final pack may be
produced before this gate is approved.
未通过前可继续生成带 `[UNVERIFIED]` 标记的草案，但不得生成可直接
发布的最终包。

## Procedure for the AI

1. Generate `output/<project>/gates/gate_01_scientific_integrity.md`
   from the checklist below, pre-filled with the actual claims —
   the human confirms concrete statements, not abstract questions.
2. Present the gate file to the user, grouped so causal claims and
   low-confidence claims come first.
3. Record the user's decision per item: `confirmed` /
   `corrected (with the correction)` / `must not communicate`.
4. Apply corrections to the ledger; move "must not communicate" items
   to claim_notes.md as excluded; update state.json
   (`gate_status.scientific_integrity`, `unverified_claims`).

## Checklist to pre-fill (one section per item, quoting the ledger)

### A. Core findings 核心发现
For each main-finding claim: quote `normalized_claim` +
`original_evidence`. Ask: 该发现表述是否准确？Is this accurate as stated?

### B. Causal wording 因果措辞
For each claim typed causal_* or observational_association: show the
allowed zh/en phrasing. Ask: 因果/相关措辞是否正确？可以更强还是必须更弱？

### C. Numbers 数字
Every N, effect size, percentage, version number in the ledger,
with source location. Ask: 数字是否准确？

### D. Missing limitations 遗漏的局限
List the limitations captured. Ask: 是否有关键局限未被列入？

### E. Non-communicable content 不可传播内容
Ask explicitly: 是否存在尚未公开、涉密、或不宜传播的内容混入了
ledger？（未公开数据、审稿意见、失败案例、内部细节）

### F. Software reality check（repo 适用）
For each `software_capability` claim: 该功能当前是否真实可用？
Is this capability actually working today, as described?

### G. Open questions
Any claim with confidence=low or human_approval_required=yes not
covered above.

## Decision block (end of the generated gate file)

```
GATE 1 DECISION
Reviewed by: <name>
Date: <date>
Result: approved | approved_with_changes | rejected
Changes required:
- ...
```

The AI never fills the decision block itself.
