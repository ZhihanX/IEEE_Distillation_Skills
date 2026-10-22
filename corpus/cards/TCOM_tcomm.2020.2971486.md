---
doi: 10.1109/tcomm.2020.2971486
title: "Reconfigurable Intelligent Surface-Based Index Modulation: A New Beyond MIMO Paradigm for 6G"
journal: TCOM
year: 2020
band: 2019-2021
cites: 777
cites_per_year: 120.9
article_type: research
topic: RIS
source: xplore-html
xplore: 8981888
auto:
  words_total: 4427
  n_sections: 6
  n_subsections: 6
  n_figures: 9
  n_tables: 0
  n_display_eq: 49
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, remark: 4, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 31.5
  we_per_1k: 14.4
  title_words: 12
  abstract_words: 197
  abstract_sentences: 6
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 0, roadmap: 1, however: 3, transition: 1, resultsShow: 0, motivatedBy: 1, toAddress: 0, gapWord: 0, nonconvex: 1, npHard: 0, closedForm: 0, outperform: 0, intensifier: 4, worthNoting: 6, observe: 1, thisIsBecause: 0, asExpected: 0, insight: 4, tradeoff: 1, figVerb: 0, promising: 3, gen: 6, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 5, convexOpt: 1}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [context, aim, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 7
  intro_moves: [field, tech, tech, prior, solution, aim, contrib, roadmap]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 4
  contrib_verbs: [propose, formulate, present, assess]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: none
  gap_type: [combination, new-architecture]
  motivating_figure: true
  problem_class: analysis-only
  solution: [closed-form, bound-surrogate]
  theory_role: central
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 2
  baseline_naming: acronym
  x_axes: [SNR, receive-antennas, spectral-efficiency, phase-error]
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[技术 A]-Based [技术 B]: A New Beyond MIMO Paradigm for 6G"，12 词。冒号后是愿景式副标题（"A New … Paradigm for 6G"），把一个具体方案定位成范式。

## 2. 摘要（6 句，197 词）
- 第 1 句 RIS 背景；"In this paper, we bring the concept of RIS-assisted communications to the realm of index modulation (IM) by proposing …"——"bring A to the realm of B" 式组合锚点。
- 第 3 句解释两种方案为什么好（反射增强 + 接收天线索引携带信息）。
- 检测器 + 统一 BEP 分析框架 → 仿真验证 → "Our findings also reveal that RIS-based IM, …, can become a potential candidate for future wireless communication systems in the context of beyond multiple-input multiple-output (MIMO) solutions."

## 3. 引言逻辑（7 段，约 1120 词；全文仅约 4400 词，偏短）
1. 时间锚点开场："As of the first quarter of 2020, the first commercial fifth generation (5G) wireless networks have been already deployed, …" → 6G 需要 "radically new communication paradigms in the physical layer"。
2. 控制传播环境的两类方案：基于可重构天线 / 散射体的 IM 方案、RIS。
3. RIS 与 MIMO / 波束成形 / 中继 / 反向散射都不同；借软件定义无线电的定义创造新术语 "software-defined surface (SDS)"。
4. 已有 RIS 工作逐篇一句（含作者自己的 SEP 分析与 RIS-AP 概念）+ 推荐综述。
5. IM 概念 → "The undeniable potential of both IM- and RIS-based communication schemes has been the main motivation of this study." → Fig. 1 给出三种可能实现（IM 作用于发端天线 / RIS 区域 / 收端天线），逐个说明前两种的缺点 → "we decided to focus on the third approach in this preliminary work."
6. "In this paper, we propose the visionary concept of RIS-based IM …" + 与 massive MIMO 的区别 + First / Second / Third / Finally 四点贡献（散文）。
7. 路线图。无记号段。

## 4. Idea 是怎么提出的
- 空白类型：组合（RIS × IM）+ 新架构。没有写"已有工作不足"，而是"两种技术潜力都大 → 结合"。
- 写法亮点：在引言里先摆出设计空间（三种概念实现，Fig. 1），再用一句话分别排除前两种（需要额外信令 / 降低有效增益），最后选第三种——把"为什么是这个设计"讲清楚。
- 自我定位为 "preliminary work"，并在结论里把另外两种实现列为开放问题——设计空间图同时生成了后续选题。

## 5. 科研方法
- 系统：RIS 作为 AP 的一部分反射近处射频源的未调制载波；按信息比特选择目标接收天线并对准其相位（RIS-SSK），RIS-SM 再叠加 M 阶调制。
- 两种检测器：贪婪（能量最大，非相干，无需信道估计）与 ML；比较复杂度。
- 误码分析：大 N 下用中心极限定理近似、PEP 上界、联合界；贪婪与 ML 分节推导；先推 RIS-SM 再令 x 为常数得 RIS-SSK（"To provide a more concise and intuitive presentation, …"）。
- 4 个 Remark 给出洞见（如贪婪检测下 PEP 与接收天线数无关，ML 下增加 nR 反而改善）。无定理环境。

## 6. 仿真与实验
- 参数写在正文；说明 "as usual practice, the large-scale path-loss is not considered since it is implicitly taken into account in the received SNR."
- 理论 vs 仿真（贪婪、ML）→ 两种检测器对比（"approximately 2 dB improvement"）→ 与 RIS-AP、传统 RSSK 对比 → 相位估计误差（von Mises 分布）。

## 7. 图表
- 9 图 0 表。Fig. 1 三种概念实现（a)(b)(c)），Fig. 2 两种方案框图。结果 caption 短标签（"Theoretical and computer simulation results for RIS-SSK with greedy detection."）。

## 8. 句式库
- 时间锚点："As of the first quarter of 2020, the first commercial fifth generation (5G) wireless networks have been already deployed, …"
- 范式需求："…, which necessitate radically new communication paradigms in the physical layer [2]."
- 组合锚点："In this paper, we bring the concept of RIS-assisted communications to the realm of index modulation (IM) by proposing …"
- 动机："The undeniable potential of both IM- and RIS-based communication schemes has been the main motivation of this study."
- 设计取舍："Since the first concept requires …, and the second concept reduces …, we decided to focus on the third approach in this preliminary work."
- 与主流方案区分："Different from emerging massive MIMO systems with fully digital or hybrid beamforming, our design neither requires multiple RF chains nor analog phase shifters …"

## 9. 结论
- 1 段 206 词，现在完成时（"has been proposed … It has been shown …"）→ 强判断："may be a game-changing paradigm for next-generation communication networks" → 开放问题（另两种 IM 实现、低复杂度接收机、非理想因素）→ "We also hope that the theoretical insights provided in this work may be useful for …"。无数字。
