---
doi: 10.1109/jsac.2018.2864426
title: "Computation Rate Maximization in UAV-Enabled Wireless-Powered Mobile-Edge Computing Systems"
journal: JSAC
year: 2018
band: 2016-2018
cites: 815
cites_per_year: 100.7
article_type: research
topic: UAV
source: xplore-html
xplore: 8434285
auto:
  words_total: 6995
  n_sections: 6
  n_subsections: 14
  n_figures: 8
  n_tables: 2
  n_display_eq: 29
  n_algorithms: 2
  statements: {theorem: 5, lemma: 2, proposition: 0, corollary: 0, remark: 4, proof: 4, proof_in_appendix: 2}
  n_appendix: 2
  mean_sentence_words: 22.3
  we_per_1k: 0.5
  title_words: 9
  abstract_words: 195
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 7, contribList: 2, roadmap: 1, however: 7, transition: 11, resultsShow: 1, motivatedBy: 2, toAddress: 10, gapWord: 0, nonconvex: 7, npHard: 0, closedForm: 2, outperform: 3, intensifier: 7, worthNoting: 1, observe: 4, thisIsBecause: 0, asExpected: 0, insight: 1, tradeoff: 2, figVerb: 5, promising: 5, gen: 0, contrast: 7, firstTime: 1, novel: 0, weProposeFirst: 0, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 10, convexOpt: 5, convergence: 4, SCA: 3, lagrange: 3, bisection: 2, KKT: 1, ADMM: 1, DRL: 1, gameTheory: 1, lyapunov: 1}
code:
  title_pattern: [X-in-Y]
  abstract_moves: [context, gap, aim, method, method, method, theory, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 12
  intro_moves: [field, tech, tech, aim, prior, prior, prior, gap, prior, gap, contrib, roadmap]
  related_work: in-intro-subsection
  contrib_format: numbered
  contrib_n: 3
  contrib_verbs: [formulate, propose, show]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: none
  gap_type: [combination, limitation]
  motivating_figure: true
  problem_class: MINLP
  solution: [AO, lagrangian-dual, closed-form, SCA, bisection]
  theory_role: supporting
  proofs_location: mixed
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 4
  baseline_naming: descriptive
  x_axes: [trajectory-plot, transmit-power, number-of-users, iterations]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[目标] Maximization in [三重修饰的系统]"，9 词。"UAV-Enabled Wireless-Powered Mobile-Edge Computing"——三个连字符修饰语叠加，组合型选题的典型标题。

## 2. 摘要（10 句，195 词）
- 背景句同时介绍两个技术（MEC、WPT）→ "However, … significantly impacted by the severe propagation loss." → "In order to address this issue, an unmanned aerial vehicle (UAV)-enabled MEC wireless-powered system is studied in this paper."（被动语态 + 句尾锚点）。
- 后续全部被动语态："… are investigated", "These problems are non-convex and challenging to solve.", "… are, respectively, proposed", "… are derived"。
- 结尾两句结果，第二句强调"converge fast and have low computational complexity"。

## 3. 引言逻辑（4 段 + A. Related Work and Motivation 6 段 + B. Contributions and Organization）
1. IoT 与设备能力受限。
2–3. 两项使能技术（MEC 的两种卸载模式；WPT 及其路损问题 → UAV 供能架构）。
4. 提前给出本文和首创声明："Motivated by the above mentioned reasons, a UAV-enabled and wireless powered MEC network is studied in this paper. … To the authors' best knowledge, this is the first work that …"
5–9. 相关工作按三条线（MEC 资源分配 / 能量收集 MEC / UAV 供能与 UAV-MEC）逐篇综述，每线末尾指出不足。
10. 汇总空白："Although resource allocation problems have been well studied in …, few investigations have been conducted for …" + 现有方案为何不适用 + 难点（"The reasons are from two aspects. On one hand, … On the other hand, …"）。
11. "In contrast to [5]–[16], this paper studies …"，并预先回应弱点（"Although the computation performance is limited by the flight time of the UAV, it is worth studying … since …"）→ 3 条编号贡献。
12. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：三重组合（UAV × WPT × MEC）+ 已有方案不适用（不含轨迹设计）。
- 写法亮点：
  - 首创声明出现两次（第 4 段与贡献第 1 条 "It is the first time that …"）；
  - 主动预判审稿人质疑（UAV 续航有限）并给出适用场景（山区、沙漠、灾后）。

## 5. 科研方法
- 部分卸载：两阶段交替——给定轨迹时用拉格朗日对偶得 CPU 频率、发射功率、卸载时间的闭式解（Theorem 1–3，次梯度更新对偶变量），给定资源时用 SCA 优化轨迹（Theorem 4、Lemma 2）。
- 二元卸载：引入二元变量，三阶段交替，给出最优模式选择（Theorem 5：取决于"计算速率与运行代价"的折中）。
- 每个定理后接 Remark 解释物理含义（如阈值结构："users choose to offload their computation tasks only when the channel … is stronger than a threshold"）。
- "Theorem 3 can be readily proved based on the proof for Theorem 1. Thus this proof is omitted for the sake of saving space."
- 算法以表格形式给出（Table I/II），单列复杂度分析。

## 6. 仿真与实验
- "The simulation settings are based on the works in [7], [14], [16], and [23]."——参数沿用文献。
- baseline：只本地计算、只卸载、不联合优化、不同轨迹。
- 附运行时间表（Table IV），并写明测试机器配置。

## 7. 图表
- 8 图 4 表（2 个是算法表）。caption 描述型："The weighted sum computation bits of all users versus the transmit power of the UAV under different schemes."

## 8. 句式库
- 引出本文（被动）："In order to address this issue, an unmanned aerial vehicle (UAV)-enabled MEC wireless-powered system is studied in this paper."
- 难度声明："These problems are non-convex and challenging to solve."
- 空白汇总："Although resource allocation problems have been well studied in …, few investigations have been conducted for designing … in …"
- 预先回应弱点："Although the computation performance is limited by the flight time of the UAV, it is worth studying … since these systems are promising in environments such as …"
- 省略证明："… can be readily proved based on the proof for Theorem 1. Thus this proof is omitted for the sake of saving space."

## 9. 结论
- 2 段：第 1 段被动语态复述；第 2 段承认 UAV 续航限制并提出多天线作为未来工作。
