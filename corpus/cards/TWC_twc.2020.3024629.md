---
doi: 10.1109/twc.2020.3024629
title: "A Joint Learning and Communications Framework for Federated Learning Over Wireless Networks"
journal: TWC
year: 2021
band: 2019-2021
cites: 1318
cites_per_year: 228.9
article_type: research
topic: federated-edge-learning
source: xplore-html
xplore: 9210812
auto:
  words_total: 7576
  n_sections: 6
  n_subsections: 14
  n_figures: 10
  n_tables: 2
  n_display_eq: 36
  n_algorithms: 1
  statements: {theorem: 1, lemma: 1, proposition: 2, corollary: 0, proof: 4, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 25.0
  we_per_1k: 11.3
  title_words: 12
  abstract_words: 306
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 2, roadmap: 1, however: 8, transition: 4, resultsShow: 1, motivatedBy: 0, toAddress: 4, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 2, outperform: 0, intensifier: 3, worthNoting: 0, observe: 22, thisIsBecause: 5, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 6, promising: 1, gen: 0, contrast: 4, firstTime: 1, novel: 3, weProposeFirst: 0, wlog: 0, code: 0, prototype: 0}
  # 首创句写作 "To our best knowledge, this is the first work …"，toTheBest 正则不匹配这种变体，由 firstTime 计入
  methods: {convergence: 25, complexity: 4, DNN: 2}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, context, gap, context, aim, theory, method, method, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper
  intro_paragraphs: 4
  intro_moves: [field, gap, prior, gap, contrib, roadmap]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, formulate, derive, analyze]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: table
  gap_type: [limitation, combination]
  motivating_figure: true
  problem_class: MINLP
  solution: [bound-surrogate, closed-form, reformulation]
  theory_role: central
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [data-samples, number-of-users, iterations, number-of-RBs]
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "A Joint [A] and [B] Framework for [任务] Over [网络]"，12 词。"Joint … Framework" 宣告跨层（学习 × 通信）定位；以冠词 A 开头的名词短语标题。

## 2. 摘要（9 句，306 词，偏长）
- "In this article, the problem of training federated learning (FL) algorithms over a realistic wireless network is studied."——被动锚点，"realistic" 暗示已有工作不现实。
- 第 2–4 句交代模型并直接点出无线因素如何影响训练（包错误、资源有限 → 需选用户）。
- 方法三步：先推导期望收敛速率闭式（"to quantify the impact of wireless factors on FL"）→ 给定选择 / RB 下求最优功率 → 优化用户选择与 RB。
- 末句数字 + 在摘要里逐个定义 3 个基准："… can improve the identification accuracy by up to 1.4%, 3.5% and 4.1%, respectively, compared to: 1) …, 2) …, and 3) …"。

## 3. 引言逻辑（4 段，约 780 词，较短；内分 A. Related Works / B. Contributions）
1. 集中式学习 → 隐私与通信资源 → 分布式学习 → FL → "However, to train an FL algorithm over a wireless network, the users must transmit the training parameters over wireless links which can introduce training errors, …"
2. （A 小节，一大段）已有 FL 工作逐篇一句 → "While interesting, these prior works [5] and [11]–[18] assumed that wireless networks can readily integrate FL algorithms. However, in practice, …" → 包错误、带宽限制用户数、能量与时延 → 需要选用户 → 再批评研究过通信层面的工作 "these works are limited in several ways. First, … Meanwhile, … However, …"。
3. （B 小节）"The main contribution of this article is, thus, a novel framework …" + 首创声明（"To our best knowledge, this is the first work that provides a comprehensive study of the connection between …"）+ 4 条 bullet。
4. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：已有工作局限（默认无线网络可直接承载 FL）+ 组合（学习性能 × 无线资源联合优化）。
- 写法亮点：用 "While interesting, these prior works … assumed that …" 先肯定再指出隐含假设；对"部分相关"的工作单独再批一轮（只停留在高层讨论 / 没考虑包错误 / 只研究三种固定调度策略）——两轮批评层层收窄到本文。
- 跨层目标：优化目标直接是 FL 损失函数，而不是速率或误包率；用推导的收敛上界把学习指标与无线参数连接起来。

## 5. 科研方法
- 模型：机器学习模型（本地 / 全局更新）→ OFDMA 传输（每用户一个 RB）→ 包错误率（出错的本地模型被丢弃）→ 能耗（传输 + 训练）→ 问题：最小化训练损失，约束时延与能耗。
- 理论：Lipschitz、强凸等假设（编号列出）→ Theorem 1 期望收敛速率上界（含包错误项）→ Proposition 1 收敛条件 → Lemma 1 无包错误时的对照结果。
- 优化：只需最小化上界中的"间隙项"→ Proposition 2 最优功率闭式 → 化为二分图匹配，用匈牙利算法求最优用户选择与 RB 分配 → 复杂度分析。
- 主要证明在附录。

## 6. 仿真与实验
- Table II 系统参数；两个任务：线性回归（合成数据，Fig. 3 给可视化例子）与 MNIST 手写数字识别（Fig. 10 给识别例子）。
- 三个基准在正文用 a) b) c) 定义：最优用户选择 + 随机资源、标准 FL（随机选择与分配）、只最小化误包率而不看 FL 参数的无线优化。
- 结果：训练损失 vs 样本数、匈牙利算法迭代次数 vs 用户数、收敛间隙、识别精度 vs 迭代 / 用户数 / RB 数。

## 7. 图表
- 10 图 2 表 1 算法。Fig. 1 FL-无线架构，Fig. 2 FL 学习流程。Table I 是记号表。caption 短标签，统一写成 "… as the … varies" 句式。

## 8. 句式库
- 无线带来的问题："However, to train an FL algorithm over a wireless network, the users must transmit the training parameters over wireless links which can introduce training errors, …"
- 隐含假设："While interesting, these prior works … assumed that wireless networks can readily integrate FL algorithms."
- 必要性："In practice, to effectively deploy FL over real-world wireless networks, it is necessary to investigate how the wireless factors affect the performance of FL algorithms."
- 部分相关工作的局限："Here, we note that, although some works … have studied communication aspects of FL, these works are limited in several ways."
- 首创："To our best knowledge, this is the first work that provides a comprehensive study of the connection between the performance of FL algorithms and the underlying wireless network."
- 推导目的："… a closed-form expression for the expected convergence rate of the FL algorithm is first derived to quantify the impact of wireless factors on FL."

## 9. 结论
- 1 段 148 词，现在完成时（have developed / have formulated / have derived）→ "Simulation results have shown that … yields significant improvements in the performance compared to existing implementations of the FL algorithm that do not account for the properties of the wireless channel."。无数字、无未来工作。
