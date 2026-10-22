---
doi: 10.1109/jsac.2023.3288261
title: "Stacked Intelligent Metasurfaces for Efficient Holographic MIMO Communications in 6G"
journal: JSAC
year: 2023
band: 2022-2025
cites: 390
cites_per_year: 122.8
article_type: research
topic: RIS
source: xplore-html
xplore: 10158690
auto:
  words_total: 8148
  n_sections: 6
  n_subsections: 18
  n_figures: 17
  n_tables: 0
  n_display_eq: 29
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 2, corollary: 0, remark: 5, proof: 2, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 28.8
  we_per_1k: 9.3
  title_words: 10
  abstract_words: 254
  abstract_sentences: 11
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 2, roadmap: 1, however: 4, transition: 31, resultsShow: 0, motivatedBy: 2, toAddress: 4, gapWord: 0, nonconvex: 2, npHard: 0, closedForm: 0, outperform: 2, intensifier: 1, worthNoting: 0, observe: 1, thisIsBecause: 0, asExpected: 1, insight: 4, tradeoff: 1, figVerb: 7, promising: 0, gen: 5, contrast: 0, firstTime: 0, novel: 3, weProposeFirst: 1, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 5, convergence: 6, penalty: 2}
code:
  title_pattern: [X-for-Y, X-in-Y]
  abstract_moves: [context, context, aim, method, method, method, method, method, method, theory, result]
  abstract_has_numbers: true
  abstract_anchor: we-verb
  intro_paragraphs: 8
  intro_moves: [field, prior, prior, prior, gap, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: numbered
  contrib_n: 4
  contrib_verbs: [establish, formulate, analyze, demonstrate]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-architecture, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [gradient]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [number-of-layers, number-of-elements, element-spacing, number-of-streams, iterations, SNR]
  fig1_role: architecture
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: true
  conclusion_future_work: true
---

## 1. 标题
- "[新器件] for Efficient [新范式] Communications in 6G"，10 词。两个新概念（SIM、HMIMO）+ "in 6G" 时代标签。

## 2. 摘要（11 句，254 词）
- 无 "In this paper"，用 "We harness this new SIM for …" 起目标句。
- 1–2 用两句介绍新器件及与单层超表面（RIS、透镜）的关系。
- 方法部分用序数词串联："First of all, … Secondly, … We then … Furthermore, … Finally, …"。
- 第 5 句用 "In sharp contrast to the conventional MIMO designs, SIM is capable of automatically accomplishing transmit precoding and receiver combining, as the EM waves propagate through them."——机理对比句。
- 结尾给数字："e.g., 150% capacity improvement over both conventional MIMO and its RIS-aided counterparts."

## 3. 引言逻辑（小节化：A 相关技术 / B 动机 / C 贡献 / D 组织 / E 记号）
1. 6G 愿景（3GPP R17、500 亿设备预测、通信感知计算控制一体化）。
2–4. A. Related Technologies：分 RIS、HMIMO 两小节综述；HMIMO 小节里抛出问题 "a natural question arises– what will the next-generation MIMO be like?"
5. B. Motivation："we first elaborate on our motivation by answering the question– why do we need SIM? – from the following three perspectives:"，编号列出三点（HMIMO 缺实现、RIS 的乘性路损与 MAC 负担、DL 受限于 CPU/GPU → 波计算）。
6. C. Contributions："Motivated by the aforementioned observations, …" + 4 条编号贡献（establish / formulate / analyze / demonstrate）。
7. D. Organization；8. E. Notations。

## 4. Idea 是怎么提出的
- 空白类型：新架构（多层超表面）+ 已有方案局限（单层超表面自由度有限、RIS 乘性衰落、数字计算瓶颈）。
- 写法亮点：用两个设问句组织动机（"what will the next-generation MIMO be like?" 和 "why do we need SIM?"），然后分三点作答——引言里的"自问自答"结构。
- 把新器件和三个不同方向（HMIMO、RIS、波域计算）同时挂钩，抬高定位。

## 5. 科研方法
- 系统模型很长（约 2400 词）：基于 Rayleigh-Sommerfeld 衍射理论写层间传输系数，空间相关 HMIMO 信道。
- 问题：最小化端到端信道与目标对角阵的 Frobenius 误差（"channel fitting"）——把"让信道变成并行子信道"转成拟合问题，是本篇独特的形式化。
- 求解：梯度下降，分 Step 1–5（求偏导、归一化防梯度爆炸 / 消失、更新相位、更新缩放因子、指数衰减学习率），算法写成表格。
- 分析：容量上下界（最好 / 最差子信道），Proposition 1/2 给缩放律；复杂度按实数乘法次数计。
- 5 个 Remark 主动交代简化假设（连续相位、层间系数偏差、相关模型、自适应增益）。

## 6. 仿真与实验
- 先扫系统参数（层数、每层单元数、单元间距、数据流数），NMSE 和容量成对出图（Fig. 3/4、5/6、7/8、9/10）。
- 再验证算法（端到端信道矩阵可视化热图、收敛曲线），最后和 massive MIMO、RIS-MIMO、单层超表面比较。
- 结论里提炼出设计规则："a 7-layer SIM having half-wavelength element spacing achieved an excellent channel fitting performance"。

## 7. 图表
- 17 图（本批最多之一）。Fig. 1 传统 MIMO vs SIM-HMIMO 的对比示意，Fig. 2 详细结构。
- caption 描述型且附参数："The channel capacity versus the number of transmit metasurface layers, where we have S = 4, M = N = 100, …"

## 8. 句式库
- 设问："As the 6G research is ramping up, a natural question arises– what will the next-generation MIMO be like?"
- 动机引导："Before proceeding, we first elaborate on our motivation by answering the question– why do we need SIM? – from the following three perspectives:"
- 机理对比："In sharp contrast to the conventional MIMO designs, SIM is capable of …"
- 研究起步："The existing research on HMIMO communications is still in its infancy and lacks practical implementations."
- 承上启下："Motivated by the aforementioned observations, in this paper, we present …"

## 9. 结论
- 2 段：第 1 段过去时复述；第 2 段 "In conclusion, our pivotal findings are as follows."，按 Firstly / Secondly 给出设计规则和数字（7 层、150%），最后提出主动 SIM 作为未来方向。
