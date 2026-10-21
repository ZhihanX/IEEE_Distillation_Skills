# IEEE 期刊论文蒸馏 Skill

目标：从高引 IEEE 期刊论文中蒸馏出写作用词、行文逻辑、画图思路、idea 提出方式和科研方法，
最终总结成一个 Claude skill（`skills/ieee-journal-writing/`）。

## 范围
- 第一批期刊：TWC、JSAC、TCOM（IEEE Transactions on Communications）。
- 选文门槛：Crossref 引用数 ≥ 50。Crossref 的数字比 Google Scholar 低，所以这个门槛比 Scholar 上的 50 更严。
- 排序用年均引用（`cites_per_year`），并按 2016–18 / 2019–21 / 2022–25 三个年份段分层，避免只学到老文章。
- 综述 / 教程（`is_survey=1`，或卡片里 `article_type` 不是 research）单独统计，不和研究论文混在一起归纳。
- 控制主题分布：任一主题（如 RIS）不超过每本期刊选文的约 25%。

## 流程
1. `pipeline/fetch_corpus.py` → `corpus/candidates.csv`（已完成，3582 篇候选）。
2. 取全文：
   - 本地会话：用用户 Chrome 里的 IEEE Xplore（机构登录）逐篇打开 `https://doi.org/<doi>` 读 HTML 全文。
   - 备选：`pipeline/match_arxiv.py` 找 arXiv 预印本（arXiv 要求 API 请求间隔 ≥ 3 秒）。
3. 每篇按 `pipeline/card_template.md` 写一张卡片到 `corpus/cards/`。
4. 汇总所有卡片，按维度统计频率（如“42/60 篇在引言末尾列贡献”），每条规律附 1–2 个短例句和来源 DOI。
5. 写 skill：`SKILL.md`（触发条件 + 工作流 + 索引）+ `references/`（structure、idea-framing、phrasebank、figures、methodology、ieee-conventions）。

## 规则
- 不提交 PDF 或全文（`data/` 已在 `.gitignore`）；卡片和 skill 里只放单句短引用（≤ 30 词）。
- 每条写作规律都要能追溯到卡片里的证据，不写没有统计支撑的主观建议。
- 卡片记录来源是 IEEE 正式版还是 arXiv 预印本，两者措辞可能不同。
