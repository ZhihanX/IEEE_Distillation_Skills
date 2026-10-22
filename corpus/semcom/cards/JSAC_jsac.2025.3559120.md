---
doi: 10.1109/jsac.2025.3559120
title: "Generative Semantic Communications With Foundation Models: Perception-Error Analysis and Semantic-Aware Power Allocation"
journal: JSAC
year: 2025
band: 2022-2025
cites: 48
cites_per_year: 38.1
article_type: research
topic: semantic
source: xplore-html
xplore: 10960413
auto:
  words_total: 5491
  n_sections: 7
  n_subsections: 11
  n_figures: 10
  n_tables: 0
  n_display_eq: 37
  n_algorithms: 1
  statements: {theorem: 1, lemma: 2, proposition: 0, corollary: 2, definition: 2, assumption: 1, remark: 3, proof: 4, proof_in_appendix: 2}
  n_appendix: 3
  mean_sentence_words: 22.5
  we_per_1k: 3.1
  title_words: 12
  abstract_words: 162
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 1, roadmap: 0, however: 7, transition: 4, resultsShow: 1, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 1, npHard: 0, closedForm: 1, outperform: 3, intensifier: 2, worthNoting: 0, observe: 0, thisIsBecause: 1, asExpected: 0, insight: 2, tradeoff: 2, figVerb: 8, promising: 1, gen: 0, contrast: 1, firstTime: 0, novel: 1, weProposeFirst: 2, wlog: 0, code: 0, prototype: 0}
  methods: {bisection: 6, DNN: 1, complexity: 1}
  domain: {perception: 42, LLM: 12, ratedist: 11, MSSSIM: 10, DeepJSCC: 4, QAM: 4, diffusion: 4, Kodak: 3, SSIM: 3, GAN: 2, JPEG: 2, VAE: 2, feedback: 2, knowledgeBase: 2, transformer: 2}
code:
  title_pattern: [colon-subtitle, X-with-Y]
  abstract_moves: [context, aim, theory, theory, method, method, result, result]
  abstract_has_numbers: true            # "up to 90% power saving"
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, theory-prior, prior, prior, gap, aim]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, analyze, investigate, obtain]
  contrib_quantified: true              # 10% / 90% 节能
  first_claim: false
  roadmap: false
  notation: none
  gap_type: [practicality, new-paradigm]
  motivating_figure: true
  problem_class: nonconvex-continuous   # 语义感知功率最小化（感知约束非凸）
  solution: [closed-form, bisection]    # 比例法闭式解；二分法求局部最优
  theory_role: central                  # 率-失真-感知下的感知-误差单调性（Lemma 1/2、Corollary 1）
  proofs_location: appendix
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 1                        # 语义无关（等 SNR）功率分配；框架有效性另与 JPEG、Cheng2020 比较
  baseline_naming: descriptive
  x_axes: [perception-requirement, BER, BLER]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
semcom:
  category: generative
  source: [image]
  task: [reconstruction]
  paradigm: separate-learned            # 预训练基础模型做语义编 / 解码 + 标准比特传输（BPSK / 有限码长编码）
  architecture: [diffusion, LLM]        # 文本提示反演 + 边缘图，扩散模型再生成
  channel: [Rayleigh]
  adaptivity: [power]
  training: [none-pretrained]           # 不额外训练
  metrics: [CLIP, MS-SSIM, custom]      # 功耗、BER / BLER
  datasets: [Kodak]
  baselines: [optimization, separate]
  snr_mismatch_test: false
  complexity_reported: false
  digital_compatible: true
  hardware_validation: false
  theory: rate-distortion               # 率-失真-感知函数与感知-误差关系
  idea_delta: [generative-prior, system-optimization, theory, new-metric]
  builds_on: [rate-distortion-perception theory, text-guided diffusion (prompt inversion + edge map), finite blocklength coding]
  open_problems_n: 2
---

## 1. 标题
- "Generative Semantic Communications With [工具]: [理论分析] and [资源分配]"，12 词。冒号后两个名词短语分别对应"理论 + 优化"两部分贡献——通信系统类论文的典型双段式。

## 2. 摘要（8 句，162 词）
- 基础模型可在超低码率下高保真交换语义 → 本文框架（两种解码方案：不编码前传含错 / 编码丢弃含错）→ 两句理论（率-失真-感知刻画、语义价值定义）→ 两句优化（功率最小化、利用单调性的两种方法）→ Kodak 上得到感知-误差函数 → 结果带数字（"up to 90% power saving"）。

## 3. 引言逻辑（6 段）
- Shannon 系统关注准确重建 → 语义通信 → 语义信息论的发展脉络（逻辑概率、模糊数学、率失真、Niu & Zhang）→ "Despite these advances, a universal semantic information theory for SemCom system design remains an open challenge."
- deep JSCC 本质仍是率-失真（失真损失）→ 生成式语义通信（VAE / GAN / 扩散）→ 两个挑战：端到端训练需要模拟调制、训练成本高且泛化差 → 基础模型（BERT / GPT / DALL·E / Sora）作为共享知识库 → 本文（编解码固定后，传输可靠性成为感知质量的关键）→ 4 条贡献（含数字）。

## 4. Idea 是怎么提出的
- 空白类型：实用性（端到端训练与数字系统冲突、泛化差）+ 新范式（预训练基础模型作为不训练的语义编 / 解码器）。
- 核心洞见：语义编 / 解码器固定之后，问题就从"学编码"变成"传输可靠性 → 感知质量"的映射；证明这一映射单调（Corollary 1），就可以把它当作约束做经典的功率分配——不同语义流（文本提示 vs 边缘图）重要性不同，应差异化分配功率。
- 一个反直觉发现被写入结论：某些语义流可分配零功率，意味着可关掉对应的语义提取器。

## 5. 科研方法
- 框架：I 个语义提取器（文本提示反演 + HED 边缘图 / NTC 压缩）→ 多流比特 → 不编码 BPSK（前传含错）或有限码长编码（误块则丢弃）→ 扩散模型再生成。
- 理论：率-失真-感知函数 → Lemma 1 感知-码率单调 → 比特独立假设下的互信息（Lemma 2）→ Corollary 1 感知值随误码非减 → Definition 1/2 语义价值。
- 优化：P1 / P2（满足感知要求的总功率最小化）→ Corollary 2 约束取等 → Theorem 1 比例法闭式解 → Algorithm 1 二分搜索局部最优。
- 感知-误差函数由仿真数据曲线拟合得到。

## 6. 仿真与实验
- Kodak；CLIP 与 MS-SSIM 两种感知指标。
- 框架有效性（vs JPEG、Cheng2020 的 bpp 与视觉质量）→ 感知-误差函数与语义价值 → 总功耗（未编码最多省 10%、编码最多省 90%）→ BER / BLER / 容量 → 感知值 CDF → 再生图像。

## 7. 图表
- 10 图 0 表 1 算法。Fig. 4 拟合得到的感知-误差函数是理论与优化之间的桥梁；Fig. 9 用 CDF 展示约束满足程度。

## 8. 句式库
- 指出理论空白："Despite these advances, a universal semantic information theory for SemCom system design remains an open challenge."
- 指出 deep JSCC 的本质局限："However, distortion of SemCom systems may no longer serve as the key performance indicator for emerging applications with specific tasks or goals, where accurate semantic information conveying becomes …"
- 端到端架构的两个挑战："Firstly, analog modulations are required for gradient computation and back-propagation during training, which conflicts with modern digital communication systems."
- 资源分配的动机："Since semantic features exhibit varying levels of importance, conventional resource allocation strategies may be inefficient."
- 从结果引出未来工作："This insight points toward future research in adaptive semantic communications with channel feedback to improve both radio and computation efficiency."

## 9. 结论
- 1 段 157 词：复述框架、理论、方法、验证 → 关键发现（部分语义流功率可为零）→ 未来工作（带信道反馈的自适应语义通信）。

## 10. Idea 拆解
- **基线**：端到端 deep JSCC / 生成式 JSCC（jsac.2023.3288243、twc.2024.3379244）；语义无关的等 SNR 功率分配。
- **增量**：用预训练基础模型替代端到端训练的编解码器，用率-失真-感知理论刻画"传输错误 → 感知质量"的单调关系，并据此做语义感知的功率分配（generative-prior + theory + system-optimization + new-metric）。
- **为什么有效**：不同语义流对感知质量的贡献不同（语义价值不同），而感知-误差关系单调，因此可把感知约束转化为各流的 BER / BLER 约束并闭式或二分求解。
- **证据**：编码情形下最多节省 90% 功率；语义价值随指标（CLIP vs MS-SSIM）改变，验证了"重要性依赖任务"。
- **弱点**：感知-误差函数靠仿真曲线拟合，泛化到别的模型 / 数据集需重测；比特独立假设；只有 Kodak 24 张图；生成模型的计算开销与时延未计入；基准只是等 SNR 分配。
- **开放问题**：
  - "This insight points toward future research in adaptive semantic communications with channel feedback to improve both radio and computation efficiency."
  - "Despite these advances, a universal semantic information theory for SemCom system design remains an open challenge."
  - 推断：通信功率与生成计算能耗的联合优化；多用户下的语义感知资源分配；视频 / 多模态的感知-误差刻画；感知-误差函数的解析模型（替代曲线拟合）。
