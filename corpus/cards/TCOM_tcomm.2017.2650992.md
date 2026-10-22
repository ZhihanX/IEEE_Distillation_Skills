---
doi: 10.1109/tcomm.2017.2650992
title: "Optimal Joint Power and Subcarrier Allocation for Full-Duplex Multicarrier Non-Orthogonal Multiple Access Systems"
journal: TCOM
year: 2017
band: 2016-2018
cites: 514
cites_per_year: 53.6
article_type: research
topic: NOMA-RSMA-access
source: xplore-html
xplore: 7812683
auto:
  words_total: 7346
  n_sections: 6
  n_subsections: 13
  n_figures: 8
  n_tables: 1
  n_display_eq: 35
  n_algorithms: 3
  statements: {theorem: 1, lemma: 0, proposition: 0, corollary: 0, definition: 5, remark: 1, proof: 1, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 24.9
  we_per_1k: 13.0
  title_words: 13
  abstract_words: 170
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 5, contribList: 0, roadmap: 0, however: 12, transition: 29, resultsShow: 3, motivatedBy: 0, toAddress: 2, gapWord: 0, nonconvex: 8, npHard: 0, closedForm: 0, outperform: 0, intensifier: 4, worthNoting: 0, observe: 4, thisIsBecause: 3, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 0, promising: 0, gen: 0, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 2, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 11, convergence: 9, convexOpt: 9, SCA: 4, FP: 1, lagrange: 1, penalty: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, method, method, method, method, result, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 4
  intro_moves: [field, prior, gap, tech, prior, gap, tech, prior, gap, aim, contrib]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 3
  contrib_verbs: [formulate, solve, propose]
  contrib_quantified: false
  first_claim: true
  roadmap: false
  notation: model-start
  gap_type: [combination, theory-gap]
  motivating_figure: true
  problem_class: MINLP
  solution: [monotonic, FP, SCA, penalty, relaxation]   # monotonic = 单调优化（多块外逼近）全局最优
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [iterations, transmit-power, number-of-users, scheduled-users, fairness, SI-cancellation]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "Optimal Joint [A] and [B] Allocation for [系统]"，13 词。以 "Optimal" 开头直接宣告求得全局最优——这是本文相对已有次优方案的核心卖点。

## 2. 摘要（8 句，170 词）
- "In this paper, we investigate resource allocation algorithm design for … employing a full-duplex (FD) base station for serving multiple half-duplex (HD) downlink and uplink users simultaneously."
- 非凸问题 → "We apply monotonic optimization to develop an optimal joint power and subcarrier allocation policy." → 最优解的定位："The optimal resource allocation policy serves as a system performance benchmark due to its high computational complexity." → SCA 次优方案"to strike a balance between computational complexity and optimality"。
- 三句结果（次优接近最优；吞吐增益；更公平）。无数字。

## 3. 引言逻辑（4 段，约 1270 词，段落很长；无路线图）
1. 多载波多址（OFDMA）的资源分配工作 → "However, even with the schemes proposed in [3]–[5], the spectral resources are still underutilized as some subcarriers may have to be assigned exclusively to users with poor channel conditions …"
2. NOMA → 单载波工作 → MC-NOMA 工作都是次优 → "Thus, the maximum improvement in spectral efficiency provided by optimal MC-NOMA systems compared to MC-OMA systems is still unknown." → 自己的会议版 [1]（HD 下的最优设计）→ 但 HD 基站上下行正交仍浪费频谱。
3. 全双工（自干扰与上下行同信道干扰）→ FD 资源分配工作（都是 OMA）→ 引入 NOMA 的潜力 → 为什么更难（每个子载波要配对多个上下行用户；SIC 顺序、配对、功率耦合；"These unique challenges do not exist for … traditional FD MC-OMA systems."）→ 首创声明。
4. "In this paper, we address the above issues." → 问题 → 单调优化求最优 → SCA 次优 → 结果预告（含 "careful SI suppression is necessary …" 这样的设计启示）。

## 4. Idea 是怎么提出的
- 空白类型：组合（FD × 多载波 NOMA）+ 理论空白（最优性能未知，已有都是次优）。
- 写法亮点：三段引言各为一个技术"积木"（多载波 → NOMA → FD），每段末尾都指出"仍然没用满频谱 / 仍不知道最优增益"，层层把最后一块积木（FD MC-NOMA）推出来。
- "最优 + 次优"双方案结构：最优解（单调优化）因复杂度高只作性能基准，次优解（SCA）用于实际——摘要中就明确交代两者的分工。
- 会议版延续：从自己 HD MC-NOMA 的最优设计 [1] 扩展到 FD。

## 5. 科研方法
- 模型：FD 基站、K 个下行与 J 个上行 HD 用户，每个子载波最多复用两个下行 + 两个上行用户，SIC 解码顺序（Fig. 1 caption 详细说明谁先解谁）；加权和吞吐；混合组合非凸问题。
- 最优：单调优化预备知识用 5 个 Definition 给出（Box、Normal、Polyblock、Projection、单调优化问题）→ 改写为单调优化标准形 → 多块外逼近算法（Fig. 2 图示）；投影步是分式规划。Remark 1 说明算法从不可行点出发、最终收敛到可行最优。
- 次优：二元变量松弛 + 罚项（Theorem 1：罚因子足够大时等价，证明在附录）→ d.c. 规划 → SCA 迭代（多项式复杂度）。

## 6. 仿真与实验
- Table I 参数；用户权重取归一化距离（照顾远端用户）。
- 3 个基准（FD MC-OMA、HD MC-NOMA、HD MC-OMA）以 "baseline scheme 1/2/3" 编号，并逐一解释性能差距原因。
- 收敛 → 吞吐 vs 下行功率 → vs 用户数 → 被调度用户数 → Jain 公平指数 → vs 自干扰消除常数（得出"必须仔细抑制 SI"）。

## 7. 图表
- 8 图 1 表 3 算法。Fig. 1 系统示意（caption 交代 SIC 顺序），Fig. 2 多块外逼近示意（"The red star is an optimal point on the boundary …"）。结果图 caption 写全纵横轴名与单位及参数（"Average system throughput (bits/s/Hz) versus …"）。

## 8. 句式库
- 频谱仍未用满："However, even with the schemes proposed in [3]–[5], the spectral resources are still underutilized as …"
- 最优增益未知："Thus, the maximum improvement in spectral efficiency provided by optimal MC-NOMA systems compared to MC-OMA systems is still unknown."
- 已有方法不能套用："Existing user pairing methodologies for FD MC-OMA systems …, cannot be applied in FD MC-NOMA systems since they do not take into account the MUI introduced by NOMA."
- 独特挑战："These unique challenges do not exist for the resource allocation algorithm design in traditional FD MC-OMA systems."
- 最优解作基准："The optimal resource allocation policy serves as a system performance benchmark due to its high computational complexity."
- 折中："… a suboptimal iterative scheme based on successive convex approximation is proposed to strike a balance between computational complexity and optimality."

## 9. 结论
- 1 段 167 词，过去时复述（studied / was formulated / was applied / served as a performance benchmark）→ 三条结果（近优、吞吐提升、吞吐与公平的平衡）。无数字、无未来工作。
