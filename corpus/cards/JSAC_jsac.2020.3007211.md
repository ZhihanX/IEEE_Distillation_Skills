---
doi: 10.1109/jsac.2020.3007211
title: "Smart Radio Environments Empowered by Reconfigurable Intelligent Surfaces: How It Works, State of Research, and The Road Ahead"
journal: JSAC
year: 2020
band: 2019-2021
cites: 3224
cites_per_year: 544.1
article_type: overview      # 综述 + 教程（电磁建模框架）+ 文献全景 + 研究路线
topic: RIS
source: xplore-html
xplore: 9140329
auto:
  words_total: 45485
  n_sections: 9
  n_subsections: 56
  n_figures: 35
  n_tables: 1
  n_display_eq: 51
  n_algorithms: 0
  statements: {theorem: 0, lemma: 0, proposition: 0, corollary: 0, proof: 0, proof_in_appendix: 0}
  n_appendix: 0
  mean_sentence_words: 24.2
  we_per_1k: 2.4
  title_words: 18
  abstract_words: 245
  abstract_sentences: 7     # 提取器把 "C. E. Shannon" 等人名缩写误切成多句，人工计为 7 句
code:
  title_pattern: [colon-subtitle]
  abstract_moves: [context, context, context, context, implication, aim, implication]
  abstract_has_numbers: false
  abstract_anchor: in-this-paper
  intro_paragraphs: 5
  intro_moves: [aim, field, field, solution, prior]
  related_work: separate-section   # "The State of Research"（约 2.2 万词，按主题分小节）
  contrib_format: none
  contrib_n: 0
  contrib_verbs: []
  contrib_quantified: false
  first_claim: false
  roadmap: true                    # 单列一节 "Structure of the Paper"（60 词）
  notation: table
  gap_type: [unification]
  motivating_figure: true
  problem_class: none
  solution: []
  theory_role: none
  proofs_location: none
  complexity_analysis: false
  convergence_analysis: false
  sim_param_table: false
  baselines_n: 0
  baseline_naming: none
  x_axes: []
  fig1_role: framework
  caption_style: short-label
  prototype_or_measurement: false
  code_released: false
  conclusion_paragraphs: 2
  conclusion_has_numbers: false
  conclusion_future_work: false
---

> 本卡只做结构与写法层面的记录（overview 不参与研究论文的统计）；只抽取了摘要、引言、章节结构与图注。

## 1. 标题
- "[概念] Empowered by [技术]: How It Works, State of Research, and The Road Ahead"，18 词。副标题三段式直接对应论文三大块（原理 / 现状 / 展望），是长综述的目录式副标题。

## 2. 摘要（7 句，245 词）
- 前 5 句定义与定位 RIS（两种实现方式；与相控阵、多天线、中继的硬件对比；C-SWaP；使能"智能无线环境"）。
- "In this paper, we (i) introduce …; (ii) overview …; (iii) present …; (iv) provide …; and (v) discuss …"——用罗马数字把五项工作压进一句。
- 末句提出学科层面的主张：需要把 Shannon 的通信理论与 Green、Maxwell 的电磁理论"重新统一"。

## 3. 引言（5 段，约 680 词）
- 第 1 段是一连串问题（"What is a reconfigurable intelligent surface (RIS)? What is a smart radio environment (SRE)? …"），以问题清单作为全文的阅读动机。
- 之后每段以粗体短语起头（run-in heading）："Increasing data traffic." → "Current network design assumptions."（前五代网络把无线环境视为不可控的三条公设）→ "An emerging paradigm: Programming the environment." → "The road to smart radio environments."
- 路线图单列为第 2 节。

## 4. 章节组织
- RIS（实物样机照片、近无源、概念结构、"surfaces vs. smart surfaces"、超材料）→ 智能无线环境（应用、场景、机器学习的作用）→ 宏观均匀化的通信理论建模（约 1.6 万词的教程主体：表面电磁学、超表面建模、反射系数、近场 / 远场、Huygens-Fresnel）→ 研究现状（约 2.2 万词：综述、合作项目、物理与电磁、初期工作、路损与信道建模、调制 ……）→ The Road Ahead → 结论 → 视频演示链接。

## 5. 图表
- 35 图 1 表。Fig. 1 "Radio environments vs. smart radio environments" 对比概念图；Fig. 2–3 为 MIT、NTT DOCOMO 的样机照片；大量电磁原理图与数值曲线（部分 "reproduced from [5]"，注明来源）；Table I 为常用记号。caption 短标签为主，复用他人图时在 caption 中标出处。

## 6. 对 skill 的意义
- 长综述的引言可以用"问题清单 + 粗体段首"组织，而不是研究论文的"现状 → 空白 → 贡献"。
- 结论以引用 Green 文集序言收尾，属罕见的文学化写法；正文 we 密度极低（2.4/千词），以客观陈述为主。
