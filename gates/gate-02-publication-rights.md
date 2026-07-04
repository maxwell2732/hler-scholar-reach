# Human Gate 2 — Publication Rights / 发布权利与合规确认

**When**: after Stage 7 (visual briefs), before the launch plan is
finalized. / 在视觉说明完成后、发布计划定稿前。

**Default posture**: uncertainty is NOT safety. Any item answered
`unknown` blocks the affected content until resolved.
存在不确定性时不得默认安全；`unknown` 即阻塞相关内容。

## Procedure for the AI

1. Generate `output/<project>/gates/gate_02_publication_rights.md`
   pre-filled with what the materials show (manifest `constraints`,
   audit findings, figure_selection.md rights column).
2. For every item, state the evidence found or `unknown — needs your
   answer`.
3. Record decisions; update the campaign brief constraints, the
   figure selection, the launch calendar (embargo → T0), and
   state.json (`gate_status.publication_rights`, `unresolved_risks`).

## Checklist to pre-fill

### Papers 论文

- [ ] Embargo：有无 embargo？日期？（evidence or unknown）
- [ ] 正式发表状态：ledger 中的 publication_status 与事实一致？
- [ ] 传播许可：期刊/会议是否允许在此阶段公开传播？
- [ ] Manuscript version：哪个版本可以公开（preprint / accepted
      manuscript / version of record）？依据（期刊自存档政策）？
- [ ] 出版商图片版权：figure_selection.md 中每张图的 rights 状态
- [ ] 共同作者知情：所有共同作者是否知悉并同意此次传播？
- [ ] 未公开数据：内容中是否引用了尚未公开的数据或结果？
- [ ] 同行评审泄露：是否有任何内容来自审稿过程？

### Repositories 代码仓库

- [ ] 敏感文件：audit 的安全扫描结果（secrets、tokens、.env、
      个人路径、受限数据）——列出发现的具体路径
- [ ] LICENSE 与再分发：宣传中的用法是否与 LICENSE 一致？
- [ ] 依赖合规：是否重打包了他人成果而未署名？
- [ ] 截图内容：演示截图中是否含 API keys、个人信息、真实数据？

### Both 通用

- [ ] 机构规定：所属机构是否对外宣传有审批要求？
- [ ] 资助方要求：资助致谢是否按要求出现？

## Decision block

```
GATE 2 DECISION
Reviewed by: <name>
Date: <date>
Result: approved | approved_with_changes | rejected
Blocked items (remain blocked until resolved):
- ...
```

The AI never fills the decision block itself.
