---
doi: 10.1109/tccn.2024.3422496
title: "Joint Source-Channel Coding for Channel-Adaptive Digital Semantic Communications"
journal: TCCN
year: 2025
band: 2022-2025
cites: 83
cites_per_year: 49.6
article_type: research
topic: semantic
source: xplore-html
xplore: 10584091
auto:
  words_total: 7728
  n_sections: 7
  n_subsections: 10
  n_figures: 8
  n_tables: 2
  n_display_eq: 35
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, remark: 2, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.2
  we_per_1k: 8.6
  title_words: 8
  abstract_words: 199
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 3, contribList: 1, roadmap: 0, however: 3, transition: 4, resultsShow: 0, motivatedBy: 5, toAddress: 7, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 9, intensifier: 3, worthNoting: 0, observe: 0, thisIsBecause: 1, asExpected: 0, insight: 1, tradeoff: 3, figVerb: 11, promising: 1, gen: 0, contrast: 3, firstTime: 0, novel: 4, weProposeFirst: 1, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 11, DNN: 4}
  domain: {QAM: 25, CIFAR: 14, complexityCost: 14, accuracy: 12, MNIST: 10, DeepJSCC: 7, JPEG: 5, LDPC: 5, quantization: 5, attention: 4, AWGN: 3, PSNR: 2, IB: 1, OFDM: 1, Rayleigh: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, gap, method, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, prior, prior, prior, aim, contrib]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [develop, present, devise, demonstrate]
  contrib_quantified: false
  first_claim: true                     # "To the best of the authors' knowledge, no previous studies have explored …"
  roadmap: false
  notation: none
  gap_type: [practicality, limitation]
  motivating_figure: true
  problem_class: learning
  solution: [DNN, bound-surrogate, exhaustive-search]   # 变分下界做损失；推理阶段按 BER 约束选调制阶数
  theory_role: supporting               # QAM 比特错误 / 正确判决概率随 SNR 与阶数的刻画
  proofs_location: none
  complexity_analysis: true             # 低复杂度判决边界；训练时间 / 参数量相同的说明
  convergence_analysis: false
  sim_param_table: true                 # Table I 网络结构
  baselines_n: 5                        # NECST(Ideal)、NECST(Sample Mixing)、DeepJSCC、DeepJSCC-Q、JPEG + 1/2 LDPC
  baseline_naming: acronym
  x_axes: [SNR]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: digital
  source: [image]
  task: [classification, reconstruction, retrieval]
  paradigm: digital-jscc
  architecture: [CNN]
  channel: [AWGN, Rayleigh]            # 准静态块衰落 + 均衡
  adaptivity: [SNR, modulation]
  training: [end-to-end, robust-sampling]   # BSEC 参数从多种分布采样；warm-up
  metrics: [accuracy, PSNR, custom]     # mAP、BER、频谱效率
  datasets: [MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100]
  baselines: [DeepJSCC, other-learned, separate]
  snr_mismatch_test: true               # 单一编解码器覆盖全 SNR 与多种调制阶数
  complexity_reported: true
  digital_compatible: true
  hardware_validation: false
  theory: none
  idea_delta: [digitalization, adaptivity, robustness]
  builds_on: [NECST, DeepJSCC-Q, adaptive modulation and coding (AMC)]
  open_problems_n: 3
---

## 1. 标题
- "[方法] for [限定词] [范式]"，8 词。"Channel-Adaptive Digital" 两个限定词合起来就是本文的空白。

## 2. 摘要（8 句，199 词）
- 首句直接给本文（"In this paper, we propose a novel joint source-channel coding (JSCC) approach for channel-adaptive digital semantic communications."）→ 挑战（信道动态 + 多种调制阶数）→ 三个组件各一到两句（鲁棒解调、鲁棒训练与 BSEC 建模、信道自适应调制）→ 结果一句（分类、重建、检索三任务）。

## 3. 引言逻辑（5 段 + 4 条贡献）
- 语义通信 vs 传统通信 → JSCC 的多模态文献 → "Unfortunately, these studies rely on the end-to-end training of the JSCC encoder and decoder for specific training environments."
- 信道自适应 JSCC（注意力 / SNR 模块）→ "However, this approach escalates both the network size and training complexity." → 这些方法是模拟的，不兼容数字系统。
- 数字 JSCC（量化、BPSK、QAM 映射）→ "The common limitation of these techniques is the use of a fixed modulation scheme during the training of the JSCC encoder and decoder." → 首创性声明。
- 本文三组件 → 贡献 bullet。无路线图、无记号段。

## 4. Idea 是怎么提出的
- 空白类型：实用性（模拟方案不兼容数字系统）+ 已有方法局限（数字 JSCC 训练时固定调制阶数，换阶数就失配）。
- 核心洞见：不在训练里显式建模"调制 + 衰落 + 均衡 + 解调"，而把它们的合效应抽象成比特级的二元对称删除信道（BSEC），再从分布中随机采样其参数——训练覆盖一个"比特错误率区间"，推理时只要选出 BER 落在该区间内的最高调制阶数即可（训练 / 测试环境在比特层面对齐）。
- 第二个洞见：在硬判决与软判决之间加一个"不确定就输出 0.5"的三值解调，兼顾鲁棒性与可控的统计建模。

## 5. 科研方法
- 系统：CNN 编码器输出比特序列 → QAM 调制 → 准静态衰落 → 均衡 → 鲁棒解调（LLR 幅度低于阈值输出 0.5）→ 解码器 + 任务头。
- 低复杂度：为 2^M-QAM 推导缩放后的上下判决边界，避免对全部星座点算距离（Fig. 2）。
- 训练：BSEC 建模 → 比特翻转概率从 Uniform[0, α_i] 等多种分布采样 → 互信息变分下界损失（沿用 NECST）→ warm-up 期改善初始训练。
- 推理：刻画 QAM 的比特错误 / 正确判决概率随 SNR 与阶数的关系 → 为每个潜变量选最高可用阶数（Remark 2 与 AMC 对比）。

## 6. 仿真与实验
- MNIST、Fashion-MNIST、CIFAR-10、CIFAR-100；基准 NECST 两种训练、DeepJSCC、DeepJSCC-Q、JPEG + 1/2 LDPC。
- 固定 4-QAM 下的分类精度 / BER / PSNR / mAP（Fig. 4–6）→ 信道自适应调制下的精度与频谱效率（Fig. 7–8、Table II）。
- 核心结论：自适应调制的平均精度与 4-QAM 几乎相同，平均频谱效率接近 16-QAM；单一编解码器优于需要多对编解码器的 NECST(Ideal)。

## 7. 图表
- 8 图 2 表 0 算法。Fig. 2 判决边界示意（16-QAM 第二比特）；Fig. 3 展示调制阶数随 SNR 的分配——用来"提供洞见"的机制图。

## 8. 句式库
- 训练环境依赖："Unfortunately, these studies rely on the end-to-end training of the JSCC encoder and decoder for specific training environments."
- 模块化自适应的代价："However, this approach escalates both the network size and training complexity."
- 数字 JSCC 的共同局限："The common limitation of these techniques is the use of a fixed modulation scheme during the training of the JSCC encoder and decoder."
- 定义语义通信（对比式）："In contrast, in semantic communication, the goal of the transmitter is to convey the meaning of the message, aiming to maximize the performance of a desired task at the receiver."
- 解释权衡："This is because the bit-error probability decreases as the modulation order decreases, leading to the fundamental trade-off between the classification accuracy and spectral efficiency."

## 9. 结论
- 2 段：现在完成时复述三组件 → 三条未来方向（调制 / 量化 / 损失的进一步设计；软输出解调；多任务多用户）。无数字。

## 10. Idea 拆解
- **基线**：NECST（BSC 上的神经 JSCC，固定比特翻转概率）；DeepJSCC-Q（jsait.2022.3231042，固定星座）；模拟信道自适应 JSCC（twc.2021.3090048 等）。
- **增量**：BSEC 抽象 + 参数随机采样的鲁棒训练，配合三值解调与推理期按 SNR 选调制阶数，使一个数字 JSCC 模型适配多种 SNR 与调制阶数（digitalization + adaptivity + robustness）。
- **为什么有效**：训练时覆盖了一个比特翻转概率区间；推理时选择的调制阶数保证实际 BER 落在该区间内，因此训练 / 测试在比特层面不失配。
- **证据**：Table II 中自适应调制的平均精度与 4-QAM 几乎相同、频谱效率接近 16-QAM；在全 SNR 范围优于 NECST(Ideal)。
- **弱点**：小图（28×28、32×32）与简单数据集；无信道编码（比特错误直接进入语义）；BSEC 假设比特间独立，忽略同一 QAM 符号内比特的相关性；重建任务 PSNR 较低；无硬件验证。
- **开放问题**：
  - "An important direction of future research is to further optimize the performance of the proposed approach through the development of advanced designs for modulation schemes, quantization methods, and loss functions."
  - "Another promising research direction is to extend the proposed JSCC approach to accommodate soft-output demodulation for JSCC-based semantic communications."
  - "Investigating an extension of the proposed approach to support multi-task multi-user semantic communications, where multiple devices engage in different tasks concurrently, would also be an important direction for future research."
  - 推断：与信道编码 / HARQ 的结合；高分辨率图像与重建任务；符号内比特相关性的建模（非独立 BSEC）。
