---
doi: 10.1109/twc.2024.3369170
title: "Privacy-Preserving Task-Oriented Semantic Communications Against Model Inversion Attacks"
journal: TWC
year: 2024
band: 2022-2025
cites: 73
cites_per_year: 33.6
article_type: research
topic: semantic
source: xplore-html
xplore: 10458014
auto:
  words_total: 5883
  n_sections: 5
  n_subsections: 22
  n_figures: 15
  n_tables: 3
  n_display_eq: 44
  n_algorithms: 4
  statements: {theorem: 0, lemma: 0, proposition: 1, corollary: 0, assumption: 4, remark: 1, proof: 2, proof_in_appendix: 1}
  n_appendix: 3
  mean_sentence_words: 20.6
  we_per_1k: 15.4
  title_words: 8
  abstract_words: 200
  abstract_sentences: 9
  phrases: {toTheBest: 1, inThisPaper: 9, contribList: 1, roadmap: 1, however: 6, transition: 8, resultsShow: 3, motivatedBy: 3, toAddress: 4, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 2, intensifier: 10, worthNoting: 0, observe: 6, thisIsBecause: 1, asExpected: 0, insight: 0, tradeoff: 6, figVerb: 5, promising: 1, gen: 3, contrast: 3, firstTime: 0, novel: 0, weProposeFirst: 4, wlog: 0, code: 0, prototype: 0}
  methods: {convergence: 5, DNN: 2, KKT: 2, complexity: 2, monteCarlo: 1}
  domain: {accuracy: 22, SSIM: 12, MNIST: 8, CIFAR: 7, complexityCost: 7, PSNR: 6, IB: 5, Rayleigh: 5, AWGN: 4, ImageNet: 2, SNRmismatch: 2}
code:
  title_pattern: [X-against-Y]
  abstract_moves: [context, context, gap, aim, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 7
  intro_moves: [field, scenario-gap, prior-gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, convert, propose, evaluate]
  contrib_quantified: false
  first_claim: true                     # "there hardly exists any work addressing privacy issues in task-oriented semantic communications"
  roadmap: true
  notation: intro-end
  gap_type: [security, new-scenario]
  motivating_figure: true               # Fig. 2 模型反演攻击示意
  problem_class: learning
  solution: [DNN, bound-surrogate, adversarial-training, multi-objective]   # VIB 上界 + 对抗学习 + MGDA
  theory_role: supporting               # Proposition 1 收敛性
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true                 # Table I–III 网络结构
  baselines_n: 3                        # NECST-G、NECST-G-DP（多个隐私预算）、ESCS（加密语义通信）
  baseline_naming: acronym
  x_axes: [SNR, latency, sparsity]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: theory-security
  source: [image]
  task: [classification]
  paradigm: task-feature
  architecture: [CNN]
  channel: [AWGN, Rayleigh]
  adaptivity: [SNR]                     # IBAL-D：按信道条件用 MGDA 自适应调整隐私-效用权重
  training: [adversarial-training, multi-objective]
  metrics: [accuracy, custom]           # 攻击者重建的 SSIM / PSNR（越低越好）
  datasets: [MNIST, CIFAR-10, ImageNet]
  baselines: [other-learned]
  snr_mismatch_test: true               # 快变信道、过期 CSI
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: information-bottleneck
  idea_delta: [security-privacy, adaptivity]
  builds_on: [jsac.2021.3126087 (VIB task-oriented), adversarial learning against model inversion, MGDA, NECST]
  open_problems_n: 0
---

## 1. 标题
- "Privacy-Preserving [范式] Against [攻击]"，8 词。"X Against Y" 是安全类论文的标题模式。

## 2. 摘要（9 句，200 词）
- 两句背景（6G 核心技术、任务导向低时延推理）→ 让步式空白："Although transmitting only task-related information does protect a certain level of user privacy, adversaries could apply model inversion techniques to reconstruct the raw data or extract useful information …" → IBAL → 三句方法（IB、变分上界、对抗学习最大化重建失真）→ 自适应权重 → 结果。

## 3. 引言逻辑（7 段）
- DL 通信 → 自动驾驶等应用对时延的要求 → 任务导向语义通信 → 只传任务特征"在一定程度上"保护隐私，但模型反演仍可恢复原始数据 → 首创声明 → 传统隐私方法（k-匿名、l-多样性、t-接近）不适合高维数据、难以接入端到端训练、差分隐私损伤性能 → 本文 IBAL（IB + 对抗学习；选择"最大化失真"的理由：发送端不知道攻击者意图）→ 贡献 → 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：安全（任务导向特征仍可被反演）+ 新场景。
- 核心洞见：IB 已经压掉了与任务无关的信息，再加一个"模拟攻击者"的解码器，训练编码器使攻击者的重建失真最大——把隐私保护变成发送端编码器与攻击者之间的博弈；隐私-效用权重随信道变化，因此用多目标优化（MGDA）自动找 Pareto 驻点而非手调权重。
- 写法亮点：把方法拆成 Problem 1/2/3（如何算 IB 损失、如何训练整个系统、如何按信道调权重），逐个回答。

## 5. 科研方法
- 系统：特征提取器 + JSC 编码器 → 信道 → 任务推理模块；攻击者用模型反演网络从截获特征重建图像（Table III）。
- 目标：min (1−λ)·L_IB − λ·重建失真；VIB 上界（重参数化 + Monte Carlo）。
- IBAL：交替训练——固定发送端训练解码器（攻击者代理），再固定解码器训练发送端与推理模块（Algorithm 1）。
- IBAL-D：多目标优化 + MGDA 求 Pareto 驻点（KKT 条件），自适应 λ（Algorithm 2）；Proposition 1 收敛性（四个假设）。

## 6. 仿真与实验
- MNIST、CIFAR-10，补充 ImageNet2012（经数据适配网络）；AWGN、Rayleigh。
- 基准：NECST-G、NECST-G-DP（隐私预算 0.9 / 0.1 / 0.05）、ESCS（加密语义通信）。
- 精度 vs SNR 与攻击者 SSIM vs SNR → 重建可视化 → 不同时延 → 动态信道 IBAL-D vs IBAL-D-NO → 快变信道 → 稀疏源数据 → 大规模数据集 → 与加密结合。

## 7. 图表
- 15 图 3 表 4 算法。Fig. 1–2 并列"正常系统"与"模型反演攻击"（颜色区分发送端 / 接收端 / 攻击者）；Fig. 5、8 用攻击者重建的图像直观展示隐私效果；Fig. 14 与加密结合的框架。

## 8. 句式库
- 让步式空白（摘要）："Although transmitting only task-related information does protect a certain level of user privacy, adversaries could apply model inversion techniques to reconstruct the raw data or extract useful information …"
- 首创性："To our best knowledge, there hardly exists any work addressing privacy issues in task-oriented semantic communications."
- 传统方法不适用："Directly transplanting existing privacy methods into semantic communication systems may result in the inability to train the semantic communication system."
- 设计选择的理由："The reason why we choose to maximize distortion is that the transmitter may not know the specific intentions of adversaries in advance."
- 与差分隐私的对比："Compared with the DP approach, our approach does not cause a significant negative impact on task performance."

## 9. 结论
- 1 段 177 词，现在完成时复述；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：VIB 任务导向通信（jsac.2021.3126087）；NECST + 差分隐私；加密语义通信 ESCS。
- **增量**：在任务导向语义通信中加入对模型反演攻击的对抗训练，并用多目标优化按信道自适应平衡隐私与效用（security-privacy + adaptivity）。
- **为什么有效**：编码器被显式训练成让代理攻击者重建失真最大，同时 IB 约束保证任务所需信息保留；MGDA 避免了手调权重在不同 SNR 下失衡。
- **证据**：攻击者 SSIM / PSNR 最低，而分类精度仅略低于不设防的 NECST-G；隐私效果与 DP（预算 0.05）相当但精度明显更高。
- **弱点**：防御只针对训练时的代理攻击者结构，对更强 / 不同结构的攻击者无保证；隐私度量用 SSIM / PSNR（非形式化隐私定义）；小图分类任务；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：可证明的隐私保证（信息论隐私泄露界，如 I(S; Ẑ) 上界）；生成式攻击者（扩散模型反演）下的鲁棒性；窃听信道下语义安全（物理层安全 + 语义）；多用户、联邦训练中的隐私；与 jsac.2023.3288249 的对抗鲁棒性统一框架。
