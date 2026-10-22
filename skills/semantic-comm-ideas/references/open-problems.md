# 开放问题清单（按主题）

由 `pipeline/aggregate_semcom.py` 从 39 张卡片第 10 节自动汇总（完整版见 `corpus/semcom/summary.md` 第 6 节）。
- **[原文]**：作者在结论或正文里写的局限 / 未来工作（原句，≤ 30 词，后附 DOI 后缀）。
- **[推断]**：蒸馏时从论文弱点推出、作者没写的问题，是假设，使用前必须查新。
  写着"后续 xxx"的推断项表示语料里已有论文部分回应了它，不再是空白，除非换设定。
- 一条可属多个主题；主题按条目数排序。括号内：条目数，涉及论文数。

使用方法：生成 idea 时，先在与用户方向相关的主题下挑 2–3 条，再用 `landscape.md` 和实时检索确认没人做过；
检查 idea 时，看它是否回应了某条 [原文] 问题——能回应原文问题的 idea 在引言里更容易立住。

## new modality / task / dataset（45 条，27 篇）

- [原文] "Future research avenues could explore the further optimization of the encoder-decoder framework and expand the model's application to other modalities."（tccn.2024.3401712）
- [原文] 结论 bullet："Extension to more complex downstream tasks: … How to extend the proposed designs to more complex downstream tasks is an interesting …"（twc.2023.3349330）
- [原文] 结论 bullet："Extension to more complex datasets: Extending our proposed framework on more complex datasets such as ImageNet is also worth pursuing in future work."（twc.2023.3349330）
- [原文] "One possible direction of future works is to generalize this work to other types of sources such as audio and video."（tccn.2022.3151935）
- [原文] "… the general design principles presented in this work can be potentially applied to other information sources, such as audio or video."（jsait.2020.2987203）
- [推断] 视频 / 多模态的感知-误差刻画（jsac.2025.3559120）
- [推断] 高分辨率图像与重建任务（tccn.2024.3422496）
- [推断] 衰落信道与数字传输下的多模态融合（tccn.2024.3401712）
- [推断] 高分辨率图像（tcomm.2024.3386577）
- [推断] 多用户、多接收端各自执行不同任务（广播多任务）（twc.2023.3349330）
- [推断] 任务之间的理论权衡刻画（twc.2023.3349330）
- [推断] 对任务型语义特征的去噪（twc.2024.3379244）
- [推断] 新任务的增量 / 持续学习（不遗忘）（tcomm.2024.3364990）
- [推断] 多用户场景下的统一多任务系统（tcomm.2024.3364990）
- [推断] 语义 HARQ 的通用化（其他模态的语义错误检测器）（jsac.2022.3221968）
- [推断] 数字化视频语义传输（码本 / 量化 + 数字调制）（jsac.2022.3221977）
- [推断] MIMO / OFDM 下的视频 deep JSCC（jsac.2022.3221977）
- [推断] 多用户视频流的带宽共享（jsac.2022.3221977）
- [推断] 生成式先验提升低码率视频感知质量（如视频会议，jsac.2022.3221968）（jsac.2022.3221977）
- [推断] 多接收端多任务下的接收端主导训练（jsac.2022.3221991）
- [推断] 图像 / 视频的语义速率曲线建模（jsac.2022.3222000）
- [推断] 多任务（多个语义失真）的率失真区域（tcomm.2023.3274122）
- [推断] 在噪声 / 衰落多址信道上的分布式任务导向 JSCC（如空中计算 AirComp 融合特征）（twc.2022.3191118）
- [推断] 把"质量预测 + 资源分配"推广到多用户 / 多任务的无线资源分配（后续大量 system-level 论文的基础）（twc.2023.3234408）
- [推断] 多说话人 / 多语言（twc.2023.3240969）
- [推断] 韵律、情感等副语言语义的传输（twc.2023.3240969）
- [推断] 与大语音模型（Whisper 类）结合（twc.2023.3240969）
- [推断] 多用户语音语义通信的资源分配（twc.2023.3240969）
- [推断] 文本、语音等其他模态的语义噪声（twc.2023.3265201）
- [推断] 语义概念的不等错误保护（jsac.2022.3221999）
- [推断] 通用场景（非街景）上的语义概念定义（jsac.2022.3221999）
- [推断] 检测、分割等复杂任务（jsac.2021.3126087）
- [推断] 多模态知识图谱（jsac.2022.3191112）
- [推断] 数字化视频 JSCC（jsac.2022.3191354）
- [推断] 多用户 / 广播视频（jsac.2022.3191354）
- [推断] 任务导向视频（检测、跟踪）（jsac.2022.3191354）
- [推断] 视频扩展（后续 jsac.2022.3221977）（jsac.2022.3180802）
- [推断] 用户 / 任务动态变化（jsac.2022.3191326）
- [推断] 统一多任务模型（后续 tcomm.2024.3364990）（jsac.2022.3191326）
- [推断] 语音 / 图像 / 多模态（jsac.2021.3087240、twc.2023.3240969）（tsp.2021.3071210）
- [推断] 面向识别 / 合成任务的语音语义通信（后续 twc.2023.3240969）（jsac.2021.3087240）
- [推断] 多说话人与噪声环境（jsac.2021.3087240）
- [推断] 数字化与低码率语音语义编码（jsac.2021.3087240）
- [推断] 与语音大模型结合（jsac.2021.3087240）
- [推断] 视频等其他信源（后续 DeepWiVe）（tccn.2019.2919300）

## digital compatibility / modulation / channel coding（44 条，28 篇）

- [原文] "An important direction of future research is to further optimize the performance of the proposed approach through the development of advanced designs for modulation schemes, quantization methods, and loss functions."（tccn.2024.3422496）
- [原文] "Another promising research direction is to extend the proposed JSCC approach to accommodate soft-output demodulation for JSCC-based semantic communications."（tccn.2024.3422496）
- [原文] "Looking ahead, our future efforts will focus on the design and optimization of constellation geometry shaping to enhance the system's performance."（tcomm.2024.3386577）
- [推断] 与 HARQ / 自适应调制编码（AMC）结合（jsac.2025.3531546）
- [推断] 高阶调制下的速率控制（jsac.2025.3531546）
- [推断] 与信道编码 / HARQ 的结合（tccn.2024.3422496）
- [推断] 符号内比特相关性的建模（非独立 BSEC）（tccn.2024.3422496）
- [推断] 数字化（量化 + 星座）下的 Swin 骨干（后续 D²-JSCC 等）（tccn.2024.3424842）
- [推断] 轻量化部署（tccn.2024.3424842）
- [推断] 隐私性的信息论量化（tccn.2023.3326302）
- [推断] 文本 / 视觉两路的带宽分配与不等错误保护（tccn.2024.3401712）
- [推断] 衰落信道与数字传输下的多模态融合（tccn.2024.3401712）
- [推断] 与信道编码（纠错码）的联合（tcomm.2024.3386577）
- [推断] 调制阶数随信道自适应（后续 tccn.2024.3422496 的方向）（tcomm.2024.3386577）
- [推断] 与数字调制兼容（twc.2023.3349330）
- [推断] 数字调制下的扩散去噪（twc.2024.3379244）
- [推断] 与数字调制兼容的 MIMO JSCC（twc.2024.3422794）
- [推断] 码本大小与调制阶数的联合自适应（tcomm.2024.3364990）
- [推断] 语义 HARQ 的通用化（其他模态的语义错误检测器）（jsac.2022.3221968）
- [推断] 数字化视频语义传输（码本 / 量化 + 数字调制）（jsac.2022.3221977）
- [推断] 与 HARQ / 反馈结合缓解 GOP 内误差传播（jsac.2022.3221977）
- [推断] 实时性（模型加速、轻量化）（jsac.2022.3221977）
- [推断] 衰落信道与数字调制下的生成式 JSCC（jsac.2023.3288243）
- [推断] 生成式与数字语义系统的对抗鲁棒性（jsac.2023.3288249）
- [推断] 数字化（码本 / 量化）（twc.2023.3240969）
- [推断] 码本索引的信道编码与不等错误保护（twc.2023.3265201）
- [推断] 码本大小、调制阶数与信道质量的联合自适应（后续数字 JSCC 系列）（twc.2023.3265201）
- [推断] 语义—感知准则下的联合信源信道编码（端到端过信道训练）（jsac.2022.3221999）
- [推断] 语义概念的不等错误保护（jsac.2022.3221999）
- [推断] 数字化 IB 特征（离散码本）（jsac.2021.3126087）
- [推断] 传输错误对三元组 / 知识图谱的影响与纠错（jsac.2022.3191112）
- [推断] 数字化视频 JSCC（jsac.2022.3191354）
- [推断] 低阶星座下的性能提升（后续 tcomm.2024.3386577 用概率建模）（jsait.2022.3231042）
- [推断] 调制阶数随 SNR 自适应（后续 tccn.2024.3422496）（jsait.2022.3231042）
- [推断] 与信道编码 / 比特接口的结合（D²-JSCC 等）（jsait.2022.3231042）
- [推断] 衰落与 MIMO 下的星座约束 JSCC（jsait.2022.3231042）
- [推断] 数字化 NTSCC（熵模型 + 真实信道码的速率控制，后续 jsac.2025.3531546）（jsac.2022.3180802）
- [推断] 数字化与隐私（多用户特征泄露）（jsac.2022.3191326）
- [推断] 数字化与量化（后续 digital 系列）（tsp.2021.3071210）
- [推断] 物联网轻量化（L-DeepSC）（tsp.2021.3071210）
- [推断] 分层传输与 HARQ / 反馈结合（twc.2021.3090048）
- [推断] 数字化与低码率语音语义编码（jsac.2021.3087240）
- [推断] 反馈与 ARQ/HARQ 的结合（后续出现 HARQ 类语义传输）（jsait.2020.2987203）
- [推断] 数字化与星座约束（后续 DeepJSCC-Q、D²-JSCC）（tccn.2019.2919300）

## multi-user / multiple access / networking（29 条，22 篇）

- [原文] 结论 bullet："Multi-user case: Future research could explore the extension of the D2-JSCC framework to a multi-user scenario, but the adaptive design of source-channel coders may pose challenges due to …"（jsac.2025.3531546）
- [原文] "Investigating an extension of the proposed approach to support multi-task multi-user semantic communications, where multiple devices engage in different tasks concurrently, would also be an important direction for future research."（tccn.2024.3422496）
- [原文] 结论 bullet："Heterogeneous transmission design with multiple S- and B-users: This paper considered a fundamental model with one S-user and one B-user."（jsac.2022.3222000）
- [原文] 结论 bullet："Opportunistic semantic and bit transmission design: This paper assumed that each user can only use one specific transmission method, i.e., semantic or bit-based transmission."（jsac.2022.3222000）
- [原文] "There are many interesting future research directions on this exciting topic, e.g., to apply the IB-based framework to the scenario with multiple devices, to develop a theoretical understanding …"（jsac.2021.3126087）
- [推断] 多用户下的语义感知资源分配（jsac.2025.3559120）
- [推断] 非正交语义多址（语义 NOMA，见 jsac.2022.3222000）（tccn.2023.3326302）
- [推断] 与经典多址在相同资源下的公平比较（tccn.2023.3326302）
- [推断] 多用户、多接收端各自执行不同任务（广播多任务）（twc.2023.3349330）
- [推断] 多用户、联邦训练中的隐私（twc.2024.3369170）
- [推断] 多用户 MIMO 下的语义传输与干扰管理（twc.2024.3422794）
- [推断] 多用户场景下的统一多任务系统（tcomm.2024.3364990）
- [推断] 多方会议的多用户资源分配（jsac.2022.3221968）
- [推断] 多用户视频流的带宽共享（jsac.2022.3221977）
- [推断] 多天线 / RSMA 下的语义-比特共存（jsac.2022.3222000）
- [推断] RIS / ISAC 等其他技术与语义通信的结构性结合（jsac.2023.3240713）
- [推断] 多用户场景下的语义干扰攻击（jsac.2023.3288249）
- [推断] 在噪声 / 衰落多址信道上的分布式任务导向 JSCC（如空中计算 AirComp 融合特征）（twc.2022.3191118）
- [推断] 设备间异构算力与带宽的联合调度（twc.2022.3191118）
- [推断] 真实多传感器（多摄像头、雷达 + 视觉）数据（twc.2022.3191118）
- [推断] 把"质量预测 + 资源分配"推广到多用户 / 多任务的无线资源分配（后续大量 system-level 论文的基础）（twc.2023.3234408）
- [推断] 多用户语音语义通信的资源分配（twc.2023.3240969）
- [推断] 多设备协同推理（后续 twc.2022.3191118）（jsac.2021.3126087）
- [推断] 多用户 / 广播视频（jsac.2022.3191354）
- [推断] 语义感知的多址与资源分配（见 tccn.2023.3326302、jsac.2022.3222000）（jsac.2022.3191326）
- [推断] 数字化与隐私（多用户特征泄露）（jsac.2022.3191326）
- [推断] 多用户（jsac.2022.3191326）（tsp.2021.3071210）
- [推断] 多用户广播中不同用户收到不同层数（twc.2021.3090048）
- [推断] 多用户下的反馈利用（jsait.2020.2987203）

## theory / limits / metrics（25 条，16 篇）

- [原文] 结论 bullet："E2E metric design: This paper described the E2E performance using the classical MSE metric, which might not be optimal for certain task-oriented applications."（jsac.2025.3531546）
- [原文] "Despite these advances, a universal semantic information theory for SemCom system design remains an open challenge."（jsac.2025.3559120）
- [原文] 结论 bullet："Performance limit characterization of the heterogeneous transmission with multimodal data: The semantic rate considered in this paper is used for characterizing the performance of text semantic communications."（jsac.2022.3222000）
- [原文] "This is probably because the semantics involved in CIFAR are much more complex than the ones in MNIST, and further understanding such a phenomenon would be an interesting …"（jsac.2023.3288249）
- [原文] "Second, we seek to generalize our goal-oriented communication setup beyond separable distortion criteria, since in real world applications one is more interested in relations between the input and …"（tcomm.2023.3274122）
- [原文] "There are many interesting future research directions on this exciting topic, e.g., to apply the IB-based framework to the scenario with multiple devices, to develop a theoretical understanding …"（jsac.2021.3126087）
- [原文] "While the optimal rate-distortion region for the multiple description problem remains open for general source distributions, optimal characterization is known for Gaussian sources [9]."（理论上仍开放）（twc.2021.3090048）
- [推断] 感知指标下的失真刻画（jsac.2025.3531546）
- [推断] 感知-误差函数的解析模型（替代曲线拟合）（jsac.2025.3559120）
- [推断] 隐私性的信息论量化（tccn.2023.3326302）
- [推断] 任务之间的理论权衡刻画（twc.2023.3349330）
- [推断] 可证明的隐私保证（信息论隐私泄露界，如 I(S（twc.2024.3369170）
- [推断] Ẑ) 上界）（twc.2024.3369170）
- [推断] 知识库失配的理论刻画（jsac.2022.3221991）
- [推断] 生成幻觉的度量与控制（语义保真 vs 感知）（jsac.2023.3288243）
- [推断] JSCC 中率-失真-感知权衡的理论刻画（jsac.2023.3288243）
- [推断] 可认证鲁棒性（certified robustness）在语义通信中的界（jsac.2023.3288249）
- [推断] 把 SRDF 作为学习型语义编码的理论基准（如用神经网络估计 SRDF 并与 deep JSCC 比较）（tcomm.2023.3274122）
- [推断] 加入信道得到语义 JSCC 的可达性 / 逆定理（tcomm.2023.3274122）
- [推断] 多任务（多个语义失真）的率失真区域（tcomm.2023.3274122）
- [推断] 与率-失真-感知理论的统一（tcomm.2023.3274122）
- [推断] 用感知指标（LPIPS 等）做质量预测与约束（twc.2023.3234408）
- [推断] 语义度量与人类评价的一致性检验（jsac.2022.3191112）
- [推断] 感知指标训练与生成式解码器（jsac.2022.3180802）
- [推断] 语义信息论的严格度量（tsp.2021.3071210）

## adaptivity (SNR / bandwidth / content)（24 条，19 篇）

- [原文] 结论 bullet："Multi-user case: Future research could explore the extension of the D2-JSCC framework to a multi-user scenario, but the adaptive design of source-channel coders may pose challenges due to …"（jsac.2025.3531546）
- [原文] "This insight points toward future research in adaptive semantic communications with channel feedback to improve both radio and computation efficiency."（jsac.2025.3559120）
- [原文] 原文局限："It is worth emphasizing that in the event of a change in channel SNR, all systems undergo retraining to optimize their performance under the specific SNR condition."（twc.2024.3379244）
- [原文] 结论 bullet："Variable length JSCC. Building upon the adaptability of ViT-based models to varying antenna numbers, future investigations can extend this concept to accommodate variable code lengths, …"（twc.2024.3422794）
- [原文] "As part of future work, the coding efficiency of DeepWiVe may be improved by considering variable GoP sizes."（jsac.2022.3191354）
- [原文] "Another possible future work is to design novel pilot structures and CSI feedback schemes to improve the accuracy of the CSI and the quality of reconstructed source via …"（tccn.2022.3151935）
- [原文] "We will explore adaptive power allocation strategies through reinforcement learning as a future extension of this work, …"（jsait.2020.2987203）
- [原文] "An implementation of such hybrid solution is left for future work."（根据反馈噪声决定是否利用反馈）（jsait.2020.2987203）
- [推断] 与 HARQ / 自适应调制编码（AMC）结合（jsac.2025.3531546）
- [推断] 减少联合自适应的性能损失（tccn.2024.3424842）
- [推断] 用户数可变 / 动态接入（tccn.2023.3326302）
- [推断] 文本 / 视觉两路的带宽分配与不等错误保护（tccn.2024.3401712）
- [推断] 调制阶数随信道自适应（后续 tccn.2024.3422496 的方向）（tcomm.2024.3386577）
- [推断] 码本大小与调制阶数的联合自适应（tcomm.2024.3364990）
- [推断] 关键点 + 残差的分层传输兼顾细节（jsac.2022.3221968）
- [推断] 多用户视频流的带宽共享（jsac.2022.3221977）
- [推断] 设备间异构算力与带宽的联合调度（twc.2022.3191118）
- [推断] 码本大小、调制阶数与信道质量的联合自适应（后续数字 JSCC 系列）（twc.2023.3265201）
- [推断] 语义特征域条件编码（后续 jsac.2022.3221977 DVST）（jsac.2022.3191354）
- [推断] 调制阶数随 SNR 自适应（后续 tccn.2024.3422496）（jsait.2022.3231042）
- [推断] 带宽自适应与 SNR 自适应同时实现的单一模型（twc.2021.3090048）
- [推断] 分层传输与 HARQ / 反馈结合（twc.2021.3090048）
- [推断] Transformer 架构下的可变长度编码（后续 SwinJSCC、NTSCC 的速率自适应）（twc.2021.3090048）
- [推断] SNR / 带宽自适应的单一模型（后续 ADJSCC、bandwidth-agile、SwinJSCC 解决）（tccn.2019.2919300）

## fading / MIMO / OFDM / real channels（23 条，17 篇）

- [原文] 结论 bullet："Fading channel: More advanced techniques, e.g., truncated power control can be combined with the D2-JSCC framework to overcome channel fading."（jsac.2025.3531546）
- [原文] 结论 bullet："JSCC with space-time coding. In the open-loop scenario, full potential of the spatial and temporal dimensions in MIMO can be harnessed by integrating DeepJSCC with space-time codes [56]."（twc.2024.3422794）
- [原文] "Another future direction is to add more details to the OFDM system such as carrier frequency offset (CFO) and packet detection so that the system is more practical."（tccn.2022.3151935）
- [原文] "Another possible future work is to design novel pilot structures and CSI feedback schemes to improve the accuracy of the CSI and the quality of reconstructed source via …"（tccn.2022.3151935）
- [原文] "We will also explore the performance of the system for non-Gaussian channels as well as for channels with memory, for which we do not have capacity-approaching channel codes."（tccn.2019.2919300）
- [推断] MIMO / OFDM 下的 Transformer JSCC（tccn.2024.3424842）
- [推断] 异步与多径下的正交性（tccn.2023.3326302）
- [推断] 衰落信道与数字传输下的多模态融合（tccn.2024.3401712）
- [推断] 衰落 / MIMO / OFDM 下的 JCM（tcomm.2024.3386577）
- [推断] MIMO / OFDM 与频率选择性信道下的条件分布推导（twc.2024.3379244）
- [推断] 与信道估计联合（不依赖完美 CSI）（twc.2024.3379244）
- [推断] 多用户 MIMO 下的语义传输与干扰管理（twc.2024.3422794）
- [推断] 大规模 MIMO / 相关信道下的扩展（twc.2024.3422794）
- [推断] 与数字调制兼容的 MIMO JSCC（twc.2024.3422794）
- [推断] MIMO / OFDM 下的视频 deep JSCC（jsac.2022.3221977）
- [推断] 不完美 CSI 下的鲁棒设计（jsac.2023.3240713）
- [推断] 衰落信道与数字调制下的生成式 JSCC（jsac.2023.3288243）
- [推断] 攻击检测与信道估计联合（jsac.2023.3288249）
- [推断] 在噪声 / 衰落多址信道上的分布式任务导向 JSCC（如空中计算 AirComp 融合特征）（twc.2022.3191118）
- [推断] 衰落 / MIMO（jsac.2021.3126087）
- [推断] 衰落与 MIMO 下的星座约束 JSCC（jsait.2022.3231042）
- [推断] MIMO-OFDM 下的 JSCC（后续 twc.2024.3422794）（tccn.2022.3151935）
- [推断] MIMO / OFDM 下按熵分配子信道与功率（jsac.2022.3180802）

## security / privacy / robustness（17 条，9 篇）

- [推断] 隐私性的信息论量化（tccn.2023.3326302）
- [推断] 可证明的隐私保证（信息论隐私泄露界，如 I(S（twc.2024.3369170）
- [推断] 生成式攻击者（扩散模型反演）下的鲁棒性（twc.2024.3369170）
- [推断] 窃听信道下语义安全（物理层安全 + 语义）（twc.2024.3369170）
- [推断] 多用户、联邦训练中的隐私（twc.2024.3369170）
- [推断] 与 jsac.2023.3288249 的对抗鲁棒性统一框架（twc.2024.3369170）
- [推断] 生成内容的身份安全（深伪风险）（jsac.2022.3221968）
- [推断] 梯度回传的隐私泄露分析（与 twc.2024.3369170 的模型反演攻击相关）（jsac.2022.3221991）
- [推断] 不完美 CSI 下的鲁棒设计（jsac.2023.3240713）
- [推断] 黑盒 / 迁移攻击（jsac.2023.3288249）
- [推断] 可认证鲁棒性（certified robustness）在语义通信中的界（jsac.2023.3288249）
- [推断] 生成式与数字语义系统的对抗鲁棒性（jsac.2023.3288249）
- [推断] 攻击检测与信道估计联合（jsac.2023.3288249）
- [推断] 多用户场景下的语义干扰攻击（jsac.2023.3288249）
- [推断] 黑盒 / 物理层攻击（后续 jsac.2023.3288249）（twc.2023.3265201）
- [推断] 隐私（特征可被反演，后续 twc.2024.3369170）（jsac.2021.3126087）
- [推断] 数字化与隐私（多用户特征泄露）（jsac.2022.3191326）

## generative / foundation models（17 条，13 篇）

- [推断] 通信功率与生成计算能耗的联合优化（jsac.2025.3559120）
- [推断] 更大模型 / 生成式先验带来的感知质量提升（tccn.2024.3424842）
- [推断] 接收端用生成模型（扩散）从文本 + 粗视觉特征重建（tccn.2024.3401712）
- [推断] LLM 推理时延与能耗的系统级优化（tccn.2024.3401712）
- [推断] 生成式攻击者（扩散模型反演）下的鲁棒性（twc.2024.3369170）
- [推断] 数字调制下的扩散去噪（twc.2024.3379244）
- [推断] 基础模型作为统一语义编解码器（tcomm.2024.3364990）
- [推断] 扩散 / 3D 人脸模型提升保真（jsac.2022.3221968）
- [推断] 生成内容的身份安全（深伪风险）（jsac.2022.3221968）
- [推断] 生成式先验提升低码率视频感知质量（如视频会议，jsac.2022.3221968）（jsac.2022.3221977）
- [推断] 通用图像上的生成式 JSCC（扩散模型替代 GAN，见 twc.2024.3379244 等）（jsac.2023.3288243）
- [推断] 生成幻觉的度量与控制（语义保真 vs 感知）（jsac.2023.3288243）
- [推断] 衰落信道与数字调制下的生成式 JSCC（jsac.2023.3288243）
- [推断] 生成式与数字语义系统的对抗鲁棒性（jsac.2023.3288249）
- [推断] 扩散模型替代 GAN（jsac.2022.3221999）
- [推断] 感知指标训练与生成式解码器（jsac.2022.3180802）
- [推断] 与语音大模型结合（jsac.2021.3087240）

## complexity / energy / latency / deployment（12 条，10 篇）

- [原文] "This insight points toward future research in adaptive semantic communications with channel feedback to improve both radio and computation efficiency."（jsac.2025.3559120）
- [原文] "LaMoSC's limitation is how to lighten the proposed multimodal semantic encoding and decoding so that it can be applied on mobile devices."（tccn.2024.3401712）
- [推断] 通信功率与生成计算能耗的联合优化（jsac.2025.3559120）
- [推断] 轻量化部署（tccn.2024.3424842）
- [推断] LLM 推理时延与能耗的系统级优化（tccn.2024.3401712）
- [推断] 少步 / 一步采样（一致性模型、蒸馏）降低时延（twc.2024.3379244）
- [推断] 实时性（模型加速、轻量化）（jsac.2022.3221977）
- [推断] 测试时优化的复杂度 / 时延（jsac.2023.3288243）
- [推断] 反馈开销计入后的权衡（twc.2022.3191118）
- [推断] 实时流式传输的时延（twc.2023.3240969）
- [推断] 能效目标（后续 jsac.2023.3240713）（jsac.2022.3191112）
- [推断] 物联网轻量化（L-DeepSC）（tsp.2021.3071210）

## knowledge base / continual & online learning（10 条，6 篇）

- [原文] "There are many interesting problems to further investigate in the future, such as how to coordinate the training of semantic encoder and decoder with minimum communication cost, how …"（jsac.2022.3221991）
- [推断] 新任务的增量 / 持续学习（不遗忘）（tcomm.2024.3364990）
- [推断] 在线 / 持续学习应对数据漂移（jsac.2022.3221991）
- [推断] 知识库失配的理论刻画（jsac.2022.3221991）
- [推断] 知识库更新频率与公共消息开销的权衡（jsac.2023.3240713）
- [推断] 在线更新预测器以适应新数据分布（twc.2023.3234408）
- [推断] 传输错误对三元组 / 知识图谱的影响与纠错（jsac.2022.3191112）
- [推断] 多模态知识图谱（jsac.2022.3191112）
- [推断] 收发两端知识图谱不一致（jsac.2022.3191112）
- [推断] 知识库失配与持续学习（tsp.2021.3071210）

## architecture / training improvements（8 条，8 篇）

- [原文] "An important direction of future research is to further optimize the performance of the proposed approach through the development of advanced designs for modulation schemes, quantization methods, and loss functions."（tccn.2024.3422496）
- [原文] "In future work, we can explore the design of a more powerful network architecture to improve the transmission performance of the proposed DeepMA model."（tccn.2023.3326302）
- [原文] "The idea of using alternating minimization appears to be a promising methodology to study and compute such general classes of distortion fidelities."（tcomm.2023.3274122）
- [原文] "… thus our future work is improving the network architecture and training algorithm of the DeepJSCC-V model to further improve its coding capability."（twc.2023.3234408）
- [原文] "The next step in improving the performance of the deep JSCC scheme is to exploit more advanced NN architectures in the autoencoder that have been shown to improve …"（tccn.2019.2919300）
- [推断] MIMO / OFDM 下的 Transformer JSCC（tccn.2024.3424842）
- [推断] Transformer 架构下的可变长度编码（后续 SwinJSCC、NTSCC 的速率自适应）（twc.2021.3090048）
- [推断] 用 Transformer 处理反馈（后续 twc.2024.3386052）（jsait.2020.2987203）

## hardware / over-the-air validation（3 条，2 篇）

- [原文] "The performance of the models should also be evaluated in practical channels, using, for example, software defined radios (SDRs)."（jsac.2022.3191354）
- [原文] "Another future direction is to add more details to the OFDM system such as carrier frequency offset (CFO) and packet detection so that the system is more practical."（tccn.2022.3151935）
- [推断] 硬件 / 空口验证（tccn.2022.3151935）

## 其他

- [推断] 用实际 deep JSCC 模型在叠加干扰下训练验证回归模型（jsac.2022.3222000）
- [推断] 用实际 deep JSCC 模型替换抽象语义函数，评估端到端语义性能（jsac.2023.3240713）
- [推断] 按语义重要性分配子载波（后续 tcomm.2024.3397862）（tccn.2022.3151935）
- [原文] "Given the above, it is interesting to further investigate task-oriented communication strategies for other edge AI systems and applications, e.g., to design tighter bounds in variational approximations, to …"（twc.2022.3191118）

