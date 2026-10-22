---
doi: 10.1109/jsac.2022.3156632
title: "Integrated Sensing and Communications: Toward Dual-Functional Wireless Networks for 6G and Beyond"
journal: JSAC
year: 2022
band: 2022-2025
cites: 4036
cites_per_year: 929.6
article_type: overview      # JSAC 专刊综述（"In this IEEE JSAC Special Issue overview, we provide a comprehensive review …"）
topic: ISAC-sensing
source: xplore-html
xplore: 9737357
auto:
  words_total: 22832
  n_sections: 9
  n_subsections: 92
  n_figures: 21
  n_tables: 4
  n_display_eq: 79
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 27.2
  we_per_1k: 4.9
  title_words: 12
  abstract_words: 231
  abstract_sentences: 9
code:
  title_pattern: [colon-subtitle, toward]
  abstract_moves: [context, context, aim, aim, aim, aim, aim, aim, aim]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 20
  intro_moves: [field, field, tech, prior, prior, prior, prior, prior, prior, prior, prior, prior, prior, prior, prior, prior, aim, aim, roadmap, prior]
  related_work: table             # Table I 列出已有 ISAC 综述，引言末段逐篇说明差异
  contrib_format: none
  contrib_n: 0
  contrib_verbs: []
  contrib_quantified: false
  first_claim: false
  roadmap: true                   # "D. Structure of the Paper"，并配一张结构图（Fig. 3）
  notation: none
  gap_type: [unification]
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
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 5
  conclusion_has_numbers: false
  conclusion_future_work: true
---

> 本卡只做结构与写法层面的记录（overview 不参与研究论文的统计）；只抽取了摘要、引言、章节结构与图注。

## 1. 标题
- "[领域名]: Toward [愿景] for 6G and Beyond"，12 词。综述标题 = 领域全称 + "Toward …" 愿景副标题。

## 2. 摘要（9 句，231 词）
- 两句背景（5G 标准化已定 → 猜测 6G；感知成为 6G RAN 的关键特征）→ "In this IEEE Journal on Selected Areas in Communications (JSAC) Special Issue overview, we provide a comprehensive review on the background, range of key applications and state-of-the-art approaches …"
- 之后每句对应一节，动词序列：commence by discussing → shed light on → analyze → discuss → provide our vision → identify。全摘要是"导览"，没有结果。

## 3. 引言（20 段，约 2650 词，4 个小节）
- A. 背景与动机：B5G/6G 应用需要通信 + 感知 → 技术趋势（高频、大阵列）使两者趋同 → 信息处理上的本质区别 → ISAC 的多种旧称（RadCom、JCR、JRC、DFRC …）。
- B. 历史视角（4 个小小节）：1960 年代最早的脉冲间隔调制 → 早期雷达 → 雷达与通信相互启发（相控阵 → MIMO；OFDM 雷达；DARPA SSPARC）→ 平行发展（massive MIMO 与 phased-MIMO 雷达同年诞生）→ 汇聚；Fig. 2 时间线图。
- C. 范式转变：给出 ISAC 的正式定义，并区分两种增益（integration gain / coordination gain）。
- D. 结构：逐节导览 + 与已有综述的区别（Table I）。

## 4. 章节组织
- 应用与产业进展（7 个案例 + 标准化）→ 性能权衡（指标 → 信息论极限 → PHY → 空间自由度 → 跨层）→ 波形设计（非重叠资源分配 / 统一波形：感知中心、通信中心、联合设计）→ 接收信号处理 → 通信辅助感知（感知网络）→ 感知辅助通信（波束训练、跟踪、资源分配、物理层安全）→ 与其他新技术（边缘智能、RIS、UAV）→ 结论。
- 每个技术节都以 "Summary and Open Challenges" 小节收尾，列出 2–3 个带编号的开放问题——综述"每节自带未来方向"的结构。

## 5. 图表
- 21 图 4 表。Fig. 1 ISAC 全景概念图；Fig. 2 历史时间线；Fig. 3 "Framework of ISAC technologies and structure of the paper"（把技术框架与论文结构画在一张图里）；其余多为原理示意（状态相关信道、分辨单元、旁瓣控制波束、索引调制、OFDM 信号处理流程）。caption 均为短标签。
- 表：已有综述对比（Table I）、案例与 KPI（Table II）等。

## 6. 对 skill 的意义
- 综述引言用"历史叙事"建立领域合法性（几十年、多个名字、两条技术线汇聚），再给出正式定义与"增益"概念，最后用对比表说明与已有综述的区别。
- 结论 5 段，逐段对应正文模块，以 "We firmly believe that ISAC will …" 的展望句收尾。
