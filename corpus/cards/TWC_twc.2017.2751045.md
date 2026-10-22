---
doi: 10.1109/twc.2017.2751045
title: "Mobile Unmanned Aerial Vehicles (UAVs) for Energy-Efficient Internet of Things Communications"
journal: TWC
year: 2017
band: 2016-2018
cites: 1004
cites_per_year: 112.5
article_type: research
topic: UAV
source: xplore-html
xplore: 8038869
auto:
  words_total: 10232
  n_sections: 6
  n_subsections: 13
  n_figures: 14
  n_tables: 1
  n_display_eq: 41
  n_algorithms: 1
  statements: {theorem: 2, lemma: 0, proposition: 2, corollary: 0, proof: 4, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 22.0
  we_per_1k: 12.8
  title_words: 11
  abstract_words: 270
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 1, roadmap: 1, however: 8, transition: 26, resultsShow: 2, motivatedBy: 0, toAddress: 1, gapWord: 1, nonconvex: 9, npHard: 0, closedForm: 1, outperform: 0, intensifier: 8, worthNoting: 0, observe: 11, thisIsBecause: 0, asExpected: 2, insight: 0, tradeoff: 4, figVerb: 13, promising: 0, gen: 0, contrast: 3, firstTime: 0, novel: 3, weProposeFirst: 4, wlog: 1, code: 0, prototype: 0}
  # 首创句为 "To our best knowledge, this paper is one of the first comprehensive studies …"，两个短语正则都未命中
  methods: {complexity: 5, convergence: 5, convexOpt: 3, lagrange: 3, KKT: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, aim, method, method, method, method, result, result, result, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, tech, prior, gap, contrib, contrib, roadmap]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 3
  contrib_verbs: [propose, derive, derive]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: none
  gap_type: [new-scenario, combination]
  motivating_figure: true
  problem_class: MINLP
  solution: [decomposition, reformulation, lagrangian-dual, closed-form]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [max-power, snapshot-layout, number-of-UAVs, number-of-channels, update-times, number-of-updates, iterations]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[平台] for Energy-Efficient [应用] Communications"，11 词。缩写在标题里写全称再加括号（"Unmanned Aerial Vehicles (UAVs)"），"Mobile" 一词点出与静态部署的区别。

## 2. 摘要（10 句，270 词）
- 被动锚点："In this paper, the efficient deployment and mobility of multiple unmanned aerial vehicles (UAVs), …, are investigated."
- "a novel framework is proposed for jointly optimizing …"（四个联合变量）→ First（给定激活设备求位置与关联）/ Next（移动模式）/ To this end（更新时刻）/ Moreover（最小能耗轨迹）。
- 结果带两个数字："… reduced by 45% compared with a case, in which stationary aerial base stations are deployed."、"a maximum of 28% enhanced system reliability"；再加一个权衡洞见（更新次数 vs 移动能耗 vs 发射功率），末句 "In essence, …" 用一句话解释该权衡。

## 3. 引言逻辑（6 段，约 1070 词）
1. UAV 作中继 / 空中基站（"On the one hand, … On the other hand, …"）及优势（即时部署、LoS、可移动降低发射功率）。
2. UAV 在 IoT 中的角色（电池受限设备无法远距离传输 → UAV 作移动汇聚点）→ "Nevertheless, to effectively use UAVs for the IoT, several technical challenges must be addressed such as …"
3. 已有工作逐篇 + 每处补一句局限（"However, these works considered a single UAV in their models."；"However, this work is limited to a static sensor network, …"）→ 概括："In fact, none of the prior studies in [1]–[14], addressed the problem of jointly optimizing …" → 谨慎的首创声明（"one of the first comprehensive studies"）。
4. "The main contribution of this paper is a novel framework for …"：第一步（分解为关联 + 功率 / 位置两个子问题迭代求解，并说明与全局最优的精度—开销权衡）。
5. 第二步（时变网络：更新时刻闭式 + 最小能耗轨迹）+ 结果预告。
6. 路线图。无记号段。

## 4. Idea 是怎么提出的
- 空白类型：新场景（多 UAV 为时变 IoT 上行收数据）+ 组合（部署、移动、关联、功控联合）。
- 写法亮点：把问题拆成"静态快照（给定激活设备的最优部署）"与"时间维（何时移动、怎么移动）"两步，贡献也按这两步写成两段。
- 首创声明加了限定词（"one of the first comprehensive studies"），比 "the first" 稳妥。

## 5. 科研方法
- 模型：空地概率 LoS 路损；两种 IoT 激活模型——周期型（举例：气象监测、智能电表）与概率型（Beta 分布，举例：健康监测、交通控制）；按位置分配信道。
- 快照问题 (OP)：分解为 (P1) 关联 + 功控（引用已知迭代算法 [21]，Proposition 1 给服务某设备所需的高度上下界）与 (P2) UAV 位置（逐个 UAV 优化；干扰情形近似处理，无干扰情形二次近似后凸化，Theorem 1 用对偶给出最优二维坐标）→ 两子问题迭代；Fig. 2 用框图总结求解步骤。
- 时间维：Proposition 2（周期激活下各更新时刻的精确活跃设备数）、Theorem 2（概率激活下的更新时刻，正则化不完全 Beta 函数的逆）；轨迹为最小移动能耗的指派问题（ILP），能耗模型引旋翼功率公式。
- 证明在正文。

## 6. 仿真与实验
- Table I 参数；1 km×1 km、500 个 IoT 设备、城区环境。
- 与"预部署静止空中基站"比较；最后与穷举最优解比较精度与时间（Fig. 14），并说明离散化分辨率。
- 结果多：可靠性、快照布局图（颜色表示关联）、发射功率 vs UAV 数（有 / 无干扰）、vs 信道数、活跃设备数随更新时刻、更新时刻曲线、UAV 能耗 vs 更新次数（揭示权衡："Interestingly, there is an inherent tradeoff between …"）、收敛。

## 7. 图表
- 14 图 1 表 1 算法。Fig. 1 系统模型，Fig. 2 求解框图，Fig. 3 近似误差图（验证二次近似）。caption 短标签（"Total transmit power of devices vs. number of UAVs in the interference-free scenario."）。"Fig. X shows …" 句式出现 13 次。

## 8. 句式库
- 正反两面角色："On the one hand, UAVs can be used as wireless relays …. On the other hand, UAVs can act as mobile aerial base stations …"
- 挑战清单："Nevertheless, to effectively use UAVs for the IoT, several technical challenges must be addressed such as optimal deployment, mobility and energy-efficient use of UAVs …"
- 逐篇局限："However, these works considered a single UAV in their models."
- 总体空白："In fact, none of the prior studies in [1]–[14], addressed the problem of jointly optimizing …"
- 谨慎首创："To our best knowledge, this paper is one of the first comprehensive studies on …"
- 权衡解释："In essence, a higher number of updates can lead to lower transmit powers for the IoT devices at the cost of an increased mobility for the UAVs."

## 9. 结论
- 1 段 179 词，现在完成时复述（have proposed / have determined / have investigated / have derived / have obtained）→ 定性结果 + 基本权衡。无数字、无未来工作。
