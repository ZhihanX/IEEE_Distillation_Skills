---
doi: 10.1109/jsait.2022.3231042
title: "DeepJSCC-Q: Constellation Constrained Deep Joint Source-Channel Coding"
journal: JSAIT
year: 2022
band: 2022-2025
cites: 153
cites_per_year: 39.8
article_type: research
topic: semantic
source: xplore-html
xplore: 9998051
auto:
  words_total: 5754
  n_sections: 6
  n_subsections: 4
  n_figures: 13
  n_tables: 0
  n_display_eq: 20
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.2
  we_per_1k: 15.0
  title_words: 7
  abstract_words: 193
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 1, roadmap: 0, however: 8, transition: 3, resultsShow: 0, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 1, intensifier: 1, worthNoting: 1, observe: 5, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 2, promising: 2, gen: 0, contrast: 3, firstTime: 0, novel: 0, weProposeFirst: 3, wlog: 0, code: 3, prototype: 0}
  # code 3 为误报（"source code rate" 等）
  methods: {complexity: 4, DNN: 3}
  domain: {DeepJSCC: 42, quantization: 31, QAM: 25, AWGN: 11, LDPC: 8, BPG: 6, CBR: 5, MSSSIM: 4, PSNR: 3, VQ: 3, attention: 3}
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [context, context, gap, gap, aim, result, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb       # "Herein, we propose DeepJSCC-Q, …"
  intro_paragraphs: 7
  intro_moves: [field, prior, prior, gap, aim, approach, contrib]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [propose, show, show, show, show]
  contrib_quantified: false
  first_claim: false
  roadmap: false
  notation: none
  gap_type: [practicality]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2                 # BPG + 802.11ad LDPC（多种 QAM）、无约束 DeepJSCC
  baseline_naming: descriptive
  x_axes: [SNR, modulation-order, constellation-map, bandwidth-ratio]
  fig1_role: framework           # 传统分离式数字系统框图
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: digital
  source: [image]
  task: [reconstruction]
  paradigm: digital-jscc
  architecture: [CNN, attention]
  channel: [AWGN, Rayleigh]
  adaptivity: [none]
  training: [end-to-end]
  metrics: [PSNR, MS-SSIM]
  datasets: [ImageNet, Kodak]
  baselines: [separate, DeepJSCC]
  snr_mismatch_test: true
  complexity_reported: false
  digital_compatible: true
  hardware_validation: false
  theory: none
  idea_delta: [digitalization]
  builds_on: [DeepJSCC, soft-to-hard vector quantization]
  open_problems_n: 2
---

## 1. 标题
- "[方法名]: [约束条件] [方法全称]"，7 词。"Constellation Constrained" 直接点出与原 DeepJSCC 的唯一差别。

## 2. 摘要（7 句，193 词）
- 两句背景（机器学习为 JSCC 提供新途径、结果优于数字方案）→ 两句空白："However, end-to-end training of such schemes requires a differentiable channel input representation; hence, prior works have assumed that any complex value can be transmitted over the channel." + 这阻碍了只接受数字星座的硬件 / 协议 → "Herein, we propose DeepJSCC-Q …" → 两句结果（高阶调制下接近无约束版本；保留平滑退化）。

## 3. 引言逻辑（7 段）
- 信源 / 信道编码 → 分离定理与有限码长 → 跨层优化型 JSCC 增益不足以抵消复杂度 → DeepJSCC 的优点 → 它去掉了星座图，而商用硬件实现固定的标准星座（以 802.11ad、802.15.4 为例）→ "Therefore, in practice, DeepJSCC can be difficult to implement without custom hardware." → 本文 → 把问题表述为"离散输入 AWGN 信道上的 JSCC"与"中间带量化层的自编码器训练" → 5 条贡献。

## 4. Idea 是怎么提出的
- 空白类型：实用性（模拟 DeepJSCC 无法在标准硬件上部署）。
- 写法亮点：用具体标准（IEEE 802.11ad 只用 BPSK/QPSK/16QAM/64QAM；802.15.4 只用 OQPSK）把"不实用"落到可核查的事实上。
- 反直觉的对比点："This emphasizes a main difference between DeepJSCC and digital transmission, where a larger constellation implies a higher communication rate."（在 DeepJSCC-Q 中更大星座只意味着更细的量化，不改变码率）。

## 5. 科研方法
- 编码器输出连续潜变量 → 软-硬量化层（前向硬量化到最近星座点，反向用 softmax 加权平均）→ 信道 → 解码器。
- 两种量化：固定星座（QAM）与可学习星座；加 KL 正则鼓励均匀使用星座点。

## 6. 仿真与实验
- ImageNet 训练、Kodak 测试；AWGN 与慢衰落；基准 BPG + 802.11ad LDPC（多种调制取包络）、无约束 DeepJSCC。
- 结果：所有 M-QAM 下都有平滑退化；4096-QAM 时几乎与无约束 DeepJSCC 相同、并处于分离方案包络上；学到的星座在低阶时更优，且分布非平凡（Fig. 10–11）。

## 7. 图表
- 13 图 0 表。Fig. 4 图解软-硬量化（以 QPSK 为例）；Fig. 10–11 星座点及使用概率可视化。

## 8. 句式库
- 空白："However, end-to-end training of such schemes requires a differentiable channel input representation; hence, prior works have assumed that any complex value can be transmitted over the channel."
- 部署障碍落到标准："For example, the IEEE 802.11ad physical layer (PHY) specification [15] states the use of BPSK, QPSK, 16-QAM and 64-QAM."
- 不实用的结论："Therefore, in practice, DeepJSCC can be difficult to implement without custom hardware."
- 隐含假设（相关工作节）："However, an implicit assumption in all of the works above is the ability for the communication hardware to transmit arbitrary complex valued channel inputs."
- 意义收尾："These promising results can bring DNN-based JSCC schemes closer to real world deployment."

## 9. 结论
- 1 段 179 词，现在完成时复述 + 部署意义；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：DeepJSCC（tccn.2019.2919300 及其改进架构）。
- **增量**：在编码器后加入软-硬量化层，把信道输入限制为有限星座（可固定可学习）（digitalization）。
- **为什么有效**：量化层在前向保持离散、在反向可微，使端到端训练可行；高阶星座的量化误差小，逼近无约束情形。
- **证据**：4096-QAM 时性能几乎等同无约束 DeepJSCC；低阶时学到的星座优于 QAM；在所有 M-QAM 下都无悬崖效应。
- **弱点**：最优表现依赖极高阶（4096）星座，实际硬件很少支持；硬判决量化有信息损失（后续 VAE 概率建模方法指出）；没有信道编码，误码直接进入语义；无复杂度分析。
- **开放问题**：
  - 推断：低阶星座下的性能提升（后续 tcomm.2024.3386577 用概率建模）；调制阶数随 SNR 自适应（后续 tccn.2024.3422496）；与信道编码 / 比特接口的结合（D²-JSCC 等）；衰落与 MIMO 下的星座约束 JSCC。
