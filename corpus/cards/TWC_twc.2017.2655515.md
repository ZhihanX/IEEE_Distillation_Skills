---
doi: 10.1109/twc.2017.2655515
title: "Cell-Free Massive MIMO Versus Small Cells"
journal: TWC
year: 2017
band: 2016-2018
cites: 2687
cites_per_year: 280.1
article_type: research
topic: cell-free-massive-MIMO
source: xplore-html
xplore: 7827017
auto:
  words_total: 7127
  n_sections: 7
  n_subsections: 27
  n_figures: 11
  n_tables: 3
  n_display_eq: 66
  n_algorithms: 2
  statements: {theorem: 2, lemma: 0, proposition: 2, corollary: 0, remark: 8, proof: 3, proof_in_appendix: 2}
  n_appendix: 1
  mean_sentence_words: 23.3
  we_per_1k: 11.9
  title_words: 6
  abstract_words: 197
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 0, roadmap: 1, however: 5, transition: 9, resultsShow: 0, motivatedBy: 0, toAddress: 0, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 5, outperform: 4, intensifier: 7, worthNoting: 0, observe: 4, thisIsBecause: 0, asExpected: 1, insight: 3, tradeoff: 0, figVerb: 0, promising: 1, gen: 1, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 0, code: 0, prototype: 0}
  methods: {bisection: 4, convergence: 1, complexity: 1}
code:
  title_pattern: [versus]
  abstract_moves: [context, method, method, method, theory, method, result, result, result]
  abstract_has_numbers: true
  abstract_anchor: none
  intro_paragraphs: 8
  intro_moves: [tech, aim, approach, tech, gap, gap, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [consider, derive, compare, devise, compare]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-architecture, practicality, comparison]
  motivating_figure: true
  problem_class: convex
  solution: [closed-form, bisection, heuristic]
  theory_role: central
  proofs_location: mixed
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [CDF, number-of-users, number-of-APs]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "X Versus Y"，6 词，最短的一类。新概念名（Cell-Free Massive MIMO）本身就是卖点，"Versus" 预告了全文的比较结论。

## 2. 摘要（9 句，197 词）
- 没有 "In this paper"，第一句直接定义系统（"A Cell-Free Massive MIMO … system comprises …"），随后三句短句交代天线、CSI 获取、波束成形——像系统说明书。
- 第 5 句："Closed-form expressions for individual user uplink and downlink throughputs lead to max-min power control algorithms."（分析结果直接导出算法）。
- 第 7 句给一个带比较的判断："A pilot assignment algorithm helps …, but power control is far more important in that regard."
- 最后两句给数字："nearly fivefold improvement in 95%-likely per-user throughput …, and tenfold improvement when shadow fading is correlated."
- 句子普遍短、陈述式，无 we（摘要里 0 个 we）。

## 3. 引言逻辑（4 段 + A. Related Work 2 段 + B. Specific Contributions）
1. 技术背景：Massive MIMO → 集中式 vs 分布式部署的取舍（"at the cost of increased backhaul requirements"）。
2. 命名新系统："In this work, we consider a distributed Massive MIMO system … There are no cells or cell boundaries. Therefore, we call this system 'Cell-Free Massive MIMO'."
3. 关键设计取向：不共享瞬时 CSI、强调 per-user 而非 sum-throughput、用 max-min 功控。
4. 概念定位：承认它是 network MIMO / DAS / CoMP 的一种具体化，然后点出差异在"operating regime"，并类比"cellular Massive MIMO 之于 multiuser MIMO"。
5–6. 相关工作两段，各以一句空白收尾："By contrast, in the current paper, we assume TDD operation …"；"Yet, a comprehensive performance comparison … is not available in the existing literature."
- B 小节直接列 5 条贡献（consider / derive / compare / devise / compare），然后路线图、Notation。

## 4. Idea 是怎么提出的
- 空白类型：新架构（命名一个新的工作区间）+ 实用性（已有分布式大规模 MIMO 分析都假设完美 CSI）。
- 关键写法：不回避"这是已有概念的变体"，而是主动承认并说明"新在哪里"——"The outstanding aspect of Cell-Free Massive MIMO is its operating regime: …"。
- 比较对象选得好：选工业界熟悉的 small cells 做对手，结论直接可用。

## 5. 科研方法
- 系统模型：单天线 AP / 用户，TDD，三阶段（上行训练、下行数据、上行数据），用 bullet 列出全部假设（信道、互易、回传理想、符号独立）。
- 分析：先 M→∞ 的渐近分析（只剩导频污染），再有限 M 的闭式可达速率（Theorem 1/2），多个 Remark 解释和集中式 Massive MIMO 的差异。
- 资源管理：贪婪导频分配（Algorithm 1）；max-min 功控证明拟凹 / 拟线性（Proposition 1/2），用二分 + SOCP / LP 求全局最优。
- 单独一节给出 small-cell 系统的对应模型和功控，保证比较公平。

## 6. 仿真与实验
- 先讲大尺度衰落模型（三斜率路损 + 两分量相关阴影），参数表 Table I。
- "To ensure a fair comparison …, we choose … which makes the total radiated power equal in all cases."
- 主图是每用户吞吐的 CDF（强调 95%-likely 性能而非均值）；再扫用户数、AP 数、导频长度；Table II/III 汇总数字。

## 7. 图表
- 11 图 3 表 2 算法。Fig. 1 系统示意。结果图大多是 CDF。
- caption 描述型且带参数："… Here, M=100, K=40, and τ^cf=τ^sc …"；成对图用 "Same as Figure 3 but for the uplink"。

## 8. 句式库
- 命名："There are no cells or cell boundaries. Therefore, we call this system 'Cell-Free Massive MIMO'."
- 定位："In principle, Cell-Free Massive MIMO is an incarnation of general ideas known as …"
- 指出假设过强："However, in all those papers, perfect CSI was assumed at both the APs and the users, …"
- 文献空白："Yet, a comprehensive performance comparison between … that takes into account … is not available in the existing literature."
- 公平比较："To ensure a fair comparison between Cell-Free Massive MIMO and small-cell systems, we choose …"

## 9. 结论
- 2 段 113 词：过去时总结分析内容 → 主要结论（更鲁棒、95% 吞吐高一个数量级）→ 最后一句主动承认代价："In terms of implementation complexity, however, small-cell systems require much less backhaul than Cell-Free Massive MIMO." 无未来工作。
