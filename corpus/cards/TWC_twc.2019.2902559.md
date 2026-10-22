---
doi: 10.1109/twc.2019.2902559
title: "Energy Minimization for Wireless Communication With Rotary-Wing UAV"
journal: TWC
year: 2019
band: 2019-2021
cites: 2112
cites_per_year: 281.3
article_type: research
topic: UAV
source: xplore-html
xplore: 8663615
auto:
  words_total: 9100
  n_sections: 6
  n_subsections: 9
  n_figures: 8
  n_tables: 1
  n_display_eq: 51
  n_algorithms: 2
  statements: {theorem: 0, lemma: 1, proposition: 0, corollary: 0, remark: 1, proof: 1, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 27.1
  we_per_1k: 6.9
  title_words: 8
  abstract_words: 242
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 0, however: 13, transition: 18, resultsShow: 2, motivatedBy: 0, toAddress: 8, gapWord: 0, nonconvex: 16, npHard: 0, closedForm: 2, outperform: 5, intensifier: 4, worthNoting: 0, observe: 7, thisIsBecause: 0, asExpected: 4, insight: 2, tradeoff: 3, figVerb: 5, promising: 1, gen: 0, contrast: 8, firstTime: 0, novel: 1, weProposeFirst: 8, wlog: 1, code: 0, prototype: 0}
  methods: {SCA: 17, convexOpt: 6, convergence: 6, KKT: 3}
code:
  title_pattern: [X-for-Y, X-with-Y]
  abstract_moves: [aim, aim, method, method, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 7
  intro_moves: [field, prior, gap, aim, contrib, contrib, contrib]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 3
  contrib_verbs: [derive, formulate, propose]
  contrib_quantified: false
  first_claim: false
  roadmap: false
  notation: table
  gap_type: [limitation, new-scenario]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [reformulation, SCA, heuristic]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: false
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 4
  baseline_naming: descriptive
  x_axes: [iterations, trajectory-plot, time, QoS-requirement]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[目标] Minimization for [系统] With [器件类型]"，8 词。与同组 2017 年固定翼论文形成系列：只把 "Fixed-Wing" 换成 "Rotary-Wing"。

## 2. 摘要（9 句，242 词）
- "This paper studies …" → "We aim to minimize the total UAV energy consumption, including both propulsion energy and communication related energy, while satisfying …"
- "To this end, we first derive a closed-form propulsion power consumption model for rotary-wing UAVs, and then formulate …"（先建模再建问题，与 2017 篇同构）。
- 难度句给出两个原因："The problem is difficult to be optimally solved, as it is non-convex and involves infinitely many variables over time."
- 两阶段方法：先简单协议（fly-hover-communicate，借 TSPN）获得洞见，再一般情形（新提出的 path discretization + SCA）。

## 3. 引言逻辑（7 段，约 1300 词）
1. 空中平台演进：HAP → LAP → UAV，列出 UAV 的优势与用例。
2. 已有 UAV 通信工作分两类（准静态空中基站 / 移动基站、中继、AP），逐类列文献。
3. 关键问题：机载能量有限 → 推进能耗使能效设计不同于地面 → 自己 2017 年的固定翼工作 → "However, the above results for fixed-wing UAVs cannot be applied for rotary-wing UAVs, due to their fundamentally different mechanical designs …" + 只考虑单节点 → "This thus motivates our current work …"
4. "In this paper, we study …" → 旋翼的优势（垂直起降、悬停，市场更流行）→ 场景与目标 → "The main contributions of this paper are summarized as follows."
5–7. 三段散文式贡献（First, … / Based on the derived power consumption model, … / Next, …），每段都解释"为什么这样做"（如功率模型非凸非凹、V=0 时有限 → 设计方法不同；路径离散化不需预设任务时长）。
- 无路线图、无记号段（记号放在模型节的 Table I）。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（固定翼模型不适用旋翼）+ 新场景（多地面节点）。这是"自我延续"型选题：在自己的高引工作上换一个关键假设。
- 写法亮点：用两个物理事实对比两类 UAV 的功率模型（固定翼 V=0 时功率无穷，旋翼有限且可悬停），说明为什么需要新的轨迹设计方法。
- 方法上的新意（path discretization）放在贡献第 3 段，并点明与常用 time discretization 的区别："Different from the widely used time discretization approach …, path discretization does not require the mission completion time to be pre-specified."

## 5. 科研方法
- 模型：概率 LoS 信道（比自由空间更一般，并说明两点差别）、TDMA、旋翼推进功率模型（附录推导，受力图）、ME / MR 两个特殊速度。
- 问题 (P1)：连续时间轨迹与调度 + 任务时长，无穷维、非凸。
- fly-hover-communicate：单节点最优解（Lemma 1：以 MR 速度飞行）→ 多节点归结为 TSPN（NP-hard，含 TSP 为特例）+ 凸优化。
- 一般解：路径离散化 → (P4) → 引入松弛变量 → SCA，收敛到 KKT 点。

## 6. 仿真与实验
- 参数附现实依据（"which complies with the FAA regulation that small unmanned aircrafts should not fly over 400 feet (122 m)"）。
- 先收敛（并说明另一算法 "result is omitted due to the space limitation"），再不同吞吐要求下的轨迹与速度，再验证吞吐近似的精度，最后能耗 / 任务时间 vs 吞吐要求，与 3 种带引号命名的基准比较。

## 7. 图表
- 8 图 1 表（记号与术语表）。Fig. 1 场景图在引言，Fig. 2 功率—速度曲线（模型可视化）。轨迹图 caption 解释标记（"Red squares denote GNs, and blue circles represent …"）。

## 8. 句式库
- 不可迁移："However, the above results for fixed-wing UAVs cannot be applied for rotary-wing UAVs, due to their fundamentally different mechanical designs and hence drastically different propulsion energy models."
- 动机收束："This thus motivates our current work to investigate …"
- 难度双因："The problem is difficult to be optimally solved, as it is non-convex and involves infinitely many variables over time."
- 先简后繁："To tackle this problem, we first consider the simple fly-hover-communicate design to gain useful insights."
- 与常用方法区分："Different from the widely used time discretization approach …, path discretization does not require …"

## 9. 结论
- 1 段 127 词，一般现在时复述（"This paper studies … is derived … We first propose … Furthermore, we propose …"），无数字、无未来工作。
