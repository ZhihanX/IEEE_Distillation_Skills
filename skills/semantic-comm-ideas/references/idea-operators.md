# 增量算子：从基线到新 idea

统计口径：37 篇研究论文的 `semcom.idea_delta`（一篇可有多个）。"代表论文"给 DOI 后缀；引号内是原文单句（≤ 30 词）。
每篇论文的增量类型数：2 类 16/37，3 类 16/37，4 类 2/37，1 类 3/37（DeepJSCC tccn.2019.2919300、DeepSC-S jsac.2021.3087240、
DeepJSCC-Q jsait.2022.3231042——都是各自方向的第一篇）。**非开创型 idea 默认叠加 2–3 个算子。**

## 1. 算子一览

| 算子 | 频率 | 一句话 | 代表论文 |
|---|---|---|---|
| adaptivity | 13/37 | 一个模型适配多 SNR / 多速率 / 内容 / 调制 | twc.2021.3090048，twc.2023.3234408，jsac.2022.3180802，tccn.2024.3422496 |
| new-component | 9/37 | 新网络模块或新结构 | tccn.2024.3424842，jsac.2022.3180802，tccn.2022.3151935 |
| new-metric | 8/37 | 新的优化目标或评价指标 | tsp.2021.3071210，jsac.2023.3288243，jsac.2022.3191112，tcomm.2023.3274122 |
| new-modality | 8/37 | 换信源：文本、语音、视频、多模态 | tsp.2021.3071210，jsac.2021.3087240，jsac.2022.3191354，jsac.2022.3221977 |
| theory | 7/37 | 信息论 / 率失真 / 性能界 / IB | jsac.2021.3126087，jsac.2025.3531546，jsac.2022.3222000，tcomm.2023.3274122 |
| digitalization | 6/37 | 量化、星座、码本、接入标准数字链路 | jsait.2022.3231042，tcomm.2024.3386577，jsac.2025.3531546 |
| new-task | 5/37 | 从重建换成任务（识别、分类、检索） | twc.2023.3240969，twc.2023.3349330，jsac.2022.3221991 |
| multi-user | 5/37 | 多用户、多设备、多址 | jsac.2022.3191326，twc.2022.3191118，tccn.2023.3326302 |
| generative-prior | 5/37 | 生成模型作先验或解码器 | jsac.2023.3288243，twc.2024.3379244，jsac.2025.3559120 |
| new-channel | 4/37 | 新信道或新系统设定（多径 OFDM、MIMO、反馈、并行子信道） | jsait.2020.2987203，tccn.2022.3151935，twc.2024.3422794 |
| system-optimization | 4/37 | 把语义模型当黑盒做资源分配 | jsac.2022.3191112，jsac.2023.3240713，jsac.2025.3559120 |
| knowledge-base | 4/37 | 显式共享知识（知识图谱、说话人照片、LLM 生成的文本） | jsac.2022.3191112，jsac.2022.3221968，tccn.2024.3401712 |
| robustness | 4/37 | 语义噪声、数据漂移、信道 / 调制失配 | twc.2023.3265201，jsac.2022.3221991，jsac.2023.3288249 |
| new-paradigm | 3/37 | 首次把端到端学习用于该问题 | tccn.2019.2919300，tsp.2021.3071210，jsac.2021.3126087 |
| feedback-retransmission | 3/37 | 反馈、HARQ、选择性重传 | jsait.2020.2987203，jsac.2022.3221968，twc.2022.3191118 |
| security-privacy | 3/37 | 对抗攻击、模型反演、多址中的隐私 | jsac.2023.3288249，twc.2024.3369170，tccn.2023.3326302 |

## 2. 每个算子的写法、证据与陷阱

### adaptivity（13/37）
- **做法**：把 SNR / 速率 / CSI 作为网络输入（注意力调制、SNR 嵌入）；按熵模型或重要性截断潜特征；按 SNR 选调制阶数。
- **机理例句**："The common limitation of these techniques is the use of a fixed modulation scheme during the training of the JSCC encoder and decoder."（tccn.2024.3422496）
- **所需证据**：单模型 vs 每个 SNR / 速率单独训练的模型（上界）；SNR 失配曲线；平均速率 / 频谱效率节省。
- **陷阱**：只和"固定模型"比、不和"每点单训模型"比；自适应带来的额外信令开销不计入。

### new-component（9/37）
- **做法**：换骨干（CNN → Swin）、加熵模型 / 超先验、把 OFDM 等已知信号处理模块嵌入网络。
- **机理例句**："The global attention mechanism inside Transformer enables a closer connection among image patches, which further contributes to the stronger capability to combat channel noise and interference."（tccn.2024.3424842）
- **非平凡性要求**：SwinJSCC 预先回应了"只是换骨干"的质疑："Thus, a naive alternation of CNN as Swin Transformer in JSCC cannot yet achieve considerable performance gain."（tccn.2024.3424842）
- **陷阱**：没有同参数量 / 同 FLOPs 的消融，审稿人会把增益归因于模型变大。

### new-metric（8/37）
- **做法**：句子相似度（tsp.2021.3071210）、MSE + LPIPS（jsac.2023.3288243）、语义相似度 MSS（jsac.2022.3191112）、
  误导率（jsac.2023.3288249）、按任务选保真度准则（tcomm.2023.3274122）。
- **机理例句**："This work reveals the cardinal role of context-dependent fidelity criteria in goal-oriented semantic communication."（tcomm.2023.3274122）
- **所需证据**：新指标与人类判断或下游任务的一致性；在旧指标上不明显变差（或坦白变差并解释）。
- **陷阱**：用自己定义的指标同时训练和评测（循环论证）；新指标依赖某个预训练网络时的偏差。

### new-modality（8/37）
- **做法**：把已有范式换到新信源（文本 → 语音 → 视频 → 多模态），并找出新信源特有的结构（语音静音段、视频帧间相关、说话人头像关键点）。
- **机理例句**："Although semantic communications have been designed for intelligent speech transmission, investigation on semantic communications to execute speech-centric intelligent tasks at the receiver is still missing."（twc.2023.3240969）
- **所需证据**：新信源的标准数据集与标准指标（语音 PESQ / WER，视频 HEVC 测试序列 + BD-rate）；与该模态的标准编解码器（H.264 / H.265 / AV1）+ 信道编码比较。
- **陷阱**：只是把图像网络套到新信源上，没有利用新信源的结构——modality 线 6 篇都给出了模态特有的设计。

### theory（7/37）
- **做法**：IB / 变分界做损失（jsac.2021.3126087、tcomm.2024.3386577）；失真上界指导速率控制（jsac.2025.3531546）；
  拟合 DL 性能曲线后做速率区域分析（jsac.2022.3222000）；纯率失真刻画（tcomm.2023.3274122）。
- **桥接手法**：深度模型性能无闭式时，用数据回归拟合（广义 logistic、曲线拟合）接入解析分析——
  "However, a key challenge is that there is no closed-form expression for a key parameter, namely the semantic similarity, …"（jsac.2022.3222000）
- **陷阱**：拟合曲线换数据集 / 模型就要重测；理论只停在"作为损失函数"，没有给出可检验的结论。

### digitalization（6/37）
- **核心难点是不可微**："Specifically, the process of digital modulation requires a mapping from the continuous real-world source data to discrete constellation symbols, which is equivalent to a non-differentiable function [27]."（tcomm.2024.3386577）
- **已有解法**：软-硬量化（jsait.2022.3231042）；码本 / 只传索引（twc.2023.3265201、tcomm.2024.3364990）；
  学习到星座的转移概率（tcomm.2024.3386577）；比特级信道抽象 + 参数采样（tccn.2024.3422496）；
  不求梯度、用理论做源-信道速率控制（jsac.2025.3531546）。
- **动机写法**：落到具体标准——"For example, the IEEE 802.11ad physical layer (PHY) specification [15] states the use of BPSK, QPSK, 16-QAM and 64-QAM."（jsait.2022.3231042）
- **所需证据**：与无约束模拟版本的差距；多种调制阶数；与"学习型信源编码 + LDPC / 极化码"比较；有无悬崖效应。
- **陷阱**：最优表现依赖极高阶星座（如 4096-QAM）；没有真实信道码；误码对语义的影响不分析。

### new-task（5/37）
- **做法**：接收端只执行任务不重建（twc.2023.3240969）；同时服务重建与分类（twc.2023.3349330）；任务对发送端未知（jsac.2022.3221991）。
- **机理例句**："We would like to emphasize that semantic information is determined by specific tasks, instead of being an intrinsic feature of the source."（jsac.2022.3221991）
- **所需证据**：任务指标 vs 传输符号数的权衡曲线；与"先重建再做任务"的级联方案比较。

### multi-user（5/37）
- **做法**：多用户多模态统一框架（jsac.2022.3191326）；分布式 IB（twc.2022.3191118）；学习正交语义符号的同频多址（tccn.2023.3326302）；
  语义 / 比特用户共存的速率区域（jsac.2022.3222000）；RSMA 公共消息承载共享知识（jsac.2023.3240713）。
- **好问题的写法**——质疑经典结论是否仍成立："Nevertheless, an interesting question arises, when considering semantic communications, does this conclusion still hold or do we need to develop new tailored MA schemes?"（jsac.2022.3222000）
- **陷阱**：用户数、任务固定；多用户干扰只靠线性检测；不与 OFDMA / TDMA 在同样资源下比较。

### generative-prior（5/37）
- **做法**：GAN 反演或生成式解码器（jsac.2023.3288243）；扩散模型做信道去噪（twc.2024.3379244）；
  预训练基础模型作编解码器（jsac.2025.3559120）；LLM 生成辅助文本（tccn.2024.3401712）；GAN 语义解码（jsac.2022.3221999）。
- **机理例句**（跨领域类比）："Interestingly, by comparing (1) and (2), we can find that the designed process of DM and the wireless communications system are similar."（twc.2024.3379244）
- **所需证据**：感知指标（LPIPS / FID）+ 失真指标；极低带宽 / 低 SNR 的"边缘情形"；采样时延或 MACs。
- **陷阱**：生成"幻觉"违背语义保真却不被度量；只在窄分布（人脸）上验证；推理代价不计入。

### new-channel（4/37）
- **做法**：反馈信道（jsait.2020.2987203）、多径 OFDM（tccn.2022.3151935）、MIMO（twc.2024.3422794）、并行子信道 / 部分接收（twc.2021.3090048）。
- **非平凡性写法**："Directly replacing the simple channel model such as AWGN with the multipath fading channel in the prior JSCC works may lead to sub-optimal performance due to the inter-symbol interference."（tccn.2022.3151935）
- **所需证据**：与"分离式方案 + 对应的经典信道处理"（如 SVD 预编码 + 注水、LS / MMSE 估计）比较；信道估计误差下的表现。

### system-optimization（4/37）
- **做法**：以语义指标为目标做 RB / 功率 / 速率 / 波束成形分配（jsac.2022.3191112、jsac.2023.3240713、jsac.2025.3559120、jsac.2022.3222000）。
- **动机例句**："Since semantic features exhibit varying levels of importance, conventional resource allocation strategies may be inefficient."（jsac.2025.3559120）
- **陷阱**：没有在噪声信道上端到端验证语义性能——networking 线 3/3 篇都如此：语义层要么是拟合曲线 / 抽象函数（jsac.2022.3222000、jsac.2023.3240713），要么假设语义传输本身无误码、信道只影响速率与时延（jsac.2022.3191112）。

### knowledge-base（4/37）
- **做法**：显式共享知识减少传输——知识图谱三元组（jsac.2022.3191112）、预共享说话人照片只传关键点（jsac.2022.3221968）、
  LLM 生成描述文本（tccn.2024.3401712）、接收端主导训练不暴露任务（jsac.2022.3221991）。
- **机理例句**："Transmission errors in SVC only lead to a changed expression, whereas those in the conventional methods directly destroy pixels."（jsac.2022.3221968）
- **陷阱**：知识库的建立、更新、失配开销不计入；收发知识不一致时的退化不测。

### robustness（4/37）
- **做法**：码本吸收语义噪声（twc.2023.3265201）、域适应应对数据漂移（jsac.2022.3221991）、BSEC 参数采样覆盖调制 / 信道失配（tccn.2024.3422496）、对抗训练（jsac.2023.3288249）。
- **机理例句**："The discrete feature representation can combat semantic noise."（twc.2023.3265201）

### new-paradigm（3/37）
- 三篇都是开创型：DeepJSCC（图像端到端 JSCC）、DeepSC（文本语义）、VIB 任务导向（边缘推理）。
- **写法**："Inspired by research results in both areas, we aim to provide a new view on communication systems from the semantic level."（tsp.2021.3071210）
- 新范式 idea 现在很难再有；同类声明需要非常具体的设定限定。

### feedback-retransmission（3/37）
- **做法**：反馈信道分层传输（jsait.2020.2987203）、语义错误检测器驱动 HARQ（jsac.2022.3221968）、置信度驱动的选择性重传（twc.2022.3191118）。
- **关键洞见**：语义错误的形态不同于比特错误，CRC 不再合适——"However, the conventional error detector, such as cyclic redundancy check, cannot reflect the degree of expression changes."（jsac.2022.3221968）

### security-privacy（3/37）
- **做法**：语义导向的物理层对抗攻击与防御（jsac.2023.3288249）；对抗学习防模型反演（twc.2024.3369170）；正交语义符号的隐私（tccn.2023.3326302）。
- **威胁模型要说清**："As the bits/symbols are treated equally on these systems, such content-oriented attacks are not applicable to semantic communications."（jsac.2023.3288249）
- **陷阱**：白盒假设偏强；防御只对训练时的代理攻击者有效；隐私用 SSIM / PSNR 衡量而非形式化定义。

## 3. idea 的来源手法（从卡片第 4 节归纳）

| 手法 | 例子 | 怎样写成非平凡 |
|---|---|---|
| 从 CV / ML 迁移工具 | MAE + VQ-VAE（twc.2023.3265201），StyleGAN 反演（jsac.2023.3288243），MCR²（twc.2023.3349330），扩散模型（twc.2024.3379244），Swin（tccn.2024.3424842），超先验熵模型（jsac.2022.3180802） | 说清"信道"带来的新问题：噪声、带宽约束、SNR 变化；给出原工具不能直接用的理由 |
| 把经典通信机制装进语义系统 | HARQ（jsac.2022.3221968），AMC / 自适应调制（tccn.2024.3422496），OFDM（tccn.2022.3151935），MIMO（twc.2024.3422794），NOMA / RSMA（jsac.2022.3222000、jsac.2023.3240713），多址（tccn.2023.3326302） | 指出语义系统里该机制的前提失效（如 CRC 不反映语义错误；NOMA 优于 OMA 的结论不再成立） |
| 放松一个隐含假设 | 任意复值信道输入 → 标准星座（jsait.2022.3231042）；发送端知道任务 → 不知道（jsac.2022.3221991）；固定调制 → 多阶调制（tccn.2024.3422496） | 用一句"implicit assumption"点出整批文献共享的假设 |
| 结构同构 | 扩散前向过程 ≈ 加噪信道（twc.2024.3379244）；共同知识 ≈ RSMA 公共消息（jsac.2023.3240713） | 用公式或系统图并排展示同构，再说明不完全同构之处如何处理 |
| 理论桥接 | 拟合语义相似度曲线后做速率区域（jsac.2022.3222000）；失真上界指导速率控制（jsac.2025.3531546） | 给出由理论得到、可被实验检验的结论（单调性、增长阶、最优结构） |
| 换信源 / 换任务 | 文本 → 语音 → 视频（tsp.2021.3071210 → jsac.2021.3087240 → jsac.2022.3191354） | 找到新信源特有的结构并据此设计模块 |

## 4. 非平凡性自检（生成 idea 时每个候选都要过）
1. 直接把 A 和 B 拼起来会出什么问题？（不可微、维度不匹配、信道不同、训练不稳定、代价不可接受）
2. 本文用什么洞见解决这个问题？能否用一句话说清"为什么有效"？
3. 这个洞见能否用一个机理实验（可视化、消融、玩具例子）单独验证？——卡片里的高引论文几乎都有一张"机理图"
   （如 NTSCC 的速率分配可视化、JCM 的星座使用概率、DeepMA 的相关矩阵、视频会议的"表情改变 vs 像素毁坏"对比）。
