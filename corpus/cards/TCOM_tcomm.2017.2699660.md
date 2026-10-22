---
doi: 10.1109/tcomm.2017.2699660
title: "Offloading in Mobile Edge Computing: Task Allocation and Computational Frequency Scaling"
journal: TCOM
year: 2017
band: 2016-2018
cites: 587
cites_per_year: 62.8
article_type: research
topic: MEC-offloading
source: xplore-html
xplore: 7914660
auto:
  words_total: 6841
  n_sections: 7
  n_subsections: 7
  n_figures: 6
  n_tables: 2
  n_display_eq: 37
  n_algorithms: 4
  statements: {theorem: 0, lemma: 0, proposition: 4, corollary: 0, remark: 2, proof: 4, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 22.8
  we_per_1k: 15.2
  title_words: 11
  abstract_words: 160
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 1, however: 10, transition: 4, resultsShow: 2, motivatedBy: 0, toAddress: 0, gapWord: 0, nonconvex: 1, npHard: 3, closedForm: 0, outperform: 1, intensifier: 2, worthNoting: 0, observe: 2, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 4, figVerb: 1, promising: 0, gen: 0, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 9, wlog: 0, code: 0, prototype: 0}
  methods: {SDR: 23, complexity: 8, BnB: 2, convexOpt: 2, gameTheory: 1}
code:
  title_pattern: [X-in-Y, colon-subtitle]
  abstract_moves: [aim, aim, method, method, result, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, prior, gap, gap, aim, contrib, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [investigate, propose, show]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: table
  gap_type: [limitation, new-scenario, practicality]
  motivating_figure: true
  problem_class: MINLP
  solution: [relaxation, SDR, exhaustive-search, closed-form]
  theory_role: supporting
  proofs_location: mixed
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [number-of-tasks, Gaussian-samples, energy-latency-tradeoff, weight-ratio]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[操作] in [领域]: [变量 A] and [变量 B]"，11 词。冒号前是大领域（MEC 卸载），冒号后直接列出两个联合优化变量（任务分配 + 计算频率调节）。

## 2. 摘要（7 句，160 词）
- "In this paper, we propose an optimization framework of offloading from a single mobile device (MD) to multiple edge devices."——锚点句同时给出场景新意（单设备→多边缘节点）。
- 第 2 句目标 + 变量："We aim to minimize both … by jointly optimizing …"；第 3 句分两种情形（固定 / 可变 CPU 频率）。
- 难度句用 NP-hard 一笔带过，然后两种情形各配两种算法（LR / SDR；ES / SDR）。
- 结尾三句结果：SDR 近优 → 多 AP + 可变频率带来增益 → "Finally, we show that the MD's flexible CPU range can have an impact on the task allocation."（洞见型结果）。无数字。

## 3. 引言逻辑（6 段 + 贡献列表，约 990 词）
1. 移动设备 → 移动云计算 → "However, cloud servers are usually logically and spatially far from MDs, which leads to huge communications latency." → 小基站就近计算。
2. 历史脉络（cloudlet 2009 → MEC 术语）→ 单用户 / 多用户资源分配逐篇一句 → "However, in all the above works, a MD can only associate with either a single edge device or a remote server."
3. 第二条线：DVFS；已有工作要么固定频率，要么任务模型过简（不可分 / 无限可分）→ "In practice, offloadable data contains some files or tasks which cannot be divided into smaller parts."
4. 第三条线："Last but not least, …"——已有工作只优化能耗或只优化时延。
5. "In this paper, we study …"：把三条空白一次性对应到本文设定 → "In summary, the main contributions of this paper are as follows:" + 3 条 bullet（系统模型 / 数学框架 / 数值结果，三条分别以 "In terms of …" 开头）。
6. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：已有工作局限（单 AP、单目标）+ 新场景（多 AP 卸载）+ 实用性（任务粒度不规则）。
- 写法亮点：三段各写一条"维度"的空白（关联节点数 / CPU 频率与任务粒度 / 目标函数），第 5 段一句话把三维组合起来——"三缺口合一"式定位。
- 贡献按"模型—方法—结果"三层组织，每条用 "In terms of the system model … / In terms of the mathematical framework …" 开头。

## 5. 科研方法
- 模型：N 个独立任务、M 个正交信道 AP + 本地 CPU；时延取各 CPU 的 makespan，能耗 = 计算 + 收发；加权和目标（λt, λe）。
- 固定频率：引入辅助变量 t 化 min-max → 线性松弛（LR）或二次型齐次化 + SDR + 高斯随机化（Algorithm 2）。
- 可变频率：Proposition 2 给出给定分配下的最优频率闭式（分段）→ 穷举搜索作最优基准；另做 SDR 低复杂度版本。
- Proposition 1 证 NP-hard；Section V 用 Proposition 3/4 分析 CPU 频率范围对卸载决策的影响（"全卸载 / 全本地"阈值）。
- 证明大部分在正文，Proposition 2 证明放附录。

## 6. 仿真与实验
- 参数取自真实设备（N810，400 MHz，0.8 W）与 Gzip 应用（330 cycles/byte），并给出处；Table II 默认参数。
- 先算法对比（三种数据率区间各一子图）→ 高斯样本数 L 对近似比的影响 → 多 AP 下能耗—时延权衡曲线 → 固定 vs 可变频率、权重比的影响。
- 基准：Local Processing、Random Assignment，以及最优解（穷举 / 分支定界）。

## 7. 图表
- 6 图 2 表（Table I 记号表、Table II 参数）4 算法。Fig. 1 多 AP 卸载框架图。几乎每张结果图都是 (a)(b)(c) 子图，caption 写清每个子图的条件（数据率区间）。

## 8. 句式库
- 指出远端代价："However, cloud servers are usually logically and spatially far from MDs, which leads to huge communications latency."
- 概括已有工作的共同局限："However, in all the above works, a MD can only associate with either a single edge device or a remote server."
- 实用性缺口："In practice, offloadable data contains some files or tasks which cannot be divided into smaller parts."
- 第三条缺口引出："Last but not least, computational offloading affects both the MD's energy consumption and its tasks' execution latency."
- 无标准解法："… for the general case when the MD's CPU frequency is elastic, there is no standard method as to find the optimal solution."

## 9. 结论
- 1 段 217 词：过去时复述（proposed / aimed / considered）→ SDR 多项式时间 + 近优 → 洞见 → 明确指出本文假设（AP 处理所有任务）在多设备时不成立 → "this scenario will be a good avenue for future research."（由自身假设引出未来工作）。
