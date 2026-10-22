---
doi: 10.1109/tcomm.2025.3541027
title: "Networked ISAC for Low-Altitude Economy: Coordinated Transmit Beamforming and UAV Trajectory Design"
journal: TCOM
year: 2025
band: 2022-2025
cites: 110
cites_per_year: 93.6
article_type: research
topic: ISAC-sensing
source: xplore-html
xplore: 10879807
auto:
  words_total: 6338
  n_sections: 6
  n_subsections: 13
  n_figures: 8
  n_tables: 0
  n_display_eq: 48
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 2, corollary: 0, proof: 2, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 25.2
  we_per_1k: 15.3
  title_words: 12
  abstract_words: 301
  abstract_sentences: 9
  phrases: {toTheBest: 0, inThisPaper: 2, contribList: 0, roadmap: 1, however: 6, transition: 10, resultsShow: 2, motivatedBy: 0, toAddress: 9, gapWord: 2, nonconvex: 11, npHard: 0, closedForm: 0, outperform: 2, intensifier: 7, worthNoting: 1, observe: 9, thisIsBecause: 3, asExpected: 0, insight: 0, tradeoff: 3, figVerb: 6, promising: 0, gen: 1, contrast: 2, firstTime: 0, novel: 0, weProposeFirst: 2, wlog: 1, code: 0, prototype: 0}
  # contribList 0：贡献列表引导句为 "The main results are summarized in the following:"，提取器未匹配
  methods: {SCA: 16, SDR: 8, AO: 7, convergence: 6, complexity: 5, convexOpt: 1}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [aim, method, method, method, method, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: this-paper-verb
  intro_paragraphs: 8
  intro_moves: [field, tech, prior, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [consider, optimize, provide]
  contrib_quantified: false
  first_claim: false           # 只有 "has not been investigated in the literature yet" 式空白声明
  roadmap: true
  notation: intro-end
  gap_type: [new-scenario]
  motivating_figure: true
  problem_class: MINLP
  solution: [AO, SCA, SDR]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [iterations, trajectory-map, sensing-threshold]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1     # 另附 4 条带粗体小标题的未来方向 bullet
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[技术] for [新应用]: [设计变量 1] and [设计变量 2] Design"，12 词。主标题给"技术 + 新应用场景"（LAE 是 2024 年后的热词），副标题列出优化变量——典型的"场景主标题 + 变量副标题"。

## 2. 摘要（9 句，301 词）
- "This paper exploits the networked integrated sensing and communications (ISAC) to support low-altitude economy (LAE), in which …"（一句交代整个场景，60 余词）。
- 两个设定维度（ULA 水平 / 垂直放置；两类 UAV 接收机能否消除感知干扰）→ "Under each setup, we jointly design …" → 目标与约束 → "These problems are highly non-convex and challenging to solve, due to …"（给出两个难点原因）→ AO + SCA + SDR。
- 结果两句："… efficiently balance the sensing-communication performance tradeoffs and significantly outperform various benchmarks." + 设计洞见（水平天线更好、具备干扰消除能力的接收机更有利）。无数字。

## 3. 引言逻辑（8 段，约 1320 词）
1. LAE 定义与愿景 → "The successful implementation of LAE, however, requires the safe operation of various aircraft." → 通信与感知双需求。
2. ISAC 是 6G 关键技术 → 网络化 ISAC → "Compared with conventional ISAC systems with isolated transceivers, networked ISAC offers several advantages. First, … Next, … Furthermore, …"（列优势）。
3. 已有工作 "On the one hand"（蜂窝连接 UAV）/ "On the other hand"（GBS 为 UAV 提供 ISAC）→ "However, these works only considered …" → "The research on using terrestrial networked ISAC systems to support LAE has not been investigated in the literature yet."
4. "It is worth noting that there is another line of research on UAV-assisted ISAC, …" → "However, these prior works are not applicable for terrestrial ISAC supporting LAE, …"（排除相近方向）。
5. "Different from prior works, this paper studies …" → "However, the efficient design … is particularly challenging. First, … Next, … Furthermore, …"（三个技术难点）→ "Therefore, we are motivated to address the above challenges in this work."
6. 3 条 bullet "main results"；7. 路线图；8. Notations。

## 4. Idea 是怎么提出的
- 空白类型：新场景（地面网络化 ISAC 服务低空经济：通信对象与感知目标都在 3D 空中）。
- 写法亮点："新场景的需求 → 新技术的优势（First/Next/Furthermore）→ 两条相关研究线都不适用 → 本文场景的三个难点（First/Next/Furthermore）"，用对称的列举结构组织引言；空白声明落在"场景未被研究"而不是"方法有缺陷"。
- 把设计维度（天线放置 × 接收机类型）做成 2×2 的四种情形，得出可操作的部署结论。

## 5. 科研方法
- 模型：M 个 GBS（ULA，水平或垂直）+ K 个授权 UAV（单天线）；时隙化飞行周期；联合信息信号 + 专用感知信号；两类接收机（Type-I 传统、Type-II 可消除感知干扰）；感知指标为目标区域的照射功率。
- 问题：(P1)–(P4) 四种情形，最大化平均和速率，约束为照射功率、GBS 功率、飞行约束（速度、防碰撞）与二进制关联——混合整数非凸。
- 求解：AO 三块——关联（利用结构可最优求解的整数规划）、波束成形（SCA + SDR，Proposition 1/2 由非秩一解构造等价秩一解）、轨迹（一阶 Taylor + 信任域约束保证近似精度）；单独小节做复杂度分析；Case 1 详解后，其他三种情形一节内说明差异。

## 6. 仿真与实验
- 参数写在正文（3 GBS、400 m × 400 m、每 GBS 4 天线）；2 个基准（直线飞行 + 波束成形；各向同性发射 + 功率与轨迹联合设计），bullet 定义。
- 收敛（约 15 次迭代）→ Type-I / Type-II 的照射功率热图 + 轨迹 → 关联随时隙变化 → 基准的热图与轨迹 → 3 UAV 3 GBS 场景 → 和速率 vs 感知门限（权衡曲线）。

## 7. 图表
- 8 图 0 表。Fig. 1 场景示意（授权 UAV + 非授权目标）；多数结果图为"照射功率热图 + 轨迹叠加"的地图式可视化，caption 解释图例（"the carmine '+' denote the authorized UAVs location …, and the arrow … correspond to their association relationship"）。

## 8. 句式库
- 新范式的前提："The successful implementation of LAE, however, requires the safe operation of various aircraft."
- 列优势："Compared with conventional ISAC systems with isolated transceivers, networked ISAC offers several advantages."
- 场景空白："The research on using terrestrial networked ISAC systems to support LAE has not been investigated in the literature yet."
- 排除相邻方向："However, these prior works are not applicable for terrestrial ISAC supporting LAE, in which …"
- 难点引出："However, the efficient design of cooperative transmit beamforming at GBSs and trajectory optimization of authorized UAVs is particularly challenging."
- 动机收束："Therefore, we are motivated to address the above challenges in this work."
- 补充（skill 引用）："Illustration of networked ISAC for communicating with authorized UAVs and monitoring of unauthorized objects in 3D space."
- 补充（skill 引用）："… the carmine '+' denote the authorized UAVs location of this time slot, and the arrow associated with each authorized UAV and GBS correspond to their association relationship."
- 补充（skill 引用）："Section II presents the networked ISAC model for LAE and formulates the problem."
- 补充（skill 引用）："Notations: Lowercase and uppercase letters with boldface refer to vectors and matrices, respectively."
- 补充（skill 引用）："The authors in [11] exploited the cellular-connected UAV to enable bi-static sensing with GBS."
- 补充（skill 引用）："It is observed that the average sum rate achieved by the proposed design quickly increased with the number of iterations and converged in about 15 iterations."
- 补充（skill 引用）："These problems are highly non-convex and challenging to solve, due to the involvement of binary UAV-GBS association variables …"
- 补充（skill 引用）："To solve these non-convex problems, we propose efficient algorithms by using the techniques of alternating optimization, successive convex approximation, and semi-definite relaxation."

## 9. 结论
- "Concluding Remarks"：1 段 207 词，过去时复述 → 两条设计洞见 → "In the following, we discuss some interesting issues that are unaddressed in this paper to motivate future works." → 4 条带粗体标题的未来方向 bullet（不完美干扰消除、GBS 部署优化、IRS 辅助、多模态感知）。无数字。
