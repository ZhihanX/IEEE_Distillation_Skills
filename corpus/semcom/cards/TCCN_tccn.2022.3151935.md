---
doi: 10.1109/tccn.2022.3151935
title: "OFDM-Guided Deep Joint Source Channel Coding for Wireless Multipath Fading Channels"
journal: TCCN
year: 2022
band: 2022-2025
cites: 200
cites_per_year: 46.1
article_type: research
topic: semantic
source: xplore-html
xplore: 9714510
auto:
  words_total: 7323
  n_sections: 4
  n_subsections: 13
  n_figures: 17
  n_tables: 6
  n_display_eq: 13
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 2
  mean_sentence_words: 22.5
  we_per_1k: 18.7
  title_words: 11
  abstract_words: 178
  abstract_sentences: 8
  phrases: {toTheBest: 2, inThisPaper: 5, contribList: 1, roadmap: 0, however: 14, transition: 7, resultsShow: 0, motivatedBy: 2, toAddress: 0, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 17, intensifier: 7, worthNoting: 0, observe: 5, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 2, figVerb: 0, promising: 1, gen: 0, contrast: 5, firstTime: 0, novel: 1, weProposeFirst: 2, wlog: 1, code: 0, prototype: 0}
  methods: {DNN: 21, complexity: 5, convergence: 1}
  domain: {OFDM: 45, PSNR: 31, SSIM: 20, CIFAR: 16, feedback: 12, LDPC: 10, BPG: 9, CelebA: 9, DeepJSCC: 9, accuracy: 9, perception: 8, MSSSIM: 7, CNN: 6, AWGN: 5, QAM: 5, SNRmismatch: 5, Rayleigh: 3, Kodak: 2, complexityCost: 2}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, method, method, method, method, result, result, result]
  abstract_has_numbers: true    # "2.5 – 4 dB SNR gain"
  abstract_anchor: we-verb
  intro_paragraphs: 6
  intro_moves: [field, prior, solution, prior, aim, contrib]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [extend, design, evaluate, evaluate, evaluate]
  contrib_quantified: true
  first_claim: true             # "To the best of our knowledge, there is no existing JSCC work specifically designed and optimized for the multipath fading channels."
  roadmap: false
  notation: none
  gap_type: [new-scenario, limitation]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: true     # Table III 各子网复杂度
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3                # BPG + 802.11n LDPC + OFDM（完美 CSI / MMSE 估计）、无 OFDM 的直接 JSCC、注水功率分配
  baseline_naming: descriptive
  x_axes: [number-of-symbols, number-of-pilots, SNR, PAPR, path-number-mismatch]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: image-jscc
  source: [image]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [CNN, GAN]
  channel: [OFDM, feedback]
  adaptivity: [CSI]             # 有 CSI 反馈时用预编码网络做子载波功率分配
  training: [end-to-end]
  metrics: [PSNR, SSIM, MS-SSIM, accuracy]
  datasets: [CIFAR-10, CIFAR-100, CelebA, OpenImages, Kodak]
  baselines: [separate, own-ablation]
  snr_mismatch_test: true       # SNR 失配与多径数 L 失配
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [new-channel, new-component]   # 多径 + OFDM；把信道估计 / 均衡等领域知识模块嵌入网络
  builds_on: [DeepJSCC, model-based deep learning, end-to-end learned OFDM]
  open_problems_n: 4
---

## 1. 标题
- "[领域知识]-Guided [方法] for [信道]"，11 词。"OFDM-Guided" 点出"模型驱动 + 数据驱动"的卖点。

## 2. 摘要（8 句，178 词）
- 问题一句 → "Inspired by recent works on deep learning based JSCC and model-based learning methods, we combine an autoencoder with OFDM to cope with multipath fading." → 三句方法（CNN 直接映射到 OFDM 基带样本；多径与 OFDM 写成不可训练但可微的层；解码器加入显式信道估计、均衡和子网络）→ 三句结果，含数字："… 2.5 – 4 dB SNR gain for the equivalent image quality compared to … BPG and LDPC …"。

## 3. 引言逻辑（6 段）
- 分离定理需要无限码长 → 悬崖效应 → 传统 JSCC（矢量量化、索引分配）效果不佳 → deep JSCC 系列（RNN 文本、模拟存储、图像、反馈、渐进、注意力、BSC 信道）→ "Different from prior JSCC works, we consider JSCC in the more realistic and challenging multipath fading channels." + 首创。
- 直接把 AWGN 换成多径会因符号间干扰而次优 → 引入模型驱动深度学习（OFDM 作为领域知识）→ 端到端学习 OFDM 的文献只学星座、不管信源 → 本文 → 5 条 bullet 贡献。

## 4. Idea 是怎么提出的
- 空白类型：新信道（多径衰落）+ 已有方法局限（已有 deep JSCC 只考虑 AWGN 和平坦衰落；端到端 OFDM 学习不含信源编码）。
- 核心洞见：不要让黑盒网络去学"对抗多径"，而是把 OFDM、信道估计、均衡这些已知最优或近似最优的结构直接放进网络，网络只学残差修正——"model-based deep learning"。
- 消融实验（Table I/II）直接证明"加领域知识比纯黑盒好"，这是这类 idea 必须提供的证据。

## 5. 科研方法
- 编码器输出作为频域 OFDM 符号；IDFT/DFT、CP 增删都是固定线性层；解码器：LS/MMSE 信道估计 + 均衡 + 两个轻量残差子网（CE subnet、EQ subnet）；联合优化重建损失与信道估计损失。
- 附加模块：训练中加入削波以降低 PAPR；CSI 反馈下的预编码网络做子载波功率分配；对抗损失提升感知质量。

## 6. 仿真与实验
- CIFAR-10/100、CelebA（小图）+ Open Images 训练、Kodak 测试（大图）；OFDM 参数 64 点 FFT、CP 16、8 径。
- 基准：BPG + 802.11n LDPC + OFDM，逐点选最佳 QAM 与码率；完美 CSI 与 MMSE 估计两种。
- 消融（是否 OFDM、是否显式估计 / 均衡、是否残差子网）、信息符号数与导频数的权衡、PAPR-PSNR 权衡、CSI 反馈、对抗损失、SNR 与多径数失配。
- 坦白："As can be seen from Figure 14, our method provides similar PSNR in the low SNR region but worse PSNR in the high SNR region."（大图上 PSNR 高 SNR 时不如基准，但 MS-SSIM 更好）

## 7. 图表
- 17 图 6 表。Fig. 1 分离方案与 deep JSCC 框图对比；Fig. 2 带 OFDM 的流程与解码器细节（颜色区分可训练 / 领域知识模块）；Table I/II 消融，Table III 复杂度。

## 8. 句式库
- 场景切割："Different from prior JSCC works, we consider JSCC in the more realistic and challenging multipath fading channels."
- 直接替换为何不行："Directly replacing the simple channel model such as AWGN with the multipath fading channel in the prior JSCC works may lead to sub-optimal performance due to the inter-symbol interference."
- 模型驱动的理由："Instead of naively treating a neural network as a black box, our model-based deep learning framework imposes a guided structure for neural networks with analytical models and signal …"
- 指出相近工作缺什么："However, those prior works only focus on learning modulation constellation designs for arbitrary binary bit sequence inputs without considering the source coding."
- 可微性论证："… IDFT/DFT and CP removal/insertion can be treated as linear layers (i.e., matrix vector multiplications) with fixed parameters …"

## 9. 结论
- 2 段：首创 + 领域知识的作用 + 对比结果 + PAPR + 鲁棒性 → 三个未来方向。无数字。

## 10. Idea 拆解
- **基线**：DeepJSCC（tccn.2019.2919300）；方法论来自模型驱动深度学习和端到端学习 OFDM。
- **增量**：把信道从 AWGN / 平坦衰落换成多径衰落，并把 OFDM、信道估计、均衡作为固定模块嵌入网络（new-channel + new-component）。
- **为什么有效**："By adding the OFDM data-path and other interpretable steps, we guide the black-box neural network to a better minimum …"
- **证据**：相同图像质量下比 BPG + LDPC + OFDM 有 2.5–4 dB SNR 增益；加入 OFDM 后 15 dB 时 PSNR 提升超过 3 dB（Table I/II）。
- **弱点**：大图高 SNR 时 PSNR 落后；CSI 反馈部分假设完美 CSI；OFDM 参数固定；没有 CFO、同步等实际损伤。
- **开放问题**：
  - "Another future direction is to add more details to the OFDM system such as carrier frequency offset (CFO) and packet detection so that the system is more practical."
  - "Another possible future work is to design novel pilot structures and CSI feedback schemes to improve the accuracy of the CSI and the quality of reconstructed source via …"
  - "One possible direction of future works is to generalize this work to other types of sources such as audio and video."
  - 推断：MIMO-OFDM 下的 JSCC（后续 twc.2024.3422794）；按语义重要性分配子载波（后续 tcomm.2024.3397862）；硬件 / 空口验证。
