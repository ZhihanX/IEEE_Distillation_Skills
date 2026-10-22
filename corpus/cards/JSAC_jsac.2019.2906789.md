---
doi: 10.1109/jsac.2019.2906789
title: "Space/Aerial-Assisted Computing Offloading for IoT Applications: A Learning-Based Approach"
journal: JSAC
year: 2019
band: 2019-2021
cites: 847
cites_per_year: 114.1
article_type: research
topic: MEC-offloading
source: xplore-html
xplore: 8672604
auto:
  words_total: 6396
  n_sections: 8
  n_subsections: 10
  n_figures: 11
  n_tables: 2
  n_display_eq: 30
  n_algorithms: 2
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 26.9
  we_per_1k: 8.9
  title_words: 9
  abstract_words: 226
  abstract_sentences: 7
  phrases: {toTheBest: 1, inThisPaper: 4, contribList: 1, roadmap: 0, however: 11, transition: 8, resultsShow: 1, motivatedBy: 1, toAddress: 4, gapWord: 1, nonconvex: 1, npHard: 1, closedForm: 0, outperform: 0, intensifier: 2, worthNoting: 0, observe: 10, thisIsBecause: 2, asExpected: 0, insight: 2, tradeoff: 0, figVerb: 6, promising: 3, gen: 3, contrast: 2, firstTime: 1, novel: 0, weProposeFirst: 5, wlog: 0, code: 0, prototype: 0}
  methods: {convergence: 7, complexity: 6, DNN: 2, DRL: 2, convexOpt: 1, lyapunov: 1}
code:
  title_pattern: [X-aided-Y, X-for-Y, colon-subtitle]
  abstract_moves: [gap, aim, method, method, method, method, result]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 4
  intro_moves: [field, gap, solution, gap, aim, contrib]
  related_work: separate-section
  contrib_format: bullets
  contrib_n: 3
  contrib_verbs: [formulate, adopt, evaluate]
  contrib_quantified: false
  first_claim: true
  roadmap: false
  notation: table
  gap_type: [new-scenario, new-architecture]
  motivating_figure: true
  problem_class: learning
  solution: [DRL, DNN, heuristic]
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: true
  baselines_n: 3
  baseline_naming: descriptive
  x_axes: [edge-capacity, number-of-tasks, episodes, cost-weights]
  fig1_role: architecture
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---

## 1. 标题
- "[网络]-Assisted [任务] for [应用]: A Learning-Based Approach"，9 词。冒号后方法类副标题（与 "A Deep Reinforcement Learning Approach" 同型）。

## 2. 摘要（7 句，226 词）
- 第 1 句同时给问题与难点："IoT computing offloading is a challenging issue, especially in remote areas where common edge/cloud infrastructure is unavailable."
- "In this paper, we present a space-air-ground integrated network (SAGIN) edge/cloud computing architecture for …"——先架构（UAV 提供边缘计算、卫星接入云）。
- First（UAV 边缘服务器 VM 分配 + 任务调度）/ Second（SAGIN 卸载 → MDP → 深度强化学习，策略梯度处理大动作空间、actor-critic 加速学习）。
- 末句两部分结果（近优低复杂度；收敛快、总代价低）。无数字。

## 3. 引言逻辑（4 段，约 900 词；无路线图段）
1. 5G 与 IoT 应用 → "However, besides efficient and reliable communication, a wide spectrum of applications also require massive computing capabilities." → 云计算时延长 → MEC 及其研究议题。
2. "However, 5G networks may fail to provide ubiquitous coverage to suburban and rural areas, …" → "To this end, we propose to employ the space-air-ground integrated network (SAGIN) architecture …" → 三个网络段各自的资源与限制（LEO/GEO、UAV/HAP/气球）→ "However, employing the SAGIN in IoT computing offloading introduces several challenging issues. Firstly, … Secondly, …"
3. "In this paper, we present …"：VM 化 + 混合整数规划 + 启发式；MDP + 无模型 RL + actor-critic → 首创声明（并说明意义："which validates the feasibility of SAGIN supporting computation-intensive applications for remote IoT users"）。
4. "The main contributions of the paper can be summarized as follows." + 3 条 bullet。
- 相关工作单列一节（MEC / SAGIN 两个小节）。

## 4. Idea 是怎么提出的
- 空白类型：新场景（无地面覆盖的偏远 IoT）+ 新架构（空天地一体化同时提供边缘与云计算）。
- 写法亮点：先找"现有范式失效的地方"（5G 覆盖不到的郊区与农村），再提出一个现成但尚未用于计算卸载的网络架构；挑战用 Firstly / Secondly 两条写清，分别对应论文的两部分方法。
- 首创声明后接一句"它证明了什么 / 能提供什么指导"，把首创包装成可行性验证。

## 5. 科研方法
- 模型：地面（IoT 设备）、空中（UAV 边缘服务器）、空间（卫星接入云）三段；多用户多任务；代价 = 时延 + 能耗 + 服务器使用费（加权）。
- VM 分配与任务调度：混合整数规划（含 0–1 二次子问题，NP-hard）→ 启发式算法（Fig. 2 用一个两 VM 的例子说明调度思路）。
- 卸载：MDP 四要素（状态 / 动作 / 转移概率 / 奖励）编号列出 → 状态空间指数增长 + 模型难以准确刻画 → 无模型 RL；Q-learning 处理不了大动作空间 → 策略梯度 + actor-critic + 深度网络（Fig. 3 实现框图）。
- 无定理。

## 6. 仿真与实验
- Table II 参数；IoT 设备参数参照具体硬件（ARM Cortex-M、200 MC/s、141 mW）并给出处。
- VM 部分：与 'Brute-force'、'Random' 比较时延与运行时间（暴力法运行时间指数增长）。
- RL 部分：收敛 → 不同代价权重（α、β、ϖ）下的总代价 → 能耗与时延分解 → 卸载方式选择比例；与 'Random'、'Greedy on edge' 比较（基准用引号标签 + 编号列表定义）。

## 7. 图表
- 11 图 2 表 2 算法。Table I 记号表放在引言之后；Fig. 1 SAG-IoT 架构总览，Fig. 2 调度示例，Fig. 3 actor-critic 框图（caption 说明两网络各自作用）。结果 caption 短标签（"Total cost v.s. α."）。

## 8. 句式库
- 通信之外的需求："However, besides efficient and reliable communication, a wide spectrum of applications also require massive computing capabilities."
- 覆盖盲区："However, 5G networks may fail to provide ubiquitous coverage to suburban and rural areas, where IoT devices could be widely deployed …"
- 提出架构："To this end, we propose to employ the space-air-ground integrated network (SAGIN) architecture for the computing offloading of remote IoT applications."
- 挑战枚举："However, employing the SAGIN in IoT computing offloading introduces several challenging issues. Firstly, … Secondly, …"
- 首创 + 意义："To the best of our knowledge, our work is the first work to study the computing offloading problem in SAGIN, which validates the feasibility of …"
- 方法选择理由："Although Q-learning methods have shown great potentials in solving RL problems with a large state space, it usually cannot efficiently deal with problems with large or even continuous action spaces, …"

## 9. 结论
- 1 段 125 词，现在完成时复述 → "Our work can offer valuable insights to the important yet underexplored field of edge/cloud computing in SAGIN." → 一句未来工作（通信、缓存、计算联合优化）。无数字。
