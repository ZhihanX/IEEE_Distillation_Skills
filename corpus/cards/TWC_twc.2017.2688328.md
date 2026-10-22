---
doi: 10.1109/twc.2017.2688328
title: "Energy-Efficient UAV Communication With Trajectory Optimization"
journal: TWC
year: 2017
band: 2016-2018
cites: 2104
cites_per_year: 225.2
article_type: research
topic: UAV
source: xplore-html
xplore: 7888557
auto:
  words_total: 7485
  n_sections: 7
  n_subsections: 8
  n_figures: 9
  n_tables: 2
  n_display_eq: 55
  n_algorithms: 1
  statements: {theorem: 2, lemma: 2, proposition: 0, corollary: 0, proof: 4, proof_in_appendix: 1}
  n_appendix: 2
  mean_sentence_words: 26.8
  we_per_1k: 6.9
  title_words: 6
  abstract_words: 230
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 1, however: 4, transition: 21, resultsShow: 2, motivatedBy: 0, toAddress: 3, gapWord: 0, nonconvex: 5, npHard: 0, closedForm: 4, outperform: 0, intensifier: 4, worthNoting: 0, observe: 2, thisIsBecause: 0, asExpected: 3, insight: 1, tradeoff: 3, figVerb: 5, promising: 2, gen: 1, contrast: 3, firstTime: 1, novel: 0, weProposeFirst: 1, wlog: 1, code: 0, prototype: 0}
  methods: {convergence: 3, FP: 1, KKT: 1, bisection: 1, complexity: 1, convexOpt: 1}
code:
  title_pattern: [X-with-Y]
  abstract_moves: [context, aim, method, method, theory, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 7
  intro_moves: [tech, tech, gap, aim, prior, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [derive, study, introduce, study]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [practicality, new-scenario]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [SCA, FP, closed-form]
  theory_role: supporting
  proofs_location: mixed
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [iterations, trajectory-plot, time]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "Energy-Efficient [系统] With [设计手段]"，6 词。目标（能效）做形容词前置，手段（轨迹优化）放 With 短语。

## 2. 摘要（8 句，230 词）
- "In this paper, assuming that the UAV flies horizontally with a fixed altitude, we study … , a new design paradigm that jointly considers both …"——把关键假设放进锚点句，并用同位语给工作定性（"a new design paradigm"）。
- "To this end, we first derive a theoretical model …"：先建模型（贡献之一），再定义能效。
- 反直觉结论单独成句："we show that both the rate-maximization and energy-minimization designs lead to vanishing energy efficiency and thus are energy-inefficient in general."
- 再依次给出圆轨迹设计和一般约束设计，最后定性结果。

## 3. 引言逻辑（7 段）
1. UAV 通信的优势（成本、灵活、LoS）。
2. 三类应用（覆盖、中继、信息分发 / 数据收集），各配场景。
3. 挑战："Despite their ample applications, UAV communication systems face many new challenges." → 能量受限 → "energy-efficient designs for UAV communication systems are significantly different from those … on terrestrial communication systems"，用 Firstly / Secondly 说明两点不同（动机更关键、推进能耗远大于通信能耗）。
4. "In this paper, we study …" → 直觉分析（"Intuitively, from the throughput maximization perspective, the UAV should stay stationary … However, hovering with strictly zero speed is known to be inefficient … or even impossible …"）→ 需要折中 → 4 条贡献。
5. 相关工作放在贡献之后：逐篇一句 → "However, none of the above works on trajectory optimization considers the energy efficiency of the system." → 首创声明。
6. 路线图；7. Notations。

## 4. Idea 是怎么提出的
- 空白类型：实用性（已有 UAV 能效工作忽略推进能耗）+ 新场景。
- 核心洞见：UAV 的"能效"由飞行状态（速度、加速度）决定，与地面系统根本不同；先用直觉说明两个极端（悬停 / 节能直飞）都不行，引出折中。
- 两处首创声明：一处在贡献里（"the derived model is the first theoretical model that relates …"），一处在相关工作段末（"our paper is the first work that studies …"）。
- 跨学科建模：附录 A 用空气动力学推导推进功耗（受力图 Fig. 8/9），并做 "sanity check"（与已知功率—速度曲线对照）。

## 5. 科研方法
- 模型：固定高度、LoS 信道；推进能耗模型只依赖速度和加速度。
- 第 III 节无约束分析：Theorem 1 给出能耗最小解（以节能速度直飞），说明两种极端设计能效都趋于 0。
- 第 IV 节圆轨迹：能效化为半径和速度的闭式函数，求最优。
- 第 V 节一般约束：离散线性状态空间近似 + 能耗上界 + 速率一阶泰勒下界 → 序列凸优化（Algorithm 1），Lemma 1 证明单调收敛到 KKT 点，多项式复杂度。

## 6. 仿真与实验
- 参数正文给出，并说明推导出的数值意义（"the maximum SNR achieved when the UAV is just above the GT can be obtained as 30dB"；"P ≪ Pem, thus the UAV transmission power can be practically ignored"）。
- 结果以轨迹图、速度曲线和两张性能对比表（速率 / 功耗 / 能效三列）呈现；baseline 为速率最大、能耗最小、直线飞行。

## 7. 图表
- 9 图 2 表。Fig. 1 系统图、Fig. 2 引用的功率—速度典型曲线、Fig. 3 圆周飞行示意；附录有两张受力图。
- 用表格汇总不同设计的速率 / 功耗 / 能效，比图更直接。

## 8. 句式库
- 挑战过渡："Despite their ample applications, UAV communication systems face many new challenges [1]."
- 本质差异："Note that energy-efficient designs for UAV communication systems are significantly different from those in the existing literature on terrestrial communication systems."
- 直觉 + 反转："Intuitively, from the throughput maximization perspective, the UAV should stay stationary … However, hovering with strictly zero speed is known to be inefficient … or even impossible …"
- 折中："Thus, the energy-efficient trajectory design needs to strike an optimal balance between …"
- 首创："To the authors' best knowledge, our paper is the first work that studies …, which provides a new framework for …"

## 9. 结论
- 1 段 137 词，一般现在时逐条复述（"This paper studies … A theoretical model … is derived … it is shown that …"），无数字、无未来工作。
