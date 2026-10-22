---
doi: 10.1109/jsac.2017.2725519
title: "A Survey on Non-Orthogonal Multiple Access for 5G Networks: Research Challenges and Future Trends"
journal: JSAC
year: 2017
band: 2016-2018
cites: 2264
cites_per_year: 251.3
article_type: overview      # JSAC 专刊综述（引言末："including the papers published in this JSAC special issue"）
topic: NOMA-RSMA-access
source: xplore-html
xplore: 7973146
auto:
  words_total: 7861
  n_sections: 9
  n_subsections: 17
  n_figures: 6
  n_tables: 0
  n_display_eq: 14
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, example: 4, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 25.2
  we_per_1k: 1.1
  title_words: 14
  abstract_words: 123
  abstract_sentences: 6
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [context, context, context, aim, aim, aim]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb    # "This survey provides an overview of …"
  intro_paragraphs: 5
  intro_moves: [field, tech, prior, tech, roadmap]
  related_work: none
  contrib_format: none
  contrib_n: 0
  contrib_verbs: []
  contrib_quantified: false
  first_claim: false
  roadmap: true                       # "The goal of this survey is … Sections II and III …"（提取器 roadmap 未匹配）
  notation: none
  gap_type: [unification]
  motivating_figure: false
  problem_class: none
  solution: []
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 0
  baseline_naming: none
  x_axes: []
  fig1_role: scenario
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false       # 未来方向单列为第 VIII 节，结论段本身不提
---

> 本卡只做结构与写法层面的记录（overview 不参与研究论文的统计）；只抽取了摘要、引言、章节结构与图注。

## 1. 标题
- "A Survey on [技术] for [代际]: Research Challenges and Future Trends"，14 词。标题首词直接是 "A Survey on"，副标题点明"挑战与趋势"。

## 2. 摘要（6 句，123 词，偏短）
- 3 句技术定义（NOMA 对 5G 的作用、核心思想、"several recently proposed 5G multiple access schemes can be viewed as special cases"）→ "This survey provides an overview of …" → 把专刊论文放进已有文献脉络 → 未来挑战。

## 3. 引言（5 段，约 780 词）
1. NOMA 是 5G 接入设计原则 → 列出各种方案（功率域、SCMA、PDMA、LDS、LPMA、IDMA），归纳共同概念。
2. "Unlike NOMA, conventional orthogonal multiple access (OMA) techniques, … serve a single user in each orthogonal resource block." → 用一个"信道差的高优先级用户"的简单例子说明 OMA 的频谱低效。
3. 相关概念早已存在于信息论（叠加编码、SIC、MPA）→ 与 CDMA 的哲学差异。
4. 兼容性与标准化（LTE-A 的 MUST、ATSC 3.0 的 LDM）。
5. "The goal of this survey is to provide a comprehensive overview of the latest NOMA research results and innovations, including the papers published in this JSAC special issue." + 节导览。

## 4. 章节组织
- 单载波 NOMA（功率域、CR-NOMA）→ 多载波 NOMA（混合 NOMA、LDS/SCMA/PDMA）→ MIMO-NOMA → 协作 NOMA → mmWave NOMA → 实现问题（编码调制、非理想 CSI、跨层资源分配）→ 未来研究挑战（SWIPT、认知无线电、安全、其他 5G 场景、5G 之后）→ 结论。
- 用 4 个 "Example" 环境（带简单推导的数值例子）解释原理——综述中的"教学式例子"。

## 5. 图表
- 6 图 0 表，全部为原理示意（两用户下行、SCMA 因子图、准退化、协作 NOMA 两种形式、mmWave 随机波束、LPMA）。caption 一句话描述。

## 6. 对 skill 的意义
- 专刊综述（guest editorial 性质）结构紧凑：摘要很短、无贡献列表、无相关工作节；按"技术变体 → 与其他技术结合 → 实现 → 未来"组织；结论 1 段，以 "we hope that this survey and the papers in this special issue will be useful …" 收尾。
- we 密度极低（1.1/千词），几乎全用第三人称陈述。
