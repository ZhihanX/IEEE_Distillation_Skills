---
doi: 10.1109/jsac.2022.3221991
title: "Deep Learning-Enabled Semantic Communication Systems With Task-Unaware Transmitter and Dynamic Data"
journal: JSAC
year: 2023
band: 2022-2025
cites: 259
cites_per_year: 68.9
article_type: research
topic: semantic
source: xplore-html
xplore: 9953099
auto:
  words_total: 9635
  n_sections: 7
  n_subsections: 14
  n_figures: 14
  n_tables: 0
  n_display_eq: 15
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, definition: 4, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.3
  we_per_1k: 7.2
  title_words: 11
  abstract_words: 198
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 11, contribList: 1, roadmap: 1, however: 8, transition: 13, resultsShow: 2, motivatedBy: 1, toAddress: 7, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 4, intensifier: 2, worthNoting: 0, observe: 13, thisIsBecause: 4, asExpected: 0, insight: 0, tradeoff: 5, figVerb: 12, promising: 1, gen: 1, contrast: 2, firstTime: 1, novel: 1, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  methods: {DNN: 12, convergence: 8, complexity: 2}
  domain: {accuracy: 23, JPEG2000: 21, PSNR: 15, MNIST: 11, VAE: 10, CIFAR: 9, feedback: 7, GAN: 6, CNN: 5, knowledgeBase: 3, AWGN: 2}
code:
  title_pattern: [X-with-Y]
  abstract_moves: [context, gap, gap, aim, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 11
  intro_moves: [field, prior, gap, gap, aim, approach, contrib, contrib, contrib, result, roadmap]
  related_work: separate-section
  contrib_format: paragraph               # "three-folded"，First / Second / The third 分段
  contrib_n: 3
  contrib_verbs: [propose, propose, introduce]
  contrib_quantified: false
  first_claim: true                       # 结论 "This paper is the first work addressing …"
  roadmap: true
  notation: none
  gap_type: [practicality, new-assumption]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: supporting                 # HΔH 散度 / PAD 刻画数据集相似度
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4                          # VAE 方法、JPEG2000 方法；DA 部分：不适配、完全重训
  baseline_naming: descriptive
  x_axes: [compression-ratio, epochs]
  fig1_role: framework
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: task-multiuser
  source: [image]
  task: [classification, segmentation, reconstruction]
  paradigm: task-feature
  architecture: [MLP, CNN, GAN]           # 语义编码网络（无激活函数的线性层）+ CycleGAN 数据适配
  channel: [AWGN]
  adaptivity: [domain]                    # 数据分布变化（MNIST→SVHN/USPS、CIFAR10→STL10）
  training: [receiver-led, two-stage, domain-adaptation]
  metrics: [accuracy, PSNR, IoU]
  datasets: [MNIST, CIFAR-10, PASCAL-VOC2012, SVHN, USPS, STL-10]
  baselines: [separate, other-learned, own-ablation]
  snr_mismatch_test: false
  complexity_reported: false
  digital_compatible: false
  hardware_validation: false
  theory: other                           # 域适应界（HΔH 散度）
  idea_delta: [new-task, robustness, knowledge-base]
  builds_on: [DeepSC transfer learning, CycleGAN domain adaptation, semantic information theory]
  open_problems_n: 2
---

## 1. 标题
- "Deep Learning-Enabled Semantic Communication Systems With [约束 1] and [约束 2]"，11 词。标题直接列出两个"放松的假设"。

## 2. 摘要（8 句，198 词）
- 现有系统依赖收发双方共享背景知识 → 两个"In practice"式空白（语义由接收端任务定义、发送端不知道；实际数据分布与知识库不同）→ 本文 → 两部分（SC 网络、DA 网络）→ 各一句机理 → 结果一句。

## 3. 引言逻辑（11 段）
- 6G 原生智能 → 语义通信 → 已有 DL 系统的共同框架（共享知识库）→ "However, it is worthwhile to mention that in many practical scenarios, the original setup of fully shared background knowledge with complete observable and semantic information does not stand for granted." → 接收端回传全部语义信息的代价与隐私问题 → 数据分布变化与重训成本 → 本文（两阶段训练、两大挑战）→ 三段式贡献（First / Second / The third）→ 实验结论段 → 路线图。

## 4. Idea 是怎么提出的
- 空白类型：实用性 + 放松假设（"收发双方都知道任务""训练 / 测试同分布"这两个隐含假设在实际中不成立）。
- 核心洞见一：接收端主导训练——接收端只回传损失对接收信号的梯度 ∇_Y L 与 Y，发送端据此更新编码器，从而"不告诉发送端任务是什么"也能端到端训练（附带弱隐私）。
- 核心洞见二：数据分布变化时不重训编解码器，而在发送端用 CycleGAN 把新数据"翻译"成知识库数据的样子（只需发送端本地训练、无通信开销）。
- 写法亮点：把"不平等参与者"（接收端资源和权限更多）作为系统设定明确写出。

## 5. 科研方法
- 语义编码网络：编码器 f、解码器 g、接收端固定的任务函数 φ；损失 = λ·观测失真 + 语用失真（按任务输出是离散还是连续分两类，Definition 1–3，含"弹性"权衡超参数 λ_s）；Algorithm 1 接收端主导训练。
- 数据适配网络：CycleGAN（对抗损失 + 循环一致损失）把观测数据 S 转换为库数据 K 的形式；HΔH 散度 / PAD 刻画两数据集相似度，预测适配效果。

## 6. 仿真与实验
- AWGN，SNR = 3 / 10 dB；MNIST 识别、CIFAR-10 分类、PASCAL-VOC2012 分割；基准 VAE 方法与 JPEG2000 方法。
- 精度 / IoU / PSNR vs 压缩率 → 可视化 → DA：SVHN / USPS → MNIST、STL10 → CIFAR10，对比"不适配"与"完全重训"。
- 坦白：PSNR 上无优势（JPEG2000 在多数压缩率下 PSNR 更好）；优势只在低压缩率的任务性能上。

## 7. 图表
- 14 图 0 表 2 算法。Fig. 1–3 系统、语义编码、数据适配三张结构图；caption 均为短标签。

## 8. 句式库
- 挑战共享知识假设："However, it is worthwhile to mention that in many practical scenarios, the original setup of fully shared background knowledge with complete observable and semantic information does not stand for granted."
- 语义由任务定义："We would like to emphasize that semantic information is determined by specific tasks, instead of being an intrinsic feature of the source."
- 指出被忽视的问题："Since the pragmatic task is typically unknown to the transmitter, the implementation of the training process at the transmitter and the receiver, which has been overlooked in many …"
- 首创性（结论）："This paper is the first work addressing the applicability of semantic or task-oriented communication in practical scenarios with unequal participants and varying data environments."
- 首创性（知识库层级）："To our best knowledge, a knowledge base with different access levels has not been considered in the existing literature on semantic communications."

## 9. 结论
- 2 段：复述 → 首创声明 + 未来问题（最小通信代价协调训练；时变信道）+ 部署愿景（IoT、无人机）。

## 10. Idea 拆解
- **基线**：共享知识库的 DL 语义通信（DeepSC tsp.2021.3071210 等）；DeepSC 的迁移学习重训。
- **增量**：放松"发送端知道任务"与"同分布"两个假设——接收端主导的梯度回传训练 + 发送端本地域适应（new-task + robustness + knowledge-base）。
- **为什么有效**：发送端只需要损失对其输出的梯度即可更新，无需知道任务；CycleGAN 让编码器面对的输入分布不变，因此不用重训。
- **证据**：低压缩率下任务性能优于 VAE / JPEG2000；DA 后接近完全重训（CIFAR10→STL10 在 80 轮内仅差 5%），远好于不适配。
- **弱点**：训练期的梯度回传通信开销只定性讨论；"弱隐私"未量化（梯度可能泄露任务）；只有 AWGN；编码器为无激活的线性层，表达力弱；PSNR 劣于 JPEG2000；DA 依赖两数据集足够相似。
- **开放问题**：
  - "There are many interesting problems to further investigate in the future, such as how to coordinate the training of semantic encoder and decoder with minimum communication cost, how …"
  - 推断：梯度回传的隐私泄露分析（与 twc.2024.3369170 的模型反演攻击相关）；多接收端多任务下的接收端主导训练；在线 / 持续学习应对数据漂移；知识库失配的理论刻画。
