---
doi: 10.1109/twc.2024.3379244
title: "CDDM: Channel Denoising Diffusion Models for Wireless Semantic Communications"
journal: TWC
year: 2024
band: 2022-2025
cites: 176
cites_per_year: 84.1
article_type: research
topic: semantic
source: xplore-html
xplore: 10480348
auto:
  words_total: 7477
  n_sections: 6
  n_subsections: 16
  n_figures: 20
  n_tables: 1
  n_display_eq: 44
  n_algorithms: 3
  statements: {theorem: 1, lemma: 0, proposition: 2, corollary: 0, assumption: 2, proof: 2, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 22.0
  we_per_1k: 8.9
  title_words: 9
  abstract_words: 224
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 6, contribList: 1, roadmap: 1, however: 10, transition: 14, resultsShow: 4, motivatedBy: 3, toAddress: 1, gapWord: 2, nonconvex: 0, npHard: 0, closedForm: 1, outperform: 7, intensifier: 4, worthNoting: 4, observe: 9, thisIsBecause: 3, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 11, promising: 2, gen: 2, contrast: 5, firstTime: 0, novel: 2, weProposeFirst: 2, wlog: 0, code: 0, prototype: 1}
  # prototype 1 为误报（"experimental setup"）；gen 2 为误报（"generation step"）
  methods: {DNN: 6, complexity: 4, monteCarlo: 3, DRL: 1, randomMatrix: 1}
  domain: {PSNR: 21, AWGN: 18, Rayleigh: 18, diffusion: 16, CBR: 15, DIV2K: 15, LDPC: 11, CNN: 10, JPEG2000: 10, GAN: 9, CIFAR: 6, complexityCost: 6, transformer: 6, attention: 4, perception: 4, Swin: 3}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [context, gap, aim, method, method, theory, method, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 13
  intro_moves: [tech, tech, field, gap, prior, prior, prior, aim, field, prior, gap, contrib, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [design, derive, derive, apply]
  contrib_quantified: false
  first_claim: true                     # "To the best of our knowledge, there is no existing work on AI concentrating on removing noise in signal space."
  roadmap: true
  notation: none
  gap_type: [new-tool, limitation]
  motivating_figure: false              # Fig. 1 是扩散模型原理图
  problem_class: learning
  solution: [DNN, bound-surrogate]      # 变分下界损失
  theory_role: supporting               # Proposition 1/2 均衡后接收信号的条件分布；Theorem 1 条件熵下降的充分条件
  proofs_location: inline
  complexity_analysis: true             # Table I MACs
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4                        # JSCC、DnCNN + JSCC、GAN + JSCC、JPEG2000 + LDPC
  baseline_naming: descriptive
  x_axes: [SNR, CBR, sampling-steps, noise-schedule]
  fig1_role: background
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
  architecture: [diffusion, Swin, CNN]   # U-Net 去噪 + Swin JSCC
  channel: [AWGN, Rayleigh]
  adaptivity: [SNR]                      # 按 SNR 选起始采样步 t_max
  training: [multi-stage]                # 三阶段：JSCC → 冻结编码器训 CDDM → 重训解码器
  metrics: [PSNR, MS-SSIM]
  datasets: [CIFAR-10, DIV2K]
  baselines: [other-learned, separate]
  snr_mismatch_test: true                # Fig. 17 训练于 20 dB、跨 SNR 测试；另有信道估计误差
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: other                          # 条件熵下降的充分条件
  idea_delta: [generative-prior, new-component]
  builds_on: [DDPM, SwinJSCC / WITT, DnCNN]
  open_problems_n: 0
---

## 1. 标题
- "[方法名]: [方法全称] for Wireless Semantic Communications"，9 词。方法名就是"信道去噪扩散模型"的首字母。

## 2. 摘要（8 句，224 词）
- 扩散模型背景 → 用一个问题引出 idea："The property of DM for eliminating noise leads us to wonder whether DM can be applied to wireless communications to help the receiver mitigate the channel noise." → 本文 → 模块位置（均衡之后的新物理层模块）→ 训练 / 采样算法 → 理论（条件熵下降）→ 与 JSCC 结合的三阶段训练 → 结果一句（MSE 低于 MMSE 均衡后；优于 JSCC 与 JPEG2000 + LDPC）。

## 3. 引言逻辑（13 段）
- 扩散模型（2 段，含公式 (1)）→ AWGN 信道公式 (2) → 类比："Interestingly, by comparing (1) and (2), we can find that the designed process of DM and the wireless communications system are similar."
- 图像去噪类工作只在像素空间 → 首创性声明（信号空间去噪）→ 通信里的扩散模型多用于决策 → 语义通信里的扩散模型都当条件生成解码器："… without considering diffusion models as a module for denoising and purifying the received signal."
- 本文 CDDM（从接收信号而非纯噪声开始反向采样，步数少）→ 语义通信与 deep JSCC 文献 → 空白：只靠更大模型、信道失真靠端到端优化"硬扛" → 本文结合 → 4 条贡献 → 路线图。

## 4. Idea 是怎么提出的
- 空白类型：新工具迁移（AIGC 的扩散模型 → 物理层去噪）+ 已有方法局限（扩散模型在语义通信中只作生成式解码器；JSCC 只靠端到端学习对抗信道）。
- 核心洞见：扩散前向过程"逐步加高斯噪声"与信道"信号 + 噪声"同构；只要把前向过程设计成与"均衡后接收信号"的条件分布一致（Proposition 1/2），就可以把接收信号直接当作某个中间步 x_m，从这一步开始反向采样去噪——既去噪又省采样步。
- 用公式对照（(1) vs (2)）写出类比，是"跨领域迁移"型 idea 的典型写法。

## 5. 科研方法
- 系统：Swin JSCC 编码器 → Rayleigh / AWGN → MMSE 均衡 → 归一化重排 → CDDM（U-Net）→ JSCC 解码器。
- 理论：Proposition 1/2 推导均衡后信号的条件分布（含 W_s、W_n 两个对角权重）→ 匹配的前向过程与 KL 推导 → 变分下界损失（可重加权）→ 按 SNR 选起始步 m → Theorem 1：两个假设下条件熵下降的充分条件；Monte Carlo 验证假设与"最大采样步"。
- 三阶段训练：训练 JSCC → 冻结编码器训 CDDM → 联合 CDDM 重训解码器。

## 6. 仿真与实验
- CIFAR-10（32×32）与 DIV2K（高分辨率）；基准 JSCC、DnCNN + JSCC、GAN + JSCC、JPEG2000 + LDPC。
- 超参数影响（7 种噪声调度、t_max、重加权损失）→ MSE（含信道估计误差）→ 可视化（标注"额外带宽成本百分比"）→ PSNR vs SNR / CBR → 失配 SNR → MS-SSIM → MACs（Table I）。
- 每条曲线 caption 都写明 CBR 与 SNR 设置。

## 7. 图表
- 20 图 1 表 3 算法。Fig. 1 扩散原理；Fig. 2 系统架构；Fig. 3 CDDM 的前向 / 反向过程（与信道对应）；Fig. 4–5 用 Monte Carlo 验证理论假设——理论 + 实验验证假设的组合。

## 8. 句式库
- 用问题引出 idea："The property of DM for eliminating noise leads us to wonder whether DM can be applied to wireless communications to help the receiver mitigate the channel noise."
- 公式类比："Interestingly, by comparing (1) and (2), we can find that the designed process of DM and the wireless communications system are similar."
- 首创性："To the best of our knowledge, there is no existing work on AI concentrating on removing noise in signal space."
- 区分已有用法："However, these works employ conditional diffusion models as a decoder to generate the desired images conditioned on the received signal, without considering diffusion models as a module for …"
- 批评"堆模型"："Despite its great potential, previous studies predominantly concentrate on the development of a more sophisticated model architecture with increased capacity to enhance overall performance."

## 9. 结论
- 1 段 128 词，现在完成时复述；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：Swin 版 deep JSCC（tccn.2024.3424842 一系）；以扩散模型做条件生成解码器的语义通信（如 jsac.2023.3288243 同期工作）；DnCNN / GAN 去噪。
- **增量**：把扩散模型做成均衡之后的"信道去噪"物理层模块，前向过程按信道与均衡器的条件分布设计，并从接收信号对应的中间步开始采样（generative-prior + new-component）。
- **为什么有效**：前向过程与真实信道 + 均衡后的分布一致（KL 推导），所以学到的反向过程正好去掉信道噪声；Theorem 1 说明在较少采样步内条件熵下降。
- **证据**：MSE 低于 MMSE 均衡后；PSNR / MS-SSIM 在 AWGN、Rayleigh、信道估计误差下都优于 JSCC 与 DnCNN / GAN 去噪；可视化中基准需额外带宽才能达到同样质量。
- **弱点**：采样带来的时延与复杂度（虽给了 MACs，但无墙钟时延）；理论假设（网络输出零均值、损失有界）偏强；不同 SNR 需重训（文中"all systems undergo retraining"）；只做重建、只做模拟传输；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：少步 / 一步采样（一致性模型、蒸馏）降低时延；MIMO / OFDM 与频率选择性信道下的条件分布推导；数字调制下的扩散去噪；与信道估计联合（不依赖完美 CSI）；对任务型语义特征的去噪。
  - 原文局限："It is worth emphasizing that in the event of a change in channel SNR, all systems undergo retraining to optimize their performance under the specific SNR condition."
