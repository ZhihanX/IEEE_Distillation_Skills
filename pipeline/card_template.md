# 单篇蒸馏卡片模板

每篇论文一张卡片，存为 `corpus/cards/<journal>_<doi 后缀>.md`（如 `JSAC_jsac.2018.2815360.md`）。
引用原文只摘短句（单句、≤ 30 词），用于说明句式；不要复制段落。

卡片 = YAML front matter（汇总脚本 `pipeline/aggregate_cards.py` 只读这部分）+ 正文 1–9 节（人读，给规律配例句）。
`auto` 下的数字直接抄 `pipeline/xplore_extract.js` 的输出；`code` 下用受控词表手工编码，一个字段一个判断，
拿不准就写 `unclear`，不要猜。

```yaml
---
doi: 10.1109/jsac.2018.2815360
journal: JSAC                  # TWC / JSAC / TCOM
year: 2018
band: 2016-2018                # 2016-2018 / 2019-2021 / 2022-2025
cites: 1019                    # Crossref，抓取于 2026-10
cites_per_year: 118.6
article_type: research         # research / overview（综述、教程、展望、邀请文章）
topic: MEC-offloading          # select_papers.py 的 primary_topic，读完可改
source: xplore-html            # xplore-html / arxiv-v<N>
xplore: 8314696
auto:                          # 抄提取器 stats / phrases / methods
  words_total: 4692
  n_sections: 6
  n_subsections: 18
  n_figures: 5
  n_tables: 3
  n_display_eq: 24
  n_algorithms: 1
  statements: {theorem: 1, lemma: 1, proposition: 0, corollary: 0, proof: 2, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 24.1
  we_per_1k: 14.8
  title_words: 11
  abstract_words: 176
  abstract_sentences: 8
  phrases: {toTheBest: 2, contribList: 1, roadmap: 1, ...}
  methods: {KKT: 2, convexOpt: 3, ...}
code:
  title_pattern: [X-for-Y]     # X-for-Y / X-via-Y / X-with-Y / X-in-Y / X-aided-Y / colon-subtitle / versus / question /
                               # noun-phrase / toward / verb-ing（Exploiting / Using / Leveraging …）
  abstract_moves: [context, gap, aim, method, method, method, result]
                               # 每句一个：context / gap / aim / method / theory / result / implication
  abstract_has_numbers: true   # 摘要里有具体量化数字（%、dB、倍数）
  abstract_anchor: in-this-paper   # in-this-paper / this-paper-verb / we-verb / none
  intro_paragraphs: 6
  intro_moves: [field, tech, gap, solution, approach, roadmap]
                               # 每段一个：field / tech / prior / gap / aim / solution / approach / contrib / roadmap / notation / reproducibility（代码数据链接段）
  related_work: separate-section   # separate-section / in-intro / in-intro-subsection / table / none
  contrib_format: bullets      # bullets / numbered / paragraph / none
  contrib_n: 3
  contrib_verbs: [propose, present, conduct]
  contrib_quantified: true     # 贡献条目里出现性能数字
  first_claim: true            # "to the best of our knowledge … first" 类首创声明
  roadmap: true                # "The rest of this paper is organized as follows"
  notation: table              # intro-end / model-start / table / footnote / none
  gap_type: [combination, new-architecture]
                               # limitation / new-scenario / new-architecture / theory-gap / combination（A、B 各自有研究但未结合）/
                               # counterintuitive / unification / scalability / practicality /
                               # tool-transfer（把其他领域的新工具引入通信，如 DRL、LLM、扩散模型）
                               # / comparison（A 与 B 孰优尚无定论，如 RIS vs 中继、cell-free vs small cells）
  motivating_figure: true      # 引言或模型开头有示意图（场景 / 架构）
  problem_class: MINLP         # convex / nonconvex-continuous / MINLP / combinatorial / stochastic /
                               # analysis-only / learning / estimation / none
  solution: [decomposition, KKT, relaxation]
                               # AO / BCD / SCA / SDR / MM / FP / penalty / manifold / lagrangian-dual / KKT /
                               # closed-form / decomposition / relaxation / bisection / heuristic / DRL / DNN /
                               # stochastic-geometry / random-matrix / CRB / compressed-sensing / game / lyapunov /
                               # bound-surrogate（用推出的性能界当优化目标）/ gradient（投影 / 普通梯度下降）/
                               # reformulation（变量替换等把原问题等价变成凸或可解形式）/ exhaustive-search /
                               # tensor-decomposition（PARAFAC 等）/ message-passing（AMP / VAMP / BP）
  theory_role: supporting      # central / supporting / none
  proofs_location: body        # body / appendix / mixed / none
  complexity_analysis: false
  convergence_analysis: true   # 有收敛性证明或论证（单调有界、命题等）；只画收敛曲线记入 x_axes: iterations
  sim_param_table: true
  baselines_n: 2
  baseline_naming: descriptive # descriptive（"random offloading"）/ acronym / reference-only
  x_axes: [computation-amount, data-size]
  fig1_role: architecture      # system-model / architecture / scenario / framework / result / none
  caption_style: short-label   # short-label / descriptive / self-contained-conclusion
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 1
  conclusion_has_numbers: false
  conclusion_future_work: true
---
```

## 1. 标题
- 结构模式、词数；有无缩写、冒号副标题

## 2. 摘要（按句拆 move）
- 每句的功能：背景 / 空白 / 本文方法 / 关键技术 / 量化结果 / 意义
- 是否给出具体数字；是否出现 "In this paper" 类锚点句

## 3. 引言逻辑
- 段落序列：每段一句话概括其作用（建立领域 → 现有工作 → 空白 → 本文）
- 相关工作的组织方式（按方法分组 / 按场景分组 / 表格对比）
- 贡献列表：条数、每条的开头动词、是否带量化
- 是否有 "The rest of this paper is organized as follows"
- 记号说明段（Notation）位置

## 4. Idea 是怎么提出的
- 空白类型：现有方法局限 / 新场景新硬件 / 理论缺口 / 反直觉观察 / 统一框架
- 核心洞见句（摘一句）
- 有没有 motivating example 或开篇示意图

## 5. 科研方法
- 系统模型：场景图、信道模型、假设
- 问题形式化：目标函数、约束、是否非凸
- 求解路线：AO / SCA / SDR / BCD / 拉格朗日对偶 / 闭式解 / 深度学习 / 随机几何
- 理论结果：定理、引理、命题数量，证明放附录还是正文
- 复杂度 / 收敛性分析

## 6. 仿真与实验
- 仿真参数表、baseline 数量与命名方式、横轴变量
- 是否有实测 / 原型；是否开源代码
- 结果段的写法：现象 → 原因解释 → 启示

## 7. 图表
- 图表总数、Fig. 1 的角色（系统模型 / 框架 / 问题示意）
- 结果图类型（性能 vs SNR / 天线数 / 用户数 / 迭代次数的收敛曲线 …）
- caption 风格：长短、是否自含结论
- 表格：参数表 / 对比表 / 符号表

## 8. 句式库（按功能，各摘 1–2 句）
- 指出空白、陈述贡献、对比 baseline、解释结果、承认局限、展望未来

## 9. 结论
- 结构：总结 → 主要发现 → 未来工作；是否重复数字
