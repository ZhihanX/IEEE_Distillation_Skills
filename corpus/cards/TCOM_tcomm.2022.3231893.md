---
doi: 10.1109/tcomm.2022.3231893
title: "Active RIS vs. Passive RIS: Which Will Prevail in 6G?"
journal: TCOM
year: 2023
band: 2022-2025
cites: 1070
cites_per_year: 297.9
article_type: research
topic: RIS
source: xplore-html
xplore: 9998527
auto:
  words_total: 9314
  n_sections: 8
  n_subsections: 29
  n_figures: 11
  n_tables: 0
  n_display_eq: 42
  n_algorithms: 2
  statements: {theorem: 0, lemma: 5, proposition: 0, corollary: 0, remark: 4, proof: 5, proof_in_appendix: 2}
  n_appendix: 2
  mean_sentence_words: 29.7
  we_per_1k: 12.1
  title_words: 10
  abstract_words: 211
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 1, however: 5, transition: 4, resultsShow: 1, motivatedBy: 1, toAddress: 14, gapWord: 0, nonconvex: 3, npHard: 0, closedForm: 2, outperform: 5, intensifier: 2, worthNoting: 0, observe: 8, thisIsBecause: 0, asExpected: 0, insight: 2, tradeoff: 0, figVerb: 0, promising: 3, gen: 4, contrast: 2, firstTime: 0, novel: 1, weProposeFirst: 4, wlog: 2, code: 0, prototype: 1}
  methods: {FP: 1, AO: 4, ADMM: 3, penalty: 6, lagrange: 5, convergence: 14, complexity: 11}
code:
  title_pattern: [versus, question, colon-subtitle]
  abstract_moves: [context, gap, aim, method, method, theory, method, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, gap, solution, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [develop, analyze, formulate, extend]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [limitation, new-architecture, comparison]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [FP, BCD, ADMM, penalty, closed-form]
  theory_role: supporting
  proofs_location: mixed
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [frequency, reflection-gain, distance, power-budget, number-of-elements, self-interference]
  fig1_role: architecture
  caption_style: descriptive
  prototype_or_measurement: true
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: true
  conclusion_future_work: true
---

## 1. 标题
- 问句式对比标题："A vs. B: Which Will Prevail in 6G?"，10 词。把论文的核心结论包装成悬念问题，不出现任何方法词。

## 2. 摘要（8 句）
- 1 背景："As a revolutionary paradigm for controlling wireless channels, …" → 2 空白（"multiplicative fading" 加引号命名问题）→ 3 "In this paper, the concept of active RISs is proposed to overcome this fundamental limitation." → 4 用 "Unlike passive RISs …" 定义新概念 → 5 信号模型 + 实测验证 → 6 渐近分析 → 7 和速率优化 → 8 结果带具体数字（"only a limited sum-rate gain of 22%, while active RISs can achieve a significant sum-rate gain of 130%"）。
- 摘要首尾呼应：结尾再次点名 "multiplicative fading" 被克服。

## 3. 引言逻辑（6 段，约 860 词）
1. 领域：1G→5G 改进收发机、信道不可控 → RIS 让信道可控 → 列优点和应用。
2. 空白：先承认优势（N² 增益）→ "However, in practice, these capacity gains are typically only observed in …" → 命名并解释 "multiplicative fading" → 指出已有工作回避了它（"Many existing works on RISs have bypassed this effect by only considering scenarios with severely obstructed direct links"）→ 用一个加粗式的问题收尾："How to break the fundamental performance bottleneck caused by the 'multiplicative fading' effect?"
3. 方案：主动 RIS，"At the expense of additional power consumption, …"（主动承认代价）+ 同期工作。
4. 贡献 4 条（develop / analyze / formulate / extend），按"模型→分析→优化→非理想扩展"推进。
5. 路线图；6. Notations。

## 4. Idea 是怎么提出的
- 空白类型：根本局限 + 新架构。先给现象起一个好记的名字（"multiplicative fading"），再说明它是物理层面的根本瓶颈，最后提出改硬件而不是改算法。
- 把研究问题写成一个直接问句，是本篇最可借鉴的写法。
- 反直觉点（Remark 4）：主动器件引入噪声，但 SNR 增益反而更高，并解释原因。

## 5. 科研方法
- 第 II 节先回顾被动 RIS 及其局限，再提出主动 RIS 硬件结构和信号模型（含热噪声项）。
- 第 III 节单用户渐近 SNR（Lemma 1/2），推出被动 RIS 超过主动 RIS 所需的元件数（Lemma 3）和适用场景（Lemma 4）。
- 第 IV 节 MU-MISO 和速率最大化：FP 等价变换（Lemma 5）后四块变量轮流更新，各有闭式或 QCQP 解。
- 第 V 节自干扰：建模 → MSE 最小化 → ADMM + SUMT 交替求解。
- 第 VI 节专门一节讲收敛与复杂度。

## 6. 仿真与实验
- 先用自制主动 RIS 单元实测验证信号模型（反射增益 vs 频率、噪声功率 vs 增益），再做系统仿真——"实测验证模型 + 仿真评估系统"的组合。
- baseline：被动 RIS [26]、随机相位、无 RIS；直连链路弱 / 强两种场景对照。
- 横轴：距离、总功耗、元件数、自干扰因子。

## 7. 图表
- 11 图 0 表。Fig. 1 两种 RIS 的硬件结构对比，Fig. 4 实验设备照片（多子图），Fig. 7 仿真场景布局。
- caption 描述型并交代系统："Simulation results for the sum-rate versus the number of RIS elements N in an RIS-aided MU-MISO system."

## 8. 句式库
- 研究问题："Therefore, to advance the practicability of RISs in future 6G wireless networks, a critical issue for RISs to be addressed is: How to break …?"
- 指出回避："Many existing works on RISs have bypassed this effect by only considering scenarios with severely obstructed direct links."
- 承认代价："At the expense of additional power consumption, active RIS can compensate for the large path loss of reflected links, …"
- 解释反直觉："The reason behind this counterintuitive behavior is that, …"
- 区分相近概念："Note that active RISs are fundamentally different from the relay-type RISs equipped with RF components …"

## 9. 结论
- 1 段 173 词，现在完成时（"we have proposed / developed / analyzed"），重复摘要里的 22% / 130%，最后一句列 4 个未来方向。
