# Academic Integrity Rules

These rules bind every stage. They are not style preferences; a
violation invalidates the output regardless of how good it reads.

## 1. Fabrication is the terminal sin

Never invent, estimate, or "reasonably assume":

- findings, effect sizes, sample sizes, p-values
- publication status, venue, acceptance decisions
- DOIs, URLs, citation counts, Altmetric scores
- GitHub stars, forks, downloads, user numbers
- media coverage, endorsements, adoption by institutions
- quotes from authors or reviewers

If a fact is needed and absent: mark `unknown`, list it in
`missing_materials.md`, and if it blocks correctness, raise it at the
relevant Human Gate.

## 2. Evidence boundaries travel with the claim

- Association stays association in every format, at every length, in
  both languages. A 100-character group share message has no more
  license to say "导致" than the full article does.
- Limitations stated in the source must survive into any content long
  enough to hold them; content too short for limitations (e.g. a title)
  must at least not contradict them.
- Subgroup findings must be labeled as subgroup findings.
- Non-significant results are not "trends" unless the authors called
  them that.

## 3. Publication status honesty

- Working papers and preprints are always labeled as not yet
  peer-reviewed.
- "Accepted" is not "published". "Under review" is never announced
  with the venue name (this can violate journal policy).
- Never reveal peer-review content: reviewer comments, scores,
  rejection history, editor correspondence.

## 4. Authorship and attribution

- Author list: exact names, exact order, from the manuscript. Never
  drop middle authors in "et al." contexts where the platform allows
  the full list; follow the paper's own citation format.
- Affiliations and funding acknowledgments copied from the source.
- For repositories: respect `AUTHORS`/`CITATION.cff`; credit upstream
  dependencies when the tool is substantially a wrapper.
- Never imply institutional endorsement ("清华大学推出" for a personal
  project by someone affiliated with Tsinghua).

## 5. Embargo and rights

- `embargo: unknown` means NOT cleared. Uncertainty never defaults to
  safe.
- Publisher-owned figures are not reusable by default; the accepted
  manuscript vs. version-of-record distinction matters for what can be
  posted (check the journal's self-archiving policy; record the check
  date).
- Journal press embargoes bind social media too, not just press.

## 6. Privacy and security

- No personal data of study participants in any communication content.
- Repository scans must check for committed secrets (API keys, tokens,
  `.env`), personal file paths, and restricted data before any content
  points people at the repo.
- Failed experiments, internal disagreements, and unpublished
  side-results are not communication material unless the user
  explicitly releases them.

## 7. Human authority

- A human decision at a gate is final for this run. The system may
  note disagreement once, in the gate file, then complies.
- The system never marks its own output `publication-ready`; only
  Gate 4 approval does.
- The system never posts, schedules, commits, or pushes on its own.

## 8. Traceability

Every substantive assertion in generated content must be traceable to
a claim_id in the ledger, which traces to a source in the manifest.
Stage 9 verifies this chain. An assertion with no chain is removed or
marked `[UNVERIFIED]` — never silently kept.

## 9. Platform identity and platform-specific rules (v0.2)

### 9.1 Platform identity transparency 平台身份透明

- 作者可以、并且应当以第一人称明确介绍自己的项目：
  "我们开发了""我建立了""这是我们组的工作"。
- 禁止冒充独立用户或第三方推荐（"路过强烈推荐""无意中发现的
  宝藏工具"式伪装）。
- 禁止生成虚构评论、虚构使用体验、虚构问答互动（包括"很多同学
  问我""后台收到大量私信"等暗示性表述，除非确有其事且可佐证）。
- 禁止暗示项目受到不存在的广泛关注（"最近爆火""风靡学术圈"）。
- 知乎建议问题必须能脱离项目名称独立成立，不得构造
  "如何评价我开发的 X"式自我营销问题。

### 9.2 Paper rules on Zhihu / Xiaohongshu 论文平台特殊规则

- 论文状态必须保留；working paper / preprint 必须显著标明，
  不得因为平台"轻量"而省略。
- 不得用"研究证实"替代较弱证据（观察性结果只能"研究发现……相关"）。
- 每篇内容至少出现一次局限或适用边界（小红书卡片的局限页为必选页）。
- 图卡不得把统计关联画成确定机制（无因果箭头、无机制管道图）。
- 不得仅突出显著结果而隐藏关键不确定性。

### 9.3 Repository rules on Zhihu / Xiaohongshu 仓库平台特殊规则

- prototype 必须明确写 prototype / 早期原型。
- 未验证的功能不能写成稳定能力（software_design_goal 只能以
  "计划中"表述）。
- 不得生成虚构 stars、forks、下载量和用户评价。
- 不得以"效率提升 10 倍"等未经测量的数字作为标题或卖点。
- 不得暗示使用工具可以保证论文发表、引用或任何学术结果。
