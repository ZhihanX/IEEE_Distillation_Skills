---
doi: 10.1109/twc.2024.3422794
title: "Deep Joint Source-Channel Coding for Adaptive Image Transmission Over MIMO Channels"
journal: TWC
year: 2024
band: 2022-2025
cites: 117
cites_per_year: 58.3
article_type: research
topic: semantic
source: xplore-html
xplore: 10597355
auto:
  words_total: 7204
  n_sections: 5
  n_subsections: 33
  n_figures: 11
  n_tables: 6
  n_display_eq: 31
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 25.5
  we_per_1k: 16.9
  title_words: 11
  abstract_words: 151
  abstract_sentences: 6
  phrases: {toTheBest: 1, inThisPaper: 1, contribList: 1, roadmap: 0, however: 7, transition: 6, resultsShow: 0, motivatedBy: 2, toAddress: 2, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 9, intensifier: 5, worthNoting: 0, observe: 14, thisIsBecause: 0, asExpected: 1, insight: 0, tradeoff: 0, figVerb: 0, promising: 0, gen: 0, contrast: 2, firstTime: 0, novel: 2, weProposeFirst: 0, wlog: 1, code: 0, prototype: 1}
  methods: {complexity: 7, DNN: 1}
  domain: {MIMO: 126, DeepJSCC: 100, BPG: 24, CBR: 15, LDPC: 15, transformer: 12, PSNR: 11, Kodak: 8, attention: 8, CIFAR: 5, capacityBound: 5, perception: 5, CelebA: 4, ImageNet: 4, LPIPS: 4, CNN: 2, Swin: 2}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, method, result, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 8
  intro_moves: [field, prior, prior, prior, gap, gap, aim, contrib]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [present, apply, validate]
  contrib_quantified: false
  first_claim: true            # 贡献列表："This paper presents the first DeepJSCC scheme over the MIMO system for image transmission."
  roadmap: false
  notation: none
  gap_type: [new-scenario, limitation]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: true    # Table IV 参数量、FLOPs、编解码时间
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3               # BPG + LDPC（球形译码）、BPG + 容量界（含注水）、神经压缩 + 容量界
  baseline_naming: acronym
  x_axes: [SNR, bandwidth-ratio, CSI-error, number-of-antennas]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2     # 另附 2 条带标题的未来方向 bullet
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: image-jscc
  source: [image]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [transformer]
  channel: [MIMO, Rayleigh]
  adaptivity: [SNR, CSI]        # 信道热图 + 自注意力；随机 SNR / 随机天线数训练
  training: [end-to-end]
  metrics: [PSNR, LPIPS]
  datasets: [CIFAR-10, ImageNet, Kodak, CelebA]
  baselines: [separate]
  snr_mismatch_test: true       # universal 模型跨 SNR、跨天线数测试
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [new-channel, adaptivity]
  builds_on: [DeepJSCC, ViT-based adaptive JSCC]
  open_problems_n: 2
---

## 1. 标题
- "[方法] for [特性] [任务] Over [信道]"，11 词。

## 2. 摘要（6 句，151 词，偏短）
- 第 1 句锚点 + 方法名 DeepJSCC-MIMO → 开环 / 闭环两种系统 → 超过分离基准、对估计误差鲁棒、不重训就能适应信道与天线配置 → 机理（自注意力学习特征映射与功率分配）→ 失真与感知质量都提升 → 鲁棒性与应用前景。

## 3. 引言逻辑（8 段）
- 多媒体需求 → 分离定理与有限码长 → DeepJSCC 的已有扩展（带宽自适应、多径、原型、星座约束、PAPR）→ "However, existing DeepJSCC schemes solely consider single-antenna transmitters and receivers." → 端到端 MIMO 学习只传比特、只针对固定 SNR（Table I 对比）→ 首创（"prior research has not delved into …"）→ 四个挑战用 bullet 列出（性能、模型泛化、信道适应、信道鲁棒）→ 本文与 3 条贡献。

## 4. Idea 是怎么提出的
- 空白类型：新信道（MIMO，开环 CSIR / 闭环 CSIT）+ 已有方法局限（端到端 MIMO 学习不考虑语义、不适应信道）。
- 核心洞见：把 CSI 转成"每个信道符号面对的等效噪声功率"热图，与图像 patch 一起送进 ViT，让自注意力同时学"哪些语义特征放到哪个子信道、给多少功率"。
- 保留成熟的模型驱动组件（SVD 预编码、MMSE/ZF 均衡），网络只学剩下的——与 OFDM-Guided JSCC 同一思路。

## 5. 科研方法
- 图像转 patch 序列 → 信道热图（开环：均衡后的等效噪声；闭环：SVD 子信道增益）→ ViT 编码器 → 功率归一化 → MIMO 信道 → 均衡 → 孪生层 + ViT 解码器；损失 = MSE + 0.1 × LPIPS（可选）。
- universal 版本：训练时随机 SNR（0–22 dB）与随机天线数，单一模型适应不同条件。

## 6. 仿真与实验
- 2×2 MIMO，CIFAR-10 为主，ImageNet 训练 + Kodak / CelebA 测试；相关 MIMO 信道结果放在扩展版附录。
- 基准：BPG + LDPC（球形译码）、BPG + 容量界（闭环用注水）、多种神经压缩算法 + 容量界（Table II）。
- 实验维度：SNR 自适应、带宽比、信道估计误差、模型效率（Table IV）、SVD 消融、信道热图消融、功率分配可视化、天线数适应。

## 7. 图表
- 11 图 6 表。Table I 在引言对比已有端到端 MIMO 方案；Fig. 10 把信道热图与学到的功率分配并排可视化（解释机制）。

## 8. 句式库
- 空白："However, existing DeepJSCC schemes solely consider single-antenna transmitters and receivers."
- 难点："It is challenging to design a practical JSCC scheme for MIMO channels, where the model needs to learn how to map the input signal to multiple antennas, …"
- 指出相近工作没做到："However, we remark that the aforementioned works focus on the transmission of bits/one-hot vectors for specific signal-to-noise ratio (SNR) values, and do not consider the contextual features of …"
- 设计直觉："We expect that feeding the CSI in the form of a heatmap will simplify the training process as the model only needs to focus on the 'additive' noise …"
- 首创："This paper presents the first DeepJSCC scheme over the MIMO system for image transmission."

## 9. 结论
- 2 段 + 2 条带标题的未来方向（与空时编码结合的 JSCC；可变码长 JSCC）。无数字。

## 10. Idea 拆解
- **基线**：单天线 DeepJSCC（tccn.2019.2919300 等）与端到端 MIMO 自编码器（只传比特）。
- **增量**：把 DeepJSCC 推广到 MIMO，并用"信道热图 + ViT 自注意力"让单一模型适应 SNR、CSI 误差、天线数（new-channel + adaptivity）。
- **为什么有效**：自注意力能同时看到语义特征和每个子信道的噪声水平，从而学出"重要特征放到好子信道"的映射与功率分配（Fig. 10 可视化支持）。
- **证据**：闭环下 R = 1/24、1/12 时比 BPG + 容量界至少高 1.98 dB / 1.78 dB；CelebA 上低 SNR 最高 2.1 dB 增益；universal 模型相对专用模型损失至多约 0.27 dB。
- **弱点**：主要实验是 2×2 i.i.d. 瑞利；ViT 复杂度随序列长度平方增长；模拟符号；无硬件验证。
- **开放问题**：
  - 结论 bullet："JSCC with space-time coding. In the open-loop scenario, full potential of the spatial and temporal dimensions in MIMO can be harnessed by integrating DeepJSCC with space-time codes [56]."
  - 结论 bullet："Variable length JSCC. Building upon the adaptability of ViT-based models to varying antenna numbers, future investigations can extend this concept to accommodate variable code lengths, …"
  - 推断：多用户 MIMO 下的语义传输与干扰管理；大规模 MIMO / 相关信道下的扩展；与数字调制兼容的 MIMO JSCC。
