---
doi: 10.1109/jsac.2023.3287540
title: "Full-Duplex Communication for ISAC: Joint Beamforming and Power Optimization"
journal: JSAC
year: 2023
band: 2022-2025
cites: 346
cites_per_year: 111.9
article_type: research
topic: ISAC-sensing
source: xplore-html
xplore: 10158711
auto:
  words_total: 8779
  n_sections: 6
  n_subsections: 14
  n_figures: 12
  n_tables: 1
  n_display_eq: 51
  n_algorithms: 3
  statements: {theorem: 2, lemma: 0, proposition: 2, corollary: 0, remark: 1, proof: 4, proof_in_appendix: 4}
  n_appendix: 5
  mean_sentence_words: 25.0
  we_per_1k: 13.2
  title_words: 9
  abstract_words: 259
  abstract_sentences: 10
  phrases: {toTheBest: 0, inThisPaper: 5, contribList: 1, roadmap: 1, however: 3, transition: 21, resultsShow: 1, motivatedBy: 2, toAddress: 9, gapWord: 0, nonconvex: 8, npHard: 1, closedForm: 3, outperform: 1, intensifier: 5, worthNoting: 0, observe: 11, thisIsBecause: 3, asExpected: 0, insight: 0, tradeoff: 1, figVerb: 5, promising: 0, gen: 0, contrast: 4, firstTime: 0, novel: 0, weProposeFirst: 1, wlog: 2, code: 0, prototype: 0}
  methods: {complexity: 16, convergence: 10, SCA: 8, KKT: 7, convexOpt: 3, lagrange: 2, AO: 1, CRB: 1}
code:
  title_pattern: [X-for-Y, colon-subtitle]
  abstract_moves: [context, aim, method, method, method, gap, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 8
  intro_moves: [field, prior, prior, gap, aim, contrib, roadmap, notation]
  related_work: in-intro
  contrib_format: bullets
  contrib_n: 4
  contrib_verbs: [extend, derive, propose, consider]
  contrib_quantified: false
  first_claim: false
  roadmap: true
  notation: intro-end
  gap_type: [limitation, unification]
  motivating_figure: true
  problem_class: nonconvex-continuous
  solution: [closed-form, SCA, SDR, AO]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: true
  convergence_analysis: true
  sim_param_table: false
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [radar-SINR, iterations, angle, self-interference, SINR-target]
  fig1_role: scenario
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[关键能力] for [应用]: Joint [A] and [B] Optimization"，9 词。冒号前说"做什么推广"（全双工通信用于 ISAC），冒号后说"怎么做"（联合优化）。

## 2. 摘要（10 句，259 词）
- 第一句先概括已有工作的设定（全双工感知 + 半双工通信），第二句直接说推广："To achieve higher spectral efficiency, in this paper, we extend existing ISAC beamforming design to a general case by considering the FD capability for both radar and communication."——"推广到一般情形"式锚点句。
- 中段：系统 → 变量 → 两个准则（功耗最小 / 和速率最大）→ 难点（上下行与回波、干扰紧耦合）→ 先求接收波束闭式解再代回 → 特例的低复杂度设计。
- 结尾 "brings tremendous improvements in terms of both power efficiency and spectral efficiency compared to the conventional ISAC with HD communication"，无数字。

## 3. 引言逻辑（8 段，约 1460 词）
1. ISAC 动机（车联网、智能工厂、频谱重叠）及优势。
2. 发射波束成形工作综述 → "Note that these works only design the transmit beamforming while the reception of radar echo is not considered."
3. 考虑回波接收的工作，分两类并用 Fig. 1 (a)(b) 图示（下行 ISAC / 上行 ISAC）——引言里直接画出已有工作的两种设定。
4. 空白：这些工作雷达是全双工、通信却是半双工 → "Therefore, to achieve higher spectral efficiency, it is motivated to consider the FD capability also for communication" → 新难点（感知—通信干扰 + 上下行耦合）→ 已有算法逐一说明为何不能直接用。
5. "Motivated by the above discussions, we investigate …" + Table I 与已有 FD ISAC 工作对比。
6. 两个问题的形式化思路 + 与 [14]–[19] 的区别 → 4 条贡献。
7. 路线图；8. Notations。

## 4. Idea 是怎么提出的
- 空白类型：已有工作局限（通信半双工）+ 统一 / 推广（覆盖上行、下行、感知三者的一般情形）。
- 写法亮点：用一张示意图（Fig. 1）和一张对比表（Table I）在引言里把"已有设定"和"本文设定"并排摆出——比文字描述更清楚地界定新意。

## 5. 科研方法
- 模型：双 ULA 全双工基站、K 个上行用户、L 个下行用户、点目标、信号相关干扰 + 残余自干扰；接收端线性波束得到雷达 SINR 和上行 SINR。
- 先求最优接收波束闭式解（Proposition 1，MVDR / MMSE 形式）→ 代回得到只含发射波束与功率的等价问题 → SCA + 秩松弛（Theorem 1 证明松弛紧）。
- 特例（只有上行通信）：交替优化，子问题化为 SOCP（Theorem 2、Proposition 2）。
- 和速率最大化同样先代入闭式接收机再 SCA。
- 证明全部在附录，另有附录专门给出 TDD 基准的细节。

## 6. 仿真与实验
- 参数在 "Parameter Setup" 小节正文给出；三个基准："HD mode"、"communication-only"、"sensing-only"（引号标签，各自说明其作用：例如 communication-only 用于"evaluate the impact of integrating the sensing functionality"）。
- 除性能曲线外，大量使用波束方向图（雷达 / 通信两种功能分别画）直观展示设计效果。

## 7. 图表
- 12 图 1 表。Fig. 1 已有工作的两种 ISAC 设定（引言），Fig. 2 本文系统（含自干扰消除流程）。caption 短标签，Fig. 1 例外（长说明）。

## 8. 句式库
- 推广型目标："To achieve higher spectral efficiency, in this paper, we extend existing ISAC beamforming design to a general case by considering …"
- 指出遗漏："Note that these works only design the transmit beamforming while the reception of radar echo is not considered."
- 动机推导："Therefore, to achieve higher spectral efficiency, it is motivated to consider the FD capability also for communication …"
- 不能直接套用："Existing algorithms in [14]–[19] cannot be straightforwardly applied to address these challenges. Specifically, …"
- 难度："… whose globally optimal solutions are hard to obtain by polynomial-time algorithms in general."
- 基准作用："This scheme helps evaluate the impact of integrating the sensing functionality on the communication performance."

## 9. 结论
- 1 段 163 词：过去时复述 → "The performance gains are most notable when the residual SI power is low and the sensing requirement is less restrictive."（指出增益最明显的条件）→ 一句未来工作。
