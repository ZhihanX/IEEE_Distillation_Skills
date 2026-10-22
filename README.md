# IEEE Distillation Skills

从高引 IEEE 期刊论文（Crossref 引用 ≥ 50）中蒸馏写作用词、逻辑结构、画图思路、idea 提出方式与科研方法，
总结成 Claude skill。第一批期刊：TWC、JSAC、TCOM。

## 目录
- `pipeline/fetch_corpus.py`：从 Crossref 按期刊、年份、引用数筛选候选论文
- `pipeline/select_papers.py`：按年份段分层、控制主题比例，从候选中选出要精读的论文
- `pipeline/match_arxiv.py`：为候选论文匹配 arXiv 预印本（全文备选来源）
- `pipeline/resolve_xplore.py`：把 DOI 解析成 IEEE Xplore 文档号
- `pipeline/xplore_extract.js`：在 Xplore 全文页里运行的只读提取脚本（结构统计 + 关键段落）
- `pipeline/card_template.md`：单篇论文的蒸馏卡片模板（YAML 编码 + 中文笔记）
- `pipeline/aggregate_cards.py`：汇总卡片，生成频率统计 `corpus/summary.md`
- `corpus/candidates.csv`：候选论文列表（DOI、年份、引用数、年均引用、是否综述）
- `corpus/selected.csv`：精读名单（78 篇：72 篇研究论文 + 6 篇综述 / 教程）
- `corpus/selection_changes.csv`：精读时的名单调整（研究名额里混入的综述改记为 overview，并按同刊同年份段顺延补位）
- `corpus/cards/`：每篇论文的蒸馏卡片（80 张：72 篇研究论文 + 8 篇综述 / 教程）
- `corpus/summary.md`、`corpus/summary.json`：卡片汇总的频率统计
- `skills/ieee-journal-writing/`：最终的 skill（`SKILL.md` + `references/` 下 6 个专题文件）

### 语义通信 / JSCC 子语料（第二轮蒸馏）
- `pipeline/fetch_semcom.py`：从 Crossref 取语义通信 / JSCC 候选（TWC、JSAC、TCOM、TCCN、TSP、JSAIT，2018–2025，引用 ≥ 10）
- `pipeline/semcom_card_template.md`：语义通信卡片的附加字段（`semcom:` 块）与第 10 节"Idea 拆解"
- `pipeline/aggregate_semcom.py`：汇总语义通信卡片 → `corpus/semcom/summary.md` / `summary.json`，并生成 skill 的 `open-problems.md`
- `pipeline/landscape_semcom.py`：234 篇候选的标题标签 → `corpus/semcom/landscape.csv` / `landscape.md`，并生成 skill 的 `landscape.md`
- `corpus/semcom/candidates.csv`：234 篇候选；`corpus/semcom/selected.csv`：按 7 条研究线选出的 39 篇
- `corpus/semcom/cards/`：34 张新卡片；另有 5 篇已在主语料，直接在 `corpus/cards/` 的原卡片里补了 `semcom:` 块和第 10 节
- `skills/semantic-comm-ideas/`：语义通信 / JSCC 选题 skill——生成 idea 与检查 idea（`SKILL.md` + `references/` 下 6 个文件）

## 使用 skill
把 `skills/ieee-journal-writing/` 和 `skills/semantic-comm-ideas/` 复制到 `~/.claude/skills/`（或项目的 `.claude/skills/`）即可。
两个 skill 可单独使用：`semantic-comm-ideas` 负责选题与评估，`ieee-journal-writing` 负责写成论文。

## 汇总卡片
```bash
python3 pipeline/aggregate_cards.py
python3 pipeline/aggregate_semcom.py
python3 pipeline/landscape_semcom.py
```

## 重新生成候选列表
```bash
python3 pipeline/fetch_corpus.py --journals TWC,JSAC,TCOM --min-cites 50
```
