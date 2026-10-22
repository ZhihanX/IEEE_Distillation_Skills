---
doi: 10.1109/tcomm.2022.3171800
title: "Terahertz Band Communication: An Old Problem Revisited and Research Directions for the Next Decade"
journal: TCOM
year: 2022
band: 2022-2025
cites: 681
cites_per_year: 156.9
article_type: overview      # 回顾型综述（作者团队 2014 年路线图的十年回顾 + 下一个十年的方向）
topic: mmWave-THz
source: xplore-html
xplore: 9766110
auto:
  words_total: 14269
  n_sections: 9
  n_subsections: 36
  n_figures: 11
  n_tables: 6
  n_display_eq: 0
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 24.1
  we_per_1k: 6.2
  title_words: 14
  abstract_words: 189
  abstract_sentences: 8
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [context, context, prior, context, context, aim, aim, implication]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb    # "With this paper, our aim is looking back to the last decade …"
  intro_paragraphs: 6
  intro_moves: [field, tech, tech, field, prior, aim]
  related_work: table                 # 单列 "Related Work"（268 词）+ Table I 相关教程 / 综述 / 杂志文章
  contrib_format: bullets
  contrib_n: 0
  contrib_verbs: []
  contrib_quantified: false
  first_claim: false
  roadmap: true                       # 另有 Fig. 5 "The structure of this paper"
  notation: none
  gap_type: [unification]
  motivating_figure: true
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
  fig1_role: framework                # "Performance objectives for 6G."
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

> 本卡只做结构与写法层面的记录（overview 不参与研究论文的统计）；只抽取了摘要、引言、章节结构与图注。

## 1. 标题
- "[领域]: An Old Problem Revisited and Research Directions for the Next Decade"，14 词。副标题点出"回顾 + 展望"的时间框架。

## 2. 摘要（8 句，189 词）
- 两句定位（6G 关键技术）→ 作者自述历史："In 2014, our team published two comprehensive roadmaps for the development and progress of THz communication networks, …" → 领域升温 → "With this paper, our aim is looking back to the last decade and revisiting the old problems …" → 开放挑战与方向（从器件到测试平台）→ 愿景句。

## 3. 引言（6 段，约 1030 词）
- THz（0.1–10 THz）定义与需求 → mmWave 已入 5G 但难达 Tbps → THz 的带宽优势与新应用（Fig. 2–4：Tera-WiFi、纳米尺度片上通信、ISAC）→ FCC 2019 年开放实验牌照 → 作者团队 2014 年路线图的影响 → 全文主线："the grand challenge in THz communications: the limited communication distance …"（器件物理 + 信道物理），并以 bullet 列出主要贡献（逐节对应）。

## 4. 章节组织
- 相关工作（Table I）→ 器件技术（电子 / 光子 / 等离激元三条路径、智能天线、数字后端）→ 信道测量与建模（三种测量方法、确定性 / 统计建模、链路预算表）→ PHY 功能（调制编码、动态混合波束、波束估计与跟踪、同步、定位、安全）→ 高层协议（MAC、干扰与覆盖、多跳、路由调度）→ 实验与仿真平台（测试床汇总表）→ 政策与标准化 → 结论。
- 多数技术节末尾有 "Open Challenges" 小节。

## 5. 图表
- 11 图 6 表，0 个公式。图以应用愿景、技术路径、收发机架构、测量方法、THz 路损窗口为主；表为汇总性质（相关综述、天线系统性质、测量技术、信道特征及其影响、链路预算、测试床）。Fig. 5 为论文结构图。

## 6. 对 skill 的意义
- 团队回顾型综述可以用自己的早期路线图作为叙事起点（"In 2014, we published …"），以"十年前的问题现在解决到哪"组织全文；用一个贯穿全文的"grand challenge"统一各章。
- 结论第 2 段用 "with the following take-away lessons. First, … " 的编号式教训总结。
