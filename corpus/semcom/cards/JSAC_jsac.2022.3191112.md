---
doi: 10.1109/jsac.2022.3191112
title: "Performance Optimization for Semantic Communications: An Attention-Based Reinforcement Learning Approach"
journal: JSAC
year: 2022
band: 2022-2025
cites: 226
cites_per_year: 55.2
article_type: research
topic: semantic
source: xplore-html
xplore: 9832831
auto:
  words_total: 6585
  n_sections: 5
  n_subsections: 11
  n_figures: 12
  n_tables: 2
  n_display_eq: 24
  n_algorithms: 1
  statements: {theorem: 0, lemma: 1, proposition: 0, corollary: 0, proof: 1, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.7
  we_per_1k: 9.8
  title_words: 10
  abstract_words: 294
  abstract_sentences: 12
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 2, roadmap: 1, however: 5, transition: 1, resultsShow: 2, motivatedBy: 0, toAddress: 2, gapWord: 0, nonconvex: 1, npHard: 0, closedForm: 0, outperform: 0, intensifier: 4, worthNoting: 0, observe: 15, thisIsBecause: 2, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 1, promising: 0, gen: 0, contrast: 6, firstTime: 0, novel: 1, weProposeFirst: 2, wlog: 0, code: 0, prototype: 0}
  methods: {convergence: 15, complexity: 9, penalty: 6, DNN: 5, DRL: 2}
  domain: {attention: 19, accuracy: 11, BLEU: 5, knowledgeBase: 3}
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [aim, model, model, model, metric, gap, problem, problem, method, method, method, result]
  abstract_has_numbers: true            # 减少 41.3% 数据、总 MSS 提升两倍
  abstract_anchor: in-this-paper
  intro_paragraphs: 5
  intro_moves: [field, prior-gap, prior-gap, contrib, roadmap]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [consider, propose, formulate, propose, analyze]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: table                       # Table I
  gap_type: [new-metric, resource-allocation]
  motivating_figure: true
  problem_class: mixed-integer          # RB 分配（离散）+ 语义三元组选择
  solution: [RL]                        # 注意力 + PPO（APPO）
  theory_role: supporting               # 收敛性（Lemma 1，沿用 [33]）
  proofs_location: inline
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true                 # Table II
  baselines_n: 5                        # APG、ADQN、传原文、随机选三元组等
  baseline_naming: descriptive
  x_axes: [iterations, RBs, users, masked-ratio, tokens]
  fig1_role: framework
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
semcom:
  category: networking
  source: [text]
  task: [reconstruction]                # 知识图谱三元组 → 图到文本生成
  paradigm: knowledge-based
  architecture: [attention, transformer, RL]
  channel: [OFDMA, Rayleigh]
  adaptivity: [resource-allocation]
  training: [RL]
  metrics: [custom, BLEU]               # 语义相似度指标 MSS（准确性 + 完整性）
  datasets: [AGENDA, DocRED]
  baselines: [separate, optimization, own-ablation]
  snr_mismatch_test: false
  complexity_reported: true
  digital_compatible: true              # 三元组以 token / 比特传输
  hardware_validation: false
  theory: none
  idea_delta: [system-optimization, new-metric, knowledge-base]
  builds_on: [knowledge graph extraction, graph-to-text generation, PPO]
  open_problems_n: 0
---

## 1. 标题
- "Performance Optimization for Semantic Communications: An [方法] Approach"，10 词。网络优化类论文的典型标题（"Performance Optimization for X"）。

## 2. 摘要（12 句，294 词，很长）
- 框架 → 系统模型三句（BS 抽取语义、知识图谱三元组、用户图到文本恢复）→ 指标 MSS → 资源受限 → BS 需选 RB 并选部分语义 → 优化问题 → APPO → 注意力评估三元组重要性 → 动态学习率保证收敛 → 结果带数字（41.3%、两倍）。

## 3. 引言逻辑（5 段）
- 海量数据需求 → 语义通信 → "However, deploying semantic communications in wireless networks faces several challenges including …"（列 5 个挑战）。
- 相关工作按缺陷逐条批评：自编码器输出"对人类不可理解"；控制信号不适用于文本 / 图像；没有语义度量；已有度量只看正确性不看完整性；都假设全部语义可传；传统资源分配不考虑语义 → 贡献 5 条 → 路线图。

## 4. Idea 是怎么提出的
- 空白类型：新指标（准确性 + 完整性的语义相似度）+ 资源分配（语义感知的 RB 分配与部分语义选择）。
- 核心洞见：把语义信息显式化为知识图谱三元组（可解释、可计数、可裁剪），资源不足时只传"重要的"三元组——"语义选择"与"无线资源分配"联合成一个优化问题；三元组重要性由注意力网络（三元组与原文 token 的相关度）给出，作为 RL 状态。
- 网络 / 资源优化型语义论文的模板：定义语义度量 → 以其为目标 → 资源约束 → 学习型求解。

## 5. 科研方法
- 四阶段：语义抽取（实体识别 + 关系抽取 → 三元组）→ 语义导向资源分配与语义选择（OFDMA RB）→ 图到文本恢复 → 语义相似度评估。
- MSS = φ·准确性 + (1−φ)·完整性（基于 token 出现次数）。
- 问题：最大化总 MSS，满足时延约束（非凸、目标与变量关系难以显式刻画）。
- APPO：注意力网络（输入层、隐藏层相关度、输出层、softmax）→ PPO（状态 = 重要性分布、动作 = RB 分配、奖励 = 总 MSS）+ 动态学习率 → 复杂度与收敛（Lemma 1）。

## 6. 仿真与实验
- 单 BS、30 用户；AGENDA 与 DocRED 文本；基准 APG（会议版）、ADQN、传原文、随机选三元组等。
- 三元组与原文相关度示例（Fig. 4–6）→ 数据量减少比例 → 不同指标训练的恢复文本 → 收敛（10 次独立运行均值 ± 标准差）→ 总 MSS vs RB 数、用户数、遮挡比例。

## 7. 图表
- 12 图 2 表 1 算法。Fig. 2、5、6 用具体文本 + 彩色三元组展示语义抽取与选择——让"语义"可见；Fig. 9 带阴影的收敛曲线。

## 8. 句式库
- 挑战清单："However, deploying semantic communications in wireless networks faces several challenges including extraction of data meaning, semantic-oriented resource allocation, semantic encoding and decoding, measurement of semantic communication performance, and …"
- 批评自编码器语义："However, the output of the autoencoder being a vector of decimals is incomprehensible for humans and does not have any physical meaning."
- 批评度量不完整："While interesting, the metrics developed in [10]–​[13] only capture whether the information in the received data is correct without guaranteeing that the received data contains all the information …"
- 资源约束动机："In practice, due to wireless resource limitations (e.g., bandwidth), the BS may not be able to transmit the entire semantic information to all users [14]."
- 传统资源分配不适用："However, the solutions in these existing works [15]–​[19] cannot be applied in semantic communications since they do not consider the effects of semantic information extraction and transmission on resource allocation."

## 9. 结论
- 1 段 209 词：现在完成时复述各环节 + 与传统 RL 的对比；无数字、无未来工作。

## 10. Idea 拆解
- **基线**：会议版 APG；传统资源分配（不考虑语义）；传原文的标准通信。
- **增量**：知识图谱显式语义 + 准确性 / 完整性兼顾的 MSS 指标 + 注意力 PPO 联合优化 RB 分配与语义三元组选择（system-optimization + new-metric + knowledge-base）。
- **为什么有效**：三元组远比原文短（数据量降 41.3%）；注意力给出三元组重要性，使资源不足时优先传重要语义。
- **证据**：总 MSS 是标准通信的两倍；收敛更快更稳；对遮挡 token 鲁棒。
- **弱点**：信道只影响 RB 速率 / 时延（语义传输本身视为无错）；MSS 基于 token 计数，语义深度有限；依赖外部抽取 / 生成模型的质量；无未来工作讨论。
- **开放问题**（论文未写，均为推断）：
  - 推断：传输错误对三元组 / 知识图谱的影响与纠错；多模态知识图谱；收发两端知识图谱不一致；语义度量与人类评价的一致性检验；能效目标（后续 jsac.2023.3240713）。
