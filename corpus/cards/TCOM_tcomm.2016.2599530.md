---
doi: 10.1109/tcomm.2016.2599530
title: "Mobile-Edge Computing: Partial Computation Offloading Using Dynamic Voltage Scaling"
journal: TCOM
year: 2016
band: 2016-2018
cites: 737
cites_per_year: 71.3
article_type: research
topic: MEC-offloading
source: xplore-html
xplore: 7542156
auto:
  words_total: 7199
  n_sections: 6
  n_subsections: 24
  n_figures: 11
  n_tables: 1
  n_display_eq: 51
  n_algorithms: 5
  statements: {theorem: 2, lemma: 3, proposition: 0, corollary: 0, remark: 6, proof: 5, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 21.7
  we_per_1k: 16.6
  title_words: 9
  abstract_words: 198
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 7, contribList: 1, roadmap: 1, however: 3, transition: 27, resultsShow: 0, motivatedBy: 1, toAddress: 9, gapWord: 0, nonconvex: 9, npHard: 0, closedForm: 1, outperform: 2, intensifier: 1, worthNoting: 0, observe: 7, thisIsBecause: 5, asExpected: 1, insight: 0, tradeoff: 1, figVerb: 10, promising: 1, gen: 0, contrast: 3, firstTime: 0, novel: 0, weProposeFirst: 4, wlog: 1, code: 0, prototype: 0}
  methods: {convergence: 6, complexity: 2, lyapunov: 1}
code:
  title_pattern: [colon-subtitle, verb-ing]
  abstract_moves: [context, aim, method, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, prior, gap, gap, contrib, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, derive, propose, study]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: table
  gap_type: [combination, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [reformulation, closed-form, heuristic, exhaustive-search]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: false
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 4
  baseline_naming: descriptive
  x_axes: [distance, latency-constraint, number-of-servers, iterations]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[领域]: [问题] Using [技术]"，冒号前放领域名、冒号后放具体问题 + 使能技术，9 词。

## 2. 摘要（8 句，198 词）
- 第 1 句一句话交代组合的价值："The incorporation of dynamic voltage scaling technology into computation offloading offers more flexibilities for mobile edge computing."
- 第 2 句 "In this paper, we investigate … by jointly optimizing … with two system design objectives: … (ECM) and … (LM)."——两个目标并列并给缩写。
- 方法句均以 "To tackle / To address …, we …" 开头，一问题一方法。
- 结尾 "extensive simulations demonstrate that our proposed algorithms can significantly reduce …"，无数字。

## 3. 引言逻辑（6 段，约 850 词）
1. 设备资源有限 → "To address this limitation, computation offloading provides a promising technique …"
2. 卸载架构（MAUI、CloneCloud、TROPIC…）→ 关键挑战："how to balance the tradeoff between computation cost and communication cost"。
3. 全卸载 vs 部分卸载 → 逐篇列部分卸载工作 → "However, the aforementioned researches only consider a fixed computational speed of SMD, which is neither energy-optimal nor latency-optimal at the SMD's side."
4. DVS 介绍 → 唯一相关工作 [19] 的两点不足 → "Consequently, the existing offloading designs cannot be directly utilized … This motivates the study of this paper."
5. "In this paper, we focus on …" → 首创声明 → 说明部分结果已在会议版发表（"Part of the results have been presented in our previous work, …"）→ 4 条贡献。
6. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：组合（DVS × 部分卸载）+ 已有工作假设过强（CPU 速度固定）。
- 写法：先找出"唯一沾边的工作"并列出它的两处不足，再说明新变量（DVS）让问题更难（"DVS technology further complicates partial computation offloading decisions by …"），证明不是简单叠加。
- 首创句："To our knowledge, we are the first to design the energy-optimal and latency-optimal partial computation offloading strategies when SMD has the capability of DVS."
- 期刊扩展会议版时主动披露差异，是 IEEE 期刊的规范做法。

## 5. 科研方法
- 两个对偶问题：能耗最小（时延约束）、时延最小（能耗约束）。
- ECM：变量替换化为凸问题，除卸载比外全闭式；Theorem 1 给出结构性结论（有 DVS 时全卸载不可能最优）。
- LM：非凸非光滑，引入辅助变量光滑化，单变量搜索求局部最优，Theorem 2 保证收敛。
- 都扩展到多服务器（计算分配闭式 + 小规模穷举用户关联）。
- 6 个 Remark 用来处理实际问题（时延敏感性、量化分割比例）。

## 6. 仿真与实验
- 参数写在正文，每个参数都标注出处（"P0 = 0.4 W [13]"、"so that the energy consumption is consistent with the measurements in [37]"）——参数可信度靠引用撑。
- baseline：全卸载、本地执行、无 DVS 的部分卸载、穷举（LES）。
- 结果写法："As expected, EPCO outperforms the other three schemes, since it combines the advantages of …"，并用在线游戏举例说明意义。

## 7. 图表
- 11 图 1 表（参数符号表）5 个算法框。caption 极短："The minimum energy consumption vs. d."

## 8. 句式库
- 一句话价值："The incorporation of dynamic voltage scaling technology into computation offloading offers more flexibilities for …"
- 关键挑战："… a key technical challenge is how to balance the tradeoff between computation cost and communication cost …"
- 共同局限："However, the aforementioned researches only consider a fixed computational speed of SMD, which is neither energy-optimal nor latency-optimal …"
- 不能直接套用："Consequently, the existing offloading designs cannot be directly utilized for … This motivates the study of this paper."
- 会议版披露："Part of the results have been presented in our previous work, which investigates …"

## 9. 结论
- 1 段 166 词，现在完成时逐条复述，无数字、无未来工作。
