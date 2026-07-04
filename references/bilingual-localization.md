# Bilingual Localization Guide — 翻译不等于本地化

Chinese and English communication packages are built from the same
claim ledger but are **separately composed**, not translated from each
other. Same facts, different rhetorical architecture.

## Why sentence-by-sentence translation fails

- 中文学术传播读者期待"来龙去脉"：先讲背景与问题缘起，再讲做了什么。
  英文读者（尤其社交平台）期待 30 秒内看到 problem → contribution。
- 英文平台文化奖励明确陈述 limitations；中文语境中生硬翻译的
  "本研究存在以下局限"在公众号里读起来像论文，而应转化为
  "几点需要说明的边界"式的自然表达。
- 直译的英文推荐语在中文里显得空洞（"exciting work!" → "激动人心的
  工作"），直译的中文谦辞在英文里显得不自信。

## 中文平台内部同样不做互译（v0.2）

"翻译不等于本地化"同样适用于中文平台之间：知乎、小红书、公众号
承担不同角色（见 `references/channel-profiles.md` 中文平台角色
分层），从同一 claim ledger 独立构建，而不是同一篇文章的长短改写。
知乎从问题出发；小红书按视觉卡片重组；公众号做完整解释与归档。

## Chinese content priorities（中文内容优先呈现）

1. 研究背景与问题缘起 —— 为什么会做这项研究/工具
2. 方法与过程的可理解解释 —— 读者想知道"怎么做的"
3. 学术价值与现实关联
4. 工具类：完整的使用过程演示（一步步）
5. 图文并茂；视频教程接受度高
6. 局限性：以"边界说明"的方式自然融入，而不是删掉

## English content priorities

1. Problem — one sentence, concrete
2. Contribution — what THIS work adds
3. Evidence — design and key numbers, with boundaries
4. Limitations — stated plainly, early enough to be honest
5. Reusable resource — what the reader can take away today
6. Link and citation — canonical, once

## Equivalence rules (what MUST stay identical)

- All numbers: sample size, effect direction, version numbers, dates
- Claim strength: if EN says "associated with", ZH must say "相关"
  — never "导致" (this is checked in Stage 9)
- Publication/maturity status
- Author names (use the paper's own romanization/characters; never
  auto-transliterate names)
- The canonical link

## Divergence rules (what SHOULD differ)

| Aspect | 中文 | English |
|---|---|---|
| Opening | 背景/缘起，可讲述 | Problem statement, direct |
| Structure | 叙事推进，小标题分节 | Front-loaded, inverted pyramid |
| Method depth | 更详细，教学式 | Compressed, one plain sentence + link |
| Tone markers | 克制的第一人称复数（"我们发现"） | Direct first person, no false modesty |
| CTA | 阅读原文/引用/联系 | Try it / read it / reach out |
| Length norms | 公众号 1500–4000 字正常 | LinkedIn >300 words already long |

## Terminology handling

- 首次出现的关键术语：中文内容给出"中文译名（English term）"；
  英文内容不夹中文。
- 没有通行中文译名的方法名（如 difference-in-differences 的场合），
  给出解释性译法并保留英文原名。
- 机构名使用其官方中文/英文名称，不自行翻译。

## Anti-patterns（禁止）

- 用机器翻译产出另一语言版本后仅做润色
- 中文版删除英文版明确写出的局限性（或反之）
- 中文标题加"重磅""震撼"等以补偿"信息密度损失"
- 英文版为了简洁把 working paper 状态省略

## 句式与标点：避免机器腔（v0.2，中英文均适用）

以下句式在生成内容中读起来像模板，一律避免：

1. **"不是……而是……"对比框架**（英文对应 "this is X, not Y" 及
   "X, not Y" 同位补刀）。直接陈述肯定的那一半；需要否定时单独
   成句。
   - 差："约束是可检查的，不是希望性的。"
   - 好："约束因此变得可检查。"
2. **元话语开场**："这里需要先说明……""但要说清边界……""值得
   注意的是……"。删掉引导语，直接说内容本身。
3. **破折号克制**：中文"——"与英文"—"尽量少用，一句话内绝不
   出现两个。列举改用括号或冒号；补充说明改用逗号或拆句。
   Markdown 列表项的"- 路径 — 说明"格式不在此限。

理由：本项目的卖点是可信的学术传播，内容一旦读出模板腔，
可信度先打折。Stage 5/6 生成内容后按本节自查一遍。
