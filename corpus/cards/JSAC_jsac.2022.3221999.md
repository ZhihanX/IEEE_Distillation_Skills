---
doi: 10.1109/jsac.2022.3221999
title: "Toward Semantic Communications: Deep Learning-Based Image Semantic Coding"
journal: JSAC
year: 2023
band: 2022-2025
cites: 345
cites_per_year: 91.8
article_type: research
topic: semantic
source: xplore-html
xplore: 9953076
auto:
  words_total: 8348
  n_sections: 5
  n_subsections: 22
  n_figures: 12
  n_tables: 2
  n_display_eq: 31
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 24.2
  we_per_1k: 10.4
  title_words: 8
  abstract_words: 227
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 0, however: 11, transition: 12, resultsShow: 1, motivatedBy: 1, toAddress: 3, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 6, intensifier: 6, worthNoting: 0, observe: 4, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 3, figVerb: 1, promising: 1, gen: 0, contrast: 2, firstTime: 0, novel: 9, weProposeFirst: 11, wlog: 0, code: 0, prototype: 0}
  # roadmap 0 是因为原文写 "The rest of this work is organized as follows."（旧正则未覆盖 work），实际有路线图
  methods: {DRL: 6, DNN: 2, monteCarlo: 1}
code:
  title_pattern: [toward, colon-subtitle]
  abstract_moves: [context, prior, aim, method, method, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 9
  intro_moves: [field, prior, gap, prior, gap, prior, gap, solution, aim, contrib, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [propose, propose, propose]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: none
  gap_type: [new-scenario, limitation]
  motivating_figure: true
  problem_class: learning
  solution: [DRL, DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 6
  baseline_naming: acronym
  x_axes: [bitrate, SNR, visual-examples]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: image-jscc
  source: [image]
  task: [reconstruction, segmentation]
  paradigm: separate-learned               # 语义概念编码 + 软量化 + 熵编码，再经信道
  architecture: [CNN, GAN, RL]
  channel: [AWGN]
  adaptivity: [content]                    # RL 为每个语义概念选量化等级
  training: [multi-stage, RL]
  metrics: [mIoU, FID, KID, PSNR, SSIM]
  datasets: [Cityscapes]
  baselines: [separate, other-learned]
  snr_mismatch_test: false
  complexity_reported: false
  digital_compatible: true
  hardware_validation: false
  theory: none
  idea_delta: [new-metric, generative-prior, new-component]
  builds_on: [learned image compression, GAN-based compression (HiFiC / DSSLIC), reinforcement learning bit allocation]
  open_problems_n: 0
---

## 1. 标题
- "Toward [新范式]: [方法]-Based [对象] [任务]"，8 词。"Toward …" 开头表达"迈向某范式的一步"，冒号后说明具体做的是图像语义编码。

## 2. 摘要（10 句，227 词）
- 第 1 句语义通信价值；第 2 句已有工作集中在文本（"Most existing works explore the semantic encoding and transmission for text …"）。
- "In this paper, we conceive the semantic communications for image data that is much more richer in semantics and bandwidth sensitive."——锚点句同时给出换模态的理由。
- 方法名（RL-ASC）+ "Firstly / Secondly / Thirdly / Finally" 四个组件（语义概念表示、语义-感知重建准则、RL 比特分配、GAN 解码器），中间插一句效果解释（"Thus, the task-related information is preserved …"）。
- 末句实验结论无数字。

## 3. 引言逻辑（9 段，约 1040 词）
1. 从 1949 年 Weaver 的通信三层次讲起 → 深度学习使语义层可行（与 DeepSC-S 同样的"理论溯源"开场）。
2. 已有语义通信集中于文本 / 语音。
3. "Actually, the vision modal is more informative than text modal, and the video/image traffic accounts for 75% of IP traffic nowadays [8]." → 图像语义通信更重要。
4. 早期图像 JSCC 工作逐篇。
5. "However, the aforementioned works lack the interpretation ability of the image content." → 像素级率失真优化的问题（伪影伤害下游任务）→ "Therefore, blindly minimizing pixel-wise distortion may bring unnecessary bit overhead."
6. 以语义相似度为准则的初步工作逐篇，每篇一个 "However, …" 局限。
7. "Moreover, all of the above methods cannot meet the semantic and perception performance requirements jointly in low bit rate." → RL 与 GAN 各自为何合适 → 直接用朴素 GAN 不可行。
8. "In this paper, we propose …" + 3 条 bullet 贡献（均以 "We propose" 开头）。
9. 路线图（"The rest of this work is organized as follows."）。

## 4. Idea 是怎么提出的
- 空白类型：新场景（从文本模态到图像模态）+ 已有方法局限（像素级重建准则与语义任务不匹配）。
- 写法亮点：用一个统计数字（图像 / 视频占 IP 流量 75%）论证换模态的重要性；把"重建准则从像素到语义—感知"作为核心转变，并在方法节小标题里直接写成 "From Pixel to Semantic Concept"、"From Pixel Loss to Semantic-Perceptual Loss"。
- 每种借用工具都先说"为什么合适"，再说"为什么不能直接用"（RL 适合离散量化选择；朴素 GAN 会偏离输入细节）。

## 5. 科研方法
- 系统（Fig. 1）：语义编码器（按类别提取"语义概念"）→ RL 智能体为每个概念选量化等级 → 软量化 + 熵编码 → 生成式语义解码器（局部生成器 + 全局生成器 + 注意力融合）+ 多尺度判别器。
- 重建准则：率—语义—感知三方权衡（分割损失 + 感知损失 + 码率）；语义指标不可微 → 用 RL 处理。
- RL：MDP 状态 / 动作 / 奖励（编码某概念后率—语义—感知性能的提升）。
- 三阶段训练（编解码器 → RL 比特分配 → 整体微调），各写成算法。无定理。

## 6. 仿真与实验
- 节名 "Experimental Results"；Setup 分 Datasets（Cityscapes）、Baselines（BPG、JPEG2000、JPEG、DSSLIC、HiFiC，并为公平起见微调 DSSLIC）、Evaluation Metrics（mIoU、FID、KID，并解释为何 PSNR/SSIM 不够）、Compression Modes（三种码率 + 去掉 RL 的消融版本）。
- 语义性能（客观 + 主观可视化）→ 感知性能（客观 + 主观）→ 率失真（坦承在 PSNR/SSIM 上不如基准："the baselines achieve better performance since they are optimized with the PSNR or SSIM metric"）→ AWGN 抗噪。
- 公平性说明："… the proposed RL-ASC encodes the image at a bitrate 0.33 bpp while the baselines encode the image at a bitrate equal to or higher than 0.33 bpp."
- 借鉴 BD-rate 提出 BD-mIoU 指标（Table II）。

## 7. 图表
- 12 图 2 表 2 算法。Fig. 1 系统框架，Fig. 2–4 网络结构图。结果图 caption 写明指标方向（"The higher value means better performance."），可视化图 caption 说明样本如何选取（"two randomly selected input image"）。

## 8. 句式库
- 理论溯源："Dating back to 1949, Weaver [1] defined three levels of communications: the bit level, the semantic level, and the effective level."
- 统计数字论证重要性："Actually, the vision modal is more informative than text modal, and the video/image traffic accounts for 75% of IP traffic nowadays [8]."
- 已有工作共同缺陷："However, the aforementioned works lack the interpretation ability of the image content."
- 批评旧准则："Therefore, blindly minimizing pixel-wise distortion may bring unnecessary bit overhead."
- 工具不可直接用："However, it is not feasible to directly adopt the naive GANs for image semantic decoding, since …"
- 坦承劣势并解释："As shown in Fig. 11, the baselines achieve better performance since they are optimized with the PSNR or SSIM metric."

## 9. 结论
- 1 段 215 词，过去时复述各组件 → "FID, KID, and mIoU can be valuable tools to better predict human preferences …"（对评价指标的结论）→ 抗噪。无数字、无未来工作。

## 10. Idea 拆解
- **基线**：像素级率失真优化的学习型 / 传统图像压缩（BPG、JPEG2000、HiFiC、DSSLIC）；以文本为主的语义通信。
- **增量**：把重建准则从像素失真改为"率—语义—感知"三方权衡，按语义概念用 RL 分配比特，并用 GAN 解码器保证感知质量（new-metric + generative-prior + new-component）。
- **为什么有效**："Therefore, blindly minimizing pixel-wise distortion may bring unnecessary bit overhead."——按语义重要性分配比特，把码率花在对下游任务（分割）有用的区域。
- **证据**：同等或更低 bpp 下 mIoU、FID、KID 优于基准；提出 BD-mIoU 汇总增益；AWGN 下有一定抗噪性。
- **弱点**：PSNR / SSIM 不如基准（论文坦承）；只有 Cityscapes 一个数据集；信道部分较弱（主要是信源编码）；RL 训练复杂；无复杂度与未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：语义—感知准则下的联合信源信道编码（端到端过信道训练）；扩散模型替代 GAN；语义概念的不等错误保护；通用场景（非街景）上的语义概念定义。
