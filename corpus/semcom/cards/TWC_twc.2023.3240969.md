---
doi: 10.1109/twc.2023.3240969
title: "Deep Learning Enabled Semantic Communications With Speech Recognition and Synthesis"
journal: TWC
year: 2023
band: 2022-2025
cites: 284
cites_per_year: 91.9
article_type: research
topic: semantic
source: xplore-html
xplore: 10038754
auto:
  words_total: 6378
  n_sections: 6
  n_subsections: 24
  n_figures: 10
  n_tables: 4
  n_display_eq: 14
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.6
  we_per_1k: 2.9
  title_words: 10
  abstract_words: 162
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 1, roadmap: 1, however: 7, transition: 33, resultsShow: 0, motivatedBy: 4, toAddress: 0, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 5, intensifier: 6, worthNoting: 2, observe: 0, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 2, promising: 2, gen: 1, contrast: 0, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 0, code: 0, prototype: 0}
  methods: {DNN: 18, complexity: 5, convergence: 2, DRL: 1}
  domain: {DeepSC: 51, CNN: 11, WER: 8, AWGN: 6, Rayleigh: 5, Rician: 5, accuracy: 3, attention: 3, QAM: 2, polar: 2, transformer: 2}
code:
  title_pattern: [X-with-Y]
  abstract_moves: [aim, method, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 7
  intro_moves: [field, gap-quantify, taxonomy, prior, aim, roadmap, notation]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, extract, develop, build]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-task]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: true             # 参数量 8580 万；Table II 编码符号数
  convergence_analysis: false
  sim_param_table: true                 # Table I
  baselines_n: 4                        # 语音收发机、文本收发机、特征收发机（IEEE 754 + 极化码 + 64-QAM）、SR + DeepSC
  baseline_naming: descriptive
  x_axes: [SNR, epochs]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: true        # 软件演示（非无线硬件）
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: modality
  source: [speech]
  task: [recognition, synthesis]
  paradigm: task-feature
  architecture: [CNN, RNN]              # CNN + GRU 双向 RNN；接收端 Tacotron 2 + WaveNet 合成
  channel: [AWGN, Rayleigh, Rician]
  adaptivity: [none]                    # 选出一个"鲁棒模型"应对多种信道
  training: [end-to-end, separate-module]   # CTC 损失端到端；合成模块单独训练
  metrics: [CER, WER, custom]           # FDSD、KDSD（语音合成质量）
  datasets: [LJSpeech]
  baselines: [separate, DeepSC, other-learned]
  snr_mismatch_test: true               # 不同信道 / SNR 训练与测试交叉
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [new-task, new-modality]
  builds_on: [DeepSC, DeepSC-S, Deep Speech 2, Tacotron 2]
  open_problems_n: 0
---

## 1. 标题
- "Deep Learning Enabled Semantic Communications With [任务 1] and [任务 2]"，10 词。沿用 DeepSC 的标题骨架，只换任务。

## 2. 摘要（7 句，162 词）
- 首句就是本文（DeepSC-ST）→ 两个任务 → 识别端机理（只传与识别相关的语义特征、接收端恢复文本）→ 合成端机理（文本 + 说话人信息重生成语音）→ 鲁棒模型 → 结果 → 软件演示。

## 3. 引言逻辑（7 段）
- AI 应用的传输需求 → Shannon & Weaver → "However, it is challenging to quantify the semantic information due to the lack of a mathematical model." → DL 绕开建模 → 任务导向语义通信 → 两类目标（数据重建 / 智能任务）→ 文本 / 语音 / 图像文献，语音类三篇各一句 → "Although semantic communications have been designed for intelligent speech transmission, investigation on semantic communications to execute speech-centric intelligent tasks at the receiver is still missing." → 频谱稀缺 → 本文（只传文本相关特征，省掉说话人音色、背景噪声等）→ 贡献 → 路线图 → 记号。

## 4. Idea 是怎么提出的
- 空白类型：新任务（语音语义通信从"重建波形"转为"在接收端执行语音识别 / 合成"）。
- 核心洞见：语音中与"说了什么"相关的信息远少于波形本身——发送端只传文本相关的语义特征，接收端识别出文本；需要语音时再用接收端已注册的说话人信息（用户 ID）合成。把"知识"（说话人特征）放在接收端，传输只承载内容。
- 一个模型、两种用户需求（只要文本 / 要语音），合成模块可选。

## 5. 科研方法
- 发送端：语谱 → CNN + GRU 双向 RNN 语义编码器 → 全连接信道编码。
- 接收端：信道解码 → 特征解码器 → 贪心解码（CTC）得到文本 → 可选 Tacotron 2 + WaveNet 按用户 ID 合成语音。
- 指标：CER / WER（识别），FDSD / KDSD（合成，基于深度语音识别模型的特征距离）。

## 6. 仿真与实验
- LJSpeech；完美 CSI；AWGN、Rayleigh、Rician。
- 4 个基准设计得很细：传语音、传文本、传本文语义特征（IEEE 754 浮点 + 极化码 + 64-QAM）、SR + DeepSC 级联。
- 复杂度（参数量、编码符号数 Table II）→ CTC 收敛 → CER / WER vs SNR → FDSD / KDSD vs SNR + 主观问卷（Table III）→ 识别句子样例（Table IV）→ 软件演示 → 语谱图。
- 坦白：高 SNR（≥ 8 dB）时 WER 不如文本收发机与特征收发机。

## 7. 图表
- 10 图 4 表 2 算法。Fig. 9 软件演示界面截图（作为 proof-of-concept）；Table IV 具体句子对比——语义通信论文常用的定性证据。

## 8. 句式库
- 语义信息难以量化："However, it is challenging to quantify the semantic information due to the lack of a mathematical model."
- 空白（新任务）："Although semantic communications have been designed for intelligent speech transmission, investigation on semantic communications to execute speech-centric intelligent tasks at the receiver is still missing."
- 任务导向的动机："Moreover, in some applications, users only request some critical semantic information from the source, which motivates us to transmit the application-related semantic information."
- 模块可省略的说明："It is worth mentioning that Tacotron 2 is trained separately from the speech recognition task and can be omitted in the communication scenarios where users only request the text information."

## 9. 结论
- 1 段 123 词，复述 + 软件演示 + "envisioned to be a promising candidate"；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：DeepSC（tsp.2021.3071210，文本）；DeepSC-S（jsac.2021.3087240，语音波形重建）；分离式语音 / 文本传输。
- **增量**：把语音语义通信的目标从波形重建换成"接收端语音识别 + 可选合成"，只传文本相关特征（new-task + new-modality）。
- **为什么有效**：识别任务只需要内容信息，丢掉音色 / 噪声等无关成分，所需符号数大幅减少（Table II）；低 SNR 时端到端学习的特征比分离方案更鲁棒。
- **证据**：低 SNR 下 CER / WER 优于全部基准；FDSD / KDSD 优于 SR + DeepSC；编码符号数远少于传语音。
- **弱点**：完美 CSI；高 SNR 时不如传统文本 / 特征收发机；合成依赖接收端预注册说话人信息（隐私与可扩展性）；单数据集、单说话人语料（LJSpeech）；模型大（8580 万参数）；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：多说话人 / 多语言；韵律、情感等副语言语义的传输；数字化（码本 / 量化）；与大语音模型（Whisper 类）结合；多用户语音语义通信的资源分配；实时流式传输的时延。
