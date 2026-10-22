---
doi: 10.1109/twc.2017.2789293
title: "Joint Trajectory and Communication Design for Multi-UAV Enabled Wireless Networks"
journal: TWC
year: 2018
band: 2016-2018
cites: 1872
cites_per_year: 217.9
article_type: research
topic: UAV
source: xplore-html
xplore: 8247211
auto:
  words_total: 7898
  n_sections: 5
  n_subsections: 10
  n_figures: 11
  n_tables: 0
  n_display_eq: 37
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 29.1
  we_per_1k: 6.6
  title_words: 10
  abstract_words: 225
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 0, roadmap: 1, however: 7, transition: 15, resultsShow: 2, motivatedBy: 1, toAddress: 5, gapWord: 0, nonconvex: 14, npHard: 1, closedForm: 0, outperform: 1, intensifier: 6, worthNoting: 4, observe: 7, thisIsBecause: 2, asExpected: 1, insight: 0, tradeoff: 10, figVerb: 0, promising: 1, gen: 1, contrast: 6, firstTime: 0, novel: 1, weProposeFirst: 7, wlog: 2, code: 0, prototype: 0}
  methods: {convergence: 15, complexity: 11, convexOpt: 10, BCD: 9, AO: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, aim, method, method, method, method, method, theory, method, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 8
  intro_moves: [field, prior, gap, aim, approach, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 5
  contrib_verbs: [relax, apply, show, propose, show]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, limitation]
  motivating_figure: true
  problem_class: MINLP
  solution: [relaxation, BCD, SCA, heuristic]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [trajectory-plot, time, period, iterations]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "Joint [A] and [B] Design for [系统]"，10 词。"Joint X and Y Design/Optimization" 是 UAV、RIS 优化论文最常见的标题骨架之一。

## 2. 摘要（10 句，225 词）
- "This paper considers a multi-UAV enabled wireless communication system, where …"（this-paper-verb 锚点）。
- 目标句把"为什么选 max-min"写进去："To achieve fair performance among users, we maximize the minimum throughput …"
- "The formulated problem is a mixed integer nonconvex optimization problem that is challenging to solve. As such, we propose …"——问题难度与方法之间用 "As such" 连接。
- 单独一句收敛保证 + 一句初始化方案（"based on the simple circular trajectory and the circle packing scheme"）。

## 3. 引言逻辑（8 段，约 1530 词）
1. 领域：UAV 市场数字（"2 billion dollars in 2016 … 127 billion dollars by 2020"）、Facebook / Google 项目、3GPP、FAA 批准——用工业界信号建立重要性 → 学术研究分两条线（static-UAV / mobile-UAV）。
2. static-UAV：部署 / 放置优化，逐篇一句。
3. mobile-UAV：移动性的价值（与小基站类比："This is analogous and yet in sharp contrast to the existing small-cell technology …"）→ 已有轨迹工作只考虑单 UAV 单用户 → [24] 的局限（"which simplifies the analysis but limits the applicability in practice"）。
4. "In this paper, we study a general multi-UAV enabled wireless communication system …" → 为何要多 UAV（SWAP 限制、并行服务缓解吞吐—时延折中）。
5. 目标与首创句 → "On one hand, … On the other hand, …" 说明联合设计的好处 → "However, such a joint trajectory and adaptive communication design problem is non-trivial to solve. This is because …"
6. 方法与结论（散文式）："To tackle the above challenges, we first relax …"
7. 路线图；8. Notations。

## 4. Idea 是怎么提出的
- 空白类型：新场景（多 UAV、多用户、二维分布）+ 已有工作局限（单 UAV、一维、恒速）。
- 写法亮点：先把领域按"是否利用移动性"二分，自己落在 mobile-UAV 一边，再从"单 → 多"推出本文；用工业界动态（市场规模、3GPP、FAA）代替空泛的 "has attracted much attention"。
- 首创句嵌在目标段里："Such a joint optimization problem is practically appealing, but has not been investigated in the literature to the authors' best knowledge."

## 5. 科研方法
- 周期性 TDMA、LoS 信道、多 UAV 同频（有干扰）；变量：用户调度与关联（二元）、轨迹、功率。
- 先松弛二元变量（目标值成为上界）→ BCD 三块交替：调度关联（LP）、轨迹（SCA 下界）、功率（SCA 上界）→ 证明收敛。
- 单列"轨迹初始化"小节（圆轨迹 + 圆填充），以及"从松弛解重构二元解"小节——处理实际可用性的细节。
- 无定理环境，收敛和复杂度以正文论证给出。

## 6. 仿真与实验
- 参数在正文；只用一次随机用户位置实现（明确说明 "based on one random realization of the user locations"）。
- 先单 UAV（轨迹随周期 T 变化、速度曲线、max-min 速率、接入时延），再多 UAV（收敛、Scheme I/II/III 对比各设计维度的贡献、轨迹对比、功率曲线）。
- 用 "Scheme I / II / III" 做消融式对比（全联合 / 不优化功率 / …），量化每个设计维度的增益。

## 7. 图表
- 11 图 0 表。轨迹图是核心可视化（采样点、方向箭头、用户位置标记），caption 详细说明标记含义。

## 8. 句式库
- 产业信号："As reported in [3], the global market for commercial UAV applications, estimated at about 2 billion dollars in 2016, will skyrocket to …"
- 类比 + 对照："This is analogous and yet in sharp contrast to the existing small-cell technology, where …"
- 局限："… which simplifies the analysis but limits the applicability in practice."
- 难点："However, such a joint trajectory and adaptive communication design problem is non-trivial to solve. This is because … are closely coupled with each other …"
- 引出方法："To tackle the above challenges, we first relax the binary variables …"

## 9. 结论
- 2 段：第 1 段现在完成时总结；第 2 段先讨论上行如何推广及其难点，再用编号 1)–3) 列出未来方向（空地共存、3D 轨迹、能效轨迹）。
