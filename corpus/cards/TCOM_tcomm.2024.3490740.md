---
doi: 10.1109/tcomm.2024.3490740
title: "Cell-Free ISAC MIMO Systems: Joint Sensing and Communication Beamforming"
journal: TCOM
year: 2025
band: 2022-2025
cites: 140
cites_per_year: 104.3
article_type: research
topic: ISAC-sensing
source: xplore-html
xplore: 10742291
auto:
  words_total: 9049
  n_sections: 8
  n_subsections: 20
  n_figures: 6
  n_tables: 0
  n_display_eq: 50
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 4, corollary: 0, remark: 2, proof: 1, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 24.5
  we_per_1k: 19.4
  title_words: 9
  abstract_words: 181
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 6, contribList: 1, roadmap: 0, however: 2, transition: 3, resultsShow: 0, motivatedBy: 1, toAddress: 1, gapWord: 0, nonconvex: 6, npHard: 0, closedForm: 0, outperform: 0, intensifier: 1, worthNoting: 6, observe: 0, thisIsBecause: 0, asExpected: 1, insight: 0, tradeoff: 3, figVerb: 0, promising: 1, gen: 1, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 1, code: 0, prototype: 0}
  # roadmap 0：原文以 "Organization: In Section II, …" 开头，正则未覆盖，实际有路线图
  methods: {SDR: 15, lagrange: 4, bisection: 1, complexity: 1, convexOpt: 1}
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [aim, theory, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 9
  intro_moves: [field, gap, aim, prior, prior, gap, prior, aim, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [present, develop, investigate, analyze, develop]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [SDR, lagrangian-dual, reformulation]
  theory_role: supporting
  proofs_location: mixed
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [power-ratio, target-distance, number-of-UEs, sensing-streams]
  fig1_role: system-model
  caption_style: self-contained-conclusion
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[系统]: Joint [A] and [B] Beamforming"，9 词。冒号前是系统名（Cell-Free ISAC MIMO），冒号后是设计对象。

## 2. 摘要（7 句，181 词）
- "This paper considers a cell-free integrated sensing and communication (ISAC) MIMO system, where …"——this paper 主语锚点句。
- 推导多基地感知 SNR → 两种"单方优先"基准方案（以 namely 列出）→ 联合设计（max-min 公平，推导最优结构）→ 固定波束下的功率分配。
- 结果两句均为"对比式"表述：联合设计"达到通信优先方案的 SINR、同时接近感知优先方案的 SNR"；并优于 RZF + 功率分配。无数字。

## 3. 引言逻辑（9 段，约 1300 词；内分 A. Prior Work / B. Contributions）
1. ISAC 价值 → "While these problems have recently attracted increasing research interest, the prior work has mainly focused on the single ISAC basestation case." → 多基站相互干扰 → 协作 → cell-free ISAC → "With this motivation, this paper investigates …"（第 1 段就交代全文动机与目标）。
2. （A 小节）cell-free massive MIMO 研究 → "Most of these studies, however, did not include the unification of the sensing and communication functions …"
3. 单节点 JSC / DFRC 研究。
4. 分布式 JSC：每个用户只由一个 AP 服务 → 不是完整的 cell-free 设定。
5. 最相关工作 [30]（固定波束只优化功率）及其扩展、作者自己的会议版 [1] 与其他波束工作 → "With this motivation, we propose and compare various beamforming and power allocation strategies, …"
6. （B 小节）模型与研究问题（多少条感知流）→ 5 条 bullet 贡献。
7. 贡献后再用一段散文总结主要结果（"We have extensively evaluated the proposed approaches and showed that …"）。
8. "Organization: …" 路线图；9. Notation。

## 4. Idea 是怎么提出的
- 空白类型：新场景（多 AP 协作的 cell-free ISAC）+ 已有方法局限（单 AP 服务每个用户、或固定波束只做功率分配）。
- 写法亮点：把"单方优先"的两种朴素做法先作为基准方案正式提出并各自成节（通信优先感知波束 / 感知优先通信波束），再引出联合设计——基准本身就是结构化的对照组。
- 提出一个可回答的研究问题并写进小节标题："How Many Sensing Streams Do We Need?"（结论：感知流数受 AP 数限制）。
- 会议版延续：引言明确 "in our prior work [1], we investigated joint beamforming design, …"。

## 5. 科研方法
- 模型：发射 AP 子集与接收 AP 子集（可重叠）；通信 SINR；多基地感知 SNR（附录推导）——"To define a general sensing objective that is correlated with the performance of various sensing tasks, …, we adopt the joint SNR …"。
- 基准：共轭 / 零空间投影感知波束；RZF 通信波束；感知优先下的最优通信波束（SOCP）。
- 联合设计：非凸 QCQP → SDP → SDR；Proposition 1（证明扩展 [23, Theorem 1]）给出秩一最优解构造；对偶问题分析感知流数（Proposition 2–4）。
- 功率分配：先列出相对波束优化的两点实际优势（大尺度更新、前传开销小）再建模，用 SDR + 秩一启发式重建。

## 6. 仿真与实验
- 节名就叫 "Results"；7 个方案用编号列表定义（含两个 SDR 上界）。
- 先简单 LoS 场景（两 AP，目标与 UE 沿一条线随机放置）研究机理，再 "As we have only investigated a simplified setup so far to examine the effects, we now provide a more realistic setup."（Rayleigh、方形区域）。
- 横轴：通信 / 感知功率分配比、目标到最近 AP 的距离、UE 数与感知流数。

## 7. 图表
- 6 图 0 表 0 算法（图很少）。caption 的特点是第二句直接写结论："The proposed JSC optimization provides almost a constant sensing SNR for different distances, with a significant gain over the NS solutions."——读者只看图注即可获得结论。

## 8. 句式库
- 已有研究局限于单节点："While these problems have recently attracted increasing research interest, the prior work has mainly focused on the single ISAC basestation case."
- 由现实推出新架构："In practice, however, multiple ISAC basestations will operate in the same geographical region, frequency band, and time, causing interference on each other …"
- 动机收束："With this motivation, this paper investigates the joint sensing and communication beamforming design of these cell-free ISAC MIMO systems."
- 指标选择理由："To define a general sensing objective that is correlated with the performance of various sensing tasks …, we adopt the joint SNR of the received signals as the sensing objective."
- 先简后繁："As we have only investigated a simplified setup so far to examine the effects, we now provide a more realistic setup."
- 结论型图注："The proposed JSC optimization provides a significant gain for sensing while satisfying the best communication SINR."

## 9. 结论
- 1 段 81 词（极短），过去时复述 + 重复摘要中的对比结论。无数字、无未来工作。
