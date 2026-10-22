---
doi: 10.1109/tcomm.2017.2787700
title: "Computation Offloading and Resource Allocation in Mixed Fog/Cloud Computing Systems With Min-Max Fairness Guarantee"
journal: TCOM
year: 2018
band: 2016-2018
cites: 470
cites_per_year: 55.2
article_type: research
topic: MEC-offloading
source: xplore-html
xplore: 8240666
auto:
  words_total: 6409
  n_sections: 9
  n_subsections: 20
  n_figures: 12
  n_tables: 2
  n_display_eq: 47
  n_algorithms: 4
  statements: {theorem: 0, lemma: 0, proposition: 3, corollary: 0, remark: 2, proof: 7, proof_in_appendix: 4}
  n_appendix: 1
  mean_sentence_words: 25.2
  we_per_1k: 12.0
  title_words: 14
  abstract_words: 171
  abstract_sentences: 5
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 1, however: 11, transition: 4, resultsShow: 0, motivatedBy: 0, toAddress: 4, gapWord: 0, nonconvex: 4, npHard: 3, closedForm: 0, outperform: 0, intensifier: 0, worthNoting: 0, observe: 3, thisIsBecause: 3, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 3, promising: 1, gen: 0, contrast: 1, firstTime: 0, novel: 1, weProposeFirst: 2, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 13, convergence: 11, SDR: 8, lagrange: 7, bisection: 5, convexOpt: 4, FP: 3, gameTheory: 2, KKT: 1, monteCarlo: 1}
code:
  title_pattern: [X-in-Y, X-with-Y]
  abstract_moves: [context, aim, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, tech, prior, gap, aim, contrib, roadmap, notation]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [formulate, devise, propose, perform]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [limitation, combination]
  motivating_figure: true
  problem_class: MINLP
  solution: [SDR, bisection, FP, lagrangian-dual, relaxation]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [iterations, randomization-runs, number-of-UEs, applications, local-capability, delay-constraint]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[任务 A] and [任务 B] in [系统] With [约束] Guarantee"，14 词。"With Min-Max Fairness Guarantee" 把区别于已有工作的设计目标直接放进标题。

## 2. 摘要（5 句，171 词，短）
- 第 1 句雾 / 云协作的价值；"In this paper, we tackle the computation offloading problem in a mixed fog/cloud system by jointly optimizing …"（一句列全变量与约束）。
- 问题性质一句（min-max 加权代价、MINLP）→ "Due to the NP-hardness of the problem, we propose a low-complexity suboptimal algorithm …"（SDR + 随机化 / 分式规划 + 拉格朗日对偶分解）。
- 末句结果覆盖收敛、公平性与增益，无数字。

## 3. 引言逻辑（6 段，约 650 词，很短；相关工作单独成节）
1. UE 计算需求 → "However, UEs are usually resource-constrained, …" → MCC → "However, the delay caused by transferring data to the remote cloud server is usually unacceptable …"
2. MEC / 雾计算作为补充；声明本文不区分两个概念。
3. 已有工作要么只优化卸载决策、要么只优化资源分配；且只看系统级性能导致用户间不公平。
4. "Different from the above approaches, in this paper, we study the joint optimization of …" → min-max 公平 → MINLP + 低复杂度次优算法 → 4 条 bullet 贡献（第 1 条以 "Different from [6], [12], and [13], …" 开头）。
5. 路线图；6. Notation。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（单一优化维度、系统级目标造成不公平）+ 组合（卸载决策 × 计算资源 × 功率 × 带宽联合）。
- 写法亮点：公平性动机给了具体机制——信道好的用户受益、信道差的用户被牺牲——从而自然引出 min-max 目标。
- 相关工作节按"单用户 / 多用户 / 联合优化"分类综述。

## 5. 科研方法
- 场景：N 个 UE、一个 WiFi AP 作雾节点、远端云；本地 / 雾 / 云三种执行方式的时延与能耗分别建模（Fig. 1 系统拓扑图引自 [19]）；Remark 1 说明 NP-hard 的两个来源（min-max 与二元变量）。
- CORA（Fig. 2 流程图）：引入松弛变量 → QCQP → SDR（CVX 求解）→ 按概率随机抽取卸载决策并重复 L 次 → 给定决策下：计算资源用二分法（BCRA，Algorithm 2）；功率与带宽用分式规划（Dinkelbach 型，Algorithm 3）+ 拉格朗日对偶分解与次梯度（Algorithm 4，嵌套）。
- 单列 "Complexity Analysis of CORA" 节（O(N^6.5 log(1/ε))）。命题证明在附录。

## 6. 仿真与实验
- Table II 参数分 "Unchanged" 与 "Default" 两类（Remark 2 专门解释）；5000 次平均。
- 先分别验证三个迭代算法的收敛（Fig. 3–5）→ 随机化次数 L 的影响 → 与 Local-only、Offloading-only、Resource-only 比较（UE 数、受益 UE 数、不同应用（m 皇后问题）、本地算力、时延约束）→ 公平性对比。

## 7. 图表
- 12 图 2 表 4 算法。Fig. 1 系统拓扑（引用他文图），Fig. 2 算法流程图。caption 短标签（"The max EC among all UEs vs. the number of UEs N."）。

## 8. 句式库
- 资源受限："However, UEs are usually resource-constrained, possessing limited computation capability and battery, which makes it impractical to run sophisticated applications on them [2]."
- 远端时延："However, the delay caused by transferring data to the remote cloud server is usually unacceptable for some latency-sensitive applications."
- 只做一半："However, most of those previous works put their emphasis either on offloading decision making [2], [10], or resource allocation [6], without a joint consideration of both."
- 不公平机制："…, where UEs with good channel conditions … will benefit from computation offloading, but at the cost of degraded performance of UEs under bad channel conditions, resulting in unfairness among UEs."
- 转折到本文："Different from the above approaches, in this paper, we study the joint optimization of …"

## 9. 结论
- 节名 "Conclusions and Future Work"：第 1 段现在完成时复述（have investigated / have proposed）+ 仿真结论；第 2 段 "Our future work are listed as follows:" 后接 4 条 bullet（移动性、长期优化、多雾节点、队列时延）。无数字。
