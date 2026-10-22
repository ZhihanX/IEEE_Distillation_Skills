---
doi: 10.1109/jsac.2020.3000803
title: "Massive MIMO Transmission for LEO Satellite Communications"
journal: JSAC
year: 2020
band: 2019-2021
cites: 569
cites_per_year: 92.1
article_type: research
topic: cell-free-massive-MIMO   # 选文正则归类；实为卫星通信 massive MIMO
source: xplore-html
xplore: 9110855
auto:
  words_total: 7425
  n_sections: 6
  n_subsections: 17
  n_figures: 4
  n_tables: 1
  n_display_eq: 69
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 4, corollary: 0, remark: 2, proof: 4, proof_in_appendix: 0}
  n_appendix: 3
  mean_sentence_words: 29.9
  we_per_1k: 11.4
  title_words: 7
  abstract_words: 279
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 4, contribList: 1, roadmap: 1, however: 4, transition: 13, resultsShow: 2, motivatedBy: 5, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 4, outperform: 0, intensifier: 11, worthNoting: 3, observe: 5, thisIsBecause: 0, asExpected: 0, insight: 1, tradeoff: 0, figVerb: 0, promising: 0, gen: 3, contrast: 4, firstTime: 0, novel: 0, weProposeFirst: 4, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 6}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [context, gap, aim, method, method, theory, method, theory, result, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, tech, gap, solution, gap, approach, aim, roadmap]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 5
  contrib_verbs: [introduce, establish, develop, propose, demonstrate]
  contrib_quantified: false
  first_claim: false          # 只有隐含首创："so far massive MIMO has not been applied to satellite communication systems"
  roadmap: true
  notation: table             # Table I "Variable list" 放在引言末
  gap_type: [new-scenario, practicality]
  motivating_figure: true     # Fig. 1 系统示意在模型节开头
  problem_class: analysis-only   # 广义瑞利商闭式预编码 + 渐近界 + 分组启发式，无迭代优化
  solution: [closed-form, heuristic]
  theory_role: central
  proofs_location: appendix
  complexity_analysis: false  # 只有 "low-complexity" 的定性说法，无复杂度推导
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 4              # IntF 上界、iCSI（genie-aided）、Fixed DFT、传统 FR4
  baseline_naming: acronym
  x_axes: [SNR, number-of-groups]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[技术] Transmission for [新场景]"，7 词。地面成熟技术 + 新场景的最短组合，本身就是 idea 声明。

## 2. 摘要（10 句，279 词）
- 场景定位（LEO 纳入 5G 及以后）→ 空白句："Massive MIMO techniques, though widely used in terrestrial communication systems, have not been applied to LEO satellite communication systems."
- "In this paper, we propose … and exploit statistical channel state information (sCSI) to address the difficulty of obtaining instantaneous CSI (iCSI) at the transmitter."（方案 + 难点放在同一句）。
- 方法链：信道建模（多普勒 / 时延补偿）→ 闭式 DL 预编码 / UL 接收 → 上界条件 → "Motivated by this, we propose …" 分组算法 → 渐近最优。
- 两句结果："Numerical results demonstrate … significantly enhances …"；"Notably, the proposed sCSI based precoder and receiver achieve the similar performance with the iCSI based ones that are often infeasible in practice."（用不现实的理想基准衬托）。无数字。

## 3. 引言逻辑（8 段，约 990 词）
1. 卫星通信补充地面网络 → LEO（< 2000 km）优势 → OneWeb / SpaceX 项目。
2. 多波束：FR4 → FFR → 波束间干扰 → 线性预编码更实用。
3. "It is worth noting that most of the existing works … rely on precise instantaneous channel state information (iCSI)." → "However, …" TDD 相干时间短于传输时延、FDD 反馈开销与过时 → iCSI 不可得。
4. 地面 massive MIMO 的优势 → "Motivated by this, we propose to exploit massive MIMO along with FFR for LEO satellite communication systems, …"
5. 空白收束："Consequently, incorporating massive MIMO into LEO satellite communication systems is still an open and challenging task."（iCSI 不可得 + 星上载荷复杂度）。
6. sCSI 慢变、易获取 → 地面已有 sCSI 预编码 → 卫星更适合。
7. "In this paper, we investigate …"，并主动声明可推广（GEO、HAP）→ 5 条 bullet 贡献。
8. 路线图 + Table I 变量表。

## 4. Idea 是怎么提出的
- 空白类型：新场景（把地面 massive MIMO 搬到 LEO）+ 实用性（iCSI 在卫星上不可得 → 改用 sCSI）。
- 写法亮点："地面成熟 → 卫星尚未应用 → 直接搬不行（两条原因）→ 换信息类型（sCSI）"——迁移型 idea 的标准论证：先证明"值得搬"，再证明"不能照搬"，最后给出"怎么改"。
- 理论结果反哺算法：Proposition 2 给出"信道方向正交"时达到上界 → 由此设计按空间角分组（"Motivated by this"）。

## 5. 科研方法
- 模型：UPA 卫星天线；LEO 信道的四个物理性质分小节建模（1) Doppler 2) Delay 3) Angle 4) Gain，Rician）→ 用户端做多普勒与时延补偿以简化设计 → OFDM 信号模型。
- 设计：以平均 SLNR / 平均 SINR 为准则得到闭式 sCSI 预编码 / 接收机（Proposition 1）→ DL-UL 对偶 → 上界与取得条件（Proposition 2）→ Remark 2：天线数足够大时退化为 DFT 固定波束。
- 分组：SAUG 按空间角区间分组 → 遍历和速率上界（Proposition 3）与下界（Proposition 4），下界与上界在天线数 / 组数大时重合 → 渐近最优。
- 3 个附录给 Proposition 2–4 证明。

## 6. 仿真与实验
- 参数写在正文（16×16 UPA、Rician 因子 10 dB、空间角均匀分布）。
- 基准 4 条 bullet：IntF（"genie-aided" 无干扰上界）、iCSI（genie-aided 获得）、提出的 sCSI、DFT 固定；另与传统 FR4 比。基准开头注明 "Note that massive MIMO has not been applied to LEO satellite communications"，解释为何没有现成方案可比。
- 只有 3 张结果图：sCSI vs iCSI（真实与估计 sCSI）→ vs 组数 → FFR vs FR4（不同 Rician 因子）。

## 7. 图表
- 4 图 1 表 0 算法。Fig. 1 系统示意（模型节）；Table I 变量表（引言）。结果图 caption 较长，交代比较对象与设置（如注明估计 sCSI 用 50 个样本平均）。
- 理论密集、图少（4 图 / 69 个公式）的 JSAC 论文：价值主要在模型与闭式结果。

## 8. 句式库
- 迁移空白："Massive MIMO techniques, though widely used in terrestrial communication systems, have not been applied to LEO satellite communication systems."
- 开放难题收束："Consequently, incorporating massive MIMO into LEO satellite communication systems is still an open and challenging task."
- 实际不可行："… which makes obtaining accurate iCSI via the UL-DL reciprocity a mission impossible."
- 推广声明："While this paper focuses on the LEO satellite communications, the proposed massive MIMO transmission schemes can also be extended to other non-terrestrial communication systems, …"
- 理论 → 算法："Motivated by this, we propose a space angle based user grouping (SAUG) algorithm …"
- 理想基准衬托："Notably, the proposed sCSI based precoder and receiver achieve the similar performance with the iCSI based ones that are often infeasible in practice."
- 补充（skill 引用）："Illustration of the LEO satellite communication system setup."
- 补充（skill 引用）："TABLE I Variable list"
- 补充（skill 引用）："Appendix A Proof of Proposition 2"
- 补充（skill 引用）："From (23) and (30), we can obtain the DL-UL duality between the proposed sCSI based DL precoder and UL receiver."
- 补充（skill 引用）："It is worth noting that most of the existing works on downlink (DL) precoding in multibeam satellite communications, e.g., [4], [5], rely on precise instantaneous channel state information (iCSI)."
- 补充（skill 引用）："Assume without loss of generality that the antennas are separated by one-half wavelength in both the x- and y-axes, …"
- 补充（skill 引用）："As different UTs are usually spatially separated by a few wavelengths, it is reasonable to assume that the channel realizations between the satellite and different UTs are uncorrelated [17]."
- 补充（skill 引用）："In this paper, we have investigated massive MIMO transmission for LEO satellite communications exploiting sCSI with FFR."
- 补充（skill 引用）："Future work includes detailed investigation on low complexity sCSI estimation, …"
- 补充（skill 引用）："Low earth orbit (LEO) satellite communications are expected to be incorporated in future wireless networks, in particular 5G and beyond networks, …"
- 补充（skill 引用）："It is shown that the DL ASLNRs and UL ASINRs of all UTs reach their upper bounds under some channel condition."
- 补充（skill 引用）："Numerical results demonstrate that the proposed massive MIMO transmission scheme with FFR significantly enhances the data rate of LEO satellite communication systems."
- 补充（skill 引用）："The rest of the paper is organized as follows."
- 补充（skill 引用）："In Section II, we investigate the channel model and the corresponding transmission signal model for LEO satellite communication systems."

## 9. 结论
- 1 段 225 词，现在完成时开头 → 过去时逐条复述（建模、闭式、上界条件、分组、渐近最优）→ 结果两句 → 4 个具体未来方向（sCSI 估计、多天线终端、低 PAPR、多星系统）。无数字。
