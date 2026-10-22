---
doi: 10.1109/twc.2020.3037554
title: "Energy Efficient Federated Learning Over Wireless Communication Networks"
journal: TWC
year: 2021
band: 2019-2021
cites: 1034
cites_per_year: 184.9
article_type: research
topic: federated-edge-learning
source: xplore-html
xplore: 9264742
auto:
  words_total: 6559
  n_sections: 6
  n_subsections: 14
  n_figures: 11
  n_tables: 0
  n_display_eq: 83
  n_algorithms: 4
  statements: {theorem: 4, lemma: 5, proposition: 0, corollary: 0, proof: 8, proof_in_appendix: 1}
  n_appendix: 7
  mean_sentence_words: 21.6
  we_per_1k: 14.2
  title_words: 8
  abstract_words: 237
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 2, roadmap: 1, however: 5, transition: 6, resultsShow: 1, motivatedBy: 0, toAddress: 7, gapWord: 1, nonconvex: 2, npHard: 0, closedForm: 2, outperform: 6, intensifier: 0, worthNoting: 0, observe: 12, thisIsBecause: 4, asExpected: 0, insight: 0, tradeoff: 2, figVerb: 7, promising: 1, gen: 0, contrast: 2, firstTime: 0, novel: 2, weProposeFirst: 0, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 13, convergence: 10, bisection: 6, SCA: 3, FP: 2, lagrange: 2, KKT: 1}
code:
  title_pattern: [noun-phrase]
  abstract_moves: [aim, context, context, context, aim, method, method, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper
  intro_paragraphs: 4
  intro_moves: [field, gap, prior, gap, contrib, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [derive, formulate, construct, show]
  contrib_quantified: true
  first_claim: false
  roadmap: true
  notation: none
  gap_type: [limitation, combination]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [AO, closed-form, bisection, decomposition]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 4
  baseline_naming: acronym
  x_axes: [computations, accuracy, transmit-power, batch-size, completion-time]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "Energy Efficient [任务] Over [网络]"，8 词。与同组 "A Joint Learning and Communications Framework for FL Over Wireless Networks" 同属 "FL Over Wireless …" 系列，前缀换成目标（Energy Efficient）。

## 2. 摘要（8 句，237 词）
- 被动锚点："In this paper, the problem of energy efficient transmission and computation resource allocation for federated learning (FL) over wireless communication networks is investigated."
- 三句交代为什么要联合考虑学习与通信：模型交换 → 计算与通信时延都由学习精度决定；能量有限 → 计算与传输能耗都要算。
- 问题 → "an iterative algorithm is proposed where, at every step, closed-form solutions for … are derived."（列出 5 个变量）→ 初始可行点：构造完成时间最小化问题 + 二分法。
- 末句数字："… can reduce up to 59.5% energy consumption compared to the conventional FL method."

## 3. 引言逻辑（4 段，约 530 词，很短）
1. 隐私与资源 → 分布式学习 → FL → 无线链路资源有限 + 设备能量有限 → "Indeed, because of these resource constraints, it is necessary to optimize the energy efficiency for FL implementation."
2. 已有工作 [28]–[34] 逐篇一句 → "However, the works in [28]–[32] focused on the delay/energy for wireless transmission without considering the delay/energy tradeoff between learning and transmission." → 两篇最接近的工作（含自己的 [33]）分别指出遗漏：忽略本地计算时延、要求同步上传、没有收敛分析。
3. "The main contribution of this paper is a novel energy efficient computation and transmission resource allocation scheme for …" + 4 条 bullet（最后一条带 59.5%）。
4. 路线图。无记号段。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（只管传输能耗 / 时延，不管学习与传输的权衡）+ 组合（学习精度 × 计算频率 × 带宽 × 功率联合）。
- 写法亮点：对最接近的两篇工作（包括作者自己的前作）逐条点出具体遗漏，而不是笼统说"没研究"——自我批评前作也是定位手段（"In [33], we investigated …. However, this prior work ignored the computation delay of local FL model."）。
- 关键建模思想：把本地精度 η 作为优化变量，通过收敛分析把"本地迭代次数"与"全局迭代次数"都写成 η 的函数，于是学习与通信在同一个能耗—时延模型里权衡。

## 5. 科研方法
- 模型：本地计算（CPU 频率、能耗 κ f²）→ FDMA 上传 → 广播；DANE 算法（Algorithm 1）；Lemma 1（本地迭代数与 η）、Theorem 1（全局迭代数上界，假设 A1/A2：Lipschitz、强凸）；另有小节扩展到非凸损失（B2：有界非凸）。
- 能耗最小化 (19)：两步迭代——Theorem 2（时间分配与 η 的最优解，"it is optimal to transmit with the minimum time for each user"）、Theorem 3（带宽与功率的最优解）→ Algorithm 3；复杂度对比 SCA（线性于 K）。
- 可行初始点：完成时间最小化 (35)，Lemma 2 单调性 → 二分法；Lemma 3/4、Theorem 4 给可行性充要条件（Algorithm 4）。
- 证明分 7 个附录（每个附录标题写明证明哪条结果）。

## 6. 仿真与实验
- 参数写在正文（50 用户、3GPP 路损、真实 blog feedback 数据集）。
- 收敛（IID / 非 IID）→ 实际迭代数与 Theorem 1 上界对比 → 完成时间（与 EB-FDMA、FE-FDMA、TDMA [34] 比较，方案名用引号标签）→ 批大小 → 时间分解 → 总能耗（EXH-FDMA 作为近优参照）→ 能耗分解 → 能耗—完成时间权衡（与随机选择 RS 比较）。

## 7. 图表
- 11 图 0 表 4 算法。Fig. 1 系统图，Fig. 2 FL 流程，Fig. 3 FDMA 实现时序图。caption 短标签。

## 8. 句式库
- 必要性："Indeed, because of these resource constraints, it is necessary to optimize the energy efficiency for FL implementation."
- 已有工作的盲点："However, the works in [28]–[32] focused on the delay/energy for wireless transmission without considering the delay/energy tradeoff between learning and transmission."
- 批评自己的前作："In [33], we investigated the FL loss function minimization problem …. However, this prior work ignored the computation delay of local FL model."
- 结构性结论："Theorem 2 shows that it is optimal to transmit with the minimum time for each user."
- 理论与仿真对照："… the gap of the exact number of required iterations with the upper bound derived in Theorem 1 decreases as the accuracy … decreases, which indicates that the upper bound is …"

## 9. 结论
- 1 段 115 词，现在完成时复述（have investigated / have derived / have formulated / have proposed）→ "Numerical results have shown that the proposed scheme outperforms conventional schemes in terms of total energy consumption, especially for small maximum average transmit power."（给出增益最明显的条件）。无数字、无未来工作。
