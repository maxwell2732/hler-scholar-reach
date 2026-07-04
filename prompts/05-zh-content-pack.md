# Stage 5 — 中文传播包

Goal：基于核心叙事与 claim ledger，生成中文渠道内容。中文内容独立
创作（见 `references/bilingual-localization.md`），不从英文版翻译。
所有渠道规范见 `references/channel-profiles.md`。

## 平台分层（v0.2）

中文平台不是同一文本的长短版本。按 campaign brief 的
`channels_zh` 只生成被请求的渠道，每个渠道按其角色独立构建：
`wechat`（完整解释与归档）、`institutional_news`（正式发布）、
`group_share`（熟人触达）、`video`（演示证明）、`zhihu`（问题驱动
解释）、`xiaohongshu`（视觉化发现）。分层矩阵与硬边界见
`references/channel-profiles.md`"中文平台角色分层"。

## 前置条件

- Stage 4 完成。若 Gate 1 尚未通过，所有文件带
  `> STATUS: DRAFT — 待 Gate 1 确认` 头部及句级 `[UNVERIFIED]` 标记。

## Paper 输出

```
output/<project-name>/05_zh/
├── wechat_article.md        # 公众号长文
├── wechat_titles.md         # 5–8 个备选标题 + 每个的取舍说明
├── institutional_news.md    # 机构新闻稿
├── group_share_message.md   # 群分享（100–200 字）
├── video_script_60sec.md    # 60 秒视频脚本
├── video_script_long.md     # 5–12 分钟视频脚本
└── figure_caption_zh.md     # 图表中文说明（仅限有权使用的图）
```

若请求了 zhihu / xiaohongshu 渠道，另生成本文件末尾"知乎输出"
"小红书输出"两节所列文件（paper 与 repository 通用）。

### 公众号文章结构

标题 → 导语（3 句内说清这是什么研究、发现了什么）→ 研究背景 →
研究问题 → 数据和方法（教学式解释，注明简化处）→ 核心发现（逐条，
带边界措辞）→ 学术贡献 → 现实意义（克制，不越过证据）→
几点需要说明的边界（=局限性，自然表达）→ 论文信息与访问方式
（作者、状态、链接、推荐引用格式）。

### 禁止（Gate 3 会扫描，但生成时就要避免）

- 摘要直译；标题党；"国际领先/填补空白/重磅"
- 隐去局限性；把 working paper 写成"发表于"
- 相关性写成因果（对照 ledger 的 allowed_language_zh）

### 备选标题要求

`wechat_titles.md` 中每个标题注明：吸引力来源、是否完全被 ledger
支持、风险点。不提供任何"标题党但有效"的选项。

## Repository 输出

```
output/<project-name>/05_zh/
├── launch_blog.md             # 发布长文（可用于公众号）
├── tutorial_intro.md          # 入门教程（跟随 Quick Start 实测步骤）
├── group_share_message.md
├── bilibili_title_options.md  # 标题 ≤40 字；含封面文字建议（≤13 字）
├── bilibili_description.md    # 简介区：链接、引用方式、章节时间轴占位
├── video_script_60sec.md
└── video_script_long.md
```

### Repo 内容重点（按此顺序回答）

为谁开发 → 解决什么真实问题（具体场景）→ 如何使用（真实步骤）→
与直接写 prompt 的区别 → Human-in-the-Loop 设计（人负责什么）→
已知限制（如实，含 prototype 状态）→ GitHub 地址 → 引用方式。

### 视频脚本格式

两列式：`[画面]`（屏幕内容/操作）与 `[口播]`（讲稿）。60 秒版前
5 秒必须出现"这个工具帮你做什么"；长版按章节分段并给出章节名。
只演示 ledger 中 `software_capability` 级别的功能；design goal
只能以"计划中"表述。

## 知乎输出（v0.2，paper 与 repository 通用）

```
output/<project-name>/05_zh/
├── zhihu_question_options.md   # 3–6 个建议问题 + 每个的合规判断
├── zhihu_answer.md             # 回答体（8 步结构）
├── zhihu_article.md            # 文章体（8 步结构）
└── zhihu_summary.md            # 100–200 字，文章顶部摘要或对外分享
```

- 结构遵循 `references/channel-profiles.md` 中 `zhihu` 档案；
  回答体模板见 `templates/zhihu-answer.md`。
- 建议问题必须：真实、有知识价值、能脱离项目名称独立成立；
  禁止"如何评价我开发的……"、伪造第三方口吻、假装已有大量关注。
  `zhihu_question_options.md` 中每个问题附一行合规说明。
- 回答体第 4 步引入项目时必须透明署名（"我们开发了/我建立了"）。
- 不得从公众号文章复制改写；从问题出发重新组织。

## 小红书输出（v0.2，paper 与 repository 通用）

```
output/<project-name>/05_zh/
├── xiaohongshu_titles.md        # 6–10 个标题，分问题型/方法型/工具型/教程型
├── xiaohongshu_post.md          # 正文（6 步结构，100–300 字）
├── xiaohongshu_carousel.md      # 6–8 页卡片脚本（结构化 YAML，见模板）
├── xiaohongshu_topics.md        # 3–6 个真实相关话题 + "仅为建议"声明
└── xiaohongshu_visual_brief.md  # 封面与卡片视觉说明（竖版 3:4）
```

- 卡片脚本使用 `templates/xiaohongshu-carousel.yaml` 的结构化格式，
  每页含 page/role/headline/body/suggested_visual/claims_used/
  prohibited_implications/alt_text，保证可解析、可交给图像生成。
- 标题不使用"震惊/必看/绝了/封神/闭眼入"等词；任何较强表述加
  `[需人工判断]` 标记。
- 局限页（第 7 页）是必选页。
- paper 特殊规则与 repo 特殊规则见
  `references/academic-integrity.md` 第 9 节。

## 通用规则

- 句式风格：遵守 `references/bilingual-localization.md`"句式与
  标点：避免机器腔"（禁"不是……而是……"、禁元话语开场、破折号
  极度克制），每个文件完成后按该节自查。
- 群分享消息与长文遵守同一 claim 边界；所有渠道同理。
- 数字、状态、链接与 Stage 4 完全一致。
- 每个文件末尾附 HTML 注释：`<!-- claims used: C01, C03, ... -->`；
  小红书卡片按页在 `claims_used` 字段标注。
- 完成每个渠道后更新 state.json 的 `completed_channel_outputs` 与
  `channel_review_status`（初始为 draft）。

## Exit criteria

- campaign brief 请求的全部渠道文件生成；claims-used 注释/字段齐全
- state.json 更新（含渠道级状态）
