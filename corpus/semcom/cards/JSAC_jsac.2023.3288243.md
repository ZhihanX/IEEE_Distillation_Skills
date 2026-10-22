---
doi: 10.1109/jsac.2023.3288243
title: "Generative Joint Source-Channel Coding for Semantic Image Transmission"
journal: JSAC
year: 2023
band: 2022-2025
cites: 209
cites_per_year: 65.8
article_type: research
topic: semantic
source: xplore-html
xplore: 10158995
auto:
  words_total: 6579
  n_sections: 6
  n_subsections: 6
  n_figures: 9
  n_tables: 0
  n_display_eq: 16
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 25.7
  we_per_1k: 10.3
  title_words: 8
  abstract_words: 229
  abstract_sentences: 9
  phrases: {toTheBest: 1, inThisPaper: 4, contribList: 1, roadmap: 0, however: 10, transition: 7, resultsShow: 1, motivatedBy: 4, toAddress: 0, gapWord: 2, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 8, intensifier: 10, worthNoting: 1, observe: 2, thisIsBecause: 0, asExpected: 1, insight: 0, tradeoff: 2, figVerb: 5, promising: 1, gen: 2, contrast: 2, firstTime: 1, novel: 5, weProposeFirst: 5, wlog: 0, code: 0, prototype: 0}
  # toTheBest 实际 3 处（贡献 bullet 内 2 处未计入句子统计）
  methods: {compressedSensing: 4, DNN: 2}
  domain: {perception: 52, DeepJSCC: 49, LPIPS: 19, GAN: 16, CelebA: 9, ImageNet: 7, AWGN: 5, attention: 5, MSSSIM: 4, PSNR: 4, complexityCost: 4, SSIM: 3, VAE: 3, ratedist: 2, SNRmismatch: 2, OFDM: 2}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, gap, gap, aim, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, gap, approach, scenario, approach, contrib]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [study, propose, propose, show]
  contrib_quantified: false
  first_claim: true                     # "this is the first work to study distortion-perception trade-off in the context of JSCC"
  roadmap: false
  notation: none
  gap_type: [limitation, new-metric]
  motivating_figure: false
  problem_class: learning
  solution: [DNN, gradient]             # InverseJSCC：在 StyleGAN 潜空间做测试时优化（ILO）
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 1                        # DeepJSCC（含训练集失配版本）
  baseline_naming: acronym
  x_axes: [SNR]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: generative
  source: [image]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [GAN, CNN, attention]   # 预训练 StyleGAN-2 生成器
  channel: [AWGN]
  adaptivity: [none]
  training: [pretrained-generator, end-to-end, test-time-optimization]
  metrics: [LPIPS, MS-SSIM, PSNR]
  datasets: [CelebA-HQ, ImageNet, FFHQ]
  baselines: [DeepJSCC]
  snr_mismatch_test: false
  complexity_reported: false
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [generative-prior, new-metric]
  builds_on: [DeepJSCC, StyleGAN-2, intermediate layer optimization (ILO), rate-distortion-perception]
  open_problems_n: 0
---

## 1. 标题
- "Generative [方法类] for [语义] [模态] Transmission"，8 词。"Generative" 一词即全部增量。

## 2. 摘要（9 句，229 词）
- DeepJSCC 有前景 → 连续两个 "However" 句给空白（只关注失真不关注感知；极端低 BCR / 低 SNR 下尤甚）→ 本文两个方案 InverseJSCC / GenerativeJSCC → 二者区别一句 → 共同损失（MSE + LPIPS）→ InverseJSCC 机理 → 两句结果（"significantly" 各一次）。

## 3. 引言逻辑（6 段，含 A 小节贡献）
- 分离定理在极端时延 / 带宽下次优 → URLLC / 6G 时延需求 → DeepJSCC 成功但只用 MSE / SSIM → 语义通信中接收端未必要求最小失真 → 引入"率-失真-感知权衡" → 本文思路（StyleGAN + 与人眼对齐的指标）→ 场景一：编码器训练集通用、接收端知道目标数据集分布 → InverseJSCC → 场景二：端到端 GenerativeJSCC → 4 条贡献（2 条含"to the best of our knowledge"首创声明）。
- 无路线图；相关工作单列一节（DeepJSCC、深度生成模型、无监督逆问题）。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（失真指标 ≠ 感知质量）+ 新指标（把图像压缩领域的"感知损失 / 率-失真-感知权衡"引入 JSCC）。
- 核心洞见一（InverseJSCC）：把"DeepJSCC 编码 + 信道 + 解码"整体看作逆问题中的前向算子，在预训练 StyleGAN 的潜空间里搜索与接收重建一致的图像——编码器不变、无需配对数据。
- 核心洞见二（GenerativeJSCC）：把 StyleGAN-2 生成器直接作为解码器的一部分端到端训练，用 MSE + LPIPS 加权损失。
- 卖点放在"边缘情形"（BCR 低至 0.0013、SNR 低至 −5 dB），这是生成先验收益最大的区域。

## 5. 科研方法
- InverseJSCC：前向算子 A = 预训练 DeepJSCC（含 AWGN）；ILO 式优化潜向量 w 与噪声 n_G，目标是 A(G(w)) 与接收重建的 MSE + LPIPS；前向算子只部分已知（信道噪声随机）。
- GenerativeJSCC：编码器 → 不可训练信道 → 残差网络 + StyleGAN-2 生成器（映射潜向量 + 噪声输入）；两阶段训练。

## 6. 仿真与实验
- AWGN；StyleGAN-2 在 FFHQ 预训练；CelebA-HQ 与 ImageNet 子集；BCR ∈ {0.0013, 0.0052}，SNR ∈ [−5, 5] dB。
- InverseJSCC：LPIPS vs SNR，包括"训练集失配"（A 用 ImageNet 训练、测试 CelebA-HQ）→ 可视化。
- GenerativeJSCC：LPIPS / MS-SSIM / PSNR vs SNR；低 BCR 时连 PSNR 也优于 DeepJSCC。

## 7. 图表
- 9 图 0 表。Fig. 2–3 把"DeepJSCC 作为前向算子 + GAN 反演"的结构画出来；Fig. 7、9 人脸重建可视化（感知类论文的必备证据）。

## 8. 句式库
- 空白（失真 vs 感知）："However, these methods mostly focus on the distortion of the reconstructed signals with respect to the input image, rather than their perception by humans."
- 引入外领域概念："In image compression literature, this aspect has recently been acknowledged as the perception loss, resulting in the rate-distortion-perception trade-off [21]."
- 首创声明（工具迁移）："To the best of our knowledge, unsupervised inverse problems, which show exceptional denoising performance, have not been studied in the context of wireless communication."
- 指出边缘情形："However, this often results in a significant loss of perceptual quality for the edge cases."
- 对比式定位："In contrast, our work takes advantage of the outstanding generative performance of pre-trained SotA GANs as well as distortion metrics that align with human visual judgment in order …"

## 9. 结论
- 1 段 178 词：复述两方案与结果；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：DeepJSCC（tccn.2019.2919300 及其注意力 / 视频关键帧版本）。
- **增量**：用预训练生成模型（StyleGAN-2）作为接收端先验——测试时逆问题求解（InverseJSCC）或端到端生成式解码器（GenerativeJSCC），并以 MSE + LPIPS 作为目标（generative-prior + new-metric）。
- **为什么有效**：极低带宽 / 低 SNR 时接收信息不足以恢复细节，生成先验用数据分布"补全"细节，使重建落在自然图像流形上，感知质量提升；在窄领域（人脸）上甚至同时降低像素失真。
- **证据**：LPIPS 在边缘情形明显优于 DeepJSCC；InverseJSCC 在训练集失配时性能损失小；GenerativeJSCC 低 BCR 时 PSNR 也更好。
- **弱点**：只在人脸（窄分布）上验证，泛化到自然图像未知；InverseJSCC 的测试时优化计算量大，未报告时延 / 复杂度；只有 AWGN；基准只有 DeepJSCC（无 BPG + LDPC 等分离方案）；生成"幻觉"可能违背语义保真，未讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：通用图像上的生成式 JSCC（扩散模型替代 GAN，见 twc.2024.3379244 等）；生成幻觉的度量与控制（语义保真 vs 感知）；测试时优化的复杂度 / 时延；衰落信道与数字调制下的生成式 JSCC；JSCC 中率-失真-感知权衡的理论刻画。
