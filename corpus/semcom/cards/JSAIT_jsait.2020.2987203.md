---
doi: 10.1109/jsait.2020.2987203
title: "DeepJSCC-f: Deep Joint Source-Channel Coding of Images With Feedback"
journal: JSAIT
year: 2020
band: 2019-2021
cites: 485
cites_per_year: 75.5
article_type: research
topic: semantic
source: xplore-html
xplore: 9066966
auto:
  words_total: 8531
  n_sections: 5
  n_subsections: 11
  n_figures: 18
  n_tables: 0
  n_display_eq: 5
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, remark: 2, proof: 0, proof_in_appendix: 0}
  n_appendix: 2
  mean_sentence_words: 28.9
  we_per_1k: 15.9
  title_words: 9
  abstract_words: 207
  abstract_sentences: 6
  phrases: {toTheBest: 4, inThisPaper: 6, contribList: 0, roadmap: 0, however: 7, transition: 1, resultsShow: 0, motivatedBy: 4, toAddress: 0, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 13, intensifier: 7, worthNoting: 0, observe: 9, thisIsBecause: 0, asExpected: 1, insight: 0, tradeoff: 2, figVerb: 0, promising: 2, gen: 0, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 0, code: 5, prototype: 0}
  # code: 5 为误报（"source codes"、"channel codes"）
  methods: {DNN: 5, complexity: 5, DRL: 1, convergence: 1}
  domain: {feedback: 83, DeepJSCC: 44, PSNR: 19, BPG: 16, AWGN: 12, CNN: 12, CBR: 11, LDPC: 9, capacityBound: 8, CIFAR: 6, JPEG2000: 6, JPEG: 5, QAM: 4, Kodak: 3, MSSSIM: 3, SSIM: 3, SNRmismatch: 3, Rayleigh: 2}
code:
  title_pattern: [colon-subtitle, X-with-Y]
  abstract_moves: [aim, context, gap, aim, method, implication]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 11
  intro_moves: [field, field, gap, prior, prior, prior, prior, aim, solution, approach, contrib]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 5
  contrib_verbs: [present, show, outperform, enable, show]
  contrib_quantified: false
  first_claim: true          # "To the best of our knowledge, this is the first practical JSCC scheme that can fully exploit channel output feedback, …"
  roadmap: false
  notation: none
  gap_type: [theory-gap, new-scenario]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4             # DeepJSCC（无反馈）、JPEG/JPEG2000/BPG + LDPC、BPG + 容量界、Deepcode（试过但无法用于长码）
  baseline_naming: descriptive
  x_axes: [SNR, number-of-layers, bandwidth-ratio, target-quality, feedback-SNR]
  fig1_role: system-model
  caption_style: self-contained-conclusion   # 多数结果图 caption 直接写出结论（如 "Initially, the addition of feedback rounds increases performance, but after a point, the gains stagnate."）
  prototype_or_measurement: false
  code_released: unclear     # 正文 "The model was implemented1 in Tensorflow" 带脚注 1，提取器不读脚注，未核实是否为代码链接
  conclusion_paragraphs: 4
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: image-jscc
  source: [image]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [CNN]
  channel: [AWGN, Rayleigh, feedback]
  adaptivity: [bandwidth-rate]   # 可变长传输：达到目标质量即停
  training: [multi-stage]        # 逐层训练
  metrics: [PSNR, SSIM, MS-SSIM]
  datasets: [CIFAR-10, ImageNet, Kodak]
  baselines: [DeepJSCC, separate]
  snr_mismatch_test: true        # 前向与反馈两条信道都测了失配
  complexity_reported: false
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [feedback-retransmission, new-channel]
  builds_on: [DeepJSCC, Schalkwijk-Kailath scheme]
  open_problems_n: 4
---

## 1. 标题
- "[方法名]: [方法全称] of [信源] With [新条件]"，9 词。方法名 = 基线名 + 后缀（DeepJSCC-f），一眼看出是哪个工作的扩展。

## 2. 摘要（6 句，207 词）
- 先给信息论背景："From a Shannon theoretic perspective feedback does not improve the asymptotic end-to-end performance, …" → 空白："… there are no known practical joint source-channel coding (JSCC) schemes that can exploit the feedback signal and surpass the performance of separation-based schemes." → 本文 → 首创 + 意义。

## 3. 引言逻辑（11 段，约 2000 词）
- 分离定理的地位与失效条件 → 反馈不增容量但能改善误差指数、简化 JSCC → "However, there has been limited success in converting these theoretical gains of feedback into practical coding schemes."
- DNN 信道译码 → 自编码器 → Deepcode（RNN 反馈码）的局限（短码长、码率 1/r）→ 学习型压缩 → DeepJSCC 与可逐级细化性质。
- 本文问题为何难（编码器还要学会利用反馈中的接收端信念）→ 灵感来自 Schalkwijk-Kailath 方案 → Fig. 2 在引言就给出主要结果图 → 散文式总结贡献。

## 4. Idea 是怎么提出的
- 空白类型：理论缺口转实用（反馈的理论收益一直没有实用编码方案）+ 新信道设定（有输出反馈的图像传输）。
- 核心洞见：把 Schalkwijk-Kailath "根据接收端当前估计发送纠错信息" 的思路推广到非线性、按块分层的 CNN 自编码器，每层根据接收端的重建结果继续细化。
- 一个设计带来两种用法：固定长度（提高质量）和可变长度（达到目标质量即停，降低平均时延）。

## 5. 科研方法
- L 层自编码器，每层 = 编码器 + 解码器 + 合并器；编码器输入原图和接收端上一层的重建（经反馈获知）；逐层训练，MSE 损失。
- 研究层数 L 的影响（存在最优 L）、可变速率、慢衰落、带噪反馈与反馈信道失配。

## 6. 仿真与实验
- CIFAR-10 为主，ImageNet 训练 + Kodak 测试验证泛化；基准为 DeepJSCC（无反馈）、JPEG/JPEG2000/BPG + LDPC、BPG + 容量界；附录 A 详述分离方案的实现。
- 坦白："We should remark that, to the best of our knowledge, DeepJSCC-f is the first practical JSCC implementation in the literature able to transmit images exploiting channel output feedback …"
- 带噪反馈严重时表现不如单层，作者提出混合方案但留作未来工作。

## 7. 图表
- 18 图 0 表（含附录 2 张视觉对比）。Fig. 1 反馈系统模型、Fig. 2 在引言给出核心对比结果、Fig. 3–4 架构；结果图 caption 多直接写结论。

## 8. 句式库
- 理论到实用的空白："However, there has been limited success in converting these theoretical gains of feedback into practical coding schemes."
- 难度说明："Note that this is a significantly challenging problem as the neural encoder not only needs to learn how to map the image into the channel input space, …"
- 没有直接对手的说明："… so there are no direct competitor to the results presented here."
- 首创："To the best of our knowledge, this is the first practical JSCC scheme that can fully exploit channel output feedback, …"
- 自我定位："This work is just a first step towards JSCC strategies using deep neural networks."

## 9. 结论
- 4 段：首创 + 三类对比 → 多步传输与可变速率 → 模拟特性与适应性 → 未来工作（更好的结构与训练、音频与视频）。无数字。

## 10. Idea 拆解
- **基线**：DeepJSCC（tccn.2019.2919300）与其可逐级细化版本；思想来源为 Schalkwijk-Kailath 反馈方案。
- **增量**：给 DeepJSCC 加上信道输出反馈，分 L 层传输，每层根据接收端当前重建继续发送细化信息（feedback-retransmission + new-channel）。
- **为什么有效**：发送端通过反馈知道接收端的估计，可以把信道资源用在误差最大的地方；"… the transmission over each layer depends on the original image as well as the receiver's reconstruction up to that point."
- **证据**：CIFAR-10、k/n = 1/3、4 层时低 SNR 下比"BPG + 容量界"高至多约 3 dB PSNR；可变长传输下达到同样目标 PSNR 所需平均带宽明显更低。
- **弱点**：反馈很噪时不如不用反馈；假设前向与反馈信道独立、单位时延；只在小图上做了大部分实验；没有复杂度与时延的定量报告。
- **开放问题**：
  - "We will explore adaptive power allocation strategies through reinforcement learning as a future extension of this work, …"
  - "An implementation of such hybrid solution is left for future work."（根据反馈噪声决定是否利用反馈）
  - "… the general design principles presented in this work can be potentially applied to other information sources, such as audio or video."
  - 推断：反馈与 ARQ/HARQ 的结合（后续出现 HARQ 类语义传输）；用 Transformer 处理反馈（后续 twc.2024.3386052）；多用户下的反馈利用。
