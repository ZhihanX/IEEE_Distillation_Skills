# 检查 idea：问题清单与审稿风险

统计口径：37 篇研究论文。"k/37" 来自卡片 YAML；"≥k/37" 来自卡片第 10 节"弱点"行的关键词计数（下限）。

## 1. 新颖性
- [ ] 能否用"基线（DOI）+ 增量算子"一句话说清？说不清通常意味着增量不明确。
- [ ] 在 `landscape.md` 对应主题下找到最接近的 1–3 篇，并写出差异（设定、方法、指标中至少一项）。
- [ ] 实时检索：arXiv / IEEE Xplore / Google Scholar，关键词组合 = 信源 + 范式 + 增量 + 信道，限定最近两年；
  语料只到 2025 年、只覆盖 6 本期刊且引用 ≥ 10，最新工作多在 arXiv 和会议（ICC、Globecom、WCNC）上。
- [ ] 若父论文的兄弟节点已经加过同一增量（`design-space.md` 第 3 节），新颖性只能来自新设定或新机理。
- [ ] 首创声明：20/37 篇有，且都带具体限定。例："This paper presents the first DeepJSCC scheme over the MIMO system for image transmission."（twc.2024.3422794）
  没把握时用弱化说法，例："Specifically, this paper takes the lead to investigate a new architecture named SwinJSCC to address the limitations of CNN-based JSCC methods …"（tccn.2024.3424842）

## 2. 重要性
- [ ] 空白属于哪类？语料：limitation 17/37，new-scenario 15/37，practicality 12/37，theory-gap 4/37，unification 3/37，tool-transfer 3/37。
- [ ] 是否回应了 `open-problems.md` 中某条 [原文] 问题？引言里可以直接引用该文献的未来工作句来立论。
- [ ] 实用性空白要落到可核查的事实上（标准、硬件、协议），例："Therefore, in practice, DeepJSCC can be difficult to implement without custom hardware."（jsait.2022.3231042）
- [ ] 是否只是"把 A 用到 B"？若是，要能说出 B 的特殊结构带来的新问题（见 `idea-operators.md` 第 4 节）。

## 3. 合理性
- [ ] 机理假设可检验：计划了哪张图 / 哪个消融来证明"为什么有效"？
- [ ] 不可微环节（量化、调制、信道码、检测、生成采样）如何训练？是否有已知解法可用（`idea-operators.md` digitalization 一节）？
- [ ] 训练与测试是否一致：SNR、调制阶数、数据分布、CSI 质量。
- [ ] 理论是否依赖强假设（高斯特征、比特独立、Lipschitz 常数、拟合曲线）？弱点里"假设偏强或未验证"≥8/37。
- [ ] 安全 / 隐私类：威胁模型（白盒 / 黑盒、攻击者知道什么）写清楚了吗？

## 4. 评测完整性
按 `evaluation.md` 第 1 节逐项打勾。语料中最常见的缺项（审稿时最容易被指出）：

| 风险 | 语料频率 | 预先回应 |
|---|---|---|
| 没有复杂度 / 时延分析 | 未报告 18/37；弱点提及 ≥15/37 | 参数量、FLOPs / MACs、编解码时间对比表 |
| 小图 / 数据集少 | 弱点提及 ≥13/37 | 补 Kodak / CLIC / DIV2K 或该模态的标准高分辨率集 |
| 只有 AWGN / 信道受限 | 只有 AWGN 9/37；弱点提及 ≥12/37 | 补 Rayleigh / 多径 / MIMO，至少一组信道估计误差 |
| 没有 SNR 失配实验 | 18/37 没做 | 单 SNR 训练、全 SNR 测试 + "每点单训"包络 |
| 只能模拟传输 | 数字兼容只有 14/37；弱点提及 ≥6/37 | 讨论或实验验证数字化路径（量化 + 标准调制） |
| 没有硬件 / 空口验证 | 0/37 | 有条件做 SDR；没有就在结论里列为未来工作 |
| 假设偏强或未验证 | 弱点提及 ≥8/37 | 数值验证假设（如 Monte Carlo、分布拟合） |
| 基准弱 / 不全 | 弱点提及 ≥2/37；基准数中位数 3 | 分离式（实际码 + 容量界）+ 最强学习方法 + 消融 |

## 5. 写作与定位（交给 `ieee-journal-writing`）
- 语义通信子语料的写作习惯（与主语料 72 篇大体一致）：贡献用 bullet 31/37；摘要写数字只有 6/37；
  Fig. 1 是框架图 23/37、系统模型图 9/37；相关工作写在引言里 17/37（含引言小节共 26/37）；有路线图 26/37；
  结论写未来工作 17/37。
- 坦白劣势是常见且被接受的写法（例如在 PSNR 上不如为 PSNR 优化的基准），关键是给出原因：
  "Although, H.265 performs better than DeepWiVe in terms of the PSNR metric, DeepWiVe outperforms H.265 when compared in terms of MS-SSIM, …"（jsac.2022.3191354）
- 空白句要指向具体文献的具体假设，例："However, an implicit assumption in all of the works above is the ability for the communication hardware to transmit arbitrary complex valued channel inputs."（jsait.2022.3231042）

## 6. 输出格式
检查结果用 SKILL.md 中的"检查结果模板"。每个"低"分维度都给出一条具体、可执行的修改建议
（补哪个实验、换哪个基准、加哪个限定、改哪句空白句），并标明依据来自哪条统计或哪篇卡片。
