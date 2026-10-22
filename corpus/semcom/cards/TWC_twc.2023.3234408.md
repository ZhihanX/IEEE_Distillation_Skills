---
doi: 10.1109/twc.2023.3234408
title: "Predictive and Adaptive Deep Coding for Wireless Image Transmission in Semantic Communication"
journal: TWC
year: 2023
band: 2022-2025
cites: 274
cites_per_year: 86.3
article_type: research
topic: semantic
source: xplore-html
xplore: 10015684
auto:
  words_total: 8615
  n_sections: 4
  n_subsections: 13
  n_figures: 13
  n_tables: 0
  n_display_eq: 14
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 30.2
  we_per_1k: 15.8
  title_words: 12
  abstract_words: 271
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 13, contribList: 0, roadmap: 1, however: 9, transition: 4, resultsShow: 5, motivatedBy: 1, toAddress: 5, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 2, intensifier: 1, worthNoting: 0, observe: 19, thisIsBecause: 1, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 1, promising: 0, gen: 0, contrast: 2, firstTime: 0, novel: 1, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 4, convergence: 4, DNN: 1, bisection: 1}
  domain: {DeepJSCC: 99, PSNR: 72, CIFAR: 16, AWGN: 13, LDPC: 10, Rayleigh: 9, BPG: 8, CNN: 5, ImageNet: 5, Kodak: 5, attention: 5, JPEG: 4, JPEG2000: 4}
code:
  title_pattern: [X-for-Y, X-in-Y]
  abstract_moves: [context, context, gap, aim, method, implication, result, result]
  abstract_has_numbers: true    # "average error lower than 0.5dB"
  abstract_anchor: in-this-paper
  intro_paragraphs: 12
  intro_moves: [field, field, prior, tech, prior, gap, prior, prior, gap, aim, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, propose, propose, use]
  contrib_quantified: false
  first_claim: true             # "It is necessary to emphasize that, instance-level CR optimization is a new problem and has not been considered before."
  roadmap: true
  notation: intro-end
  gap_type: [limitation, practicality]
  motivating_figure: true
  problem_class: learning
  solution: [DNN, exhaustive-search]   # CR 优化器按表查找 / 逐级搜索最小 CR
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2                # ADJSCC（多个固定 CR 模型）、BPG + LDPC
  baseline_naming: acronym
  x_axes: [SNR, target-quality, compression-ratio, channel-index]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: true  # "average prediction error … lower than 0.5dB"
  conclusion_future_work: true
semcom:
  category: image-jscc
  source: [image]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [CNN]
  channel: [AWGN, Rayleigh]
  adaptivity: [SNR, bandwidth-rate, content]
  training: [multi-stage]        # 先训练 DeepJSCC-V，再用它训练 OraNet
  metrics: [PSNR]
  datasets: [CIFAR-10, CIFAR-100, ImageNet, Kodak]
  baselines: [other-learned, separate]
  snr_mismatch_test: false
  complexity_reported: false
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [adaptivity, new-component]   # 可变码长 + 质量预测网络（OraNet）
  builds_on: [ADJSCC, DeepJSCC-A]
  open_problems_n: 3
---

## 1. 标题
- "[形容词 + 形容词] Deep Coding for [任务] in [范式]"，12 词。

## 2. 摘要（8 句，271 词）
- 两句背景 → 空白："However, existing DeepJSCC-based semantic communication frameworks still cannot achieve adaptive code rates for different channel SNRs and image contents, which reduces its flexibility and bandwidth efficiency." → 本文（给定目标质量下的码率优化）→ 三个模块一句写完 → 两句结果（含 "average error lower than 0.5dB"）。

## 3. 引言逻辑（12 段，约 1680 词）
- 分离式编码与悬崖效应 → JSCC → DeepJSCC → 两条 bullet 列出已有 DeepJSCC 的两个问题（SNR 自适应、CR 自适应）→ 用数字说明代价："… we need to prepare 5×8=40 DeepJSCC models, which greatly increases the training and deployment cost …" → ADJSCC 解决 SNR 自适应 → DeepJSCC-A 解决 CR 自适应但有四点不足（逐条 "First … Secondly … Thirdly … Fourthly"）→ 类比传统系统的自适应调制编码依赖已知的性能-SNR 关系，而语义通信中质量同时取决于 SNR、CR、内容，关系难以建模 → 第三个问题：传输质量预测 → 本文 4 条贡献。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（一模型一 SNR 一 CR；DeepJSCC-A 码率选择有限且无法控制质量）+ 实用性（部署成本、按质量要求控制带宽）。
- 核心洞见：传统链路自适应之所以可行，是因为"BER/BLER 随 SNR 的关系已知"；语义通信缺的正是这张表——于是训练一个网络（OraNet）来预测"给定内容、SNR、CR 时的重建质量"，再据此做码率优化。"先预测质量，再按质量约束最小化资源"是可迁移的一般套路。
- 把问题分为数据级（平均 PSNR 约束）与实例级（每张图的 PSNR 约束），并声明后者是新问题。

## 5. 科研方法
- DeepJSCC-V：沿用 ADJSCC 的注意力特征块；用码掩码只保留前 R 比例的特征通道实现任意 CR；训练时随机 SNR、随机 CR。
- OraNet：输入语义码的通道均值 / 标准差特征 + SNR + CR，输出预测 PSNR（残差全连接块）。
- CR 优化器：数据级查表；实例级对每张图逐级查询 OraNet，找满足 PSNR 门限的最小 CR。
- 观察：语义码前面的通道承载更多信息（类似 PCA），解释了"截断即降速率"为什么可行。

## 6. 仿真与实验
- CIFAR-10 训练、CIFAR-100 测试；ImageNet 训练、Kodak24 测试；AWGN 与慢 Rayleigh 衰落。
- 与 ADJSCC 同 CR 对比 PSNR、数据级最小 CR 对比、OraNet 预测误差、Kodak 上与 BPG + LDPC 对比、实例级 CR 优化示例。
- 坦白：Kodak 上 AWGN 下 PSNR 低于 BPG + LDPC，且 SNR 越高差距越大。

## 7. 图表
- 13 图 0 表 2 算法。Fig. 1 框架图（三个模块）；Fig. 6 语义码通道统计与 PSNR 的关系（解释可预测性）。

## 8. 句式库
- 空白："However, existing DeepJSCC-based semantic communication frameworks still cannot achieve adaptive code rates for different channel SNRs and image contents, which reduces its flexibility and bandwidth efficiency."
- 用数字说明部署代价："… we need to prepare 5×8=40 DeepJSCC models, which greatly increases the training and deployment cost of DeepJSCC models."
- 对比传统链路自适应："However, in semantic communication, adaptive rate control still cannot be well addressed even if we have DeepJSCC models with flexible rate adjustment abilities, …"
- 新问题声明："It is necessary to emphasize that, instance-level CR optimization is a new problem and has not been considered before."
- 坦白不足（结论）："… it still cannot achieve superior performance compared with conventional BPG+LDPC-based transmission schemes in all SNR regime, …"

## 9. 结论
- 1 段 265 词，复述三模块 → 结果（含 0.5 dB）→ 承认不如 BPG + LDPC → 未来工作：改进网络结构与训练算法。

## 10. Idea 拆解
- **基线**：ADJSCC（SNR 自适应）、DeepJSCC-A（速率自适应）。
- **增量**：可变码长的 DeepJSCC-V + 质量预测网络 OraNet + 基于预测的 CR 优化（adaptivity + new-component）。
- **为什么有效**：语义码各通道的重要性有序（前面的通道信息量大），截断即可降速率；重建质量可由语义码统计量、SNR、CR 预测。
- **证据**：OraNet 预测误差平均小于 0.5 dB；同目标 PSNR 下数据级 CR 明显低于 ADJSCC。
- **弱点**：Kodak 上不如 BPG + LDPC；只用 PSNR；OraNet 在极低 SNR 下预测误差大；CR 只能在离散集合中选；没有复杂度与时延分析。
- **开放问题**：
  - "… thus our future work is improving the network architecture and training algorithm of the DeepJSCC-V model to further improve its coding capability."
  - 推断：用感知指标（LPIPS 等）做质量预测与约束；把"质量预测 + 资源分配"推广到多用户 / 多任务的无线资源分配（后续大量 system-level 论文的基础）；在线更新预测器以适应新数据分布。
