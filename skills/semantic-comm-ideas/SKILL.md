---
name: semantic-comm-ideas
description: Generate and check research ideas in semantic communications and deep joint source-channel coding (DeepJSCC / JSCC) — image / video / speech / text semantic transmission, task-oriented and goal-oriented communication, edge inference, digital semantic communication (quantization, constellations, codebooks), generative semantic communication (diffusion, GAN, LLM, foundation models), multi-user and networked semantic systems, theory, security and privacy. Use to brainstorm candidate ideas from the design space and open problems, to position an idea against IEEE TWC/JSAC/TCOM/TCCN/TSP/JSAIT work, to check novelty, significance, soundness and evaluation completeness, and to anticipate reviewer objections. 适用于：语义通信 / JSCC 选题、idea 生成、idea 查新与评估、实验设计检查、审稿风险预判。
---

# 语义通信 / JSCC：生成 idea 与检查 idea

依据：39 篇逐篇蒸馏卡片（37 篇研究论文 + 2 篇综述，2019–2025，TWC / JSAC / TCOM / TCCN / TSP / JSAIT）。
它们是从 234 篇候选（Crossref 引用 ≥ 10、标题匹配语义通信 / JSCC / 任务导向）中，按 7 条研究线
（image-jscc、digital、generative、modality、task-multiuser、networking、theory-security）各取年均引用最高的论文选出的。

- "k/37" = 37 篇研究论文中有 k 篇（来自卡片 YAML 的编码字段，见 `corpus/semcom/summary.md`）。
- "≥k/37" = 卡片第 10 节文字的关键词计数，是下限。
- 英文例句是原文单句短引（≤ 30 词），后附 DOI 后缀（省略 `10.1109/`），能在对应卡片里找到原句。
- 标"推断"的开放问题是蒸馏时从论文弱点推出来的，作者没写，使用前要查新。
- 选题地图只覆盖 234 篇候选的标题；任何"没人做过"的判断都必须再做实时检索。

## 两种模式

用户给出方向、背景或约束（"想做 JSCC + 某某"）时走**生成**；给出具体 idea 或论文草稿时走**检查**。
两种模式最后都输出表格 + 下一步建议；需要写成论文时交给 `ieee-journal-writing` skill。

## 生成 idea（G1–G6）

1. **G1 定位**：把用户的方向映射到设计空间的各轴——信源、任务、范式、架构、信道、自适应、训练方式、指标、基准
   （`references/design-space.md` 第 1 节）。先问清三件事：要不要兼容数字链路、有没有复杂度 / 时延约束、
   能不能做硬件实验。缺信息时按最常见的设定假设：图像（27/37）、重建任务（31/37）、AWGN + Rayleigh（AWGN 27/37，Rayleigh 23/37）。
2. **G2 找基线**：在继承关系图里找最近的"父论文"（`design-space.md` 第 3 节）。语料内最常被当作基线的是
   DeepJSCC（tccn.2019.2919300，12 次）、DeepSC（tsp.2021.3071210，4 次）、NTSCC（jsac.2022.3180802，3 次）、
   IB 任务导向（jsac.2021.3126087，3 次）。
3. **G3 选增量**：从 `references/idea-operators.md` 选 2–3 个增量算子叠加。37 篇中增量类型数为 2 的 16/37、3 的 16/37，
   只有 1 个的 3/37（且都是开创型论文）。最常见的算子：adaptivity 13/37、new-component 9/37、new-metric 8/37、new-modality 8/37。
4. **G4 找空位**：三个来源交叉——
   (a) `references/open-problems.md` 里作者自述的未来工作和推断问题；
   (b) `references/landscape.md` 占位表里的空格与少格（例如标题提到 OFDM 的只有 2/234、MIMO 7/234）；
   (c) 评测上的系统性空白：硬件 / 空口验证 0/37、开源代码 1/37、可直接接入数字链路 14/37。
5. **G5 写候选**：给出 3–5 个候选，每个都填下面的"候选 idea 模板"。每个候选必须说清"为什么不是平凡的拼接"
   ——即直接组合会遇到什么困难、本文的机理洞见是什么（见 `idea-operators.md` 第 3 节"非平凡性"）。
6. **G6 初筛排序**：对每个候选快速走一遍检查工作流的 C2–C5，按"新颖性 / 重要性 / 可行性 / 评测成本"打分（高 / 中 / 低），
   给出推荐顺序，并为第一名列出最小可行实验。

### 候选 idea 模板
| 项 | 内容 |
|---|---|
| 暂定标题 | 按 `ieee-journal-writing` 的标题模式（"[方法名]: … for …" 或 "X for Y"） |
| 一句话定位 | 已有工作做到哪里 + 还缺什么 + 本文做什么 |
| 基线（父论文） | 1–2 篇，写 DOI 后缀 |
| 增量算子 | 2–3 个，取自 `idea-operators.md` |
| 机理假设 | 为什么会有效（一句话，可检验） |
| 非平凡性 | 直接组合会遇到什么问题、本文如何解决 |
| 最小实验 | 数据集、信道、指标、基准、横轴（按 `evaluation.md`） |
| 主要风险 | 取自 `review-checklist.md` 的风险项 |
| 最接近的已有工作 | 选题地图 + 实时检索各列 1–3 篇 |

## 检查 idea（C1–C6）

1. **C1 拆解**：按卡片第 10 节的格式写出 基线 / 增量 / 为什么有效 / 证据（计划中的）/ 弱点。说不清基线或增量的 idea 先退回 G2–G3。
2. **C2 新颖性**：
   - 在 `references/landscape.md` 和完整版 `corpus/semcom/landscape.md` 里按关键词找最接近的标题；
   - 再做实时检索（arXiv、IEEE Xplore、Google Scholar，关键词 = 信源 + 范式 + 增量 + 信道，加 2024–2025 年限）；
   - 判定为：已有（同设定同方法）/ 部分已有（同方法不同设定，或同设定不同方法）/ 组合新 / 新，并写明依据。
   - 首创声明在 20/37 篇中出现，都带具体限定（设定、架构或信道）；判定为"部分已有"时只能用弱化说法。
3. **C3 重要性**：对照空白类型（limitation 17/37、new-scenario 15/37、practicality 12/37、theory-gap 4/37），
   检查 idea 是否回应了 `open-problems.md` 里的某条作者原文问题；能回应原文问题的 idea 更容易在引言里立住。
4. **C4 合理性**：机理是否成立；有没有踩 `references/evaluation.md` 第 3 节的公平性陷阱（带宽 / 信道使用数不一致、
   拿容量界当实际方案、每个 SNR 重训的基准与单模型比较、完美 CSI 假设未声明等）。
5. **C5 评测完整性**：按 `references/evaluation.md` 的清单逐项打勾，标出缺项与补法。
6. **C6 审稿风险**：按 `references/review-checklist.md` 列出最可能的 3–5 条审稿意见及预先回应；
   最后用 `ieee-journal-writing` 的 `references/idea-framing.md` 检查空白句和首创声明的写法。

### 检查结果模板
| 维度 | 结论（高 / 中 / 低） | 依据 | 建议 |
|---|---|---|---|
| 新颖性 | | 最接近的 1–3 篇及差异 | |
| 重要性 | | 回应了哪条开放问题 / 哪类空白 | |
| 合理性 | | 机理与潜在漏洞 | |
| 评测完整性 | | 缺项（对照清单） | |
| 审稿风险 | | 最可能的意见 | 预先回应 |

## 关键数字速查（37 篇研究论文）
| 项 | 数字 |
|---|---|
| 信源 | image 27/37，text 7/37，video 3/37，speech 3/37 |
| 范式 | analog-jscc 17/37，task-feature 7/37，digital-jscc 4/37，separate-learned 3/37，knowledge-based 3/37 |
| 信道 | AWGN 27/37，Rayleigh 23/37，MIMO 4/37，OFDM 4/37，Rician 4/37；只有 AWGN 9/37 |
| 数据集 | CIFAR-10 21/37，Kodak 12/37，ImageNet 12/37，MNIST 7/37 |
| 指标 | PSNR 23/37，MS-SSIM 12/37，accuracy 12/37，LPIPS 4/37 |
| 基准 | 分离式方案 30/37，DeepJSCC 13/37，其他学习方法 17/37，消融 8/37；基准数中位数 3 |
| 鲁棒性与代价 | SNR 失配实验 19/37，复杂度报告 19/37，数字兼容 14/37，硬件验证 0/37，开源代码 1/37 |
| 理论 | 无理论 21/37，辅助理论 12/37，以理论为主 4/37 |
| 横轴 | SNR 28/37，带宽比 / CBR / 压缩比 14/37 |

## 参考文件
- `references/design-space.md`：设计空间各轴的取值与频率、7 条研究线画像、继承关系图。
- `references/idea-operators.md`：16 种增量算子（定义、频率、代表论文、机理、所需证据、陷阱）与 idea 来源手法。
- `references/open-problems.md`：作者原文的未来工作与推断问题，按主题归类。
- `references/evaluation.md`：数据集、指标、基准、信道、鲁棒性与复杂度的评测清单，公平性规则。
- `references/review-checklist.md`：新颖性 / 重要性 / 合理性 / 评测的检查问题与常见审稿风险。
- `references/landscape.md`：234 篇候选论文的标题标签、模态 × 主题占位表、主题年份趋势、各主题高引标题。
