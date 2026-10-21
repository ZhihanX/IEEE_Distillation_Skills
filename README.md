# IEEE Distillation Skills

从高引 IEEE 期刊论文（Crossref 引用 ≥ 50）中蒸馏写作用词、逻辑结构、画图思路、idea 提出方式与科研方法，
总结成 Claude skill。第一批期刊：TWC、JSAC、TCOM。

## 目录
- `pipeline/fetch_corpus.py`：从 Crossref 按期刊、年份、引用数筛选候选论文
- `pipeline/match_arxiv.py`：为候选论文匹配 arXiv 预印本（全文备选来源）
- `pipeline/card_template.md`：单篇论文的蒸馏卡片模板
- `corpus/candidates.csv`：候选论文列表（DOI、年份、引用数、年均引用、是否综述）
- `corpus/cards/`：每篇论文的蒸馏卡片（待生成）
- `skills/ieee-journal-writing/`：最终的 skill（待生成）

## 重新生成候选列表
```bash
python3 pipeline/fetch_corpus.py --journals TWC,JSAC,TCOM --min-cites 50
```
