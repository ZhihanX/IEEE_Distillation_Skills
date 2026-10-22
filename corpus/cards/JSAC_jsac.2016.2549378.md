---
doi: 10.1109/jsac.2016.2549378
title: "Cooperative Non-orthogonal Multiple Access With Simultaneous Wireless Information and Power Transfer"
journal: JSAC
year: 2016
band: 2016-2018
cites: 910
cites_per_year: 86.6
article_type: research
topic: NOMA-RSMA-access
source: xplore-html
xplore: 7445146
auto:
  words_total: 7100
  n_sections: 5
  n_subsections: 22
  n_figures: 8
  n_tables: 0
  n_display_eq: 88
  n_algorithms: 0
  statements: {theorem: 5, lemma: 0, proposition: 0, corollary: 5, proof: 8, proof_in_appendix: 0}
  n_appendix: 4
  mean_sentence_words: 26.5
  we_per_1k: 15.7
  title_words: 11
  abstract_words: 154
  abstract_sentences: 6
  phrases: {toTheBest: 0, inThisPaper: 7, contribList: 1, roadmap: 2, however: 1, transition: 3, resultsShow: 0, motivatedBy: 2, toAddress: 0, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 3, outperform: 0, intensifier: 0, worthNoting: 4, observe: 3, thisIsBecause: 5, asExpected: 0, insight: 3, tradeoff: 0, figVerb: 7, promising: 1, gen: 2, contrast: 0, firstTime: 0, novel: 2, weProposeFirst: 0, wlog: 2, code: 0, prototype: 0}
  methods: {stochGeom: 6, complexity: 2, monteCarlo: 2}
code:
  title_pattern: [X-with-Y]
  abstract_moves: [aim, method, method, theory, theory, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 7
  intro_moves: [field, tech, prior, aim, aim, contrib, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, derive, derive, confirm]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: none
  gap_type: [combination, new-scenario]
  motivating_figure: true
  problem_class: analysis-only
  solution: [stochastic-geometry, closed-form]
  theory_role: central
  proofs_location: mixed
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2
  baseline_naming: acronym
  x_axes: [SNR, density, rate, zone-radius]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "Cooperative [接入技术 A] With [技术 B]"，11 词，两个缩写都写全称（NOMA、SWIPT）。"A With B" 结构直接宣告"把两个热点结合起来"。

## 2. 摘要（6 句，154 词，短）
- 被动语态锚点："In this paper, the application of simultaneous wireless information and power transfer (SWIPT) to nonorthogonal multiple access (NOMA) networks in which users are spatially randomly located is investigated."
- 协议一句（近用户作为能量收集中继帮远用户）→ 三种用户选择方案（理由："Since the locations of users have a significant impact on the performance, …"）→ 闭式中断概率与吞吐。
- 理论结论："These analytical results demonstrate that the use of SWIPT will not jeopardize the diversity gain compared to the conventional NOMA."——摘要里给出一个"不损失"型洞见。

## 3. 引言逻辑（7 段，约 1170 词；引言内分 A. Motivation and Contributions / B. Organization 两个小节）
1. NOMA 的核心思想（功率域复用）+ 已有 NOMA 工作逐篇一句。
2. 第二条技术线 SWIPT：理想假设 → TS / PS 接收机 → AF / DF 中继中的 SWIPT（"On the one hand, … On the other hand, …"）。
3. （小节 A）NOMA 的特点导致远用户性能下降 → 已有协作 NOMA [5] 的思想：近用户已通过 SIC 获知远用户信息 → "In this case, it is natural to consider the use of the near users as DF relays …"
4. "In this paper, we consider this setting, but with the additional feature that the near users are energy constrained …" → "the aforementioned two communication concepts, cooperative NOMA and SWIPT, can be naturally linked together" → 随机几何建模。
5. 混合多址的必要性 → 用一个问题引出用户选择："a natural question arises: which near NOMA user should help which far NOMA user?" → 三种方案（RNRF / NNNF / NNFF）定义。
6. "The primary contributions of our paper are summarized as follows." + 4 条 bullet。
7. （小节 B）路线图。

## 4. Idea 是怎么提出的
- 空白类型：组合（协作 NOMA × SWIPT）+ 新场景（近用户能量受限）。
- 写法亮点：用 "it is natural to …" / "can be naturally linked together" 把组合包装成"顺理成章"，而不是生硬拼接；再用一个设问句（谁帮谁？）引出第二层贡献（用户选择）。
- 主动划定范围："The insights obtained from these opportunistic user selection schemes provide guidance for the design of dynamic user clustering algorithms, a topic beyond the scope of the paper."

## 5. 科研方法
- 随机几何：近用户在圆盘、远用户在圆环内服从齐次 PPP；两阶段传输（直传 + 近用户用 PS 收集的能量 DF 转发），远用户 MRC 合并。
- 对三种选择方案各自按同一模板推导："近用户中断 → 远用户中断 → 分集分析 → 时延敏感吞吐"，形成整齐的 3×4 小节结构。
- 5 个定理（一般 α，用 Gaussian–Chebyshev 近似，参数 N、M、K 控制精度—复杂度）+ 5 个推论（α=2 特例简化）。
- 分集分析作为洞见来源："To obtain further insights into the derived outage probability, we provide a diversity analysis …"；指出远用户中断概率衰减速率为 ln SNR / SNR² 而非 1/SNR²。

## 6. 仿真与实验
- 无参数表，参数在首段与 caption 中给出；用颜色区分三种方案（"we use red, blue and black color lines to represent …"）。
- 每张图同时画解析曲线与 Monte-Carlo 仿真点；RNRF 作为随机选择基准、非协作 NOMA 作为对比基准。
- 观察用编号列出："Several observations can be drawn as follows: 1) … 2) …"。

## 7. 图表
- 8 图 0 表。Fig. 1 网络模型（圆盘 + 圆环，颜色标注近 / 远用户）。caption 描述型，把全部参数值写进 caption（"…, where α=2, R_DB=2 m, and SNR=30 dB."）。

## 8. 句式库
- 顺理成章的组合："In this case, it is natural to consider the use of the near users as DF relays to transmit information to the far users."
- 在已有设定上加一个特征："In this paper, we consider this setting, but with the additional feature that the near users are energy constrained …"
- 设问引出子问题："Based on the proposed protocol and the considered stochastic geometric model, a natural question arises: which near NOMA user should help which far NOMA user?"
- 不损失型结论："… the use of SWIPT will not jeopardize the diversity gain compared to the conventional NOMA."
- 划定范围："…, a topic beyond the scope of the paper."

## 9. 结论
- 1 段 173 词，现在完成时复述（has been considered / has been proposed / have been derived）→ 衰减速率对比 → "We conclude that by carefully choosing the parameters of the network, …, acceptable system performance can be guaranteed …"（设计建议式收尾）。无数字、无未来工作。
