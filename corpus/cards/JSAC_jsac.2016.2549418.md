---
doi: 10.1109/jsac.2016.2549418
title: "Energy-Efficient Hybrid Analog and Digital Precoding for MmWave MIMO Systems With Large Antenna Arrays"
journal: JSAC
year: 2016
band: 2016-2018
cites: 976
cites_per_year: 92.9
article_type: research
topic: mmWave-THz
source: xplore-html
xplore: 7445130
auto:
  words_total: 6038
  n_sections: 5
  n_subsections: 5
  n_figures: 10
  n_tables: 1
  n_display_eq: 39
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 2, corollary: 0, constraint: 3, proof: 2, proof_in_appendix: 2}
  n_appendix: 2
  mean_sentence_words: 30.0
  we_per_1k: 13.3
  title_words: 14
  abstract_words: 240
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 8, contribList: 1, roadmap: 1, however: 4, transition: 7, resultsShow: 1, motivatedBy: 2, toAddress: 3, gapWord: 0, nonconvex: 3, npHard: 0, closedForm: 0, outperform: 1, intensifier: 2, worthNoting: 3, observe: 12, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 9, promising: 1, gen: 1, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 4, wlog: 2, code: 0, prototype: 0}
  methods: {complexity: 25, convergence: 3, compressedSensing: 1}
code:
  title_pattern: [X-for-Y, X-with-Y]
  abstract_moves: [context, gap, aim, method, theory, method, result, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper
  intro_paragraphs: 7
  intro_moves: [field, tech, gap, contrib, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: numbered
  contrib_n: 3
  contrib_verbs: [propose, prove, propose]
  contrib_quantified: true
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [limitation, tool-transfer]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [decomposition, closed-form]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4
  baseline_naming: descriptive
  x_axes: [SNR, number-of-antennas, CSI-accuracy, number-of-RF-chains]
  fig1_role: architecture
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: true
  conclusion_future_work: true
---

## 1. 标题
- "Energy-Efficient [技术] for [系统] With [规模条件]"，14 词。目标（能效）前置做形容词，与 Zeng 2017 UAV 能效论文同一骨架。

## 2. 摘要（8 句，240 词）
- 首句同时交代背景和动机（混合预编码为了省 RF 链能耗）→ 第 2 句 "However, most hybrid precoding techniques consider a fully connected architecture requiring a large number of phase shifters, which is also energy-intensive."
- "In this paper, we focus on the more energy-efficient hybrid precoding with subconnected architecture, and propose …"
- 方法来源点名："Inspired by the idea of SIC for multiuser signal detection, we first propose to decompose …"
- 结果带量化："the complexity of SIC-based hybrid precoding is only about 10% as complex as that of the recently proposed spatially sparse precoding"。

## 3. 引言逻辑（7 段，约 840 词，较短）
1. mmWave + massive MIMO 的互补（On one hand / On the other hand）。
2. 数字预编码的能耗用具体数字说明（"about 250 mW per RF chain"，64 天线需 16 W）→ 混合预编码的核心思想。
3. 已有混合预编码分两类（稀疏近似 / 码本）→ "However, these algorithms are all designed for … the fully-connected architecture" → 用编号列出全连接结构的三个代价 1)–3) → 子连接结构更节能 → "Unfortunately, designing the optimal hybrid precoding with the sub-connected architecture is still a challenging problem …, since such architecture changes the constraints on the original problem …"
4. "In this paper, we propose …" + 3 条编号贡献（第 3 条含 10% 复杂度数字）。
5. 单独一段首创声明："It is worth pointing out that to the best of the authors' knowledge, our work in this paper is the first one that considers …"
6. 路线图；7. Notation。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（全连接结构能耗大）+ 工具迁移（把多用户检测里的 SIC 思想搬到预编码设计）。
- 核心洞见：子连接结构使预编码矩阵块对角，可以按子阵列逐个优化（像 SIC 逐个检测用户一样逐个"消去"），每个子问题等价于找离无约束最优解最近的可行向量（Proposition 1）。
- 用"三个约束"（statement 块 Constraint 1–3）把子连接结构的特殊性形式化，说明为什么已有算法不适用。

## 5. 科研方法
- 先列出三个约束（块对角、等幅、功率）→ 总速率按子阵列分解（SIC 结构）→ 子问题闭式（Proposition 1）→ 用幂迭代代替 SVD、用 Proposition 2 的秩一更新代替矩阵求逆 → 复杂度按乘法 / 除法次数逐项统计（Table I），并提到硬件实现时除法代价高。
- 2 个命题，证明都在附录。

## 6. 仿真与实验
- 基准：全连接的空间稀疏预编码与无约束最优、子连接的传统模拟预编码与无约束最优——两种架构各给一个上界。
- 依次：完美 CSI 下速率（两种规模）、天线数、用户天线数、非完美 CSI、有限字母输入（BPSK）、能效 vs RF 链数（功耗参数逐个给出处）。
- 结果写法："We observe from Fig. 3 that …"（observe 出现 12 次）。

## 7. 图表
- 10 图 1 表。Fig. 1 两种混合预编码架构对比（a)(b) 子图），Fig. 2 SIC 结构框图。caption 描述型，标注系统规模。

## 8. 句式库
- 用数字说明代价："… whose energy consumption is a large part (about 250 mW per RF chain [9]) of the total energy consumption at mmWave frequencies …"
- 编号列代价："… which may bring three additional limitations: 1) …; 2) …; 3) …"
- 已有方法不适用的原因："… since such architecture changes the constraints on the original problem of hybrid precoding with the fully-connected architecture."
- 方法来源："Inspired by the idea of SIC derived for multi-user signal detection [21], we propose to decompose …"
- 首创："It is worth pointing out that to the best of the authors' knowledge, our work in this paper is the first one that considers …"

## 9. 结论
- 1 段 158 词：过去时按步骤复述（first showed / Then, we proved / Finally, … was proposed）→ 重复 10% 复杂度数字 → 一句未来工作（有限反馈、相位量化）。
