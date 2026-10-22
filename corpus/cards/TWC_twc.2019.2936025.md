---
doi: 10.1109/twc.2019.2936025
title: "Intelligent Reflecting Surface Enhanced Wireless Network via Joint Active and Passive Beamforming"
journal: TWC
year: 2019
band: 2019-2021
cites: 4335
cites_per_year: 626.0
article_type: research
topic: RIS
source: xplore-html
xplore: 8811733
auto:
  words_total: 10239
  n_sections: 6
  n_subsections: 15
  n_figures: 12
  n_tables: 1
  n_display_eq: 33
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 4, corollary: 0, proof: 4, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 31.6
  we_per_1k: 8.3
  title_words: 12
  abstract_words: 212
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 9, contribList: 0, roadmap: 1, however: 12, transition: 17, resultsShow: 2, motivatedBy: 2, toAddress: 2, gapWord: 0, nonconvex: 11, npHard: 0, closedForm: 3, outperform: 2, intensifier: 11, worthNoting: 6, observe: 13, thisIsBecause: 3, asExpected: 0, insight: 4, tradeoff: 2, figVerb: 0, promising: 2, gen: 1, contrast: 3, firstTime: 0, novel: 1, weProposeFirst: 3, wlog: 1, code: 0, prototype: 1}
  methods: {AO: 13, SDR: 12, convexOpt: 4, bisection: 1, convergence: 9, complexity: 6}
code:
  title_pattern: [X-aided-Y, X-via-Y]
  abstract_moves: [context, context, aim, method, theory, result, implication]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 9
  intro_moves: [field, solution, tech, gap, aim, approach, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 4
  contrib_verbs: [apply, propose, extend, demonstrate]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-architecture, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [SDR, AO, closed-form, decomposition]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 5
  baseline_naming: descriptive
  x_axes: [distance, number-of-elements, SINR-target, Rician-factor, transmit-power, delay]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[新器件] Enhanced [系统] via [方法]"，12 词。"Joint Active and Passive Beamforming" 这个短语后来成了领域标准术语——标题里造了一个可复用的概念名。

## 2. 摘要（7 句，212 词）
- 1–2 背景："IRS is a revolutionary and transformative technology for …"，第 2 句用一句话讲清 IRS 工作原理（"without the need of any transmit radio-frequency (RF) chains"）。
- 3 "In this paper, we study an IRS-aided single-cell wireless system where …"；4 "We formulate and solve new problems to minimize …"。
- 5 渐近分析并与传统有源波束成形 / 中继比较。
- 6 结果用对比而非数字："can achieve the same rate performance as a benchmark massive MIMO system without using IRS, but with significantly reduced active antennas/RF chains."
- 7 "We also draw useful insights into optimally deploying IRS in future wireless systems."（以"洞见"收尾）。

## 3. 引言逻辑（9 段，约 1950 词）
1. 领域与痛点：5G 三大技术（UDN、massive MIMO、mmWave）→ "However, the network energy consumption and hardware cost still remain critical issues" → 举例逐一说明 → "innovative research on … is still imperative"。
2. 方案："In this paper, intelligent reflecting surface (IRS) is proposed as a promising new solution to achieve the above goal." → 解释为什么以前反射面没用于移动通信、现在为什么可以（MEMS / 超表面）。
3. 区分："It is worth noting that the proposed IRS differs significantly from …"，用 First / Second / Third 分别对比 AF 中继、反向散射、有源智能表面，并给出对比表 Table I。
4. 部署优势 + 实测佐证 → "However, the research on IRS design … is still in its infancy, which thus motivates this work."
5. 系统与问题：单用户的直觉解释（直连强则对准用户，被遮挡则对准 IRS，"creating a virtual LoS link"）。
6. 多用户的额外好处（干扰抑制）→ 难点（非凸 SINR + 单位模约束）→ 已有单位模设计只在收或发一侧，"not applicable to our considered joint active and passive beamforming optimization"。
7. 方法与结论（散文式贡献）+ 与最相近工作 [15] 的两点区别（First / Second）。
8. 路线图；9. Notations。

## 4. Idea 是怎么提出的
- 空白类型：新架构（研究"尚处起步阶段"）+ 已有方法不适用。
- 两个写法亮点：一是用对比表把新器件和三类相近技术逐项区分（防审稿人说"这就是中继"）；二是在形式化之前先给物理直觉（单用户时 AP 该对准谁）。
- 和最相近工作逐点区分："This paper differs from [15] in the following two main aspects. First, … Second, …"

## 5. 科研方法
- 模型：单小区、多天线 AP、IRS、K 个单天线用户；忽略二次及以上反射；线性预编码。
- Proposition 1：可行性条件（秩条件），并指出 IRS 让条件更易满足。
- 单用户：SDR 求近似解并给出下界（用于评估其他算法差距）→ 交替优化，各子问题闭式解 → Proposition 2/3：IRS 的 N² 功率缩放 vs FD AF 中继的 N。
- 多用户：交替优化（MMSE 预编码 + 相位，Proposition 4 单调收敛）和两阶段算法（低复杂度），给出"性能—复杂度"折中。

## 6. 仿真与实验
- 3D 坐标、ULA + URA、路损模型写在正文；先单用户后多用户。
- baseline：SDR 下界、AP-user MRT、AP-IRS MRT、随机相位、无 IRS、FD/HD AF 中继、massive MIMO。
- 有一张"机理可视化"图（Fig. 9：AP 波束方向与 IRS 协作方式随 SINR 的变化），解释算法"为什么"有效。
- 最后考虑 IRS 带来的时延开销（delay ratio），讨论实际代价。

## 7. 图表
- 12 图 1 表（引言里的技术对比表）。caption 全是短标签："AP transmit power versus the number of reflecting elements at the IRS, N."

## 8. 句式库
- 痛点："However, the network energy consumption and hardware cost still remain critical issues in practical systems."
- 提出方案："In this paper, intelligent reflecting surface (IRS) is proposed as a promising new solution to achieve the above goal."
- 区分相近技术："It is worth noting that the proposed IRS differs significantly from other related existing technologies such as …"
- 研究起步："However, the research on IRS design … is still in its infancy, which thus motivates this work."
- 已有方法不适用："… such designs are mainly restricted to either the transmitter or the receiver side, which are not applicable to our considered …"
- 解释结果："This is because the user farther away from the AP may be closer to the IRS and thus it is able to receive stronger reflected signal from the IRS."

## 9. 结论
- 2 段 416 词：第 1 段过去时总结方法与发现（单用户 N²、多用户干扰抑制、部署洞见）；第 2 段讨论信道估计这一未解决问题，并说明投稿日期之后才看到的同期工作（"after the initial version of this paper was submitted on October 12, 2018, we became aware of another parallel work [28]"）——一种保护首发权的写法。
