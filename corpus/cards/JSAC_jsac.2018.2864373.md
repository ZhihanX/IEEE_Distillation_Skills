---
doi: 10.1109/jsac.2018.2864373
title: "Energy-Efficient UAV Control for Effective and Fair Communication Coverage: A Deep Reinforcement Learning Approach"
journal: JSAC
year: 2018
band: 2016-2018
cites: 600
cites_per_year: 74.2
article_type: research
topic: UAV
source: xplore-html
xplore: 8432464
auto:
  words_total: 4734
  n_sections: 8
  n_subsections: 8
  n_figures: 7
  n_tables: 2
  n_display_eq: 8
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 22.9
  we_per_1k: 16.0
  title_words: 14
  abstract_words: 212
  abstract_sentences: 9
  phrases: {toTheBest: 1, inThisPaper: 3, contribList: 0, roadmap: 1, however: 5, transition: 8, resultsShow: 0, motivatedBy: 0, toAddress: 2, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 2, intensifier: 2, worthNoting: 0, observe: 2, thisIsBecause: 4, asExpected: 1, insight: 0, tradeoff: 1, figVerb: 3, promising: 1, gen: 0, contrast: 2, firstTime: 0, novel: 6, weProposeFirst: 2, wlog: 0, code: 0, prototype: 0}
  methods: {DNN: 9, penalty: 4, DRL: 3}
code:
  title_pattern: [X-for-Y, colon-subtitle]
  abstract_moves: [context, context, gap, gap, gap, aim, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 5
  intro_moves: [field, tech, gap, solution, contrib, roadmap]
  related_work: separate-section
  contrib_format: paragraph
  contrib_n: 2
  contrib_verbs: [present, justify]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: table
  gap_type: [tool-transfer, new-scenario]
  motivating_figure: true
  problem_class: learning
  solution: [DRL, DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [coverage-range, number-of-UAVs, energy-ratio, time, hyperparameters]
  fig1_role: scenario
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "Energy-Efficient [控制] for [目标 A] and [目标 B]: A Deep Reinforcement Learning Approach"，14 词。冒号后是方法类副标题（"A … Approach"），点明这是工具迁移型论文。

## 2. 摘要（9 句，212 词）
- 前两句 UAV 作为空中基站的用途；"However, UAVs have limited communication ranges and energy resources." 后接一句具体化 + "It is thus challenging to …"——三句讲难点。
- "Toward this end, we propose to leverage emerging deep reinforcement learning (DRL) for UAV control and present a novel and highly energy-efficient DRL-based method, which we call …"——给方法起缩写名（DRL-EC3）。
- 方法三点用 1) 2) 3) 内嵌列出 → "We conduct extensive simulations for performance evaluation." → 优于两个常用基准。无数字。

## 3. 引言逻辑（5 段，约 810 词，较短）
1. UAV 作空中基站 + 真实事件例子（2011 年东日本大地震中的救援通信）。
2. 两个好处（First / Second）。
3. 任务难点（Fig. 1 场景图在此）：通信范围与能量有限、网关少 → First（覆盖需移动 + 公平性）/ Second（能量）/ 连通性。
4. "To address the above issues, we propose to leverage emerging deep reinforcement learning (DRL) …" → 为什么是 DRL（"We believe DRL provides a promising solution because …"）→ 直接用 DRL 的困难（DQN 只能离散动作 → 选 DDPG；多目标 + 连通约束）→ "it remains unknown if it can succeed on control tasks in complex communication networks" → 首创声明 → 方法名与贡献（散文）。
5. 路线图（与实际章节顺序不一致：路线图说 Section II 是系统模型，实际 Section II 是 Related Work）。

## 4. Idea 是怎么提出的
- 空白类型：工具迁移（DRL / DDPG 用于 UAV 连续控制）+ 新场景（长期覆盖 + 公平 + 能耗 + 连通）。
- 写法亮点：迁移型论文主动交代"为什么不能直接用"——动作空间连续、多目标、连通约束——让迁移本身成为贡献；用 "it remains unknown if it can succeed …" 把"能否迁移"包装成开放问题。
- 单列 Related Work 节，末尾用两条 bullet 总结差异（"None of them have carefully addressed energy efficiency …"、"Unlike a static UAV deployment problem …, dynamic UAV control is studied here."）。

## 5. 科研方法
- 模型：网格化区域、PoI 覆盖分数、Jain 公平指数、能耗（飞行 + 悬停）、连通性；问题陈述用 1)–4) 列出四个目标而非数学优化问题。
- 单列 "Preliminaries" 节介绍 RL / DQN / DDPG 背景。
- DRL-EC3：状态（覆盖分数、覆盖状态、UAV 位置）、动作（方向 + 距离）、奖励（公平 × 覆盖增量 / 能耗，越界与断连给罚项）编号列出；actor-critic 网络结构（400/300 神经元）写明；算法按行号解释（"The second part (Lines 8–20) is exploration."）。
- 全文仅 8 个显示公式，无定理。

## 6. 仿真与实验
- 参数写在正文（10×10 单位区域）；4 个指标（平均覆盖分数、公平指数、归一化能耗、能效）与 2 个基准（Random、Greedy）都用 bullet 定义。
- 每张图之后用编号列表写观察，且每条观察带具体数字（"…, DRL-EC3 achieves an energy efficiency of 1.43, compared to 0.80 given by the best baseline, …"）。
- 收敛（累计奖励曲线）+ Table II 超参数影响。
- 单列 "Discussions" 节：去中心化多智能体、可扩展性。

## 7. 图表
- 7 图 2 表。Fig. 1 场景图在引言。结果图均为 (a)(b)(c) 三联子图，caption 写 "The impact of X on (a) …, (b) …, and (c) …"。

## 8. 句式库
- 真实事件动机："For example, in 2011 Great East Japan earthquake, some people were trapped in broken down houses or otherwise cut-off areas, …"
- 方法选择信念："We believe DRL provides a promising solution because it can well handle a sophisticated state space and time-varying environment; …"
- 迁移困难："However, it is not straightforward to solve the UAV control problem using DRL."
- 开放问题："Even though DRL has made remarkable successes on a few game-playing tasks, it remains unknown if it can succeed on control tasks in complex communication networks, …"
- 首创："To the best of our knowledge, we are the first to leverage DRL for enabling energy-efficient UAV control in the context of providing communication coverage for ground users."
- 方法命名："… present a novel and highly energy-efficient DRL-based method, which we call DRL-based energy-efficient control for coverage and connectivity (DRL-EC3)."

## 9. 结论
- 1 段 105 词（很短），过去时复述 + 重复摘要结果句，列出四个指标名。无数字、无未来工作。
