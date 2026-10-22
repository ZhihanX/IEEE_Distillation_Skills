---
doi: 10.1109/jsac.2023.3240707
title: "Energy Efficiency Maximization in RIS-Assisted SWIPT Networks With RSMA: A PPO-Based Approach"
journal: JSAC
year: 2023
band: 2022-2025
cites: 309
cites_per_year: 90.2
article_type: research
topic: RIS
source: xplore-html
xplore: 10032267
auto:
  words_total: 7159
  n_sections: 6
  n_subsections: 20
  n_figures: 13
  n_tables: 1
  n_display_eq: 52
  n_algorithms: 4
  statements: {theorem: 0, lemma: 0, proposition: 2, corollary: 0, remark: 1, proof: 2, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 25.3
  we_per_1k: 1.1
  title_words: 12
  abstract_words: 255
  abstract_sentences: 9
  phrases: {toTheBest: 1, inThisPaper: 1, contribList: 1, roadmap: 1, however: 3, transition: 29, resultsShow: 2, motivatedBy: 0, toAddress: 2, gapWord: 0, nonconvex: 2, npHard: 1, closedForm: 0, outperform: 1, intensifier: 0, worthNoting: 0, observe: 10, thisIsBecause: 1, asExpected: 1, insight: 1, tradeoff: 0, figVerb: 11, promising: 0, gen: 2, contrast: 1, firstTime: 0, novel: 1, weProposeFirst: 1, wlog: 1, code: 0, prototype: 0}
  methods: {SCA: 19, convergence: 8, complexity: 6, DNN: 3, FP: 3, penalty: 3, DRL: 2, SDR: 1, convexOpt: 1}
code:
  title_pattern: [X-in-Y, X-aided-Y, X-with-Y, colon-subtitle]
  abstract_moves: [aim, method, method, method, method, method, result, result, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 10
  intro_moves: [field, tech, tech, tech, prior, gap, prior, gap, aim, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [formulate, propose, formulate, show]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [combination, tool-transfer]
  motivating_figure: true
  problem_class: MINLP
  solution: [DRL, DNN, SCA, FP, SDR, AO, relaxation]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 4
  baseline_naming: descriptive
  x_axes: [episodes, number-of-antennas, phase-resolution, RIS-location, number-of-elements, EH-threshold, time-varying, CSI-error]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[目标] Maximization in [技术 A]-Assisted [技术 B] Networks With [技术 C]: A PPO-Based Approach"，12 词。三个热点技术缩写同时进入标题，冒号后方法副标题。

## 2. 摘要（9 句，255 词）
- "This paper investigates reconfigurable intelligent surface (RIS)-assisted simultaneous wireless information and power transfer (SWIPT) networks with rate splitting multiple access (RSMA)."——三个全称一次写全。
- 问题一句（列全四类变量）→ "To tackle the non-convex problem with both discrete and continuous variables, a deep reinforcement learning-based approach is proposed with the proximal policy optimization (PPO) framework."
- 与传统优化对比："Different from traditional optimization approaches which optimizes the beamforming vectors and phase shifts separately and alternatively, our proposed PPO-based approach optimizes all the variables in unison."
- 为评估 DRL 另设计 SCA + Dinkelbach 方案（SCA-D）作为参照 → 三句结果（接近 SCA-D、RSMA 贡献大、时变信道下运行时间短）。无数字。

## 3. 引言逻辑（10 段，约 1510 词；内分 A. Background / B. Related Work and Motivation / C. Contributions）
1. IoT 设备 2025 年超 750 亿 → 能耗与频谱 → 能效（EE）是核心指标。
2. RSMA 原理（公共流 + 私有流，SIC）→ B5G/6G 候选。
3. 高频 LoS 依赖 → RIS。
4. IoT 电池受限 → SWIPT（PS 接收机）→ 三者互补："Fortunately, the common stream can be used as an energy carrier in RSMA, …, while a virtual LoS link can be established by employing RIS." → "designing RIS-assisted SWIPT with RSMA is of great significance …"
5. （B 小节）RIS-SWIPT 工作与 RSMA+RIS / RSMA+SWIPT 工作逐篇（每篇写目标与约束）。
6. "Nevertheless, in the aforementioned works …, only two of the technologies of RSMA, RIS, and SWIPT were investigated in a single communication system …" → 首创式空白："To the best of the authors' knowledge, the energy-efficient system design for RIS-assisted SWIPT networks with RSMA has still been an open issue thus far."
7. 第二条线：时变信道要求快速计算 → DRL 工作逐篇 → "Nevertheless, the optimality of the DRL-based approaches is not guaranteed, which is required to be evaluated by the optimization approaches."
8. （C 小节）"In this work, we focus on …" + 4 条 bullet。
9. 路线图；10. Notations。

## 4. Idea 是怎么提出的
- 空白类型：组合（三种技术首次放在同一系统）+ 工具迁移（PPO 处理离散 + 连续混合变量）。
- 写法亮点：把"三技术组合"的合理性落到具体机制（RSMA 公共流可兼作能量载体且不干扰私有流解码；RIS 补 LoS），不是简单拼接。
- 方法论上的自我约束：明确承认 DRL 不保证最优，因此另设计一个基于优化的上界方案（SCA-D）专门用来"评估"DRL——学习方法 + 优化参照的双方案结构。

## 5. 科研方法
- 模型：多天线发射端、K 个 PS 用户、离散相位 RIS、1 层 RSMA、非线性 EH 模型；EE = 和速率 / 总功耗；Proposition 1：NP-hard。
- PPO：MDP 的动作空间（功率用 tanh 生成、方向由 MRT（公共流）+ ZF（私有流）构造——Remark 1 解释理由、PS 比、公共速率、离散相位）、状态空间（"include as much environmental information related to Problem P0 as possible"）、动态奖励函数（含约束违反惩罚）；裁剪代理目标保证单调改进；位置小变化无需重训。
- SCA-D：放松离散相位得上界问题（Proposition 2）→ 交替优化：给定相位时 SDR + Dinkelbach + SCA；给定其余变量时相位用一阶近似 SCA（Algorithm 2–4）；复杂度 O(·)。

## 6. 仿真与实验
- 参数写在正文（3GPP TR 36.814 路损、Rician 4、非线性 EH 参数出处）；Table I 为 PPO 超参数；网络结构（四层前馈）与输入输出维度写明。
- 结果小节 A–I：收敛（滑动窗口平滑）→ 消融实验（每次去掉一类变量）→ 与 MRT 设计、Split 设计比较 → 连续 vs 离散相位、无 RIS → RSMA vs SDMA（随 RIS 位置）→ 换目标（和速率、功率最小化）检验通用性 → 更多用户 / 更大 RIS / 更远距离 → 非线性 vs 线性 EH → 时变信道（运行时间优势）→ 非完美 CSIT。

## 7. 图表
- 13 图 1 表 4 算法。Fig. 1 系统图，Fig. 2 PPO 框架图。caption 短标签（"The achievable EE with employing RSMA and SDMA."）。

## 8. 句式库
- 规模数字开场："… a large number of wireless Internet-of-Things (IoT) devices have been deployed …, which is expected to exceed 75 billion by 2025 [1]."
- 技术互补："Fortunately, the common stream can be used as an energy carrier in RSMA, …, while a virtual LoS link can be established by employing RIS."
- 只研究了其中两项："Nevertheless, in the aforementioned works …, only two of the technologies of RSMA, RIS, and SWIPT were investigated in a single communication system …"
- 首创式空白："To the best of the authors' knowledge, the energy-efficient system design for RIS-assisted SWIPT networks with RSMA has still been an open issue thus far."
- 承认学习方法的局限："Nevertheless, the optimality of the DRL-based approaches is not guaranteed, which is required to be evaluated by the optimization approaches."
- 与传统交替优化区分："Different from traditional optimization approaches which optimizes the beamforming vectors and phase shifts separately and alternatively, our proposed PPO-based approach optimizes all the variables in unison."

## 9. 结论
- 1 段 141 词，过去时被动复述（was proposed / was reformulated / was further proposed）→ 有效性与 RSMA 的贡献。无数字、无未来工作。全文 we 密度仅 1.1 / 千词——几乎全被动语态。
