---
doi: 10.1109/tcomm.2025.3621049
title: "Modeling and Beamforming Optimization for Pinching-Antenna Systems"
journal: TCOM
year: 2025
band: 2022-2025
cites: 136
cites_per_year: 136.0
article_type: research
topic: movable-fluid-antenna
source: xplore-html
xplore: 11202577
auto:
  words_total: 7257
  n_sections: 5
  n_subsections: 21
  n_figures: 12
  n_tables: 0
  n_display_eq: 67
  n_algorithms: 3
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, remark: 2, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.3
  we_per_1k: 4.3
  title_words: 7
  abstract_words: 223
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 1, roadmap: 2, however: 17, transition: 11, resultsShow: 2, motivatedBy: 1, toAddress: 9, gapWord: 0, nonconvex: 1, npHard: 0, closedForm: 1, outperform: 0, intensifier: 8, worthNoting: 4, observe: 4, thisIsBecause: 2, asExpected: 3, insight: 1, tradeoff: 0, figVerb: 3, promising: 4, gen: 2, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 3, wlog: 0, code: 0, prototype: 1}
  methods: {penalty: 23, complexity: 23, AO: 12, convergence: 11, convexOpt: 2, SCA: 1, DNN: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, context, method, method, method, method, method, result]
  abstract_has_numbers: true
  abstract_anchor: this-paper-verb
  intro_paragraphs: 9
  intro_moves: [field, tech, tech, gap, solution, prior, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, derive, formulate, provide]
  contrib_quantified: true
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [practicality, limitation, new-architecture]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [penalty, AO, closed-form, exhaustive-search, reformulation]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [iterations, SINR-target, distance, number-of-antennas, discrete-positions, CSI-error]
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Modeling and Beamforming Optimization for [新架构]"，7 词。"建模 + 优化"双任务标题，与 IRS 实用相移模型论文（TCOM 2020）同一思路：新器件先把物理模型做实，再做波束设计。

## 2. 摘要（8 句，223 词）
- 前两句介绍技术本身（"a revolutionary flexible antenna technology …"；工作原理一句）——新技术论文先花两句讲"它是什么"。
- "This paper first proposes a physics-based hardware model for PASS, where …"——以 this paper 为主语的锚点句。
- 随后：信号模型 → 两种功率模型 → 功率最小化问题（连续 / 离散激活）→ 两个算法（penalty-AO、ZF 低复杂度）。
- 末句用编号 1)–4) 列 4 条数值结论，含 "reduces transmit power by over 95%"。

## 3. 引言逻辑（9 段，约 1490 词）
1. 从 Marconi 讲起的历史纵深：MIMO → massive MIMO（Marzetta 2010）→ 5G 部署。
2. "However, massive MIMO has faced numerous challenges, as it is expected to transition from 'Massive' in 5G … to 'Gigantic' in 6G …" → RF 链成本 → 低精度 ADC / 混合架构 / 超表面天线。
3. 柔性天线（RIS、流体、可移动天线）："Unlike massive MIMO which focuses on enlarging the wireless channel dimension, the flexible-antenna technique focuses on enabling the reconfiguration of the wireless channel."
4. 共同局限（结合 Fig. 1 左图）：都不能从根本上解决路径损耗和 LoS 阻挡；逐类说明（RIS 双衰落、MA/FA 只能移动几个波长）→ "It is worth pointing out that all the aforementioned MIMO systems lack antenna array reconfigurability, …"
5. PASS 原理（NTT DOCOMO 2022 原型、0.01 dB/m 波导损耗）与优势（Fig. 1 右图）。
6. 已有 PASS 理论工作逐篇一句。
7. 两个挑战（"On the one hand, the physics modeling of PASS is still underdeveloped …" / "On the other hand, most existing works design PASS under simplified assumptions …"）→ "Motivated by these challenges, this paper aims to …" → 4 条 bullet 贡献。
8. 路线图；9. Notations。

## 4. Idea 是怎么提出的
- 空白类型：实用性（已有工作默认"功率全部辐射且各天线等功率"，缺乏物理依据）+ 方法局限（简化场景；GNN 方法换配置要重训）+ 新架构。
- 写法亮点：引言用一张左右对比图（传统系统 vs PASS）承载"已有技术都解决不了的两个问题"，再用同一张图的右半边引出新技术。
- 对已有假设的批评措辞克制："such assumptions may lack a solid physical foundation and fail to accurately reflect real-world behaviors."

## 5. 科研方法
- 硬件模型：夹持天线 = 开口定向耦合器；耦合模理论求波导与天线间的场分布 → 功率由耦合长度决定（Remark 1）。
- 信号模型：单天线 → 同一波导上多天线（功率依次耦合出去）→ 等功率模型 / 比例功率模型两种简化。
- 优化：发射功率最小化，联合发射波束与天线位置，SINR + 最小间距约束；目标函数关于位置高度多峰（Fig. 4 专门画出"简单"场景下的多峰信道增益）。
- 算法 1：penalty-based AO（V、U、Um、X 四块，X 逐元素一维搜索，连续 / 离散两种激活都可用）；算法 2：ZF 消除用户间干扰后的低复杂度 AO。复杂度逐变量给出 O(·)。
- 无定理，只有 2 个 Remark。

## 6. 仿真与实验
- 室内场景，参数写在正文（Fig. 5 仿真几何）；基准两种：Conventional MIMO、Massive MIMO（各自给阵列配置）。
- 结果按 "Impact of …" 小节组织（最小 SINR / 距离 / 天线数 / 离散位置数 / 信道估计误差），每小节一张图。
- 反直觉现象明确点出并解释："it is somewhat counterintuitive that the transmit power in conventional MIMO initially decreases before increasing. This phenomenon arises because …"

## 7. 图表
- 12 图 0 表 3 算法。Fig. 1 传统 vs PASS 对比图（引言），Fig. 2 耦合器物理示意，Fig. 3 联合波束架构，Fig. 4 多峰目标函数示意（说明为什么要一维搜索）。结果图 caption 统一 "Transmit power versus …"。

## 8. 句式库
- 演进叙事："The flexible antenna technique is a new evolution of MIMO."
- 对比定位："Unlike massive MIMO which focuses on enlarging the wireless channel dimension, the flexible-antenna technique focuses on enabling the reconfiguration of the wireless channel."
- 共同短板："It is worth pointing out that all the aforementioned MIMO systems lack antenna array reconfigurability, …"
- 双挑战："On the one hand, the physics modeling of PASS is still underdeveloped, which is crucial for establishing an accurate signal model."
- 假设缺乏依据："… such assumptions may lack a solid physical foundation and fail to accurately reflect real-world behaviors."
- 反直觉结果："Furthermore, it is somewhat counterintuitive that … This phenomenon arises because …"

## 9. 结论
- 2 段 158 词：第 1 段现在完成时复述（"This paper has proposed … serving as a valuable reference for future research."）；第 2 段 "However, several key challenges remain unresolved." 列 3 条局限 / 方向（上行建模、混合架构、实际部署）。无数字。
