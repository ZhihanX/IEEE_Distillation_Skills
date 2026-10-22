---
doi: 10.1109/tccn.2023.3326302
title: "DeepMA: End-to-End Deep Multiple Access for Wireless Image Transmission in Semantic Communication"
journal: TCCN
year: 2024
band: 2022-2025
cites: 71
cites_per_year: 28.3
article_type: research
topic: semantic
source: xplore-html
xplore: 10288558
auto:
  words_total: 8652
  n_sections: 5
  n_subsections: 11
  n_figures: 10
  n_tables: 2
  n_display_eq: 21
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.8
  we_per_1k: 19.5
  title_words: 12
  abstract_words: 228
  abstract_sentences: 6
  phrases: {toTheBest: 0, inThisPaper: 13, contribList: 1, roadmap: 1, however: 3, transition: 8, resultsShow: 2, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 2, intensifier: 4, worthNoting: 2, observe: 14, thisIsBecause: 1, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 9, promising: 0, gen: 0, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  methods: {DNN: 1, complexity: 1, convergence: 1}
  domain: {DeepJSCC: 46, PSNR: 22, AWGN: 11, CIFAR: 11, LDPC: 7, BPG: 6, OFDM: 6, Rayleigh: 6, CNN: 5, ImageNet: 5, attention: 5, Kodak: 4, DeepSC: 3}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [context, aim, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 8
  intro_moves: [field, tech, prior, background, gap, gap-aim, roadmap, notation]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 2
  contrib_verbs: [propose, conduct]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, practicality]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2                        # ADJSCC（单用户独占信道）、BPG + LDPC
  baseline_naming: acronym
  x_axes: [SNR]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: task-multiuser
  source: [image]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [CNN, attention]        # 残差卷积 + 注意力特征块（沿用 ADJSCC）
  channel: [AWGN, Rayleigh]
  adaptivity: [SNR]
  training: [end-to-end]
  metrics: [PSNR, custom]               # SSV 相关矩阵、AACD 用户检测
  datasets: [CIFAR-10, CIFAR-100, ImageNet, Kodak]
  baselines: [DeepJSCC, separate]
  snr_mismatch_test: false
  complexity_reported: false
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [multi-user, new-component, security-privacy]
  builds_on: [ADJSCC, CDMA orthogonal codes]
  open_problems_n: 1
---

## 1. 标题
- "[方法名]: End-to-End Deep Multiple Access for [任务] in Semantic Communication"，12 词。

## 2. 摘要（6 句，228 词）
- 语义通信抗噪优势 → 本文 DeepMA（JSCC + 正交调制）→ 长句机理（多个独立编解码对、编码为相互正交的语义符号向量、解码器从叠加信号中恢复自己的数据）→ 三种场景（D2D、下行、上行）→ 评估设置 → 结果（有效、灵活、隐私保护，带宽效率与传统多址可比）。

## 3. 引言逻辑（8 段 + 2 条反对理由 + 2 条贡献）
- 传统分离式架构（信源编码、信道编码、调制）次优 → DL 端到端语义通信 → 语义通信的压缩与抗噪优势、无悬崖效应 → 多址技术综述（OFDMA、TDMA、CDMA、NOMA）→ TDMA / OFDMA 不能同频 → NOMA 与 CDMA 不适合语义通信（bullet：NOMA 的 SIC 复杂；CDMA 要求比特正确，与有损连续符号不兼容）→ "how to achieve co-frequency multiple access to enable multiple semantic data streams to be transmitted simultaneously with the same frequency remains an unexplored problem" → 本文 → 贡献 → 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：新场景（点对点 → 多址）+ 实用性（传统同频多址与连续有损语义符号不兼容）。
- 核心洞见：让每个编码器在 JSCC 的同时学会"正交调制"（类似 CDMA 的正交码，但由网络学出），各用户的语义符号向量相互正交，叠加后每个解码器能自动滤掉非目标分量；正交性还带来用户检测（相关度 AACD）与"未配对解码器解不出"的隐私性。
- 写作手法：逐一排除已有多址技术（OFDMA/TDMA 不同频、NOMA 复杂、CDMA 不兼容），把"必须新设计"论证成必然。

## 5. 科研方法
- DMANet：N 个编解码对（EDP），每个编码器做 JSCC + 正交调制 → 同步叠加为 MSSV → 信道（AWGN / 慢 Rayleigh）→ 解码器先经 SSV 门（SSVG）做用户检测，再联合正交解调 + 信源信道解码。
- 三种场景的系统模型（D2D、下行、上行），训练时各 EDP 损失求和（Algorithm 1）。

## 6. 仿真与实验
- CIFAR-10 训练 / CIFAR-100 测试；ImageNet 训练 / Kodak24 测试；基准 ADJSCC（独占信道）与 BPG + LDPC。
- DMANet-3 的三种测试（多路复用、独占、交叉解码 = 隐私）→ SSV 相关矩阵（Table I/II）→ AACD 用户检测 → PSNR vs SNR（AWGN、Rayleigh）及 EDP 数的影响 → Kodak24 与 BPG + LDPC。
- 坦白：同等资源下 DeepMA 比 ADJSCC 的 PSNR 低（部分资源用于正交调制）。

## 7. 图表
- 10 图 2 表 1 算法。Fig. 2 三种多址场景并列；Fig. 5 用"交叉解码失败"的图像直观展示隐私性；Table I/II 相关矩阵证明正交性——"机理可视化"的证据。

## 8. 句式库
- 新问题："As a new communication paradigm, currently, semantic communication research mainly addresses the deep learning-based joint source-channel coding (DeepJSCC) problem for point-to-point communication tasks [3], and how to achieve …"
- 文献空白收束："All the works discussed above focus on the DeepJSCC problem for achieving point-to-point semantic communication scenario, and the OMA problem has not been investigated."
- 机理解释："This is because these SSVs are mutually orthogonal, and the decoders can automatically filter out the non-desired SSVs."
- 悬崖效应定义："Compared with traditional digital communication schemes, DeepJSCC does not suffer from the 'cliff effect', and it has a strong noise resiliency capability against the degradation of channel SNR."
- 坦白代价："However, the DMANet also needs to allocate more resources to the orthogonal modulation process, and therefore its remaining source coding resources will be lower than ADJSCC, and the …"

## 9. 结论
- 1 段 135 词：复述 + 坦白正交调制带来的性能损失；无数字。

## 10. Idea 拆解
- **基线**：ADJSCC（单用户 SNR 自适应 deep JSCC）；CDMA / NOMA 等传统多址。
- **增量**：让 deep JSCC 编码器学习相互正交的语义符号，实现同频多址、用户检测与隐私（multi-user + new-component + security-privacy）。
- **为什么有效**：训练使不同 EDP 的输出近似正交，叠加后对目标解码器而言其他用户的分量近似被滤除。
- **证据**：SSV 相关矩阵近似对角；未配对解码器无法恢复图像；PSNR 接近独占信道的 ADJSCC 且无悬崖效应。
- **弱点**：用户数固定、编解码对必须联合训练（新增用户需重训）；要求严格同步；没有与 OFDMA / TDMA 在相同总带宽下的严格对比；正交性带来的 PSNR 损失；无复杂度分析。
- **开放问题**：
  - "In future work, we can explore the design of a more powerful network architecture to improve the transmission performance of the proposed DeepMA model."
  - 推断：用户数可变 / 动态接入；非正交语义多址（语义 NOMA，见 jsac.2022.3222000）；异步与多径下的正交性；与经典多址在相同资源下的公平比较；隐私性的信息论量化。
