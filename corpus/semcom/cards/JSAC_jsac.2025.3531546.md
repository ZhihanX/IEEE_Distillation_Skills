---
doi: 10.1109/jsac.2025.3531546
title: "D²-JSCC: Digital Deep Joint Source-Channel Coding for Semantic Communications"
journal: JSAC
year: 2025
band: 2022-2025
cites: 70
cites_per_year: 46.4
article_type: research
topic: semantic
source: xplore-html
xplore: 10845799
auto:
  words_total: 6888
  n_sections: 6
  n_subsections: 17
  n_figures: 10
  n_tables: 0
  n_display_eq: 44
  n_algorithms: 2
  statements: {theorem: 2, lemma: 2, proposition: 0, corollary: 1, assumption: 1, approximation: 2, remark: 2, proof: 5, proof_in_appendix: 0}
  n_appendix: 4
  mean_sentence_words: 23.2
  we_per_1k: 9.3
  title_words: 9
  abstract_words: 200
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 1, contribList: 2, roadmap: 1, however: 10, transition: 7, resultsShow: 2, motivatedBy: 1, toAddress: 3, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 2, outperform: 2, intensifier: 3, worthNoting: 2, observe: 13, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 3, promising: 1, gen: 2, contrast: 2, firstTime: 0, novel: 4, weProposeFirst: 3, wlog: 2, code: 0, prototype: 0}
  methods: {complexity: 5, DNN: 4, convergence: 4, DRL: 1}
  domain: {quantization: 10, DeepJSCC: 9, PSNR: 9, BPG: 8, Kodak: 6, MSSSIM: 6, AWGN: 3, CBR: 3, CLIC: 3, polar: 3, QAM: 2, ratedist: 2}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [context, gap, aim, method, method, method, theory, method, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 8
  intro_moves: [field, prior, prior, prior, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, propose, propose, reveal]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [practicality, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous   # 源 / 信道速率与 DNN 参数联合优化端到端失真
  solution: [bound-surrogate, exhaustive-search, gradient]   # 最小化失真上界；查表选模型；带信道失真项的损失重训
  theory_role: central
  proofs_location: appendix
  complexity_analysis: false
  convergence_analysis: false            # 只画迭代收敛曲线（Fig. 6）
  sim_param_table: false
  baselines_n: 3                         # DJSCC、NTSCC、BPG + LDPC / 容量界
  baseline_naming: acronym
  x_axes: [iterations, SNR, bandwidth-ratio, block-length]
  fig1_role: framework                   # (a) 传统 deep JSCC vs (b) D²-JSCC
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2               # 另附 3 条带标题的未来方向 bullet
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: digital
  source: [image]
  task: [reconstruction]
  paradigm: separate-learned             # 学习型信源编码（超先验）+ 数字信道编码（随机码 / 极化码），二者速率联合控制
  architecture: [CNN, VAE]
  channel: [AWGN]
  adaptivity: [SNR, bandwidth-rate, content]
  training: [multi-stage]                # 无误传输下预训练模型表 → 按 SNR 选模型 → 带信道失真重训
  metrics: [PSNR, MS-SSIM]
  datasets: [OpenImages, Kodak, CLIC]
  baselines: [DeepJSCC, NTSCC, separate]
  snr_mismatch_test: false
  complexity_reported: false
  digital_compatible: true
  hardware_validation: false
  theory: performance-bound              # 端到端失真上界（Theorem 1）与信道失真随 SNR 的增长阶（Theorem 2）
  idea_delta: [digitalization, theory, adaptivity]
  builds_on: [learned image compression with hyperprior, NTSCC, classic digital JSCC rate control]
  open_problems_n: 4
---

## 1. 标题
- "[方法名]: Digital Deep Joint Source-Channel Coding for Semantic Communications"，9 词。方法名中的上标 "²" 表示"数字 + 深度"两层含义。

## 2. 摘要（9 句，200 词）
- 背景 → 空白："Most existing SemCom techniques utilize deep neural networks (DNNs) to implement analog source-channel mappings, which are incompatible with existing digital communication architectures." → "this paper proposes a novel framework …" → 学习型信源编码（自适应先验）+ 信道编码 → 用贝叶斯模型与 DNN 的 Lipschitz 假设刻画端到端失真 → 两步速率控制算法 → 结果：优于经典 deep JSCC，并缓解分离方案的悬崖效应与平台效应。

## 3. 引言逻辑（8 段）
- 6G 多媒体需求 → 语义通信 → "However, the intricate nature of channel environment and the constraints imposed by existing digital hardware present challenges …"
- 传统 JSCC 分模拟（Shannon-Kotel'nikov 映射）与数字（码字分配、量化器设计、速率控制、不等错误保护）两类，都基于过于简化的信源模型。
- deep JSCC 是"模拟"的，不兼容数字硬件 → 半模拟方案（学到星座的转移概率）仍缺数字信道编解码、对信道统计变化敏感 → 学习型信源编码 + 数字信道编码的已有工作假设信源编码与信道无关。
- 本文 + 要解决的两个开放问题（量化与信道编解码不可微；DNN 不可解析导致端到端失真无闭式）→ 4 条贡献 → 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：实用性（模拟 / 半模拟方案不兼容标准数字系统）+ 已有方法局限（学习型信源编码与信道统计脱节）。
- 核心洞见：不再追求"端到端可微"，而是回到经典数字 JSCC 的"源-信道速率分配"，用理论（失真上界 + 随 SNR 的增长阶）指导"从预训练模型表中选模型 + 带信道失真重训"——用解析刻画替代端到端梯度。
- 把"悬崖效应 / 平台效应（leveling-off）"作为要解决的现象，并用 Theorem 2 解释其成因。

## 5. 科研方法
- 架构：超先验学习型信源编码（量化 + 熵编码）→ 分包 → 信道编码（理想随机码或极化码 + BPSK）→ AWGN。
- 理论：两个近似（特征稀疏高斯、均匀量化噪声）+ Lipschitz 假设 → Theorem 1 端到端失真上界 = 源失真 + 信道失真 → Corollary 1 进一步化简 → Lemma 2 给定源速率的最优信道码率 → Theorem 2 信道失真随容量下降呈指数增长。
- 算法：Step I 从查表中穷举选模型；Step II 加入信道失真项重训并更新超参数（区分平台阶段与悬崖阶段两种方向）。

## 6. 仿真与实验
- Open Images 训练，Kodak / CLIC 测试；基准 DJSCC、NTSCC、BPG + LDPC / 容量界。
- 收敛过程（两种阶段）→ PSNR vs SNR / 带宽比 / 码块长度 → MS-SSIM。
- 坦白：与 NTSCC 相比仅有小幅劣势（Kodak、SNR 4 dB 时低 0.39 dB）——数字方案以少量性能换兼容性。

## 7. 图表
- 10 图 0 表 2 算法。Fig. 1 用实线（信号流）与虚线（优化路径）对比两种架构；Fig. 3–4 验证近似与理论（特征分布、近似失真 vs 仿真）。

## 8. 句式库
- 空白："Most existing SemCom techniques utilize deep neural networks (DNNs) to implement analog source-channel mappings, which are incompatible with existing digital communication architectures."
- 半模拟方案的不足："However, the semi-analog JSCC still lacks the digital channel encoder/decoder and thus is incompatible with the standard systems."
- 指出前提假设："However, these works assume that the deep source coding is independent of the channel statistics."
- 列开放问题："The D2-JSCC addresses the following open problems in the digital SemCom: 1) … 2) …"
- 验证近似（写法）："Validation: To validate this approximation, we depict the PDFs of some randomly selected feature elements in Fig. 3."

## 9. 结论
- "Concluding Remarks" 2 段 + 3 条带标题的未来方向（端到端指标设计、多用户、衰落信道）。

## 10. Idea 拆解
- **基线**：模拟 deep JSCC / NTSCC（jsac.2022.3180802）；半模拟数字方案（DeepJSCC-Q、JCM）；经典数字 JSCC 速率控制。
- **增量**：学习型信源编码 + 标准数字信道编码，并用推导出的失真上界做源-信道速率联合控制（digitalization + theory + adaptivity）。
- **为什么有效**：Theorem 2 表明信道失真在容量下降时指数增长，因此按 SNR 选择合适的源速率可同时避开平台阶段（源失真主导）和悬崖阶段（信道失真主导）。
- **证据**：优于经典 DJSCC，接近 NTSCC（差距约 0.4 dB），无明显悬崖效应；极化码实际编码下同样有效。
- **弱点**：只有 AWGN 与 BPSK；依赖预训练模型表（存储开销）；近似假设（高斯特征、Lipschitz 常数估计）的误差未系统评估；只优化 MSE。
- **开放问题**：
  - 结论 bullet："E2E metric design: This paper described the E2E performance using the classical MSE metric, which might not be optimal for certain task-oriented applications."
  - 结论 bullet："Multi-user case: Future research could explore the extension of the D2-JSCC framework to a multi-user scenario, but the adaptive design of source-channel coders may pose challenges due to …"
  - 结论 bullet："Fading channel: More advanced techniques, e.g., truncated power control can be combined with the D2-JSCC framework to overcome channel fading."
  - 推断：与 HARQ / 自适应调制编码（AMC）结合；高阶调制下的速率控制；感知指标下的失真刻画。
