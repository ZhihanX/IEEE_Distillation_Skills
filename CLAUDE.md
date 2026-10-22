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
2. 选文：`pipeline/select_papers.py` → `corpus/selected.csv`（每刊每年份段 8 篇研究论文 + 每刊 3 篇综述；
   主题按标题正则归类，单主题不超过配额的 25%；标题像综述但混进研究名额的，读的时候改记为 overview 并顺延补一篇，
   记录在 `corpus/selection_changes.csv`）。
3. 取全文：
   - 主来源：IEEE Xplore HTML 全文（内置浏览器，机构登录）。`pipeline/resolve_xplore.py` 把 DOI 解析成 arnumber
     （`corpus/xplore_ids.csv`）；逐篇 `navigate` 到 `https://ieeexplore.ieee.org/document/<arnumber>/`，
     再把 `pipeline/xplore_extract.js` 的内容原样交给 javascript_tool 执行。脚本只读 DOM、返回 JSON（结构统计、
     引言 / 结论全文、其他节首句、图表 caption、定理类陈述、句式与方法计数），不存储、不外发。
   - 每次都用完整 `navigate`（站内跳转不会重新加载正文）；按正常阅读节奏一篇一篇来，不要批量抓取。
   - Xplore 不可用时等一会儿再试；备选是 `pipeline/match_arxiv.py` 匹配到的 arXiv 预印本（`corpus/arxiv_matches.jsonl`，
     arXiv 要求请求间隔 ≥ 3 秒），卡片里 `source` 记为 `arxiv-v<N>`。
4. 每篇按 `pipeline/card_template.md` 写一张卡片到 `corpus/cards/<JOURNAL>_<doi 后缀>.md`：
   YAML 头（`auto:` 抄提取器输出，`code:` 用模板里的受控词表人工编码）+ 中文正文 1–9 节。
5. `python3 pipeline/aggregate_cards.py` → `corpus/summary.md` / `summary.json`：按期刊、年份段统计每个编码值的
   “k/n”和数值的中位数 [四分位距]；写 skill 时每条规律引用这里的频率，并从卡片里挑 1–2 个短例句和 DOI。
6. 写 skill：`SKILL.md`（触发条件 + 工作流 + 索引）+ `references/`（structure、idea-framing、phrasebank、figures、methodology、ieee-conventions）。
   skill 里每条英文例句后面都标 DOI 后缀，且必须能在该 DOI 的卡片里找到原句（卡片里没有的，先把原句补进该卡第 8 节）；
   频率一律引用 `corpus/summary.md` 或从卡片 YAML 现算，卡片笔记的关键词计数只能写成 "≥k/72"。

## 第二轮：语义通信 / JSCC 子语料（skill `semantic-comm-ideas`）
1. `pipeline/fetch_semcom.py` → `corpus/semcom/candidates.csv`（TWC、JSAC、TCOM、TCCN、TSP、JSAIT，2018–2025，引用 ≥ 10，
   标题匹配语义通信 / JSCC / 任务导向，234 篇）。
2. 选文：`corpus/semcom/selected.csv`，按 7 条研究线（image-jscc、digital、generative、modality、task-multiuser、networking、
   theory-security）各取年均引用高的论文，另加 2 篇综述，共 39 篇；`has_main_card = 1` 的 5 篇已在主语料。
3. 取全文同上（Xplore + `xplore_extract.js`，提取器已加入领域词典 `domain` 和开放问题句 `open`）。
4. 卡片：通用部分按 `pipeline/card_template.md`，再加 `pipeline/semcom_card_template.md` 的 `semcom:` 块和第 10 节"Idea 拆解"。
   新卡片存 `corpus/semcom/cards/`；已有主卡片的论文直接在原卡片里补。第 10 节的开放问题分"原文"（≤ 30 词原句）和"推断"（标明）。
   受控词表外的取值允许，但要在 `aggregate_semcom.py` 的 `ALIAS` 里归并近义写法。
5. `python3 pipeline/aggregate_semcom.py` → `corpus/semcom/summary.md` / `summary.json`（字段频率、评测完整性、增量类型、
   继承关系、开放问题按主题、弱点主题、写作字段），同时生成 `skills/semantic-comm-ideas/references/open-problems.md`。
6. `python3 pipeline/landscape_semcom.py` → `corpus/semcom/landscape.csv` / `landscape.md`（标题标签、模态 × 主题占位表），
   同时生成 `skills/semantic-comm-ideas/references/landscape.md`。标签只看标题，空格不等于没人做过。
7. skill 的频率写成 "k/37"（37 篇研究论文），关键词计数写成 "≥k/37"；英文例句规则同上（DOI 后缀、能在卡片里找到原句、≤ 30 词）。
   改卡片后重跑第 5、6 步，再检查 skill 里引用的数字是否变化。

## 规则
- 不提交 PDF 或全文（`data/` 已在 `.gitignore`）；卡片和 skill 里只放单句短引用（≤ 30 词）。
- 每条写作规律都要能追溯到卡片里的证据，不写没有统计支撑的主观建议。
- 卡片记录来源是 IEEE 正式版还是 arXiv 预印本，两者措辞可能不同。
