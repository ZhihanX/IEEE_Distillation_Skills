---
doi: 10.1109/jsac.2020.3000802
title: "Intelligent Reflecting Surface Aided MIMO Broadcasting for Simultaneous Wireless Information and Power Transfer"
journal: JSAC
year: 2020
band: 2019-2021
cites: 807
cites_per_year: 130.7
article_type: research
topic: RIS
source: xplore-html
xplore: 9110849
auto:
  words_total: 7921
  n_sections: 6
  n_subsections: 6
  n_figures: 9
  n_tables: 0
  n_display_eq: 82
  n_algorithms: 5
  statements: {theorem: 4, lemma: 3, proposition: 0, corollary: 0, proof: 6, proof_in_appendix: 4}
  n_appendix: 4
  mean_sentence_words: 23.0
  we_per_1k: 15.4
  title_words: 13
  abstract_words: 199
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 3, contribList: 1, roadmap: 1, however: 8, transition: 12, resultsShow: 3, motivatedBy: 0, toAddress: 5, gapWord: 0, nonconvex: 7, npHard: 0, closedForm: 1, outperform: 2, intensifier: 2, worthNoting: 0, observe: 4, thisIsBecause: 0, asExpected: 4, insight: 1, tradeoff: 1, figVerb: 1, promising: 1, gen: 1, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 3, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 27, convergence: 18, BCD: 16, KKT: 12, lagrange: 6, SCA: 4, bisection: 4, convexOpt: 3, SDR: 2, MM: 1, WMMSE: 1, manifold: 1, compressedSensing: 1, DNN: 1}
code:
  title_pattern: [X-aided-Y, X-for-Y]
  abstract_moves: [aim, method, method, method, theory, theory, method, result]
  abstract_has_numbers: false
  abstract_anchor: none
  intro_paragraphs: 6
  intro_moves: [tech, prior, gap, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: numbered
  contrib_n: 5
  contrib_verbs: [formulate, develop, formulate, study, verify]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [combination, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [BCD, WMMSE, SCA, lagrangian-dual, bisection, MM]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [user-location, iterations, number-of-elements, EH-requirement, path-loss-exponent]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[器件] Aided [系统] for [目标技术]"，13 词。两个领域（IRS、SWIPT）都用全称，便于检索。

## 2. 摘要（8 句，199 词）
- 无 "In this paper"，首句即 "An intelligent reflecting surface (IRS) is invoked for enhancing the energy harvesting performance of a … (SWIPT) aided system."（invoke 是该作者组常用动词）。
- 中段突出算法的收敛保证："… which is guaranteed to converge to the Karush-Kuhn-Tucker (KKT) point of each subproblem."；"The BCD algorithm is rigorously proved to converge to the KKT point of the original problem."
- 结尾："… converges rapidly, which is appealing for practical applications."

## 3. 引言逻辑（6 段，约 1400 词）
1. IRS 原理和优点（与中继对比：无源、无热噪声、可贴附）→ 段末点出难点："However, the optimization variables are coupled and the joint design leads to a complex optimization problem that is difficult to solve."
2. 已有 IRS 工作长综述，按场景分组（单用户 / 多用户 / 安全 / MEC / 多播 / 多小区 / 信道估计），并逐个点评缺点（如 SDR 复杂度高、高斯随机化有性能损失）。
3. SWIPT 背景 → ER 需要更高功率、链路距离受限 → "To mitigate this issue, we propose to deploy an IRS in the vicinity of ERs …" → 唯一相关工作 [30] 的局限（SDR、多天线不适用）→ "Hence, in this paper we formulate …"
4. "Against this background, the main contributions of this paper are summarized as follows:" + 5 条编号贡献（含首创句）。
5. 路线图；6. Notations。

## 4. Idea 是怎么提出的
- 空白类型：组合（IRS × SWIPT × 多天线用户）+ 已有方法局限（单天线、SDR）。
- 直观动机：ER 对功率要求远高于 IR，所以把 IRS 放在 ER 附近补偿路损——"放在哪里"本身就是一个设计洞见（结果部分再次强调 IRS 位置的重要性）。
- 首创句写在贡献条目里，并说明比最相近工作更难："To the best of our knowledge, this is the first treatise considering …, which is much more challenging than … of [30] since …"

## 5. 科研方法
- WMMSE 等价变换 → BCD 拆成预编码子问题和相移子问题。
- 预编码：SCA + 拉格朗日对偶分解，近闭式解；对偶变量用二分（Lemma 1 单调性）；Theorem 1 收敛到 KKT 点。
- 相移：化为带 EH 约束的非凸 QCQP → MM + 价格机制（Lemma 3 单调性、二分），Theorem 2 子问题全局最优、Theorem 3 收敛。
- 总算法 Theorem 4 收敛到原问题 KKT 点；每个子算法都给复杂度。
- 单列一节 "Feasibility Check"：问题可能不可行，先判可行性——少见但实用。
- 4 个附录全部是证明。

## 6. 仿真与实验
- 参数在正文（路损指数逐链路给出）。基准：'No-IRS'、'Fixed Phase'（单引号标签命名）。
- 横轴含 ER / IR 位置、路损指数——用来讨论"IRS 应放在哪里"："This provides an important engineering design insight: the location of IRS should be carefully considered …"

## 7. 图表
- 9 图 0 表 5 算法。caption 短标签："WSR versus the number of phase shifters."

## 8. 句式库
- 难点："However, the optimization variables are coupled and the joint design leads to a complex optimization problem that is difficult to solve."
- 点评已有方法："However, its complexity is high since the number of optimization variables increases quadratically with the number of phase shifts."
- 提出方案："To mitigate this issue, we propose to deploy an IRS in the vicinity of ERs to provide additional transmission links …"
- 引出贡献："Against this background, the main contributions of this paper are summarized as follows:"
- 设计洞见："This provides an important engineering design insight: the location of IRS should be carefully considered …"

## 9. 结论
- 2 段：第 1 段复述（"eminently suitable for practical implementations"）；第 2 段坦白完美 CSI 假设，列出鲁棒设计、离散相移两个方向。
