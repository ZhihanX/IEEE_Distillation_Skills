---
doi: 10.1109/jsac.2022.3221968
title: "Wireless Semantic Communications for Video Conferencing"
journal: JSAC
year: 2023
band: 2022-2025
cites: 271
cites_per_year: 72.1
article_type: research
topic: semantic
source: xplore-html
xplore: 9955991
auto:
  words_total: 6975
  n_sections: 6
  n_subsections: 22
  n_figures: 9
  n_tables: 3
  n_display_eq: 37
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 18.8
  we_per_1k: 0.1                        # 几乎全用被动语态
  title_words: 6
  abstract_words: 193
  abstract_sentences: 11
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 1, however: 17, transition: 11, resultsShow: 0, motivatedBy: 0, toAddress: 1, gapWord: 2, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 1, intensifier: 7, worthNoting: 0, observe: 0, thisIsBecause: 0, asExpected: 0, insight: 1, tradeoff: 0, figVerb: 4, promising: 0, gen: 0, contrast: 4, firstTime: 0, novel: 6, weProposeFirst: 0, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 4}
  domain: {feedback: 29, quantization: 10, OFDM: 9, QAM: 8, SNRmismatch: 7, LDPC: 4, SSIM: 2, AWGN: 1, CNN: 1, Rayleigh: 1, accuracy: 1, perception: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, context, context, gap, aim, insight, gap, method, result, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 5
  intro_moves: [field, prior, scenario-gap, aim, roadmap]
  related_work: in-model-section
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [establish, combine, exploit]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: none
  gap_type: [new-scenario, practicality]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: true             # Table III 帧率
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3                        # H264（+ RS / LDPC）、AV1；以及 SVC 各变体
  baseline_naming: acronym
  x_axes: [BER, bpp]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 3
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: modality
  source: [video]
  task: [reconstruction]                # 说话人人脸视频（关键点驱动生成）
  paradigm: knowledge-based             # 显式共享知识：说话人照片；只传关键点
  architecture: [CNN, GAN]              # 关键点检测器 + 生成器 + 块级判别器
  channel: [AWGN, Rayleigh, OFDM]       # 频率选择性多径
  adaptivity: [feedback-HARQ, CSI]
  training: [multi-stage, end-to-end]
  metrics: [SSIM, custom]               # Ploss（VGG 感知损失）、AKD（平均关键点距离）
  datasets: [VoxCeleb]
  baselines: [separate, own-ablation]
  snr_mismatch_test: true               # Table II 匹配 / 失配信道
  complexity_reported: true
  digital_compatible: true              # 关键点量化成比特，可接 QAM / OFDM
  hardware_validation: false
  theory: none
  idea_delta: [new-modality, feedback-retransmission, knowledge-base, new-metric]
  builds_on: [first-order motion model (keypoint-driven face reenactment), IR-HARQ, adaptive modulation]
  open_problems_n: 0
---

## 1. 标题
- "Wireless Semantic Communications for [应用场景]"，6 词。以具体应用（视频会议）命名。

## 2. 摘要（11 句，193 词）
- 三句背景（视频会议耗资源；传统压缩降分辨率；SVC 只传关键点）→ 空白（关键点传输错误的影响研究不足）→ 本文 SVC 网络 → 洞见（传输错误只改变表情，而非毁坏像素）→ 第二个空白（CRC 无法反映表情变化程度）→ SVC-HARQ + 语义错误检测器 → 结果 → SVC-CSI → 结果。两次 "However" 引出两层空白。

## 3. 引言逻辑（5 段 + 3 条带小标题贡献）
- 语义通信中共享知识的作用与实现难度 → DL 在通信与语义通信中的应用 → 视频会议的资源需求 → 关键点驱动的人脸重演已用于压缩 → "However, the existing studies only relate to the source coding module, and the effect of errors from the physical channel transmission is unclear." → 本文（三层框架、HARQ、CSI）→ 路线图。

## 4. Idea 是怎么提出的
- 空白类型：新场景（视频会议）+ 实用性（把语义编码接入经典链路自适应机制 HARQ / AMC）。
- 核心洞见一：视频会议中说话人照片可作为显式共享知识预先传输，实时只传少量关键点（每帧 160 bit）——这是"显式知识库"型语义通信。
- 核心洞见二：语义传输的错误形态不同于比特错误（关键点偏移 → 表情改变而非像素毁坏），所以 CRC 不再适合作为 HARQ 的判据，需要"语义错误检测器"（VGG 质量检测器 / 基于相邻帧流畅度的检测器）。
- 把通信领域的经典工具（IR-HARQ、按子信道 SNR 排序分配）与语义系统结合，说明"语义通信也需要链路层设计"。

## 5. 科研方法
- SVC：关键点检测器 → 全连接编码 + 量化 → 比特 → 信道 → 解量化 + 全连接解码 → 生成器（共享照片 + 关键点重建帧）。
- SVC-HARQ：首传 160 bit，语义检测器判定 ACK / NACK，不合格则增量传输（只针对易错关键点）。
- SVC-CSI：按子信道 SNR 对符号排序，网络学会把重要信息放在好的子信道；两种调制（全分辨率星座 / 量化后 16-QAM）；SVC-CSI-HARQ 在失配信道下恢复鲁棒性。
- 损失：VGG 感知损失 + 块级判别器 + 等变损失；指标 Ploss、AKD、SSIM。

## 6. 仿真与实验
- VoxCeleb 人脸视频（256×256）；基准 H264（不同 CRF，+ RS / LDPC）、AV1。
- 码率对比（Table I，bpp）→ 内容损失与错误形态示例（Fig. 5）→ 两种检测器的接受率 → HARQ 下 Ploss / AKD / 吞吐 vs BER → CSI 反馈的权重可视化 → 星座与功率分配 → 匹配 / 失配信道（Table II）→ 帧率（Table III）。
- 坦白：AV1 的 SSIM 始终优于 SVC；SVC-CSI 在失配信道下鲁棒性下降。

## 7. 图表
- 9 图 3 表。Fig. 1 三层框架（语义层 / 技术层 / 效果层）；Fig. 5 并排展示"像素毁坏 vs 表情改变"两种错误——机制论证的关键图；Fig. 8(b) 用权重灰度图解释 CSI 的作用。

## 8. 句式库
- 场景空白："However, the existing studies only relate to the source coding module, and the effect of errors from the physical channel transmission is unclear."
- 错误形态对比（摘要）："Transmission errors in SVC only lead to a changed expression, whereas those in the conventional methods directly destroy pixels."
- 指出传统检错不适用："However, the conventional error detector, such as cyclic redundancy check, cannot reflect the degree of expression changes."
- 语义 + 链路自适应的挑战："Although the combination of the semantic networks and conventional link adaptive methods is naturally considered, the novel mechanism on semantic transmission brings challenges in the design at the technical level."
- 权衡收尾（结论）："The combination of CSI and ACK feedback can balance performance, bit consumption, and robustness."

## 9. 结论
- 3 段分别对应 SVC、SVC-HARQ、SVC-CSI；最后一段坦白 CSI 方案鲁棒性下降，用 CSI + ACK 组合收尾。无未来工作。

## 10. Idea 拆解
- **基线**：关键点驱动的人脸视频压缩（first-order motion model 等）；H264 / AV1 + 信道编码；经典 IR-HARQ 与自适应调制。
- **增量**：把关键点语义压缩放到真实信道上，提出语义错误检测器驱动的 HARQ 与 CSI 反馈下的子信道语义分配（new-modality + feedback-retransmission + knowledge-base + new-metric）。
- **为什么有效**：共享照片承载了大部分外观信息，关键点只承载运动，码率极低；关键点错误只影响表情，可由流畅度检测并增量重传修复。
- **证据**：每帧仅 160 bit 即达到与 H264 相当的 Ploss；高 BER 下仍可辨认说话人；SVC-HARQ 在不同 BER 下灵活消耗比特并逼近各 BER 下单独训练的最优。
- **弱点**：仅限说话人头像这一窄场景；需预先共享照片（隐私、换人 / 换背景时失效）；SSIM 不如 AV1；评价以 Ploss / AKD 为主，缺主观评测；按 BER 而非 SNR 评估（绕开了调制编码细节）；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：语义 HARQ 的通用化（其他模态的语义错误检测器）；关键点 + 残差的分层传输兼顾细节；扩散 / 3D 人脸模型提升保真；多方会议的多用户资源分配；生成内容的身份安全（深伪风险）。
