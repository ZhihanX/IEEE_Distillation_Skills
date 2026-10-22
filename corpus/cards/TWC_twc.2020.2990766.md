---
doi: 10.1109/twc.2020.2990766
title: "Multicell MIMO Communications Relying on Intelligent Reflecting Surfaces"
journal: TWC
year: 2020
band: 2019-2021
cites: 999
cites_per_year: 161.8
article_type: research
topic: RIS
source: xplore-html
xplore: 9090356
auto:
  words_total: 8013
  n_sections: 6
  n_subsections: 25
  n_figures: 14
  n_tables: 1
  n_display_eq: 62
  n_algorithms: 4
  statements: {theorem: 1, lemma: 1, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.0
  we_per_1k: 9.8
  title_words: 8
  abstract_words: 238
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 1, however: 16, transition: 12, resultsShow: 1, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 4, npHard: 0, closedForm: 1, outperform: 1, intensifier: 3, worthNoting: 0, observe: 6, thisIsBecause: 2, asExpected: 4, insight: 3, tradeoff: 0, figVerb: 3, promising: 2, gen: 1, contrast: 0, firstTime: 0, novel: 0, weProposeFirst: 4, wlog: 0, code: 0, prototype: 0}
  # 首创句 "To the best of our knowledge, this is the first attempt …" 位于贡献列表 <li> 中，提取器不统计列表项，故 toTheBest 记为 0
  methods: {complexity: 28, convergence: 20, BCD: 16, bisection: 3, lagrange: 3, manifold: 3, convexOpt: 2, MM: 1}
code:
  title_pattern: [X-via-Y]
  abstract_moves: [context, aim, aim, context, method, method, method, theory, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, gap, tech, gap, prior, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: numbered
  contrib_n: 4
  contrib_verbs: [optimize, derive, extend, show]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [WMMSE, BCD, closed-form, MM, manifold, bisection]
  theory_role: supporting
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [iterations, number-of-elements, path-loss-exponent, IRS-location, user-location, reflection-amplitude, weights, deployment-scheme]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[场景] MIMO Communications Relying on [技术]"，8 词。"Relying on" 相当于 via / aided，突出场景（多小区）在前、使能技术在后。

## 2. 摘要（10 句，238 词）
- 第 1 句技术定位（"constitute a disruptive wireless communication technique …"）。
- "In this paper, we propose to invoke an IRS at the cell boundary of multiple cells to assist the downlink transmission to cell-edge users, whilst mitigating the inter-cell interference, …"——部署位置写进锚点句。
- 目标（WSR）→ 多天线收发 → BCD（闭式预编码 + MM / CCM 两种相位算法）→ "Both algorithms are guaranteed to converge to at least locally optimal solutions." → 扩展到多 IRS 与网络 MIMO → 仿真确认。无数字。

## 3. 引言逻辑（6 段，约 1200 词）
1. 千倍容量需求 → massive MIMO / mmWave / UD-CRAN → 各自代价（RF 链复杂度与功耗、前传瓶颈、遮挡）。
2. "As a remedy, …" IRS 原理（相长 / 相消叠加）→ 与雷达中固定反射面、AF 中继的区别 → 部署便利 → "However, to reap the aforementioned benefits …, the phase shifts have to be appropriately optimized along with the active beamforming weights at the BS." → 单模约束在混合预编码 / 恒包络预编码中的经验不能直接用。
3. 已有 IRS 发射设计按场景罗列 → "However, the above-mentioned papers only studied the single-cell scenario, whilst there is a paucity of investigations on the multicell scenario …" → 小区间干扰 → "Hence, in this paper, we propose to employ an IRS at the cell boundary …"（Fig. 1 在引言）→ 机理：反射干扰与直达干扰相消 → 变量耦合 → 已有工作只考虑单天线用户 → 多天线用户使速率表达式更复杂、已有技术不能直接用。
4. 4 条编号贡献（第 1 条以首创声明开头）。
5. 路线图；6. Notations。

## 4. Idea 是怎么提出的
- 空白类型：新场景（多小区、小区边缘用户）+ 已有方法局限（单小区、单天线用户）。
- 写法亮点：位置即创新——把 IRS 放在小区边界，并用一句机理说明它为什么能同时增强信号和抑制小区间干扰（"the inter-cell interference reflected by the IRS can be superimposed destructively on the direct interference …"）。
- 两个"复杂化维度"（多小区 + 多天线用户）分别引出、分别说明为何让问题更难。

## 5. 科研方法
- 问题：WSR 最大化，变量为各 BS 预编码矩阵与 IRS 相位，约束为功率与单模。
- 速率-MSE 关系（WMMSE 式）重写 → BCD：预编码用拉格朗日乘子法得闭式（按 A_l 满秩 / 低秩两种情形，二分求乘子）；相位化为单模约束 QCQP → MM（构造代理函数，Lemma 1）或复圆流形 CCM（Fig. 2 几何解释；Theorem 1 引自 [35] 给步长条件保证收敛）→ Table I 复杂度对比。
- "Extension to Other Scenarios" 节：网络 MIMO（多 BS 协作传同一数据）与多 IRS（堆叠后与单 IRS 形式相同）。
- 无附录、无自证定理（定理引自文献）。

## 6. 仿真与实验
- 参数写在正文（路损模型与指数、BS/IRS/用户高度，并解释 IRS 链路取近自由空间指数的理由）。
- 两小区场景（"In order to obtain more insights about the benefits of deploying IRS, we first consider …"）：BCD 收敛、MM/CCM 收敛 → 基准 RandPhase、No-IRS（另比较 Net-MIMO）→ 相位数、IRS 链路路损指数（承认理想位置未必可得）、IRS 位置、用户位置、反射幅度、权重（公平性）。
- 四小区场景：单 IRS 三种移动轨迹、两 IRS（总元件数相同）→ 得出"分布式部署优于集中式"的部署建议。

## 7. 图表
- 14 图 1 表 4 算法。Fig. 1 多小区系统图（引言），Fig. 2 CCM 几何解释，Fig. 3/12 仿真布局。caption 短标签（"Achievable WSR versus the location of the IRS x_IRS."）。

## 8. 句式库
- 已有技术代价："However, escalating signal processing complexity, increased hardware costs as well as high power consumption are incurred by …"
- 引出新技术："As a remedy, intelligent reflecting surface (IRS) has been proposed as a revolutional technique of …"
- 单场景局限："However, the above-mentioned papers only studied the single-cell scenario, whilst there is a paucity of investigations on the multicell scenario in the existing literature."
- 机理说明："… the inter-cell interference reflected by the IRS can be superimposed destructively on the direct interference impinging from the adjacent BS …"
- 已有技术不能直接用："Given the complex mathematical data rate expression, the techniques conceived in [15]–[23], … cannot be directly applied."
- 部署建议："Furthermore, the location of IRS should be carefully chosen to guarantee a favourable BS-IRS link and IRS-user link."

## 9. 结论
- 1 段 195 词，现在完成时开头（"we have enhanced …"）后转过去时复述 → 机理 → 增益 → 两条部署建议（位置要仔细选；靠近用户簇时分布式部署更优）。无数字、无未来工作。
