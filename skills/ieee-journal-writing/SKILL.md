---
name: ieee-journal-writing
description: Draft, structure, or revise an IEEE Transactions research paper in wireless communications and networking (IEEE TWC, JSAC, TCOM and similar journals) — title, abstract, introduction and contribution list, research-gap framing, system model and problem formulation, algorithm and theory sections, simulation results, figures and captions, conclusion. Also use to turn a research idea into a paper outline, or to check a draft against what highly cited IEEE papers do. 适用于：IEEE 期刊论文写作、TWC/JSAC/TCOM 投稿、摘要/引言/贡献/仿真/图注的撰写与修改、把 idea 写成论文提纲。
---

# IEEE 期刊论文写作（TWC / JSAC / TCOM）

依据：80 篇高引论文的逐篇蒸馏卡片——72 篇研究论文、8 篇综述 / 教程，2016–2025 年，Crossref 引用 ≥ 50，
按年均引用在三个年份段分层抽样，单一主题不超过约 25%。

- "k/72" = 72 篇研究论文中有 k 篇这样做；"中位数 [四分位距]" 来自 `corpus/summary.md`。
- "≥k/72" = 卡片笔记的关键词计数，是下限。
- 例句是原文单句短引（≤ 30 词），后附 DOI 后缀（省略 `10.1109/`）。例句用来示范句子的功能，写作时换成自己的内容，不要照抄。
- 这些规律描述的是"高引论文通常怎么写"，不是投稿硬性要求；与目标期刊的作者指南冲突时以指南为准。

## 工作流
1. **判断文体**。默认是研究论文。综述 / 教程的结构完全不同，见 `references/structure.md` 第 9 节。
2. **定 idea 的说法**。先写一句"已有工作做到哪里 + 还缺什么 + 本文做什么"的定位句。选 1–2 种空白类型：
   limitation 45/72 最常见；62/72 篇组合使用两种。见 `references/idea-framing.md`。
3. **搭骨架**。按下方"默认骨架"列出各节，再按 `references/structure.md` 给每段指定功能。
4. **写正文**。按段落功能从 `references/phrasebank.md` 选句式，再改写成自己的内容。
5. **方法与仿真**。见 `references/methodology.md`：问题类型 → 求解路线 → 理论结果 → 复杂度 / 收敛 → 仿真设置与基准 → 结果分析。
6. **图表**。见 `references/figures.md`：Fig. 1、结果图的横轴、caption、表格。
7. **终稿检查**。用下方清单和 `references/ieee-conventions.md` 检查。

用户只给 idea 时，先产出：标题候选（2–3 个）、摘要（8 句）、引言段落提纲（每段一句功能说明）、
贡献列表（3–4 条）、章节列表、计划的图（Fig. 1 + 结果图横轴），再逐节展开。

## 默认骨架（研究论文）

| 部分 | 默认做法 | 依据（72 篇研究论文） |
|---|---|---|
| 标题 | 约 10 词，"X for Y" 结构；冒号副标题可选 | 词数 10 [8–12]；X-for-Y 42/72，colon-subtitle 22/72 |
| 摘要 | 单段 8 句、约 220 词：背景 → "In this paper, we …" → 方法 2–3 句 → 结果 | 句数 8 [8–9]，词数 220 [197–253]；in-this-paper 52/72；以结果句收尾 69/72 |
| 引言 | 7 段：领域 → 技术 → 已有工作 → 空白 → 本文 → 贡献列表 → 路线图 → 记号说明 | 段数 7 [6–8]；首段为领域 62/72；末尾是路线图或记号 66/72 |
| 贡献 | 3–4 条 bullet，每条以动词开头 | 条数 4 [3–4]；bullets 44/72，numbered 10/72；首个动词 propose 20/72、formulate 12/72 |
| 相关工作 | 写在引言里，不单列一节 | in-intro 47/72，引言内小节 16/72，单列 9/72 |
| 章节 | 6 节：Introduction / System Model（含 Problem Formulation）/ 1–2 节方法 / Simulation（Numerical）Results / Conclusion | 节数 6 [6–7] |
| 体量 | 正文约 7,750 词，10 张图，约 40 个行间公式，2 个算法框，1 张表 | 见 `corpus/summary.md` |
| 理论 | 2–3 个定理 / 命题 / 引理，配 Remark 解读；证明放附录 | 定理类陈述中位数 2.5；remark 33/72；证明在附录或附录+正文 35/72 |
| 仿真 | 3 个基准，用描述性名称；收敛曲线 + 关键参数扫描 | 基准 3 [2–4]；描述性命名 55/72；迭代曲线 27/72 |
| 结论 | 1 段：复述做了什么 + 关键发现；不重复数字 | 1 段 56/72；无数字 66/72；写未来工作 36/72 |

## 终稿检查清单
- [ ] 摘要只有一句锚点句（"In this paper, we …"），最后一句是结果；摘要可以不写数字（只有 13/72 写了数字）。
- [ ] 每个"空白"句都指向具体文献（"the works in [11]–[14] only consider …"），而不是笼统的 "existing works"。
- [ ] 引言结尾依次是：贡献列表 → "The rest of this paper is organized as follows." → Notations（roadmap 62/72；记号放引言末 43/72）。
- [ ] 每条贡献都能在正文某一节找到对应内容。
- [ ] 首创声明（33/72 有）带限定："To the best of our knowledge, this is the first work that …" + 具体设定；没把握时用 "one of the first" 一类弱化说法。
- [ ] 非凸 / NP-hard 等难度声明后紧跟求解思路（nonconvex 一词出现在 46/72 篇）。
- [ ] 每个定理后用一句话解读它的含义（"Theorem 1 reveals that …"）。
- [ ] 仿真节先交代参数（表或正文）和基准定义，再逐图分析；至少有一个上界、最优解或理想 CSI 作参照（≥ 19/72）。
- [ ] 每个结果段写"现象 → 原因（"This is because …"，39/72）→ 启示"，不只描述曲线走势。
- [ ] Fig. 1 是系统模型 / 场景图（system-model 45/72），放在引言末或模型节开头。
- [ ] 结论不引入新结果；需要时最后一句写未来工作。

## 期刊与年代差异（按需参考）
- **JSAC**：单列相关工作较多（8/24）、编号贡献较多（7/24）、DNN 方法较多（9/24）、记号表较多（8/24）。
- **TWC**：贡献动词 derive 最多（13/24），迭代收敛图最常见（12/24），仿真参数表最多（12/24）。
- **TCOM**：结论写未来工作最多（17/24），首创声明最少（6/24），证明放附录或附录+正文最多（16/24）。
- **2022–2025**：冒号副标题增多（11/24），不含定理的论文增多（10/24），Fig. 1 更常是新架构图（8/24）。

## 参考文件
- `references/structure.md`：各部分的段落功能、长度与顺序；综述 / 教程的结构。
- `references/idea-framing.md`：空白类型、引言论证链、标题、首创声明、与相近工作的区分。
- `references/phrasebank.md`：按功能分类的句式与例句。
- `references/methodology.md`：问题类型、求解路线、理论、复杂度 / 收敛、仿真设置与结果分析。
- `references/figures.md`：图表数量、Fig. 1、结果图、caption、表格、算法框。
- `references/ieee-conventions.md`：IEEE 期刊惯例，包括节号、记号段、定理环境、附录、引用与命名。

## 相关 skill
- 语义通信 / JSCC 方向的选题（生成 idea、查新、评估实验设计、预判审稿风险）用 `semantic-comm-ideas`；
  idea 定下来后再回到本 skill 写论文。
