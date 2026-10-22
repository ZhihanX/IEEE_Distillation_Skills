---
doi: 10.1109/jsac.2023.3240713
title: "Energy Efficient Semantic Communication Over Wireless Networks With Rate Splitting"
journal: JSAC
year: 2023
band: 2022-2025
cites: 181
cites_per_year: 52.8
article_type: research
topic: semantic
source: xplore-html
xplore: 10032275
auto:
  words_total: 4623
  n_sections: 5
  n_subsections: 7
  n_figures: 9
  n_tables: 1
  n_display_eq: 50
  n_algorithms: 1
  statements: {theorem: 1, lemma: 0, proposition: 0, corollary: 0, proof: 1, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.9
  we_per_1k: 5.2
  title_words: 10
  abstract_words: 187
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 2, contribList: 1, roadmap: 0, however: 2, transition: 3, resultsShow: 2, motivatedBy: 0, toAddress: 12, gapWord: 0, nonconvex: 10, npHard: 0, closedForm: 1, outperform: 1, intensifier: 0, worthNoting: 0, observe: 3, thisIsBecause: 1, asExpected: 0, insight: 1, tradeoff: 1, figVerb: 4, promising: 0, gen: 1, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 9, DNN: 3, SCA: 3, DRL: 1, KKT: 1, bisection: 1}
  domain: {accuracy: 9, capacityBound: 2, complexityCost: 2, knowledgeBase: 1, MIMO: 1}
code:
  title_pattern: [X-with-Y]
  abstract_moves: [aim, model, model, model, model, problem, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, tech, prior, prior, field-gap, contrib]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [investigate, adopt, propose]
  contrib_quantified: false
  first_claim: true                     # "there is no prior works that consider the integration of semantic communication and RSMA"
  roadmap: false
  notation: none
  gap_type: [combination]
  motivating_figure: true
  problem_class: nonconvex-continuous   # 能耗最小化：提取率、计算频率、功率、速率分配、波束成形
  solution: [AO, closed-form, SCA, lagrange]
  theory_role: supporting               # Theorem 1 提取率闭式解
  proofs_location: inline
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: true                 # Table I
  baselines_n: 3                        # FDMA、NOMA、穷举初始化（EXH-RSMA）
  baseline_naming: acronym
  x_axes: [transmit-power, bandwidth, data-size, computation-capacity]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: networking
  source: [text]                        # 概率图提取多级语义（沿用 [54] 的参数）
  task: [reconstruction]
  paradigm: system-level
  architecture: [probability-graph]
  channel: [MISO]                       # 多天线 BS、单天线用户、路损 + 阴影
  adaptivity: [resource-allocation]
  training: [none]
  metrics: [energy, custom]             # 总通信 + 计算能耗；语义精度约束
  datasets: []
  baselines: [optimization]
  snr_mismatch_test: false
  complexity_reported: true
  digital_compatible: true
  hardware_validation: false
  theory: none
  idea_delta: [system-optimization, multi-user]
  builds_on: [RSMA, probability-graph semantic extraction, SCA beamforming]
  open_problems_n: 0
---

## 1. 标题
- "Energy Efficient Semantic Communication Over Wireless Networks With [多址技术]"，10 词。"性能目标 + 语义通信 + 使能技术"三段式。

## 2. 摘要（8 句，187 词）
- 问题陈述 → 模型三句（BS 用概率图提取多级语义；RSMA：私有语义走私有消息、共同知识走公共消息）→ 同时考虑计算与传输能耗 → 优化问题（时延、计算、功率约束）→ 交替算法 + 每步闭式解 → 结果仅一句"verify the effectiveness"。

## 3. 引言逻辑（6 段）
- 新应用的需求 → "However, due to limited wireless resources such as frequency and time, conventional orthogonal multiple access schemes cannot support massive connectivity concern for next-generation wireless communication networks [5]." → NOMA → RSMA 原理与挑战 → RSMA 文献两段（MIMO、RIS、UAV、学习方法）→ 语义通信 + 关键联系："Due to the inherent similarity of common knowledge and common message, RSMA can be utilized to enhance the system performance of downlink semantic communication." → 首创声明 → 3 条贡献。无路线图。

## 4. Idea 是怎么提出的
- 空白类型：组合（语义通信 × RSMA，此前无人结合）。
- 核心洞见：语义通信需要收发双方共享"共同知识"，RSMA 的"公共消息"恰好被所有用户解码——两者结构同构，于是用公共消息广播知识库更新、私有消息传各用户的小尺寸语义信息。
- "结构相似性 → 技术组合"是网络优化类语义论文常见的 idea 生成方式；本文引言约 2/3 篇幅在讲 RSMA，语义部分只占一段。

## 5. 科研方法
- 模型：N 天线 BS、K 用户；有向概率图提取语义（提取率 ρ_k）；RSMA 下行（公共 + 私有）；计算时间 / 能耗 + 传输时间 / 能耗。
- 问题：最小化总能耗，约束含完成时间、语义精度、计算能力、速率与功率分配。
- 算法：交替优化三个子问题——提取率（Theorem 1 闭式解，拉格朗日）、计算频率（闭式）、功率 / 速率 / 波束成形（松弛变量 + SCA）。

## 6. 仿真与实验
- K = 5、20 MHz、路损 128.1 + 37.6 log10 d；语义任务参数沿用 [54]。
- 总能耗 vs 最大发射功率（含 1000 次初始化的穷举近似全局最优）、带宽、数据量、计算能力；对比 FDMA、NOMA。
- 结果节仅 660 词——网络优化类论文"仿真轻、建模与推导重"（50 个显示公式）。

## 7. 图表
- 9 图 1 表 1 算法。Fig. 2 多级语义提取示例；Fig. 5 精度与计算量随提取率的曲线（用于论证子问题结构）；结果图全为"总能耗 vs 参数"。

## 8. 句式库
- 多址动机："However, due to limited wireless resources such as frequency and time, conventional orthogonal multiple access schemes cannot support massive connectivity concern for next-generation wireless communication networks [5]."
- 结构相似性（idea 的核心句）："Due to the inherent similarity of common knowledge and common message, RSMA can be utilized to enhance the system performance of downlink semantic communication."
- 首创声明："To our best knowledge, there is no prior works that consider the integration of semantic communication and RSMA."
- 求解概述："To solve this problem, an alternating algorithm is proposed where the closed-form solutions for semantic information extraction ratio and computation frequency are obtained at each step."
- 解释趋势："This is because high bandwidth decreases the transmit time between users and the BS, which allows long computation time and consequently reduces the local computation energy consumption."

## 9. 结论
- 1 段 174 词，几乎逐句复述摘要；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：RSMA 资源分配文献；语义提取的概率图模型（[54]，同组前作）；FDMA / NOMA 下的能耗最小化。
- **增量**：首次把语义通信与 RSMA 结合，联合优化语义提取率、计算频率、功率、速率与波束成形以最小化总能耗（system-optimization + multi-user）。
- **为什么有效**：共同知识用公共消息一次广播给所有用户，私有语义更小、更省能；提取率在计算能耗与传输能耗之间折中。
- **证据**：在不同功率、带宽、数据量、算力下总能耗均低于 FDMA 与 NOMA，接近穷举初始化的结果。
- **弱点**：语义部分高度抽象（精度与计算量函数取自前作的拟合）；无真实语义数据或端到端语义性能评估；只验证能耗；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：用实际 deep JSCC 模型替换抽象语义函数，评估端到端语义性能；知识库更新频率与公共消息开销的权衡；不完美 CSI 下的鲁棒设计；RIS / ISAC 等其他技术与语义通信的结构性结合。
