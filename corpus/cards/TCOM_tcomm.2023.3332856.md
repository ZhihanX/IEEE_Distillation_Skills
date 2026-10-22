---
doi: 10.1109/tcomm.2023.3332856
title: "Active RIS-Aided ISAC Systems: Beamforming Design and Performance Analysis"
journal: TCOM
year: 2024
band: 2022-2025
cites: 291
cites_per_year: 112.3
article_type: research
topic: RIS
source: xplore-html
xplore: 10319318
auto:
  words_total: 9474
  n_sections: 8
  n_subsections: 27
  n_figures: 11
  n_tables: 0
  n_display_eq: 75
  n_algorithms: 1
  statements: {theorem: 1, lemma: 6, proposition: 0, corollary: 0, remarks: 2, proof: 6, proof_in_appendix: 0}
  n_appendix: 2
  mean_sentence_words: 25.3
  we_per_1k: 10.3
  title_words: 9
  abstract_words: 169
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 1, roadmap: 1, however: 9, transition: 20, resultsShow: 0, motivatedBy: 2, toAddress: 9, gapWord: 0, nonconvex: 5, npHard: 0, closedForm: 0, outperform: 1, intensifier: 7, worthNoting: 2, observe: 6, thisIsBecause: 0, asExpected: 0, insight: 1, tradeoff: 0, figVerb: 3, promising: 3, gen: 1, contrast: 4, firstTime: 0, novel: 1, weProposeFirst: 2, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 7, AO: 5, SDR: 5, convergence: 5, convexOpt: 4, CRB: 1, MM: 1, SCA: 1}
code:
  title_pattern: [X-aided-Y, colon-subtitle]
  abstract_moves: [aim, aim, method, theory, theory, result, implication]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 7
  intro_moves: [field, prior, tech, prior, gap, solution, gap, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: numbered
  contrib_n: 4
  contrib_verbs: [investigate, propose, derive, validate]
  contrib_quantified: true
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [limitation, new-architecture]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [AO, MM, SDR, reformulation]
  theory_role: supporting
  proofs_location: mixed
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [iterations, number-of-elements, RIS-power, RIS-location, power-CDF, CSI-error, beampattern]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false   # 未来工作单独成节（"Practical Issues and Open Problems"），结论里不再写
---

## 1. 标题
- "[器件]-Aided [系统]: Beamforming Design and Performance Analysis"，9 词。冒号后"设计 + 分析"双任务，是 TCOM 常见副标题。

## 2. 摘要（7 句，169 词）
- "This paper considers an active reconfigurable intelligent surface (RIS)-aided integrated sensing and communication (ISAC) system."——最简锚点句，没有背景铺垫。
- 目标句（雷达 SINR 最大化 + 约束全列）→ 方法句（MM 处理非凸目标，四次问题用 SDR）→ 两句分析（缩放阶、功率分配与部署）→ 验证有源 RIS 优于无源 RIS。
- 末句："Additionally, we deliberate on several open problems that remain for future research."——摘要里预告"开放问题"一节。

## 3. 引言逻辑（7 段，约 1640 词）
1. ISAC 作为 6G 候选技术 → 两个视角论证 DFRC："From the spectrum resource perspective, … From the hardware deployment perspective, …"
2. ISAC 波形设计的分类：时 / 空 / 频分 → SCD、CCD、JD 三类，各自一句优缺点。
3. mmWave 遮挡 → RIS → RIS-ISAC 两类场景（RIS 只帮通信 / RIS 建立感知虚拟链路）逐篇综述 → "Nevertheless, due to the multiplicative fading effect, the equivalent path loss of the four-hop sensing link can be regarded as the product, rather than the sum, …"
4. 对抗四跳损耗的新架构（加传感器 / 有源 RIS）→ 命名新现象 "multiple-self-reflection (MSR)" → 已有有源 RIS-ISAC 工作 [34][35] 各自遗漏了什么（未考虑四跳回波、忽略 RIS 噪声、未计回波功耗）。
5. "Motivated by the above background, our contributions are summarized as follows:" + 4 条编号贡献（第 4 条含 "up to 70 dB"）。
6. 路线图；7. Notations。

## 4. Idea 是怎么提出的
- 空白类型：已有工作局限（逐篇点出遗漏的建模因素）+ 新架构（有源 RIS 用于四跳感知链路）。
- 写法亮点："product, rather than the sum" 一句把四跳链路的核心困难讲透，直接引出"放大"这一解法；对相近工作的批评落到具体的建模遗漏，而不是泛泛的"未研究"。
- 给新现象起名（MSR）方便后文引用。

## 5. 科研方法
- 模型：DFRC BS、有源 RIS（每单元配功放，引入热噪声与功耗约束）、点目标、UMi 路损；回波含 BS-RIS-BS 自干扰。
- 求解：MM 把雷达 SINR 目标化为双线性下界（Lemma 1）→ AO：W 用 MM-SDP（构造可行初始点，Lemma 2 给可行条件），Φ 化为 SOS 形式后 SDR；复杂度按内点法单列小节。
- 分析：简化为单天线雷达 → Lemma 4/5 上下界 + 夹逼定理得 Theorem 1（雷达 SINR 随 N 线性增长，"although the signal is reflected by the active RIS twice"）→ Lemma 6 功率分配 → 部署位置分析。定理后的 Remarks 给直观解释。
- 正文末单列 "Practical Issues and Open Problems"（有源 RIS 架构、宽带、信号处理）。

## 6. 仿真与实验
- 参数写在正文；方案以引号标签命名（'DFRC'、'Sens. only'、'Act. RIS'）；与无源 RIS 比较时计入硬件功耗以保证公平（"Both the hardware power consumption and the transmit power … are taken into consideration."）。
- 依次：不同自干扰下的收敛 → 近似 SINR vs N（验证缩放律）→ 有源 vs 无源 → 功率分配 → 部署位置 → 功率 CDF → 非理想 CSI（SINR 与和速率）→ 波束方向图。

## 7. 图表
- 11 图 0 表 1 算法。Fig. 1 系统图，Fig. 2 仿真布局。caption 短标签（"Radar SINR versus the location of the RIS x."）。

## 8. 句式库
- 双视角论证："From the spectrum resource perspective, … From the hardware deployment perspective, …"
- 核心难点："… the equivalent path loss of the four-hop sensing link can be regarded as the product, rather than the sum, of the path loss of …"
- 已有工作遗漏："Nevertheless, the noise and the interference induced by the active RIS were neglected in [35]."
- 动机 + 贡献："Motivated by the above background, our contributions are summarized as follows:"
- 定理直观解释："The scaling order can be intuitively explained as follows."
- 复杂度可接受："Remarks: It is worth noting that the existing studies on active RIS also exhibit a similar level of complexity [34]."

## 9. 结论
- 1 段 246 词，过去时复述 → 分析结论逐条（缩放阶 N、功率要仔细分配、靠近目标部署）→ "Overall, our study offered insights into … and highlighted the potential advantages of …"。无数字；未来工作放在前一节。
