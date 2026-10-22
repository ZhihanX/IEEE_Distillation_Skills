---
doi: 10.1109/twc.2023.3307696
title: "MIMO Capacity Characterization for Movable Antenna Systems"
journal: TWC
year: 2024
band: 2022-2025
cites: 450
cites_per_year: 179.4
article_type: research
topic: movable-fluid-antenna
source: xplore-html
xplore: 10243545
auto:
  words_total: 8450
  n_sections: 5
  n_subsections: 15
  n_figures: 9
  n_tables: 0
  n_display_eq: 46
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 27.2
  we_per_1k: 10.8
  title_words: 7
  abstract_words: 186
  abstract_sentences: 6
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 1, roadmap: 1, however: 8, transition: 23, resultsShow: 2, motivatedBy: 0, toAddress: 2, gapWord: 0, nonconvex: 6, npHard: 0, closedForm: 1, outperform: 4, intensifier: 8, worthNoting: 2, observe: 3, thisIsBecause: 2, asExpected: 0, insight: 2, tradeoff: 0, figVerb: 3, promising: 1, gen: 1, contrast: 3, firstTime: 0, novel: 0, weProposeFirst: 8, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 23, AO: 13, convergence: 12, SCA: 7, convexOpt: 3}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, context, aim, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 9
  intro_moves: [field, gap, gap, gap, solution, prior, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [derive, investigate, present]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [limitation, new-architecture]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [AO, SCA, closed-form]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 7
  baseline_naming: acronym
  x_axes: [iterations, region-size, SNR, number-of-antennas]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[性能指标] Characterization for [新器件] Systems"，7 词。"Capacity Characterization" 暗示"刻画极限"，与 IRS 的 "Capacity Characterization for IRS Aided MIMO"（同组）同构——同一作者组对新器件的固定套路：建模 → 容量刻画 → 多用户。

## 2. 摘要（6 句，186 词）
- "In this paper, we propose a new … system with movable antennas (MAs) to exploit the antenna position optimization for enhancing the capacity."
- 第 2 句用 "Different from conventional MIMO systems with fixed-position antennas (FPAs), …" 说清机理（与 2024 MA 建模论文的摘要第 2 句几乎同构）。
- "We aim to characterize the capacity of …, by jointly optimizing …" → "First, …" / "Next, …" 两步方法。
- 结尾 "… and useful insights are drawn into the capacity gains of MA systems."

## 3. 引言逻辑（9 段，约 1660 词）
1. 容量需求 → MIMO / massive MIMO → "However, … they generally demand considerably higher hardware costs and energy consumption …"
2–4. 一条"替代方案阶梯"，每级都以 However 收尾：天线选择 / 混合预编码（位置固定，无法利用空间变化）→ 可旋转 ULA（只能旋转）→ 流体天线（只能沿一维线移动）→ 连续孔径 MIMO（信道估计和电流优化难）。
5. "To exploit more spatial DoFs for enhancing the channel capacity, we propose a new MIMO communication system enabled by movable antennas (MAs)." → 实现方式（柔性电缆 + 步进电机）→ 与 FPA 对比。
6. 已有 MA 工作（含自己的接收端 MA 会议版）→ 与天线选择的区别（"On one hand, … On the other hand, …"）→ 为什么需要更高效的位置优化算法。
7. "In this paper, we study …" + 假设完美 CSI 以刻画极限 → 3 条贡献。
8. 路线图；9. Notations。

## 4. Idea 是怎么提出的
- 空白类型：已有方案局限 + 新架构。写法上用"逐级排除替代方案"：列出 4 类相近方案，每类给一句致命局限，最后自然落到 MA。
- 主动说明与最相近的天线选择的差别，并预先回答"为什么不直接用 AS 算法"（复杂度随区域增大）。
- "To characterize the fundamental capacity limit, we assume that perfect CSI is available …"——为分析极限而做的理想化假设，明确说明目的。

## 5. 科研方法
- 场响应信道模型（沿用同组建模论文）；问题：联合优化收 / 发天线位置与发送协方差，含最小间距约束，高度非凹。
- 交替优化：Q 用特征模传输 + 注水（闭式），每个天线位置用 SCA（构造二阶下界，附录给梯度、Hessian 与 δ 的构造）；收敛与复杂度分别分析。
- 圆填充初始化；低 SNR 下的简化算法（SEPM）；MISO / SIMO 特例。
- 全文无定理环境。

## 6. 仿真与实验
- 7 个基准用编号列表定义，每个都有缩写（FPA、AS、SEPM、RMA、APS、RP、RULA）——覆盖"固定阵列 / 选择 / 只动接收端 / 离散位置 / 随机位置 / 旋转阵列"各类替代方案，与引言的"替代方案阶梯"呼应。
- 低 SNR 与高 SNR 分开展示；扫区域大小、SNR、天线数；最后比较不同预编码架构下 MA 与 FPA。

## 7. 图表
- 9 图 0 表。Fig. 1 系统图，Fig. 2 空间角与路径差示意，Fig. 3 圆填充初始化示意。caption 短标签。

## 8. 句式库
- 成本代价："However, although MIMO/massive MIMO can enhance … significantly, they generally demand considerably higher hardware costs and energy consumption, due to …"
- 固定位置局限："However, since the antennas are deployed at fixed positions …, they cannot fully utilize the spatial variation of wireless channels in a given transmit/receive region, …"
- 替代方案局限："However, due to the limitations of liquid materials, the FAS can only support a single fluid antenna moving over a 1D line, which limits its capability …"
- 提出方案："To exploit more spatial DoFs for enhancing the channel capacity, we propose a new MIMO communication system enabled by movable antennas (MAs)."
- 理想化假设的目的："To characterize the fundamental capacity limit, we assume that perfect CSI is available at both the transmitter and receiver."

## 9. 结论
- 1 段 179 词：过去时复述 → 定性结论 + 机理解释（"the MIMO channel power can be significantly improved while the condition number of the MIMO channel decreases"）。无数字、无未来工作。
