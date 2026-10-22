---
doi: 10.1109/tcomm.2020.2973976
title: "Joint Radar and Communication Design: Applications, State-of-the-Art, and the Road Ahead"
journal: TCOM
year: 2020
band: 2019-2021
cites: 2020
cites_per_year: 318.5
article_type: overview      # 混合体：前半为综述（应用 + 文献），后半提出 mmWave DFRC 基站的新收发架构并给仿真
topic: ISAC-sensing
source: xplore-html
xplore: 8999605
auto:
  words_total: 15714
  n_sections: 9
  n_subsections: 52
  n_figures: 13
  n_tables: 4
  n_display_eq: 85
  n_algorithms: 3
  statements: {theorem: 0, lemma: 0, proposition: 2, corollary: 0, remark: 7, proof: 2, proof_in_appendix: 0}
  n_appendix: 2
  mean_sentence_words: 26.9
  we_per_1k: 8.1
  title_words: 11
  abstract_words: 368
  abstract_sentences: 13
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [context, context, gap, aim, method, method, method, method, method, method, result, result, implication]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper    # "In the first part of this paper, we overview … In the second part, we propose …"
  intro_paragraphs: 22
  intro_moves: [field, field, field, prior, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech, tech]
  related_work: separate-section    # "Literature Review" 单列一节（约 4400 词，RCC / DFRC 分组）
  contrib_format: paragraph
  contrib_n: 0
  contrib_verbs: []
  contrib_quantified: false
  first_claim: true                 # toTheBest 2 次
  roadmap: true
  notation: table                   # Table I 缩写表 + Table II 记号表
  gap_type: [unification, new-architecture]
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
  fig1_role: framework              # Fig. 1 为 DFRC 技术演进时间线
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 6
  conclusion_has_numbers: false
  conclusion_future_work: true
---

> 本卡只做结构与写法层面的记录（overview 不参与研究论文的统计）；只抽取了摘要、引言、章节结构与图注。

## 1. 标题
- "[领域]: Applications, State-of-the-Art, and the Road Ahead"，11 词。与 JSAC 的 RIS 长综述同款"三段式目录副标题"。

## 2. 摘要（13 句，368 词，语料中最长之一）
- 三句背景（频谱共享 → 硬件共享 → "Nevertheless, the success … critically depends on high-quality joint radar and communication designs."）。
- "In the first part of this paper, we overview …" / "In the second part, we propose a novel transceiver architecture and frame structure …"——明确把论文分为"综述 + 原创"两部分。
- 原创部分 6 句方法（目标搜索与信道估计、混合波束成形、接收机、角度跟踪）+ 结果 + "Finally, the paper concludes with an overview of the open problems …"。

## 3. 引言（22 段，约 2430 词）
- A. Background：频谱拥挤与拍卖价格 → 雷达的发展与应用 → CRSS 的两条研究方向（RCC 共存 / DFRC 双功能）。
- B. Civilian Applications（5 类：共存、5G mmWave 车联网定位、Wi-Fi 室内定位与行为识别、UAV、其他）与军事应用（多功能射频、军用 UAV、雷达辅助 LPI 通信、无源雷达），Table III / IV 汇总。
- 应用驱动的综述引言：先讲"用在哪"，再讲"怎么做"。

## 4. 章节组织
- 文献综述（RCC：机会频谱接入、干扰信道估计、闭式预编码、优化设计、接收机；DFRC：时间线 Fig. 1）→ 系统模型 → DFRC 框架（三阶段）→ 阶段 1 目标搜索与信道估计 → 阶段 2 发射波束成形与下行 → 阶段 3 目标跟踪与上行 → 数值结果 → 结论与未来研究（总结 + 4 个编号方向：学习型 CRSS、安全、V2X、信息论）→ 两个附录证明。

## 5. 图表
- 13 图 4 表 3 算法。前 4 张表都在引言（缩写、记号、共存案例、应用汇总）；Fig. 1 时间线；Fig. 3 帧结构 + 信号处理流程；结果图含波束图、谱效率-目标数权衡、角度跟踪 RMSE。caption 短标签。

## 6. 对 skill 的意义
- "综述 + 原创方案"的混合型期刊长文：摘要和引言都用 "first part / second part" 显式分界；综述部分按应用场景与技术路线双维度组织，原创部分沿用研究论文的"模型 → 框架 → 分阶段设计 → 仿真"结构。
- 结论单独设 "Future Works" 小节、带粗体编号标题，是综述结尾的常见形式。
