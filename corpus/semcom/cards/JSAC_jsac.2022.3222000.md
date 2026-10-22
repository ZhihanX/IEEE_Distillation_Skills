---
doi: 10.1109/jsac.2022.3222000
title: "Heterogeneous Semantic and Bit Communications: A Semi-NOMA Scheme"
journal: JSAC
year: 2023
band: 2022-2025
cites: 160
cites_per_year: 42.6
article_type: research
topic: semantic
source: xplore-html
xplore: 9953095
auto:
  words_total: 8101
  n_sections: 7
  n_subsections: 21
  n_figures: 12
  n_tables: 0
  n_display_eq: 48
  n_algorithms: 0
  statements: {theorem: 0, lemma: 1, proposition: 0, corollary: 0, remark: 2, proof: 1, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.8
  we_per_1k: 7.0
  title_words: 8
  abstract_words: 319
  abstract_sentences: 11
  phrases: {toTheBest: 0, inThisPaper: 8, contribList: 2, roadmap: 1, however: 16, transition: 6, resultsShow: 0, motivatedBy: 2, toAddress: 4, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 2, outperform: 4, intensifier: 2, worthNoting: 3, observe: 16, thisIsBecause: 7, asExpected: 0, insight: 3, tradeoff: 3, figVerb: 1, promising: 1, gen: 4, contrast: 7, firstTime: 0, novel: 3, weProposeFirst: 5, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 3, DNN: 2}
  domain: {DeepSC: 12, DeepJSCC: 3, MIMO: 1, Rayleigh: 1, sentSim: 1}
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [aim, metric, gap, method, model, method, method, theory, theory, result, result]
  abstract_has_numbers: false
  abstract_anchor: passive-aim             # "Multiple access (MA) design is investigated to …"
  intro_paragraphs: 8
  intro_moves: [field, field, prior, gap-question, aim, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [exploit, propose, characterize, validate]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, open-question]
  motivating_figure: true
  problem_class: nonconvex-continuous    # 功率 / 带宽分配刻画 SvB 速率区域与功率区域边界
  solution: [closed-form, water-filling, one-dimensional-search]
  theory_role: central                   # 速率区域、功率区域的边界刻画（Lemma 1、Remark 1–2）
  proofs_location: inline
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2                         # OMA、NOMA（本文提出的三种方案相互比较）
  baseline_naming: acronym
  x_axes: [semantic-rate, bit-rate, target-similarity, K]
  fig1_role: background                  # DeepSC 框架
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2               # 另附 3 条带标题的未来方向 bullet
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: networking
  source: [text]
  task: [reconstruction]
  paradigm: system-level
  architecture: [transformer]            # 以 DeepSC 的性能曲线为语义层模型
  channel: [Rayleigh]
  adaptivity: [resource-allocation]
  training: [none]
  metrics: [semantic-rate, bit-rate, power]
  datasets: []                           # 语义相似度曲线来自 DeepSC 实验数据的回归
  baselines: [optimization]
  snr_mismatch_test: false
  complexity_reported: false
  digital_compatible: true               # 比特用户走传统编码
  hardware_validation: false
  theory: performance-bound              # 语义-比特速率区域
  idea_delta: [multi-user, theory, system-optimization]
  builds_on: [DeepSC, semantic rate metric, NOMA / rate region theory]
  open_problems_n: 3
---

## 1. 标题
- "[新场景]: A [方法] Scheme"，8 词。冒号前是场景（语义 / 比特异构共存），冒号后是方案名。

## 2. 摘要（11 句，319 词，很长）
- 被动语态开篇（"Multiple access (MA) design is investigated …"）→ 语义速率指标 → 关键挑战（语义相似度无闭式）→ 数据回归（广义 logistic 函数）→ 异构框架（S-user + B-user）→ 三种多址（OMA、NOMA、semi-NOMA）→ semi-NOMA 机理 → 定义 SvB 速率区域与功率区域 → 最优资源分配 → 解的结构表明 semi-NOMA 更优 → 两条数值结论（编号 1)、2)）。

## 3. 引言逻辑（8 段，A–C 小节）
- 1G–5G 与 6G 需求 → 语义通信 + Weaver 三层次 → A：语义信息论（逻辑概率、GMSC、贝叶斯博弈）与 DL 语义通信（文本 JSCC、DeepJSCC、DeepSC、语义速率）→ B：未来网络需同时支持语义与比特传输 → 关键问题："It is well known that NOMA is capacity-achieving while OMA is suboptimal in the conventional bit-based transmission [23]. Nevertheless, an interesting question arises, when considering semantic communications, does …" → 本文回答 → 贡献 → 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：新场景（语义用户与比特用户共存）+ 开放问题（经典结论"NOMA 优于 OMA"在语义场景是否仍成立）。
- 核心洞见：语义速率依赖带宽 × 语义相似度（相似度随 SNR 呈 S 形饱和），与比特速率的 log(1+SNR) 结构不同——于是"全共享带宽"未必最优，"部分共享 + 部分正交"的 semi-NOMA 统一了 OMA / NOMA 且严格更优。
- 把不可解析的 DL 性能（DeepSC 的语义相似度）用数据回归拟合成广义 logistic 函数——让网络理论分析可以"接上"深度学习语义系统。这是网络 / 理论类语义论文的通用桥接手法。
- 用一个"经典结论是否仍成立"的问题驱动全文，结论给出反直觉答案（NOMA 不一定优于 OMA）。

## 5. 科研方法
- 语义速率 S = W·I/(K·L)·ε(K, γ)；ε 用广义 logistic 函数对 DeepSC 数据回归（Fig. 2）。
- 三种多址的系统模型、SvB 速率区域与功率区域定义。
- 边界刻画：OMA（Lemma 1 带宽区间）、NOMA、semi-NOMA（两路比特流间注水功率分配）；Remark 1：NOMA 区域不一定包含 OMA 区域；Remark 2：semi-NOMA 区域包含两者。

## 6. 仿真与实验
- Rayleigh + 路损（指数 4），W = 1 MHz。
- SvB 速率区域：三种信道差异情形、不同 K → 功率区域：最小发射功率 vs 目标语义速率、目标相似度、K。
- 结论：semi-NOMA 最优，即使对称信道 OMA 也严格次优；S-user 信道更好、B-user 更差时配对收益最大。

## 7. 图表
- 12 图 0 表。Fig. 4–6 三种多址的频带示意并列，Fig. 7 资源分配变量汇总——"方案对比示意图"是多址类论文的标准做法；结果图为速率区域边界曲线。

## 8. 句式库
- 驱动问题："Nevertheless, an interesting question arises, when considering semantic communications, does this conclusion still hold or do we need to develop new tailored MA schemes?"
- 不可解析的挑战（摘要）："However, a key challenge is that there is no closed-form expression for a key parameter, namely the semantic similarity, which characterizes the sentence similarity between an original sentence …"
- 历史定位："It is worth mentioning that the concept of semantic communications is not a completely new idea."
- 反直觉结论："In contrast to the conventional bit-based transmission, our results revealed that NOMA does not necessarily outperform OMA, and semi-NOMA is promising given its flexible transmission strategies."
- 统一性论证："It can be observed that the proposed semi-NOMA scheme not only unifies both OMA and NOMA as special cases but also provides more flexible transmission options."

## 9. 结论
- "Conclusion and Future Work"：1 段复述 + 配对指导 → 1 句引出 + 3 条带标题的开放问题 bullet。

## 10. Idea 拆解
- **基线**：DeepSC（tsp.2021.3071210）与语义速率指标；比特通信中的 OMA / NOMA 速率区域理论。
- **增量**：首次研究语义与比特用户共存的多址设计，用回归拟合使语义速率可解析，刻画三种多址的速率 / 功率区域并提出统一两者的 semi-NOMA（multi-user + theory + system-optimization）。
- **为什么有效**：语义相似度随 SNR 饱和，高 SNR 时多给功率收益很小，因此把一部分带宽与比特流共享、另一部分正交，比全共享或全正交都灵活。
- **证据**：semi-NOMA 的速率区域严格包含 OMA 与 NOMA；所需最小功率最低；对称信道下 OMA 仍次优。
- **弱点**：语义层只是 DeepSC 曲线的回归，结论依赖该曲线形状；单 S-user + 单 B-user、单天线；未考虑语义用户的 SIC 误差传播与 DeepSC 在干扰下的实际表现；无端到端仿真。
- **开放问题**：
  - 结论 bullet："Heterogeneous transmission design with multiple S- and B-users: This paper considered a fundamental model with one S-user and one B-user."
  - 结论 bullet："Performance limit characterization of the heterogeneous transmission with multimodal data: The semantic rate considered in this paper is used for characterizing the performance of text semantic communications."
  - 结论 bullet："Opportunistic semantic and bit transmission design: This paper assumed that each user can only use one specific transmission method, i.e., semantic or bit-based transmission."
  - 推断：多天线 / RSMA 下的语义-比特共存；用实际 deep JSCC 模型在叠加干扰下训练验证回归模型；图像 / 视频的语义速率曲线建模。
