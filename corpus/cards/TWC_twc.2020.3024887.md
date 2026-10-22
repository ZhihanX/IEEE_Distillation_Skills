---
doi: 10.1109/twc.2020.3024887
title: "Wireless Communications With Reconfigurable Intelligent Surface: Path Loss Modeling and Experimental Measurement"
journal: TWC
year: 2021
band: 2019-2021
cites: 1481
cites_per_year: 257.2
article_type: research
topic: RIS
source: xplore-html
xplore: 9206044
auto:
  words_total: 7659
  n_sections: 6
  n_subsections: 22
  n_figures: 17
  n_tables: 2
  n_display_eq: 38
  n_algorithms: 0
  statements: {theorem: 1, lemma: 0, proposition: 5, corollary: 0, proof: 10, proof_in_appendix: 4}
  n_appendix: 4
  mean_sentence_words: 28.4
  we_per_1k: 4.4
  title_words: 12
  abstract_words: 192
  abstract_sentences: 6
  phrases: {toTheBest: 1, inThisPaper: 3, contribList: 1, roadmap: 3, however: 3, transition: 13, resultsShow: 0, motivatedBy: 1, toAddress: 0, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 1, intensifier: 2, worthNoting: 2, observe: 8, thisIsBecause: 1, asExpected: 0, insight: 1, tradeoff: 0, figVerb: 11, promising: 0, gen: 6, contrast: 0, firstTime: 0, novel: 0, weProposeFirst: 0, wlog: 0, code: 0, prototype: 1}
  # toTheBest 手工改为 1（原文用弯引号 authors’，旧版正则漏计）；roadmap 3 次全是 "the rest of the article" 一类误匹配，文中没有路线图段
  methods: {}
code:
  title_pattern: [X-with-Y, colon-subtitle]
  abstract_moves: [context, context, aim, theory, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 5
  intro_moves: [field, tech, tech, prior, gap, aim, contrib]
  related_work: in-intro
  contrib_format: numbered
  contrib_n: 3
  contrib_verbs: [introduce, propose, report]
  contrib_quantified: false
  first_claim: true
  roadmap: false
  notation: none
  gap_type: [practicality, theory-gap]
  motivating_figure: true
  problem_class: analysis-only
  solution: [closed-form]
  theory_role: central
  proofs_location: mixed
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 0
  baseline_naming: none
  x_axes: [distance, received-power-map, angle-of-incidence, control-voltage]
  fig1_role: system-model   # Fig. 1 是预备知识里的天线辐射方向图，Fig. 2 才是系统图
  caption_style: descriptive
  prototype_or_measurement: true
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Wireless Communications With [新技术]: [建模] and [实验测量]"，12 词。冒号后两项点明"理论 + 实测"双重贡献——在全是仿真的领域里，"Experimental Measurement" 本身就是卖点。

## 2. 摘要（6 句，192 词）
- 前两句技术背景（RIS 操纵电磁波的能力 → 低成本覆盖增强）。
- "In this article, free-space path loss models for RIS-assisted wireless communications are developed for different scenarios by studying the physics and electromagnetic nature of RISs."——被动语态锚点句。
- 模型揭示的依赖关系一口气列出（距离、尺寸、近 / 远场、辐射方向图）→ 三块加工好的 RIS 在微波暗室测量 → "The measurement results match well with the modeling results, …, which may pave the way for further theoretical studies and practical applications in this field."

## 3. 引言逻辑（5 段，约 880 词，无路线图、无记号段）
1. 5G 商用（massive MIMO、mmWave 试验）→ ITU 预测 2030 年每月 5 ZB 流量 → 6G。
2. 6G 候选技术清单（THz、UM-MIMO、AI、OAM、VLC…）→ RIS（超表面单元可实时调控幅度 / 相位 / 极化）。
3. RIS 的两种角色：新收发机架构、可编程传播环境（"RISs, on the other hand, may in principle make the wireless environment controllable and programmable, …"）。
4. "Against this background, …"：已有 RIS 工作按主题一句一类地罗列（波束、安全、速率、能效、性能分析、与中继比较、硬件非理想、信道估计）。
5. "However, the major limitation of existing research on RIS-assisted wireless communications is the lack of tractable and reliable physical and electromagnetic models for the RISs." → 首创声明（没有经实验验证的路径损耗模型）→ "Therefore, channel measurements are urgently needed, …" → "Motivated by these considerations, we develop …" → 3 条编号贡献（第 3 条 "We report the world's first experimental results …"）。

## 4. Idea 是怎么提出的
- 空白类型：实用性（已有工作把 RIS 简化为对角相移矩阵）+ 理论空白（缺少考虑尺寸、近远场的路径损耗模型）。
- 写法亮点：先用一大段"按主题罗列"显示领域繁荣，再用一句 However 指出这些工作共同依赖的模型基础不牢——繁荣 → 地基不稳的反差。
- 首创声明有两层：理论层（"there is no experimentally validated path loss model …"）+ 实验层（"world's first experimental results"）。

## 5. 科研方法
- 预备知识节（Preliminaries）：近场 / 远场、辐射方向图与增益——为通信读者补电磁背景。
- Theorem 1 给出一般公式（接收功率与各单元距离、辐射方向图、反射系数的关系）→ Proposition 1–5 分三种场景简化（远场波束、近场波束、近场广播）→ Table I 汇总各场景路径损耗模型。
- 由仿真重新界定近 / 远场边界。
- 证明部分在正文、部分在附录 A–D。

## 6. 仿真与实验
- 先数值仿真验证各公式（Table II 列出三块 RIS 与两种天线参数）。
- 再暗室测量：列出仪器型号（信号源、频谱仪）、测量系统框图 + 照片、三块超表面照片；测量结果按场景分小节，另测入射角敏感性和 RIS 功耗。
- 没有"基准方案"，比较对象是模型 vs 仿真 vs 测量。

## 7. 图表
- 17 图 2 表。大量 (a)(b)(c) 子图：功率分布热图 + 功率随 d1、d2 变化曲线；测量节含实验照片。caption 为长描述型，逐个子图交代参数（"(a) Received signal power distribution when d1 = 3.5 m and d2 = 10 m."）。

## 8. 句式库
- 指出共同局限："However, the major limitation of existing research on RIS-assisted wireless communications is the lack of tractable and reliable physical and electromagnetic models for the RISs."
- 过度简化："Most of the existing research works are based on simplistic mathematical models that regard the RIS as a diagonal matrix with phase shift values."
- 紧迫性："Therefore, channel measurements are urgently needed, which may provide authentic information on the path loss of …"
- 实验首创："We report the world's first experimental results that assess and validate the path loss of RIS-assisted wireless communications."
- 定理解读："Theorem 1 reveals that the received signal power is proportional to …"
- 价值收尾："This work can help researchers understand the fundamentals of large-scale fading in RIS-assisted wireless communication systems, …"

## 9. 结论
- 1 段 188 词，现在完成时复述（have developed / have been derived / have been conducted）→ 测量与模型吻合 → 对研究者的用处（链路预算、性能分析）→ 一句未来工作（小尺度衰落）。无数字。
