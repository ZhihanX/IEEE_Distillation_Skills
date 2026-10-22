---
doi: 10.1109/tcomm.2024.3386577
title: "Joint Coding-Modulation for Digital Semantic Communications via Variational Autoencoder"
journal: TCOM
year: 2024
band: 2022-2025
cites: 146
cites_per_year: 69.8
article_type: research
topic: semantic
source: xplore-html
xplore: 10495330
auto:
  words_total: 7560
  n_sections: 5
  n_subsections: 13
  n_figures: 9
  n_tables: 3
  n_display_eq: 29
  n_algorithms: 0
  statements: {theorem: 1, lemma: 1, proposition: 2, corollary: 1, proof: 1, proof_in_appendix: 1}
  n_appendix: 4
  mean_sentence_words: 24.2
  we_per_1k: 15.5
  title_words: 9
  abstract_words: 193
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 1, roadmap: 1, however: 6, transition: 8, resultsShow: 1, motivatedBy: 0, toAddress: 2, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 9, intensifier: 2, worthNoting: 0, observe: 8, thisIsBecause: 0, asExpected: 0, insight: 1, tradeoff: 2, figVerb: 1, promising: 1, gen: 1, contrast: 3, firstTime: 0, novel: 1, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  # contribList 1 为误匹配（"can be summarized as follows" 出现在 Gumbel-Max 说明中），本文无贡献列表
  methods: {monteCarlo: 5, complexity: 4, convergence: 3, DNN: 3}
  domain: {QAM: 25, accuracy: 10, VAE: 9, quantization: 9, PSNR: 8, DeepJSCC: 7, CIFAR: 4, AWGN: 3, SNRmismatch: 2}
code:
  title_pattern: [X-for-Y, X-via-Y]
  abstract_moves: [context, gap, aim, method, method, theory, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 9
  intro_moves: [field, prior, gap, gap, approach, approach, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 3
  contrib_verbs: [outperform, result, attain]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [practicality, limitation]
  motivating_figure: true
  problem_class: learning
  solution: [DNN, bound-surrogate]   # 以互信息的变分下界作为损失
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true          # Table III FLOPs、参数量、训练时间
  convergence_analysis: false
  sim_param_table: true              # Table I 网络结构，Table II 超参数
  baselines_n: 4                     # Analog、DeepJSCC-Q、Uniform 量化、NN 量化
  baseline_naming: acronym
  x_axes: [SNR, transmission-rate, modulation-order, constellation-map, epochs]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 3
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: digital
  source: [image]
  task: [reconstruction, classification]
  paradigm: digital-jscc
  architecture: [VAE, CNN, MLP]
  channel: [AWGN]
  adaptivity: [modulation]        # 学到的星座概率分布随 SNR 改变（概率整形）
  training: [end-to-end]
  metrics: [PSNR, accuracy]
  datasets: [CIFAR-10, Tiny-ImageNet]
  baselines: [other-learned]
  snr_mismatch_test: false
  complexity_reported: true
  digital_compatible: true
  hardware_validation: false
  theory: information-theoretic   # Info-Max 目标的变分推断下界（Theorem 1）
  idea_delta: [digitalization, theory]
  builds_on: [DeepJSCC-Q, VAE, Gumbel-Softmax]
  open_problems_n: 2
---

## 1. 标题
- "[方法] for [范式] via [工具]"，9 词。

## 2. 摘要（8 句，193 词）
- 语义通信定义 → 空白："Most existing approaches typically utilize neural networks (NNs) to design end-to-end semantic communication systems, where NN-based semantic encoders output continuously distributed signals to be sent directly to the …" → "In this work, we propose a joint coding-modulation (JCM) framework …" → 两句机理（学"到星座符号的转移概率"避开不可微；联合设计让调制与信道匹配）→ 理论（有信息论意义的损失）→ 两句结果（优于量化类数字方法；与模拟方案的差距随调制阶数增加而缩小）。

## 3. 引言逻辑（9 段）
- 语义通信 → 各模态与网络结构 → "However, using NN-based semantic encoders also makes it difficult to deploy semantic communication systems on modern digital communication devices." → 模拟传输难以实现（功放非理想、协议兼容）→ 数字调制不可微 → 已有三种做法（均匀量化、MLP 量化 + BPSK、DeepJSCC-Q 的硬-软量化器）各自的缺陷 → 两个问题：不可微、与信道状态不匹配 → 本文两条设计方法 → 变分学习与 Info-Max 损失 → 三个实验发现（散文贡献）→ 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：实用性（模拟语义通信难以部署在数字设备上）+ 已有方法局限（量化与信道条件分离、硬判决丢信息）。
- 核心洞见：不让网络直接"输出星座点"，而是输出"每个符号取各星座点的概率"，再按概率采样（Gumbel-Softmax 重参数化）——把不可微问题变成概率建模问题；联合训练后网络自动学到随 SNR 变化的概率整形（低 SNR 时近似高斯）。
- 实验中的意外发现（高阶调制更好、自动学到概率整形）被写进贡献，增加了"机理洞见"的分量。

## 5. 科研方法
- 概率编码-调制器（ResNet + MLP 输出 2√M × n 个类别概率）→ 星座符号生成器（Gumbel-Max 采样，反向用 Softmax 近似）→ AWGN → 两个解码器（重建 + 语义 / 分类）。
- 目标：Info-Max（互信息）→ Theorem 1 给出变分推断下界（VILB）作为损失 → Proposition 1/2 给出 BPSK 与矩形 M-QAM 的转移概率模型 → Corollary 1 图像任务下的具体损失（MSE + 交叉熵加权）。

## 6. 仿真与实验
- CIFAR-10（分类标签作为语义信息），Tiny ImageNet 补充；基准：模拟传输、DeepJSCC-Q、均匀量化、NN 量化。
- PSNR / 分类精度 vs SNR（BPSK、4QAM、16QAM）、vs 传输速率、vs 调制阶数；星座点经验分布可视化（Fig. 7–8）；复杂度与收敛（Table III、Fig. 9）。
- 坦白：所有方法分类精度几乎相同，差异主要体现在重建 PSNR；高 SNR 下才明显优于基准（如 BPSK、18 dB 时比 DeepJSCC-Q 高 0.4 dB）。

## 7. 图表
- 9 图 3 表。Fig. 1 系统模型；Fig. 7–8 用"点的大小 ∝ 出现概率"可视化学到的概率整形，是解释机制的关键图。

## 8. 句式库
- 部署障碍："However, using NN-based semantic encoders also makes it difficult to deploy semantic communication systems on modern digital communication devices."
- 模拟传输难实现："Such analog transmission approach, however, is difficult to implement in practice, due to the non-ideal characteristics of hardware components including power amplifier."
- 不可微："Specifically, the process of digital modulation requires a mapping from the continuous real-world source data to discrete constellation symbols, which is equivalent to a non-differentiable function [27]."
- 总结两个问题："Overall, the problems of the non-differentiability of the digital modulation process and the mismatch between digital modulation and channel states still remain to be solved in realizing digital …"
- 实用建议式结论："Therefore, the JCM framework provides a convenient way of conducting digital modulation, namely by using the highest modulation order that the transmission device can support."

## 9. 结论
- 3 段：方法与理论 → 实验发现与使用建议 → 未来工作（星座几何整形）。无数字。

## 10. Idea 拆解
- **基线**：DeepJSCC-Q（jsait.2022.3231042，硬-软量化器）与均匀 / NN 量化的数字语义通信。
- **增量**：用 VAE 学"到星座符号的转移概率"实现可微的数字调制，并用互信息变分下界作为损失（digitalization + theory）。
- **为什么有效**："Our approach learns the transition probability from source data to discrete constellation symbols, thereby avoiding the non-differentiability problem of digital modulation."
- **证据**：各 SNR、速率、调制阶数下 PSNR 优于量化类数字方法；与模拟方案的差距随调制阶数增大而缩小；学到近似高斯的概率整形。
- **弱点**：只有 AWGN；小图（32×32、64×64）；分类精度与基准无差别；无硬件验证；采样带来的随机性对时延 / 可靠性的影响未讨论。
- **开放问题**：
  - "Looking ahead, our future efforts will focus on the design and optimization of constellation geometry shaping to enhance the system's performance."
  - 推断：衰落 / MIMO / OFDM 下的 JCM；高分辨率图像；与信道编码（纠错码）的联合；调制阶数随信道自适应（后续 tccn.2024.3422496 的方向）。
