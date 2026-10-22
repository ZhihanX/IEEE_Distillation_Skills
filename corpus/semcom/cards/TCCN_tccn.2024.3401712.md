---
doi: 10.1109/tccn.2024.3401712
title: "LaMoSC: Large Language Model-Driven Semantic Communication System for Visual Transmission"
journal: TCCN
year: 2024
band: 2022-2025
cites: 70
cites_per_year: 38.0
article_type: research
topic: semantic
source: xplore-html
xplore: 10531769
auto:
  words_total: 6461
  n_sections: 6
  n_subsections: 17
  n_figures: 11
  n_tables: 2
  n_display_eq: 20
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 20.9
  we_per_1k: 6.8
  title_words: 10
  abstract_words: 180
  abstract_sentences: 10
  phrases: {toTheBest: 1, inThisPaper: 2, contribList: 0, roadmap: 1, however: 6, transition: 12, resultsShow: 1, motivatedBy: 1, toAddress: 2, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 10, intensifier: 9, worthNoting: 1, observe: 1, thisIsBecause: 0, asExpected: 0, insight: 3, tradeoff: 0, figVerb: 2, promising: 2, gen: 0, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 0, code: 0, prototype: 2}
  # contribList 0 为漏检（"We summarize the contributions as follows:"）
  methods: {DNN: 4, complexity: 1}
  domain: {LLM: 41, attention: 26, PSNR: 18, LPIPS: 16, JPEG: 12, BPG: 10, MSSSIM: 10, perception: 8, SSIM: 7, DeepJSCC: 5, transformer: 5, accuracy: 5, complexityCost: 4, knowledgeBase: 4, sentSim: 4, CIFAR: 3, DeepSC: 3}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [context, context, gap, aim, method, method, method, result, result, result]
  abstract_has_numbers: true            # 比 Deep-JSCC / MLSC 高 5.5% / 2.6%（4 dB）
  abstract_anchor: this-paper-verb
  intro_paragraphs: 6
  intro_moves: [field, prior, gap, aim, result, roadmap]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [propose, design, conduct]
  contrib_quantified: false
  first_claim: true                     # "LaMoSC is the pioneering approach that integrates … LLM … into the domain of semantic communication"
  roadmap: true
  notation: table                       # Table I Summary of Notations
  gap_type: [new-tool, limitation]
  motivating_figure: false
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: true             # 双工作站原型上的编解码 / 传输时延
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 5                        # JPEG、BPG、Deep-JSCC、Deep-JSCC-f、MLSC
  baseline_naming: acronym
  x_axes: [SNR, compression-ratio, network-type, image-count]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: true        # 两台工作站测时延（非无线硬件）
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: generative
  source: [image, text]                 # 图像 + LLM 生成的提示文本
  task: [reconstruction]
  paradigm: knowledge-based
  architecture: [LLM, transformer, attention]   # BLIP-2 生成提示、BERT 文本编码、ViT 编解码、跨模态多头注意力
  channel: [AWGN]
  adaptivity: [none]
  training: [end-to-end, pretrained-frozen]
  metrics: [PSNR, MS-SSIM, LPIPS]
  datasets: [CIFAR-10, ADE20K, ImageNet]
  baselines: [separate, DeepJSCC, other-learned]
  snr_mismatch_test: false
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [knowledge-base, new-modality, generative-prior]
  builds_on: [DeepJSCC, MLSC, BLIP-2, BERT, ViT]
  open_problems_n: 2
---

## 1. 标题
- "[方法名]: [工具]-Driven Semantic Communication System for [模态] Transmission"，10 词。

## 2. 摘要（10 句，180 词）
- 两句背景 → 空白（单模态视觉特征在低 SNR 下解码不准）→ 本文 LaMoSC → 三句方法（LLM 驱动的多模态融合框架、视觉-文本端到端编解码、注意力融合）→ 三句结果（低 SNR 优势、比 Deep-JSCC / MLSC 高 5.5% / 2.6%、泛化能力）。

## 3. 引言逻辑（6 段 + 2 条挑战 bullet + 3 条贡献 bullet）
- AI 与语义通信 → "However, existing semantic communication systems, which predominantly rely on single modality features such as text, images, or audio, face limitations in robustness and quality, particularly in low signal-to-noise …" + 一个具体例子（猫被解码成花）→ 研究两大方向 → 空白（单模态、稳定环境）→ LLM 的能力 → 两个挑战（bullet）→ 本文分别回应两个挑战 → 原型与结果（带数字）→ 贡献 → 路线图。

## 4. Idea 是怎么提出的
- 空白类型：新工具迁移（LLM / 多模态大模型）+ 已有方法局限（单模态特征在低 SNR 下易错）。
- 核心洞见：在发送端用多模态 LLM（BLIP-2）从图像"生成"一段描述文本，把它作为额外的语义模态与视觉特征融合后传输；当视觉特征在低 SNR 下部分损坏时，文本语义提供冗余与纠正。
- "挑战 → 对应设计"的一一对应写法：两个挑战 bullet，"To address the first challenge …" / "To address the second challenge …"。

## 5. 科研方法
- 编码：BLIP-2 生成提示文本 → BERT 文本编码 + ViT 图像编码 → 跨模态多头注意力融合（文本作 query）→ 与图像特征拼接 → 信道编码。
- 解码：信道解码 → ViT 解码器重建。
- 损失：MSE + SSIM 重建损失 + 提示文本语义相似度损失（三个权重 λ1–λ3）。

## 6. 仿真与实验
- CIFAR-10、ADE20K；ImageNet 测泛化；基准 JPEG、BPG、Deep-JSCC、Deep-JSCC-f、MLSC。
- PSNR / MS-SSIM / LPIPS vs SNR 与压缩比 → 消融（去 LLM、拼接替代注意力、去 ViT）→ 原型时延（编码 73 ms）→ 未见数据集泛化。
- 坦白：低压缩比时 DeepJSCC 的 PSNR 高于 MLSC-image；编码时延较高。

## 7. 图表
- 11 图 2 表。Table I 记号表；Fig. 4 图像-提示对示例（直观展示 LLM 生成的语义）；Table II 消融。

## 8. 句式库
- 单模态空白："However, existing semantic communication systems, which predominantly rely on single modality features such as text, images, or audio, face limitations in robustness and quality, particularly in low signal-to-noise …"
- 首创性（"pioneering"）："To the best of our knowledge, LaMoSC is the pioneering approach that integrates the power of large-scale pre-training LLM and explicit knowledge into the domain of semantic communication."
- 相关工作收束："However, there has not been in-depth research on multimodal feature extraction and fusion in semantic communication."
- 坦白局限（结论）："LaMoSC's limitation is how to lighten the proposed multimodal semantic encoding and decoding so that it can be applied on mobile devices."

## 9. 结论
- 2 段：问题 → 两个挑战与对应设计 → 评估与泛化 → 局限（轻量化）+ 未来工作（优化编解码框架、其他模态）。

## 10. Idea 拆解
- **基线**：Deep-JSCC（tccn.2019.2919300）、Deep-JSCC-f（jsait.2020.2987203）、多层语义感知 MLSC。
- **增量**：用多模态 LLM 在发送端生成文本描述作为辅助语义，与视觉特征经跨模态注意力融合后联合传输（knowledge-base + new-modality + generative-prior）。
- **为什么有效**：LLM 生成的文本是对图像的高层语义压缩，对信道噪声更稳健；低 SNR 时视觉特征受损，文本特征经注意力补足语义一致性。
- **证据**：4 dB 时比 Deep-JSCC / MLSC 高 5.5% / 2.6%；消融中去掉 LLM 或用拼接替代注意力均明显下降；未见数据集（ImageNet）上泛化最好。
- **弱点**：只有 AWGN；文本模态带来的额外带宽开销与公平性（相同 CBR 下比较？）交代不清；编码时延高、模型大；CIFAR-10 小图上用 LLM 生成描述的必要性存疑；无理论。
- **开放问题**：
  - "LaMoSC's limitation is how to lighten the proposed multimodal semantic encoding and decoding so that it can be applied on mobile devices."
  - "Future research avenues could explore the further optimization of the encoder-decoder framework and expand the model's application to other modalities."
  - 推断：文本 / 视觉两路的带宽分配与不等错误保护；接收端用生成模型（扩散）从文本 + 粗视觉特征重建；LLM 推理时延与能耗的系统级优化；衰落信道与数字传输下的多模态融合。
