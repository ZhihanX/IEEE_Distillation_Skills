---
doi: 10.1109/tcomm.2019.2956472
title: "Distributed Federated Learning for Ultra-Reliable Low-Latency Vehicular Communications"
journal: TCOM
year: 2020
band: 2019-2021
cites: 391
cites_per_year: 58.6
article_type: research      # 顺延补位：替换改记为 overview 的 tcomm.2019.2914652（Wireless Access in URLLC）
topic: federated-edge-learning
source: xplore-html
xplore: 8917592
auto:
  words_total: 7739
  n_sections: 6
  n_subsections: 9
  n_figures: 10
  n_tables: 1
  n_display_eq: 24
  n_algorithms: 3
  statements: {theorem: 0, lemma: 0, proposition: 2, corollary: 0, proof: 2, proof_in_appendix: 0}
  n_appendix: 2
  mean_sentence_words: 26.5
  we_per_1k: 4.2
  title_words: 8
  abstract_words: 210
  abstract_sentences: 8
  phrases: {toTheBest: 1, inThisPaper: 2, contribList: 1, roadmap: 1, however: 9, transition: 9, resultsShow: 2, motivatedBy: 0, toAddress: 1, gapWord: 0, nonconvex: 0, npHard: 0, closedForm: 0, outperform: 2, intensifier: 0, worthNoting: 2, observe: 1, thisIsBecause: 0, asExpected: 0, insight: 0, tradeoff: 2, figVerb: 5, promising: 0, gen: 0, contrast: 6, firstTime: 0, novel: 2, weProposeFirst: 3, wlog: 0, code: 0, prototype: 0}
  methods: {lyapunov: 9, convergence: 2, convexOpt: 1, lagrange: 1, penalty: 1}
code:
  title_pattern: [X-for-Y]
  abstract_moves: [aim, method, method, method, method, method, result, result]
  abstract_has_numbers: true
  abstract_anchor: in-this-paper    # 被动式锚点："In this paper, the problem of … is studied."
  intro_paragraphs: 6
  intro_moves: [field, prior, gap, prior, contrib, roadmap]
  related_work: in-intro
  contrib_format: paragraph
  contrib_n: 5
  contrib_verbs: [propose, formulate, obtain, develop, use]
  contrib_quantified: true     # 60.9%、28.6%、33.2%
  first_claim: true            # "To the best of our knowledge, with the exception of [1], no work has studied …"
  roadmap: true
  notation: none
  gap_type: [limitation, tool-transfer]
  motivating_figure: true
  problem_class: stochastic
  solution: [lyapunov, gradient]
  theory_role: supporting
  proofs_location: appendix
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 4               # FP、QSO、QSR + 集中式 CEN 参照
  baseline_naming: acronym
  x_axes: [CDF, number-of-users, distance, block-length]
  fig1_role: system-model
  caption_style: descriptive
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[形容词] [学习工具] for [需求] [场景] Communications"，8 词。工具（Federated Learning）在前、场景在后，属"把新工具引入通信问题"型标题。

## 2. 摘要（8 句，210 词）
- 被动语态锚点："In this paper, the problem of joint power and resource allocation (JPRA) for ultra-reliable low-latency communication (URLLC) in vehicular networks is studied."——全摘要几乎无 "we"（we_per_1k 4.2，语料中偏低）。
- 方法链：功耗最小化 + 概率排队时延约束 → EVT 定义新可靠性度量 → FL 估计尾分布（显式写出 i.i.d. 假设）→ 考虑 FL 通信时延 + Lyapunov 得到分布式策略 → 曼哈顿移动模型仿真。
- 两句量化结果："… with up to 79% reductions in the amount of exchanged data." / "… up to 60% reductions of VUEs with large queue lengths, while reducing the average power consumption by two folds, compared to an average queue-based baseline."（数字 + 对比对象）。

## 3. 引言逻辑（6 段，约 1570 词）
1. V2V → 智能交通 → "However, … heavily rely on the availability of V2V communication links with extremely low errors and delays." → URLLC 建模的多个维度 → 排队时延需 RRM → 能效。
2. 已有 RRM 文献逐条罗列 → 归纳共性："The URLLC aspects of this prior art … are captured by either improving the average latencies or imposing a probabilistic constraint …" → "Although …, it fails to control rare events …"（尾部事件）。
3. "In practice, to enable a truly URLLC experience, it is imperative to model and capture extreme, low probability events." → EVT 文献 → 收集样本的开销未被研究 → VUE 不愿共享 QSI → "This shortcoming warrants a collaborative learning model that does not rely on sharing individual QSI."（由缺口推出所需工具的性质）。
4. FL 原理与文献 → 自己的前作 [1] 及其不足 → 首创声明（"with the exception of [1]"）。
5. 贡献段（散文）："The main contribution of this paper is to propose …" → 按步骤叙述 → 末尾 3 个百分比。
6. 路线图。

## 4. Idea 是怎么提出的
- 空白类型：已有方法局限（平均时延 / 概率约束控制不了尾部）+ 工具迁移（EVT 刻画极端事件、FL 免共享原始数据）。
- 写法亮点："需求 → 工具 A（EVT）→ 工具 A 带来的新问题（样本收集开销、隐私）→ 工具 B（FL）"的两级推导，每个工具都由上一步的缺陷"召唤"出来。
- 坦白假设：摘要与贡献段都写出 i.i.d. 假设，结论中再把它列为局限和未来工作。

## 5. 科研方法
- 模型：RSU 分组分配 RB 的 V2V 网络（Fig. 1）；排队模型；网络级功耗最小化，约束为队列长度超阈值的概率与超出部分的统计量。
- EVT：超阈值队列长度服从 GPD（Pickands–Balkema–de Haan）→ 用 GPD 的前两阶矩重写约束 → 虚拟队列 + Lyapunov 漂移加罚（Proposition 1）→ 每个 VUE 的分布式功率分配。
- 学习：块最大值采样 → 集中式 CEN（SVRG 求 MLE）vs 同步 FL vs 异步 FL（Proposition 2 给对数似然梯度）→ 三种方式与 RSU 通信的开销（复用 V2V 的 RB）。

## 6. 仿真与实验
- 250 m × 250 m 曼哈顿移动模型、9 个路口；参数 Table I（注明来源 [4]、[6]、[18]、[31]）。
- 先比较学习精度与通信量（CEN vs async-FL），再与 3 个基准（FP 固定功率、QSO 仅队列稳定、QSR 平均队列概率约束）比较功率、平均 / 最大队列、可靠性、尾分布均值与方差、收发距离影响，最后单列小节讨论有限码长影响。
- 公平性说明："For a fair comparison, the transmit power of vTxs in FP is chosen as the average of transmit powers from all other five methods."

## 7. 图表
- 10 图 1 表 3 算法。Fig. 1 系统示意、Fig. 2 VUE 与 RSU 间四个过程的关系图、Fig. 3 三种学习方式的时序图（上传 / 下载与 V2V 切换）。
- 多数结果图用 (a)/(b) 子图成对展示（如功率 + 平均队列、最大队列 + 可靠性）。

## 8. 句式库
- 依赖性："However, the performance of emerging transportation applications heavily rely on the availability of V2V communication links with extremely low errors and delays."
- 归纳已有工作的共性："The URLLC aspects of this prior art … are captured by either improving the average latencies or imposing a probabilistic constraint to maintain small queue lengths."
- 共性的不足："Although such a probabilistic constraint on the queue length improves network reliability, it fails to control rare events …"
- 由缺陷召唤工具："This shortcoming warrants a collaborative learning model that does not rely on sharing individual QSI."
- 带例外的首创："To the best of our knowledge, with the exception of [1], no work has studied the use of federated learning in the context of URLLC."
- 承认假设："It is worth noting that the accuracy of FL-based tail distribution modeling relies on the assumption of IID queue length samples."
- 补充（skill 引用）："Furthermore, the proposed method yields up to 60% reductions of VUEs with large queue lengths, while reducing the average power consumption by two folds, …"
- 补充（skill 引用，结构标签）："Appendix A Proof of Proposition 1"

## 9. 结论
- 1 段 224 词，现在完成时（"we have formulated / have proposed / have shown"）→ 定性结果（无数字）→ 承认 i.i.d. 假设 → 未来工作：non-IID 数据下的 FL。
