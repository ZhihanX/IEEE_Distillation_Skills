---
doi: 10.1109/tcomm.2021.3051897
title: "Intelligent Reflecting Surface-Aided Wireless Communications: A Tutorial"
journal: TCOM
year: 2021
band: 2019-2021
cites: 2941
cites_per_year: 542.1
article_type: overview      # 教程（tutorial）
topic: RIS
source: xplore-html
xplore: 9326394
auto:
  words_total: 22814
  n_sections: 7
  n_subsections: 37
  n_figures: 27
  n_tables: 4
  n_display_eq: 40
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 1, corollary: 0, remark: 1, proof: 1, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 35.6
  we_per_1k: 4.3
  title_words: 7
  abstract_words: 153
  abstract_sentences: 6
code:
  title_pattern: [X-aided-Y, colon-subtitle]
  abstract_moves: [context, context, implication, gap, aim, aim]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 13
  intro_moves: [field, gap, gap, tech, tech, tech, tech, tech, gap, prior, aim, roadmap, notation]
  related_work: table               # Table II 列出代表性综述 / 概述论文，并说明本文差异
  contrib_format: paragraph
  contrib_n: 0
  contrib_verbs: []
  contrib_quantified: false
  first_claim: true                 # "this paper is the first tutorial on IRS-aided wireless communications"
  roadmap: true
  notation: intro-end
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
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

> 本卡只做结构与写法层面的记录（overview 不参与研究论文的统计）；只抽取了摘要、引言、章节结构与图注。

## 1. 标题
- "[技术]-Aided Wireless Communications: A Tutorial"，7 词。文体名（A Tutorial）放在副标题。

## 2. 摘要（6 句，153 词）
- 技术定义 → 原理（大量低成本无源元件动态改变信道）→ 预期（有源 + 无源混合网络实现可持续容量增长）→ "Despite its great potential, IRS faces new challenges to be efficiently integrated into wireless networks, such as …"（教程也写"挑战"句）→ "In this paper, we provide a tutorial overview of …" → 未来方向。

## 3. 引言（13 段，约 2250 词，4 个小节，小节标题用问句）
- A. Motivation：6G 目标 → 已有技术（超密网络、massive MIMO、mmWave）的代价 → "it is imperative to develop disruptively new and innovative technologies …" → 时变信道带来的可靠性挑战。
- B. What is IRS?：原理（Fig. 1 主要功能）→ 实现优势（First…）→ 范式转变（Fig. 2）→ 应用全景（Fig. 3）+ Table I 产业进展与样机。
- C. What's New?：与传统超表面应用的区别 → 通信视角的新问题（Firstly 反射设计 / 信道估计 / 部署）。
- D. Objective, Contribution, and Organization：已有综述（Table II）→ "Compared with the above works, this paper is the first tutorial on IRS-aided wireless communications, with an emphasis on …" → 路线图 → Notations。

## 4. 章节组织
- 基础（信号与信道模型、硬件架构与实际约束）→ 反射优化（SISO 功率缩放律、MISO 主被动联合波束、MIMO / OFDM、多用户、离散相位、多小区）→ 信道估计（半无源 / 无源）→ 部署（链路级、网络级：分布式 vs 集中式）→ 扩展（安全、WPT、UAV、mmWave、MEC 等）→ 结论。
- 每个主要节以 "Other Related Work and Future Direction" 小节收尾，并配一张"代表性工作汇总表"（Table III 反射优化、Table IV 信道估计）。

## 5. 图表
- 27 图 4 表。除概念图外，教程中嵌入大量自做数值例子（"Achievable rate versus N …"、与 massive MIMO / AF 中继比较、部署策略比较），用来说明结论而非比较方案；末图 Fig. 27 描绘多跳反射的未来愿景。caption 为短标签。

## 6. 对 skill 的意义
- 教程与综述的区别：教程以"原理 + 典型问题的建模与求解思路 + 小算例"为主，每节有汇总表和未来方向；也可以作首创声明（"the first tutorial on …"）。
- 引言用问句小标题（What is IRS? / What's New?）组织，平均句长 35.6 词，为语料中最长之一。
