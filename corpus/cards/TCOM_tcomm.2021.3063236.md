---
doi: 10.1109/tcomm.2021.3063236
title: "Channel Estimation for RIS-Empowered Multi-User MISO Wireless Communications"
journal: TCOM
year: 2021
band: 2019-2021
cites: 666
cites_per_year: 124.7
article_type: research
topic: RIS
source: xplore-html
xplore: 9366805
auto:
  words_total: 6648
  n_sections: 7
  n_subsections: 17
  n_figures: 12
  n_tables: 1
  n_display_eq: 44
  n_algorithms: 4
  statements: {theorem: 0, lemma: 1, proposition: 0, corollary: 0, remark: 1, proof: 1, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.7
  we_per_1k: 9.1
  title_words: 8
  abstract_words: 240
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 1, roadmap: 1, however: 7, transition: 7, resultsShow: 2, motivatedBy: 4, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 2, outperform: 3, intensifier: 0, worthNoting: 0, observe: 2, thisIsBecause: 1, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 1, promising: 1, gen: 1, contrast: 3, firstTime: 0, novel: 1, weProposeFirst: 0, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 14, CRB: 8, convergence: 2, compressedSensing: 1, monteCarlo: 1, DNN: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, gap, aim, method, method, theory, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [tech, gap, prior, prior, prior, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [introduce, present, investigate, prove]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [limitation, tool-transfer, theory-gap]
  motivating_figure: true
  problem_class: estimation
  solution: [tensor-decomposition, AO, message-passing, CRB]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [SNR]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "Channel Estimation for [器件]-Empowered [系统] Wireless Communications"，8 词。"-Empowered" 是 RIS 文献里与 "-Aided / -Assisted / -Enabled" 并列的高频修饰词。

## 2. 摘要（9 句，240 词）
- 背景 → 挑战句："Accurate and low-overhead channel estimation in RIS-based systems is one of the most critical challenges due to the usually large number of RIS unit elements and their distinctive hardware constraints."
- "In this paper, we focus on … and propose a channel estimation framework based on the parallel factor decomposition to unfold the resulting cascaded channel model."
- 两个算法（ALS / VAMP）、CRB、下行和速率各一句；结尾两句结果，其中一句 "the ALS technique achieves the CRB"。

## 3. 引言逻辑（8 段，约 1400 词）
1. RIS 原理与优势（与 AF 中继对比）。
2. RIS 应用工作列表 → 段末空白："The existing research works have proved the great potential of RIS, however, most of the existing research works … assumed the perfect channel state information availability."
3. 信道估计难点（需同时估计多条信道、单元多、硬件非线性）→ 逐篇点评已有 CE 方法（"…, however, the authors just estimate cascaded channels instead of separate channels"；"which has a low complexity but a more constrictive requirement on the training parameters"）。
4. 机器学习方法及其局限（需大量离线训练或要求 RIS 带有源单元）。
5. PARAFAC 在中继信道估计中的成功 → 自己的会议版 → "However, the performance of the presented algorithm was not theoretically studied, …"（用自己会议版的不足引出期刊版增量）。
6. "In this paper, motivated by the PARAFAC decomposition [43], [44], we leverage …" → 4 条贡献。
7. 路线图；8. Notation。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限 + 工具迁移（PARAFAC 从中继信道估计 / 心理测量学引入）+ 理论缺口（会议版无性能分析）。
- 核心洞见：级联信道的接收训练信号天然构成三阶张量，可以用 PARAFAC 分解把 BS-RIS 与 RIS-用户两段信道分开估计（而不只是估计级联信道）。
- 方法来源交代得很清楚："The PARAFAC decomposition is a subset of multi-way analysis inspired from psychometrics and chemometrics, …"

## 5. 科研方法
- 系统模型 + PARAFAC 预备知识 + 训练信号的三种展开形式。
- ALS：初始化、迭代、终止准则分三步写；VAMP 作为替代的 LS 步骤。
- 可行性条件（Lemma 1：要求 M, K ≥ N），并在 Remark 中坦白这对大 RIS 是限制。
- CRB 分析（单独一节），说明 VAMP 难以给出 CRB 的原因。
- 再用估计信道算 MRT / ZF / MMSE 预编码下的下行和速率。

## 6. 仿真与实验
- 基准：genie-aided LS、LSKRF [30]。指标：NMSE、CRB 对比、和速率。
- 先 NMSE（对比 + 扫 N、P），再 CRB，再和速率（三种预编码、扫 P、扫 N）。
- 解释句："This is because that a larger P means more training pilots and thus CE performance improves, …"

## 7. 图表
- 12 图 1 表（复杂度表）4 算法。caption 描述型并带参数："NMSE performance comparisons between the proposed algorithms, genie-aided LS estimation, and LSKRF [30] versus the SNRs in dB for M=K=T=N=P=16."
- 结果图横轴几乎全是 SNR，用多条曲线区分参数——单变量横轴 + 参数族曲线。

## 8. 句式库
- 挑战："Accurate and low-overhead channel estimation in RIS-based systems is one of the most critical challenges due to …"
- 共同假设："The existing research works have proved the great potential of RIS, however, most of the existing research works … assumed the perfect channel state information availability."
- 点评方法："…, which has a low complexity but a more constrictive requirement on the training parameters."
- 会议版增量："However, the performance of the presented algorithm was not theoretically studied, and hence, the accuracy and stability … were not thoroughly investigated."
- 承认局限（结论）："However, the proposed algorithms also have the limitations, e.g., …"

## 9. 结论
- 1 段 184 词：过去时复述 → 复杂度比较 → 主动列出局限（单元数约束、模糊性）→ 仿真结论。无未来工作段，但局限写在结论里。
