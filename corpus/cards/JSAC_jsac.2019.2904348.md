---
doi: 10.1109/jsac.2019.2904348
title: "Adaptive Federated Learning in Resource Constrained Edge Computing Systems"
journal: JSAC
year: 2019
band: 2019-2021
cites: 2014
cites_per_year: 274.3
article_type: research
topic: federated-edge-learning
source: xplore-html
xplore: 8664630
auto:
  words_total: 10200
  n_sections: 8
  n_subsections: 26
  n_figures: 11
  n_tables: 2
  n_display_eq: 24
  n_algorithms: 3
  statements: {theorem: 2, lemma: 2, proposition: 2, corollary: 0, definition: 1, assumption: 1, remark: 1, proof: 6, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.5
  we_per_1k: 13.7
  title_words: 9
  abstract_words: 197
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 12, contribList: 1, roadmap: 0, however: 7, transition: 2, resultsShow: 0, motivatedBy: 0, toAddress: 0, gapWord: 0, nonconvex: 2, npHard: 0, closedForm: 2, outperform: 0, intensifier: 0, worthNoting: 0, observe: 8, thisIsBecause: 1, asExpected: 1, insight: 1, tradeoff: 3, figVerb: 0, promising: 1, gen: 0, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 5, wlog: 0, code: 0, prototype: 10}
  methods: {convergence: 20, complexity: 5, DNN: 5}
code:
  title_pattern: [X-in-Y]
  abstract_moves: [context, context, gap, aim, aim, theory, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 5
  intro_moves: [field, gap, aim, approach, contrib]
  related_work: separate-section
  contrib_format: numbered
  contrib_n: 3
  contrib_verbs: [analyze, propose, evaluate]
  contrib_quantified: false
  first_claim: true
  roadmap: false
  notation: table
  gap_type: [new-scenario, theory-gap, limitation]
  motivating_figure: true
  problem_class: learning
  solution: [bound-surrogate, heuristic]
  theory_role: central
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [aggregation-interval, number-of-nodes, aggregation-time, time-budget, time, control-parameter]
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: true
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Adaptive [方法] in [资源受限的场景]"，9 词。形容词 "Adaptive" 就是方法核心（自适应聚合频率），"Resource Constrained" 点明约束。

## 2. 摘要（8 句，197 词）
1–2. context：边缘产生大量数据；ML 模型从数据中训练。
3. gap："Due to bandwidth, storage, and privacy concerns, it is often impractical to send all the data to a centralized location."
4. aim："In this paper, we consider the problem of learning model parameters from data distributed across multiple edge nodes, …"
5. 范围："Our focus is on a generic class of machine learning models that are trained using gradient-descent-based approaches."（先划定适用范围，增强普适性）
6. theory → method："We analyze the convergence bound … based on which we propose a control algorithm …"（理论→算法的因果链写在一句里）。
7–8. result：原型 + 大规模仿真，"performs near to the optimum"，无数字。

## 3. 引言逻辑（5 段，约 640 词，偏短）
1. 领域：边缘数据爆炸 + 隐私 / 带宽 → 本地处理（给出 "over 90%" 预测数字）→ MEC。
2. 趋势与难点：ML 将成为 MEC 主要负载；段末 "However, it is challenging to perform distributed machine learning on resource-constrained MEC systems."
3. 目标："In this paper, we address the problem of how to efficiently utilize the limited computation and communication resources at the edge for the optimal learning performance." 并引入 Fig. 1 和"联邦学习"这个名字。
4. 机制：讲清"本地更新 / 全局聚合"两种步骤及各自消耗的资源，落到"there is a complex relationship among …"——把研究问题具体化为一个可调参数（聚合频率）。
5. 贡献：一句话说算法 + 为何重要（"This is important because …"）→ 3 条编号贡献（analyze / propose / evaluate）。
- 无路线图句；相关工作单列一节，末尾 "In contrast to the above research, our work in this paper formally addresses …"。
- 记号：Table II "Summary of Main Notations"。

## 4. Idea 是怎么提出的
- 空白：已有收敛界只允许一步本地更新（理论缺口）；已有自适应方案是经验设计、没有理论目标（局限）；边缘资源受限（新场景）。
- 核心洞见：把"多久聚合一次"变成一个可优化的控制变量，用收敛界做替代目标来选它。
- 首创说法："To the best of our knowledge, the adaptation of global aggregation frequency for federated learning with resource constraints has not been studied in the literature."

## 5. 科研方法
- 先 "Preliminaries and Definitions"（损失函数、学习问题、分布式梯度下降 Algorithm 1），再 "Problem Formulation"（资源预算约束下最小化损失）。
- 理论：假设（凸、Lipschitz、光滑）→ 定义梯度散度 δ 刻画 non-i.i.d. → Theorem 1/2 收敛界 → Proposition 1/2 说明近似解的性质。
- 算法：用界近似目标，在线估计参数，每次聚合重算 τ*；给出复杂度 O(K(NM+τ_max))；再扩展到 SGD。

## 6. 仿真与实验
- 原型（3 台树莓派 + 2 台笔记本，Wi-Fi）+ 仿真（5–500 节点），4 种模型 × 5 个数据集 × 4 种数据分布 case。
- 3 个 baseline：集中式 GD、固定 τ 的经典联邦学习、τ=1 的同步分布式 GD——都是"本方法的特例"，用 "which is equivalent to … in our setting" 点明。
- "For a fair comparison, we implement … for all baselines"——专门交代公平性。
- 结果小节按变量编号（1)–7)）：节点数、聚合时间、时间预算、瞬时行为、参数敏感性、同步 vs 异步。

## 7. 图表
- 11 图 2 表 3 算法。Fig. 1 系统架构（引言）。
- caption 大多短标签（"SVM (SGD) with different numbers of nodes."），但 Fig. 4 是自含结论的长 caption（说明本方法的点接近最优）。

## 8. 句式库
- 研究问题："In this paper, we address the problem of how to efficiently utilize the limited … resources at the edge for the optimal learning performance."
- 重要性："This is important because the training of machine learning models is usually resource-intensive, …"
- 和相关工作切割："In contrast to the above research, our work in this paper formally addresses the problem of …"
- 自然的问题："Therefore, a natural question is how to make efficient use of a given amount of resources to minimize …"
- 解释结果："This is because the model tends overfit the datasets on the faster nodes, …"
- 结果预期："As expected, the gradient deviation δ is larger for Cases 2 and 4 where …"

## 9. 结论
- 1 段 120 词，现在完成时（"we have focused / have analyzed / has been proposed"），无数字，两条未来工作（异构资源、非凸损失的收敛分析）。
