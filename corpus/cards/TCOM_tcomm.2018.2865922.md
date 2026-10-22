---
doi: 10.1109/tcomm.2018.2865922
title: "Common Throughput Maximization in UAV-Enabled OFDMA Systems With Delay Consideration"
journal: TCOM
year: 2018
band: 2016-2018
cites: 447
cites_per_year: 57.0
article_type: research
topic: UAV
source: xplore-html
xplore: 8438896
auto:
  words_total: 8936
  n_sections: 5
  n_subsections: 12
  n_figures: 7
  n_tables: 0
  n_display_eq: 30
  n_algorithms: 2
  statements: {theorem: 1, lemma: 1, proposition: 0, corollary: 0, proof: 2, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 27.7
  we_per_1k: 7.5
  title_words: 10
  abstract_words: 262
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 2, however: 13, transition: 11, resultsShow: 0, motivatedBy: 5, toAddress: 7, gapWord: 0, nonconvex: 8, npHard: 0, closedForm: 0, outperform: 1, intensifier: 4, worthNoting: 4, observe: 9, thisIsBecause: 4, asExpected: 2, insight: 0, tradeoff: 10, figVerb: 0, promising: 2, gen: 2, contrast: 5, firstTime: 0, novel: 1, weProposeFirst: 11, wlog: 1, code: 0, prototype: 1}
  methods: {complexity: 12, BCD: 11, convergence: 9, convexOpt: 7, lagrange: 6, KKT: 1}
code:
  title_pattern: [X-in-Y, X-with-Y]
  abstract_moves: [context, prior, gap, aim, method, aim, theory, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, tech, prior, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 5
  contrib_verbs: [formulate, show, propose, propose, verify]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [theory-gap, new-scenario]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [BCD, lagrangian-dual, SCA]
  theory_role: supporting
  proofs_location: body
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [trajectory-plot, MRR, flight-period]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[目标] Maximization in [系统] With [新约束] Consideration"，10 词。"With Delay Consideration" 点出与已有 UAV 吞吐工作唯一但关键的区别。

## 2. 摘要（10 句，262 词）
- 第 1 句 UAV 的意义；第 2 句让步式概括已有工作："Although prior works have shown the performance improvement by exploiting the UAV's mobility, they mainly focus on delay-tolerant applications."
- 第 3 句把空白写成开放问题："…, it remains unknown whether the UAV is able to provide any performance gain in delay-constrained communication scenarios."
- "Motivated by the above, we study, in this paper, …" → 新指标 MRR 的定义 → 目标。
- "First, we show … which reveals a fundamental throughput-delay tradeoff …" → "Next, we propose …" → "Furthermore, …" → "Finally, …"——First/Next/Furthermore/Finally 串起四个贡献。无数字。

## 3. 引言逻辑（8 段，约 2060 词）
1. 新闻式开场：无人机出货量预测（2015 年 640 万 → 2021 年 6770 万）、奥运会无人机灯光秀、"Safe DRONE Act of 2017"、Qualcomm 4G 试验——用产业事实证明重要性。
2. UAV 通信三大优势（First / Second / Third）→ 适合应急 / 临时场景 → "However, there are also open challenges …"。
3. 已有工作按演进梳理：部署 → 预定轨迹 → 停靠点 → 轨迹 + 通信联合设计 → 多用户周期服务 → 结论："As a result, the throughput gain brought by the UAV's mobility does not come for free but in fact at the cost of user communication delay [7]."
4. 业务时延需求差异（毫秒级视频会议 vs 秒级文件下载，举 YouTube 例子）→ 所有轨迹工作只考虑时延容忍业务 → "Therefore, it remains unknown whether mobile UAVs are still able to provide throughput gains …"
5. "Motivated by such an open question, we study in this paper …"：为何选 OFDMA → 定义 MRR → 目标 → 与已有工作相比"more general and practically useful" → 直觉解释新权衡（飞向一些用户就远离另一些用户）。
6. 贡献散文段（First / Next / … / Furthermore / Finally），其中详细交代"常规 BCD 会卡在初始点"这一发现及修正。
7. 路线图；8. Notations。

## 4. Idea 是怎么提出的
- 空白类型：理论空白（时延约束下移动性是否还有增益——开放问题）+ 新场景（混合时延业务）。
- 写法亮点：把空白写成一个"是否"问题（"it remains unknown whether …"），再用 Theorem 1 给出回答（最大最小吞吐对 MRR 单调不增），形成"问题—定理"闭环。
- 引入一个可调参数（MRR）把"时延容忍 / 时延敏感"连续化，从而能画出吞吐—时延权衡曲线。
- 直觉先行："Intuitively, when the UAV flies towards some users to capture better channels with them, it gets farther away spontaneously from other users …"

## 5. 科研方法
- 模型：固定高度 UAV、LoS 信道（引测量结果支撑）、OFDMA 带宽 + 功率分配、离散化轨迹、速度约束；MRR 约束。
- Theorem 1（正文证明）：最大目标值关于 MRR 逐元素非增。
- 求解：BCD——资源分配子问题用拉格朗日对偶最优求解（分解为 KN+1 个并行子问题，再构造原问题解）；轨迹子问题用 SCA（构造下界）。
- 关键发现：常规 BCD 在 MRR 约束下"will very likely get stuck at the initial point"→ 提出参数辅助 BCD（临时 MRR 从大逐步降到目标值）。
- 圆形轨迹初始化方案；收敛性分析在正文给出。

## 6. 仿真与实验
- 参数写在正文（H=500 m、B=10 MHz、T=270 s …）。
- 先同质 MRR（轨迹图 + 吞吐 vs MRR + 吞吐 vs 周期 T）→ 异质 MRR → 大规模随机用户。
- 对比 4 种轨迹（提出 / fly-and-hover / 圆形 / 静止 UAV），编号列出并描述。

## 7. 图表
- 7 图 0 表 2 算法。Fig. 1 场景图在引言。轨迹图占了一半（不同 MRR 下轨迹形状变化直接展示权衡）。caption 短标签 + 条件。

## 8. 句式库
- 产业事实开场："As predicted in [2], the number of unmanned aerial vehicles (UAVs), …, will continue to surge over the next several years, with …"
- 让步概括："Although prior works have shown the performance improvement by exploiting the UAV's mobility, they mainly focus on delay-tolerant applications."
- 代价揭示："…, the throughput gain brought by the UAV's mobility does not come for free but in fact at the cost of user communication delay."
- 开放问题："Therefore, it remains unknown whether mobile UAVs are still able to provide throughput gains over static UAVs/ground BSs, when …"
- 承接："Motivated by such an open question, we study in this paper …"
- 常规方法失效："…, it is shown that the conventional block coordinate descent method … will very likely get stuck at the initial point, …"
- 定理解读："Theorem 1 sheds light on the fundamental tradeoff between the max-min average throughput and the user communication delay requirement: …"

## 9. 结论
- 1 段 289 词，现在时复述（We first show … Then, we show … we propose …）→ "We hope that the results of the paper can help assessing more practically …" → 由单 UAV 的局限引出 3 个未来方向（多 UAV、队列时延、能效轨迹）。无数字。
