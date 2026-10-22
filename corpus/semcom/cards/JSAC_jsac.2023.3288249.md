---
doi: 10.1109/jsac.2023.3288249
title: "Physical-Layer Adversarial Robustness for Deep Learning-Based Semantic Communications"
journal: JSAC
year: 2023
band: 2022-2025
cites: 92
cites_per_year: 29.0
article_type: research
topic: semantic
source: xplore-html
xplore: 10159517
auto:
  words_total: 7310
  n_sections: 6
  n_subsections: 49
  n_figures: 10
  n_tables: 4
  n_display_eq: 18
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 22.4
  we_per_1k: 18.8
  title_words: 8
  abstract_words: 259
  abstract_sentences: 10
  phrases: {toTheBest: 1, inThisPaper: 2, contribList: 1, roadmap: 1, however: 9, transition: 1, resultsShow: 1, motivatedBy: 1, toAddress: 0, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 0, intensifier: 4, worthNoting: 1, observe: 6, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 3, figVerb: 0, promising: 0, gen: 0, contrast: 5, firstTime: 0, novel: 8, weProposeFirst: 3, wlog: 2, code: 0, prototype: 0}
  methods: {DNN: 9, complexity: 6}
  domain: {OFDM: 20, PSNR: 19, SSIM: 18, CIFAR: 12, accuracy: 11, MNIST: 8, QAM: 6, LDPC: 5, Rayleigh: 4, ImageNet: 3}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, argue, gap, question, question, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb             # "We argue that …"
  intro_paragraphs: 14
  intro_moves: [field, tech, motivation, gap, gap, criteria, approach, approach, approach, contrib, prior, prior, prior, roadmap]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [present, introduce, propose, conduct]
  contrib_quantified: true              # SemBlock 参数减少约 40% / 64%
  first_claim: true                     # "To the best of our knowledge, the physical-layer adversarial robustness … is still largely underexplored."
  roadmap: true
  notation: table                       # Table I
  gap_type: [security, practicality]
  motivating_figure: true               # Fig. 3 把"汽车"误导为"鸟"
  problem_class: learning
  solution: [DNN, adversarial-training]
  theory_role: none
  proofs_location: none
  complexity_analysis: true             # 参数量与推理时间（Table III）
  convergence_analysis: false
  sim_param_table: true                 # Table II
  baselines_n: 3                        # 干扰攻击、PGD、PGM（攻击基准）；1/2 LDPC + QPSK / 16QAM（系统对比）
  baseline_naming: acronym
  x_axes: [class-index, PSR, SNR]
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
  task: [classification, reconstruction]
  paradigm: analog-jscc
  architecture: [CNN]                   # 轻量 SemBlock（深度可分离卷积，MobileNet V2 风格）
  channel: [OFDM, AWGN, Rayleigh]
  adaptivity: [none]
  training: [end-to-end, adversarial-training]
  metrics: [accuracy, PSNR, SSIM, custom]   # 误导率（misleading rate）
  datasets: [MNIST, CIFAR-10, ImageNet]
  baselines: [separate, other-learned]
  snr_mismatch_test: false
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [security-privacy, robustness, new-metric]
  builds_on: [PGM universal perturbation for E2E comm, adversarial training, MobileNet V2, DeepJSCC]
  open_problems_n: 1
---

## 1. 标题
- "Physical-Layer Adversarial Robustness for Deep Learning-Based Semantic Communications"，8 词。

## 2. 摘要（10 句，259 词）
- 背景 → 立场句（"We argue that central to the success of ESC is the robust interpretation of conveyed semantics at the receiver side …"）→ 空白（无线信道开放 + 神经网络脆弱）→ 两个问题 Q1（攻击）、Q2（防御）→ MobileSC → SemAdv 回答 Q1 → SemMixed 回答 Q2 → 实验 → "有趣发现"（低 SNR 下 MobileSC 甚至比传统块式系统更鲁棒）。

## 3. 引言逻辑（14 段，A–F 小节）
- A 背景：ITU 流量预测、ESC 与 Weaver 问题。
- B 动机：ESC 的目标是正确理解 → 鲁棒解释是核心 → DNN 对小扰动脆弱 → 视觉对抗训练不能直接搬（时变信道；攻击加在信号而非输入）→ 已有通用扰动方法（PGM）针对内容、不针对语义 → [27] 只在输入端加语义噪声 → 首创性声明。
- C 方法：四条攻击准则（语义导向、不可察觉、与输入无关、可控）→ MobileSC → SemAdv 如何满足四准则 → SemMixed。
- D 贡献 → E 相关工作三个方面 → F 路线图 + 记号表。

## 4. Idea 是怎么提出的
- 空白类型：安全（物理层对抗攻击下的语义鲁棒性）+ 实用性（攻击应在空中信号上、且攻击者不知道输入）。
- 核心洞见：语义通信的安全威胁不同于比特通信——攻击者可以只针对某一类语义（如"汽车"）在空中注入类噪声的扰动，让接收端误判而其他类几乎不受影响；因此需要"语义导向"的攻击生成器，并以此做对抗训练。
- 写法亮点：用 Q1 / Q2 两个问题框定贡献；用四条准则（每条一个 bullet）把"实际威胁模型"定义清楚，再逐条说明方法如何满足——"先立标准、再给方案"。

## 5. 科研方法
- MobileSC：SemBlock 轻量编码器（深度可分离卷积）→ OFDM 发射（IFFT、CP、削波、导频）→ 信道 → OFDM 接收 → 可选语义解码器 → 分类器；多任务损失（重建 + 语义）。
- SemAdv：MLP 扰动生成器，仅以随机向量为输入（与输入无关）；目标集 / 无辜集的奖惩损失（语义导向）；方差正则 + 功率归一化（不可察觉）；替换标签实现定向误导（可控）。
- SemMixed：预训练后，每个 mini-batch 随机混合 SemAdv 与 PGM 扰动做对抗训练，并保留一半干净样本。

## 6. 仿真与实验
- MNIST、CIFAR-10、ImageNet 子集（10 类）；SNR = 10 dB、PSR = −4 dB。
- 按类别细粒度比较精度 / PSNR / SSIM / 误导率（干扰、PGD、PGM、SemAdv）→ 三种对抗训练的鲁棒性 → 参数量与推理时间 → 与 1/2 LDPC + QPSK / 16QAM 的传输效率与鲁棒性比较 → 案例可视化。
- 一个有意思的观察：SemAdv 几乎不降低 PSNR 却显著降低分类精度——像素指标无法反映语义攻击。

## 7. 图表
- 10 图 4 表 2 算法；49 个小节（层级很细）。Fig. 3 用"车 → 鸟"的具体攻击场景作为动机图；结果按类别给柱状图，突出"只伤目标类"。

## 8. 句式库
- 立场句（摘要）："We argue that central to the success of ESC is the robust interpretation of conveyed semantics at the receiver side, especially for security-critical applications such as automatic driving …"
- 脆弱性来源："However, robustifying semantic interpretation is challenging as ESC is extremely vulnerable to physical-layer adversarial attacks due to the openness of wireless channels and the fragileness of neural models."
- 迁移的困难："However, directly adapting these methods to ESC is challenging as a communication system needs to take the time-varying wireless channels into consideration."
- 首创性："To the best of our knowledge, the physical-layer adversarial robustness of DNN-based semantic communications, although non-trivial to robust semantic interpretation for safety-critical applications in practice, is still largely underexplored."
- 指出已有攻击不适用："As the bits/symbols are treated equally on these systems, such content-oriented attacks are not applicable to semantic communications."

## 9. 结论
- 1 段 165 词，复述框架、攻击、防御与"有趣发现"；无未来工作段。

## 10. Idea 拆解
- **基线**：端到端通信的通用对抗扰动（PGM）与 FGM 攻击；输入端语义噪声（twc.2023.3265201 一系）；视觉领域对抗训练。
- **增量**：提出语义导向、不可察觉、与输入无关、可控的物理层对抗攻击生成器，以及混合对抗训练防御，并用轻量 MobileSC 验证（security-privacy + robustness + new-metric）。
- **为什么有效**：生成器在训练中学到只对目标语义有效的通用扰动；对抗训练把这类扰动纳入训练分布，从而恢复目标类的精度。
- **证据**：SemAdv 让目标类精度下降 17 / 18 / 60 个点，其他类下降不到 10 点；对抗训练后 MNIST 精度近 100%，CIFAR-10 仍有约 5% 差距。
- **弱点**：白盒（攻击者能访问预训练模型）；只有分类任务的语义；没有理论鲁棒性保证；未与物理层检测（如异常检测）结合；无未来工作讨论。
- **开放问题**：
  - "This is probably because the semantics involved in CIFAR are much more complex than the ones in MNIST, and further understanding such a phenomenon would be an interesting …"
  - 推断：黑盒 / 迁移攻击；可认证鲁棒性（certified robustness）在语义通信中的界；生成式与数字语义系统的对抗鲁棒性；攻击检测与信道估计联合；多用户场景下的语义干扰攻击。
