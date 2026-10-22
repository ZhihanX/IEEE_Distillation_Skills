---
doi: 10.1109/jsac.2018.2815360
title: "Task Offloading for Mobile Edge Computing in Software Defined Ultra-Dense Network"
journal: JSAC
year: 2018
band: 2016-2018
cites: 1019
cites_per_year: 118.6
article_type: research
topic: MEC-offloading
source: xplore-html
xplore: 8314696
auto:
  words_total: 4692
  n_sections: 6
  n_subsections: 12
  n_figures: 5
  n_tables: 3
  n_display_eq: 24
  n_algorithms: 1
  statements: {theorem: 1, lemma: 1, proposition: 0, corollary: 0, proof: 2, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.0
  we_per_1k: 14.4
  title_words: 11
  abstract_words: 176
  abstract_sentences: 8
  phrases: {toTheBest: 2, inThisPaper: 9, contribList: 1, roadmap: 1, however: 7, transition: 8, resultsShow: 1, motivatedBy: 0, toAddress: 5, gapWord: 0, nonconvex: 0, npHard: 5, closedForm: 0, outperform: 0, intensifier: 0, worthNoting: 0, observe: 1, thisIsBecause: 2, asExpected: 0, insight: 1, tradeoff: 1, figVerb: 1, promising: 0, gen: 3, contrast: 0, firstTime: 1, novel: 1, weProposeFirst: 4, wlog: 0, code: 0, prototype: 0}
  methods: {KKT: 1, convexOpt: 1, convergence: 2, complexity: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, context, gap, aim, method, method, method, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, tech, gap, solution, approach, roadmap]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [propose, present, conduct]
  contrib_quantified: true
  first_claim: true
  roadmap: true
  notation: table
  gap_type: [combination, new-architecture]
  motivating_figure: true
  problem_class: MINLP
  solution: [decomposition, AO, KKT, relaxation]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: false
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [computation-amount, data-size]
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Task Offloading for [技术] in [新架构]"：问题 + for + 技术 + in + 场景，11 词，无冒号、无缩写。
- 新意全在场景限定语 "Software Defined Ultra-Dense Network" 上，问题名本身很普通。

## 2. 摘要（8 句）
1. context：新应用 → 计算密集且时延敏感。
2. context：UDN 中的 MEC 被看作解决方案。
3. gap："However, … makes it challenging to offload tasks for users."
4. aim："In this paper, leveraging the idea of software defined network, we investigate the task offloading problem …"（锚点句 + 借用的思想 + 目标"最小化时延同时省电"）。
5–7. method：建模为 NP-hard 的 MINLP → 拆成两个子问题 → 提出方案。用 "Specifically," "In order to solve it," "Based on …" 串起三步。
8. result：给出 20% 时延、30% 能耗两个数字，并点名两个 baseline。

## 3. 引言逻辑（6 段，约 980 词）
1. 领域：设备与流量增长（带预测数字和引用）→ 应用受限于终端算力与电量 → 需要计算卸载。
2. 技术：UDN 是 5G 关键技术，MEC 被提出；用 (i)(ii) 列出 MEC 的两个优点。
3. 空白：MEC 与 UDN 的研究彼此分离；用 (i)(ii) 列出两个挑战，落到"需要一个控制器"。
4. 方案：SDN 作为新范式 → "to the best of our knowledge, there is no exiting work on …" → 本文提出 SD-UDN，指向 Fig. 1。
5. 方法与结果：MINLP、NP-hard、拆分、交替优化，提前给出 20%/30%，以 "In summary, the main contributions of this paper include:" 引出 3 条贡献。
6. 路线图："The remainder of this paper is organized as follows."
- 相关工作单列一节（4 段），节末用 "Taking into account the limitations of existing work, in this paper, we …" 回扣本文；另有 Table I 对比已有卸载方案。
- 贡献 3 条：框架（propose）/ 算法（present）/ 实验（conduct，含数字）。
- 记号放在模型节的 Notation Table（Table II）。

## 4. Idea 是怎么提出的
- 空白类型：组合型。MEC 和 UDN 各自成熟，但"most of the existing work on ultra dense network and mobile edge computing are separate"；再借第三个领域（SDN）的集中控制把两者接起来。
- 核心洞见：把控制面从分散的小基站解耦、集中到宏基站上的 SD-UDN 控制器，从而拿到全局信息做卸载决策。
- Fig. 1 在引言里就出现，画三层架构（用户面 / 数据面 / 控制面）。

## 5. 科研方法
- 系统模型：n 个密集小基站各带边缘云；本地计算模型 + 边缘计算模型（CPU 周期、上传速率），忽略回传时延（"Similar to many studies such as [18] and [36], we ignore …"，借文献给假设背书）。
- 问题：在电池能耗约束下最小化平均任务时延；MINLP，正文证明 NP-hard。
- 求解：固定卸载决策后资源分配是凸问题（Lemma 1）→ KKT 得最优解（Theorem 1）；任务放置是 0-1 规划，引入连续变量迭代求解；两者交替。
- 理论：1 个引理 + 1 个定理，证明都在正文；单列 "Convergence Analysis" 小节，无复杂度分析。

## 6. 仿真与实验
- 参数表 Table III；任务计算量和数据量按正态 / 均匀 / Pareto 分布生成。
- baseline 2 个：random offloading、uniform offloading，按方案描述命名，并在正文列表中逐条说明其两步做法。
- 横轴：计算量、数据量；每张图分 (a)(b)(c) 三种分布。
- 结果段写法："As shown in Fig. 2 and Fig. 3, we can conclude that the larger …" → 再给相对 baseline 的百分比 → "This is because …" 解释。

## 7. 图表
- 5 图 3 表。Fig. 1 架构图在引言；Fig. 2–5 全是结果图。
- caption 很短，只是标签："Impact of computation amount on task duration."，不含结论。
- 表：方案对比表（相关工作）、符号表、仿真参数表。

## 8. 句式库
- 指出空白："However, at present, most of the existing work on ultra dense network and mobile edge computing are separate."
- 首创声明："To the best of our knowledge, this is the first study of task offloading for mobile edge computing in SD-UDN."
- 引出贡献："In summary, the main contributions of this paper include:"
- 用文献背书假设："Similar to many studies such as [18] and [36], we ignore the transmission delay …"
- 解释结果："This is because the data size after task processing is generally smaller than it before processing, …"

## 9. 结论
- 1 段 99 词：重述架构与方案 → 再次首创声明 → 优于 baseline（不给数字）→ 一句未来工作（用户移动性）。
- 注意：原文有语法错误（"exiting work"、"a efficient"），高引不代表文字精良；这篇的价值在选题时机和问题组合。
