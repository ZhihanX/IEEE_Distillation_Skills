---
doi: 10.1109/twc.2023.3265201
title: "Robust Semantic Communications With Masked VQ-VAE Enabled Codebook"
journal: TWC
year: 2023
band: 2022-2025
cites: 297
cites_per_year: 104.5
article_type: research
topic: semantic
source: xplore-html
xplore: 10101778
auto:
  words_total: 8336
  n_sections: 6
  n_subsections: 39
  n_figures: 11
  n_tables: 3
  n_display_eq: 19
  n_algorithms: 3
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, remark: 1, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.8
  we_per_1k: 11.1
  title_words: 8
  abstract_words: 213
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 1, however: 8, transition: 26, resultsShow: 3, motivatedBy: 0, toAddress: 3, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 8, intensifier: 13, worthNoting: 0, observe: 2, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 8, promising: 0, gen: 0, contrast: 6, firstTime: 0, novel: 6, weProposeFirst: 8, wlog: 0, code: 0, prototype: 0}
  methods: {DNN: 1, DRL: 1}
  domain: {VQ: 55, VAE: 30, accuracy: 20, JPEG: 10, LDPC: 10, transformer: 5, quantization: 4, AWGN: 2, attention: 2, feedback: 2, MIMO: 1}
code:
  title_pattern: [X-with-Y]
  abstract_moves: [gap, context, aim, method, method, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 12
  intro_moves: [field, prior, prior, prior, gap, tech, prior, aim, approach, approach, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [model, propose, develop, provide, design]
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
  sim_param_table: true        # Table I 模型结构
  baselines_n: 4               # JSCC(+AT)、JPEG + LDPC(+AT)，以及本文的消融版本
  baseline_naming: acronym
  x_axes: [SNR, codebook-size, noise-power, masking-ratio]
  fig1_role: framework
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: digital
  source: [image]
  task: [classification, retrieval, reconstruction]
  paradigm: digital-jscc
  architecture: [transformer, VQ, VAE]
  channel: [MIMO]                # 4×2 MIMO
  adaptivity: [SNR]              # 特征重要性模块（FIM）引入 SNR
  training: [multi-stage, fine-tune]   # 预训练 masked VQ-VAE + 换轻量解码器微调；对抗训练
  metrics: [accuracy, custom]    # 分类精度、检索 recall@1
  datasets: [ImageNet, CIFAR-10]
  baselines: [DeepJSCC, separate, own-ablation]
  snr_mismatch_test: true        # 训练 −3–12 dB，测试 −9–18 dB
  complexity_reported: false
  digital_compatible: true       # 只传码本索引，可直接映射到现有星座
  hardware_validation: false
  theory: none
  idea_delta: [robustness, digitalization, new-component]
  builds_on: [masked autoencoder (MAE), VQ-VAE, adversarial training]
  open_problems_n: 2
---

## 1. 标题
- "Robust Semantic Communications With [方法]"，8 词。卖点（鲁棒性）放在最前。

## 2. 摘要（10 句，213 词）
- 第 1 句就是空白（让步式）："Although semantic communications have exhibited satisfactory performance on a large number of tasks, the impact of semantic noise and the robustness of the systems have not been well investigated." → 定义"语义噪声"→ 本文框架 → 两类噪声 → 对抗训练（权重扰动）→ masked VQ-VAE → 共享离散码本 → 特征重要性模块 → 只传码本索引 → 结果一句。

## 3. 引言逻辑（12 段，A/B/C 三个小节）
- A. 先前工作：语义通信两类（数据重建 / 任务执行）→ "However, there exists a particular type of noise in semantic communications that has not been well studied [8]." → 语义噪声在编码、传输、解码三阶段的来源 → 文本与图像语义噪声的区别（图像可借用对抗样本建模）→ 对抗样本的两类生成方法与防御方法。
- B. 动机与贡献：鲁棒性对自动驾驶、医疗的重要性 → 已有对抗方法未考虑无线信道和传输开销 → 本文方案 → 指出已有方案"全分辨率星座"在数字系统中不可实现，而码本索引可直接映射到现有星座 → 5 条贡献。
- C. 路线图与记号。

## 4. Idea 是怎么提出的
- 空白类型：新问题（语义噪声 / 对抗扰动下的语义通信鲁棒性）+ 实用性（连续值信道符号不兼容数字系统）。
- 核心洞见：离散码本一举两得——离散化本身能吸收小的语义扰动（扰动后的特征仍量化到同一码字），同时只传索引、兼容数字调制并大幅降低开销。
- 把计算机视觉的对抗样本、MAE、VQ-VAE 三个工具组合到通信场景，并补上"信道"这一层（接收端语义噪声的生成不需要 CSI）。

## 5. 科研方法
- 语义噪声建模：发送端样本相关噪声（迭代 FGSM）；接收端样本无关的通用扰动（Algorithm 1）。
- 对抗训练 + 权重扰动的 min-max 问题（Algorithm 2）。
- Masked VQ-VAE（ViT 块、非对称编解码，只编码未遮挡的 patch；遮挡语义噪声高发区域）；共享离散码本 + 增大码字间距的语义相似度损失；码本索引映射到星座。
- 特征重要性模块（FIM）：抑制与噪声相关、与任务无关的特征，引入 SNR。

## 6. 仿真与实验
- 4×2 MIMO；基准 JSCC（ViT 版）与 JPEG + LDPC，各有加 / 不加对抗训练版本。
- 传输开销表（Table II）→ 分类精度 vs SNR / 码本大小 / 语义噪声功率 / 保留比例 / 信号-语义噪声比 → 白盒与黑盒噪声 → 特征激活可视化 → 码字相似度可视化 → 检索与重建。

## 7. 图表
- 11 图 3 表 3 算法。Fig. 2 把 masked VQ-VAE 与"码本抵抗语义噪声"的原理画在一起；Fig. 9–10 用激活频率和相似度热图解释机制。

## 8. 句式库
- 让步式空白（摘要首句）："Although semantic communications have exhibited satisfactory performance on a large number of tasks, the impact of semantic noise and the robustness of the systems have not been well investigated."
- 新问题定义："Semantic noise refers to the misleading between the intended semantic symbols and received ones, thus causes the failure of tasks."
- 指出已有对抗方法的不足："More importantly, the impacts of wireless channels and transmission overhead in communications are usually ignored."
- 数字兼容性论证："However, this is difficult to realize for practical systems due to the finite precision and might be impractical in the current digital communication systems [10], [11], [12]."

## 9. 结论
- 1 段 121 词，现在完成时复述；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：ViT 版 JSCC 与 JPEG + LDPC；工具来自 MAE、VQ-VAE、对抗训练。
- **增量**：提出"语义噪声"模型，并用"遮挡 + 离散码本 + 特征重要性"提升鲁棒性，同时把系统变为只传码本索引的数字系统（robustness + digitalization + new-component）。
- **为什么有效**："The discrete feature representation can combat semantic noise."（扰动被量化吸收）；遮挡减少了被扰动的输入区域。
- **证据**：语义噪声下分类精度明显高于 JSCC(+AT) 与 JPEG + LDPC(+AT)；传输符号数大幅减少（Table II）。
- **弱点**：攻击者知道模型的白盒假设偏强；主要是分类任务，重建质量只做定性展示；没有复杂度与时延；码本索引映射到星座时的误码传播分析较少。
- **开放问题**：
  - 推断：文本、语音等其他模态的语义噪声；码本索引的信道编码与不等错误保护；黑盒 / 物理层攻击（后续 jsac.2023.3288249）；码本大小、调制阶数与信道质量的联合自适应（后续数字 JSCC 系列）。
