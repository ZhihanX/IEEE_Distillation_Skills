---
doi: 10.1109/twc.2018.2803045
title: "MU-MIMO Communications With MIMO Radar: From Co-Existence to Joint Transmission"
journal: TWC
year: 2018
band: 2016-2018
cites: 951
cites_per_year: 111.8
article_type: research
topic: ISAC-sensing
source: xplore-html
xplore: 8288677
auto:
  words_total: 6838
  n_sections: 7
  n_subsections: 23
  n_figures: 12
  n_tables: 3
  n_display_eq: 62
  n_algorithms: 3
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, remark: 1, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 28.5
  we_per_1k: 11.9
  title_words: 10
  abstract_words: 197
  abstract_sentences: 8
  phrases: {toTheBest: 0, inThisPaper: 3, contribList: 1, roadmap: 3, however: 3, transition: 2, resultsShow: 2, motivatedBy: 2, toAddress: 6, gapWord: 0, nonconvex: 6, npHard: 0, closedForm: 1, outperform: 3, intensifier: 1, worthNoting: 2, observe: 7, thisIsBecause: 0, asExpected: 1, insight: 0, tradeoff: 9, figVerb: 1, promising: 0, gen: 0, contrast: 4, firstTime: 0, novel: 3, weProposeFirst: 2, wlog: 0, code: 0, prototype: 0}
  methods: {penalty: 23, manifold: 19, complexity: 18, SDR: 9, convergence: 5, convexOpt: 2, monteCarlo: 1}
code:
  title_pattern: [X-with-Y, colon-subtitle]
  abstract_moves: [aim, method, method, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: none
  intro_paragraphs: 11
  intro_moves: [field, prior, prior, gap, prior, gap, aim, approach, approach, approach, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [propose, design, reformulate, derive]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [limitation, new-architecture]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [SDR, penalty, manifold, gradient]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [beampattern-angle, PSLR-SINR-tradeoff, number-of-users, SINR-distribution, iterations, execution-time]
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false   # 未来工作（接收机设计、时空联合处理）在引言里交代
---

## 1. 标题
- "[通信] With [雷达]: From [旧范式] to [新范式]"，10 词。副标题 "From Co-Existence to Joint Transmission" 用演进叙事概括全文两种部署方案（分离 → 共享），也概括了领域走向。

## 2. 摘要（8 句，197 词）
- 没有 "In this paper"：首句即 "Beamforming techniques are proposed for a joint multi-input-multi-output (MIMO) radar-communication (RadCom) system, where a single device acts as radar and a communication base station …"
- 两种运行方式按顺序展开："we first split the antennas into two groups …" → 雷达信号落在下行信道零空间 → 通信波束匹配雷达方向图 → "To reduce the optimizations' constraints, we consider a second operational option, where all the antennas transmit a joint waveform …"
- 罚项化 + 流形算法 → 结果：共享部署显著优于分离部署；加权优化性能接近原问题但复杂度低得多。无数字。

## 3. 引言逻辑（11 段，约 1540 词；内分 A. Co-Existence / B. Co-Design / C. The Contribution of Our Work）
1. 频谱稀缺（2020 年 200 亿设备）→ S/C 波段雷达频谱可共享 → "Existing contributions on CRSS mainly focus on two aspects: 1) co-existence … and 2) co-design …"——第 1 段就给出文献分类并预告下文。
2. （A）机会式共享 → 零空间投影（NSP）开创工作 → "However, such a beamformer may result in performance loss for the radar." → 放松零迫的折中工作。
3. 基于优化的共存工作（含作者自己的鲁棒设计与 MUI 利用）。
4. （B）共存需要交换边信息、需要控制中心 → "In practical scenarios, however, such a control center imposes extra complexity on the system, …" → 双功能系统更有利。
5. 联合设计：信息论框架、雷达信息速率、波形设计（单天线 TD/啁啾/OFDM；MIMO 旁瓣控制 / 波形分集）→ "It should be highlighted that in the above MIMO schemes, each communication symbol is typically represented by one or several radar pulses, which unfortunately leads to a low date rate …"
6. （C）"In this paper, we develop a series of optimization-based transmit beamforming approaches …"：与波形设计的区别（空间处理、不改调制、数据率不变）+ 明确范围："…, we only focus our attention on the joint transmission …, and set aside the receiver designs as well as the temporal techniques for our future work."
7. 分离部署（受 NSP 启发）。8. 共享部署（减少约束）。9. 加权优化 + 流形算法 + flops 复杂度 → 4 条 bullet。
10. 路线图；11. Notations。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（共存需边信息与控制中心；双功能波形数据率低）+ 新架构（共享天线的联合发射）。
- 写法亮点：两种方案本身就构成"从共存到联合"的演进：先给受 NSP 启发的保守方案，再以"减少约束"为理由提出更激进的共享方案，最后再为共享方案降复杂度——三步各对应一段。
- 主动划界：在引言中声明只做发射端、接收端与时空联合处理留作未来工作。

## 5. 科研方法
- 设计要求用 bullet 列出（逼近期望雷达方向图 / 保证下行 SINR / 满足功率）。
- 雷达方向图设计沿用 Stoica 等人的两种经典问题；分离部署：零迫 + 方向图匹配 → SDR（Algorithm 1）。
- 共享部署："the radar's targets of interest can be viewed as virtual downlink users located in a line-of-sight (LoS) channel."；问题 (20) 之后用 "Observation 1/2/3" 列出其缺点（维度大、SDR 难满足逐天线等式约束、用户多时不可行）→ 引出罚项化。
- 两种 SINR 罚项（平方和、最大）× 两种功率约束（总 / 逐天线）→ 可行域为黎曼流形 → 黎曼共轭梯度（Fig. 2 图示切空间与回缩）；Remark 对比 SDR（在半正定锥上搜索再秩一近似）与本文直接在超球面上搜索。
- 单列 "Complexity Analysis" 节，按 flops 计算；坦言 SDR 无闭式复杂度表达，只能仿真比较。

## 6. 仿真与实验
- Monte-Carlo；参数写在正文；方案用引号标签（'Radar-Only'、'RadCom'、'Constrainted'）。
- 分离 vs 共享（多波束、3 dB 主瓣方向图；PSLR-SINR 权衡，共享部署 PSLR 增益 8 dB）→ 约束问题 vs 罚项问题可行概率 → 各加权方法的雷达-通信权衡（Table II/III 给权重向量）→ 实际 SINR 分布 → 收敛速度、执行时间、性能-复杂度权衡。

## 7. 图表
- 12 图 3 表 3 算法。Fig. 1 两种天线部署（a)(b)），Fig. 2 黎曼共轭梯度示意，Table I 每次迭代复杂度。结果 caption 短标签 + 参数（"Trade-off between PSLR and SINR for different methods, K = 10."）。

## 8. 句式库
- 文献二分预告："Existing contributions on CRSS mainly focus on two aspects: 1) co-existence of existing radar and communication devices and 2) co-design for dual-functional systems."
- 开创工作的代价："However, such a beamformer may result in performance loss for the radar."
- 现实困难："In practical scenarios, however, such a control center imposes extra complexity on the system, and is also a challenge to implement."
- 已有方案的硬伤："… each communication symbol is typically represented by one or several radar pulses, which unfortunately leads to a low date rate on the order of the radar pulse repetition frequency (PRF) …"
- 主动划界："…, we only focus our attention on the joint transmission of the RadCom system in this paper, and set aside the receiver designs … for our future work."
- 类比转化："By using the shared deployment, the radar's targets of interest can be viewed as virtual downlink users located in a line-of-sight (LoS) channel."

## 9. 结论
- 1 段 146 词，混合时态（"A novel framework is proposed …"；"We have considered …"）→ 两条结论（共享优于分离；加权优化带来有利的性能-复杂度权衡）。无数字、无未来工作。
