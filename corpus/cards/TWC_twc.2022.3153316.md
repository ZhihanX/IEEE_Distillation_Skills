---
doi: 10.1109/twc.2022.3153316
title: "Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing"
journal: TWC
year: 2022
band: 2022-2025
cites: 474
cites_per_year: 115.8
article_type: research
topic: UAV
source: xplore-html
xplore: 9725258
auto:
  words_total: 6029
  n_sections: 5
  n_subsections: 14
  n_figures: 14
  n_tables: 2
  n_display_eq: 33
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 22.8
  we_per_1k: 3.7
  title_words: 12
  abstract_words: 189
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 1, contribList: 1, roadmap: 1, however: 6, transition: 31, resultsShow: 0, motivatedBy: 0, toAddress: 8, gapWord: 1, nonconvex: 4, npHard: 0, closedForm: 0, outperform: 1, intensifier: 1, worthNoting: 0, observe: 4, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 3, promising: 0, gen: 0, contrast: 3, firstTime: 0, novel: 0, weProposeFirst: 0, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 7, penalty: 5, convergence: 4, DNN: 3, DRL: 2, convexOpt: 2, gameTheory: 1}
code:
  title_pattern: [X-for-Y, X-in-Y]
  abstract_moves: [context, context, aim, aim, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper    # 被动式："… is investigated in this paper."
  intro_paragraphs: 6
  intro_moves: [field, tech, gap, prior, contrib, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [investigate, formulate, conduct]
  contrib_quantified: false
  first_claim: true                 # 贡献列表中："Cooperative MADRL method for this scenario has never been investigated."
  roadmap: true
  notation: none
  gap_type: [limitation, tool-transfer]
  motivating_figure: true
  problem_class: learning
  solution: [DRL]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: false       # 只有训练曲线
  sim_param_table: true             # Table I 网络参数 + Table II 超参数
  baselines_n: 5                    # 含两个退化版本 MATD3-FP / MATD3-FH 与随机策略等
  baseline_naming: acronym
  x_axes: [episodes, location-map, bandwidth, computation-capacity, number-of-UAVs, weight, arrival-rate, transmit-power]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[学习方法] for [任务] in [场景]"，12 词。方法全称在前（Multi-Agent Deep Reinforcement Learning），场景 "UAV-Assisted Mobile Edge Computing" 在后——"工具 for 问题 in 场景"三段式。

## 2. 摘要（8 句，189 词）
- 两句背景（MEC 降低时延；UAV 作辅助边缘云）→ "Considering the limited computation and energy capacities of UAVs, a collaborative mobile edge computing system with multiple UAVs and multiple ECs is investigated in this paper."（被动式锚点，把动机放在句首状语）。
- 目标与变量 → "Moreover, to solve the above non-convex optimization problem, a Markov decision process is formulated …" → 多智能体 DRL → "Considering the high-dimensional continuous action space, the twin delayed deep deterministic policy gradient algorithm is exploited."（"Considering X, Y is adopted" 解释算法选择）。
- 结果一句："… can achieve better performance compared with the other optimization approaches."。无数字；全摘要无 "we"（we_per_1k 3.7，语料中很低）。

## 3. 引言逻辑（6 段，约 790 词）
1. 计算密集应用 → "However, these tasks may impose a great challenge on user equipment …" → MEC。
2. "Nevertheless, there is still a challenging issue …"（On one hand 偏远地区 / On the other hand 热点）→ "Fortunately, …" UAV 作"flying MEC servers"。
3. 已有 UAV-MEC 工作（轨迹、资源、卸载）→ "However, most existing works considered the scenario of single UAV for computation offloading." → 多 UAV 多 EC → 静态用户假设不现实 → 变量耦合 → 非凸 + 非平稳环境难以求全局最优。
4. RL 在 UAV-MEC 中的应用逐条罗列 → "However, if the number of UAVs or UEs or ECs is large, the state … and action … may grow exponentially, leading to the poor convergence efficiency."
5. "To deal with the above challenges, this paper investigates …" → 3 条 bullet 贡献（含 "has never been investigated" 式首创）。
6. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（单 UAV、静态用户；单智能体 RL 状态动作空间爆炸）+ 工具迁移（多智能体 TD3 应对高维连续动作）。
- 写法：每个设计选择都以 "Considering …" 引出理由（能力有限 → 多 UAV 协作；连续动作空间 → TD3；环境非平稳 → 集中训练分布执行）。
- 优化问题非凸 → 不求解析解，直接改写为 MDP——DRL 论文的标准过渡句式。

## 5. 科研方法
- 模型：M 个 UE（周期性任务三元组：数据量、CPU 周期、到达率）、N 个 UAV、K 个 EC；UAV 运动约束（速度、高度、区域、不重叠、防碰撞）→ G2A 上行 → UAV 计算 → A2G 转发到 EC → EC 计算；系统代价 = 时延与能耗的加权和。
- MDP：智能体 = 每个 UAV；状态 = UAV 3D 位置；动作 = 水平距离、方向角、垂直距离、发射功率、任务划分比例；奖励含约束违反惩罚（penalty）。
- 算法：合作式 MATD3（共享总奖励、集中训练分散执行、双 critic、目标策略平滑噪声、经验回放、延迟更新），Algorithm 1；网络输入输出规模给出复杂度。

## 6. 仿真与实验
- 节名 "Performance Evaluation"；400 m × 400 m、2 EC、2 UAV、30 UE 分布在两个热点（Fig. 4）；Table I 环境参数 + Table II 超参数（两层隐藏层 400/300 神经元）。
- 先训练效率（训练曲线、学到的 UAV 位置、任务划分比例），再与 5 种方法比较（含两个退化版：固定功率 MATD3-FP、固定高度 MATD3-FH，以及随机策略），固定用户与移动用户两种场景。
- 横轴：带宽、UAV 计算能力、UAV / UE 数（可扩展性）、权重 w_2（能耗-时延权衡）、任务到达率、最大发射功率。

## 7. 图表
- 14 图 2 表 1 算法。Fig. 1 系统图、Fig. 2 UAV 坐标示意（caption 与 Fig. 1 相同，疑似笔误）、Fig. 3 MATD3 框架图。结果 caption 为 "Total system cost with different …" 式短标签。

## 8. 句式库
- 挑战转折："However, these tasks may impose a great challenge on user equipment (UE), which have a limited computation and battery capabilities."
- 引出新载体："Fortunately, due to the advantages of flexible deployment and large coverage, unmanned aerial vehicles (UAVs) have been applied to assist MEC systems …"
- 单 UAV 局限："However, most existing works considered the scenario of single UAV for computation offloading."
- 规模爆炸："However, if the number of UAVs or UEs or ECs is large, the state … and action … may grow exponentially, leading to the poor convergence efficiency."
- 算法选择理由："Considering the high-dimensional continuous action space, the twin delayed deep deterministic policy gradient algorithm is exploited."
- 承接："To deal with the above challenges, this paper investigates the collaborative UAV-assisted MEC systems, …"
- 补充（skill 引用）："Similar to [24], [26], [27], assume that the ground UEs can communicate with their serving UAV via the orthogonal frequency-division multiple access."

## 9. 结论
- 1 段 127 词（偏短），全部过去时被动 / "This paper investigated …"，逐句对应摘要；无数字、无未来工作。
