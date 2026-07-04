# Human Gate 4 — Final Approval / 最终发布批准

**When**: after Stage 9 (integrity review). This is the LAST gate;
nothing is `publication-ready` until it is approved.
Stage 9 之后触发；未批准前任何输出不得标记为 publication-ready。

## Procedure for the AI

1. Verify preconditions and report honestly:
   - Gates 1–3 status (must be approved / approved_with_changes)
   - Stage 9 blocking items count (must be 0, or listed here)
   - remaining `[UNVERIFIED]` markers (must be 0, or listed here)
2. Generate `output/<project>/gates/gate_04_final_approval.md`
   pre-filled with the per-platform final file list (from the launch
   calendar) and the checklist below.
3. Approval is **per platform version**, not blanket: the user ticks
   each file they approve. Unticked files stay `draft`.
4. After approval: set approved files to `approved` in state.json
   `file_status`; write the final report from
   `templates/final-report.md`; only then may
   `publication_readiness.md` say `publication-ready` for those files.
5. Publishing itself is done by the human. The system provides files;
   it never posts, schedules, or uploads.

## Checklist to pre-fill

- [ ] 内容可以公开 — nothing embargoed/confidential remains
- [ ] 作者与机构信息准确 — names, order, affiliations checked in final text
- [ ] 科学结论准确 — Gate 1 corrections all applied (list them)
- [ ] 链接有效 — every URL listed here for the human to click-test
      (v0.1 does not auto-check links)
- [ ] 图片可以使用 — Gate 2 rights decisions reflected in final assets
- [ ] embargo 与版权已处理 — calendar respects embargo; version-of-record
      rules followed
- [ ] 所有 [UNVERIFIED] 已解决 — count is zero (verified by scanner)
- [ ] 平台最终版本逐一批准：

```
| File | Platform | Approve? |
|---|---|---|
| 05_zh/wechat_article.md | 微信公众号 | [ ] |
| ... | ... | [ ] |
```

## Decision block

```
GATE 4 DECISION
Reviewed by: <name>
Date: <date>
Result: approved | partially_approved | rejected
Approved files:
- ...
Withheld files and reasons:
- ...
```

The AI never fills the decision block itself. After this gate, any
regeneration of an approved file resets it to `draft` and re-requires
Gate 4 for that file.
