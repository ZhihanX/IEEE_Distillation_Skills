---
doi: 10.1109/jsac.2016.2525398
title: "5G-Enabled Tactile Internet"
journal: JSAC
year: 2016
band: 2016-2018
cites: 690
cites_per_year: 65.1
article_type: overview      # 选文时按研究论文入选（标题不像综述），全文为愿景 / 技术综述：0 个公式、0 个定理，按约定改记为 overview 并顺延补位
topic: other
source: xplore-html
xplore: 7403840
auto:
  words_total: 9126
  n_sections: 10
  n_subsections: 27
  n_figures: 6
  n_tables: 0
  n_display_eq: 0
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  title_words: 3
  abstract_sentences: 6
code:
  title_pattern: [noun-phrase]
  abstract_moves: [context, context, context, aim, aim, aim]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 8
  intro_moves: [field, tech, tech, gap, tech, tech, tech, roadmap]
  related_work: none
  contrib_format: none
  contrib_n: 0
  contrib_verbs: []
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: none
  gap_type: [new-scenario]
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
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 3
  conclusion_has_numbers: false
  conclusion_future_work: true
---

> 本卡只做结构与写法层面的记录（overview 不参与研究论文的统计）；只抽取了摘要、引言、章节结构与图注。

## 1. 标题
- "5G-Enabled [新概念]"，3 词。愿景型文章用最短的"使能技术 + 概念"标题。

## 2. 摘要（6 句）
- 先讲长期愿景（"democratization of skill"）→ 关键能力（实时传递触觉）→ 5G 的角色 → "This paper presents the most important technology concepts, which lay at the intersection of …" → "The paper outlines …"（列出协议、资源管理、核心网、边缘云、边缘 AI）→ "The paper also highlights the economic impact …"。三句以 "This paper / The paper" 为主语，是综述 / 愿景文的典型锚点。

## 3. 引言（8 段）
- 移动通信的社会作用 → 触觉互联网的定义与"从内容传递到技能传递"的范式转变 → ITU 的定义与需求（低时延、高可靠、高安全）→ 5G（IMT-2020）、频谱、与 LTE 紧耦合 → "we believe that 5G will play an integral part of …" → 路线图。没有"已有工作不足 → 本文贡献"的研究论文结构。

## 4. 章节组织
- 应用与服务（工业自动化、自动驾驶、机器人、医疗、VR/AR）→ 需求（超低时延、超高可靠、安全、触觉数据、边缘智能）→ 架构（主域 / 受控域 / 网络域）→ 硬件与物理层 → 无线接入（协议、资源管理）→ 网络与云 → AI 能力 → 经济影响 → 结论与未来工作。
- "按层自上而下"（应用 → 需求 → 架构 → 物理层 → 接入 → 网络 → 智能 → 经济）的综述骨架。

## 5. 图表
- 6 图 0 表 0 公式：架构功能图、5G 逻辑架构、时延目标示意、资源预留方案示意、云功能部署选项、预测式边缘 AI 示意。全部为概念图。

## 6. 对 skill 的意义
- 用于区分"研究论文"与"愿景 / 综述"两类写法：后者摘要以 "This paper presents / outlines / highlights" 串联，没有方法与结果句；引言以概念定义和需求为主，没有贡献列表。
