---
doi: 10.1109/jsac.2017.2680898
title: "Caching in the Sky: Proactive Deployment of Cache-Enabled Unmanned Aerial Vehicles for Optimized Quality-of-Experience"
journal: JSAC
year: 2017
band: 2016-2018
cites: 671
cites_per_year: 71.2
article_type: research
topic: UAV
source: xplore-html
xplore: 7875131
auto:
  words_total: 8943
  n_sections: 6
  n_subsections: 25
  n_figures: 10
  n_tables: 4
  n_display_eq: 32
  n_algorithms: 0
  statements: {theorem: 3, lemma: 0, proposition: 1, corollary: 0, proof: 4, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 24.6
  we_per_1k: 10.1
  title_words: 14
  abstract_words: 251
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 3, contribList: 2, roadmap: 1, however: 13, transition: 10, resultsShow: 1, motivatedBy: 0, toAddress: 5, gapWord: 1, nonconvex: 0, npHard: 0, closedForm: 1, outperform: 0, intensifier: 6, worthNoting: 0, observe: 20, thisIsBecause: 2, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 6, promising: 1, gen: 1, contrast: 4, firstTime: 0, novel: 4, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 14, DNN: 3}
code:
  title_pattern: [colon-subtitle, X-for-Y]
  abstract_moves: [aim, context, method, method, method, method, method, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper
  intro_paragraphs: 6
  intro_moves: [field, prior, gap, solution, prior, gap, prior, gap, contrib, roadmap]
  related_work: in-intro-subsection
  contrib_format: numbered
  contrib_n: 5
  contrib_verbs: [propose, analyze, develop, introduce, perform]
  contrib_quantified: true
  first_claim: true
  roadmap: true
  notation: table
  gap_type: [combination, new-scenario, limitation]
  motivating_figure: true
  problem_class: MINLP
  solution: [DNN, closed-form, decomposition]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 4
  baseline_naming: descriptive
  x_axes: [mobility-patterns, content-probability, number-of-users, fronthaul-rate, number-of-UAVs, cache-size]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: true   # 自行采集 100 名学生两个月的真实移动轨迹 + Youku 真实内容请求数据；无硬件原型
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[比喻主标题]: [具体做法] for [目标]"，14 词。"Caching in the Sky" 是押韵式比喻主标题，冒号后才是技术描述——高引论文中少见的"吸睛 + 说明"双段标题。

## 2. 摘要（8 句，251 词）
- 被动锚点："In this paper, the problem of proactive deployment of cache-enabled unmanned aerial vehicles (UAVs) for optimizing the quality-of-experience (QoE) … is studied."
- 第 2 句列出可用的人本信息（访问地点、请求内容、性别、职业、设备类型）→ 预测 → 关联 / 位置 / 缓存三类决策 → 优化目标（最大化 QoE 同时最小化功率）。
- 方法：概念器回声状态网络（conceptor-based ESN）预测 + 推导最优位置与缓存内容。
- 末句强调真实数据与数字："Simulation results using real pedestrian mobility patterns from BUPT and actual content transmission data from Youku show that the proposed algorithm can yield 33.3% and 59.6% gains, respectively, …"

## 3. 引言逻辑（6 段，约 1590 词；内分 A. Related Works / B. Contributions）
1. 下一代网络以用户为中心（human-in-the-loop）→ CRAN 能集中处理用户数据 → "However, an effective exploration of human-in-the-loop features in a CRAN faces many challenges …"
2. （A 小节）CRAN / 异构网中的缓存工作逐篇 → "However, most of these existing caching works [3]–[9] were typically restricted to static networks without mobility and ultra dense users." → 地面基站缓存对移动用户的具体失效情形（换小区后内容不在新基站）→ "Therefore, there is a need to introduce a more flexible base station …" → UAV。
3. UAV 通信工作只做性能分析、没有行为预测和缓存 → 前传容量受限 → 缓存可以缓解前传。
4. 行为预测工作逐篇 + 各自局限（只预测不优化 / 需存全部历史数据）→ 自己的前作 [4] 只能预测一个非线性系统 → 用"周一到周日分成七个模式"的例子解释概念器 ESN 为什么更准。
5. （B 小节）主贡献散文段（含两个 "unlike previous studies such as …" 对比、首创声明、真实数据、33.3% / 59.6%）→ "In summary, the main contributions of the paper are as follows:" + 5 条编号贡献（其中两条各带一句首创声明）。
6. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：组合（缓存 × UAV × 行为预测）+ 新场景（移动用户、受限前传）+ 已有方法局限（静态地面缓存、单一非线性预测系统）。
- 写法亮点：三段相关工作各管一条线（缓存 / UAV / 预测），每条线都以"它缺什么"结束，最后在贡献段里用两个 "Unlike previous studies such as …" 把三条线收拢。
- 用具体例子说明方法直觉（按星期几拆分移动模式），而不是只说"精度更高"。

## 5. 科研方法
- 模型：CRAN（RRH 用 K-means 分簇 + ZFBF）、缓存型 UAV（mmWave 下行 + 受限的地对空前传）、用户连续移动；QoE 由时延与设备类型（屏幕尺寸 → 速率需求，Table II MOS 模型）共同决定；Proposition 1 给时延下界。
- 预测：ESN 组件用编号列表逐项定义（agents、input、output、ESN model、conceptors），内容请求与移动两套；训练（岭回归）与预测两阶段（Table III 以表格形式给出算法）。
- 优化（Fig. 2 流程图）：Theorem 1 用户-RRH 关联条件 → Theorem 2 每个 UAV 的最优缓存集合 → Theorem 3 两种特殊情形下 UAV 最优位置闭式 → 实现与复杂度小节。证明在附录。

## 6. 仿真与实验
- 真实数据：Youku 视频请求指数；自行记录 100 名 BUPT 学生两个多月每天 9:00–12:00 的逐小时位置。Table IV 参数。
- 比较对象用 a) b) c) 列出（有先验知识的最优、前作 ESN、随机缓存 + ESN；另有无缓存、无 UAV 两种场景）。
- 先展示预测效果（概念器 ESN 记忆占用随模式数变化、内容请求概率预测曲线）→ 再系统性能（功率 vs 用户数 / UAV 数 / 缓存容量、前传速率、QoE 满意比例）→ 与穷举最优比较。

## 7. 图表
- 10 图 4 表（记号表、MOS 模型表、算法表、参数表）。Fig. 1 系统图，Fig. 2 求解流程。Fig. 3 caption 很长（逐一解释曲线颜色和图例含义），其余为短标签并在括号里给参数。

## 8. 句式库
- 用户中心愿景："The next-generation of cellular systems is expected to be largely user centric and, as such, it must be cognizant of human-related information such as …"
- 已有工作的场景局限："However, most of these existing caching works [3]–[9] were typically restricted to static networks without mobility and ultra dense users."
- 具体失效情形："… whenever a mobile user moves to a new cell, its requested content may not be available at the new base station and, consequently, the users cannot be serviced properly."
- 引出新载体："Therefore, there is a need to introduce a more flexible base station that can boost the capacity and track the users' mobility patterns …"
- 只预测不优化："Nevertheless, the mobility prediction works in [18]–[21] focused only on the prediction phase and did not study how the users' mobility patterns can be used to optimize the wireless performance …"
- 首创："To our best knowledge, this work is the first to analyze the use of caching at the level of UAVs, given ESN-based predictions on the users' behavior."

## 9. 结论
- 1 段 136 词，现在完成时复述（have proposed / have presented / have developed）→ "Simulation results have shown that the proposed approach yields significant performance gains …"。无数字、无未来工作。
