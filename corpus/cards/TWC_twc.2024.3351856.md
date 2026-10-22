---
doi: 10.1109/twc.2024.3351856
title: "Integrated Sensing and Communication With Massive MIMO: A Unified Tensor Approach for Channel and Target Parameter Estimation"
journal: TWC
year: 2024
band: 2022-2025
cites: 338
cites_per_year: 155.4
article_type: research
topic: ISAC-sensing
source: xplore-html
xplore: 10403776
auto:
  words_total: 8836
  n_sections: 7
  n_subsections: 11
  n_figures: 8
  n_tables: 2
  n_display_eq: 60
  n_algorithms: 2
  statements: {theorem: 0, lemma: 2, proposition: 1, corollary: 0, remark: 6, proof: 3, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 29.8
  we_per_1k: 8.6
  title_words: 17
  abstract_words: 262
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 1, roadmap: 0, however: 3, transition: 5, resultsShow: 1, motivatedBy: 1, toAddress: 4, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 1, outperform: 0, intensifier: 4, worthNoting: 0, observe: 8, thisIsBecause: 2, asExpected: 0, insight: 2, tradeoff: 2, figVerb: 6, promising: 1, gen: 1, contrast: 5, firstTime: 0, novel: 1, weProposeFirst: 6, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 4, compressedSensing: 3, CRB: 1, convergence: 1}
code:
  title_pattern: [X-with-Y, colon-subtitle, X-for-Y]
  abstract_moves: [context, gap, aim, method, method, theory, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 7
  intro_moves: [field, prior, gap, prior, gap, prior, gap, aim, contrib, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [characterize, propose, propose, propose]
  contrib_quantified: false
  first_claim: true
  roadmap: false
  notation: intro-end
  gap_type: [unification, limitation]
  motivating_figure: true
  problem_class: estimation
  solution: [tensor-decomposition, reformulation]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: false   # 只有 CPU 运行时间表，并坦承部分参数估计复杂度更高
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4
  baseline_naming: acronym
  x_axes: [SNR, success-rate, runtime, bandwidth]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[A] With [B]: A Unified [工具] Approach for [任务 1] and [任务 2]"，17 词（偏长）。冒号前是场景组合，冒号后用 "A Unified … Approach" 点明"一个方法解决两件事"。

## 2. 摘要（9 句，262 词）
- 第 1 句组合价值（ISAC × massive MIMO）；第 2 句 "However, a large number of antennas … raises critical challenges in acquiring both accurate channel state information and target parameter information."（两个挑战）。
- "To overcome these two challenges with a unified framework, we first analyze … and then propose a novel tensor-based approach …"——以 we 为主语的锚点句。
- Specifically / Then / On this basis / Then / In addition 串起：参数化信道 → 共享训练模式 → CPD 唯一性与最大可分辨目标数 → 统一算法 → 波束斜视情形。末句结果无数字。

## 3. 引言逻辑（7 段，约 1400 词；无路线图）
1. ISAC 与 massive MIMO 各自的地位 → 二者结合的前景与应用。
2. 已有 ISAC 设计（多波束、OFDM 感知、联合设计）→ "…, the aforementioned ISAC techniques generally assume a-priori of accurate communication channel state information or partially known target parameter information."
3. 雷达参数估计的经典方法（MUSIC、ESPRIT、压缩感知）及其在 ISAC 中的扩展 → 但通信仍需准确 CSI，大规模天线下训练开销巨大。
4. 大规模 MIMO 参数化信道估计（ESPRIT、变分贝叶斯、压缩感知、张量 CPD）逐篇。
5. 关键观察："It should be highlighted that the aforementioned parameterized channel estimation approaches exhibit some similarities to the estimation of target angles …"（目标可视为"不合作的通信用户"）→ 已有联合工作只适用 LoS → "However, these approaches can only acquire part of channel parameters …, while fail to simultaneously estimate …"
6. "In this paper, we investigate … under a unified framework …" + 4 条 bullet（第 1 条 "We make the first attempt to characterize …"）。
7. Notations。

## 4. Idea 是怎么提出的
- 空白类型：统一（信道估计与目标参数估计在数学上同构）+ 已有方法局限（只估部分参数 / 只适用 LoS）。
- 写法亮点：idea 来自一个"结构相似性"的观察——通信信道与感知信道表达式相同（模型节再次强调 "it can be interestingly observed that … exhibit a similar mathematical expression, which lays the foundation for …"），于是用同一训练信号、同一张量模型同时解决两个问题。
- 引言按"ISAC 文献 → 雷达估计文献 → 信道估计文献 → 两者相似性"四条线收拢。

## 5. 科研方法
- 模型：通信信道（多径时延、多普勒、AoA/AoD）与感知信道（目标距离、速度、方位）分别建模 → 统一模型（Remark 1/2 解释两者参数的物理含义差异）。
- 共享训练模式 → 回波与下行接收信号都写成三阶 CPD 张量 → Lemma 1（Kruskal 条件）、Lemma 2（Vandermonde 结构下更强的可辨识性）→ Table I 最大可分辨目标数。
- 算法：先估因子矩阵（ESPRIT-like，空间平滑）→ 再提取参数；AoD 与多普勒耦合用迭代交替估计；"Discussions" 小节讨论非目标干扰、目标数未知、导频设计等实际问题。
- 波束斜视：分段训练模式 + 新的 CPD 形式 + Proposition 1 唯一性条件。证明在正文。

## 6. 仿真与实验
- 参数写在正文（28 GHz、64 发射天线、100 MHz）。
- Fig. 2 用散点图对比基准与本文的目标参数估计（三行子图：AoA、AoD-距离极坐标、距离-速度）。
- 成功率、RMSE vs SNR（含 CRB 下界）、信道 NMSE、CPU 运行时间表——并坦承 "…, though it is higher for channel estimation …"（复杂度不占优的部分如实写出）；最后波束斜视情形。

## 7. 图表
- 8 图 2 表 2 算法。Fig. 1 系统与通信 / 感知信道模型合一示意。Table I 是理论结果表（最大可分辨目标数），Table II 运行时间。caption 多为短标签，Fig. 2 为长描述（逐行说明子图内容）。

## 8. 句式库
- 隐含假设："…, the aforementioned ISAC techniques generally assume a-priori of accurate communication channel state information or partially known target parameter information."
- 结构相似性："It should be highlighted that the aforementioned parameterized channel estimation approaches exhibit some similarities to the estimation of target angles and other parameters in traditional MIMO radar sensing systems."
- 类比："… the targets can thus be virtually regarded as an uncooperative communication user [39], [40]."
- 统一模型基础："… the communication channel and the sensing channel exhibit a similar mathematical expression, which lays the foundation for developing a unified algorithmic framework …"
- 首创（贡献列表内）："We make the first attempt to characterize the target parameter information and channel state information in a unified framework …"

## 9. 结论
- 1 段 179 词，过去时复述（was developed / established / proposed / analyzed）→ "Numerical results verified our theoretical analysis and the superiority of …"。无数字、无未来工作。
