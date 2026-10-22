# 设计空间：轴、研究线与继承关系

统计口径：37 篇研究论文的 `semcom:` 编码字段（`corpus/semcom/summary.md` 第 2、4、5 节）。列表字段一篇可计多个值。
DOI 一律省略 `10.1109/`。

## 1. 设计空间的轴

一个语义通信 / JSCC 工作可以用下面 9 个轴定位。生成 idea 时先填满这张表，再看哪一格可以换。

| 轴 | 取值与频率（k/37） | 备注 |
|---|---|---|
| 信源 | image 27，text 7，video 3，speech 3，多视角 1，抽象信源 1 | 图像占绝对多数；视频、语音、点云、传感数据、控制状态都少 |
| 任务 | reconstruction 31，classification 10，segmentation 3，retrieval 3，recognition 2，VQA 2 | "语义"大多仍落在重建；纯任务型（不重建）只在 task-feature 范式里 |
| 范式 | analog-jscc 17，task-feature 7，digital-jscc 4，separate-learned 3，knowledge-based 3，system-level 2，theory 1 | analog-jscc = 端到端学习、连续值信道符号 |
| 架构 | CNN 24，transformer 11，attention 8，GAN 5，VAE 3，Swin 3，MLP 3，diffusion 2，LLM 2，VQ 2，hyperprior 2，RL 2 | 2023 年后 transformer / 生成模型增多 |
| 信道 | AWGN 27，Rayleigh 23，MIMO 4，OFDM 4，Rician 4，feedback 2，erasure 1，抽象 1 | 只有 AWGN 的 9/37；MIMO 或 OFDM 合计 6 篇 |
| 自适应 | SNR 13，bandwidth-rate 11，无 10，content 5，resource-allocation 3，CSI 3，feedback-HARQ 2，modulation 2 | "一个模型适配多 SNR / 多速率"是最常见的增量 |
| 训练 | end-to-end 19，multi-stage 14，RL 3，pretrained-frozen 3，无训练 3，adversarial 2 | 多阶段训练常见于带熵模型、生成器或 RL 的系统 |
| 指标 | PSNR 23，MS-SSIM 12，accuracy 12，custom 10，SSIM 6，BLEU 4，LPIPS 4 | 感知类指标（MS-SSIM / LPIPS / FID / KID / CLIP）14/37 |
| 基准 | separate 30，other-learned 17，DeepJSCC 13，own-ablation 8，optimization 4 | 分离式基准几乎是标配 |

二元属性：SNR 失配实验 19/37，报告复杂度 19/37，数字兼容 14/37，硬件验证 0/37，开源代码 1/37。
理论：none 25/37；有理论的 12 篇里 information-bottleneck 3、rate-distortion 3、information-theoretic 2、performance-bound 2、other 2。

## 2. 七条研究线画像

| 研究线（篇数） | 年均引用中位数 | 典型增量 | 代表论文 |
|---|---|---|---|
| image-jscc（10） | 80.9 | new-component 6/10，adaptivity 6/10，new-channel 4/10 | DeepJSCC tccn.2019.2919300；SwinJSCC tccn.2024.3424842；NTSCC jsac.2022.3180802；DeepJSCC-f jsait.2020.2987203；MIMO twc.2024.3422794；OFDM tccn.2022.3151935 |
| modality（6） | 82.95 | new-modality 6/6，adaptivity 2/6 | DeepSC（文本）tsp.2021.3071210；DeepSC-S（语音）jsac.2021.3087240；DeepWiVe、DVST（视频）jsac.2022.3191354、jsac.2022.3221977 |
| task-multiuser（6） | 70.9 | new-task 3/6，multi-user 3/6，theory 2/6 | VIB 边缘推理 jsac.2021.3126087；MU-DeepSC jsac.2022.3191326；U-DeepSC tcomm.2024.3364990 |
| digital（5） | 49.6 | digitalization 5/5，theory 2/5，adaptivity 2/5，robustness 2/5 | DeepJSCC-Q jsait.2022.3231042；masked VQ-VAE twc.2023.3265201；JCM tcomm.2024.3386577；D²-JSCC jsac.2025.3531546 |
| generative（4） | 51.95 | generative-prior 4/4，new-metric 2/4 | GenerativeJSCC jsac.2023.3288243；CDDM twc.2024.3379244；基础模型 + 功率分配 jsac.2025.3559120 |
| networking（3） | 52.8 | system-optimization 3/3，multi-user 2/3 | APPO jsac.2022.3191112；RSMA jsac.2023.3240713；semi-NOMA jsac.2022.3222000 |
| theory-security（3） | 29 | security-privacy 2/3，new-metric 2/3 | 对抗鲁棒 jsac.2023.3288249；隐私 twc.2024.3369170；保真度率失真 tcomm.2023.3274122 |

观察（用于判断"哪里拥挤、哪里空"）：
- **image-jscc 最拥挤**：10 篇里 9 篇是 analog-jscc，增量集中在"换骨干 / 加模块"和"一个模型适配多 SNR、多带宽"。
  在这条线上再做同类增量，必须给出新的机理或新的设定（新信道、新约束）。
- **digital 线的共同主题是"不可微"**：量化、星座映射、信道编码都不可微，5 篇分别用软-硬量化、码本、
  概率建模（Gumbel-Softmax）、比特信道抽象（BSEC）、绕开梯度的理论速率控制来解决。
- **generative 线仍几乎都是模拟传输**：4 篇中只有基础模型那篇（jsac.2025.3559120）接数字比特链路。
- **networking 线把语义模型当黑盒**：语义层用拟合曲线或抽象函数（jsac.2022.3222000 的广义 logistic 回归、
  jsac.2023.3240713 取自前作的精度-计算量函数），或假设语义传输本身无误码（jsac.2022.3191112）；3 篇都没有在噪声信道上端到端验证语义性能。
- **多用户**：带 multi-user 增量的 5 篇（jsac.2022.3191326、twc.2022.3191118、tccn.2023.3326302、jsac.2022.3222000、
  jsac.2023.3240713）里，没有一篇同时做数字兼容和衰落信道下的端到端训练。

## 3. 继承关系（父论文 → 子论文，来自卡片第 10 节"基线"行）

被当作基线的次数：DeepJSCC tccn.2019.2919300 12 次；DeepSC tsp.2021.3071210 4 次；NTSCC jsac.2022.3180802 3 次；
VIB 任务导向 jsac.2021.3126087 3 次；DeepJSCC-Q jsait.2022.3231042、masked VQ-VAE twc.2023.3265201、
GenerativeJSCC jsac.2023.3288243 各 2 次。

```
DeepJSCC (tccn.2019.2919300, 2019)
├─ + 信道反馈 ............ DeepJSCC-f  jsait.2020.2987203
├─ + 分层 / 带宽自适应 .... bandwidth-agile  twc.2021.3090048
├─ + OFDM 多径 ........... tccn.2022.3151935
├─ + 熵模型 / 超先验 ...... NTSCC  jsac.2022.3180802 ──┬─ + 视频条件编码 ... DVST  jsac.2022.3221977
│                                                   ├─ + Swin 骨干 ....... SwinJSCC  tccn.2024.3424842
│                                                   └─ + 数字信道码 ...... D²-JSCC  jsac.2025.3531546
├─ + 星座约束 ............ DeepJSCC-Q  jsait.2022.3231042 ──┬─ + 概率建模 .... JCM  tcomm.2024.3386577
│                                                       └─ + 自适应调制 .. tccn.2024.3422496
├─ + 视频 ................ DeepWiVe  jsac.2022.3191354
├─ + MIMO ................ twc.2024.3422794
├─ + 生成先验 ............ GenerativeJSCC  jsac.2023.3288243 ──┬─ + 信道去噪扩散 ... CDDM  twc.2024.3379244（另以 SwinJSCC 为基线）
│                                                         └─ + 基础模型 ....... jsac.2025.3559120（另以 CDDM 为基线）
├─ + 任务导向 / IB ........ jsac.2021.3126087 ──┬─ + 多设备 DIB ...... twc.2022.3191118
│                                            ├─ + 隐私 ............ twc.2024.3369170
│                                            └─ + MCR² 双任务 ...... twc.2023.3349330
└─ + LLM 多模态 .......... LaMoSC  tccn.2024.3401712
DeepSC (tsp.2021.3071210, 2021)
├─ + 语音 ................ DeepSC-S  jsac.2021.3087240 ── + 识别 / 合成 ... twc.2023.3240969
├─ + 任务未知 / 数据漂移 .. jsac.2022.3221991
└─ 语义速率 → 多址 ........ semi-NOMA  jsac.2022.3222000
masked VQ-VAE (twc.2023.3265201) ── + 统一多任务 ... U-DeepSC tcomm.2024.3364990
                               └─ + 物理层对抗攻击 . jsac.2023.3288249
```

用法：找到用户 idea 最近的父节点，看兄弟节点已经加过哪些增量；同一父节点下"还没出现的增量"是候选空位，
但要先用 `landscape.md` 和实时检索确认语料外没人做过。
