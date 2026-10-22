---
doi: 10.1109/twc.2016.2531652
title: "Unmanned Aerial Vehicle With Underlaid Device-to-Device Communications: Performance and Tradeoffs"
journal: TWC
year: 2016
band: 2016-2018
cites: 1113
cites_per_year: 107.6
article_type: research
topic: UAV
source: xplore-html
xplore: 7412759
auto:
  words_total: 8451
  n_sections: 6
  n_subsections: 9
  n_figures: 16
  n_tables: 2
  n_display_eq: 37
  n_algorithms: 0
  statements: {theorem: 3, lemma: 0, proposition: 1, corollary: 0, remark: 1, proof: 4, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 23.8
  we_per_1k: 10.3
  title_words: 10
  abstract_words: 254
  abstract_sentences: 10
  phrases: {toTheBest: 1, inThisPaper: 3, contribList: 1, roadmap: 1, however: 19, transition: 26, resultsShow: 0, motivatedBy: 0, toAddress: 2, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 1, outperform: 0, intensifier: 5, worthNoting: 1, observe: 14, thisIsBecause: 0, asExpected: 4, insight: 0, tradeoff: 6, figVerb: 0, promising: 0, gen: 0, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 0, wlog: 0, code: 0, prototype: 0}
  # figVerb 0：本文写 "Figure 6 illustrates …"（全拼 Figure），提取器只匹配 "Fig."
  methods: {stochGeom: 2}
code:
  title_pattern: [X-with-Y, colon-subtitle]
  abstract_moves: [aim, aim, theory, method, theory, method, theory, result, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper    # 被动式："In this paper, the deployment of … is analyzed."
  intro_paragraphs: 8
  intro_moves: [field, prior, prior, gap, gap, contrib, contrib, roadmap]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 5
  contrib_verbs: [analyze, derive, find, compute, show]
  contrib_quantified: true     # "to increase the DU coverage probability from 0.4 to 0.7, the number of stop points should be increased from 5 to 23"
  first_claim: true
  roadmap: true
  notation: none
  gap_type: [new-scenario, theory-gap]
  motivating_figure: true
  problem_class: analysis-only
  solution: [stochastic-geometry]
  theory_role: central
  proofs_location: appendix
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 0               # 无对比方案，仿真只用来验证解析结果
  baseline_naming: none
  x_axes: [SINR-threshold, user-density, distance, altitude, coverage-probability, retransmissions]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[主体] With [共存对象]: Performance and Tradeoffs"，10 词。副标题 "Performance and Tradeoffs" 直接告诉读者这是分析型论文（不提方案）。

## 2. 摘要（10 句，254 词）
- 被动语态锚点："In this paper, the deployment of an unmanned aerial vehicle (UAV) as a flying base station … is analyzed."；第 2 句交代共存场景。
- "For this model, a tractable analytical framework for the coverage and rate analysis is derived." → "Two scenarios are considered: a static UAV and a mobile UAV." → 每个场景一句结论性的推导内容 → 重传下的 D2D 中断。
- 三句结果："Simulation and analytical results show that, depending on the density of D2D users, the optimal values for the UAV altitude … exist." → 移动可降低总功率 → 覆盖-时延权衡。无数字。

## 3. 引言逻辑（8 段，约 1610 词）
1. UAV 作空中基站的价值：LoS、敏捷部署 → "On the one hand … On the other hand …"（热点 / 应急）→ IoT → 偏远地区 → 列出待解决的技术挑战。
2. 已有工作主体：空对地信道建模。
3. 部署相关文献逐条评述，每条后紧跟 "However, …" 指出不足（确定性覆盖、只有仿真、无覆盖分析、仅 ad-hoc）。
4. D2D 的价值与底层复用 → 干扰管理挑战 → D2D 与蜂窝 / massive MIMO 共存文献 → "However, none of these prior work studied the coexistence of UAVs and underlaid D2D communications."
5. "Compared to the previous studies …, the presence of an aerial UAV base station along with D2D links introduces new challenges. First, … Second, … Third, …"（信道、可调高度、移动性）→ 首创："To our best knowledge, this paper will provide the first comprehensive fundamental analysis …"
6–7. 两段散文贡献（静态 / 移动场景各一段），含具体数字（0.4 → 0.7 需 5 → 23 个停靠点；D2D 用户 50 → 100 需 20 → 55 个停靠点）。
8. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：新场景（UAV 与底层 D2D 共存）+ 理论缺口（已有 UAV 部署工作为确定性覆盖或纯仿真）。
- 写法亮点：用"新挑战三连"（First/Second/Third）说明为什么已有地面 D2D 共存分析不能直接套用——差异来自 UAV 的三个物理特性（概率 LoS 信道、高度可调、可移动）。
- 把"移动 UAV 覆盖整个区域"映射为经典的圆盘覆盖问题（Fig. 2），借用几何结果得到最少停靠点。

## 5. 科研方法
- 模型：半径 R_c 的圆形区域；下行用户均匀分布，D2D 对服从 PPP（固定收发距离 d_0）；空对地信道为概率 LoS / NLoS + 不同路损，D2D 为 Rayleigh 衰落。
- 静态 UAV：D2D 覆盖概率（Theorem 1，Remark 1 特例退化为无 UAV 的 overlay D2D）→ 下行覆盖概率上下界（Theorem 2）与弱干扰下的精确式（Proposition 1）→ 系统和速率 → 由表达式讨论高度、面积、密度的影响（"From this theorem, we can make several key observations."）。
- 移动 UAV：由覆盖概率要求得覆盖半径 → 圆盘覆盖求最少停靠点（Table I 给 n 个圆盘的半径）→ M 次重传下 D2D 总中断（Theorem 3）。
- 证明集中在一个附录（Theorem 1–3）。

## 6. 仿真与实验
- "First, we compare our analytical results of the coverage probabilities with the simulation results."——仿真的首要任务是验证解析式；参数表 Table II（"set based on typical values such as in [9] and [20]"）。
- 无对比方案；按场景分两小节，逐图给"参数 → 趋势 → 原因"，大量 "As expected"（4 次）与 "we can see that"。
- 关键发现以数字给出（如最优高度约 300/350/400 m 对应 d_0 = 20/25/30 m）。

## 7. 图表
- 16 图 2 表。Fig. 1 网络模型；Fig. 2 五圆盘覆盖示意；Fig. 3 时延随停靠点增加（方法节内的概念图）。
- 结果 caption 一律短标签 "Y vs. X."（"Coverage probability vs. UAV altitude."），正文用 "Figure N shows …" 全拼。

## 8. 句式库
- 应用铺陈："On the one hand, UAV-based aerial base stations can be deployed to enhance the wireless capacity and coverage at temporary events or hotspots …"
- 逐条评述："However, the results presented in [11] are based on simulations and there is no significant analytical analysis."
- 共存空白："However, none of these prior work studied the coexistence of UAVs and underlaid D2D communications."
- 新挑战："… the presence of an aerial UAV base station along with D2D links introduces new challenges."
- 首创："To our best knowledge, this paper will provide the first comprehensive fundamental analysis on the performance of UAV communication in the presence of underlaid D2D links."
- 量化权衡："… to increase the DU coverage probability from 0.4 to 0.7, the number of stop points should be increased from 5 to 23."
- 补充（skill 引用）："Network model including a UAV, downlink users and D2D."
- 补充（skill 引用）："The work in [16] proposed a power efficient deployment and cell association for multiple UAVs in downlink transmissions."
- 补充（skill 引用）："The rest of this paper is organized as follows."
- 补充（skill 引用）："As expected, the total delay increases as the number of stop points increases."

## 9. 结论
- 1 段 206 词，现在完成时（"we have studied / have derived / have shown"）逐条复述两场景的结论 → 以覆盖-时延权衡收尾。无数字、无未来工作。
