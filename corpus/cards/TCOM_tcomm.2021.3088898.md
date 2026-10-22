---
doi: 10.1109/tcomm.2021.3088898
title: "Secrecy-Energy Efficient Hybrid Beamforming for Satellite-Terrestrial Integrated Networks"
journal: TCOM
year: 2021
band: 2019-2021
cites: 431
cites_per_year: 84.6
article_type: research
topic: security
source: xplore-html
xplore: 9453840
auto:
  words_total: 6229
  n_sections: 6
  n_subsections: 7
  n_figures: 14
  n_tables: 2
  n_display_eq: 39
  n_algorithms: 3
  statements: {theorem: 0, lemma: 0, proposition: 1, corollary: 0, remark: 2, proof: 1, proof_in_appendix: 0}
  n_appendix: 1
  mean_sentence_words: 28.0
  we_per_1k: 9.5
  title_words: 8
  abstract_words: 197
  abstract_sentences: 6
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 0, however: 5, transition: 5, resultsShow: 1, motivatedBy: 1, toAddress: 11, gapWord: 1, nonconvex: 12, npHard: 0, closedForm: 0, outperform: 5, intensifier: 0, worthNoting: 0, observe: 9, thisIsBecause: 0, asExpected: 0, insight: 1, tradeoff: 3, figVerb: 4, promising: 0, gen: 0, contrast: 1, firstTime: 0, novel: 2, weProposeFirst: 5, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 7, convergence: 5, SDR: 4, penalty: 3, SCA: 2, bisection: 2, FP: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, tech, gap, prior, gap, prior, gap, tech, gap, aim, contrib, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [formulate, propose, demonstrate]
  contrib_quantified: false
  first_claim: false
  roadmap: false
  notation: intro-end
  gap_type: [combination, limitation]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [FP, bisection, SDR, penalty, SCA, AO]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: false   # 只有定性的 "low-complexity" 表述，无复杂度阶
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 1
  baseline_naming: descriptive
  x_axes: [beampattern, power-budget, uncertainty-bound, number-of-RF-chains, array-geometry]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: false
---

## 1. 标题
- "[复合指标] Efficient [技术] for [网络]"，8 词。把新指标 "Secrecy-Energy Efficient" 作形容词前置，与 "Energy-Efficient Hybrid Precoding …"（JSAC 2016）同骨架。

## 2. 摘要（6 句，197 词）
- "In this paper, we investigate secrecy-energy efficient hybrid beamforming (BF) schemes for a satellite-terrestrial integrated network, wherein …"（共享 mmWave 频谱的场景直接写进锚点句）。
- 非完美窃听信道 AoD 假设下的联合设计 → "Since the formulated optimization problem is nonconvex and mathematically intractable, we propose two robust BF schemes …"
- Specifically（单 ES：Charnes-Cooper + 迭代搜索）/ In the case of multiple ESs（SCA → LMI + SOC）。
- 末句："… validated via simulations using realistic satellite and terrestrial downlink channel models."（强调信道模型真实）。无数字。

## 3. 引言逻辑（8 段，约 1180 词；无路线图）
1. 流量增长 1000 倍 → 偏远地区 → 卫星通信 → 星地融合网络（STIN）。
2. 物理层安全（波束成形、人工噪声）→ "However, artificial jamming is not suitable for satellite transmissions due to the long distance …" → 地面网络协作干扰等 STIN 安全工作。
3. 能效（EE）作为指标及相关工作。
4. "As mentioned above, existing works mainly addressed the issues of secrecy rate maximization and EE maximization separately." → 保密能效（SEE）指标及其工作。
5. 这些工作假设完美 CSI → 鲁棒设计的三类不确定性模型（确定性 / 随机 / 角度信息）。
6. mmWave 大规模阵列 → 全数字不可行 → 混合模拟-数字 BF 原理 → 最相关工作 [36] "however, the SEE performance metric and imperfect CSI assumption were not taken into account."
7. "In this paper, motivated by the above considerations and the importance of SEE as a key performance metric …, we investigate …" + 3 条 bullet。
8. Notation。

## 4. Idea 是怎么提出的
- 空白类型：组合（STIN × 保密能效 × 混合波束 × 非完美 CSI）+ 已有方法局限。
- 写法亮点：引言像"逐层叠加约束"——每段引入一个维度（卫星、安全、能效、SEE、鲁棒、混合 BF）并指出单一维度工作的不足，最后一段把所有维度合并；最相关工作 [36] 用一句 however 指出缺的两个维度。
- 选择 "角度信息不确定" 模型而非其他两种，并在脚注 / 模型节说明理由（卫星场景下更现实）。

## 5. 科研方法
- 模型：GEO 多波束卫星（阵列馈源反射面天线，Fig. 2 几何模型）服务 L 个地面站（各有窃听者），地面 BS 用 UPA 混合 BF 服务蜂窝用户；共享 mmWave；四种 BF 架构（全数字 / 全连接 / 局部子阵 / 交织子阵，Fig. 3）。
- 单 ES：用离散化近似不完美 AoD → 数字 BF 用 Charnes-Cooper 变换 + 一维（二分）搜索 → 模拟预编码 SDR 后用迭代罚函数恢复秩一（Proposition 1 给等价凸化）→ 交替迭代（Algorithm 1）。
- 多 ES：对数和使单 ES 方案失效 → 引入辅助变量 + 一阶泰勒 SCA → LMI 与 SOC → 初始点搜索算法（Algorithm 3）。Remark 2 说明两方案在单 ES 场景下的取舍。

## 6. 仿真与实验
- Table II 参数（各类功耗元件 mW 级参数给出处 [41]）；基准为文献 [22] 的全数字 BF。
- 单 ES / 多 ES 两组，各自：波束方向图 → SEE vs 功率预算 → vs 窃听信道不确定界 → vs RF 链数 → vs UPA 尺寸；比较三种混合架构。
- 发现写成对比结论：单 ES 局部子阵优于交织子阵，多 ES 则相反；RF 链增加反而降低 SEE（功耗上升）。

## 7. 图表
- 14 图 2 表 3 算法。Fig. 1 系统图，Fig. 2 阵列几何，Fig. 3 四种 BF 架构对比图（caption 解释颜色含义）；Table I 列系统模型参数含义。结果 caption 短标签（"SEE versus number of RF chains."）。

## 8. 句式库
- 互补技术："As a complementary technology, satellite communications can overcome long distances and inhospitable terrains, provide wide coverage …"
- 技术不适用于特定场景："However, artificial jamming is not suitable for satellite transmissions due to the long distance between the satellite and ground users, …"
- 分开研究："As mentioned above, existing works mainly addressed the issues of secrecy rate maximization and EE maximization separately."
- 新指标定义："… secrecy energy efficiency (SEE) has been proposed as a novel design criterion in the context of secure green communications, which is defined as the ratio between …"
- 已有方案不能扩展："However, the existing schemes for the design of digital BF cannot be directly extended to solving the above complex problem due to …"
- 收束："In this paper, motivated by the above considerations and the importance of SEE as a key performance metric …, we investigate …"

## 9. 结论
- 1 段 185 词，过去时复述两个方案 → 增益来源解释（"The advantage of the proposed hybrid BF schemes comes from the exploitation of interference from the BS …"）→ "We believe that our proposed BF scheme can provide an effective solution …"。无数字、无未来工作。
