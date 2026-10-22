# 结构：每一部分写什么、写多长、按什么顺序

统计口径：72 篇研究论文（TWC / JSAC / TCOM 各 24 篇）。"k/72" 为含该特征的论文数；数值为中位数 [四分位距]。
例句后括号内是 DOI 后缀（省略 `10.1109/`）。

## 1. 全文体量

| 指标 | 全部 | TWC | JSAC | TCOM |
|---|---|---|---|---|
| 正文词数 | 7750 [6839–8738] | 7871 | 7292 | 7761 |
| 一级节数（不含附录） | 6 [6–7] | 6 | 6 | 6.5 |
| 二级小节数 | 15.5 [11–22] | 15 | 17.5 | 14 |
| 图 | 10 [8–12] | 11 | 10 | 10 |
| 表 | 1 [0–2] | 1.5 | 1 | 1 |
| 行间公式 | 41.5 [32–55] | 44 | 31.5 | 46.5 |
| 算法框 | 2 [1–3] | 2 | 2 | 2 |
| 平均句长（词） | 26.5 [24.5–28.3] | 27.0 | 25.6 | 26.7 |
| 每千词 "we" | 9.9 [7.0–12.7] | 9.1 | 11.1 | 9.9 |

- 中间 80% 的论文（第 10–90 百分位）：正文 6,200–9,300 词，图 7–14 张，行间公式 25–68 个。
- 第一人称 "we" 是常态；也有几乎全用被动语态的高引论文（每千词 3.7–4.2：twc.2022.3153316、tcomm.2019.2956472），两种都可以，全文保持一致即可。

## 2. 标题
详见 `idea-framing.md` 第 5 节。要点：约 10 词 [8–12]；X-for-Y 42/72；冒号副标题 22/72（2022–2025 年段 11/24）。

## 3. 摘要

**长度**：8 句 [8–9]、220 词 [197–253]，单段；中间 80% 在 174–274 词之间，最短 154、最长 306 词。

**句子功能序列**（每句一个功能）：
- 开头：背景句 44/72，直接写本文 26/72，先写空白 2/72。
- 背景句数：1 句 32/72，0 句 20/72，2 句 15/72，3 句以上 5/72。背景不超过 2 句。
- 空白句：27/72 在摘要里明确写出空白（"However, … has not been …"）。
- 锚点句："In this paper, …" 52/72；"This paper + 动词" 10/72；"We + 动词" 6/72；无锚点 4/72。
- 方法句占主体：71/72 有，通常 2–4 句，按"建模 → 难点 → 求解 → 扩展"排列。
- 理论句：33/72 有（"It is shown that …"、"… is derived in closed form"）。
- 结尾：结果句 69/72，意义句 3/72。结果句 1 句 45/72，2 句 18/72，3 句以上 9/72。
- 摘要里写具体数字：13/72（TWC 6/24，JSAC 4/24，TCOM 3/24）。写数字时要带比较对象和条件。

**模板 A：背景开头（44/72）**
1. 背景：技术或场景的重要性。
   "Low earth orbit (LEO) satellite communications are expected to be incorporated in future wireless networks, in particular 5G and beyond networks, …"（jsac.2020.3000803）
2. 空白（可选）。
   "Most prior work has focused on hybrid precoding for narrow-band mmWave systems, with perfect or estimated channel knowledge at the transmitter."（tcomm.2016.2549517）
3. 锚点：本文研究什么。
   "In this paper, we consider a RIS-aided multiuser multiple-input single-output (MISO) downlink communication system."（twc.2020.2970061）
4. 问题与难点。
   "These problems are highly non-convex and challenging to solve, due to the involvement of binary UAV-GBS association variables …"（tcomm.2025.3541027）
5–6. 方法。
   "To solve these non-convex problems, we propose efficient algorithms by using the techniques of alternating optimization, successive convex approximation, and semi-definite relaxation."（tcomm.2025.3541027）
7. 理论结果（可选）。
   "It is shown that the DL ASLNRs and UL ASINRs of all UTs reach their upper bounds under some channel condition."（jsac.2020.3000803）
8. 结果。
   "Numerical results demonstrate that the proposed massive MIMO transmission scheme with FFR significantly enhances the data rate of LEO satellite communication systems."（jsac.2020.3000803）

**模板 B：直接写本文（26/72）**：第 1 句就是 "In this paper, we propose/study …"，适合方法本身就是卖点的论文。
"In this paper, we propose a class of high-efficiency deep joint source-channel coding methods that can closely adapt to the source distribution under the nonlinear transform, …"（jsac.2022.3180802）

**写数字的结果句**：
"In particular, the proposed algorithm performs quite well when the channel uncertainty is smaller than 10%."（twc.2020.2970061）
"Furthermore, the proposed method yields up to 60% reductions of VUEs with large queue lengths, while reducing the average power consumption by two folds, …"（tcomm.2019.2956472）

## 4. 引言

**长度**：7 段 [6–8]。

**段落功能出现率**：contrib 67/72，gap 67/72，field 62/72，roadmap 62/72，prior 57/72，tech 43/72，aim 43/72，notation 43/72，solution 16/72，approach 11/72。

**默认顺序**（每段一个功能）：
1. **field**（首段，62/72）：领域需求或愿景，常带 5G/6G 或产业数据。
2. **tech**（43/72）：现有技术及其代价，或新技术的原理与优势。
3. **prior**（57/72）：已有工作逐条或分组罗列，每组后用 "However, …" 点评。
4. **gap**（67/72）：归纳已有工作的共同局限 → 收束到本文问题。复杂论文会有 2–3 个 gap 段，各管一个维度。
5. **aim**（43/72）："In this paper, we …" + 系统设定；可再加一段说明核心思路（solution 16/72，approach 11/72）。
6. **contrib**（67/72）：贡献列表。
7. **roadmap**（62/72）："The rest of this paper is organized as follows."，逐节一句。
8. **notation**（43/72 放在引言末）：记号说明段。

引言最后两段的组合：roadmap → notation 38/72；contrib → roadmap 20/72。

**相关工作**：
- 写在引言段落里 47/72，用引言内小节（"A. Related Works / B. Contributions / C. Organization"）16/72，单列一节 9/72（JSAC 8/24，TCOM 1/24）。
- 组织方式：按研究线分组（"On the one hand … On the other hand …"），每组后指出局限；不要逐篇平铺。

**贡献列表**：
- 格式：bullets 44/72，散文段 18/72，编号 10/72（JSAC 7/24）。
- 条数：4 条 30/72，3 条 28/72，5 条 13/72。
- 每条开头动词：propose 44/72 篇用过，formulate 24/72，derive 23/72，develop 17/72，show 16/72；首条最常以 propose（20/72）或 formulate（12/72）开头。
- 带性能数字：10/72。不带数字是常态；要写数字就在最后一条"仿真验证"里写。
- 首创声明可以写在引言正文，也可以写进某条贡献（共 33/72 篇有首创声明；列表项里的句子提取器统计不到，以人工编码为准）。
- 引导句："The main contributions of this paper are summarized as follows:"（类似句 57/72）。

**路线图**：
"The rest of the paper is organized as follows."（jsac.2020.3000803）
随后每节一句："In Section II, we investigate the channel model and the corresponding transmission signal model for LEO satellite communication systems."（jsac.2020.3000803）

**记号段**：放在引言末 43/72，用记号表 13/72（JSAC 8/24），没有 14/72，放在模型节开头 2/72。
"Notations: Lowercase and uppercase letters with boldface refer to vectors and matrices, respectively."（tcomm.2025.3541027）

## 5. 系统模型与问题形式化

- 节名通常是 "System Model" 或 "System Model and Problem Formulation"；问题较复杂时单列 "Problem Formulation"（如 tcomm.2016.2549517 单列 "Problem Statement"）。
- 顺序：场景与 Fig. 1 → 信道模型 → 信号模型 / 性能指标 → 约束 → 优化问题 (P1) → 难点声明 → 本文的求解路线预告。
- 假设要给理由或文献："Similar to many studies such as [18] and [36], we ignore the transmission delay …"（jsac.2018.2815360）
- 理想化假设要说明用途："To characterize the fundamental capacity limit, we assume that perfect CSI is available at both the transmitter and receiver."（twc.2023.3307696）
- 多种设定时（如 2×2 的天线放置 × 接收机类型）先详解一种，再用一节说明其余情形的差异（tcomm.2025.3541027）。

## 6. 方法与理论节
详见 `methodology.md`。结构上：每个子问题一个小节；算法用 Algorithm 框汇总（中位数 2 个）；
理论结果用 Proposition / Theorem / Lemma 环境（定理类陈述中位数 2.5 个，18/72 篇没有）并紧跟 Remark 或一句解读。

## 7. 仿真 / 数值结果节

- 节名："Simulation Results" / "Numerical Results"；学习类论文常用 "Experimental Results" 或 "Performance Evaluation"。
- 第一段：场景、参数（参数表 28/72，其余写在正文）、平均次数；接着用 bullet 或编号定义基准。
- 小节按贡献顺序组织（如 tcomm.2016.2549517：最优设计与码本 → 低复杂度算法 → RF 链增益）。
- 开头句："In this section, we validate our analytical results and evaluate the performance of the proposed codebooks and hybrid precoding designs using numerical simulations."（tcomm.2016.2549517）
- 分析型论文先验证解析结果："First, we compare our analytical results of the coverage probabilities with the simulation results."（twc.2016.2531652）

## 8. 结论

- 段数：1 段 56/72，2 段 16/72。
- 时态：现在完成时开头（"In this paper, we have investigated …"），之后可转一般过去时逐条复述。
  "In this paper, we have investigated massive MIMO transmission for LEO satellite communications exploiting sCSI with FFR."（jsac.2020.3000803）
- 内容：做了什么 → 关键发现或设计洞见 → 未来工作（36/72；TCOM 17/24，TWC 7/24）。
- 不放数字 66/72；重复摘要数字的只有 6/72。
- 未来工作写具体方向，不写空话："Future work includes detailed investigation on low complexity sCSI estimation, …"（jsac.2020.3000803）
- 也可以用展望句收尾："It is hoped that this paper will motivate a new approach for more efficiently deploying antennas in future wireless networks …"（twc.2024.3492195）

## 9. 附录

- 附录节数中位数 1 [0–1]。证明位置：附录 21/72，附录 + 正文 14/72，正文 16/72，无证明 20/72，引用技术报告 1/72。
- 附录标题直接写证明对象（"Appendix A Proof of Proposition 2"，jsac.2020.3000803；"Appendix A Proof of Proposition 1"，tcomm.2019.2956472）；正文的定理后只留一句指向附录的证明说明。
- 短证明（几行）放正文，长证明放附录；篇幅紧张时可写 "… can be readily proved based on the proof for Theorem 1. Thus this proof is omitted for the sake of saving space."（jsac.2018.2864426）

## 10. 综述 / 教程（n = 8，与研究论文分开统计）

- 标题：冒号副标题 6/8，副标题常为目录式三段（"How It Works, State of Research, and The Road Ahead"，jsac.2020.3007211；"Applications, State-of-the-Art, and the Road Ahead"，tcomm.2020.2973976）或文体名（"A Tutorial"，tcomm.2021.3051897）。
- 摘要：没有结果句（结果句只出现在混合型 tcomm.2020.2973976 中），全是"本文覆盖什么"的导览句；锚点为 "In this paper, we provide …" 或 "This survey provides …"。
- 引言：领域需求 / 历史叙事 → 正式定义 → 与已有综述的区别（相关综述对比表 3/8）→ 结构说明；可用问句小标题（"What is IRS?" / "What's New?"，tcomm.2021.3051897）。
- 正文：每个技术节以 "Summary and Open Challenges" 或 "Other Related Work and Future Direction" 小节收尾（jsac.2022.3156632、tcomm.2021.3051897、tcomm.2022.3171800）；可用一张图同时展示技术框架和论文结构（jsac.2022.3156632、tcomm.2022.3171800）。
- 结论：写未来方向 6/8；段数中位数 2.5（1–6 段）。
- 判别要点：研究名额里如果有一篇没有公式、没有定理、没有贡献列表，或摘要写 "This paper presents the most important technology concepts" 一类句子，它其实是综述（本语料中有 2 篇这样被改记为 overview）。
