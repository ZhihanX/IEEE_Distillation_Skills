---
doi: 10.1109/tcomm.2019.2958916
title: "Beamforming Optimization for Wireless Network Aided by Intelligent Reflecting Surface With Discrete Phase Shifts"
journal: TCOM
year: 2020
band: 2019-2021
cites: 1223
cites_per_year: 185.5
article_type: research
topic: RIS
source: xplore-html
xplore: 8930608
auto:
  words_total: 8812
  n_sections: 6
  n_subsections: 14
  n_figures: 9
  n_tables: 1
  n_display_eq: 34
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 1, corollary: 0, definition: 1, remark: 2, proof: 1, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 31.8
  we_per_1k: 9.4
  title_words: 14
  abstract_words: 291
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 0, roadmap: 1, however: 7, transition: 19, resultsShow: 2, motivatedBy: 1, toAddress: 5, gapWord: 0, nonconvex: 4, npHard: 3, closedForm: 1, outperform: 4, intensifier: 8, worthNoting: 3, observe: 7, thisIsBecause: 1, asExpected: 0, insight: 2, tradeoff: 2, figVerb: 0, promising: 0, gen: 0, contrast: 5, firstTime: 1, novel: 0, weProposeFirst: 4, wlog: 1, code: 0, prototype: 0}
  methods: {BnB: 4, SDR: 1, convexOpt: 1, convergence: 8, complexity: 10}
code:
  title_pattern: [X-for-Y, X-aided-Y, X-with-Y]
  abstract_moves: [context, gap, aim, aim, method, method, theory, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [tech, prior, tech, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 5
  contrib_verbs: [show, propose, show, extend, show]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [practicality, theory-gap]
  motivating_figure: true
  problem_class: MINLP
  solution: [BnB, BCD, closed-form]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 4
  baseline_naming: descriptive
  x_axes: [distance, number-of-elements, SINR-target, number-of-users]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- 14 词，"Beamforming Optimization for [系统] Aided by [器件] With [实际约束]"。贡献点（离散相移）放在最后的 With 短语里。

## 2. 摘要（9 句，291 词，偏长）
- 1 背景（IRS 低成本、高能效）→ 2 空白："Prior works on IRS mainly consider continuous phase shifts at reflecting elements, which are practically difficult to implement due to the hardware limitation." → 3 "In contrast, we study in this paper …"（用 In contrast 直接接空白句）→ 4 "We aim to minimize …" → 5 MINLP 难解 → 6 先单用户（最优 + 次优）→ 7 理论结论（离散相移仍有平方增益，只损失常数）→ 8 推广到多用户 → 9 仿真验证。
- 先单用户后多用户、先最优后低复杂度，是这类优化论文的标准推进顺序。

## 3. 引言逻辑（8 段，约 2000 词，很长）
1. 技术：massive MIMO 的成本 / 能耗瓶颈 → IRS 作为新方案，逐条列特点（低成本、覆盖小易部署、轻薄、无需改动现有硬件）；最后一句交代同义术语。
2. 已有工作：O(N²) 平方增益（并解释为什么比 massive MIMO 和中继大）、"interference-free zone"，再列其他场景（安全、SWIPT、NOMA）。
3. 硬件：超表面、PIN 二极管怎么实现相移、开关速度、功耗——为下一段的"离散相移"埋伏笔。
4. 空白："The existing works … are mainly based on the assumption of continuous phase shifts … However, in practice, this is difficult to realize …"，再用 PIN 二极管数量举例；最后提出两个未知问题（平方增益是否仍成立、如何联合设计）。
5. 目标："Motivated by the above, we study in this paper …" → 问题 → MINLP、NP-hard。
6. 方法与结论：一段散文式贡献（无 bullet），依次讲 ILP + 分支定界最优解、逐元素 successive refinement、渐近分析、多用户扩展、仿真结论。
7. 路线图；8. Notations 段。

## 4. Idea 是怎么提出的
- 空白类型：实用性（连续相移不可实现）+ 理论缺口（离散后增益阶数是否保持）。
- 写法亮点：用一整段硬件实现细节为"实用性空白"提供可信度，再把空白落到两个可回答的问题上（"it remains unknown whether …, as well as how …"）。
- 核心结论句："the power loss due to discrete phase shifts … approaches a constant in dB that depends only on the number of phase-shift levels at each element, but regardless of N"。

## 5. 科研方法
- 单用户：MRT 是最优预编码 → 问题化为离散相位选择 → 用 SOS1 写成 ILP → 分支定界求全局最优；低复杂度版逐元素轮流优化（successive refinement）。
- 渐近分析：Proposition 1，随 N→∞ 的功率损失只与相位级数有关；Table I 列出 1/2/3 bit 的损失。
- 多用户：最优解（给定相位时 SOCP / SDP 求预编码 + 分支定界）与 ZF + successive refinement 次优解。
- 复杂度讨论贯穿（指数 vs 多项式）。

## 6. 仿真与实验
- 3D 坐标布局图（Fig. 2、Fig. 5）先交代几何，再给结果；参数写在正文。
- baseline：无 IRS、量化法（先求连续再量化）、码本法、连续相移上界；多用户里还比较 ZF 与 MMSE。
- 最后一个实验"IRS-aided small MIMO versus large MIMO without IRS"把结论落到成本论证上。

## 7. 图表
- 9 图 1 表。Fig. 1 系统图里嵌了一个单元结构（PIN 二极管）示意。
- caption 是 "Y versus X" 的短标签："AP transmit power versus the number of reflecting elements."

## 8. 句式库
- 空白："The existing works … on IRS-aided wireless communications are mainly based on the assumption of continuous phase shifts at its reflecting elements."
- 未知问题："Besides, it remains unknown whether the 'squared power/SNR gain' revealed in [7] still holds for the case of IRS with discrete phase shifts, …"
- 困难声明："… rendering the formulated optimization problem a mixed-integer non-linear program (MINLP) that is NP-hard and thus difficult to solve in general."
- 降复杂度："To reduce the computational complexity for the optimal solution, we further propose a low-complexity successive refinement algorithm …"
- 术语交代："It is worth noting that there have been other terminologies similar to IRS proposed in the literature, such as …"

## 9. 结论
- 2 段：第 1 段过去时总结（含 "Interestingly, it was shown that …" 强调反直觉结论）；第 2 段 "There are other important issues that are not addressed in this paper yet, some of which are listed as follows to motivate future works." 后接 4 条 bullet 未来方向（幅度调节、频率选择信道、多 IRS、多小区部署）。
