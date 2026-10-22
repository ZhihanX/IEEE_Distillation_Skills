---
doi: 10.1109/twc.2016.2633522
title: "Energy-Efficient Resource Allocation for Mobile-Edge Computation Offloading"
journal: TWC
year: 2017
band: 2016-2018
cites: 1435
cites_per_year: 149.6
article_type: research
topic: MEC-offloading
source: xplore-html
xplore: 7762913
auto:
  words_total: 7874
  n_sections: 8
  n_subsections: 29
  n_figures: 3
  n_tables: 4
  n_display_eq: 42
  n_algorithms: 5
  statements: {theorem: 3, lemma: 10, proposition: 3, corollary: 1, remark: 7, proof: 1, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 21.5
  we_per_1k: 2.4
  title_words: 7
  abstract_words: 237
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 0, roadmap: 1, however: 6, transition: 14, resultsShow: 0, motivatedBy: 1, toAddress: 6, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 0, intensifier: 1, worthNoting: 1, observe: 4, thisIsBecause: 0, asExpected: 0, insight: 4, tradeoff: 0, figVerb: 2, promising: 2, gen: 0, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 0, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 25, lagrange: 9, KKT: 4, bisection: 3, convexOpt: 2, gameTheory: 2}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, context, aim, method, theory, theory, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 7
  intro_moves: [field, aim, prior, gap, prior, aim, contrib, roadmap]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [derive, extend, propose]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: none
  gap_type: [limitation, theory-gap]
  motivating_figure: true
  problem_class: convex      # TDMA 情形为凸问题（主结果）；OFDMA 情形为混合整数问题
  solution: [KKT, lagrangian-dual, closed-form, bisection, decomposition]
  theory_role: central
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [time-slot, cloud-capacity, number-of-users, number-of-subchannels, running-time]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "Energy-Efficient Resource Allocation for [系统]"，7 词。最朴素的"目标形容词 + 问题 + for + 系统"，无副标题。

## 2. 摘要（10 句，237 词）
- 前两句定义 MECO 并说明价值（"Thereby, MECO is envisioned as a promising technique for …"）。
- "In this paper, we study resource allocation for a multiuser MECO system based on TDMA and OFDMA."
- 核心结论写进摘要："The optimal policy is proved to have a threshold-based structure with respect to a derived offloading priority function, …" + 解释："As a result, users with priorities above and below a given threshold perform complete and minimum offloading, respectively."
- 有限云容量（次优算法）→ OFDMA（混合整数 → 转化为 TDMA 对应问题）→ 近优。First / Moreover / Next 串联。无数字。

## 3. 引言逻辑（7 段，约 840 词；引言内分 A. Prior Work / B. Contribution and Organization）
1. IoT 数十亿设备 → 电池与算力有限 → MECO → 第 1 段末就写 "In this paper, we consider …"（提前亮出本文）。
2. （A 小节）计算机领域的移动卸载以中心云为前提 → 回程时延与容量瓶颈 → MECO。
3. 单用户 / 多用户 MECO 工作逐篇一句 → 关键空白："Prior work on MECO resource allocation focuses on complex algorithmic designs and yields little insight into the optimal policy structures." → "In contrast, … the optimal resource-allocation policy is shown in the current work to have a simple threshold-based structure …"
4. 传统多址资源分配只管无线资源 → MECO 需联合计算与无线资源（"making the algorithmic design more complex"）。
5. （B 小节）本文设定与假设（数据可分、BS 已知信息、集中式）。
6. "The contributions of current work are as follows." + 3 条 bullet（按三种系统情形组织：TDMA 无限容量 / TDMA 有限容量 / OFDMA）。
7. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限 + 理论空白——不是"没人做过"，而是"做过但只给复杂算法、没有策略结构洞见"。这是"结构型结果"论文的典型定位。
- 写法亮点：把"可解释的最优结构"（阈值策略 + 卸载优先级函数）当作主贡献，算法是其副产品；OFDMA 部分明确"借用 TDMA 的结构洞见"设计低复杂度算法。
- 贡献按问题情形而不是按"建模 / 算法 / 仿真"组织。

## 5. 科研方法
- 模型：TDMA / OFDMA 多址、本地计算能耗、卸载能耗、两种有限云容量模型；加权和移动能耗最小化 + 时延约束。
- Lemma 1 证明凸性 → 部分拉格朗日 + KKT → 定义卸载优先级函数（Lemma 2：某方程的根，用 Lambert W 表示）→ Theorem 1：阈值结构；Proposition 1/2（"Exclusive / Inclusive Mobile Computation Offloading"）刻画时隙长度的影响；特例小节（信道相同 / 本地计算相同）给直观结论。
- 有限容量：Theorem 2 同结构，两维搜索 → 次优一维搜索；扩展到计算时间不可忽略（Theorem 3）。
- OFDMA：四阶段次优算法（子信道预留 → 平均增益转化为 TDMA → 整数分配 → 调整），Remark 7 给复杂度对比（O(K+N+KN log(1/ε)) vs 松弛取整的 O((KN)^3.5 …)）。
- 7 个 Remark 带括号小标题，其中两个是问句："Remark 2 (Offloading or Not?)"、"Remark 5 (Which Resource is Bottleneck?)"。证明集中在附录。

## 6. 仿真与实验
- 200 次信道实现；参数写在正文。
- TDMA：与等分资源基准比较，一张三子图的 Fig. 3（时隙、云容量、用户数）。
- OFDMA：结果用表格呈现（Table I–IV：能耗 vs 子信道数 / 用户数；平均运行时间，注明 Matlab 与 CPU 型号）。

## 7. 图表
- 只有 3 图、4 表、5 个算法。Fig. 1 TDMA / OFDMA 系统示意，Fig. 2 卸载模型。结果大量用表格——与多数论文"多图少表"相反。

## 8. 句式库
- 价值铺垫："Thereby, MECO is envisioned as a promising technique for prolonging the battery lives and enhancing the computation capacities of mobiles."
- 洞见型空白："Prior work on MECO resource allocation focuses on complex algorithmic designs and yields little insight into the optimal policy structures."
- 对比本文："In contrast, …, the optimal resource-allocation policy is shown in the current work to have a simple threshold-based structure with respect to a derived offloading priority function."
- 结论解读："Theorem 1 reveals that the optimal resource-allocation policy has a threshold-based structure when offloading saves energy."
- 洞见迁移："For an infinite-capacity cloud based on OFDMA, the insight of priority-based policy structure of TDMA is used for optimizing its resource allocation."

## 9. 结论
- 1 段 125 词（很短），一般现在时（"This work studies … it shows that … we derive … we extend …"）。无数字、无未来工作。全文 we 的密度极低（2.4 / 千词），大量被动语态。
