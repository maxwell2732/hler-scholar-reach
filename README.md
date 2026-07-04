<div align="center">

# HLER Scholar Reach

### 面向论文与开源科研工具的双语学术传播工作流

**作者： 朱 晨 | 遗传社科研究 Chen Zhu | China Agricultural University (CAU) + Fable 5**  
**最后更新： 2026-07-04**

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-8250df?style=flat-square&logo=anthropic&logoColor=white)](.claude/skills/scholar-reach/SKILL.md)
[![Human in the Loop](https://img.shields.io/badge/Human--in--the--Loop-required-2da44e?style=flat-square)](#-human-gates)
[![Bilingual](https://img.shields.io/badge/languages-中文%20%7C%20English-0ea5e9?style=flat-square)](README_EN.md)
[![License](https://img.shields.io/badge/license-MIT-6e7781?style=flat-square)](LICENSE)

[![中文文档](https://img.shields.io/badge/Docs-中文-1f6feb?style=for-the-badge)](README.md)
[![English README](https://img.shields.io/badge/Docs-English-6e7781?style=for-the-badge)](README_EN.md)
[![Quick Start](https://img.shields.io/badge/Quick-Start-2da44e?style=for-the-badge)](#-quick-start)
[![Workflow](https://img.shields.io/badge/View-Workflow-8250df?style=for-the-badge)](#-工作流总览)
[![Citation](https://img.shields.io/badge/How_to-Cite-d29922?style=for-the-badge)](#-citation)

</div>

> [!IMPORTANT]
> HLER Scholar Reach 当前为 **v0.2 早期原型**。系统可以审计材料、整理受众并起草内容，所有科学结论、发表状态、版权信息和最终发布决定仍由研究者确认。系统不会自动向任何平台发帖。

> **AI prepares; human approves and publishes.**

HLER Scholar Reach 将论文、工作论文、研究报告和开源科研工具整理成可复用的中英文传播内容。每项核心表述都应追溯到原始材料或 claim ledger，并经过四个 Human Gates。

<details>
<summary><strong>📚 展开目录</strong></summary>

- [Quick Start](#-quick-start)
- [项目概览](#-项目概览)
- [工作流总览](#-工作流总览)
- [Human Gates](#-human-gates)
- [支持的成果与渠道](#-支持的成果与渠道)
- [核心机制](#-核心机制)
- [与普通 marketing skill 的区别](#-与普通-marketing-skill-的区别)
- [仓库结构](#-仓库结构)
- [使用方法](#-使用方法)
- [示例与测试](#-示例与测试)
- [学术诚信与版权](#-学术诚信与版权)
- [Roadmap](#-roadmap)
- [Citation](#-citation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

## 🚀 Quick Start

```bash
# 1. 获取本仓库
git clone https://github.com/maxwell2732/hler-scholar-reach
cd hler-scholar-reach

# 2. 在 Claude Code 中调用
/scholar-reach

# 也可以直接描述任务
# 请为当前论文生成中英文传播包。
# 请为当前 GitHub 项目制定发布和传播方案。

# 3. 运行自检
bash tests/test-structure.sh
python tests/test-claim-consistency.py
```

论文材料可以包括 PDF、摘要和结果表。处理 GitHub 项目时，可以在目标仓库中安装本 skill，也可以从 HLER Scholar Reach 读取外部仓库并把传播输出单独保存在 `output/`。

## ✨ 项目概览

| 项目 | 当前实现 |
|---|---|
| 适用对象 | 研究者、研究团队、科研机构和开源科研工具开发者 |
| Artifact | Paper、working paper、preprint、研究报告、GitHub repository |
| 中文渠道 | 微信公众号、机构新闻、微信群、B站/视频号、知乎、小红书 |
| 英文渠道 | GitHub、LinkedIn、Bluesky/X、lay summary |
| 核心控制 | Claim Ledger + 4 个 Human Gates |
| 发布方式 | 仅生成草案和发布计划，由研究者审核并手动发布 |
| 当前状态 | v0.2，早期原型，尚未经过外部用户系统验证 |

学术传播常见的风险包括把相关关系写成因果关系、把 preprint 写成正式发表论文、把早期原型包装成成熟产品，以及编造使用量或影响力指标。HLER Scholar Reach 将这些约束写进工作流和检查点，让传播内容更准确，也更容易复核。

## 🧭 工作流总览

```text
Stage 0  Intake                         材料盘点与任务识别
    ↓
Stage 1  Artifact Audit                论文或仓库审计
    ↓
Stage 2  Audience Strategy             受众与信息矩阵
    ↓
Stage 3  Claim Ledger                  可传播断言台账
    ↓
⛔ Gate 1  Scientific Integrity        科学诚信确认
    ↓
Stage 4  Core Narrative                双语叙事母版
    ↓
Stage 5  Chinese Content Pack          中文平台内容
Stage 6  English Content Pack          英文平台内容
    ↓
Stage 7  Visual Asset Briefs           视觉素材说明
    ↓
⛔ Gate 2  Publication Rights          发表权利与版权确认
    ↓
Stage 8  Launch Plan                   三波传播计划
    ↓
⛔ Gate 3  No-Hype Review              去夸大审查
    ↓
Stage 9  Integrity Review              跨文件一致性检查
    ↓
⛔ Gate 4  Final Approval              逐平台最终批准
```

各阶段的详细执行说明见 [`prompts/`](prompts/)。

## 🛡️ Human Gates

| Gate | 研究者需要确认的内容 |
|---|---|
| [Gate 1 科学诚信](gates/gate-01-scientific-integrity.md) | 核心发现、效应方向、因果措辞、数字、局限和软件功能真实性 |
| [Gate 2 发布权利](gates/gate-02-publication-rights.md) | Embargo、发表状态、可公开版本、图片版权、共同作者知情和敏感文件 |
| [Gate 3 去夸大](gates/gate-03-no-hype.md) | 强表述是否有证据支持，以及是否需要保守替换 |
| [Gate 4 最终批准](gates/gate-04-final-approval.md) | 逐平台核准最终版本，批准前不标记为 `publication-ready` |

Gate 1 尚未通过时，系统可以继续生成带 `[UNVERIFIED]` 标记的草案。Gate 4 完成前，所有内容保持 `draft` 或 `review-required`。

## 🌐 支持的成果与渠道

### Artifact 类型

- **Paper**：已发表论文、online first、accepted manuscript、working paper、preprint、研究报告。
- **GitHub Repository**：Claude Code Skill、research workflow、数据清理工具、分析代码仓库、教学工具和开源科研软件。

### 中文平台分层

| 渠道 | 主要作用 | 典型输出 |
|---|---|---|
| 微信公众号 | 完整解释与长期归档 | 长文、标题、摘要 |
| 中文机构新闻 | 正式成果发布 | 新闻稿、成果简介 |
| 微信群分享 | 熟人网络快速触达 | 100–200 字短消息 |
| B站 / 视频号 | 演示使用过程和可信度 | 长短视频脚本、章节、封面说明 |
| 知乎 | 问题驱动的知识解释 | 问题建议、回答、文章 |
| 小红书 | 视觉化发现和轻量教育 | 短正文、标题、6–8 页卡片脚本 |

知乎内容从一个可独立成立的问题出发，直接回答问题并透明介绍作者自己的项目。小红书内容以视觉卡片为中心，同时保留项目状态、局限和 claim traceability。

<details>
<summary><strong>查看小红书卡片结构示例</strong></summary>

```yaml
cards:
  - page: 7
    role: limitation
    headline: "它做不到什么"
    body: "早期原型；不自动发布；不保证任何传播效果"
    suggested_visual: "AI 准备内容，研究者审核发布"
    claims_used: [C02, C10]
    prohibited_implications: ["成熟产品", "自动化营销"]
    alt_text: "说明工具适用边界的卡片"
```

</details>

### 英文渠道

- GitHub README、Release 和 Social Preview
- LinkedIn
- Bluesky / X
- Lay summary 和 short announcement

中文和英文内容共享同一份事实与 claim strength，但采用各自适合的结构和表达。

## 🧠 核心机制

### Claim Ledger

Stage 3 将允许传播的断言整理为 CSV。每条 claim 记录：

- 原始文件和位置
- claim 类型
- 证据与置信度
- 中英文允许措辞
- 禁止措辞
- 局限和限定条件
- 是否需要人工批准

平台内容只能使用台账中已有的核心断言，并保留 claim traceability 注释。

### 三波传播法

| 阶段 | 内容 |
|---|---|
| Launch | 正式介绍成果、核心发现或主要功能，并提供主链接 |
| Use case | 展示案例、教程、方法说明或常见问题 |
| Update | 仅在出现新版本、采用案例或其他真实进展时发布 |

该设计适合低维护的学术传播，不依赖机械的每日发帖计划。

### 平台身份透明

作者可以用第一人称介绍自己的项目，例如“我们开发了”。系统禁止伪装第三方推荐、虚构评论、虚构使用体验、虚构问答和虚假社会证明。

## 🧩 与普通 marketing skill 的区别

| 维度 | 普通 marketing skill | HLER Scholar Reach |
|---|---|---|
| 素材来源 | 可以自由发挥 | 核心表述来自 claim ledger，并可追溯到原文位置 |
| 因果措辞 | 经常不区分证据等级 | 按研究设计分级，观察性结果使用关联性表述 |
| 发表状态 | 可能被包装 | Working paper、preprint 和 accepted manuscript 如实标注 |
| 软件状态 | 容易扩大能力 | Prototype、tested 和 production-ready 分开处理 |
| 发布动作 | 可能直接发布 | 生成草案，由人类审核和发布 |
| 传播节奏 | 高频运营 | 三波传播，根据真实进展更新 |
| 中英文 | 常见做法是直译 | 分别组织叙事和平台结构 |

## 📁 仓库结构

```text
hler-scholar-reach/
├── .claude/skills/scholar-reach/   # Claude Code Skill 入口
├── prompts/                         # Stage 0–9 执行说明
├── gates/                           # 四个 Human Gate
├── references/                      # 长期规则与渠道规范
├── templates/                       # YAML / JSON / CSV / Markdown 模板
├── examples/                        # 两个虚构示例
├── tests/                           # 结构与 claim 一致性测试
└── output/                          # 生成的 campaign，默认不提交到 git
```

典型输出结构：

```text
output/<project-name>/
├── state.json
├── 00_intake/  01_audit/  02_audience/  03_claims/
├── 04_narrative/  05_zh/  06_en/  07_visuals/
├── 08_launch/  09_review/  10_retrospective/
└── gates/
```

## 🛠️ 使用方法

在 Claude Code 中运行：

```text
/scholar-reach
```

也可以通过自然语言指定对象和渠道：

```text
请为当前论文生成中英文传播包。
请为当前 GitHub 项目制定发布和传播方案。
请只生成知乎回答和小红书卡片。
请读取 ../pAI-Econ-claude，并在本仓库 output 中生成传播草案。
```

v0.2 支持渠道选择：

```text
/scholar-reach --channels zhihu,xiaohongshu
```

中文渠道 ID：`wechat`、`institutional_news`、`group_share`、`video`、`zhihu`、`xiaohongshu`。  
英文渠道 ID：`github`、`linkedin`、`bluesky`、`x`、`lay_summary`。

系统先读取材料，再提出必要问题。无法确认的信息记录为 `unknown`。对仓库的改进默认生成为建议或 patch，不自动 commit、push 或创建 release。

## 🧪 示例与测试

### 示例

- [`examples/paper-example/`](examples/paper-example/)：虚构 working paper，展示如何避免把相关关系写成因果关系。
- [`examples/repository-example/`](examples/repository-example/)：虚构早期原型 `clean-panel`，展示如何避免把原型描述为成熟产品。

### 自检

```bash
bash tests/test-structure.sh
python tests/test-claim-consistency.py
```

结构测试检查核心文件、Skill frontmatter、模板字段和状态文件。Claim consistency 测试扫描禁止措辞、否定语境、行号定位和输出追溯信息。

## 📜 学术诚信与版权

完整规则见 [`references/academic-integrity.md`](references/academic-integrity.md)。

- 不编造发现、DOI、引用量、stars、forks、downloads、用户评价或媒体报道。
- 不把相关关系写成因果关系。
- 不把 preprint 或 working paper 写成正式发表论文。
- Embargo 状态不明确时记录为 `unknown`。
- 出版商图片默认不视为可自由复用。
- 不泄露同行评审内容、受限数据、密钥或个人信息。
- 作者和机构署名以原始材料及人工确认为准。

> [!NOTE]
> HLER Scholar Reach 不保证论文获得引用，也不保证项目获得 stars、forks、媒体报道或其他学术影响。它帮助研究者更准确、更有结构地整理和传播已有成果。

## 🗺️ Roadmap

### 已在 v0.2 实现

- 知乎和小红书适配
- 中文平台角色分层
- 平台身份透明规则
- No-hype 扫描与否定语境识别
- 渠道选择参数
- 结构化小红书卡片模板

### 后续方向

- ResearchGate、Reddit、Hacker News 和媒体 pitch
- 机构官网 CMS
- ORCID、Crossref、Zenodo 和 Altmetric 集成
- GitHub analytics 与自动链接检查
- 社交平台 API
- 卡片和视觉素材生成
- 多项目 campaign dashboard
- 合作者审批流程
- 传播效果复盘
- Quick、Standard 和 Full 三种运行模式

## 📖 Citation

**作者： 朱 晨 | 遗传社科研究 Chen Zhu | China Agricultural University (CAU)**

引用格式见 [`CITATION.cff`](CITATION.cff)。使用本工作流开展研究传播时，欢迎在论文、项目文档或软件说明中引用。

## 🤝 Contributing

欢迎提交 issue、改进模板或补充渠道规范。贡献前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 📄 License

本项目采用 [MIT License](LICENSE)。
