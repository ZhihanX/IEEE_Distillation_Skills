---
doi: 10.1109/tsp.2021.3071210
title: "Deep Learning Enabled Semantic Communication Systems"
journal: TSP
year: 2021
band: 2019-2021
cites: 1649
cites_per_year: 308.7
article_type: research
topic: semantic
source: xplore-html
xplore: 9398576
auto:
  words_total: 6434
  n_sections: 6
  n_subsections: 17
  n_figures: 13
  n_tables: 3
  n_display_eq: 14
  n_algorithms: 4
  statements: {theorem: 1, lemma: 0, proposition: 0, corollary: 0, definition: 2, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.9
  we_per_1k: 5.7
  title_words: 6
  abstract_words: 194
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 1, however: 9, transition: 10, resultsShow: 0, motivatedBy: 2, toAddress: 3, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 9, intensifier: 5, worthNoting: 1, observe: 1, thisIsBecause: 2, asExpected: 0, insight: 1, tradeoff: 0, figVerb: 6, promising: 0, gen: 1, contrast: 6, firstTime: 0, novel: 0, weProposeFirst: 5, wlog: 0, code: 0, prototype: 0}
  methods: {DNN: 11, convergence: 8, DRL: 1, complexity: 1, gameTheory: 1}
  domain: {DeepSC: 33, BLEU: 23, sentSim: 18, transformer: 10, AWGN: 8, Rayleigh: 8, accuracy: 7, attention: 6, CNN: 5, QAM: 4, Huffman: 2, Rician: 2}
code:
  title_pattern: [noun-phrase]
  abstract_moves: [context, context, aim, aim, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: we-verb
  intro_paragraphs: 8
  intro_moves: [field, motivation, definition, history, questions, aim, contrib, roadmap]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, compose, adopt, outperform]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-paradigm, open-question]
  motivating_figure: true
  problem_class: learning
  solution: [DNN, bound-surrogate]      # 交叉熵 + 互信息下界（MINE）
  theory_role: supporting               # KL 对偶表示（Theorem 1）
  proofs_location: none
  complexity_analysis: true             # Table III 每句平均处理时间
  convergence_analysis: false
  sim_param_table: true                 # Table I 网络设置
  baselines_n: 6                        # Huffman / 5-bit / Brotli × RS / Turbo 多种组合 + BLSTM JSCC
  baseline_naming: descriptive
  x_axes: [SNR, symbols-per-word, epochs, dropout-rate]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2              # 另附 3 条"语义通信 vs 传统通信"差异列表
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: modality
  source: [text]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [transformer]
  channel: [AWGN, Rayleigh, Rician, erasure]
  adaptivity: [none]
  training: [two-phase, transfer-learning]   # 先训互信息估计器，再整体训练；迁移学习适配新信道 / 新知识
  metrics: [BLEU, sentence-similarity]
  datasets: [Europarl]
  baselines: [separate, other-learned]
  snr_mismatch_test: true               # 训练 SNR = 12 dB，跨 SNR 测试
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: information-theoretic         # 互信息下界作为容量项
  idea_delta: [new-paradigm, new-modality, new-metric]
  builds_on: [Transformer, BLSTM text JSCC (Farsad et al.), MINE, Weaver's three levels]
  open_problems_n: 0
---

## 1. 标题
- "Deep Learning Enabled Semantic Communication Systems"，6 词。纯名词短语、不带方法名——范式开创型论文的标题写法。

## 2. 摘要（8 句，194 词）
- 两句双背景（端到端物理层 DL、NLP 的成功）→ "Inspired by research results in both areas, we aim to provide a new view on communication systems from the semantic level." → DeepSC → Transformer 目标（最大化容量、最小化语义误差）→ 迁移学习 → 新指标（句子相似度）→ 结果（低 SNR 优势、对信道变化更鲁棒）。

## 3. 引言逻辑（8 段 + 3 个问题 + 4 条贡献）
- Shannon & Weaver 三层次 → 1G–5G 已接近香农极限 + 新应用的海量数据 → 语义通信的定义与优点 → 历史（Carnap 语义信息论、GMSC、语义噪声 / 语义信道、Nash 均衡 E2E 框架）→ "However, the semantic error in [9] measures the meaning of each word rather than the whole sentence." → 三个开放问题（bullet）→ 本文 → 贡献（每条注明回答了哪个问题）→ 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：新范式（第二层次"语义"通信尚无可实现系统）+ 开放问题（用三个问题框定）。
- 核心洞见：把 NLP 的机器翻译（Transformer）搬到物理层——"发送端编码句子、接收端'翻译'回句子"，以句子语义而非比特为目标；用交叉熵保语义、用互信息下界保容量。
- 写作亮点：用"Question 1/2/3"框定问题，再在贡献和结果中逐一声明"which addresses Question 3""which solves the Question 2"——形成问题-回答闭环。

## 5. 科研方法
- 架构：Transformer 语义编码器 → 全连接信道编码器 → 信道（AWGN / Rayleigh，完美 CSI）→ 信道解码器 → Transformer 语义解码器。
- 损失：交叉熵 + 互信息（Theorem 1 的 KL 对偶表示 → MINE 下界）；两阶段训练（Algorithm 1–3）。
- 迁移学习（Algorithm 4）：新信道只重训信道编解码器；新背景知识只重训语义编解码器。
- 指标：BLEU 与基于 BERT 的句子相似度（新提出）。

## 6. 仿真与实验
- Europarl（约 200 万句）；基准：Huffman / 定长 5-bit / Brotli 信源编码 × RS / Turbo 信道编码 × 多种 QAM，以及 BLSTM 文本 JSCC。
- BLEU / 句子相似度 vs SNR（同总符号数）→ 示例句子表（Table II）→ 每词符号数 → 互信息 → 学习率 → 迁移学习收敛 → 运行时间（Table III）。

## 7. 图表
- 13 图 3 表 4 算法。Fig. 1 双层（语义层 / 传输层）框架图；Fig. 3 自注意力示例；Table II 用具体句子展示语义保持。caption 把基准组合写全（很长）。

## 8. 句式库
- 双领域启发："Inspired by research results in both areas, we aim to provide a new view on communication systems from the semantic level."
- 语义通信的目标定义："Different from the conventional communications, semantic communications aim to transmit the information relevant to the transmission goal."
- 指出前人度量粒度的不足："However, the semantic error in [9] measures the meaning of each word rather than the whole sentence."
- 开放问题收束："These aforementioned works provide some insights and remarks for the design of semantic communications, but many issues remain unexplored."
- 问题清单："Question 2: How to measure the semantic error of sentences?"

## 9. 结论
- 2 段：复述（可变长度、互信息、迁移学习、新指标）+ 适用场景 → 三条"语义通信 vs 传统通信"差异（处理域、通信目标、系统设计）。无未来工作。

## 10. Idea 拆解
- **基线**：分离式文本传输（Huffman / Brotli + RS / Turbo）；BLSTM 文本 JSCC。
- **增量**：首个基于 Transformer 的端到端文本语义通信系统（DeepSC），以句子语义为目标、互信息为容量项，并提出句子相似度指标（new-paradigm + new-modality + new-metric）。
- **为什么有效**：语义编码去除表达冗余、只保留意义；联合训练让语义特征直接适配信道噪声，低 SNR 下不会出现分离方案的悬崖。
- **证据**：低 SNR 下 BLEU 与句子相似度都明显优于所有分离基准；迁移学习显著加快新信道 / 新语料的收敛。
- **弱点**：完美 CSI；模拟传输；只有一个语料库（Europarl）；句子相似度依赖 BERT，本身可能偏向模型；高 SNR 时不如部分传统方案；单用户点对点；无未来工作讨论。
- **开放问题**（论文未写，均为推断；后续工作已大量展开）：
  - 推断：语音 / 图像 / 多模态（jsac.2021.3087240、twc.2023.3240969）；数字化与量化（后续 digital 系列）；多用户（jsac.2022.3191326）；知识库失配与持续学习；语义信息论的严格度量；物联网轻量化（L-DeepSC）。
