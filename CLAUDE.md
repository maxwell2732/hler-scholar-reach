# CLAUDE.md — hler-scholar-reach

## 写作风格（强制，适用于本仓库生成的一切文档与传播内容）

作者（Chen Zhu 朱晨）的句式偏好，中英文内容一律遵守：

1. **禁用"不是……而是……"对比句式**，英文禁用 "this is X, not Y"
   及 "X, not Y" 同位补刀。直接陈述肯定的内容；确需否定时单独成句。
   - 差："约束是可检查的，不是希望性的。"
   - 好："约束因此变得可检查。"
2. **禁用元话语开场**："这里需要先说明……""但要说清边界……"
   "值得注意的是……"。删掉引导语，直接说内容。
3. **破折号极度克制**：中文"——"与英文"—"能不用就不用，一句话内
   绝不出现两个。列举用括号或冒号，补充说明用逗号或拆句。
   Markdown 列表项的 `- 路径 — 说明` 格式除外。

完整规则与正反例见
`references/bilingual-localization.md` 的"句式与标点：避免机器腔"
一节。scholar-reach 工作流的 Stage 4/5/6 生成内容后必须按该节自查。

## 项目约定

- 作者署名统一使用：`Chen Zhu 朱晨 | 遗传社科研究`（LICENSE/
  CITATION.cff/README 三处保持一致）。
- 仓库地址：https://github.com/maxwell2732/hler-scholar-reach
- 不执行 git push、不创建 GitHub Release、不向任何平台自动发帖。
- 生成的传播内容进入 `output/<project>/`，默认不提交。
- 所有传播内容服从 claim ledger 与四道 Human Gates（见
  `.claude/skills/scholar-reach/SKILL.md`）。

## 测试

```bash
bash tests/test-structure.sh
python tests/test-claim-consistency.py
```
