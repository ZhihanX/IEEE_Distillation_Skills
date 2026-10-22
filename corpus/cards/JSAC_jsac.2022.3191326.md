---
doi: 10.1109/jsac.2022.3191326
title: "Task-Oriented Multi-User Semantic Communications"
journal: JSAC
year: 2022
band: 2022-2025
cites: 464
cites_per_year: 113.4
article_type: research
topic: semantic
source: xplore-html
xplore: 9830752
auto:
  words_total: 6723
  n_sections: 7
  n_subsections: 26
  n_figures: 9
  n_tables: 3
  n_display_eq: 15
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 25.4
  we_per_1k: 6.2
  title_words: 4
  abstract_words: 219
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 1, however: 2, transition: 8, resultsShow: 1, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 12, intensifier: 4, worthNoting: 0, observe: 0, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 1, promising: 0, gen: 0, contrast: 10, firstTime: 0, novel: 2, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 8, convergence: 2, DNN: 1}
code:
  title_pattern: [noun-phrase]
  abstract_moves: [gap, aim, method, method, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, tech, prior, gap, gap, contrib, roadmap, notation]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, demonstrate, propose, show]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario, unification]
  motivating_figure: true
  problem_class: learning
  solution: [DNN]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4
  baseline_naming: descriptive
  x_axes: [SNR, number-of-users]
  fig1_role: framework
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: true
  conclusion_future_work: false
semcom:
  category: task-multiuser
  source: [image, text]
  task: [retrieval, translation, VQA]
  paradigm: task-feature
  architecture: [transformer]
  channel: [MIMO]                          # 多天线接收机 L-MMSE 检测
  adaptivity: [none]
  training: [multi-stage]
  metrics: [Recall@1, BLEU, accuracy]
  datasets: [CUB-200-2011, WMT2018, CLEVR]
  baselines: [separate, other-learned]
  snr_mismatch_test: false
  complexity_reported: true
  digital_compatible: false
  hardware_validation: false
  theory: none
  idea_delta: [multi-user, new-task, new-modality]
  builds_on: [DeepSC, Transformer, MU-DeepSC (conference version)]
  open_problems_n: 0
---

## 1. 标题
- 4 词名词短语："Task-Oriented Multi-User Semantic Communications"。两个限定词（task-oriented、multi-user）就是对已有工作（单用户、重建型）的两处扩展。

## 2. 摘要（9 句，219 词）
- 首句就是空白（让步式）："While semantic communications have shown the potential in the case of single-modal single-users, its applications to the multi-user scenario remain limited."
- "In this paper, we investigate …" → 三个任务作为案例 → 统一 Transformer 框架 → 三个模型（DeepSC-IR / MT / VQA，命名带系列前缀）→ 一个新结构（layer-wise Transformer）。
- 结果句列出四个维度的优势（鲁棒性、复杂度、时延、任务指标），无数字。

## 3. 引言逻辑（8 段，约 1000 词）
1. 传统通信是"管道" → 数据爆炸 → 两条出路（硬件 / 软件）→ "In this work, we investigate the second approach."（先在大分类里定位）。
2. 语义通信定义 → 已有工作分两类（重建 / 任务执行）。
3–4. 两类各自逐篇综述（作者名 + 年份式："Farsad et al. [8] designed …"）→ "The prior works explore the possibility of semantic communications for transmitting signals in a single-modal single-user system. However, in practice, …" → 自己的会议版（MU-DeepSC）→ "However, a unified framework to support various tasks with multimodal data is still missing …"
5. 区分单模态多用户与多模态多用户 → "we face the following challenges:" + 编号三问（Q1 如何提取语义、Q2 如何抑制用户间干扰、Q3 如何融合多模态）。
6. "In this paper, we investigate …"（选三个代表任务作案例）→ 4 条贡献，前三条末尾分别写 "This addresses the aforementioned Q1 / Q2 / Q3."
7. 路线图；8. Notation。
- 第 II 节 "Related Works" 实际是三个任务的背景定义。

## 4. Idea 是怎么提出的
- 空白类型：新场景（多用户、多模态）+ 统一框架（一个发射机结构服务多种任务）。
- 写法亮点：把挑战写成编号问题（Q1–Q3），贡献逐条回指问题——审稿人可以一一核对"问题是否被解决"。
- 期刊版在会议版基础上的扩展有交代（会议版只做了 VQA、用 LSTM / CNN）。

## 5. 科研方法
- 纯学习型：Transformer 发射机（语义编码 + JSC 编码）、多天线接收机 L-MMSE 检测后分任务解码。
- 每个模型给训练算法（分阶段训练：先语义编码器、再 JSC 编解码器、再整体微调）。
- 无定理；附录放 Transformer 预备知识。

## 6. 仿真与实验
- 交代数据集（四个图像检索集、WMT 2018 中英、CLEVR）、训练超参数、开源实现来源。
- 四类基准：无差错上界、半传统（语义特征 + LDPC）、传统（JPEG/UTF-8 + LDPC/Turbo）、混合方案。
- 任务指标各不同（Recall@1、BLEU、答案准确率）；另用两张表比较发送符号数和复杂度。

## 7. 图表
- 9 图 3 表 2 算法。Fig. 1 整体框架，Fig. 2–4 网络结构图。
- caption 描述型，写明对比对象、调制方式、数据集："Recall@1 comparison between DeepSC-IR and JPEG-LDPC with 8-QAM over different channels, in which the dataset is CUB-200-2011."

## 8. 句式库
- 让步式空白："While semantic communications have shown the potential in the case of single-modal single-users, its applications to the multi-user scenario remain limited."
- 定位路线："There exist two ways to address this problem: 1) …; 2) … In this work, we investigate the second approach."
- 现实需求："However, in practice, we must gather multimodal data from different users/devices, transmit over the air, and process/fuse multimodal data at the receiver."
- 缺失："However, a unified framework to support various tasks with multimodal data is still missing in multi-user semantic communications."
- 挑战引导："For the design of multi-user semantic communications, we face the following challenges:"
- 回指："This addresses the aforementioned Q1."

## 9. 结论
- 1 段 188 词：现在完成时复述 → 给出数字（18 dB 增益、符号数减少 50% 以上、DeepSC-IR 仅需千分之一符号）→ 结论性判断（"an attractive alternative to traditional communication systems for particular tasks"）。无未来工作。

## 10. Idea 拆解
- **基线**：单模态单用户语义通信（DeepSC、DeepSC-S 等）；会议版 MU-DeepSC（只做 VQA，LSTM / CNN）。
- **增量**：统一的 Transformer 发射机框架服务多用户、多模态任务（检索、翻译、VQA），接收端多天线检测后分任务解码，并提出逐层 Transformer 融合多模态（multi-user + new-task + new-modality）。
- **为什么有效**：任务导向只传任务相关特征，所需符号数大幅减少；多天线检测抑制用户间干扰；逐层融合充分利用多模态互补信息。
- **证据**：结论给出 18 dB 增益、符号数减少 50% 以上、检索任务仅需千分之一符号。
- **弱点**：用户数与任务固定；多用户干扰靠线性检测处理，未联合设计多址；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：语义感知的多址与资源分配（见 tccn.2023.3326302、jsac.2022.3222000）；用户 / 任务动态变化；统一多任务模型（后续 tcomm.2024.3364990）；数字化与隐私（多用户特征泄露）。
