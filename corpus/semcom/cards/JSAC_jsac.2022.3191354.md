---
doi: 10.1109/jsac.2022.3191354
title: "DeepWiVe: Deep-Learning-Aided Wireless Video Transmission"
journal: JSAC
year: 2022
band: 2022-2025
cites: 213
cites_per_year: 52.1
article_type: research
topic: semantic
source: xplore-html
xplore: 9837870
auto:
  words_total: 7272
  n_sections: 5
  n_subsections: 4
  n_figures: 16
  n_tables: 1
  n_display_eq: 34
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.0
  we_per_1k: 12.2
  title_words: 5
  abstract_words: 211
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 0, contribList: 1, roadmap: 0, however: 5, transition: 3, resultsShow: 0, motivatedBy: 1, toAddress: 5, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 8, intensifier: 0, worthNoting: 1, observe: 6, thisIsBecause: 1, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 4, promising: 0, gen: 0, contrast: 0, firstTime: 0, novel: 1, weProposeFirst: 2, wlog: 0, code: 0, prototype: 0}
  # firstTime 0 为漏检（"the first-ever end-to-end … video transmission scheme"）
  methods: {complexity: 8, DNN: 3, DRL: 3, convergence: 3, compressedSensing: 1}
  domain: {videoCodec: 29, MSSSIM: 15, PSNR: 14, AWGN: 9, LDPC: 9, attention: 7, CBR: 4, feedback: 3, perception: 3, CNN: 2, QAM: 2, SNRmismatch: 2, complexityCost: 2, UCF101: 1}
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [aim, method, method, method, result, result, result]
  abstract_has_numbers: true            # MS-SSIM 提升 0.0485 / 0.0069
  abstract_anchor: we-verb              # "We present DeepWiVe, the first-ever …"
  intro_paragraphs: 10
  intro_moves: [field, gap, gap, prior, theory-prior, prior, aim, approach, approach, contrib]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [propose, train, optimize, show, show]
  contrib_quantified: false
  first_claim: true                     # 摘要首句 "the first-ever end-to-end JSCC video transmission scheme"
  roadmap: false
  notation: table                       # Table I
  gap_type: [new-scenario, limitation]
  motivating_figure: true               # Fig. 1 分离式视频传输框图
  problem_class: learning
  solution: [DNN, RL]                   # DQN 学带宽分配
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4                        # H.264 / H.265 + LDPC + QAM；均匀分配、启发式分配
  baseline_naming: descriptive
  x_axes: [SNR, CBR, epochs]
  fig1_role: background
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: true          # 带宽分配提升 0.35 dB / 0.25 dB
  conclusion_future_work: true
semcom:
  category: modality
  source: [video]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [CNN, attention]        # 关键帧编解码 + SSF 运动估计插值网络
  channel: [AWGN, Rayleigh]             # 块衰落（发端只知平均 SNR）
  adaptivity: [SNR, bandwidth-rate]     # SNR 输入的注意力模块；RL 帧间带宽分配
  training: [multi-stage, RL]
  metrics: [PSNR, MS-SSIM]
  datasets: [UCF101, BVI-DVC]
  baselines: [separate, own-ablation]
  snr_mismatch_test: true               # Fig. 10 估计 SNR 与实际 SNR 失配
  complexity_reported: false
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [new-modality, adaptivity]
  builds_on: [DeepJSCC, successive refinement DeepJSCC, scale-space flow video compression, DQN]
  open_problems_n: 2
---

## 1. 标题
- "[方法名]: Deep-Learning-Aided Wireless Video Transmission"，5 词。

## 2. 摘要（7 句，211 词）
- 首句即首创声明（"the first-ever end-to-end JSCC video transmission scheme"）+ 机理一句 → 残差预测 → 可变带宽 → RL 带宽分配 → 三句结果（避免悬崖效应且对 SNR 估计失配平滑退化；MS-SSIM 优于 H.264 / H.265 + LDPC，带具体数字；最优分配优于均匀 / 启发式）。

## 3. 引言逻辑（10 段 + 5 条贡献）
- 视频占互联网流量 80% → 分离式框图（Fig. 1）→ "However, the limits of the separation-based designs are beginning to rear …"（VR、无人机监控）→ 悬崖效应与保守速率 + ARQ → JSCC 理论优势与跨层方案复杂度不划算 → 模拟传输（AM/FM、SoftCast）在高斯信源上达香农界但带宽不匹配时次优 → DeepJSCC 打破复杂度壁垒 → 本文 → 视频压缩的核心（帧间相关、残差）→ JSCC 中发送端不知道残差 → 用 DNN 在接收端预测残差 → RL 带宽分配 → 贡献。

## 4. Idea 是怎么提出的
- 空白类型：新场景（deep JSCC 从图像到视频）+ 已有方法局限（分离方案的悬崖效应）。
- 核心洞见：传统视频编码依赖"发送端知道残差"（编码器内置解码器），而 JSCC 的重建依赖实际信道，发送端无法得知残差——改由接收端 DNN 预测残差，省去失真反馈；再把帧间带宽分配建模成 MDP 用 DQN 学习。
- 写法亮点：用信息论事实（高斯信源 + AWGN 下未编码传输达香农界）为"模拟 JSCC"背书，同时坦承带宽不匹配时次优——让后续 DNN 方案显得是"取两者之长"。

## 5. 科研方法
- 关键帧 deep JSCC（带 SNR 注意力模块，单模型覆盖多 SNR）；非关键帧：SSF（scaled space flow）运动 + 残差经插值编码器传输，接收端估计 SSF、残差与掩码。
- 带宽分配：GoP 为时间步的 MDP（状态 = 帧与已分配情况，动作 = 各帧带宽块数，奖励 = PSNR / MS-SSIM），DQN + ε-greedy。
- 两种 CSI 场景：静态信道全知；块衰落（发端只知平均 SNR，收端只知相位）。

## 6. 仿真与实验
- UCF101 训练、BVI-DVC 测试；训练 SNR 在 [−5, 20] dB 均匀采样。
- SNR 估计失配下与 H.264 + LDPC 比较（悬崖效应 vs 平滑退化）→ 对 H.264 / H.265（AWGN）→ 视觉示例 → 衰落信道 → 可变带宽压缩比（只重训分配网络）→ 带宽分配消融。
- 坦白：PSNR 不如 H.265，只在 MS-SSIM 上胜出。

## 7. 图表
- 16 图 1 表。Fig. 1–2 背景图（分离式系统、视频插值结构）放在引言；Fig. 7 把带宽分配画成 MDP；Fig. 10 专门展示"估计失配"——论证悬崖效应的标准图。

## 8. 句式库
- 首创声明（摘要首句）："We present DeepWiVe, the first-ever end-to-end joint source-channel coding (JSCC) video transmission scheme that leverages the power of deep neural networks (DNNs) to directly map video signals to …"
- 分离方案局限："However, the limits of the separation-based designs are beginning to rear with the emergence of more demanding video delivery applications, such as wireless virtual reality (VR) and drone-based surveillance systems."
- 悬崖效应定义："That is, when the channel condition deteriorates below the level anticipated by the channel encoder, the source information becomes irrecoverable."
- 跨层 JSCC 的不足："While there have been many such proposals over the years [6]–​[13], these techniques typically do not provide sufficient gains to justify the significant increase in system complexity."
- 坦白 PSNR 劣势："Although, H.265 performs better than DeepWiVe in terms of the PSNR metric, DeepWiVe outperforms H.265 when compared in terms of MS-SSIM, which is widely accepted as a performance …"

## 9. 结论
- 2 段：复述 + 带数字的收益 + 坦白 PSNR 劣势 → 未来工作（可变 GoP、SDR 实测）。

## 10. Idea 拆解
- **基线**：DeepJSCC（tccn.2019.2919300）及其逐级细化版本；SoftCast；H.264 / H.265 + LDPC。
- **增量**：首个 deep JSCC 视频传输方案——接收端预测残差（无需失真反馈）+ RL 帧间带宽分配（new-modality + adaptivity）。
- **为什么有效**：帧间相关通过运动 + 残差利用；模拟传输避免悬崖效应；带宽按帧的重要性动态分配。
- **证据**：所有信道条件下优于 H.264 + LDPC；MS-SSIM 优于 H.265 + LDPC；带宽分配比均匀分配高 0.35 dB。
- **弱点**：PSNR 不如 H.265；固定 GoP；DQN 动作空间离散且需单独训练；无复杂度 / 时延分析；无硬件验证（列为未来工作）。
- **开放问题**：
  - "As part of future work, the coding efficiency of DeepWiVe may be improved by considering variable GoP sizes."
  - "The performance of the models should also be evaluated in practical channels, using, for example, software defined radios (SDRs)."
  - 推断：语义特征域条件编码（后续 jsac.2022.3221977 DVST）；数字化视频 JSCC；多用户 / 广播视频；任务导向视频（检测、跟踪）。
