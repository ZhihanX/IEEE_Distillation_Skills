---
doi: 10.1109/tcomm.2019.2914652
title: "Wireless Access in Ultra-Reliable Low-Latency Communication (URLLC)"
journal: TCOM
year: 2019
band: 2019-2021
cites: 468
cites_per_year: 65.2
article_type: overview      # 选文时按研究论文入选，全文为原理 / 教程式综述（"aims to provide a broad perspective"）：0 个定理、无贡献列表、相关工作是 2400 词的文献综述，按约定改记为 overview 并顺延补位
topic: URLLC-AoI
source: xplore-html
xplore: 8705373
auto:
  words_total: 12381
  n_sections: 9
  n_subsections: 29
  n_figures: 12
  n_tables: 1
  n_display_eq: 29
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  title_words: 7
  abstract_sentences: 5
code:
  title_pattern: [X-in-Y]
  abstract_moves: [context, context, aim, aim, aim]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 4
  intro_moves: [field, field, aim, roadmap]
  related_work: separate-section
  contrib_format: none
  contrib_n: 0
  contrib_verbs: []
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: none
  gap_type: [theory-gap]
  motivating_figure: true
  problem_class: none
  solution: []
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 0
  baseline_naming: none
  x_axes: []
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 3
  conclusion_has_numbers: false
  conclusion_future_work: true
---

> 本卡只做结构与写法层面的记录（overview 不参与研究论文的统计）；只抽取了摘要、引言、章节结构与图注。

## 1. 标题
- "[主题] in [范式] ([缩写])"，7 词。原理 / 教程型文章用宽泛主题名，不出现方法或结果。

## 2. 摘要（5 句，111 词）
- 两句背景（5G 将包含 URLLC；高可靠与低时延的耦合使接入设计困难）→ "This paper aims to provide a broad perspective on the fundamental tradeoffs in URLLC, …" → "Two specific technologies are considered …" → "This paper also touches on …"。三句以 "This paper" 为主语、动词为 aims to provide / considers / touches on——综述 / 教程的典型锚点，没有结果句。

## 3. 引言（4 段）
- 无线连接成为"商品"→ URC 概念 → 5G 三类业务与 URLLC 的耦合 → 本文定位："The objective is to provide the reader with a framework that can be used to analyze and design ultra-reliable wireless systems."
- 与自己前作 [2] 的关系（"can be seen as a predecessor of this work"）+ 明确不讲什么（短包传输细节）。
- 一句提出被忽视的问题："what are the statistical requirements to measure and verify ultra-reliability?"
- 路线图逐节说明每节作用。

## 4. 章节组织
- 用例与需求 → 通信理论原理（时延-可靠性关系、五变量权衡、短包结构）→ 接入网络（确定 / 随机到达、四步 / 三步 / 免授权接入、帧同步）→ 大规模天线 → 多连接 / 接口分集 → 超可靠的统计问题 → 相关工作（3GPP、用例、统计、分集、接入、massive MIMO，2400 词）→ Discussion and Outlook。
- 每个技术节内有小算例（帧同步上界、2 用户 SINR / PER、可靠性串并联模型、速率选择的 Monte Carlo），但没有"本文方案 vs 基准"的结构。

## 5. 图表
- 12 图 1 表：概念关系图（Fig. 1 中断、可靠性、时延、截止时间的关系）、包格式示例、带宽-SNR 曲线、帧同步示意、工厂场景、DC / 接口分集架构图、端到端中断曲线。
- caption 自含设置参数（如 "The latency is set to T = 1 ms and the reliability to 1–10^-5."）。

## 6. 对 skill 的意义
- 区分"研究论文"与"原理 / 教程型期刊长文"：后者摘要无结果句、引言无贡献列表、相关工作单列且放在最后、以 "Discussion and Outlook" 收尾；即使有公式和数值例，也不形成"提出方案 → 对比基准"的论证链。
