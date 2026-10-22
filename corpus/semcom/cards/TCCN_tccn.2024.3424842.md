---
doi: 10.1109/tccn.2024.3424842
title: "SwinJSCC: Taming Swin Transformer for Deep Joint Source-Channel Coding"
journal: TCCN
year: 2025
band: 2022-2025
cites: 239
cites_per_year: 142.7
article_type: research
topic: semantic
source: xplore-html
xplore: 10589474
auto:
  words_total: 6676
  n_sections: 6
  n_subsections: 16
  n_figures: 16
  n_tables: 1
  n_display_eq: 6
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.8
  we_per_1k: 10.4
  title_words: 9
  abstract_words: 234
  abstract_sentences: 6
  phrases: {toTheBest: 0, inThisPaper: 10, contribList: 1, roadmap: 1, however: 7, transition: 8, resultsShow: 1, motivatedBy: 1, toAddress: 5, gapWord: 2, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 7, intensifier: 5, worthNoting: 0, observe: 3, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 8, promising: 1, gen: 4, contrast: 4, firstTime: 0, novel: 1, weProposeFirst: 5, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 6, DNN: 4}
  domain: {Swin: 65, DeepJSCC: 31, transformer: 27, CNN: 25, BPG: 14, LDPC: 13, MSSSIM: 11, CBR: 9, PSNR: 9, attention: 8, complexityCost: 8, perception: 8, AWGN: 7, CIFAR: 6, Rayleigh: 5, DIV2K: 3, Kodak: 3, CLIC: 1}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [context, gap, aim, result, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 10
  intro_moves: [field, prior, prior, gap, aim, approach, approach, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: numbered
  contrib_n: 2
  contrib_verbs: [propose, propose]
  contrib_quantified: false
  first_claim: true          # "Specifically, this paper takes the lead to investigate a new architecture named SwinJSCC …"（弱化版首创）
  roadmap: true
  notation: intro-end
  gap_type: [limitation, tool-transfer]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: true  # FLOPs、参数量、编解码时延（Table I、Fig. 1、Fig. 16）
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4             # CNN deep JSCC、DeepJSCC-V、ADJSCC、BPG + 5G LDPC（另含 BPG + 容量界）
  baseline_naming: acronym
  x_axes: [SNR, bandwidth-ratio, compute, SNR-rate-surface, time]
  fig1_role: result          # Fig. 1 为 "PSNR vs 复杂度" 气泡图
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: true        # 摘要："our open-source project aims to promote the research in this field"
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: image-jscc
  source: [image]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [swin, transformer]
  channel: [AWGN, Rayleigh]
  adaptivity: [SNR, bandwidth-rate]   # Channel ModNet + Rate ModNet，单一模型同时适应 SNR 与速率
  training: [end-to-end]
  metrics: [PSNR, MS-SSIM]
  datasets: [DIV2K, Kodak, CLIC2021, CIFAR-10]
  baselines: [DeepJSCC, other-learned, separate]
  snr_mismatch_test: false            # 随机 SNR 训练、单一模型覆盖 1–13 dB，未单独做失配实验
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [new-component, adaptivity]
  builds_on: [DeepJSCC, ADJSCC, Swin Transformer, NTSCC]
  open_problems_n: 3
---

## 1. 标题
- "[方法名]: Taming [新骨干网络] for [任务]"，9 词。"Taming X for Y" 是把新架构引入领域的常用说法。

## 2. 摘要（6 句，234 词）
- 背景（神经 JSCC 是语义通信关键技术）→ 空白："A general trend … is based on the convolutional neural network (CNN) backbone, whose model capacity is yet limited, inherently leading to inferior system coding gain against traditional …" → 本文（新骨干 + 单模型适应信道与速率 + 开源）→ Swin 优于 CNN 且时延更低 → 两个调制模块 → 结果（与 BPG + 5G LDPC 相当或更好、编码更快，尤其高分辨率）。

## 3. 引言逻辑（10 段，A/B 两个小节）
- A. 背景与相关工作：分离定理前提不成立 → deep JSCC 系列（Bourtsoulatze、ADJSCC、Yang-Kim 速率自适应、DeepJSCC-V 同时适应 SNR 和速率但性能下降）→ "However, these previous works employed CNN networks to focus primarily on low-resolution image datasets, …"
- B. 动机：分辨率升高时 CNN 容量不足 → 本文以 Transformer 为骨干 → "a naive alternation of CNN as Swin Transformer in JSCC cannot yet achieve considerable performance gain"（预先回应"只是换骨干"的质疑）→ JSCC 本质是信源 / 信道速率分配问题，单模型容量不足以学全所有条件下的解 → 两个即插即用模块 → 2 条编号贡献 → 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（CNN 容量有限、只在低分辨率上验证；已有自适应方案只适应 SNR 或速率之一，或者两者都适应但性能下降）+ 工具迁移（Swin Transformer）。
- 写法亮点：用有效感受野可视化（Fig. 4）和"模型宽度 vs 性能"（Fig. 3）先证明"容量是瓶颈"，再引入新骨干——用实验支撑动机，而不是只引用视觉领域的结论。
- 把 JSCC 重新表述为"速率分配问题"，为"需要更大容量才能在单模型里学会所有条件下的分配"提供理由。

## 5. 科研方法
- Swin Transformer 编码器（patch embedding + 分层 patch merging）→ Channel ModNet（SNR 调制：用 SNR 生成缩放因子逐层调制特征）→ Rate ModNet（按通道重要性排序的掩码，选出目标 CBR 对应的通道数）→ 功率归一化 → 信道 → 对称解码器。
- 三个版本：SNR 自适应、速率自适应、二者兼具（SA&RA）；训练时 SNR 在 1–13 dB 均匀采样、速率在离散集合中采样。

## 6. 仿真与实验
- DIV2K 训练，Kodak / CLIC2021 测试，CIFAR-10 作低分辨率验证；基准 CNN deep JSCC、DeepJSCC-V、ADJSCC、BPG + 5G LDPC（2/3 码率 16QAM）。
- 结果呈现：SNR-速率-PSNR 三维曲面（一个模型给出整个曲面）、PSNR vs SNR、PSNR vs CBR、MS-SSIM、视觉对比、编解码时延表（含 BD-rate、参数量、推理时间）、实际多径衰落下逐帧质量对比、模型大小消融。
- 坦白：同时适应 SNR 和速率的版本比单独训练的版本性能低（"We hypothesize that the semantic feature has been resized by the Channel ModNet, leading to the loss of some …"）。

## 7. 图表
- 16 图 1 表。Fig. 1 在引言给出"性能 vs 复杂度"总览图（结果型 Fig. 1），Fig. 3–4 动机实验，Fig. 5–8 架构与模块；caption 写明数据集、信道、SNR 与 CBR。

## 8. 句式库
- 骨干容量的空白："A general trend in many recent works … is based on the convolutional neural network (CNN) backbone, whose model capacity is yet limited, …"
- 现象归因："This phenomenon can be partially attributed to the limited representation capability of CNN, …"
- 预先回应"只是换骨干"："Thus, a naive alternation of CNN as Swin Transformer in JSCC cannot yet achieve considerable performance gain."
- 问题重述："As we can see, JSCC for wireless image/video transmission applications is a typical rate allocation problem between source coding and channel coding [3], …"
- 弱化首创："Specifically, this paper takes the lead to investigate a new architecture named SwinJSCC to address the limitations of CNN-based JSCC methods …"

## 9. 结论
- 1 段 164 词，现在完成时复述；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：CNN 骨干的 DeepJSCC 系列（tccn.2019.2919300、ADJSCC、DeepJSCC-V）；Transformer 化的思路与 NTSCC（jsac.2022.3180802）同组。
- **增量**：换成 Swin Transformer 骨干（new-component），并用两个调制模块让一个模型同时适应 SNR 与 CBR（adaptivity）。
- **为什么有效**："The global attention mechanism inside Transformer enables a closer connection among image patches, which further contributes to the stronger capability to combat channel noise and interference."
- **证据**：高分辨率（Kodak、CLIC2021）上优于 CNN 方案且差距随分辨率增大；与 BPG + 5G LDPC 相当或更好，编解码速度更快；单一模型覆盖 SNR × CBR 曲面。
- **弱点**：SA&RA 联合版本有性能损失；只有 AWGN / Rayleigh（另有一个实际多径单图实验）；只用 PSNR / MS-SSIM，无感知指标；模拟符号、无数字兼容性；无 SNR 失配专门实验。
- **开放问题**：
  - 推断：减少联合自适应的性能损失；数字化（量化 + 星座）下的 Swin 骨干（后续 D²-JSCC 等）；MIMO / OFDM 下的 Transformer JSCC；更大模型 / 生成式先验带来的感知质量提升；轻量化部署。
