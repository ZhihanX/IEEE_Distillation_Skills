---
doi: 10.1109/tcomm.2019.2944169
title: "Scheduling Policies for Federated Learning in Wireless Networks"
journal: TCOM
year: 2020
band: 2019-2021
cites: 586
cites_per_year: 86.7
article_type: research
topic: federated-edge-learning
source: xplore-html
xplore: 8851249
auto:
  words_total: 8575
  n_sections: 6
  n_subsections: 20
  n_figures: 8
  n_tables: 2
  n_display_eq: 68
  n_algorithms: 2
  statements: {theorem: 1, lemma: 2, proposition: 0, corollary: 6, assumption: 3, remark: 7, proof: 9, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 29.2
  we_per_1k: 10.6
  title_words: 8
  abstract_words: 277
  abstract_sentences: 11
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 1, however: 5, transition: 11, resultsShow: 0, motivatedBy: 1, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 4, intensifier: 1, worthNoting: 1, observe: 7, thisIsBecause: 4, asExpected: 0, insight: 4, tradeoff: 6, figVerb: 1, promising: 1, gen: 1, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 2, code: 0, prototype: 0}
  methods: {convergence: 38, stochGeom: 3, penalty: 2, DNN: 1, complexity: 1}
code:
  title_pattern: [X-for-Y, X-in-Y]
  abstract_moves: [context, context, context, context, gap, aim, theory, method, result, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 5
  intro_moves: [field, gap, prior, gap, aim, contrib, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [propose, develop, present, show, reveal]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: table
  gap_type: [theory-gap, new-scenario]
  motivating_figure: true
  problem_class: analysis-only
  solution: [stochastic-geometry, bound-surrogate]
  theory_role: central
  proofs_location: appendix
  complexity_analysis: false
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 3
  baseline_naming: acronym
  x_axes: [UE-subchannel-ratio, SINR-threshold, number-of-subchannels, training-steps]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[对象] for [任务] in [网络]"，8 词。标题只说研究对象（调度策略），不说方法（随机几何 + 收敛分析），典型分析型论文标题。

## 2. 摘要（11 句，277 词，偏长）
- 前四句铺背景：FL 出现的原因 → "Unlike centralized learning taking place in a data center, FL usually operates in a wireless edge network …" → 带宽有限只能调度部分 UE → 干扰导致传输不可靠。
- 空白一句："The performance of FL system in such a setting is not well understood."
- "In this paper, an analytical model is developed to characterize the performance of FL in wireless networks." → 收敛速率表达式 → 比较三种调度策略（RS / RR / PF）。
- 三句结论全是"条件式"洞见：高 SINR 门限下 PF 最好、低门限下 RR 更好；收敛速率随门限快速下降 → 压缩与量化的重要性；调度 UE 数与子信道带宽的权衡。无数字。

## 3. 引言逻辑（5 段，约 1140 词；内含 A. Approach and Summary of Contributions）
1. 云 → 边缘计算范式转变 → 端侧学习与隐私 → FL 流程（Fig. 1 在引言，三步 i)–iii)）→ "These properties identify the FL as one of the most promising technologies of future intelligent networks."
2. "Nonetheless, to make FL possible, one needs to tackle new challenges …"：非 i.i.d. 数据 + 有限频谱与不可靠信道 → 掉队者与容错。
3. 已有研究分两个方向："algorithmic and communication" 逐类综述 → 共同假设单小区、只有加性噪声 → "However, to fully realize the potential of federated learning, it is necessary to scale up the deployment across a large distributed network." → 干扰 + 调度 → "… a complete understanding of its performance … becomes essential."
4. （A 小节）"In this paper, we develop an analytical framework …"：PPP 建模 + 基于分布式坐标下降的算法 + 随机几何与优化理论 → 5 条 bullet 贡献（后两条是结论性发现）。
5. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：理论空白（大规模网络中 FL 性能"not well understood"）+ 新场景（多小区干扰 + 调度）。
- 写法亮点：先把已有 FL 研究二分为"算法视角 / 通信视角"，再指出两者共同的单小区无干扰假设；研究对象选的是"实际部署中现成的三种调度策略"，结论直接对应工程选择（何时用 PF、何时用 RR）。
- 贡献列表中有两条是"发现"而不是"方法"（"Through our analysis, we show that …"、"Our analysis also reveals that …"）。

## 5. 科研方法
- 模型：AP 与 UE 为独立 PPP、块衰落 + 路损、SINR 门限决定上传成功；三种调度策略在模型节用编号列表定义。
- 算法：Fenchel–Rockafellar 对偶 → 每个 UE 解局部二次子问题（分布式坐标上升，Algorithm 2）；Remark 1–3 说明相对标准 FL（Algorithm 1）的优势。
- 分析：Assumption 1–3（强凸、光滑、局部求解精度）→ Lemma 2 → Theorem 1（达到 ε 对偶间隙所需轮数）→ Corollary 1–3（RS / RR / PF 的成功概率与轮数）→ Remark 6/7 高 / 低 SINR 渐近比较 → 三种特例（一次性、多轮、全体不调度，Corollary 4–6）。
- "For better readability, most proofs and mathematical derivations have been relegated to the appendix."

## 6. 仿真与实验
- 分 "Numerical Study"（用解析式画"归一化通信轮数"）和 "Experimental Study"（MNIST 上训练 SVM 与 CNN 验证）。
- 每组结果后用 "In summary, …" 总结；实验与理论对照（"The results in the higher SINR regime are consistent with the theorems, …"），并如实报告低 SINR 下差异消失。

## 7. 图表
- 8 图 2 表 2 算法。Fig. 1 FL 流程示意（引言），Fig. 2 一轮迭代示意；Table I 记号、Table II 常见模型损失函数。caption 描述型，(a)(b) 子图分别说明高 / 低 SINR 条件。

## 8. 句式库
- 与集中式对比："Unlike centralized learning taking place in a data center, FL usually operates in a wireless edge network where the communication medium is resource-constrained and unreliable."
- 理解不足："The performance of FL system in such a setting is not well understood."
- 新挑战："Nonetheless, to make FL possible, one needs to tackle new challenges that require a fundamental departure from the standard methods designed for distributed optimization [7]."
- 已有研究分类："In response, considerable research has been carried out, which can be mainly categorized into two directions: algorithmic and communication."
- 扩展必要性："However, to fully realize the potential of federated learning, it is necessary to scale up the deployment across a large distributed network."
- 条件式结论："… running FL with PF outperforms RS and RR if the network is operating under a high … threshold, while RR is more preferable when the SINR threshold is low."

## 9. 结论
- 2 段 284 词：第 1 段现在完成时复述分析与三条发现；第 2 段讲框架的一般意义（"our work helps to understand how the key features of a wireless network … affect the convergence rate of FL …"）+ 未来方向（更先进的调度、massive MIMO、全双工、NOMA）。无数字。
