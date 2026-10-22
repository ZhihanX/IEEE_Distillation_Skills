---
doi: 10.1109/twc.2019.2922609
title: "Reconfigurable Intelligent Surfaces for Energy Efficiency in Wireless Communication"
journal: TWC
year: 2019
band: 2019-2021
cites: 3625
cites_per_year: 505.2
article_type: research
topic: RIS
source: xplore-html
xplore: 8741198
auto:
  words_total: 6919
  n_sections: 5
  n_subsections: 14
  n_figures: 10
  n_tables: 2
  n_display_eq: 38
  n_algorithms: 3
  statements: {theorem: 0, lemma: 2, proposition: 0, corollary: 0, proof: 2, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 27.3
  we_per_1k: 7.4
  title_words: 9
  abstract_words: 173
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 1, however: 6, transition: 12, resultsShow: 2, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 3, npHard: 0, closedForm: 2, outperform: 3, intensifier: 2, worthNoting: 0, observe: 6, thisIsBecause: 0, asExpected: 1, insight: 0, tradeoff: 3, figVerb: 1, promising: 0, gen: 2, contrast: 0, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 1, code: 0, prototype: 1}
  methods: {FP: 8, AO: 2, MM: 1, convergence: 6, complexity: 8}
code:
  title_pattern: [X-for-Y, X-in-Y]
  abstract_moves: [aim, aim, method, method, method, method, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper
  intro_paragraphs: 7
  intro_moves: [field, tech, gap, prior, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [develop, develop, evaluate]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [comparison, new-architecture]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [AO, gradient, FP, MM]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [transmit-power, number-of-elements]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: true
  conclusion_future_work: true
---

## 1. 标题
- "[器件] for [指标] in Wireless Communication"，9 词。目标指标（能效）直接做标题主语义，非常宽泛——早期开创性论文可以用宽标题占位。

## 2. 摘要（7 句，173 词）
- 第一句被动语态把锚点放句尾："The adoption of a reconfigurable intelligent surface (RIS) for downlink multi-user communication from a multi-antenna base station is investigated in this paper."
- "This leads to non-convex design optimization problems for which to tackle we propose two computationally affordable approaches, capitalizing on …"——问题性质和方法放一句。
- 两个算法用 "Specifically, one algorithm … Instead, the second algorithm …" 并列。
- 末句带数字："up to 300% higher energy efficiency in comparison with the use of regular multi-antenna amplify-and-forward relaying."

## 3. 引言逻辑（7 段）
1. 能效成为 5G 关键指标（50 亿设备预测、综述结论）。
2. RIS 作为绿色通信硬件：工作原理、实现方式（连续 / 离散）。
3. 优势与疑问：无放大器 → 省能；但也因此增益低于 AF 中继 → "Thus, as far as EE is concerned, it is not clear if a RIS-based system is more convenient than traditional AF relay-based systems. This work aims at answering this question, …"
4. 已有工作：主要是室内的速率与实验（逐篇描述实验参数）。
5. "In this work, we consider the downlink of an outdoor cellular network …" → 3 条贡献（功耗模型 / 两个可证收敛的算法 / 室外场景评估，"while all previous works about RIS have focused on indoor settings"）。
6. 路线图；7. Notation。

## 4. Idea 是怎么提出的
- 空白类型：比较型（RIS 与 AF 中继在能效上孰优未知）+ 新架构。
- 写法亮点：把"优势"和"劣势"放在同一段里对冲（无放大器省电 vs 无放大器增益低），从而自然引出一个必须回答的问题，再说本文就是回答它。
- 首创说法在结论："This paper has provided a first contribution in the area of radio resource allocation in cellular communication systems incorporating RIS structures."

## 5. 科研方法
- 先建 RIS 功耗模型（与单元数和相位分辨率相关），作为能效分母——"建一个更真实的模型"本身是贡献。
- ZF 预编码下的能效最大化，非凸；交替优化：相位用共轭梯度（Polak-Ribiere-Polyak）或序列分式规划（SFP，构造代理上界，Lemma 1/2），功率用分式规划。
- 单列复杂度小节。

## 6. 仿真与实验
- 3GPP 室外传播参数和硬件功耗参数列在 Table I；QoS 约束设为"正交信道 + 均匀功率"下速率的某个比例，并报告可行率（Table II）——交代约束取值的依据。
- 基准选 AF 中继（并为它也推导了能效最优算法，保证比较公平）；"It is reasonable to expect that … provides substantial EE gains compared to the case where such a surface is absent; this intuition has been verified via simulations in [1]"——跳过平凡基准。
- 结果先承认 SE 上中继更好（Fig. 3），再展示 EE 上 RIS 胜出（Fig. 4）："The trend in Fig. 3 is reversed in Fig. 4"。

## 7. 图表
- 10 图 2 表 3 算法。caption 描述型，带参数组合和子图说明。

## 8. 句式库
- 抛出待答问题："Thus, as far as EE is concerned, it is not clear if a RIS-based system is more convenient than traditional AF relay-based systems. This work aims at answering this question, …"
- 问题性质 + 方法："This leads to non-convex design optimization problems for which to tackle we propose two computationally affordable approaches, capitalizing on …"
- 场景差异化："… while all previous works about RIS have focused on indoor settings."
- 结果反转："The trend in Fig. 3 is reversed in Fig. 4, where the EE performance is sketched."
- 诚实声明："However, no global optimality claim can be made due to the following facts: …"

## 9. 结论
- 2 段（"Conclusion and Future Work"）：第 1 段过去时总结并重复 300%；第 2 段先自评首创，再列 6–7 个未来方向（连续表面、渐近分析、直连链路、信道获取、EE-SE 折中、面积划分），比多数论文详细。
