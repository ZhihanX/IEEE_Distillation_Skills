---
doi: 10.1109/jsac.2020.3007043
title: "Robust and Secure Wireless Communications via Intelligent Reflecting Surfaces"
journal: JSAC
year: 2020
band: 2019-2021
cites: 773
cites_per_year: 130.5
article_type: research
topic: RIS
source: xplore-html
xplore: 9133130
auto:
  words_total: 8130
  n_sections: 6
  n_subsections: 18
  n_figures: 9
  n_tables: 1
  n_display_eq: 46
  n_algorithms: 1
  statements: {theorem: 1, lemma: 1, proposition: 2, corollary: 0, remark: 3, proof: 3, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 26.3
  we_per_1k: 11.5
  title_words: 9
  abstract_words: 207
  abstract_sentences: 8
  phrases: {toTheBest: 2, inThisPaper: 5, contribList: 0, roadmap: 1, however: 8, transition: 18, resultsShow: 2, motivatedBy: 0, toAddress: 12, gapWord: 1, nonconvex: 15, npHard: 0, closedForm: 0, outperform: 2, intensifier: 8, worthNoting: 0, observe: 0, thisIsBecause: 2, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 3, promising: 0, gen: 0, contrast: 3, firstTime: 0, novel: 0, weProposeFirst: 2, wlog: 1, code: 0, prototype: 0}
  # roadmap 1 次是 "in the rest of this paper, we drop index …" 误匹配；文中没有路线图段
  methods: {SDR: 10, AO: 9, convergence: 7, SCA: 6, convexOpt: 4, lagrange: 4, penalty: 4, KKT: 2, complexity: 2, MM: 1, manifold: 1}
code:
  title_pattern: [X-via-Y]
  abstract_moves: [aim, context, method, aim, method, method, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 5
  intro_moves: [field, gap, tech, prior, gap, aim, contrib, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 3
  contrib_verbs: [formulate, develop, reveal]
  contrib_quantified: false
  first_claim: true
  roadmap: false
  notation: intro-end
  gap_type: [limitation, practicality]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [AO, SCA, SDR, penalty, reformulation]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 2
  baseline_naming: descriptive
  x_axes: [iterations, transmit-power, leakage-threshold, number-of-antennas, number-of-users, CSI-error, IRS-element-split]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "Robust and Secure [通信] via [技术]"，9 词。两个形容词（Robust、Secure）分别对应本文的两个设计要素（非理想 CSI、物理层安全），"via" 引出使能技术。

## 2. 摘要（8 句，207 词）
- "In this paper, intelligent reflecting surfaces (IRSs) are employed to enhance the physical layer security in a challenging radio environment."——被动锚点句，同时用 "challenging" 预告场景难度。
- 第 2 句把"难"具体化：用户无 LoS、多个多天线窃听者、窃听信道 CSI 不完美。
- AN → 联合设计 → 鲁棒非凸问题 → "an efficient algorithm is developed by capitalizing on alternating optimization, a penalty-based approach, successive convex approximation, and semidefinite relaxation."（一句列全技术栈）。
- 两句结果，第二句是部署洞见："uniformly distributing the reflecting elements among multiple IRSs is preferable over deploying them at a single IRS."

## 3. 引言逻辑（5 段，约 1490 词；无路线图）
1. 无线广播 / 叠加特性 → 物理层安全 → 已有手段（协作中继、AN、协作干扰）→ "However, these existing approaches have two main demerits. First, … Second, …" → 需要能塑造传播环境的新范式。
2. 超表面 / IRS 的特性与优势（无源、可贴在建筑上）→ "However, to fully unleash the potential of IRSs for security provisioning, joint optimization of … is required."
3. IRS + 安全的已有工作：逐篇写求解方法（SDR、MM、流形、凸近似"may lead to a significant performance loss"）→ 共同假设：单天线窃听者 + 完美窃听 CSI → 用两条理由说明这是 "overly optimistic" → 首创声明。
4. "To address the aforementioned issues, this paper investigates …"：场景 → 目标 → 两大难点（单模约束、无穷多不等式约束）→ 方法链 → 结果与洞见（贡献以散文写出，无列表）。
5. Notations。

## 4. Idea 是怎么提出的
- 空白类型：已有工作局限 + 实用性（已有 IRS 安全工作的窃听者模型太乐观）。
- 写法亮点：用"最坏情况"原则给自己的设定背书——"in practice, a worst-case assumption is needed for successful security provisioning"；Remark 1/3 在模型节再次重申该假设的合理性。
- 两层 "However"：第 1 段否定传统安全手段（成本高、恶劣环境下无效），第 3 段否定已有 IRS 安全工作（假设乐观）——先立技术、再立设定。

## 5. 科研方法
- 系统：多天线 AP、K 个无直达链路的合法用户、J 个多天线漫游用户（潜在窃听者）、L 个 IRS；窃听信道有界误差模型；最坏情况鲁棒和速率最大化（WCR-SRM），约束信息泄漏。
- AO 的选用先给理由："AO is a widely applicable and empirically efficient approach for handling optimization problems involving coupled optimization variables."（并列举其成功应用）。
- 子问题 1：Proposition 1 把泄漏约束化为 LMI，广义 S-procedure（Lemma 1）消去无穷多约束，SCA 处理非凸目标，Theorem 1 证明 SDR 紧。
- 子问题 2：单模约束 → 秩一约束 → d.c. 表示 + 罚项（Proposition 2：罚因子趋于极限时得到秩一解）+ SCA。
- 每次迭代复杂度用 O(·) 给出；收敛到驻点。证明集中在一个附录。

## 6. 仿真与实验
- Table I 系统参数；Fig. 2 仿真布局。基准两种："baseline 1"（不迭代的简单设计）、"baseline 2"（不部署 IRS）。
- 结果小节标题都写成 "X Versus Y" 形式，最后一节用问句做标题："Single IRS or Multiple IRSs?"。
- 每个结论都解释原因（如 baseline 2 损失 "is mainly due to the huge path loss of the AP-legitimate user links …"）；Fig. 4 caption 说明 "The double sided arrows indicate the performance gain …"。

## 7. 图表
- 9 图 1 表 1 算法。Fig. 1 场景图（IRS 贴在两栋楼上，标出部分信道符号）。caption 描述型，参数写进 caption。

## 8. 句式库
- 已有手段的两点缺陷："However, these existing approaches have two main demerits. First, … Second, …"
- 新范式需求："To overcome these two shortcomings of existing systems, a new cost-effective and energy-efficient paradigm is needed which is capable of shaping the radio propagation environment."
- 假设过于乐观："Therefore, the assumptions of single-antenna eavesdroppers and perfect eavesdropper CSI at the AP are generally overly optimistic which weakens the generality and practicality of …"
- 首创："To the best of the authors' knowledge, the design of robust and secure IRS-assisted wireless communication systems with multi-antenna eavesdroppers has not been studied in the literature, yet."
- 方法选择理由："In fact, AO is a widely applicable and empirically efficient approach for handling optimization problems involving coupled optimization variables."
- 难点点名："The highly non-convex unit modulus constraints … and the infinitely many inequality constraints introduced by the imperfect CSI are the main challenges for solving the problem."

## 9. 结论
- 1 段 222 词，过去时复述 → "Simulation results have verified the tremendous potential of IRSs …" → 鲁棒性 → "Furthermore, design guidelines for multi-IRS systems were provided."（以设计准则收尾）。无数字、无未来工作。
