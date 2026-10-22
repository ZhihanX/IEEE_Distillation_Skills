---
doi: 10.1109/twc.2021.3118225
title: "Simultaneously Transmitting and Reflecting (STAR) RIS Aided Wireless Communications"
journal: TWC
year: 2022
band: 2022-2025
cites: 921
cites_per_year: 208.1
article_type: research
topic: RIS
source: xplore-html
xplore: 9570143
auto:
  words_total: 7868
  n_sections: 6
  n_subsections: 26
  n_figures: 8
  n_tables: 2
  n_display_eq: 31
  n_algorithms: 3
  statements: {theorem: 1, lemma: 1, proposition: 0, corollary: 0, remark: 3, proof: 2, proof_in_appendix: 1}
  n_appendix: 1
  mean_sentence_words: 26.4
  we_per_1k: 7.3
  title_words: 9
  abstract_words: 256
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 5, contribList: 1, roadmap: 2, however: 14, transition: 12, resultsShow: 2, motivatedBy: 4, toAddress: 10, gapWord: 0, nonconvex: 18, npHard: 0, closedForm: 0, outperform: 5, intensifier: 2, worthNoting: 0, observe: 3, thisIsBecause: 4, asExpected: 0, insight: 2, tradeoff: 0, figVerb: 2, promising: 2, gen: 1, contrast: 7, firstTime: 0, novel: 3, weProposeFirst: 2, wlog: 1, code: 0, prototype: 2}
  methods: {penalty: 16, convexOpt: 8, SCA: 6, SDR: 4, BnB: 2, AO: 1, DRL: 1, lagrange: 1, convergence: 4, complexity: 12}
code:
  title_pattern: [X-aided-Y, noun-phrase]
  abstract_moves: [aim, method, method, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: none
  intro_paragraphs: 7
  intro_moves: [field, tech, prior, gap, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, formulate, develop, unveil]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [limitation, new-architecture]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [penalty, SCA, SDR, decomposition]
  theory_role: supporting
  proofs_location: mixed
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [iterations, number-of-elements, number-of-antennas, SINR-target]
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[新器件全称 (缩写)] Aided Wireless Communications"，9 词。标题本身就是在给新概念命名（全称 + 括号缩写）。

## 2. 摘要（8 句，256 词）
- 首句被动语态引出新概念并一句话说清机理："The novel concept of simultaneously transmitting and reflecting (STAR) reconfigurable intelligent surfaces (RISs) is investigated, where the incident wireless signal is divided into transmitted and reflected signals …"
- 第 2 句提出三种工作协议并给缩写（ES / MS / TS）；之后 "For ES, … Then, … For TS, …" 一协议一句方法。
- 结尾用编号列出发现："Finally, our numerical results reveal that: 1) … ; and 2) …"——结论型摘要结尾。

## 3. 引言逻辑（2 段 + A. Prior Works + B. Motivations and Contributions + C. Organization and Notation）
1. B5G/6G 需求 → 现有技术延伸（UM-MIMO、UDN、THz）→ "However, on the one hand, … On the other hand, …" 两方面代价。
2. "To overcome the above limitations, new cost-effective techniques have to be developed" → RIS 及其优势（与有源天线 / 中继对比）。
3. A. Prior Works：按目标分组的大段综述（功率最小化、能效 / 谱效、消除遮挡、其他场景），逐篇一句。
4. B. 空白："Most of the existing research contributions consider the case where the RISs are only able to reflect …" → 半空间限制 → STAR-RIS 概念、原型 → "Despite the above advantages, the investigation of how STAR-RISs can be integrated into wireless communication systems is still in its infancy." → 区分相近概念 IOS → "to the best of the authors' knowledge, … have not been studied, yet, which provides the main motivation for this work."
5. "To exploit the full potential of STAR-RISs, in this paper, we propose …" → 4 条贡献（最后一条是编号的数值发现）。
6. 路线图；7. Notations。

## 4. Idea 是怎么提出的
- 空白类型：已有器件局限（只能反射 → 收发必须同侧，"half-space SRE"）+ 新架构（全空间覆盖）。
- 写法亮点：用一对对立概念命名问题（half-space vs full-space），读者一眼看出新意；对最相近概念（IOS）单独说明差别。
- 本文贡献不止优化，还"提出协议"：把一个新器件的工作方式拆成 ES / MS / TS 三种可选协议，再各自优化、比较——"协议设计 + 优化 + 比较"三件套。

## 5. 科研方法
- 第 II 节：STAR 单元信号模型 → 三种协议（Fig. 2 图示 + Table I 汇总各协议的变量与约束）。
- 第 III 节：单播 / 组播两种场景下的功率最小化问题；Remark 1 归纳求解难点（比传统 RIS 多一组变量、耦合更强）。
- 第 IV 节：ES 用 DC 变换 + 罚函数 + SCA（Lemma 1、Theorem 1 秩一性）；MS 在此基础上处理二元约束；TS 分解为系数设计（引用已有 SDR / 分支定界）和凸的资源分配。
- 单列复杂度分析，收敛到驻点有保证。

## 6. 仿真与实验
- 3D 布局图 + 参数表；两个 baseline 编号命名："Baseline scheme 1 (also referred to as conventional RISs)"、"Baseline scheme 2 (also referred to as uniform energy splitting (UES))"。
- 先看收敛（含等式约束违反量），再扫元件数、天线数、QoS 要求；每张图分单播 / 组播两子图。
- 结果解释句："The reasons behind this can be explained as follows."

## 7. 图表
- 8 图 2 表 3 算法。Fig. 1 概念图在引言，Fig. 2 三种协议示意，Fig. 3 系统图，Fig. 4 仿真布局。
- caption 短标签："Power consumption versus M for N = 2."

## 8. 句式库
- 局限："In this case, transmitter and receiver have to be located on the same side of the RIS, thus leading to a half-space SRE."
- 起步阶段："Despite the above advantages, the investigation of how STAR-RISs can be integrated into wireless communication systems is still in its infancy."
- 空白 + 动机："However, to the best of the authors' knowledge, … have not been studied, yet, which provides the main motivation for this work."
- 引出本文："To exploit the full potential of STAR-RISs, in this paper, we propose …"
- 编号结论："Finally, our numerical results reveal that: 1) …; and 2) …"

## 9. 结论
- 2 段：第 1 段被动语态复述，结尾给出协议选择指南（"These insights provide useful guidelines for …"）；第 2 段两个具体未来方向（信道估计、部署），每个都说明为何对 STAR-RIS 特别困难。
