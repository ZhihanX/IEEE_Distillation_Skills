---
doi: 10.1109/jsac.2022.3223408
title: "Beyond Transmitting Bits: Context, Semantics, and Task-Oriented Communications"
journal: JSAC
year: 2023
band: 2022-2025
cites: 812
cites_per_year: 216.1
article_type: overview
topic: semantic
source: xplore-html
xplore: 9955525
auto:
  words_total: 24983
  n_sections: 9
  n_subsections: 34
  n_figures: 14
  n_tables: 0
  n_display_eq: 44
  n_algorithms: 0
  statements: {theorem: 7, corollary: 1}
  n_appendix: 0
  mean_sentence_words: 27.8
  we_per_1k: 4.7
  title_words: 8
  abstract_words: 129
  abstract_sentences: 6
  phrases: {toTheBest: 0, inThisPaper: 8, contribList: 1, roadmap: 1, however: 28, transition: 9, resultsShow: 0, motivatedBy: 7, toAddress: 2, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 14, intensifier: 11, worthNoting: 0, observe: 1, thisIsBecause: 1, asExpected: 0, insight: 1, tradeoff: 14, figVerb: 1, promising: 1, gen: 3, contrast: 5, firstTime: 2, novel: 6, weProposeFirst: 0, wlog: 0, code: 2, prototype: 2}
  methods: {DNN: 11, complexity: 10, DRL: 4, convergence: 4, lagrange: 3, monteCarlo: 3}
  domain: {ratedist: 51, perception: 24, knowledgeBase: 20, quantization: 17, DeepJSCC: 10, feedback: 10, accuracy: 9, MSSSIM: 7, DeepSC: 6, VQ: 5}
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [context, context, aim, aim, scope, scope]
  abstract_has_numbers: false
  abstract_anchor: this-tutorial
  intro_paragraphs: 15
  intro_moves: [field, motivation, history, history, history, history, history, history, history, position, prior-surveys, contrib, roadmap]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 6
  conclusion_paragraphs: 1
  conclusion_future_work: false
semcom:
  category: overview
  source: [image, text, video, speech]
  task: [survey]
  paradigm: theory
  theory: rate-distortion
  idea_delta: []
  builds_on: [Shannon, Weaver three levels, rate-distortion-perception, information bottleneck, DeepJSCC, AoI]
  open_problems_n: 4
---

## 概要（综述 / 教程，轻量卡片）
- 定位：以信息论为主线的语义 / 任务导向通信教程——"follow Shannon's approach"，把语义放进率失真框架，再讲学习方法如何在失真度量无法显式写出时补位。
- 结构（9 节）：引言（动机、语义的历史、已有综述）→ 语义信息度量（语义熵、知识图谱）→ 信息论基础（率失真、率-失真-感知、目标导向压缩、上下文作为边信息、IB、远程信源 / CEO 问题）→ 学习方法（远程训练、远程推理）→ 噪声信道上的语义 / 任务导向 JSCC（多终端 JSCC、远程推理）→ 实用设计（文本 / 语音 / 图像视频等多模态）→ 时间作为语义（AoI、AoII、实时重建）→ 有效性 / 语用通信 → 结论。
- 篇幅：约 2.5 万词，14 图 0 表，7 个定理（引用经典结果）。

## 引言写法
- 第一段即全文立场：Shannon 有意让系统"不关心消息含义"，这一设计在比特管道中极成功；新应用（自动驾驶、医疗、IoE）的目标是"做出正确推断 / 决策"而非精确重建 → 整合语义仍处婴儿期。
- 两条动机（流量与时延）用自动驾驶的具体例子展开；随后用 7 段讲"语义"的历史（符号学、Chomsky、Weaver 三层次、Wiener、Bar-Hillel & Carnap）——综述用"历史纵深"建立权威性。

## 对 idea 生成有用的内容
- 统一视角：大多数语义通信问题都可以写成"带特定失真度量的（远程）率失真问题"，难点在于实际信源的失真度量无法显式写出 → 这正是学习方法的切入点。
- 列出的经典开放问题（信息论层面）：
  - "Integrating semantics into system design, however, is still in its infancy with ample open problems ranging from foundational formulations to development of practical systems."
  - "How to select which are the relevant features for a given task is an open problem and depends on the metric that is used."
  - "Despite significant research efforts, the optimal characterization of the type-II error exponent for the remote HT problem for the general case (beyond testing against independence) remains open to this day."
  - "However, in the general case, the optimal performance for a generic function is an open problem, even in the lossless computation case."
- 被强调的方向：JSCC 对信道变化的适应性；"时效性即语义"（AoI 与率失真的联系）；语用 / 有效性层（智能体为达成目标而通信）。

## 句式库
- 立场句："In these applications, the goal of communication is often not to reconstruct the underlying message exactly as in conventional communication networks, but to enable the destination to make …"
- 方法论立场："In this paper, our goal is to follow Shannon's approach, in the sense that, we would like to outline a mathematical framework for semantic communication, and highlight how …"
- 网络不应是比特管道："Hence, the communication infrastructure cannot simply be an ignorant bit-pipe to enable intelligence at the higher layers, but must incorporate intelligence itself to make sure only the required …"
- 结论核心："In particular, we argued that semantics can be considered in the context of rate-distortion theory, albeit for most practical information sources it is difficult if not impossible to …"

## 10. Idea 拆解（综述视角）
- 本文不提出新方法；对 idea 生成的价值在于给出"语义 = 率失真中的任务相关失真"这一统一建模，以及信息论层面的开放问题清单（远程假设检验误差指数、一般函数计算的最优性能、特征相关性选择）。
- 推断（可由综述引出的研究方向）：为深度 JSCC 建立可计算的语义率失真基准；把 AoI / 时效性与语义失真联合优化；语用通信中的多智能体联合训练与通信。
