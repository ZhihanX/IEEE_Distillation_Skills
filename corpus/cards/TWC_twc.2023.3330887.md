---
doi: 10.1109/twc.2023.3330887
title: "Modeling and Performance Analysis for Movable Antenna Enabled Wireless Communications"
journal: TWC
year: 2024
band: 2022-2025
cites: 605
cites_per_year: 258.4
article_type: research
topic: movable-fluid-antenna
source: xplore-html
xplore: 10318061
auto:
  words_total: 10349
  n_sections: 5
  n_subsections: 25
  n_figures: 13
  n_tables: 0
  n_display_eq: 54
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 29.6
  we_per_1k: 5.2
  title_words: 10
  abstract_words: 300
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 0, roadmap: 1, however: 7, transition: 25, resultsShow: 1, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 2, outperform: 3, intensifier: 2, worthNoting: 2, observe: 5, thisIsBecause: 3, asExpected: 0, insight: 2, tradeoff: 1, figVerb: 3, promising: 1, gen: 0, contrast: 10, firstTime: 0, novel: 2, weProposeFirst: 2, wlog: 1, code: 0, prototype: 1}
  methods: {AO: 1, SCA: 1, monteCarlo: 1}
code:
  title_pattern: [X-for-Y, X-aided-Y]
  abstract_moves: [aim, context, method, theory, theory, theory, theory, theory, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [tech, solution, gap, prior, prior, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 5
  contrib_verbs: [develop, analyze, show, derive, reveal]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-architecture, limitation]
  motivating_figure: true
  problem_class: analysis-only
  solution: [closed-form]
  theory_role: central
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [region-size, CDF, number-of-paths]
  fig1_role: architecture
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Modeling and Performance Analysis for [新器件] Enabled [系统]"，10 词。开山论文的典型标题：只说"建模 + 分析"，不出现任何优化方法——新概念本身就是贡献。

## 2. 摘要（9 句，约 300 词，偏长）
- 第一句即提出新概念："In this paper, we propose a novel antenna architecture called movable antenna (MA) to improve …"
- 第二句用对比讲清物理机理："Different from conventional fixed-position antennas (FPAs) that undergo random wireless channel variation, the MAs … can be deployed at positions with more favorable channel conditions …"
- 后面 6 句全是分析结论（场响应模型、确定性信道的周期性、随机信道的上界期望、闭式近似 CDF、路径数越多增益越大），最后一句数值验证并给出"甚至可比 SIMO 波束成形"的对比结论。

## 3. 引言逻辑（8 段，约 1540 词）
1. 技术：MIMO → massive MIMO 的空间自由度。
2. 局限 + 方案："However, since the antennas are deployed at fixed positions, conventional MIMO and massive MIMO cannot fully explore the spatial variation …" → "To overcome this limitation, we propose a new antenna architecture, namely movable antenna (MA)" → 与天线选择（AS）对比（"In contrast, the MA system can reap the full spatial diversity with much fewer or even one single antenna"）。
3. 适用边界："It is worth noting that the aforementioned performance improvement of MA systems relies on …"——主动说明快变信道下不适用，再给出适用场景（IoT、NB-IoT、LoRa）。
4. 实现可行性：类比 DAS，列出雷达 / 导航 / 定位里已有的移动天线原型 → "However, the above works mainly focus on the application of MA in radar, navigation, localization, …"
5. 通信领域的已有 MA / FAS 工作 → "However, the discrete port-based channel model employed in [30] and [31] cannot completely characterize …"（为"建模"贡献铺垫）。
6. "Given the above technical advantages and potential applications of MA, we aim to investigate in this paper …"，散文式列出 5 项结论。
7. 路线图；8. Notation。

## 4. Idea 是怎么提出的
- 空白类型：新架构（固定位置天线无法利用连续空间变化）+ 已有模型局限（FAS 的离散端口模型）。
- 写法亮点：
  - 主动交代适用边界（慢变信道），比回避更能说服审稿人；
  - 先在别的领域找"已有原型"证明可实现，再说通信里还没人做；
  - 新概念配一个新模型（field-response model），并在第 II-B 节证明它退化为 LoS / 几何 / Rayleigh / Rician 等经典模型——"新模型兼容旧模型"。

## 5. 科研方法
- 纯分析论文：没有优化问题、没有定理环境，结论以编号公式和逐情形推导给出。
- 分析按"确定性信道 → 随机信道"，每部分再按路径数分情形（1 / 2 / 3 / 多 / 无穷路径），从简单到一般。
- 单列 "Implementation Issues of MA Systems"（频段、移动机构、位置优化、时间开销），讨论落地问题。

## 6. 仿真与实验
- baseline：FPA、天线选择（AS）、数字波束成形（DBF / SIMO），用 bullet 定义。
- 先验证解析结果（"the simulated CDF … perfectly matches the analytical result derived in (39)"），再用 3GPP 室内工厂信道模型评估实际性能。
- 横轴主要是归一化区域尺寸和路径数。

## 7. 图表
- 13 图 0 表。Fig. 1 架构图、Fig. 2 坐标与角度示意；Fig. 3–5 用信道增益热图展示周期性（"机理可视化"）；其余为性能曲线。
- caption 描述型并带参数取值。

## 8. 句式库
- 局限 → 方案："To overcome this limitation, we propose a new antenna architecture, namely movable antenna (MA), for exploiting the DoFs in the continuous spatial domain more efficiently."
- 与替代方案对比："In contrast, the MA system can reap the full spatial diversity with much fewer or even one single antenna moving in a given region."
- 主动划边界："It is worth noting that the aforementioned performance improvement of MA systems relies on the capability of mechanically moving the antennas …"
- 已有工作局限："However, the discrete port-based channel model employed in [30] and [31] cannot completely characterize and fully exploit the wireless channel spatial variation in continuous regions."
- 引出本文："Given the above technical advantages and potential applications of MA, we aim to investigate in this paper …"

## 9. 结论
- 1 段 424 词（很长），过去时逐条复述全部结论，最后两句给出未来方向（信道估计、位置搜索、多天线 / 多用户、宽带）。
