---
doi: 10.1109/jsac.2016.2611964
title: "Dynamic Computation Offloading for Mobile-Edge Computing With Energy Harvesting Devices"
journal: JSAC
year: 2016
band: 2016-2018
cites: 1635
cites_per_year: 166.1
article_type: research
topic: MEC-offloading
source: xplore-html
xplore: 7572018
auto:
  words_total: 8734
  n_sections: 7
  n_subsections: 21
  n_figures: 7
  n_tables: 1
  n_display_eq: 38
  n_algorithms: 1
  statements: {theorem: 1, lemma: 6, proposition: 4, corollary: 4, definition: 2, remark: 3, proof: 15, proof_in_appendix: 4}
  n_appendix: 1
  mean_sentence_words: 26.8
  we_per_1k: 12.1
  title_words: 10
  abstract_words: 255
  abstract_sentences: 11
  phrases: {toTheBest: 0, inThisPaper: 6, contribList: 1, roadmap: 1, however: 6, transition: 21, resultsShow: 1, motivatedBy: 0, toAddress: 1, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 3, intensifier: 3, worthNoting: 0, observe: 8, thisIsBecause: 0, asExpected: 0, insight: 1, tradeoff: 2, figVerb: 0, promising: 1, gen: 0, contrast: 3, firstTime: 0, novel: 0, weProposeFirst: 0, wlog: 2, code: 0, prototype: 0}
  methods: {lyapunov: 9, bisection: 2, penalty: 2, convergence: 6, complexity: 4, gameTheory: 1}
code:
  title_pattern: [X-for-Y, X-with-Y]
  abstract_moves: [context, context, gap, context, aim, method, method, method, method, theory, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 9
  intro_moves: [field, tech, gap, aim, prior, prior, gap, contrib, roadmap]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [consider, formulate, identify, verify]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: table
  gap_type: [combination, new-scenario]
  motivating_figure: true
  problem_class: stochastic
  solution: [lyapunov, closed-form, bisection]
  theory_role: central
  proofs_location: mixed
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [time, control-parameter, task-arrival-probability, harvesting-rate, deadline, distance]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Dynamic [问题] for [系统] With [新器件]"，10 词。和上一篇一样，新意在 "With Energy Harvesting Devices" 这个限定语。
- "Dynamic" 预告了方法（在线 / 随机优化），不是空洞形容词。

## 2. 摘要（11 句，255 词，偏长）
1–2. context：MEC 是新范式；卸载能改善时延。
3. gap："Nevertheless, as the on-device battery capacities are limited, computation would be interrupted …"
4. 动机：引出 EH 是必要的（"it is of significant importance to …"）。
5. aim："In this paper, we will investigate … and develop …"（将来时，这个作者组的习惯）。
6–9. method：性能指标 → 算法名（LODCO）及其联合决策的三个变量 → 卖点（不需要分布信息）→ 每时隙闭式解或二分。
10. theory："shown to be asymptotically optimal via rigorous analysis"。
11. result："Sample simulation results shall be presented to corroborate …"，没有任何数字。
- 摘要用了一句专门讲算法"独特优势"（"A unique advantage of this algorithm is that …"），把卖点单独成句。

## 3. 引言逻辑（4 段正文 + A. Related Works 3 段 + B. Contributions）
1. 领域：IoT 应用增长 vs 设备资源受限（"the tension between … becomes the bottleneck"）。
2. 技术：MEC 对比传统远端云（"In contrast, MEC has the potential to …"）。
3. 空白 + 方向：电池导致卸载性能受损；大电池 / 频繁充电都不可行（逐个否定替代方案）→ EH 是 "a promising technology"。
4. 目标："While MEC with EH devices opens new possibilities …, it also brings new design challenges." → "In this paper, we will develop new design methodologies …"
5–6. 相关工作按两条线写：计算卸载（每篇一句"在 [x] 中做了 y"，最后用 "Nevertheless, these works assume …" 指出共同假设的缺陷）；EH 通信系统。
7. 关键的"为什么不能直接套用"段："The design principles for MEC systems with EH devices are different from those for EH communication systems or MEC systems with battery-powered devices." 然后 "On one hand … On the other hand …" 分别和两条线对比。
8. 贡献：4 条 bullet（模型 / 问题与算法 / 结构性质与性能分析 / 仿真），每条都较长，含方法细节。
9. 路线图："The organization of this paper is as follows."
- 记号：Table I "Summary of Key Notations"。

## 4. Idea 是怎么提出的
- 空白类型：组合 + 新场景。MEC 和 EH 各自成熟，组合后目标函数变了（"the design objective is shifted from minimizing the battery energy consumption to optimizing the computation performance, as the harvested energy comes for free"）。
- 写法亮点：用一个专门段落论证"两条已有研究线都不能直接用"，这是组合型 idea 的标准防御。
- Fig. 1 是系统模型图（模型节开头）。

## 5. 科研方法
- 模型：单用户 + MEC 服务器，时隙化；本地执行（DVFS）、边缘执行（功率控制）、EH 能量包到达模型。
- 问题：执行代价最小化（时延 + 任务丢弃惩罚），高维 MDP，难解。
- 求解：Lyapunov 优化（drift-plus-penalty + 加权扰动方法），把随机问题化为每时隙确定性问题；每时隙闭式解或二分。
- 理论很重：1 定理 + 6 引理 + 4 命题 + 4 推论 + 2 定义 + 3 remark；主结果是渐近最优性（性能界随 V 变紧）。证明正文和附录都有。
- 先证一个结构性质（各 CPU 周期最优频率相同）来降维，是常见的"先找最优解结构再设计算法"套路。

## 6. 仿真与实验
- 参数直接写在第一段正文里，没有参数表。
- 3 个 baseline，均为 greedy 能量分配策略，命名为 "Mobile Execution (GD)" 这种描述 + 缩写标签。
- 结果分两部分："Theoretical Results Verification"（验证定理）+ "Performance Evaluation"（扫参数）。
- 横轴：时间、控制参数 V、任务到达概率、EH 速率、截止时间、距离。
- 结果句："We see from Fig. 3(a) that …, which verifies the asymptotic optimality developed in Theorem 1."（结果明确回扣定理）。

## 7. 图表
- 7 图 1 表（记号表）。Fig. 1 系统模型，其余为结果。
- caption 是描述型："System performance vs. EH rate, the solid curves correspond to ρ=0.6 and the dash-solid curves correspond to ρ=0.4."，交代线型含义但不给结论。

## 8. 句式库
- 张力句："the tension between resource-limited devices and computation-intensive applications becomes the bottleneck for …"
- 否定替代方案："This can possibly be overcome by using larger batteries … However, using larger batteries … implies increased hardware cost, which is not desirable."
- 新挑战："While MEC with EH devices opens new possibilities for cloud computing, it also brings new design challenges."
- 指出共同假设："Nevertheless, these works assume non-adjustable processing capabilities of the central processing units (CPUs) at the mobile devices, …"
- 卖点单句："A unique advantage of this algorithm is that the decisions depend only on the current system state …"
- 解释结构结果："It can be seen from Proposition 2 that the optimal CPU-cycle frequency is chosen by balancing …"

## 9. 结论
- 1 段 224 词：用过去时复述（investigated / was adopted / was developed / We found）→ 主要发现（单调性、渐近最优）→ 仿真结论（定性）→ 意义（"Our study provides a viable approach to …"）→ 两个具体扩展方向（"It would be interesting to extend …"）。
