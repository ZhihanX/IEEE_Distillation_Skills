---
doi: 10.1109/twc.2023.3338626
title: "Movable-Antenna Enhanced Multiuser Communication via Antenna Position Optimization"
journal: TWC
year: 2024
band: 2022-2025
cites: 391
cites_per_year: 173.1
article_type: research
topic: movable-fluid-antenna
source: xplore-html
xplore: 10354003
auto:
  words_total: 10097
  n_sections: 5
  n_subsections: 10
  n_figures: 13
  n_tables: 1
  n_display_eq: 36
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 28.8
  we_per_1k: 5.8
  title_words: 8
  abstract_words: 270
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 0, roadmap: 1, however: 7, transition: 24, resultsShow: 4, motivatedBy: 0, toAddress: 4, gapWord: 0, nonconvex: 8, npHard: 0, closedForm: 0, outperform: 2, intensifier: 13, worthNoting: 2, observe: 3, thisIsBecause: 5, asExpected: 0, insight: 0, tradeoff: 2, figVerb: 1, promising: 1, gen: 0, contrast: 5, firstTime: 0, novel: 0, weProposeFirst: 3, wlog: 1, code: 0, prototype: 0}
  methods: {convergence: 9, complexity: 7, AO: 3, convexOpt: 1, manifold: 1}
code:
  title_pattern: [X-via-Y, X-aided-Y]
  abstract_moves: [context, aim, method, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, tech, tech, prior, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 4
  contrib_verbs: [formulate, develop, analyze, evaluate]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [gradient, closed-form, reformulation]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 2
  baseline_naming: acronym
  x_axes: [iterations, channel-gain-map, rate-requirement, number-of-users, number-of-paths, region-size, AoD-error, PRM-error]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[新技术]-Enhanced [场景] via [优化对象]"，8 词。"Enhanced … via …"：前半句说用什么增强什么，后半句说靠什么手段——与同组 "MIMO Capacity Characterization for MA Systems" 构成系列（单链路 → 多用户）。

## 2. 摘要（8 句，270 词，偏长）
- 第 1 句技术定义式介绍（"… is a promising technology to improve … by varying the antenna position …"）。
- "In this paper, we investigate the MA-enhanced multiple-access channel (MAC) for the uplink transmission from …"
- 信道模型一句 → 问题一句（"To evaluate the MAC performance gain provided by MAs, we formulate …"）→ 难点 + 两种算法 → 算法核心（把合并矩阵和功率写成天线位置的函数，再用 MDD 优化）。
- "It is shown that … can converge to high-quality suboptimal solutions with low computational complexities." + 仿真对比（与 FPA + 天线选择），无数字。

## 3. 引言逻辑（8 段，约 2160 词，很长）
1. MIMO 的空间自由度 → "However, conventional MIMO and/or massive MIMO systems usually adopt fixed-position antennas (FPAs) …" → 固定离散部署无法利用连续空间信道变化。
2. MA 的实现方式与历史原型（雷达、导航、测向、可旋转 ULA）逐一列举。
3. MA 的三个优势："First, … full diversity"、"Second, … interference mitigation gain"、"Third, … higher spatial multiplexing rate"。
4. 已有 MA / FAS 研究逐篇较详细地复述（每篇两三句）。
5. 比较两类实现（机械 MA vs 流体天线）："On one hand, … On the other hand, …"——指出端口模型只能在离散集合里穷举，类似天线选择 → "In contrast, the field-response based channel model … provides a new paradigm for designing wireless communication systems."
6. "In light of the above, this paper considers …"：多用户 FPA 研究未利用位置自由度 → 问题、算法、收敛分析、单用户特例、仿真发现、非理想 FRI——贡献全部以散文写在一段里（约 450 词）。
7. 路线图；8. Notation。

## 4. Idea 是怎么提出的
- 空白类型：新场景（MA 用于多用户上行接入）+ 已有方法局限（端口模型离散、均匀散射假设不现实）。
- 写法亮点：先比较同一思想的两种实现路线，选定自己这一派的模型并说明它"在连续区域里优化位置"的范式优势，再落到具体问题——选题理由由"模型路线之争"给出。
- 自我延续：沿用同组 [9][10] 的场响应信道模型，并把 2D 扩展到 3D。

## 5. 科研方法
- 场响应信道模型（FRV + 路径响应矩阵 PRM）；问题：总发射功率最小化，变量为各用户 MA 位置、发射功率、BS 合并矩阵，含最低速率约束。
- 方法设计带"为什么不用 AO"的论证："In general, the alternating optimization among the three matrix/vector variables may lead to a (undesired) local optimum."——再给出原因（合并矩阵与旧位置匹配，位置难以大幅移动）。
- 解法：ZF / MMSE 合并下把合并矩阵与功率写成位置的函数 → 多方向下降（MDD）：多个候选下降方向 + 回溯线搜索（Armijo–Goldstein）；指出梯度下降和牛顿法是 MDD 的特例。
- 复杂度 O(·)、收敛性论证；单用户特例另给解法。无定理环境。

## 6. 仿真与实验
- Table I 参数；提出方案命名为 "Proposed MA-ZF"、"Proposed MA-MMSE"；基准 AS（贪婪天线选择）与 MCP，用缩写。
- 先收敛（Fig. 3）→ "To shed more light on the properties of Algorithm 2, …"（Fig. 4 目标信号与干扰功率随迭代变化，解释算法在做什么）→ 信道增益随位置的热图 → 与基准对比（速率要求 / 用户数 / 路径数 / AoA 数 / 移动区域）→ 非理想 FRI（AoD 误差、PRM 误差分开评估）。

## 7. 图表
- 13 图 1 表 2 算法。Fig. 1 系统图，Fig. 2 局部坐标与空间角示意。结果图 caption 统一 "Total transmit powers of different schemes versus …"。

## 8. 句式库
- 固定位置局限："Such fixed and discrete deployment of antennas limits the diversity and spatial multiplexing performance of MIMO systems because …"
- 新方案："Recently, movable antenna (MA) was proposed as a new solution to break the above fundamental limitations of FPA systems."
- 枚举优势："First, the MA systems can reap the full diversity in the given spatial region."
- 范式表述："Under such channel models, the antenna position can be optimized in continuous Tx/Rx regions, which provides a new paradigm for designing wireless communication systems."
- 方法设计理由："In general, the alternating optimization among the three matrix/vector variables may lead to a (undesired) local optimum."
- 解释算法行为："To shed more light on the properties of Algorithm 2, in Fig. 4, we show …"

## 9. 结论
- 2 段 459 词（偏长）：第 1 段过去时逐步复述方法与所有仿真发现；第 2 段 "A natural generalization of this work is to consider multi-MA users and/or multi-cell systems." + FRI 估计协议。无数字。
