---
doi: 10.1109/tcomm.2020.2987311
title: "Scalable Cell-Free Massive MIMO Systems"
journal: TCOM
year: 2020
band: 2019-2021
cites: 965
cites_per_year: 154.2
article_type: research
topic: cell-free-massive-MIMO
source: xplore-html
xplore: 9064545
auto:
  words_total: 8739
  n_sections: 7
  n_subsections: 21
  n_figures: 6
  n_tables: 2
  n_display_eq: 46
  n_algorithms: 0
  statements: {theorem: 0, lemma: 1, proposition: 4, corollary: 3, definition: 1, assumption: 1, remark: 3, proof: 6, proof_in_appendix: 1}
  n_appendix: 1
  mean_sentence_words: 25.8
  we_per_1k: 9.8
  title_words: 5
  abstract_words: 192
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 6, contribList: 0, roadmap: 2, however: 6, transition: 3, resultsShow: 0, motivatedBy: 5, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 1, outperform: 4, intensifier: 2, worthNoting: 0, observe: 0, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 4, promising: 0, gen: 1, contrast: 1, firstTime: 0, novel: 3, weProposeFirst: 5, wlog: 1, code: 1, prototype: 0}
  methods: {complexity: 17, monteCarlo: 2}
code:
  title_pattern: [noun-phrase]
  abstract_moves: [context, context, context, gap, aim, method, method, theory, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 9
  intro_moves: [tech, prior, prior, gap, gap, contrib, roadmap, reproducibility, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 5
  contrib_verbs: [prove, develop, derive, prove, demonstrate]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [scalability, practicality]
  motivating_figure: true
  problem_class: analysis-only
  solution: [closed-form, heuristic]
  theory_role: central
  proofs_location: mixed
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [CDF]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: true
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Scalable [已有系统]"，5 词，本批最短。一个形容词就是全部贡献：把已有概念做成"可扩展"的版本。

## 2. 摘要（9 句，192 词）
- 开头用祈使句把读者带进场景："Imagine a coverage area with many wireless access points that cooperate to jointly serve the users, instead of creating autonomous cells."
- 第 3 句交代概念的来龙去脉（以前叫 Network MIMO，现在叫 Cell-Free Massive MIMO）。
- 第 4 句给出核心挑战："The main challenge is to achieve the benefits of cell-free operation in a practically feasible way, with computational complexity and fronthaul requirements that are scalable …"
- "We propose … / We provide … / Moreover, we adapt … / A new uplink and downlink duality is proved …"
- 结尾 "Interestingly, the proposed scalable precoding and combining outperform … and also performs closely to the best unscalable alternatives."（用 Interestingly 强调"几乎不损失性能"）。

## 3. 引言逻辑（3 段 + A 小节 2 段 + B 动机与贡献 + C 组织 / 可复现 / 记号）
1. 原理：相干发送提升接收功率 → 从同址阵列推广到多 AP → Network MIMO。
2–3. 历史：早期 Network MIMO 的不现实假设 → 不重叠协作簇（4G 收益小，边缘用户干扰）→ 以用户为中心的 DCC → 被同期出现的 Massive MIMO 抢了风头。
4. 空白（措辞直接）："The key novelty is the SE analysis that features imperfect CSI, but conceptually, it is a special case of Network MIMO …" → "Hence, the original form of Cell-Free Massive MIMO was unscalable." → 列出已有工作缺的三件事（"without …, without …, and without …"）→ "This is all done in this paper."
5. 划定范围：功率控制的可扩展性"is not the focus of this paper"。
6. B. 动机与贡献（散文）："The main motivation of this paper is to define and design scalable Cell-Free Massive MIMO systems."
7. 路线图；8. Reproducible Research（GitHub 链接）；9. Notation。

## 4. Idea 是怎么提出的
- 空白类型：可扩展性 + 实用性。核心洞见是"新瓶装旧酒"的反向利用：证明 Cell-Free Massive MIMO 是 Network MIMO 中 DCC 框架的特例，从而把旧文献里的可扩展机制搬过来。
- 先给"可扩展"下形式化定义（Definition 1 (Scalability)：每个 AP 的复杂度与资源在 K→∞ 时有限），再证明原始方案不满足、新方案满足——"先定义标准再证明达标"。
- 首创句放在方法章节开头："We will now propose the first scalable implementation of Cell-Free Massive MIMO."

## 5. 科研方法
- 第 III 节先回顾原始方案并按四项任务（信道估计、数据处理、前传、功控）指出不可扩展。
- 第 IV 节 DCC 框架，Lemma 1 给出可扩展的充分条件。
- 第 V 节：联合接入 / 导频分配 / 成簇算法（三步，图示 Fig. 3）；集中式与分布式两种实现的上 / 下行 SE 表达式（Proposition 1–3）；新的上下行对偶（Proposition 4）用于由合并向量设计预编码；P-MMSE、LP-MMSE 两种可扩展处理。
- 用两张表比较前传信令量和复杂度。

## 6. 仿真与实验
- 只有 2 张结果图（UL / DL 的 SE CDF），篇幅很短；用 wrap-around 近似无限大网络。
- baseline：全 AP 服务的 MMSE、L-MMSE、原始 MR。
- 结论句："the proposed way to make Cell-Free Massive MIMO scalable leads to a negligible loss in performance"。

## 7. 图表
- 6 图 2 表。Fig. 1 网络示意，Fig. 2 动态协作簇示意，Fig. 3 接入流程三步图，Fig. 4 解释现象的 PDF 示意。caption 简短。

## 8. 句式库
- 场景开头："Imagine a coverage area with many wireless access points that cooperate to jointly serve the users, instead of creating autonomous cells."
- 直接批评："In fact, it has been a step backwards in terms of implementation feasibility."
- 列缺失："… but without making the connection to DCC, without analyzing how to …, and without discussing how … This is all done in this paper."
- 划定范围："… but a numerical evaluation of power control schemes is not the focus of this paper."
- 可复现声明："All the simulation results can be reproduced using the Matlab code and data files available at: …"

## 9. 结论
- 2 段：第 1 段过去时总结 + 解释为何几乎无损（"The reason is that each UE receives most of its power from a small subset of the APs, …"）；第 2 段坦白未深入的部分（功率分配）作为开放问题。
