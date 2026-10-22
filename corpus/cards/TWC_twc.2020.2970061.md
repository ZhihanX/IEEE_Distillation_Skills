---
doi: 10.1109/twc.2020.2970061
title: "Weighted Sum-Rate Maximization for Reconfigurable Intelligent Surface Aided Wireless Networks"
journal: TWC
year: 2020
band: 2019-2021
cites: 995
cites_per_year: 154.9
article_type: research
topic: RIS
source: xplore-html
xplore: 8982186
auto:
  words_total: 6062
  n_sections: 7
  n_subsections: 29
  n_figures: 7
  n_tables: 1
  n_display_eq: 63
  n_algorithms: 4
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 24.9
  we_per_1k: 9.6
  title_words: 10
  abstract_words: 162
  abstract_sentences: 7
  phrases: {toTheBest: 0, inThisPaper: 11, contribList: 1, roadmap: 1, however: 15, transition: 14, resultsShow: 1, motivatedBy: 0, toAddress: 4, gapWord: 0, nonconvex: 8, npHard: 0, closedForm: 8, outperform: 0, intensifier: 1, worthNoting: 0, observe: 4, thisIsBecause: 1, asExpected: 1, insight: 0, tradeoff: 0, figVerb: 4, promising: 2, gen: 0, contrast: 1, firstTime: 0, novel: 0, weProposeFirst: 0, wlog: 0, code: 0, prototype: 0}
  methods: {complexity: 24, BCD: 18, AO: 11, convergence: 11, SCA: 9, WMMSE: 3, FP: 2, SDR: 2, manifold: 2, randomMatrix: 1}
code:
  title_pattern: [X-for-Y, X-aided-Y]
  abstract_moves: [context, aim, aim, method, method, result, result]
  abstract_has_numbers: true     # "when the channel uncertainty is smaller than 10%"
  abstract_anchor: in-this-paper
  intro_paragraphs: 9
  intro_moves: [field, aim, prior, gap, approach, approach, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [study, propose, extend]
  contrib_quantified: true
  first_claim: true              # 弱化版："this paper is one of the early attempts to study …"（在列表 <li> 中）
  roadmap: true
  notation: intro-end
  gap_type: [limitation, practicality]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [FP, BCD, gradient, SCA, manifold]
  theory_role: none
  proofs_location: none
  complexity_analysis: true
  convergence_analysis: true     # 依据非凸 BCD / 随机 SCA 理论保证收敛到稳定点
  sim_param_table: true
  baselines_n: 4                 # Without RIS、Random Phase、Upper Bound（多次随机初始化取最大）+ 第 III 节的传统 AO
  baseline_naming: descriptive
  x_axes: [transmit-power, iterations, number-of-elements, RIS-location, CDF]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: true   # "a RIS with 100 passive elements"、"smaller than 10%"
  conclusion_future_work: false
---

## 1. 标题
- "[目标] Maximization for [技术] Aided [网络]"，10 词。"WSR Maximization for X-Aided Y" 是优化类论文最直白的标题——目标函数 + 系统，读者一眼知道这是哪类问题。

## 2. 摘要（7 句，162 词）
- 技术定义（"… is a promising solution to build a programmable wireless environment …"）→ "In this paper, we consider …" → 目标（联合波束成形与相位，完美 / 不完美 CSI 两种设定）。
- 方法两句：完美 CSI 用 FP 得到低复杂度、收敛到稳定解的算法 → "Then, we resort to the stochastic successive convex approximation technique and extend the proposed algorithm to …"
- 结果："The validity of the proposed methods is confirmed by numerical results." + 唯一数字："… performs quite well when the channel uncertainty is smaller than 10%."（用数字界定方法适用范围）。

## 3. 引言逻辑（9 段，约 1160 词）
1. RIS 定义与优点（无源、低功耗、无热噪声）→ 应用面 → 最有前景的应用：改善恶劣传播条件。
2. "In this paper, we investigate …"（Fig. 1 在引言）→ 与全双工 AF 中继的区别 → 目标。引言第 2 段就给出本文问题。
3. A. Related Works：已有工作多假设完美 CSI → [21][22] SDR 交替优化"cannot obtain the stationary solution, and the complexity is a little high" → [23][24] ZF 解耦但放大噪声、推导不能直接推广。
4. 信道估计难题 → 统计 CSI 方法 → "However, the performance of these methods … depends heavily on the channel model assumptions, …"
5. B. Contributions（散文）：与混合预编码的形式相似但本质不同（"Nevertheless, the main difference is that, the RIS … has no capability to suppress inter-user interference."）→ 变量深度耦合、AO 收敛慢 → 每步复杂度必须低 → FP 分四块 + 非凸 BCD。
6. 不完美 CSI 设定的合理性（AP 可知合成信道）→ 只对 RIS 相位做平均 WSR 最大化 → "This problem formulation is more general than those in [25] and [26], …" → 随机 SCA。
7. 3 条 bullet（Firstly / Secondly / Finally）。8. C. Organization and Notations：路线图；9. 记号。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（SDR-AO 无稳定点保证且复杂度高；ZF 设计放大噪声）+ 实用性（RIS 无源，难以获得完美 CSI）。
- 写法亮点：用"形式相似、本质不同"区分本文问题与混合预编码问题，说明为何不能直接套用已有算法——"look mathematically similar … Nevertheless, the main difference is …"。
- 弱化首创："this paper is one of the early attempts …"（2020 年 RIS 热点初期常见措辞）。

## 5. 科研方法
- 模型：AP（M 天线）+ RIS（N 元件）+ K 单天线用户，准静态平坦衰落；单列小节讨论信道估计（brute-force、压缩感知、半无源 RIS 三种方法 bullet），回应可实现性。
- 问题 P(A)（完美 CSI）与 P(B)（不完美 CSI：最大化 WSR 期望，TDD 帧结构 Fig. 2）。
- 第 III 节先介绍"传统"AO（WMMSE + 复圆流形共轭梯度），分析其复杂度 O(KM^3) 与收敛慢的问题——先立靶子再给新算法。
- 第 IV 节：闭式 FP（Lagrangian 对偶变换 + 二次变换）→ 四块非凸 BCD → W 用 prox-linear 更新（避免矩阵求逆与对偶搜索）→ θ 用二阶 Taylor 代理函数的 SCA → 等价于梯度投影。
- 第 V 节：内层用 BCD 求稳定点，外层随机 SCA + 梯度投影（避免样本平均法的存储负担）。

## 6. 仿真与实验
- 毫微微小区场景（Fig. 3），参数 Table I（"almost the same as those in [24]"，路损按 3GPP）；直射链路 Rayleigh、RIS 链路 Rician；交代 CSI 误差建模。
- 3 个编号基准（Without RIS / Random Phase / Upper Bound），外加第 III 节的 AO。
- WSR vs 发射功率 → 收敛 → vs RIS 元件数 → vs RIS 水平位置 → 随机用户位置的 CDF。公平性设置：权重与直射链路路损成反比并归一化。

## 7. 图表
- 7 图 1 表 4 算法。Fig. 1 系统图（引言）、Fig. 2 TDD 帧结构、Fig. 3 仿真布局。结果 caption 短标签 + 固定参数（"WSR versus N, when P_T = 5 dBm."）。

## 8. 句式库
- 技术定位："Reconfigurable intelligent surfaces (RIS) is a promising solution to build a programmable wireless environment via steering the incident signal …"
- 指出前作缺陷："Although this alternating optimization approach achieves quite good performance, the main shortcoming is that the proposed algorithm cannot obtain the stationary solution, …"
- 形似神异："The formulated problem looks mathematically similar to the WSR maximization problem in the hybrid digital/analog precoding …"
- 更一般："This problem formulation is more general than those in [25] and [26], since it is independent to the structure of channel model assumptions."
- 弱化首创："Firstly, this paper is one of the early attempts to study the WSR maximization problem for the RIS-aided multiuser downlink MISO system, …"
- 预期之中："It is seen that, if the phase vector is not optimized, the performance gain by deploying RIS is negligible as expected."
- 补充（skill 引用）："A. Related Works / B. Contributions / C. Organization and Notations"
- 补充（skill 引用）："In [21] and [22], the transmit power of the AP is minimized by decomposing the joint optimization problem into two subproblems: …"
- 补充（skill 引用）："The main contributions of this work are summarized as follows:"
- 补充（skill 引用）："Fig. 4(a) illustrates the WSR of different schemes with respect to the transmit power P_T when N=100."
- 补充（skill 引用）："In this paper, we consider a RIS-aided multiuser multiple-input single-output (MISO) downlink communication system."
- 补充（skill 引用）："In particular, the proposed algorithm performs quite well when the channel uncertainty is smaller than 10%."

## 9. 结论
- 1 段 140 词（偏短），一般现在时开头（"In this paper, we investigate …"）→ 方法复述 → 两句结果，重复摘要中的数字（100 元件、10%）。无未来工作。
