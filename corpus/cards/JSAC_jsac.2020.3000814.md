---
doi: 10.1109/jsac.2020.3000814
title: "Capacity Characterization for Intelligent Reflecting Surface Aided MIMO Communication"
journal: JSAC
year: 2020
band: 2019-2021
cites: 795
cites_per_year: 128.7
article_type: research
topic: RIS
source: xplore-html
xplore: 9110912
auto:
  words_total: 9349
  n_sections: 6
  n_subsections: 14
  n_figures: 7
  n_tables: 2
  n_display_eq: 32
  n_algorithms: 2
  statements: {theorem: 0, lemma: 3, proposition: 4, corollary: 0, proof: 6, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 33.5
  we_per_1k: 10.9
  title_words: 9
  abstract_words: 242
  abstract_sentences: 7
  phrases: {toTheBest: 1, inThisPaper: 3, contribList: 1, roadmap: 1, however: 4, transition: 18, resultsShow: 1, motivatedBy: 4, toAddress: 4, gapWord: 0, nonconvex: 5, npHard: 0, closedForm: 4, outperform: 4, intensifier: 7, worthNoting: 6, observe: 11, thisIsBecause: 1, asExpected: 0, insight: 1, tradeoff: 0, figVerb: 0, promising: 2, gen: 1, contrast: 0, firstTime: 0, novel: 1, weProposeFirst: 7, wlog: 0, code: 0, prototype: 0}
  methods: {AO: 23, complexity: 13, convergence: 10, convexOpt: 7, KKT: 1, compressedSensing: 1}
code:
  title_pattern: [X-for-Y, X-aided-Y]
  abstract_moves: [context, aim, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, gap, tech, prior, prior, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [investigate, derive, consider, provide]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, theory-gap]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [AO, closed-form, relaxation]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 6
  baseline_naming: descriptive
  x_axes: [iterations, number-of-elements, channel-power, transmit-power]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Capacity Characterization for [器件]-Aided MIMO Communication"，9 词。"Capacity Characterization" 宣告刻画基本极限——同组后来的 MA 论文直接复用此标题骨架（"MIMO Capacity Characterization for Movable Antenna Systems"）。

## 2. 摘要（7 句，242 词）
- 第 1 句 IRS 价值；"In this paper, we aim to characterize the fundamental capacity limit of IRS-aided point-to-point MIMO communication systems … in general, by jointly optimizing …"
- "First, we consider narrowband transmission … Next, we consider capacity maximization for broadband transmission …"——窄带 → 宽带两步；后者 "To tackle this more challenging problem, …"
- 结果两句，第二句是机理洞见："… various key parameters of the IRS-aided MIMO channel such as channel total power, rank, and condition number can be significantly improved for capacity enhancement."

## 3. 引言逻辑（8 段，约 1330 词）
1. 应用驱动容量需求 → massive MIMO / mmWave / UDN → "However, …, they generally require increased energy consumption and hardware cost, …" → "As such, it still remains an open and challenging problem whether deploying more active components in the wireless network can be a scalable solution …"
2. IRS 原理（反射系数、相长 / 相消）+ 与中继对比（全双工、无需放大与自干扰消除）。
3. "However, new challenges also arise …. First, …"：CSI 获取难（无射频链）+ 已有估计方法逐篇。
4. "Second, …"：被动波束设计 + IRS 与 NOMA / 安全 / SWIPT 的结合。
5. "It is worth noting that the existing works on IRS-aided communication mainly focused on SISO or MISO systems …" → MIMO 容量刻画仍未解决 → 为什么更难（多流需平衡各特征信道增益）→ 首创声明 + "which thus motivates this work."
6. "In this paper, we study …" + 两个理想化假设并说明目的（"To characterize the fundamental capacity limit, we consider that perfect CSI …"；单位幅度以降低实现复杂度）→ 4 条 bullet 贡献。
7. 路线图；8. Notations（另有 Table I 符号表）。

## 4. Idea 是怎么提出的
- 空白类型：新场景（MIMO 双端多天线）+ 理论空白（容量极限未刻画）。
- 写法亮点：引言第 1 段把领域层面的问题写成开放问题（"whether deploying more active components … can be a scalable solution"），IRS 作为回答；第 5 段说明 MIMO 比 SISO/MISO 难在哪里（多流、空间复用），让"推广到 MIMO"不只是换维度。
- 用 "First … Second …" 把 IRS 的两大挑战（CSI、反射设计）铺开后，再定位本文在第二个挑战的 MIMO 空白上。

## 5. 科研方法
- 问题 (P1)：联合优化 IRS 反射系数（单位模）与发射协方差 Q，最大化 MIMO 容量。
- 交替优化：Q 用注水闭式；每个反射系数单独优化，按 A_m^{-1}B_m 是否可对角化分两种情况给闭式最优解（Lemma 1–3、Proposition 1/2）→ 每个子问题都有闭式最优，因而单调收敛到局部最优。
- 低 SNR（最强特征信道功率最大化）与高 SNR（信道总功率最大化）两种低复杂度替代算法；MISO / SIMO 特例（Proposition 3/4）。
- MIMO-OFDM：所有子载波共用一组反射系数 → 凸松弛 + 交替优化（Algorithm 2）。证明全部在正文。

## 6. 仿真与实验
- Table II 汇总系统设置与参数；Fig. 2 给收发端与 IRS 的水平位置。
- 6 个比较方案用编号列表定义（无 IRS、随机相位、两种低复杂度替代、固定 Q 只优化反射、启发式总功率最大化）。
- 收敛 → 低 SNR 与高 SNR 两种距离分别出图（每图含 (b) 子图画特征信道功率 / 秩等信道参数以解释增益来源："To draw more insight, …"）→ 速率 vs 功率 → OFDM（"by 38.82% and 25.07% with M=20"）。

## 7. 图表
- 7 图 2 表 2 算法。Fig. 1 系统图在引言；结果图 caption 短标签并注明 SNR 区间与距离。

## 8. 句式库
- 领域开放问题："As such, it still remains an open and challenging problem whether deploying more active components in the wireless network can be a scalable solution …"
- 新挑战："However, new challenges also arise in the design and implementation of IRS-aided wireless systems. First, …"
- 已有工作集中于简单设置："It is worth noting that the existing works on IRS-aided communication mainly focused on single-input single-output (SISO) or multiple-input single-output (MISO) systems …"
- 为何更难："Note that this problem is also more difficult to solve as compared to that in IRS-aided SISO/MISO communications with single data stream transmission only, since …"
- 首创 + 动机："To the best of our knowledge, this problem has not been fully addressed yet …, which thus motivates this work."
- 理想化假设的目的："To characterize the fundamental capacity limit, we consider that perfect CSI of all channels … is available …"

## 9. 结论
- 1 段 233 词，过去时被动复述（was proposed / were derived / was considered）→ 机理洞见（信道功率、秩、条件数）→ 一句未来工作（非完美 CSI、受限反射硬件）。无数字。
