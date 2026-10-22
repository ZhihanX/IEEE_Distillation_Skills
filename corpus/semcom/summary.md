# 语义通信 / JSCC 子语料汇总

自动生成（`python3 pipeline/aggregate_semcom.py`）。研究论文 n = 37，综述 2 篇（单独列出，不计入频率）。
频率写成 k/n；列表字段一篇可计多个值。关键词主题计数（开放问题、弱点）是下界，引用时写成 "≥k/n"。

## 1. 类别与年均引用

| 类别 | 篇数 | 年均引用中位数 |
|---|---|---|
| image-jscc | 10 | 80.9 |
| task-multiuser | 6 | 70.9 |
| modality | 6 | 82.95 |
| digital | 5 | 49.6 |
| generative | 4 | 51.95 |
| networking | 3 | 52.8 |
| theory-security | 3 | 29 |

## 2. 字段频率（研究论文）

- **category**：image-jscc 10/37, task-multiuser 6/37, modality 6/37, digital 5/37, generative 4/37, networking 3/37, theory-security 3/37
- **paradigm**：analog-jscc 17/37, task-feature 7/37, digital-jscc 4/37, knowledge-based 3/37, separate-learned 3/37, system-level 2/37, theory 1/37
- **theory**：none 25/37, information-bottleneck 3/37, rate-distortion 3/37, other 2/37, performance-bound 2/37, information-theoretic 2/37
- **source**：image 27/37, text 7/37, video 3/37, speech 3/37, abstract-source 1/37, multi-view 1/37
- **task**：reconstruction 31/37, classification 10/37, segmentation 3/37, retrieval 3/37, recognition 2/37, VQA 2/37, remote-source-coding 1/37, synthesis 1/37, multi-task 1/37, translation 1/37, sentiment 1/37
- **architecture**：CNN 24/37, transformer 11/37, attention 8/37, GAN 5/37, MLP 3/37, VAE 3/37, Swin 3/37, RL 2/37, hyperprior 2/37, LLM 2/37, diffusion 2/37, VQ 2/37, probability-graph 1/37, RNN 1/37
- **channel**：AWGN 27/37, Rayleigh 23/37, OFDM 4/37, MIMO 4/37, Rician 4/37, feedback 2/37, erasure-packet 1/37, abstract 1/37
- **adaptivity**：SNR 13/37, bandwidth-rate 11/37, none 10/37, content 5/37, resource-allocation 3/37, CSI 3/37, feedback-HARQ 2/37, modulation 2/37, domain 1/37, power 1/37, task 1/37
- **training**：end-to-end 19/37, multi-stage 14/37, RL 3/37, none 3/37, pretrained-frozen 3/37, adversarial-training 2/37, domain-adaptation 1/37, receiver-led 1/37, test-time-optimization 1/37, robust-sampling 1/37, transfer-learning 1/37, separate-module 1/37, fine-tune 1/37, multi-objective 1/37
- **metrics**：PSNR 23/37, accuracy 12/37, MS-SSIM 12/37, custom 10/37, SSIM 6/37, BLEU 4/37, LPIPS 4/37, mIoU 3/37, bit-rate 2/37, latency 1/37, BD-rate 1/37, semantic-rate 1/37, power 1/37, energy 1/37, CLIP 1/37, rate-distortion 1/37, sentence-similarity 1/37, CER 1/37, WER 1/37, SDR 1/37, PESQ 1/37, Recall@1 1/37, FID 1/37, KID 1/37
- **datasets**：CIFAR-10 21/37, ImageNet 12/37, Kodak 12/37, MNIST 7/37, CIFAR-100 4/37, Tiny-ImageNet 3/37, OpenImages 3/37, CLIC 2/37, CelebA 2/37, DIV2K 2/37, Europarl 2/37, AGENDA 1/37, DocRED 1/37, BVI-DVC 1/37, UCF101 1/37, VoxCeleb 1/37, UVG 1/37, HEVC 1/37, Vimeo-90k 1/37, PASCAL-VOC2012 1/37, USPS 1/37, SVHN 1/37, STL-10 1/37, FFHQ 1/37, CelebA-HQ 1/37
- **baselines**：separate 30/37, other-learned 17/37, DeepJSCC 13/37, own-ablation 8/37, optimization 4/37, NTSCC 1/37, DeepSC 1/37
- **idea_delta**：adaptivity 13/37, new-component 9/37, new-metric 8/37, new-modality 8/37, theory 7/37, digitalization 6/37, new-task 5/37, multi-user 5/37, generative-prior 5/37, system-optimization 4/37, knowledge-base 4/37, robustness 4/37, new-channel 4/37, new-paradigm 3/37, feedback-retransmission 3/37, security-privacy 3/37

## 3. 评测完整性

- SNR 失配（训练 / 测试 SNR 不同）实验：19/37
- 报告复杂度（参数量 / FLOPs / 运行时间）：19/37
- 输出可直接接入数字链路：14/37
- 硬件 / 空口验证：0/37
- 至少一种衰落 / MIMO / OFDM 信道：27/37
- 信道只有 AWGN（不含无信道 / 抽象模型的论文）：9/37
- 基准含分离式方案（JPEG/BPG/H.26x + LDPC/容量界等）：30/37
- 报告感知类指标（MS-SSIM / LPIPS / FID / KID / CLIP）：14/37
- 开源代码：1/37
- 图像 / 视频论文中用到高分辨率数据集（Kodak / CLIC / DIV2K / ImageNet / CelebA-HQ / HEVC / UVG / Cityscapes）：20/30

## 4. idea_delta（相对基线的增量类型）

- 全体：adaptivity 13/37, new-component 9/37, new-metric 8/37, new-modality 8/37, theory 7/37, digitalization 6/37, new-task 5/37, multi-user 5/37, generative-prior 5/37, system-optimization 4/37, knowledge-base 4/37, robustness 4/37, new-channel 4/37, new-paradigm 3/37, feedback-retransmission 3/37, security-privacy 3/37
- 每篇的增量类型数：1 类 3/37, 2 类 16/37, 3 类 16/37, 4 类 2/37
- digital（5 篇）：digitalization 5/5, theory 2/5, adaptivity 2/5, robustness 2/5, new-component 1/5
- generative（4 篇）：generative-prior 4/4, new-metric 2/4, system-optimization 1/4, theory 1/4, knowledge-base 1/4, new-modality 1/4, new-component 1/4
- image-jscc（10 篇）：new-component 6/10, adaptivity 6/10, new-channel 4/10, feedback-retransmission 1/10, new-paradigm 1/10, new-task 1/10, new-metric 1/10, generative-prior 1/10
- modality（6 篇）：new-modality 6/6, adaptivity 2/6, new-metric 2/6, knowledge-base 1/6, feedback-retransmission 1/6, new-paradigm 1/6, new-task 1/6
- networking（3 篇）：system-optimization 3/3, multi-user 2/3, knowledge-base 1/3, new-metric 1/3, theory 1/3
- task-multiuser（6 篇）：new-task 3/6, multi-user 3/6, theory 2/6, adaptivity 2/6, new-paradigm 1/6, knowledge-base 1/6, robustness 1/6, new-component 1/6, security-privacy 1/6, feedback-retransmission 1/6, new-modality 1/6, digitalization 1/6
- theory-security（3 篇）：new-metric 2/3, security-privacy 2/3, robustness 1/3, theory 1/3, adaptivity 1/3

## 5. 继承关系（第 10 节"基线"行中引用的语料内论文）

被作为基线引用的次数：tccn.2019.2919300 (image-jscc) 12, tsp.2021.3071210 (modality) 4, jsac.2022.3180802 (image-jscc) 3, jsac.2021.3126087 (task-multiuser) 3, twc.2023.3265201 (digital) 2, jsac.2023.3288243 (generative) 2, jsait.2022.3231042 (digital) 2, twc.2024.3379244 (generative) 1, jsait.2020.2987203 (image-jscc) 1, twc.2021.3090048 (image-jscc) 1, jsac.2021.3087240 (modality) 1, tcomm.2024.3364990 (task-multiuser) 1, tccn.2024.3424842 (image-jscc) 1

| 论文 | 类别 | 年 | 基线（语料内） | 增量 |
|---|---|---|---|---|
| tccn.2019.2919300 | image-jscc | 2019 | — | new-paradigm |
| jsait.2020.2987203 | image-jscc | 2020 | tccn.2019.2919300 | feedback-retransmission, new-channel |
| jsac.2021.3087240 | modality | 2021 | tsp.2021.3071210 | new-modality |
| tsp.2021.3071210 | modality | 2021 | — | new-paradigm, new-modality, new-metric |
| twc.2021.3090048 | image-jscc | 2021 | tccn.2019.2919300 | adaptivity, new-channel |
| jsac.2021.3126087 | task-multiuser | 2022 | tccn.2019.2919300 | new-paradigm, theory, adaptivity |
| jsac.2022.3180802 | image-jscc | 2022 | tccn.2019.2919300 | new-component, adaptivity |
| jsac.2022.3191112 | networking | 2022 | — | system-optimization, new-metric, knowledge-base |
| jsac.2022.3191326 | task-multiuser | 2022 | — | multi-user, new-task, new-modality |
| jsac.2022.3191354 | modality | 2022 | tccn.2019.2919300 | new-modality, adaptivity |
| jsait.2022.3231042 | digital | 2022 | tccn.2019.2919300 | digitalization |
| tccn.2022.3151935 | image-jscc | 2022 | tccn.2019.2919300 | new-channel, new-component |
| jsac.2022.3221968 | modality | 2023 | — | new-modality, feedback-retransmission, knowledge-base, new-metric |
| jsac.2022.3221977 | modality | 2023 | jsac.2022.3180802 | new-modality, adaptivity |
| jsac.2022.3221991 | task-multiuser | 2023 | tsp.2021.3071210 | new-task, robustness, knowledge-base |
| jsac.2022.3221999 | image-jscc | 2023 | — | new-metric, generative-prior, new-component |
| jsac.2022.3222000 | networking | 2023 | tsp.2021.3071210 | multi-user, theory, system-optimization |
| jsac.2023.3240713 | networking | 2023 | — | system-optimization, multi-user |
| jsac.2023.3288243 | generative | 2023 | tccn.2019.2919300 | generative-prior, new-metric |
| jsac.2023.3288249 | theory-security | 2023 | twc.2023.3265201 | security-privacy, robustness, new-metric |
| tcomm.2023.3274122 | theory-security | 2023 | — | theory, new-metric |
| twc.2022.3191118 | task-multiuser | 2023 | jsac.2021.3126087 | multi-user, theory, feedback-retransmission |
| twc.2023.3234408 | image-jscc | 2023 | — | adaptivity, new-component |
| twc.2023.3240969 | modality | 2023 | tsp.2021.3071210, jsac.2021.3087240 | new-task, new-modality |
| twc.2023.3265201 | digital | 2023 | — | robustness, digitalization, new-component |
| tccn.2023.3326302 | task-multiuser | 2024 | — | multi-user, new-component, security-privacy |
| tccn.2024.3401712 | generative | 2024 | tccn.2019.2919300, jsait.2020.2987203 | knowledge-base, new-modality, generative-prior |
| tcomm.2024.3364990 | task-multiuser | 2024 | twc.2023.3265201 | new-task, digitalization, adaptivity |
| tcomm.2024.3386577 | digital | 2024 | jsait.2022.3231042 | digitalization, theory |
| twc.2023.3349330 | image-jscc | 2024 | tccn.2019.2919300, jsac.2021.3126087, tcomm.2024.3364990 | new-task, new-component, adaptivity |
| twc.2024.3369170 | theory-security | 2024 | jsac.2021.3126087 | security-privacy, adaptivity |
| twc.2024.3379244 | generative | 2024 | tccn.2024.3424842, jsac.2023.3288243 | generative-prior, new-component |
| twc.2024.3422794 | image-jscc | 2024 | tccn.2019.2919300 | new-channel, adaptivity |
| jsac.2025.3531546 | digital | 2025 | jsac.2022.3180802 | digitalization, theory, adaptivity |
| jsac.2025.3559120 | generative | 2025 | jsac.2023.3288243, twc.2024.3379244 | generative-prior, system-optimization, theory, new-metric |
| tccn.2024.3422496 | digital | 2025 | jsait.2022.3231042, twc.2021.3090048 | digitalization, adaptivity, robustness |
| tccn.2024.3424842 | image-jscc | 2025 | tccn.2019.2919300, jsac.2022.3180802 | new-component, adaptivity |

## 6. 开放问题（第 10 节，按主题汇总）

共 38 条作者原文、155 条推断（来自 39 张卡片）。一条可属多个主题；括号内是涉及的卡片数。

### new modality / task / dataset（45 条，27 篇）
- [推断] 检测、分割等复杂任务 — jsac.2021.3126087
- [推断] 多模态知识图谱 — jsac.2022.3191112
- [推断] 数字化视频 JSCC — jsac.2022.3191354
- [推断] 多用户 / 广播视频 — jsac.2022.3191354
- [推断] 任务导向视频（检测、跟踪） — jsac.2022.3191354
- [推断] 语义 HARQ 的通用化（其他模态的语义错误检测器） — jsac.2022.3221968
- [推断] 数字化视频语义传输（码本 / 量化 + 数字调制） — jsac.2022.3221977
- [推断] MIMO / OFDM 下的视频 deep JSCC — jsac.2022.3221977
- [推断] 多用户视频流的带宽共享 — jsac.2022.3221977
- [推断] 生成式先验提升低码率视频感知质量（如视频会议，jsac.2022.3221968） — jsac.2022.3221977
- [推断] 多接收端多任务下的接收端主导训练 — jsac.2022.3221991
- [推断] 图像 / 视频的语义速率曲线建模 — jsac.2022.3222000
- [推断] 视频 / 多模态的感知-误差刻画 — jsac.2025.3559120
- [原文] "… the general design principles presented in this work can be potentially applied to other information sources, such as audio or video." — jsait.2020.2987203
- [推断] 视频等其他信源（后续 DeepWiVe） — tccn.2019.2919300
- [原文] "One possible direction of future works is to generalize this work to other types of sources such as audio and video." — tccn.2022.3151935
- [原文] "Future research avenues could explore the further optimization of the encoder-decoder framework and expand the model's application to other modalities." — tccn.2024.3401712
- [推断] 衰落信道与数字传输下的多模态融合 — tccn.2024.3401712
- [推断] 高分辨率图像与重建任务 — tccn.2024.3422496
- [推断] 多任务（多个语义失真）的率失真区域 — tcomm.2023.3274122
- [推断] 高分辨率图像 — tcomm.2024.3386577
- [推断] 语音 / 图像 / 多模态（jsac.2021.3087240、twc.2023.3240969） — tsp.2021.3071210
- [推断] 在噪声 / 衰落多址信道上的分布式任务导向 JSCC（如空中计算 AirComp 融合特征） — twc.2022.3191118
- [推断] 把"质量预测 + 资源分配"推广到多用户 / 多任务的无线资源分配（后续大量 system-level 论文的基础） — twc.2023.3234408
- [推断] 多说话人 / 多语言 — twc.2023.3240969
- [推断] 韵律、情感等副语言语义的传输 — twc.2023.3240969
- [推断] 与大语音模型（Whisper 类）结合 — twc.2023.3240969
- [推断] 多用户语音语义通信的资源分配 — twc.2023.3240969
- [推断] 文本、语音等其他模态的语义噪声 — twc.2023.3265201
- [原文] 结论 bullet："Extension to more complex downstream tasks: … How to extend the proposed designs to more complex downstream tasks is an interesting …" — twc.2023.3349330
- [原文] 结论 bullet："Extension to more complex datasets: Extending our proposed framework on more complex datasets such as ImageNet is also worth pursuing in future work." — twc.2023.3349330
- [推断] 多用户、多接收端各自执行不同任务（广播多任务） — twc.2023.3349330
- [推断] 任务之间的理论权衡刻画 — twc.2023.3349330
- [推断] 对任务型语义特征的去噪 — twc.2024.3379244
- [推断] 面向识别 / 合成任务的语音语义通信（后续 twc.2023.3240969） — jsac.2021.3087240
- [推断] 多说话人与噪声环境 — jsac.2021.3087240
- [推断] 数字化与低码率语音语义编码 — jsac.2021.3087240
- [推断] 与语音大模型结合 — jsac.2021.3087240
- [推断] 视频扩展（后续 jsac.2022.3221977） — jsac.2022.3180802
- [推断] 用户 / 任务动态变化 — jsac.2022.3191326
- [推断] 统一多任务模型（后续 tcomm.2024.3364990） — jsac.2022.3191326
- [推断] 语义概念的不等错误保护 — jsac.2022.3221999
- [推断] 通用场景（非街景）上的语义概念定义 — jsac.2022.3221999
- [推断] 新任务的增量 / 持续学习（不遗忘） — tcomm.2024.3364990
- [推断] 多用户场景下的统一多任务系统 — tcomm.2024.3364990

### digital compatibility / modulation / channel coding（44 条，28 篇）
- [推断] 数字化 IB 特征（离散码本） — jsac.2021.3126087
- [推断] 传输错误对三元组 / 知识图谱的影响与纠错 — jsac.2022.3191112
- [推断] 数字化视频 JSCC — jsac.2022.3191354
- [推断] 语义 HARQ 的通用化（其他模态的语义错误检测器） — jsac.2022.3221968
- [推断] 数字化视频语义传输（码本 / 量化 + 数字调制） — jsac.2022.3221977
- [推断] 与 HARQ / 反馈结合缓解 GOP 内误差传播 — jsac.2022.3221977
- [推断] 实时性（模型加速、轻量化） — jsac.2022.3221977
- [推断] 衰落信道与数字调制下的生成式 JSCC — jsac.2023.3288243
- [推断] 生成式与数字语义系统的对抗鲁棒性 — jsac.2023.3288249
- [推断] 与 HARQ / 自适应调制编码（AMC）结合 — jsac.2025.3531546
- [推断] 高阶调制下的速率控制 — jsac.2025.3531546
- [推断] 反馈与 ARQ/HARQ 的结合（后续出现 HARQ 类语义传输） — jsait.2020.2987203
- [推断] 低阶星座下的性能提升（后续 tcomm.2024.3386577 用概率建模） — jsait.2022.3231042
- [推断] 调制阶数随 SNR 自适应（后续 tccn.2024.3422496） — jsait.2022.3231042
- [推断] 与信道编码 / 比特接口的结合（D²-JSCC 等） — jsait.2022.3231042
- [推断] 衰落与 MIMO 下的星座约束 JSCC — jsait.2022.3231042
- [推断] 数字化与星座约束（后续 DeepJSCC-Q、D²-JSCC） — tccn.2019.2919300
- [推断] 隐私性的信息论量化 — tccn.2023.3326302
- [推断] 文本 / 视觉两路的带宽分配与不等错误保护 — tccn.2024.3401712
- [推断] 衰落信道与数字传输下的多模态融合 — tccn.2024.3401712
- [原文] "An important direction of future research is to further optimize the performance of the proposed approach through the development of advanced designs for modulation schemes, quantization methods, and loss functions." — tccn.2024.3422496
- [原文] "Another promising research direction is to extend the proposed JSCC approach to accommodate soft-output demodulation for JSCC-based semantic communications." — tccn.2024.3422496
- [推断] 与信道编码 / HARQ 的结合 — tccn.2024.3422496
- [推断] 符号内比特相关性的建模（非独立 BSEC） — tccn.2024.3422496
- [推断] 数字化（量化 + 星座）下的 Swin 骨干（后续 D²-JSCC 等） — tccn.2024.3424842
- [推断] 轻量化部署 — tccn.2024.3424842
- [原文] "Looking ahead, our future efforts will focus on the design and optimization of constellation geometry shaping to enhance the system's performance." — tcomm.2024.3386577
- [推断] 与信道编码（纠错码）的联合 — tcomm.2024.3386577
- [推断] 调制阶数随信道自适应（后续 tccn.2024.3422496 的方向） — tcomm.2024.3386577
- [推断] 数字化与量化（后续 digital 系列） — tsp.2021.3071210
- [推断] 物联网轻量化（L-DeepSC） — tsp.2021.3071210
- [推断] 分层传输与 HARQ / 反馈结合 — twc.2021.3090048
- [推断] 数字化（码本 / 量化） — twc.2023.3240969
- [推断] 码本索引的信道编码与不等错误保护 — twc.2023.3265201
- [推断] 码本大小、调制阶数与信道质量的联合自适应（后续数字 JSCC 系列） — twc.2023.3265201
- [推断] 与数字调制兼容 — twc.2023.3349330
- [推断] 数字调制下的扩散去噪 — twc.2024.3379244
- [推断] 与数字调制兼容的 MIMO JSCC — twc.2024.3422794
- [推断] 数字化与低码率语音语义编码 — jsac.2021.3087240
- [推断] 数字化 NTSCC（熵模型 + 真实信道码的速率控制，后续 jsac.2025.3531546） — jsac.2022.3180802
- [推断] 数字化与隐私（多用户特征泄露） — jsac.2022.3191326
- [推断] 语义—感知准则下的联合信源信道编码（端到端过信道训练） — jsac.2022.3221999
- [推断] 语义概念的不等错误保护 — jsac.2022.3221999
- [推断] 码本大小与调制阶数的联合自适应 — tcomm.2024.3364990

### multi-user / multiple access / networking（29 条，22 篇）
- [原文] "There are many interesting future research directions on this exciting topic, e.g., to apply the IB-based framework to the scenario with multiple devices, to develop a theoretical understanding …" — jsac.2021.3126087
- [推断] 多设备协同推理（后续 twc.2022.3191118） — jsac.2021.3126087
- [推断] 多用户 / 广播视频 — jsac.2022.3191354
- [推断] 多方会议的多用户资源分配 — jsac.2022.3221968
- [推断] 多用户视频流的带宽共享 — jsac.2022.3221977
- [原文] 结论 bullet："Heterogeneous transmission design with multiple S- and B-users: This paper considered a fundamental model with one S-user and one B-user." — jsac.2022.3222000
- [原文] 结论 bullet："Opportunistic semantic and bit transmission design: This paper assumed that each user can only use one specific transmission method, i.e., semantic or bit-based transmission." — jsac.2022.3222000
- [推断] 多天线 / RSMA 下的语义-比特共存 — jsac.2022.3222000
- [推断] RIS / ISAC 等其他技术与语义通信的结构性结合 — jsac.2023.3240713
- [推断] 多用户场景下的语义干扰攻击 — jsac.2023.3288249
- [原文] 结论 bullet："Multi-user case: Future research could explore the extension of the D2-JSCC framework to a multi-user scenario, but the adaptive design of source-channel coders may pose challenges due to …" — jsac.2025.3531546
- [推断] 多用户下的语义感知资源分配 — jsac.2025.3559120
- [推断] 多用户下的反馈利用 — jsait.2020.2987203
- [推断] 非正交语义多址（语义 NOMA，见 jsac.2022.3222000） — tccn.2023.3326302
- [推断] 与经典多址在相同资源下的公平比较 — tccn.2023.3326302
- [原文] "Investigating an extension of the proposed approach to support multi-task multi-user semantic communications, where multiple devices engage in different tasks concurrently, would also be an important direction for future research." — tccn.2024.3422496
- [推断] 多用户（jsac.2022.3191326） — tsp.2021.3071210
- [推断] 多用户广播中不同用户收到不同层数 — twc.2021.3090048
- [推断] 在噪声 / 衰落多址信道上的分布式任务导向 JSCC（如空中计算 AirComp 融合特征） — twc.2022.3191118
- [推断] 设备间异构算力与带宽的联合调度 — twc.2022.3191118
- [推断] 真实多传感器（多摄像头、雷达 + 视觉）数据 — twc.2022.3191118
- [推断] 把"质量预测 + 资源分配"推广到多用户 / 多任务的无线资源分配（后续大量 system-level 论文的基础） — twc.2023.3234408
- [推断] 多用户语音语义通信的资源分配 — twc.2023.3240969
- [推断] 多用户、多接收端各自执行不同任务（广播多任务） — twc.2023.3349330
- [推断] 多用户、联邦训练中的隐私 — twc.2024.3369170
- [推断] 多用户 MIMO 下的语义传输与干扰管理 — twc.2024.3422794
- [推断] 语义感知的多址与资源分配（见 tccn.2023.3326302、jsac.2022.3222000） — jsac.2022.3191326
- [推断] 数字化与隐私（多用户特征泄露） — jsac.2022.3191326
- [推断] 多用户场景下的统一多任务系统 — tcomm.2024.3364990

### theory / limits / metrics（25 条，16 篇）
- [原文] "There are many interesting future research directions on this exciting topic, e.g., to apply the IB-based framework to the scenario with multiple devices, to develop a theoretical understanding …" — jsac.2021.3126087
- [推断] 语义度量与人类评价的一致性检验 — jsac.2022.3191112
- [推断] 知识库失配的理论刻画 — jsac.2022.3221991
- [原文] 结论 bullet："Performance limit characterization of the heterogeneous transmission with multimodal data: The semantic rate considered in this paper is used for characterizing the performance of text semantic communications." — jsac.2022.3222000
- [推断] 生成幻觉的度量与控制（语义保真 vs 感知） — jsac.2023.3288243
- [推断] JSCC 中率-失真-感知权衡的理论刻画 — jsac.2023.3288243
- [原文] "This is probably because the semantics involved in CIFAR are much more complex than the ones in MNIST, and further understanding such a phenomenon would be an interesting …" — jsac.2023.3288249
- [推断] 可认证鲁棒性（certified robustness）在语义通信中的界 — jsac.2023.3288249
- [原文] 结论 bullet："E2E metric design: This paper described the E2E performance using the classical MSE metric, which might not be optimal for certain task-oriented applications." — jsac.2025.3531546
- [推断] 感知指标下的失真刻画 — jsac.2025.3531546
- [原文] "Despite these advances, a universal semantic information theory for SemCom system design remains an open challenge." — jsac.2025.3559120
- [推断] 感知-误差函数的解析模型（替代曲线拟合） — jsac.2025.3559120
- [推断] 隐私性的信息论量化 — tccn.2023.3326302
- [原文] "Second, we seek to generalize our goal-oriented communication setup beyond separable distortion criteria, since in real world applications one is more interested in relations between the input and …" — tcomm.2023.3274122
- [推断] 把 SRDF 作为学习型语义编码的理论基准（如用神经网络估计 SRDF 并与 deep JSCC 比较） — tcomm.2023.3274122
- [推断] 加入信道得到语义 JSCC 的可达性 / 逆定理 — tcomm.2023.3274122
- [推断] 多任务（多个语义失真）的率失真区域 — tcomm.2023.3274122
- [推断] 与率-失真-感知理论的统一 — tcomm.2023.3274122
- [推断] 语义信息论的严格度量 — tsp.2021.3071210
- [原文] "While the optimal rate-distortion region for the multiple description problem remains open for general source distributions, optimal characterization is known for Gaussian sources [9]."（理论上仍开放） — twc.2021.3090048
- [推断] 用感知指标（LPIPS 等）做质量预测与约束 — twc.2023.3234408
- [推断] 任务之间的理论权衡刻画 — twc.2023.3349330
- [推断] 可证明的隐私保证（信息论隐私泄露界，如 I(S — twc.2024.3369170
- [推断] Ẑ) 上界） — twc.2024.3369170
- [推断] 感知指标训练与生成式解码器 — jsac.2022.3180802

### adaptivity (SNR / bandwidth / content)（24 条，19 篇）
- [原文] "As part of future work, the coding efficiency of DeepWiVe may be improved by considering variable GoP sizes." — jsac.2022.3191354
- [推断] 语义特征域条件编码（后续 jsac.2022.3221977 DVST） — jsac.2022.3191354
- [推断] 关键点 + 残差的分层传输兼顾细节 — jsac.2022.3221968
- [推断] 多用户视频流的带宽共享 — jsac.2022.3221977
- [原文] 结论 bullet："Multi-user case: Future research could explore the extension of the D2-JSCC framework to a multi-user scenario, but the adaptive design of source-channel coders may pose challenges due to …" — jsac.2025.3531546
- [推断] 与 HARQ / 自适应调制编码（AMC）结合 — jsac.2025.3531546
- [原文] "This insight points toward future research in adaptive semantic communications with channel feedback to improve both radio and computation efficiency." — jsac.2025.3559120
- [原文] "We will explore adaptive power allocation strategies through reinforcement learning as a future extension of this work, …" — jsait.2020.2987203
- [原文] "An implementation of such hybrid solution is left for future work."（根据反馈噪声决定是否利用反馈） — jsait.2020.2987203
- [推断] 调制阶数随 SNR 自适应（后续 tccn.2024.3422496） — jsait.2022.3231042
- [推断] SNR / 带宽自适应的单一模型（后续 ADJSCC、bandwidth-agile、SwinJSCC 解决） — tccn.2019.2919300
- [原文] "Another possible future work is to design novel pilot structures and CSI feedback schemes to improve the accuracy of the CSI and the quality of reconstructed source via …" — tccn.2022.3151935
- [推断] 用户数可变 / 动态接入 — tccn.2023.3326302
- [推断] 文本 / 视觉两路的带宽分配与不等错误保护 — tccn.2024.3401712
- [推断] 减少联合自适应的性能损失 — tccn.2024.3424842
- [推断] 调制阶数随信道自适应（后续 tccn.2024.3422496 的方向） — tcomm.2024.3386577
- [推断] 带宽自适应与 SNR 自适应同时实现的单一模型 — twc.2021.3090048
- [推断] 分层传输与 HARQ / 反馈结合 — twc.2021.3090048
- [推断] Transformer 架构下的可变长度编码（后续 SwinJSCC、NTSCC 的速率自适应） — twc.2021.3090048
- [推断] 设备间异构算力与带宽的联合调度 — twc.2022.3191118
- [推断] 码本大小、调制阶数与信道质量的联合自适应（后续数字 JSCC 系列） — twc.2023.3265201
- [原文] 原文局限："It is worth emphasizing that in the event of a change in channel SNR, all systems undergo retraining to optimize their performance under the specific SNR condition." — twc.2024.3379244
- [原文] 结论 bullet："Variable length JSCC. Building upon the adaptability of ViT-based models to varying antenna numbers, future investigations can extend this concept to accommodate variable code lengths, …" — twc.2024.3422794
- [推断] 码本大小与调制阶数的联合自适应 — tcomm.2024.3364990

### fading / MIMO / OFDM / real channels（23 条，17 篇）
- [推断] 衰落 / MIMO — jsac.2021.3126087
- [推断] MIMO / OFDM 下的视频 deep JSCC — jsac.2022.3221977
- [推断] 不完美 CSI 下的鲁棒设计 — jsac.2023.3240713
- [推断] 衰落信道与数字调制下的生成式 JSCC — jsac.2023.3288243
- [推断] 攻击检测与信道估计联合 — jsac.2023.3288249
- [原文] 结论 bullet："Fading channel: More advanced techniques, e.g., truncated power control can be combined with the D2-JSCC framework to overcome channel fading." — jsac.2025.3531546
- [推断] 衰落与 MIMO 下的星座约束 JSCC — jsait.2022.3231042
- [原文] "We will also explore the performance of the system for non-Gaussian channels as well as for channels with memory, for which we do not have capacity-approaching channel codes." — tccn.2019.2919300
- [原文] "Another future direction is to add more details to the OFDM system such as carrier frequency offset (CFO) and packet detection so that the system is more practical." — tccn.2022.3151935
- [原文] "Another possible future work is to design novel pilot structures and CSI feedback schemes to improve the accuracy of the CSI and the quality of reconstructed source via …" — tccn.2022.3151935
- [推断] MIMO-OFDM 下的 JSCC（后续 twc.2024.3422794） — tccn.2022.3151935
- [推断] 异步与多径下的正交性 — tccn.2023.3326302
- [推断] 衰落信道与数字传输下的多模态融合 — tccn.2024.3401712
- [推断] MIMO / OFDM 下的 Transformer JSCC — tccn.2024.3424842
- [推断] 衰落 / MIMO / OFDM 下的 JCM — tcomm.2024.3386577
- [推断] 在噪声 / 衰落多址信道上的分布式任务导向 JSCC（如空中计算 AirComp 融合特征） — twc.2022.3191118
- [推断] MIMO / OFDM 与频率选择性信道下的条件分布推导 — twc.2024.3379244
- [推断] 与信道估计联合（不依赖完美 CSI） — twc.2024.3379244
- [原文] 结论 bullet："JSCC with space-time coding. In the open-loop scenario, full potential of the spatial and temporal dimensions in MIMO can be harnessed by integrating DeepJSCC with space-time codes [56]." — twc.2024.3422794
- [推断] 多用户 MIMO 下的语义传输与干扰管理 — twc.2024.3422794
- [推断] 大规模 MIMO / 相关信道下的扩展 — twc.2024.3422794
- [推断] 与数字调制兼容的 MIMO JSCC — twc.2024.3422794
- [推断] MIMO / OFDM 下按熵分配子信道与功率 — jsac.2022.3180802

### security / privacy / robustness（17 条，9 篇）
- [推断] 隐私（特征可被反演，后续 twc.2024.3369170） — jsac.2021.3126087
- [推断] 生成内容的身份安全（深伪风险） — jsac.2022.3221968
- [推断] 梯度回传的隐私泄露分析（与 twc.2024.3369170 的模型反演攻击相关） — jsac.2022.3221991
- [推断] 不完美 CSI 下的鲁棒设计 — jsac.2023.3240713
- [推断] 黑盒 / 迁移攻击 — jsac.2023.3288249
- [推断] 可认证鲁棒性（certified robustness）在语义通信中的界 — jsac.2023.3288249
- [推断] 生成式与数字语义系统的对抗鲁棒性 — jsac.2023.3288249
- [推断] 攻击检测与信道估计联合 — jsac.2023.3288249
- [推断] 多用户场景下的语义干扰攻击 — jsac.2023.3288249
- [推断] 隐私性的信息论量化 — tccn.2023.3326302
- [推断] 黑盒 / 物理层攻击（后续 jsac.2023.3288249） — twc.2023.3265201
- [推断] 可证明的隐私保证（信息论隐私泄露界，如 I(S — twc.2024.3369170
- [推断] 生成式攻击者（扩散模型反演）下的鲁棒性 — twc.2024.3369170
- [推断] 窃听信道下语义安全（物理层安全 + 语义） — twc.2024.3369170
- [推断] 多用户、联邦训练中的隐私 — twc.2024.3369170
- [推断] 与 jsac.2023.3288249 的对抗鲁棒性统一框架 — twc.2024.3369170
- [推断] 数字化与隐私（多用户特征泄露） — jsac.2022.3191326

### generative / foundation models（17 条，13 篇）
- [推断] 扩散 / 3D 人脸模型提升保真 — jsac.2022.3221968
- [推断] 生成内容的身份安全（深伪风险） — jsac.2022.3221968
- [推断] 生成式先验提升低码率视频感知质量（如视频会议，jsac.2022.3221968） — jsac.2022.3221977
- [推断] 通用图像上的生成式 JSCC（扩散模型替代 GAN，见 twc.2024.3379244 等） — jsac.2023.3288243
- [推断] 生成幻觉的度量与控制（语义保真 vs 感知） — jsac.2023.3288243
- [推断] 衰落信道与数字调制下的生成式 JSCC — jsac.2023.3288243
- [推断] 生成式与数字语义系统的对抗鲁棒性 — jsac.2023.3288249
- [推断] 通信功率与生成计算能耗的联合优化 — jsac.2025.3559120
- [推断] 接收端用生成模型（扩散）从文本 + 粗视觉特征重建 — tccn.2024.3401712
- [推断] LLM 推理时延与能耗的系统级优化 — tccn.2024.3401712
- [推断] 更大模型 / 生成式先验带来的感知质量提升 — tccn.2024.3424842
- [推断] 生成式攻击者（扩散模型反演）下的鲁棒性 — twc.2024.3369170
- [推断] 数字调制下的扩散去噪 — twc.2024.3379244
- [推断] 与语音大模型结合 — jsac.2021.3087240
- [推断] 感知指标训练与生成式解码器 — jsac.2022.3180802
- [推断] 扩散模型替代 GAN — jsac.2022.3221999
- [推断] 基础模型作为统一语义编解码器 — tcomm.2024.3364990

### complexity / energy / latency / deployment（12 条，10 篇）
- [推断] 能效目标（后续 jsac.2023.3240713） — jsac.2022.3191112
- [推断] 实时性（模型加速、轻量化） — jsac.2022.3221977
- [推断] 测试时优化的复杂度 / 时延 — jsac.2023.3288243
- [原文] "This insight points toward future research in adaptive semantic communications with channel feedback to improve both radio and computation efficiency." — jsac.2025.3559120
- [推断] 通信功率与生成计算能耗的联合优化 — jsac.2025.3559120
- [原文] "LaMoSC's limitation is how to lighten the proposed multimodal semantic encoding and decoding so that it can be applied on mobile devices." — tccn.2024.3401712
- [推断] LLM 推理时延与能耗的系统级优化 — tccn.2024.3401712
- [推断] 轻量化部署 — tccn.2024.3424842
- [推断] 物联网轻量化（L-DeepSC） — tsp.2021.3071210
- [推断] 反馈开销计入后的权衡 — twc.2022.3191118
- [推断] 实时流式传输的时延 — twc.2023.3240969
- [推断] 少步 / 一步采样（一致性模型、蒸馏）降低时延 — twc.2024.3379244

### knowledge base / continual & online learning（10 条，6 篇）
- [推断] 传输错误对三元组 / 知识图谱的影响与纠错 — jsac.2022.3191112
- [推断] 多模态知识图谱 — jsac.2022.3191112
- [推断] 收发两端知识图谱不一致 — jsac.2022.3191112
- [原文] "There are many interesting problems to further investigate in the future, such as how to coordinate the training of semantic encoder and decoder with minimum communication cost, how …" — jsac.2022.3221991
- [推断] 在线 / 持续学习应对数据漂移 — jsac.2022.3221991
- [推断] 知识库失配的理论刻画 — jsac.2022.3221991
- [推断] 知识库更新频率与公共消息开销的权衡 — jsac.2023.3240713
- [推断] 知识库失配与持续学习 — tsp.2021.3071210
- [推断] 在线更新预测器以适应新数据分布 — twc.2023.3234408
- [推断] 新任务的增量 / 持续学习（不遗忘） — tcomm.2024.3364990

### architecture / training improvements（8 条，8 篇）
- [推断] 用 Transformer 处理反馈（后续 twc.2024.3386052） — jsait.2020.2987203
- [原文] "The next step in improving the performance of the deep JSCC scheme is to exploit more advanced NN architectures in the autoencoder that have been shown to improve …" — tccn.2019.2919300
- [原文] "In future work, we can explore the design of a more powerful network architecture to improve the transmission performance of the proposed DeepMA model." — tccn.2023.3326302
- [原文] "An important direction of future research is to further optimize the performance of the proposed approach through the development of advanced designs for modulation schemes, quantization methods, and loss functions." — tccn.2024.3422496
- [推断] MIMO / OFDM 下的 Transformer JSCC — tccn.2024.3424842
- [原文] "The idea of using alternating minimization appears to be a promising methodology to study and compute such general classes of distortion fidelities." — tcomm.2023.3274122
- [推断] Transformer 架构下的可变长度编码（后续 SwinJSCC、NTSCC 的速率自适应） — twc.2021.3090048
- [原文] "… thus our future work is improving the network architecture and training algorithm of the DeepJSCC-V model to further improve its coding capability." — twc.2023.3234408

### other（4 条，4 篇）
- [推断] 用实际 deep JSCC 模型在叠加干扰下训练验证回归模型 — jsac.2022.3222000
- [推断] 用实际 deep JSCC 模型替换抽象语义函数，评估端到端语义性能 — jsac.2023.3240713
- [推断] 按语义重要性分配子载波（后续 tcomm.2024.3397862） — tccn.2022.3151935
- [原文] "Given the above, it is interesting to further investigate task-oriented communication strategies for other edge AI systems and applications, e.g., to design tighter bounds in variational approximations, to …" — twc.2022.3191118

### hardware / over-the-air validation（3 条，2 篇）
- [原文] "The performance of the models should also be evaluated in practical channels, using, for example, software defined radios (SDRs)." — jsac.2022.3191354
- [原文] "Another future direction is to add more details to the OFDM system such as carrier frequency offset (CFO) and packet detection so that the system is more practical." — tccn.2022.3151935
- [推断] 硬件 / 空口验证 — tccn.2022.3151935

## 7. 弱点主题（第 10 节"弱点"行，关键词下界）

- AWGN only / limited channel：≥12/37（jsac.2021.3126087, jsac.2022.3221977, jsac.2022.3221991, jsac.2023.3288243, jsac.2025.3531546, tccn.2022.3151935, tccn.2024.3401712, tccn.2024.3424842, tcomm.2024.3386577, tsp.2021.3071210, twc.2022.3191118, twc.2023.3240969）
- no complexity / latency analysis：≥15/37（jsac.2021.3126087, jsac.2022.3191354, jsac.2022.3221977, jsac.2023.3288243, jsac.2025.3559120, jsait.2020.2987203, jsait.2022.3231042, tccn.2023.3326302, twc.2022.3191118, twc.2023.3234408, twc.2023.3265201, twc.2023.3349330, twc.2024.3379244, jsac.2022.3180802, jsac.2022.3221999）
- small images / few datasets：≥13/37（jsac.2021.3126087, jsac.2023.3288243, jsac.2025.3559120, jsait.2020.2987203, tccn.2024.3401712, tccn.2024.3422496, tcomm.2024.3386577, twc.2023.3240969, twc.2023.3349330, twc.2024.3369170, jsac.2021.3087240, jsac.2022.3221999, tcomm.2024.3364990）
- analog only (not digital-compatible)：≥6/37（jsac.2021.3126087, jsac.2022.3221977, tsp.2021.3071210, twc.2024.3379244, jsac.2021.3087240, jsac.2022.3180802）
- no hardware validation：≥5/37（jsac.2022.3191354, tccn.2019.2919300, tccn.2024.3422496, tcomm.2024.3386577, twc.2024.3422794）
- weak / missing baselines：≥2/37（jsac.2023.3288243, jsac.2025.3559120）
- strong or unverified assumptions：≥8/37（jsac.2022.3222000, jsac.2023.3240713, jsac.2023.3288249, jsac.2025.3531546, jsac.2025.3559120, tccn.2024.3422496, twc.2023.3265201, twc.2024.3379244）
- no future work stated：≥13/37（jsac.2022.3191112, jsac.2022.3221968, jsac.2022.3221977, jsac.2023.3240713, jsac.2023.3288249, tsp.2021.3071210, twc.2023.3240969, twc.2024.3369170, twc.2024.3379244, jsac.2021.3087240, jsac.2022.3180802, jsac.2022.3191326, tcomm.2024.3364990）

## 8. 写作字段（`code:` 块，研究论文）

- **gap_type**：limitation 17/37, new-scenario 15/37, practicality 12/37, theory-gap 4/37, new-paradigm 3/37, tool-transfer 3/37, unification 3/37, new-metric 2/37, open-question 2/37, combination 2/37, security 2/37, new-tool 2/37
- **first_claim**：True 20/37, False 17/37
- **contrib_format**：bullets 31/37, paragraph 4/37, numbered 2/37
- **abstract_has_numbers**：False 31/37, True 6/37
- **theory_role**：none 21/37, supporting 12/37, central 4/37
- **problem_class**：learning 31/37, nonconvex-continuous 4/37, mixed-integer 1/37, information-theoretic 1/37
- **solution**：DNN 31/37, bound-surrogate 8/37, closed-form 4/37, exhaustive-search 3/37, RL 2/37, gradient 2/37, adversarial-training 2/37, one-dimensional-search 1/37, water-filling 1/37, AO 1/37, SCA 1/37, lagrange 1/37
- **x_axes**：SNR 28/37, bandwidth-ratio 8/37, epochs 6/37, CBR 3/37, compression-ratio 3/37, latency 2/37, iterations 2/37, BER 2/37, target-quality 2/37, number-of-layers 2/37, constellation-map 2/37, modulation-order 2/37
- **fig1_role**：framework 23/37, system-model 9/37, background 3/37, result 1/37, scenario 1/37
- **complexity_analysis**：True 19/37, False 18/37
- **sim_param_table**：False 24/37, True 13/37
- **code_released**：False 35/37, unclear 1/37, True 1/37
- **conclusion_future_work**：False 20/37, True 17/37
- **related_work**：in-intro 17/37, separate-section 10/37, in-intro-subsection 9/37, in-model-section 1/37
- **roadmap**：True 26/37, False 11/37
- **baselines_n**：中位数 3，范围 0–6

## 9. 综述

- jsac.2022.3223408 Beyond Transmitting Bits: Context, Semantics, and Task-Oriented Communications（2023，年均引用 216.1）
- tccn.2024.3435524 Generative AI-Driven Semantic Communication Networks: Architecture, Technologies, and Applications（2025，年均引用 92.5）
