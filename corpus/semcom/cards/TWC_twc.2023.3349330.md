---
doi: 10.1109/twc.2023.3349330
title: "Semantic Communications for Image Recovery and Classification via Deep Joint Source and Channel Coding"
journal: TWC
year: 2024
band: 2022-2025
cites: 154
cites_per_year: 70.8
article_type: research
topic: semantic
source: xplore-html
xplore: 10388062
auto:
  words_total: 6385
  n_sections: 6
  n_subsections: 14
  n_figures: 16
  n_tables: 2
  n_display_eq: 21
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 1, corollary: 0, remark: 2, proof: 1, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 26.9
  we_per_1k: 15.5
  title_words: 14
  abstract_words: 306
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 1, roadmap: 1, however: 7, transition: 13, resultsShow: 0, motivatedBy: 2, toAddress: 3, gapWord: 2, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 5, intensifier: 5, worthNoting: 6, observe: 13, thisIsBecause: 5, asExpected: 0, insight: 0, tradeoff: 2, figVerb: 1, promising: 0, gen: 2, contrast: 2, firstTime: 0, novel: 2, weProposeFirst: 5, wlog: 0, code: 0, prototype: 1}
  # prototype 1 为误报（"experimental setups"）
  methods: {DNN: 1, complexity: 1}
  domain: {DeepJSCC: 62, MNIST: 13, CIFAR: 11, accuracy: 9, ratedist: 8, PSNR: 7, SNRmismatch: 4, AWGN: 3, Rayleigh: 2, Rician: 2}
code:
  title_pattern: [X-for-Y, X-via-Y]
  abstract_moves: [context, context, gap, aim, method, method, method, result, result, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb    # "Differently, this paper investigates …"
  intro_paragraphs: 8
  intro_moves: [field, tech, prior, prior, gap, aim, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [design, propose, present]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [limitation, unification]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: supporting           # Proposition 1：非渐近率失真下特征空间体积的度量
  proofs_location: appendix
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: true             # Table I/II 编解码网络结构与超参数
  baselines_n: 3                    # MSE 训练的 deep JSCC、SSIM 训练的 deep JSCC、BPG + 容量界
  baseline_naming: descriptive
  x_axes: [SNR, weight, label-corruption-rate]
  fig1_role: framework
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1          # 另附 3 条带标题的未来方向 bullet
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: image-jscc
  source: [image]
  task: [reconstruction, classification, multi-task]
  paradigm: analog-jscc
  architecture: [CNN]
  channel: [AWGN, Rayleigh, Rician]
  adaptivity: [SNR, bandwidth-rate]   # 门控网络按 SNR 剪枝输出特征维度
  training: [end-to-end]
  metrics: [PSNR, accuracy]
  datasets: [MNIST, CIFAR-10]
  baselines: [DeepJSCC, separate]
  snr_mismatch_test: true
  complexity_reported: false
  digital_compatible: false
  hardware_validation: false
  theory: rate-distortion           # 编码率约减（MCR²）来自非渐近率失真理论
  idea_delta: [new-task, new-component, adaptivity]
  builds_on: [DeepJSCC, maximal coding rate reduction (MCR²)]
  open_problems_n: 3
---

## 1. 标题
- "Semantic Communications for [任务 1] and [任务 2] via [方法]"，14 词。

## 2. 摘要（10 句，306 词，偏长）
- 6G 需要支持分类等 AI 任务 → 语义 / 任务导向通信是范式转变 → 空白："However, most existing works focused on the deep JSCC designs for one task of data recovery or AI task execution independently, which cannot be transferred to other unintended tasks." → "Differently, this paper investigates …" → 统一损失（编码率约减最大化 + MSE 最小化）及其作用的解释句 → 门控 deep JSCC → 实验 → 三句结果（多任务、门控节省开销、对标签噪声更鲁棒）。

## 3. 引言逻辑（8 段）
- 边缘 AI 愿景 → 语义通信 → deep JSCC 的任务相关性，把任务分为"数据恢复"和"AI 任务执行"两类 → 两类各自的文献与局限（数据恢复类不服务 AI 任务；AI 任务类特征无法恢复数据，且依赖标签、怕标签错误）→ 现实需要两者同时（VR 中的环境重建 + 物体分类）→ 与两篇多任务先驱工作的区别（用编码率约减而非交叉熵）→ 本文 → 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（单任务模型无法迁移）+ 统一（一个特征同时服务重建与分类）。
- 核心洞见：把视觉领域的"最大编码率约减（MCR²）"引入 JSCC——让特征在子空间上可分，接收端用简单的最近子空间分类器即可分类，同时 MSE 保证可重建；用一个权重 β 调节两个任务的权衡。
- 附带卖点：特征空间分类不依赖标签拟合，因而对标签错误更鲁棒（实验单列一节验证）。

## 5. 科研方法
- 编码器 → 归一化 → 信道（不可训练层）→ 接收端直接在接收特征上分类 + 解码器重建；损失 = 编码率约减项 + β × MSE；Proposition 1 给出特征空间体积的率失真度量。
- 门控 deep JSCC：门控网络以估计噪声方差为输入输出掩码，按 SNR 剪枝特征维度；域随机化训练（随机扰动 SNR）。

## 6. 仿真与实验
- MNIST 与 CIFAR-10；基准为 MSE / SSIM 训练的 deep JSCC 和 BPG + 容量界。
- 先展示"训练不含信道"时信道损伤的影响 → 端到端训练后的重建 → β 权衡 → PSNR 与分类精度 vs SNR → 门控方案在变化信道下的性能与激活维度比例（如 MNIST 在 −3 dB / 21 dB 时传输开销分别降 4.8% / 28.3%）→ 标签错误率实验。

## 7. 图表
- 16 图 2 表 2 算法。Fig. 2 用球堆积（sphere packing）图解编码率约减（把理论工具可视化）。caption 短标签。

## 8. 句式库
- 空白："However, most existing works focused on the deep JSCC designs for one task of data recovery or AI task execution independently, which cannot be transferred to other unintended tasks."
- 分类已有工作："In general, the tasks could be characterized as two core categories, namely data recovery and AI task execution."
- 现实需求："However, in practice, many applications require performing data recovery and AI task execution simultaneously."
- 与先驱工作区分："Different from the two prior works, we invoke the coding rate reduction method [26], [27], [28] to tackle the potential label corruption issue …"
- 未来工作引导："Due to the space limitation, there are other interesting issues that are unaddressed in this work."

## 9. 结论
- "Concluding Remarks" 1 段 + 3 条带标题的未来方向（更复杂下游任务、多任务之间的内在联系、更复杂数据集）。

## 10. Idea 拆解
- **基线**：单任务 deep JSCC（重建：tccn.2019.2919300；任务：信息瓶颈类 jsac.2021.3126087）；多任务先驱（tcomm.2024.3364990 等，用交叉熵）。
- **增量**：用 MCR² + MSE 的统一损失让一个 JSCC 同时服务重建与分类（new-task + new-component），并用门控网络按 SNR 调整特征维度（adaptivity）。
- **为什么有效**："… with coding rate reduction maximization, the learned features are discriminative enough to support image classification task directly in the feature space."
- **证据**：同时获得接近 MSE 训练模型的 PSNR 和明显更高的分类精度；门控方案降低传输开销而性能损失很小；标签错误下优于交叉熵训练。
- **弱点**：只在 MNIST / CIFAR-10 小图上验证；只有点对点；没有复杂度分析；与 BPG 的比较只在小图上。
- **开放问题**：
  - 结论 bullet："Extension to more complex downstream tasks: … How to extend the proposed designs to more complex downstream tasks is an interesting …"
  - 结论 bullet："Extension to more complex datasets: Extending our proposed framework on more complex datasets such as ImageNet is also worth pursuing in future work."
  - 推断：多用户、多接收端各自执行不同任务（广播多任务）；任务之间的理论权衡刻画；与数字调制兼容。
