---
doi: 10.1109/jsac.2021.3087240
title: "Semantic Communication Systems for Speech Transmission"
journal: JSAC
year: 2021
band: 2019-2021
cites: 676
cites_per_year: 130.6
article_type: research
topic: semantic
source: xplore-html
xplore: 9450827
auto:
  words_total: 6311
  n_sections: 6
  n_subsections: 18
  n_figures: 11
  n_tables: 3
  n_display_eq: 10
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 23.9
  we_per_1k: 4.1
  title_words: 6
  abstract_words: 206
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 7, contribList: 1, roadmap: 1, however: 7, transition: 36, resultsShow: 2, motivatedBy: 4, toAddress: 5, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 7, intensifier: 3, worthNoting: 1, observe: 1, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 1, promising: 3, gen: 1, contrast: 0, firstTime: 0, novel: 1, weProposeFirst: 2, wlog: 1, code: 0, prototype: 0}
  methods: {DNN: 4, DRL: 1, complexity: 7, convergence: 4}   # 提取器的 SDR 命中 18 次是 signal-to-distortion ratio，已剔除
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, aim, method, method, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 10
  intro_moves: [tech, gap, tech, gap, gap, tech, aim, contrib, roadmap, notation]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [develop, employ, develop, apply]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, tool-transfer]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [SNR, epochs]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: modality
  source: [speech]
  task: [reconstruction]
  paradigm: analog-jscc
  architecture: [CNN, attention]           # SE-ResNet
  channel: [AWGN, Rayleigh, Rician]
  adaptivity: [none]
  training: [end-to-end]
  metrics: [SDR, PESQ]
  datasets: [Edinburgh]
  baselines: [separate, other-learned, own-ablation]
  snr_mismatch_test: true
  complexity_reported: true                # 逐模块 FLOPs
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [new-modality]
  builds_on: [DeepSC, SE-ResNet attention]
  open_problems_n: 0
---

## 1. 标题
- "[新范式] Systems for [新信源] Transmission"，6 词。把已有范式（语义通信）推广到新的信源类型（语音），标题只需换一个名词。

## 2. 摘要（9 句，206 词）
- "In this paper, we make an effort to recover the transmitted speech signals in the semantic communication systems, which minimizes the error at the semantic level …"（用 "rather than" 点出范式差别）。
- 模型命名延续系列："named DeepSC-S"。
- 单独一句解释设计动机："The motivation behind the attention mechanism is to identify the essential speech information by providing higher weights to them …"
- 结尾两句结果（指标名点出 SDR、PESQ；低 SNR 下更鲁棒），无数字。

## 3. 引言逻辑（10 段，约 970 词）
1. DL 进入通信。
2. DL 通信系统仍停留在比特 / 符号级（"However, even if the DL-enabled communication systems yield better performance …, their state-of-the-art models mainly focus on performance improvement at the bit or symbol level …"）。
3. 回溯 Shannon & Weaver 的通信三层次（bullet 列出 Level A/B/C）——用经典理论为新范式背书。
4. 语义理论 → 停滞原因（缺少语义信息的数学模型）。
5. 端到端系统与已有语义通信（图像、文本）→ "The investigation on semantic communication for speech signals transmission is still missed."
6. Fig. 1 + ASR 例子说明语义通信"只传与任务相关的特征"。
7. 本文的直觉：不做 DCT 等预处理、直接从原始语音学习（"Such extra operations … runs counter to the motivation of intelligence."）。
8. "In this paper, we propose …" → "The main contributions of this article can be summarized as fourfold:"
9. 路线图；10. Notation。

## 4. Idea 是怎么提出的
- 空白类型：新场景（新信源：语音）+ 工具迁移（SE 注意力 / ResNet）。
- 写法亮点：从通信理论源头（Shannon-Weaver 三层次）讲起，提高新范式的"正当性"；空白句直白（"is still missed"）。
- 设计直觉写得具体："It is intuitive that speech signals at the silent time-slots carry no information, while speech signals at the speaking time-slots carry the essential information."——由此引出注意力机制。

## 5. 科研方法
- 系统：语义编解码器 + 信道编解码器联合设计，端到端训练（MSE 损失），信道层可微。
- SE-ResNet 作为语义编解码器；训练 / 测试算法分开写（Algorithm 1/2）；在固定信道和 SNR 下训练以获得对信道变化鲁棒的模型。
- 复杂度用 FLOPs 逐模块计算（单列 "Complexity Analysis" 小节）。
- 无定理。

## 6. 仿真与实验
- 数据集（Edinburgh DataShare）、两种采样率对应电话与多媒体两种应用场景。
- 三个基准编号：Benchmark 1（PCM + 传统信道编码）、Benchmark 2（特征学习 + 传统信道编码，"semi-traditional"）、Benchmark 3（无注意力的 CNN，用于消融）。参数分别列表（Table I–III）。
- 指标：SDR、PESQ；横轴 SNR，三种信道各一个子图。

## 7. 图表
- 11 图 3 表 2 算法。Fig. 1 概念图（不同输入的语义通信）在引言；Fig. 2–5 结构图。caption 描述型，列出全部对比对象和信道类型。

## 8. 句式库
- 范式差别："… which minimizes the error at the semantic level rather than the bit or symbol level."
- 已有工作停在低层："… their state-of-the-art models mainly focus on performance improvement at the bit or symbol level, …"
- 理论背书："Shannon and Weaver [9] categorized communications into three levels:"
- 空白："The investigation on semantic communication for speech signals transmission is still missed."
- 设计直觉："It is intuitive that speech signals at the silent time-slots carry no information, while …"
- 收尾定位："Hence, the proposed DeepSC-S is a promising candidate for speech semantic communication systems."

## 9. 结论
- 1 段 150 词，现在时复述各设计 → 低 SNR 下优于基准 → "a promising candidate" 收尾。无数字、无未来工作。

## 10. Idea 拆解
- **基线**：DeepSC（tsp.2021.3071210，文本）；PCM + 传统信道编码；特征学习 + 传统信道编码。
- **增量**：把语义通信推广到语音，用 SE 注意力直接从原始语音学习语义特征并端到端训练（new-modality）。
- **为什么有效**："It is intuitive that speech signals at the silent time-slots carry no information, while …"——注意力自动给有效语音段更高权重。
- **证据**：AWGN、Rayleigh、Rician 下 SDR / PESQ 优于传统与半传统方案，低 SNR 时优势明显。
- **弱点**：任务仍是波形重建（语义层次有限）；单一数据集；模拟传输；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：面向识别 / 合成任务的语音语义通信（后续 twc.2023.3240969）；多说话人与噪声环境；数字化与低码率语音语义编码；与语音大模型结合。
