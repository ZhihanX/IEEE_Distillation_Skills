---
doi: 10.1109/tcomm.2024.3364990
title: "A Unified Multi-Task Semantic Communication System for Multimodal Data"
journal: TCOM
year: 2024
band: 2022-2025
cites: 216
cites_per_year: 95.6
article_type: research
topic: semantic
source: xplore-html
xplore: 10431795
auto:
  words_total: 7761
  n_sections: 8
  n_subsections: 25
  n_figures: 10
  n_tables: 3
  n_display_eq: 32
  n_algorithms: 1
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 22.1
  we_per_1k: 13.1
  title_words: 9
  abstract_words: 208
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 2, contribList: 1, roadmap: 1, however: 6, transition: 24, resultsShow: 2, motivatedBy: 1, toAddress: 6, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 2, intensifier: 6, worthNoting: 1, observe: 3, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 1, promising: 1, gen: 0, contrast: 7, firstTime: 2, novel: 2, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  methods: {DNN: 2}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, gap, aim, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 10
  intro_moves: [field, prior, prior, gap, tech, gap, aim, approach, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, design, develop, devise]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [unification, practicality]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 3
  baseline_naming: acronym
  x_axes: [SNR, transmitted-symbols, feature-visualization]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: task-multiuser
  source: [image, text, speech]
  task: [classification, VQA, sentiment, reconstruction]
  paradigm: task-feature
  architecture: [transformer, VQ]
  channel: [AWGN, Rayleigh]
  adaptivity: [task, SNR, bandwidth-rate]  # 任务嵌入 + FSM 按任务 / 信道调整符号数
  training: [multi-stage]
  metrics: [accuracy, PSNR, BLEU]
  datasets: [CIFAR-10, SST-2, VQAv2, CMU-MOSEI, Europarl]
  baselines: [separate, own-ablation]
  snr_mismatch_test: false
  complexity_reported: true                # 参数量 42.85M vs 153.67M
  digital_compatible: true                 # 统一码本只传索引
  hardware_validation: false
  theory: none
  idea_delta: [new-task, digitalization, adaptivity]
  builds_on: [DeepSC, multi-task learning, VQ-VAE codebook (twc.2023.3265201)]
  open_problems_n: 0
---

## 1. 标题
- "A Unified [多任务] [系统] for [多模态数据]"，9 词。"Unified"、"Multi-Task"、"Multimodal" 三个修饰词把与已有单任务系统的区别全部放进标题。

## 2. 摘要（8 句，208 词）
- 第 1 句肯定已有成果（"Task-oriented semantic communications have achieved significant performance gains."）→ 第 2 句 "However, the employed deep neural networks … have to be updated when the task is changed or multiple models need to be stored …"
- "To address this issue, we develop a unified deep learning-enabled semantic communication system (U-DeepSC), …"——we 主语锚点 + 系统命名（延续 DeepSC 系列）。
- 四个组件：向量级动态方案（按任务调符号数）→ 随信道调整 → 轻量 FSM（分层丢弃冗余特征、加速推理）→ 统一码本（只传索引）。
- 末句结果：与单任务系统性能相当，但传输开销与模型尺寸显著减少。无数字。

## 3. 引言逻辑（10 段，约 1420 词；内分 A. Prior Work / B. Motivation and Contributions / C. Organization and Notations）
1. AI 应用 → 有限无线资源 → 语义通信。
2. （A）语义通信只传与任务相关的信息 → DL 带来的增益。
3. 已有工作二分：数据重建 / 任务执行，逐篇。
4. "Though the aforementioned semantic communication systems have exhibited satisfactory performance in certain scenarios, they only handle one task with single modality of data." → 两点实际困难 (i) 换任务就要重训、(ii) 多模型存储不现实 → 少数多任务尝试的局限。
5. CV/NLP 中的多任务学习及两点好处（存储共享、相关任务互补）+ 多模态表示学习。
6. （B）统一多任务模型"has not been thoroughly investigated" → 首创声明 → 第二个问题：不同任务所需特征数不同 → 固定输出尺寸造成冗余 → 需要按任务确定传输速率。
7. "To this end, we make the first attempt to …"：六个任务、三种模态、任务嵌入向量、动态信道编码器与 FSM、借用 [23] 的码本并扩展为统一码本（"Different from [23] where the codebook is for a specific task with single modality, …"）、统一解码器 + 掩码交叉注意力；结果预告。
8. "Specifically, the main contributions of this paper can be summarized as follows." + 4 条 bullet。
9. 路线图；10. Notations（并有 Table I 记号表）。

## 4. Idea 是怎么提出的
- 空白类型：统一（一个模型服务多任务多模态）+ 实用性（重训的梯度传输开销、边缘设备存储有限）。
- 写法亮点：用编号 (i)(ii) 列出"单任务模型在实践中的两个问题"，再用编号 (i)(ii) 列出"多任务学习的两个好处"，两组对称的理由支撑统一化动机。
- 第二层创新（动态传输开销）由"不同任务需要的特征数不同"这一观察自然引出，并给出具体例子（重建任务比推理任务需要更多特征）。

## 5. 科研方法
- 系统（Fig. 1）：图像 / 文本 / 语音三个语义编码器（Transformer）+ 信道编码器 → 统一的信道 / 语义解码器 + 轻量任务头；六个任务各自的指标与损失用编号列表定义（文本分类、VQA、视频情感、图像分类、图像重建、文本重建）。
- FSM：选择掩码向量 → Gumbel-Softmax 可微采样 → 按信道噪声设置目标保留比例 → 训练时不丢、推理时丢（掩码交叉注意力实现并行训练）。
- 统一码本（VQ-VAE 机制）实现数字传输；两阶段训练（先联合训练、后整体微调，Algorithm 1）。无定理。

## 6. 仿真与实验
- 训练超参数写在正文（AdamW、学习率、批大小，并说明调参发现）。
- 基准：传统分离编码（JPEG + LDPC 等）、T-DeepSC（同结构单任务分别训练）、上界（无噪特征）。
- 六任务性能 vs SNR（AWGN / Rayleigh）→ FSM 有效性（符号数与归一化性能损失、特征可视化、与随机选择比较）→ 参数量（Table III：42.85M vs 153.67M，仅为 28.54%）。

## 7. 图表
- 10 图 3 表 1 算法。Fig. 1 框架，Fig. 2 发射机结构（caption 很长，解释任务嵌入向量），Fig. 3 FSM，Fig. 4 统一码本，Fig. 5 接收机。结果 caption 描述型（列出六个任务与训练 SNR）。

## 8. 句式库
- 肯定后转折："Though the aforementioned semantic communication systems have exhibited satisfactory performance in certain scenarios, they only handle one task with single modality of data."
- 编号列出实际困难："These DNN models are hard to simultaneously serve different tasks with multi-modality in practice for the reasons below: (i) …; (ii) …"
- 未充分研究："Though there have been numerous semantic works for specific tasks, a unified multi-task model for different modalities of data in wireless communications has not been thoroughly investigated."
- 首创："To the best of our knowledge, this is the first work on a unified semantic communication system designed to serve various tasks."
- 内在权衡："Consequently, an inherent trade-off between performance and the number of transmitted symbols exists."
- 借用并区分："Different from [23] where the codebook is for a specific task with single modality, we design a unified codebook for multimodal data."

## 9. 结论
- 1 段 114 词，过去时复述（proposed / considered / developed / has been proposed）→ 结果定性（低 SNR 表现、与单任务相当、开销与模型尺寸减少）。无数字、无未来工作。

## 10. Idea 拆解
- **基线**：单任务单模态语义通信（T-DeepSC，同结构分别训练）；VQ-VAE 码本语义通信（twc.2023.3265201，单任务）；多任务学习。
- **增量**：一个统一模型服务六个任务、三种模态，任务嵌入 + 特征选择模块按任务与信道动态调整传输符号数，统一码本实现数字传输（new-task + digitalization + adaptivity）。
- **为什么有效**："Consequently, an inherent trade-off between performance and the number of transmitted symbols exists."——不同任务所需特征数不同，按任务丢弃冗余特征即可省带宽；多任务共享参数节省存储。
- **证据**：各任务性能与单任务模型相当；参数量仅为后者的 28.54%；FSM 在性能损失很小时显著减少符号数。
- **弱点**：任务集合固定，新增任务仍需训练；数据集多为小规模基准；码本索引的信道编码与误码影响分析有限；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：新任务的增量 / 持续学习（不遗忘）；基础模型作为统一语义编解码器；多用户场景下的统一多任务系统；码本大小与调制阶数的联合自适应。
