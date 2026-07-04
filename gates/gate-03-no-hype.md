# Human Gate 3 — No-Hype Review / 去夸大审查

**When**: after Stage 8 (launch plan), across ALL generated content
files. / 在发布计划完成后，对全部生成内容执行。

## Procedure for the AI

1. Run the scanner:
   ```bash
   python .claude/skills/scholar-reach/scripts/check_claims.py \
     --ledger output/<project>/03_claims/claim_ledger.csv \
     output/<project>
   ```
   It reports hits from (a) the universal hype lexicon below and
   (b) each ledger row's `prohibited_language`.
2. Additionally re-read the content for hype the lexicon cannot catch:
   superlatives in context ("the best tool for..."), unfounded
   comparisons ("unlike all existing methods"), implied endorsement,
   certainty inflation ("will change how...").
3. Generate `output/<project>/gates/gate_03_no_hype.md` with one entry
   per hit, in this exact format:

   ```
   ## Hit N
   - File: 05_zh/wechat_article.md, line 42
   - Text: "该方法彻底解决了面板数据清理问题"
   - Term: 彻底解决
   - Evidence check: no ledger claim supports totality; C05 is a
     software_capability limited to duplicate detection
   - Proposed replacement: "该方法针对面板数据清理中的重复记录问题
     提供了一套可复核的处理流程"
   - Human decision: [ ] accept replacement  [ ] keep original
     (justification + source required)  [ ] rewrite as: ______
   ```

4. Every hit gets all four parts: location, evidence judgment,
   conservative replacement, human decision option. No hit is
   auto-fixed without appearing in the gate file.
5. After decisions: apply accepted replacements, log in
   regeneration_log, update state.json (`gate_status.no_hype`).

## Universal lexicon (mirrors the scanner's built-in lists)

- EN: groundbreaking, revolutionary, unprecedented, first-ever,
  game-changing, transformative, solves, proves, prevents, guarantees
- ZH（v0.1 基础）: 颠覆性, 革命性, 全球首个, 国际领先, 填补国际空白,
  彻底解决, 完全证明, 杜绝, 必然导致

### v0.2 新增中文风险类别

**夸张与绝对化**（violation）：科研神器, 必备神器, 救命神器,
全网最强, 天花板, 封神, 一键完成, 零门槛, 无需任何基础, 保证发表,
保证引用, 保证涨粉, 必火, 爆款, 闭眼入, 闭眼用, 所有人都应该,
取代研究者, 取代专家, 绝了, 必看, 震惊

**虚假社会证明**（violation，除非 ledger 中存在可验证的
adoption_metric 证据）：已被广泛使用, 广泛使用, 获得大量学者认可,
风靡学术圈, 最近爆火, 爆火, 全网都在用, 众多顶刊作者推荐

**焦虑营销**（violation，默认禁止）：不会用就落后了, 再不用 AI
就晚了, 必须掌握, 不学就会被淘汰（按短语模式匹配，非逐词）

### 两级严重度（v0.2）

扫描器输出分两级：

- `violation` — 可发布内容中禁止；必须替换或由人类以可引用证据
  推翻。
- `context_review` — 扫描器无法判断语境的命中，需人扫一眼但可能
  完全合法。三种来源：(a) **否定语境**——命中词前出现否定标记
  （"本项目**不能保证**获得引用"是免责声明不是夸大）；(b) **引用
  提及**——命中词紧跟引号之后（"扫描器会标记'彻底解决'这类词"
  是在描述规则而非使用该词；引号也可能承载夸大，故降级而非忽略）；
  (c) 固有歧义词（裸"保证"，如"质量保证"）。

否定识别是单行启发式：不理解跨句范围、反讽和双重否定（"不是不
夸大"）。这是已知局限——context_review 项永远需要人看一眼，
gate 文件中列出但不强制替换。

### 平台身份透明检查（v0.2，人工判断，词表无法覆盖）

除词表扫描外，逐文件检查是否存在：伪装第三方口吻（"路过推荐"
"无意中发现的宝藏"）；虚构互动（"很多同学问我""后台收到大量
私信"，除非确有其事）；暗示不存在的热度。规则见
`references/academic-integrity.md` 第 9.1 节。命中同样按四段式
（位置/证据判断/保守替换/人类决定）写入 gate 文件。

"Keep original" is a legitimate outcome ONLY with a citable source
recorded in the manifest (e.g. a verifiable registered first, or a
dated adoption metric supplied by the user). The justification is
written by the human, not proposed by the AI.

## Decision block

```
GATE 3 DECISION
Reviewed by: <name>
Date: <date>
Result: approved | approved_with_changes | rejected
Hits overridden (kept) with justification:
- ...
```

The AI never fills the decision block itself.
