---
doi: 10.1109/jsac.2020.3000835
title: "Reconfigurable Intelligent Surface Assisted Multiuser MISO Systems Exploiting Deep Reinforcement Learning"
journal: JSAC
year: 2020
band: 2019-2021
cites: 900
cites_per_year: 145.7
article_type: research
topic: RIS
source: xplore-html
xplore: 9110869
auto:
  words_total: 6229
  n_sections: 6
  n_subsections: 14
  n_figures: 12
  n_tables: 1
  n_display_eq: 18
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 25.0
  we_per_1k: 5.1
  title_words: 11
  abstract_words: 231
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 11, contribList: 1, roadmap: 1, however: 5, transition: 2, resultsShow: 2, motivatedBy: 0, toAddress: 6, gapWord: 0, nonconvex: 5, npHard: 0, closedForm: 2, outperform: 0, intensifier: 10, worthNoting: 0, observe: 12, thisIsBecause: 3, asExpected: 1, insight: 0, tradeoff: 1, figVerb: 4, promising: 1, gen: 4, contrast: 6, firstTime: 0, novel: 0, weProposeFirst: 0, wlog: 0, code: 0, prototype: 1}
  methods: {DNN: 22, convergence: 16, AO: 5, DRL: 3, FP: 3, WMMSE: 3, complexity: 3, compressedSensing: 1, convexOpt: 1, manifold: 1}
code:
  title_pattern: [X-aided-Y, verb-ing]
  abstract_moves: [context, context, aim, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 13
  intro_moves: [field, tech, tech, tech, prior, prior, prior, prior, prior, contrib, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [propose, describe, contrast]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [tool-transfer, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [DRL, DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [transmit-power, number-of-elements, time-steps, CDF, learning-rate]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[器件] Assisted [系统] Exploiting [工具]"，11 词。工具（DRL）放在动名词短语里，和"X via Y"同功能。

## 2. 摘要（7 句，231 词）
- 1–2 背景：RIS 被看作 6G 关键技术、无需射频链。
- 3 "In this paper, we investigate the joint design of … by leveraging recent advances in deep reinforcement learning (DRL)."
- 4 方法；5 差异化："Unlike the most reported works utilizing the alternating optimization techniques to alternatively obtain …, the proposed DRL based algorithm obtains the joint design simultaneously …"
- 6–7 结果只说"comparable performance compared with two state-of-the-art benchmarks"，并承认超参数对性能影响大。无数字。

## 3. 引言逻辑（4 段 + A. Prior Works 5 段 + B. Contributions）
1. 5G massive MIMO 成功 → "However, implementing a Massive-MIMO base station (BS) is challenging, …"
2–3. RIS 的物理基础和反射阵工作方式、部署优势。
4. 与雷达反射面、中继的区别（"active" vs "passive" 波束成形）。
5–7. 已有工作：先硬件，再单用户优化（逐篇一句：方法 + 目标），再多用户（"All above mentioned works focus on single user MISO systems."）。
8–9. AI / DL / DRL 在无线中的应用，DRL 适合时变信道。
10. "In this paper, we investigate …" + 问题非凸、最优解未知 + DDPG → 3 条贡献。
11. 结果概述；12. 路线图；13. 记号。

## 4. Idea 是怎么提出的
- 空白类型：工具迁移（把 DDPG 用到 RIS 联合波束成形）+ 已有交替优化的局限（交替求解、高维）。
- 首创式表述较弱："This paper is a very early attempt to formulate a framework that incorporates the DRL technique into …"（用 "very early attempt" 而不是 "first"，更稳妥）。
- 卖点放在"联合输出"和"无需显式模型"上，而非性能更好（性能只是 comparable）。

## 5. 科研方法
- 系统：多用户 MISO，假设直连链路完全阻断；目标是遍历和速率。
- 单列一节 "Preliminary Knowledge of DRL"（RL 概念 bullet 列表、Q-learning、DDPG），再在下一节定义状态、动作、奖励。
- 无定理、无收敛证明；复杂度只有定性说法。

## 6. 仿真与实验
- 信道直接用 Rayleigh 生成，并说明"large scale path loss and the shadowing effects have been compensated"，理由是 "the objective of this paper in its current format is to develop a framework"——简化假设有明确交代。
- 2 个 state-of-the-art baseline；超参数表 Table I。
- 结果多为训练曲线（奖励 vs 步数）和对学习率 / 衰减率的敏感性分析——学习类论文特有。
- 最后坦白："the performance of DRL based algorithms is very sensitive to initialization of the DNN and the other hyper-parameters"。

## 7. 图表
- 12 图 1 表。Fig. 1 系统图（长 caption，说明 RIS 贴在建筑立面）、Fig. 2/3 网络结构示意。
- 结果 caption 描述型："Sum rate versus Pt to show the proposed DRL-based algorithm in comparison with two benchmarks."

## 8. 句式库
- 挑战："However, implementing a Massive-MIMO base station (BS) is challenging, as high hardware cost, constrained physical size, and increased power consumption …"
- 归纳已有工作："All above mentioned works focus on single user MISO systems."
- 与主流方法切割："Unlike the most reported works utilizing the alternating optimization techniques …"
- 谨慎首创："This paper is a very early attempt to formulate a framework that incorporates …"
- 交代简化："This is because the objective of this paper in its current format is to develop a framework for …"

## 9. 结论
- 1 段 211 词，几乎逐句复述贡献列表和摘要（被动语态 "was proposed"），无数字、无未来工作。
