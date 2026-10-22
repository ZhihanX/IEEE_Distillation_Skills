---
doi: 10.1109/tcomm.2022.3146400
title: "Channel Estimation for Extremely Large-Scale MIMO: Far-Field or Near-Field?"
journal: TCOM
year: 2022
band: 2022-2025
cites: 917
cites_per_year: 203.4
article_type: research
topic: near-field
source: xplore-html
xplore: 9693928
auto:
  words_total: 8969
  n_sections: 6
  n_subsections: 12
  n_figures: 13
  n_tables: 2
  n_display_eq: 34
  n_algorithms: 3
  statements: {theorem: 0, lemma: 1, proposition: 0, corollary: 0, proof: 1, proof_in_appendix: 1}
  n_appendix: 2
  mean_sentence_words: 26.6
  we_per_1k: 7.1
  title_words: 9
  abstract_words: 201
  abstract_sentences: 11
  phrases: {toTheBest: 1, inThisPaper: 7, contribList: 1, roadmap: 1, however: 12, transition: 17, resultsShow: 1, motivatedBy: 2, toAddress: 5, gapWord: 0, nonconvex: 1, npHard: 0, closedForm: 0, outperform: 5, intensifier: 3, worthNoting: 2, observe: 8, thisIsBecause: 1, asExpected: 0, insight: 0, tradeoff: 0, figVerb: 1, promising: 1, gen: 11, contrast: 3, firstTime: 1, novel: 0, weProposeFirst: 4, wlog: 1, code: 0, prototype: 0}
  methods: {complexity: 15, compressedSensing: 9, convergence: 5}
code:
  title_pattern: [X-for-Y, colon-subtitle, question]
  abstract_moves: [context, context, context, gap, gap, aim, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, gap, prior, gap, gap, contrib, roadmap, notation]
  related_work: in-intro-subsection
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [reveal, propose, propose]
  contrib_quantified: false
  first_claim: true
  roadmap: true
  notation: intro-end
  gap_type: [limitation, new-scenario]
  motivating_figure: true
  problem_class: estimation
  solution: [compressed-sensing, gradient]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: true
  baselines_n: 4
  baseline_naming: acronym
  x_axes: [design-parameter, iterations, distance, SNR, pilot-length]
  fig1_role: system-model
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[问题] for [系统]: Far-Field or Near-Field?"，9 词。副标题是二选一问句，把论文核心洞见（远场假设失效）直接抛给读者。

## 2. 摘要（11 句，201 词）
- 前 5 句构成一条完整的因果链："Existing … algorithms … heavily rely on the channel sparsity in the angular domain, which is achieved by the classical far-field planar-wavefront assumption." → "However, due to the non-negligible near-field spherical-wavefront property in XL-MIMO, this channel sparsity in the angular domain is not achievable." → "Therefore, existing far-field channel estimation schemes will suffer from severe performance loss."
- "To address this problem, in this paper, we study …" → "Specifically, unlike the classical angular-domain representation …, we propose a polar-domain representation …"
- 两个算法用 "Firstly, … Furthermore, …"；最后一句只说 "simulations are provided to verify the effectiveness"。

## 3. 引言逻辑（2 段 + A. Prior Works 3 段 + B. Our Contributions + C. Organization and Notation）
1. massive MIMO → XL-MIMO（10 倍谱效）→ 高频与大阵列。
2. 混合预编码 → 需要 CSI → "Unfortunately, …" → 导频开销不可接受。
3. 已有 CS 方法（OMP、SOMP、MP、off-grid SIGW），逐篇一句。
4. 关键段："It is worth noting that all solutions above heavily rely on the channel sparsity in the angular domain. However, this channel sparsity may not be achievable in XL-MIMO systems, …" → 用物理解释（Rayleigh 距离与天线数平方成正比，从几米到几百米）→ 能量扩散效应 → 已有方案严重退化。
5. "Unfortunately, up to now, there are no related works on near-field channel estimation …" → 相近的近场定位工作及其不适用原因 → 首创句。
6. "To fill in this gap, in this paper, …" → 3 条贡献（reveal / propose / propose）。
7. 路线图（带 "Organization:" 小标签）；8. Notation。

## 4. Idea 是怎么提出的
- 空白类型：已有假设失效（远场平面波 → 近场球面波）+ 新场景（XL-MIMO）。
- 核心洞见句："the change from massive MIMO to XL-MIMO not only means the increase in antenna number, but also leads to the fundamental change in the electromagnetic field structure."
- 第一条贡献是"揭示现象"（energy spread effect），第二条才是方法——先命名问题，再解决问题。
- Fig. 2 用同一信道在远场 / 近场下的角域表示对比，直观展示稀疏性消失（"motivating figure"）。

## 5. 科研方法
- 极坐标域表示：变换矩阵同时采样角度和距离；用 Fresnel 近似推导列相干，Lemma 1 给出距离采样规则（距离倒数等间隔、非均匀采样）。
- 两个算法：on-grid 的 P-SOMP（扩展经典 SOMP）、off-grid 的 P-SIGW（扩展 SIGW，梯度精修距离与角度）；算法命名统一加 "P-" 前缀表示极坐标域版本。
- 复杂度表 + 收敛讨论；附录给引理证明和梯度推导。

## 6. 仿真与实验
- 参数表 Table II。先选设计参数 β_Δ（Fig. 7），再展示极坐标域稀疏性（Fig. 8），再收敛（Fig. 9），最后对比（距离、SNR、导频长度）。
- 近场（5–10 m）和远场（100–120 m）两种距离分布做成子图 (a)(b)，证明新方法在远场也不吃亏。
- 最后一个实验专门验证理论推出的"非均匀距离采样"优于均匀采样——用仿真回扣理论结论。

## 7. 图表
- 13 图 2 表 3 算法。模型部分有 4 张说明图（系统、角域对比、近远场区域划分、两径近场模型）。caption 短："NMSE performance comparison against the distance."

## 8. 句式库
- 依赖假设："It is worth noting that all solutions above heavily rely on the channel sparsity in the angular domain."
- 本质变化："… not only means the increase in antenna number, but also leads to the fundamental change in the electromagnetic field structure."
- 后果："In this case, the angular-domain channel may not be sparse, and thus existing far-field channel estimation schemes … will suffer from severe performance degradation."
- 无人做过："Unfortunately, up to now, there are no related works on near-field channel estimation for high-frequency XL-MIMO."
- 填补空白："To fill in this gap, in this paper, the important problem of … is studied, which is realized by replacing … with …"
- 解释原因："This is because the Fresnel approximation adopted in the polar-domain transform is more accurate than the far-field approximation."

## 9. 结论
- 1 段 234 词：首创声明（"for the first time"）→ 依次复述现象、表示、算法 → 仿真结论（近场显著更好、远场也表现良好）→ 一句未来工作（RIS 近场信道估计）。
