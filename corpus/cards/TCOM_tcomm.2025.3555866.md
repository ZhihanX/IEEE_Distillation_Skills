---
doi: 10.1109/tcomm.2025.3555866
title: "Flexible-Antenna Systems: A Pinching-Antenna Perspective"
journal: TCOM
year: 2025
band: 2022-2025
cites: 292
cites_per_year: 289.6
article_type: research
topic: movable-fluid-antenna
source: xplore-html
xplore: 10945421
auto:
  words_total: 8288
  n_sections: 6
  n_subsections: 17
  n_figures: 15
  n_tables: 1
  n_display_eq: 60
  n_algorithms: 1
  statements: {theorem: 0, lemma: 3, proposition: 0, corollary: 1, remark: 8, proof: 1, proof_in_appendix: 1}
  n_appendix: 1
  mean_sentence_words: 27.3
  we_per_1k: 3.9
  title_words: 5
  abstract_words: 208
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 1, contribList: 1, roadmap: 0, however: 8, transition: 8, resultsShow: 3, motivatedBy: 1, toAddress: 0, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 3, outperform: 1, intensifier: 5, worthNoting: 1, observe: 0, thisIsBecause: 0, asExpected: 0, insight: 2, tradeoff: 0, figVerb: 7, promising: 0, gen: 0, contrast: 4, firstTime: 0, novel: 0, weProposeFirst: 0, wlog: 3, code: 0, prototype: 0}
  methods: {complexity: 9}
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [context, aim, theory, context, theory, method, theory, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 4
  intro_moves: [field, gap, solution, contrib]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [develop, study, investigate, investigate]
  contrib_quantified: false
  first_claim: false
  roadmap: false
  notation: none
  gap_type: [limitation, new-architecture]
  motivating_figure: true
  problem_class: analysis-only
  solution: [closed-form, exhaustive-search]
  theory_role: central
  proofs_location: mixed
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [area-size, number-of-antennas, transmit-power, propagation-loss]
  fig1_role: architecture
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[大类]: A [新技术] Perspective"，5 词。用 "Perspective" 但正文是完整的分析 + 设计研究论文——标题词不能用来判断文章类型。

## 2. 摘要（8 句，208 词）
- "This paper focuses on a new type of flexible-antenna technology, termed pinching antennas, which can be realized by …"（"termed X" 引出新术语）。
- 正文三个场景（单天线单波导 → 多天线单波导 → 多天线多波导）在摘要里按 first / Finally 依次各一到两句。
- 第 4 句把一个器件特性变成研究动机："An advantageous feature … is that multiple pinching antennas can be activated on a single waveguide at no extra cost; however, they must be fed with the same signal." → 下一句 "This feature motivates the application of NOMA"。
- 被动语态为主（we 密度 3.9/千词，本批最低）。

## 3. 引言逻辑（4 段，约 560 词，很短）
1. 用香农公式统一框架：MIMO 调 W、NOMA 调 W 和 Ps、噪声调制调 Pn，可重构天线调 γh——"Many recently developed communication techniques can be motivated by using the Shannon capacity formula"。
2. 已有可重构天线（RIS、流体 / 可移动天线）的共同局限：对抗大尺度路损能力有限、昂贵。
3. "The aforementioned issues motivate the study of pinching antennas in this paper." → DOCOMO 2022 演示 → bullet 列出两大特性。
4. "The aim of this paper is two-fold." → 4 条贡献，每条都很长（含结论和理由）。
- 无路线图、无记号段。

## 4. Idea 是怎么提出的
- 空白类型：已有方案局限（只能移动几个波长，对路损无效）+ 新架构（工业界演示过的新硬件）。
- 写法亮点：
  - 用香农公式把一整类技术放进同一张"参数表"，新技术的位置一目了然——适合"新器件 / 新维度"论文的开篇；
  - 从器件约束（同一波导上的天线只能发同一信号）自然推出要用 NOMA——"约束 → 方案"的推导式动机。

## 5. 科研方法
- 每个场景先给常规天线的基准分析，再给夹持天线的闭式遍历速率（Lemma 1、Corollary 1 高 SNR 近似、Lemma 2 优劣比较、Lemma 3 NOMA）。
- 多波导场景转化为两用户 MISO 干扰信道，证明上界可达的两个条件（相位匹配、正交），给出特殊情形和基于搜索的位置算法。
- 8 个 Remark：解释物理原因、交代 LoS 假设（"a user's LoS path can be 20 dB stronger than its non-line-of-sight (NLoS) paths"）、讨论实现方式。

## 6. 仿真与实验
- 三个小节对应三个场景，第四小节专门讨论硬件损伤（波导传播损耗 0.08 dB/m、发射功率损耗）。
- 结果写法会坦白代价："However, we note that this sum rate increase is at the price of the weak users' data rates."

## 7. 图表
- 15 图 1 表。Fig. 1 概念图（引用自他人），Fig. 2–4 三个场景的示意图——每种场景一张示意图。
- caption 很长，交代用户分布、坐标和理论曲线来源（"The analytical results are based on …"），不写结论。

## 8. 句式库
- 统一框架："Many recently developed communication techniques can be motivated by using the Shannon capacity formula [2]."
- 共同局限："We note that for most existing flexible-antenna systems, their capabilities to combat large-scale path loss are limited."
- 引出本文："The aforementioned issues motivate the study of pinching antennas in this paper."
- 目标："The aim of this paper is two-fold. One is to …, and the other is to …"
- 约束→方案："This observation means that a signal sent through the waveguide has to be a superimposed mixture of the signals of the multiple users …, which motivates the use of NOMA."
- 坦白代价："However, we note that this sum rate increase is at the price of the weak users' data rates."

## 9. 结论
- 2 段：第 1 段按三个场景复述（现在完成时 + 过去时）；第 2 段先承认局限（只做了 M=N=K=2、算法基于搜索），再给三个具体方向（一般 MISO、低复杂度位置优化、与其他可重构天线共存）。
