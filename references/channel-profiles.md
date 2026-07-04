# Channel Profiles (v0.1)

Operational profiles for the channels supported in v0.1. Platform
character limits and features change; the constraints below were last
sanity-checked against general platform knowledge on **2026-07-04** and
are written conservatively. When a limit matters for a specific post,
verify against the platform on the day of publishing and note the check
date in the launch calendar.

Every channel profile answers nine questions: primary purpose,
audience, ideal content length, recommended structure, tone, evidence
expectations, suitable calls to action, prohibited practices, and
reuse relationship with other channels.

---

## 中文平台角色分层（v0.2）

中文平台不是同一篇文章的不同长度版本。每个平台承担不同角色，内容
必须按角色独立构建：

| 渠道 ID | 渠道 | 核心角色 |
|---|---|---|
| `wechat` | 微信公众号 | 完整解释与长期归档 |
| `institutional_news` | 中文机构新闻 | 正式成果发布 |
| `group_share` | 微信群分享 | 熟人网络快速触达 |
| `video` | B站 / 视频号 | 演示和可信度证明 |
| `zhihu` | 知乎 | 问题驱动的知识解释 |
| `xiaohongshu` | 小红书 | 视觉化发现和轻量教育 |

（v0.1 的渠道 ID `wechat_article`、`bilibili_video` 作为别名继续
接受，规范化为上表 ID。）

复用关系的硬边界：

- 知乎不能简单复制公众号——知乎从一个真实问题出发，项目只是答案的
  一部分；公众号从项目本身出发。
- 小红书不能只把公众号拆成短句——小红书以卡片视觉结构重组，每页
  一个信息点。
- 视频脚本不能只是朗读 README——视频的价值是真实演示。
- 群分享文案不能成为长篇摘要——它是一句熟人推荐加一个链接。

---

## 中文渠道

### `wechat` — 微信公众号长文

- 受众姿态：主动点开、愿意读 3–8 分钟的中文读者（同行、学生、机构关注者）。
- 形式：长文，1500–4000 字；小标题分节；图文混排；文末放论文/项目信息。
- 语气：专业但可读；讲清楚背景与过程；克制而非冷漠。
- 有效做法：研究缘起故事化（但不虚构）；方法用类比解释但注明简化；
  图表配中文说明；文末给出完整的论文信息（作者、状态、链接、引用格式）。
- 避免：摘要直译；标题党；"国际领先/填补空白"；隐藏局限性；
  把 working paper 写成"发表于"。
- 外链限制：公众号内不可直接点击外部链接，重要链接需同时给出
  "阅读原文"位置建议和可复制的短链/文字链接。
- CTA：阅读原文 / 引用论文 / 联系作者。
- 核心角色：完整解释与长期归档——这是中文内容的"母版"，其他中文
  渠道可从它借素材，但不得反向由短内容拼凑成公众号文章。
- 证据要求：每个实质断言可追溯 claim ledger；局限性必须成节出现。
- 复用关系：知乎文章可与其共享叙事母版但必须重构为问题驱动；
  小红书卡片提取其要点但重排为视觉结构。

### `group_share` — 微信群或同行群简短分享

- 受众姿态：扫一眼决定是否点开；信任来自分享者本人。
- 形式：约 100–200 个汉字 + 1 个链接；无格式或极简格式。
- 必须三秒内讲清：这是什么、为什么值得看、链接在哪。
- 语气：像同行之间的推荐，不像广告。第一人称自然（"我们组的新工作"）。
- 避免：多个链接；长段落；表情符号轰炸；转发套话；把它写成长篇摘要。
- CTA：单一——点链接。
- 核心角色：熟人网络快速触达；信任由分享者背书，内容只负责准确。
- 证据要求：与长文遵守同一 claim 边界——短不等于松。
- 复用关系：从叙事母版的 one_sentence / elevator_pitch 压缩而来，
  不从公众号文章截段。

### `video` — B站或视频号教程（v0.1 别名：`bilibili_video`）

- 受众姿态：学习导向；完播率取决于前 15 秒。
- 形式：60 秒短版（竖屏可用）+ 5–12 分钟长版教程脚本；
  标题 ≤ 40 字为宜；封面文字 ≤ 13 字可读性最好。
- 有效做法：真实屏幕录制；先展示结果再讲原理；分段章节；
  简介区放完整链接和引用方式。
- 避免：纯 PPT 朗读；朗读 README；夸大工具能力；演示未经验证的功能；
  演示中出现伪造的运行结果。
- CTA：简介区链接 + 三连（可选，不强求）。
- 核心角色：演示和可信度证明——观众亲眼看到工具真的能跑。
- 证据要求：只演示 ledger 中 software_capability 级别的功能；
  录屏必须真实可复现（记录产生该画面的命令与状态）。
- 复用关系：脚本结构独立创作；简介区文字可复用 zhihu_summary 或
  群分享文案。

### `institutional_news` — 中文机构新闻稿

- 受众姿态：机构官网访问者、上级单位、同行机构。
- 形式：500–1200 字；正式、克制；第三人称。
- 结构：导语（一句话成果）→ 背景 → 主要内容 → 意义（克制）→
  论文/项目信息 → 团队与资助信息。
- 必须：作者与机构署名完整准确；发表状态如实；资助致谢按论文原文。
- 避免："国际领先""填补空白""重大突破"等无法验证的定性；
  超出论文结论的政策建议。
- CTA：论文链接。
- 核心角色：正式成果发布——机构口径的存档版本。
- 证据要求：署名、状态、资助信息逐字核对原文；最保守的措辞档位。
- 复用关系：从叙事母版正式化改写；不与社交平台内容互相复制。

### `zhihu` — 知乎（v0.2 新增）

> A question-driven, evidence-grounded knowledge explanation channel.
> 知乎不是公众号的转载渠道：内容从一个真实问题出发，论文或项目
> 只是答案的一部分。

- 核心角色：问题驱动的知识解释。
- 受众：主动搜索"如何做/为什么/有什么区别"的学生、研究者和
  跨领域读者；对营销高度敏感，对证据和边界讨论高度友好。
- 适合：解释学术或方法问题；系统说明研究方法/软件/科研工作流；
  把论文或 repo 作为问题解决方案的一部分；讨论争议、局限和适用边界。
- 不适合：纯公告；只贴摘要和链接；求赞求 star 求关注；冒充第三方
  客观推荐自己的项目；把项目写成已被广泛采用的行业标准。
- 长度：回答 800–2500 字；文章 1500–4000 字；摘要 100–200 字。
- 结构（Answer，8 步）：直接回答问题 → 为什么这个问题困难 →
  常见误区或现有方法不足 → 引入论文/repo（透明署名"我们开发了"）→
  设计、证据或功能 → 一个具体使用例子 → 局限和适用边界 →
  访问和引用方式。
- 结构（Article，8 步）：问题背景 → 为什么现有流程不够 →
  项目做了什么 → 工作流或方法 → 示例 → Human-in-the-Loop 设计 →
  局限 → 获取方式。
- 语气：同行讨论；允许观点，但观点与证据分开陈述；第一人称透明
  （"我开发了""我们的做法是"），绝不伪装成路人推荐。
- 证据要求：知乎读者会追问出处——每个关键断言给出来源；局限性
  讨论是内容价值的一部分而非免责声明。
- CTA：阅读论文 / 试用工具 / 在评论区讨论方法问题。
- 禁止：虚构"用户提问"或伪装第三方口吻；"如何评价我开发的……"式
  自我营销问题；假装已存在大量争议或关注；删掉局限性。
- 建议问题的规则：问题必须真实、有知识价值、**能脱离具体项目名称
  独立成立**（好："学术成果传播与商业营销有什么区别？"；
  坏："如何评价最近爆火的 X？"）。
- 复用关系：可与公众号共享叙事母版素材，但必须重构为问题驱动结构；
  zhihu_summary 可复用于视频简介区。

### `xiaohongshu` — 小红书（v0.2 新增）

> A visual-first discovery and lightweight educational channel.
> 小红书不是微信文章缩写版，也不是娱乐化营销文案生成器。

- 核心角色：视觉化发现和轻量教育——让目标读者"刷到"并在 30 秒内
  理解这个工具/研究和自己有什么关系。
- 受众：研究生、青年研究者、效率工具关注者；移动端浏览，视觉优先。
- 适合：AI 科研工具介绍；学术工作流；研究生效率工具；方法比较；
  教程摘要；视觉化的研究发现解释；从问题到解决方案的卡片式内容。
- 不适合：复杂统计结果的无背景罗列；伪造亲身体验；制造焦虑；
  过度承诺吸引点击；把未验证 prototype 描述成"科研神器"。
- 长度：正文 100–300 字（移动端短段落）；标题 ≤ 20 字为宜；
  卡片 6–8 页，每页一个信息点。
- 结构（正文，6 步）：一句话说明问题 → 谁会遇到这个问题 →
  项目或论文提供什么 → 3–5 个核心要点 → 一个限制或提醒 →
  获取方式。
- 结构（卡片，8 页）：封面（问题或主题）→ 痛点 → 现有做法不足 →
  项目/研究做了什么 → 核心功能或发现 → 使用方法或研究设计 →
  局限 → 获取与引用方式。卡片脚本使用结构化格式
  （`templates/xiaohongshu-carousel.yaml`），每页含 page/role/
  headline/body/suggested_visual/claims_used/prohibited_implications/
  alt_text。
- 标题：生成 6–10 个，按问题型/方法型/工具型/教程型分组；清楚说明
  内容是什么；任何较强表述标注"需人工判断"。
- 话题：3–6 个真实相关话题；不追热门、不编造平台趋势、不做
  hashtag stuffing；明确标注"仅为建议，不代表当前热度"。
- 语气：轻量、诚实、第一人称（"我做了一个工具"）；教育而非带货。
- 证据要求：每页卡片标注 claims_used；图卡不得把统计关联画成确定
  机制；限制页是必选页而非可选页。
- CTA：单一——获取方式页给出地址与引用方式。
- 禁止："闭眼入""全网最强""救命神器""封神""必看"等消费营销表达；
  伪造使用体验或评论；焦虑营销（"再不用就晚了"）；虚构热度。
- 复用关系：从叙事母版提取要点重排为卡片结构；封面视觉与
  social preview / 视频封面共享设计语言但比例不同（竖版 3:4）。

---

## English channels

### `github_readme_release` — GitHub README / Release / Social Preview

- Audience posture: evaluating in <60 seconds whether to try the tool.
- README first screen must answer: what it is, who it's for, what
  problem it solves, how to start (quick start), current status.
- Release notes: versioned, factual, grouped (Added/Changed/Fixed);
  no marketing language; breaking changes flagged first.
- Social preview: 1280×640 px; project name + one-line function;
  readable at thumbnail size (see Stage 7 briefs).
- Avoid: badges implying metrics you don't have; "production-ready"
  on prototypes; screenshots of fabricated output.
- CTA: quick start command; issues welcome; citation instructions.

### `linkedin` — LinkedIn

- Audience posture: professional peers, potential collaborators,
  hiring/funding-adjacent readers; skim in-feed.
- Form: 150–300 words; first 2 lines carry the hook (fold cutoff);
  short paragraphs; ≤3 hashtags; link in post or first comment.
- Tone: professional, first-person, direct. State problem →
  contribution → evidence boundary → link. Not a corporate ad.
- Avoid: "We are thrilled to announce..."; engagement-bait questions;
  tagging people without their consent.
- CTA: read the paper / try the tool / get in touch.

### `bluesky` / `x` — Bluesky and X threads

- Form: thread of 4–6 posts, each post carries exactly ONE idea.
  Bluesky: 300 chars/post; X: 280 chars/post (free tier) — verify on
  posting day. Write to fit the smaller limit so one thread serves both.
- Structure: 1) hook = the finding/capability with its boundary;
  2) why it matters; 3) how (method/design in one plain sentence);
  4) key limitation — stated, not buried; 5) link + citation;
  6) (optional) invitation to discuss/contribute.
- Avoid: threads >6 posts; hype adjectives; screenshots of text that
  should be text; posting figures without alt text.
- CTA: the canonical link, once, near the end.

### `lay_summary` — 英文项目介绍 / lay summary

- Audience posture: educated non-specialists; funders; interdisciplinary
  readers.
- Form: 150–400 words, plain English (~grade 10 reading level);
  no jargon without a one-phrase explanation.
- Structure: problem → what was done → what was found/built →
  what it does NOT show → where to learn more.
- The "what it does NOT show" sentence is mandatory for papers with
  observational designs.

---

## Cross-channel rules

1. One canonical link everywhere; secondary links only where the
   platform allows more than one.
2. Numbers (sample size, effect direction, version) must be identical
   across channels — they all come from the claim ledger.
3. Shorter format ≠ looser claims: the group share message obeys the
   same claim boundaries as the WeChat long article.
4. Nothing is scheduled or posted automatically. The launch calendar
   assigns each item a human owner.
