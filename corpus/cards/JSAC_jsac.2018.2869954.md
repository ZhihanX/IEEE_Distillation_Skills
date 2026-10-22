---
doi: 10.1109/jsac.2018.2869954
title: "Follow Me at the Edge: Mobility-Aware Dynamic Service Placement for Mobile Edge Computing"
journal: JSAC
year: 2018
band: 2016-2018
cites: 497
cites_per_year: 62.1
article_type: research      # 顺延补位：替换改记为 overview 的 jsac.2016.2525398（5G-Enabled Tactile Internet）
topic: MEC-offloading
source: xplore-html
xplore: 8463562
auto:
  words_total: 7597
  n_sections: 7
  n_subsections: 21
  n_figures: 7
  n_tables: 1
  n_display_eq: 28
  n_algorithms: 3
  statements: {theorem: 6, lemma: 2, proposition: 0, corollary: 0, definition: 2, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.8
  we_per_1k: 12.3
  title_words: 13
  abstract_words: 212
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 6, contribList: 0, roadmap: 1, however: 8, transition: 18, resultsShow: 0, motivatedBy: 2, toAddress: 7, gapWord: 0, nonconvex: 0, npHard: 5, closedForm: 0, outperform: 0, intensifier: 11, worthNoting: 2, observe: 3, thisIsBecause: 1, asExpected: 0, insight: 0, tradeoff: 11, figVerb: 3, promising: 0, gen: 2, contrast: 1, firstTime: 0, novel: 2, weProposeFirst: 5, wlog: 1, code: 0, prototype: 0}
  methods: {lyapunov: 11, convergence: 10, complexity: 8, penalty: 8, gameTheory: 7, KKT: 1}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [context, gap, gap, aim, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 7
  intro_moves: [field, tech, gap, tech, gap, gap, aim, contrib, roadmap]
  related_work: separate-section
  contrib_format: paragraph
  contrib_n: 3
  contrib_verbs: [propose, design, demonstrate]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: table
  gap_type: [new-scenario, limitation]
  motivating_figure: true
  problem_class: stochastic
  solution: [lyapunov, heuristic, game]
  theory_role: central
  proofs_location: external   # 正文只写 "The detailed proof is given in the technique report [33]."
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 6
  baseline_naming: acronym
  x_axes: [control-parameter, queue-backlog, migration-cost, time, user-density, running-time]
  fig1_role: scenario
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[口语化主标题]: [具体问题] for [系统]"，13 词。"Follow Me at the Edge" 用拟人化短语概括"服务跟随用户迁移"，冒号后才是规范的技术描述——与 "Caching in the Sky" 同属"吸睛主标题 + 说明副标题"。

## 2. 摘要（8 句，212 词）
- MEC 定义 → "However, with the sinking of computing capabilities, the new challenge incurred by user mobility arises: …" → "Tackling this problem is non-trivial since frequent service migration would greatly increase the operational cost."
- "To address this challenge in terms of the performance-cost tradeoff, in this paper, we study …"
- 三步方法：Lyapunov 把长期问题分解为无需先验移动信息的实时问题 → NP-hard → Markov 近似（集中式）→ 最优响应更新（分布式，面向 5G 大规模设备）。
- "Rigorous theoretical analysis and extensive evaluations demonstrate the efficacy of …"。无数字。

## 3. 引言逻辑（7 段，约 930 词）
1. 移动应用增长 → "The tension between resource-hungry applications and resource-limited end devices yields a huge challenge …"
2. 云计算 → "Unfortunately, the long communication latency to the centralized cloud data center (typically hundreds of milliseconds), …, can far exceed the stringent timeliness requirement (typically tens of milliseconds) …"（用数量级对比说明问题）。
3. MEC 的定义与时延优势。
4. "Although …, a new challenge arises by unpredicted user mobility …" → SDN 移动性管理 → 用 Fig. 1 的具体例子（用户从左节点移动到右节点）说明服务必须跟随迁移。
5. "However, the dynamic service profile placement problem is non-trivial. On one hand, … On the other hand, …" → 由此得出两条设计指导："(1) … (2) navigate the performance-cost trade-off in a cost-efficient manner."
6. "Following the above two guidances on dynamic service placement for MEC, in this paper, we propose …"——贡献直接对应上一段的两条指导（散文）。
7. 路线图。相关工作单列一节，末尾声明 "This work significantly extends the preliminary work [1]."，并用 "(1)…(2)…(3)" 写出与最接近工作 [26] 的三点区别。

## 4. Idea 是怎么提出的
- 空白类型：新场景（用户移动下的边缘服务放置）+ 已有方法局限（依赖移动预测或马尔可夫假设）。
- 写法亮点：先用一个具体例子把问题"讲出来"，再用 "On one hand / On the other hand" 把问题拆成两个相互冲突的因素，并总结成两条"设计指导"，方法部分逐条回应——"例子 → 冲突 → 指导 → 方案"的推导链。
- 核心建模选择：长期迁移成本预算（运营商按月 / 年设定）而非逐时隙约束，用 Lyapunov 虚拟队列处理，从而不需要未来信息。

## 5. 科研方法
- 模型：设备级服务模型（每个设备的服务配置放在专用 VM / 容器中）；时延 = 计算时延（节点负载共享）+ 通信时延（传播 + 传输）；迁移成本；长期成本预算下最小化平均时延（Table I 记号）。
- Lyapunov：虚拟成本队列 → 漂移加罚 → 每时隙求解实时问题（Lemma 1）。
- 实时问题 NP-hard（组合性质）→ 集中式 Markov 近似（Algorithm 2，Theorem 2 平稳分布、Theorem 3 最优性间隙）；分布式最优响应更新（Definition 1/2：Nash 均衡与最优响应，Theorem 1 有限步收敛、Theorem 4 近似比）→ Theorem 5/6 与离线最优的长期性能界。
- 所有证明放在技术报告 [33]，正文只给结论。

## 6. 仿真与实验
- ONE 模拟器、赫尔辛基市中心基于最短路径地图的移动模型（trace-driven 风格）；参数写在正文。
- 基准："Always migration"（AM）、不迁移，以及 GM、GRK、GK、FMeC（编号列表定义，各自一句策略描述）。
- 时延-成本权衡（控制参数 V）→ 队列稳定 → 平均迁移成本收敛 → 对系统动态的适应 → 不同用户密度 → 决策运行时间（注明 CPU 型号与 PyCharm 环境）。

## 7. 图表
- 7 图 1 表 3 算法。Fig. 1 用户漫游时动态服务放置示例（引言）。结果 caption 极短（"Queue stability."、"Optimality analysis."），信息放在正文。

## 8. 句式库
- 张力表述："The tension between resource-hungry applications and resource-limited end devices yields a huge challenge for the next generation network development."
- 数量级对比："… the long communication latency to the centralized cloud data center (typically hundreds of milliseconds) … can far exceed the stringent timeliness requirement (typically tens of milliseconds) …"
- 新挑战："Although the computation capacity of a mobile user is dramatically augmented by edge cloud, a new challenge arises by unpredicted user mobility in the wireless network."
- 非平凡："However, the dynamic service profile placement problem is non-trivial. On one hand, … On the other hand, …"
- 指导 → 方案："Following the above two guidances on dynamic service placement for MEC, in this paper, we propose …"
- 与最近工作区分："However, it is worth noting that our work substantially differs from and complements to [26] in at least the following three aspects: …"

## 9. 结论
- 1 段 203 词，一般现在时复述（study / design / utilize / develop / provide）→ 两个具体未来方向（超密网络中的在线网络选择；D2D 协作的联邦边缘云）。无数字。
