---
doi: 10.1109/twc.2022.3158894
title: "Beam Focusing for Near-Field Multiuser MIMO Communications"
journal: TWC
year: 2022
band: 2022-2025
cites: 548
cites_per_year: 133.9
article_type: research
topic: near-field
source: xplore-html
xplore: 9738442
auto:
  words_total: 8736
  n_sections: 5
  n_subsections: 19
  n_figures: 10
  n_tables: 0
  n_display_eq: 37
  n_algorithms: 3
  statements: {theorem: 2, lemma: 2, proposition: 0, corollary: 0, proof: 3, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 27.5
  we_per_1k: 14.4
  title_words: 7
  abstract_words: 217
  abstract_sentences: 9
  phrases: {toTheBest: 1, inThisPaper: 3, contribList: 0, roadmap: 2, however: 7, transition: 9, resultsShow: 3, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 8, npHard: 0, closedForm: 2, outperform: 0, intensifier: 1, worthNoting: 0, observe: 7, thisIsBecause: 4, asExpected: 0, insight: 3, tradeoff: 0, figVerb: 6, promising: 0, gen: 2, contrast: 0, firstTime: 1, novel: 0, weProposeFirst: 1, wlog: 0, code: 0, prototype: 0}
  methods: {AO: 3, manifold: 3, convergence: 2, BCD: 1, bisection: 1, convexOpt: 1, lagrange: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, context, aim, method, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, tech, prior, gap, tech, gap, aim, approach, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 4
  contrib_verbs: [formulate, study, derive, show]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, practicality]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [WMMSE, manifold, AO, closed-form, relaxation]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 1
  baseline_naming: descriptive
  x_axes: [user-position, antenna-length, signal-power-map, number-of-users]
  fig1_role: result     # Fig. 1 是近场边界随频率与口径变化的曲线图，Fig. 2 才是波束聚焦 vs 波束控制的概念图
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[技术] for [场景] Multiuser MIMO Communications"，7 词。"Beam Focusing" 本身就是相对 "beam steering" 的新概念，标题只需点出它和近场多用户场景。

## 2. 摘要（9 句，217 词）
- 前两句推理链：大阵列 + 高频 → 设备常处于近场（Fresnel）区域。
- "In this paper, we study the potential of beam focusing, feasible in near-field operation, in facilitating high-rate multi-user downlink MIMO systems."
- 因为聚焦能力取决于天线结构 → 研究三种架构（全数字、移相器混合、动态超表面天线 DMA）→ 建模 → 和速率问题 → 各架构的解法。
- 末句点出新自由度："… provide a new degree of freedom to mitigate interference in both angle and distance domains, which is not achievable using conventional far-field beam steering, …"

## 3. 引言逻辑（8 段，约 1380 词）
1. mmWave/THz → 大阵列 → 近场距离可达数十米 → 平面波假设失效 → 球面波 → 波束可聚焦到"位置"而非仅"方向" → 同一角度的用户也可区分。
2. 近场聚焦主要见于天线理论文献 → 通信视角的工作很少（点对点、LIS 单用户 / 两用户、RIS）→ "Nonetheless, the potential of near-field focusing in facilitating massive MIMO downlink communications with practical antenna technologies has not been thoroughly studied to date."
3. 聚焦能力依赖架构：全数字（灵活但贵）→ "However, …, the implementation of a fully-digital architecture becomes extremely challenging due to its increased cost and power consumption." → 混合架构 → DMA（已有 DMA 工作只考虑远场）→ 架构差异构成研究动机。
4. "In this paper we study …" + 首创声明（"this work represents the first study on the design of focused beams … as means of optimizing multi-user communication objectives"）。
5. 方法路线：先全数字（最灵活，作为基准）→ 混合（借用 RIS 的流形优化）→ DMA（洛伦兹约束，无法照搬远场方法，需专门算法；先单用户再多用户）。
6. 结果预告 + 预先回应"是否只是搬用远场算法"："While parts of our technical derivations build upon design algorithms proposed for far-field communications, we demonstrate that the incorporation of the near-field characteristics results in fundamentally different beam patterns …"
7. 路线图；8. 记号段（无 "Notation" 小标题）。

## 4. Idea 是怎么提出的
- 空白类型：新场景（近场多用户下行）+ 实用性（考虑实际天线架构，尤其 DMA）。
- 写法亮点：用"能力依赖于硬件"把三种架构自然纳入同一研究；贡献按"由易到难"的架构顺序展开（全数字 → 混合 → DMA），后者以前者为基准。
- 核心卖点在摘要、引言、结果三处重复："区分同一角度、不同距离的用户"——这是远场波束控制做不到的。

## 5. 科研方法
- 模型：Fraunhofer 距离定义近场 → 球面波信道向量 a_m → 三种架构的信号模型（DMA：微带线上的超材料元件，洛伦兹形响应）→ 和速率最大化 (14)，可行集随架构不同；"While the formulation of (14) does not explicitly account for the fact that transmission takes place in the near-field, this property is embedded in the equivalent channel vectors."
- 全数字：Lemma 1（和速率 ↔ 加权 MMSE）→ 交替更新（Algorithm 1）。
- 混合：Lemma 2 给定模拟部分下的数字预编码；模拟部分单模约束 → 黎曼流形共轭梯度（Algorithm 2）。
- DMA：单用户 Theorem 1 闭式最优相位（含近场聚焦项与微带传播补偿项两部分的物理解释），再投影到洛伦兹约束（Fig. 5 图示）；多用户 Theorem 2 等价重写 + 交替优化。
- "Discussion" 小节讨论目标函数选择、架构比较与频率响应假设。证明在附录。

## 6. 仿真与实验
- 28 GHz；公平比较："To make a fair comparison, We consider that the three different types of antennas have the same physical aperture …"
- 单用户：沿 z 轴的速率（聚焦 vs 波束控制）、速率 vs 天线长度。
- 多用户：两用户同方向不同距离（近场 / 远场两种情形对照）→ xz 平面信号功率热图（直观展示"按距离区分用户"）→ 和速率 vs 用户数。

## 7. 图表
- 10 图 0 表 3 算法。Fig. 1 近场边界曲线（不同频率与口径），Fig. 2 三联概念图（三维示意 / 远场波束控制导致同向用户干扰 / 近场聚焦干扰小），Fig. 3 三种架构，Fig. 4 微带线物理与数学模型，Fig. 5 洛伦兹权重映射。结果图 caption 短标签。

## 8. 句式库
- 推理链引出近场："A byproduct of utilizing large-scale antennas is that high-frequency communication may take place in the near-field (Fresnel) region, as opposed to conventional wireless systems, …"
- 新能力："… it brings forth the possibility to generate radiation patterns which focus the beam (beam focusing) at a specific location, in contrast to only a specific direction as in far-field conditions …"
- 从理论到通信的空白："While antenna theory provides tools to achieve beam focusing, how to exploit this ability to facilitate near-field wireless communications is still in its infancy, …"
- 未充分研究："Nonetheless, the potential of near-field focusing in facilitating massive MIMO downlink communications with practical antenna technologies has not been thoroughly studied to date."
- 预先回应增量质疑："While parts of our technical derivations build upon design algorithms proposed for far-field communications, we demonstrate that the incorporation of the near-field characteristics results in fundamentally different beam patterns …"
- 公平比较："To make a fair comparison, we consider that the three different types of antennas have the same physical aperture …"

## 9. 结论
- 1 段 179 词，过去时复述 → 结果分架构给出对比（单用户 DMA 聚焦最好，多用户混合架构更优）。无数字、无未来工作。
