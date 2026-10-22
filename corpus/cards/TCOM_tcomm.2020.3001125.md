---
doi: 10.1109/tcomm.2020.3001125
title: "Intelligent Reflecting Surface: Practical Phase Shift Model and Beamforming Optimization"
journal: TCOM
year: 2020
band: 2019-2021
cites: 751
cites_per_year: 123.3
article_type: research
topic: RIS
source: xplore-html
xplore: 9115725
auto:
  words_total: 6947
  n_sections: 7
  n_subsections: 11
  n_figures: 11
  n_tables: 2
  n_display_eq: 47
  n_algorithms: 3
  statements: {theorem: 0, lemma: 0, proposition: 4, corollary: 0, proof: 4, proof_in_appendix: 0}
  n_appendix: 4
  mean_sentence_words: 28.5
  we_per_1k: 8.4
  title_words: 10
  abstract_words: 244
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 1, however: 12, transition: 11, resultsShow: 2, motivatedBy: 3, toAddress: 3, gapWord: 1, nonconvex: 7, npHard: 0, closedForm: 4, outperform: 1, intensifier: 3, worthNoting: 2, observe: 11, thisIsBecause: 0, asExpected: 0, insight: 3, tradeoff: 0, figVerb: 2, promising: 4, gen: 0, contrast: 6, firstTime: 0, novel: 0, weProposeFirst: 7, wlog: 3, code: 0, prototype: 0}
  methods: {penalty: 14, convergence: 9, complexity: 7, AO: 4, convexOpt: 3, BCD: 2, bisection: 2}
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [context, gap, aim, method, method, theory, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, gap, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [propose, solve, extend]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [practicality, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [AO, penalty, BCD, closed-form, decomposition]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [number-of-elements, distance, phase-distribution, quantization-bits, SINR-target, number-of-users]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[器件]: [Practical 模型] and [优化]"，10 词。冒号前只放技术名，冒号后"建模 + 优化"两件事——与 Pinching-antenna 论文的 "Modeling and Beamforming Optimization for …" 同一套路（先修正模型，再在新模型下重做优化）。

## 2. 摘要（7 句，244 词）
- 第 1 句技术价值（"has recently emerged as a promising cost-effective technology …"）。
- 第 2 句空白直接点名已有模型的理想化假设："Prior works on IRS are mainly based on the ideal phase shift model …, which, however, is practically difficult to realize."
- 第 3 句 "In contrast, we propose in this paper a practical phase shift model …"——用 In contrast 把空白句和贡献句连起来。
- 中段问题 + 算法（AO、penalty）；第 6 句理论："to draw essential insight, we analyze the asymptotic performance loss …"；最后一句 "Simulation results unveil substantial performance gains …"。无数字。

## 3. 引言逻辑（6 段，约 940 词）
1. IRS 价值 → 已有结论（N² 平方功率增益）→ 联合主被动波束在各种场景中的应用（列 PLS、OFDM、NOMA、SWIPT）→ 一句话否定全部："However, the above prior works as well as many others … have all assumed the ideal phase shift model …"
2. 物理机理段：为什么反射幅度随相位变化（镜像电流同相 → 损耗增大），损耗不可避免，加放大器又不适用于无源 IRS——用器件物理为"模型不准"背书。
3. 后果段：理想模型下的"相位对齐"设计不再最优，需要在"幅度与相位对齐之间取平衡"→ "… cannot be accomplished by directly applying the existing models of IRS and thus motivates this work."
4. "In this paper, by establishing a practical IRS phase shift model and considering … shown in Fig. 1, we formulate and solve …" → 3 条 bullet 贡献（First / Next / Finally）。
5. 路线图；6. Notations。

## 4. Idea 是怎么提出的
- 空白类型：实用性（理想反射模型与硬件不符）+ 已有方法局限。这是"修正一个被全领域默认的假设"型选题：一段话否定整批文献，再用器件物理解释假设为何不成立。
- 新模型先用等效电路仿真和文献实验结果验证（"in accordance with the experimental results reported in the literature"），再拿来做优化——模型可信度在优化之前建立。
- 理论部分专门回答"用理想模型设计会损失多少"（Proposition 1：N→∞ 时功率比只取决于 βmin 与 α，与 N 无关），把新模型的必要性量化。

## 5. 科研方法
- 等效电路（RLC）→ 反射系数随电容 / 电阻变化 → 提出三参数解析模型 β(θ)（βmin、φ、α），与电路仿真吻合。
- 单用户：AO 逐元素更新相位，Proposition 2 给信赖域、Proposition 3 用二次拟合给闭式近似解；另一算法为 penalty-based（引入辅助变量 + 罚项，内层 BCD，外层增大罚因子）。
- 多用户：extended penalty（高性能高复杂度）与 two-stage（先最大化合成信道增益再求发射波束，低复杂度）——明确给出两种算法的复杂度 / 性能取舍。
- 复杂度用 O(·) 表达式；4 个命题证明全在附录。

## 6. 仿真与实验
- 3D 坐标设定（Fig. 5 仿真布局图），2.4 GHz，参数写在正文。
- 方案用编号列表 1)–6) 定义：下界（理想 IRS）、提出的算法若干、"Ideal IRS assumption"（理想模型设计后用在实际 IRS 上）、上界（无 IRS）——基准设计直接对准本文论点（模型失配损失）。
- 结果：验证 Proposition 1 → 距离 → 相位分布直方图（解释设计行为）→ 离散相位 → SINR 目标 → CPU 运行时间表（注明 MATLAB 版本与 PC 配置）→ 用户数。

## 7. 图表
- 11 图 2 表。Fig. 1 系统图（引言），Fig. 2–4 器件建模图（传输线模型、反射系数曲线、提出的模型），Fig. 5 仿真布局。caption 全部短标签（"AP transmit power versus number of reflecting elements."）。

## 8. 句式库
- 否定整批文献的假设："However, the above prior works as well as many others … on IRS have all assumed the ideal phase shift model with full signal reflection, …"
- 假设不现实："…, which, however, is practically difficult to realize due to the hardware limitation [30], [31]."
- 动机收束："…, which, however, cannot be accomplished by directly applying the existing models of IRS and thus motivates this work."
- 转折到本文："In contrast, we propose in this paper a practical phase shift model that captures …"
- 先简单情形求洞见："In this section, we consider the special case with a single user to draw important insights into the beamforming design."

## 9. 结论
- 1 段 178 词：过去时复述（proposed and validated / formulated and solved）→ 结果定性（"may lead to significant performance loss …, especially when the effective resistance … is large"——给出损失最明显的条件）→ 未来工作列出 4 类扩展场景 + CSI 获取 / 鲁棒设计。
