# 评测清单：数据集、指标、基准、信道与公平性

统计口径：37 篇研究论文（`corpus/semcom/summary.md` 第 2、3、8 节）。"≥k/37" 为卡片弱点文字的关键词计数（下限）。

## 1. 清单（逐项打勾）

| 项 | 语料里的做法 | 建议 |
|---|---|---|
| 信道 | AWGN 27/37，Rayleigh 23/37，MIMO 4/37，OFDM 4/37，Rician 4/37；只有 AWGN 9/37；弱点里提到"只有 AWGN / 信道受限"≥12/37 | 至少 AWGN + 一种衰落；声明 CSI 假设（完美 / 估计误差） |
| SNR 失配 | 19/37 做了训练 SNR ≠ 测试 SNR 的实验 | 画"单一 SNR 训练、全 SNR 测试"曲线，并与"每个 SNR 单独训练"的包络比较 |
| 带宽 | 横轴含带宽比 / CBR / 压缩比 14/37；SNR 横轴 28/37 | 给出 CBR（信道使用数 / 信源维度）定义；PSNR vs SNR 与 PSNR vs CBR 两类图都要有 |
| 数据集（图像） | CIFAR-10 21/37，Kodak 12/37，ImageNet 12/37，MNIST 7/37；图像 / 视频论文中 20/30 用了高分辨率数据集 | 小图（CIFAR）+ 高分辨率（Kodak、CLIC、DIV2K）各一；训练集与测试集分开（常见：ImageNet / Open Images 训练、Kodak 测试） |
| 数据集（其他模态） | 文本 Europarl 2/37；语音 LJSpeech、Edinburgh；视频 Vimeo-90k / UCF101 训练，HEVC / UVG 测试 | 沿用该模态的标准测试集 |
| 指标 | PSNR 23/37，MS-SSIM 12/37，accuracy 12/37，LPIPS 4/37；感知类（MS-SSIM / LPIPS / FID / KID / CLIP）14/37 | 失真 + 感知 + 任务指标中至少两类；生成式方法必须有感知指标 |
| 基准 | 分离式 30/37，其他学习方法 17/37，DeepJSCC 13/37，消融 8/37，资源分配基准 4/37；基准数中位数 3（0–6） | 分离式（实际 LDPC / 极化码 + 容量界）+ 最强学习方法 + 消融 |
| 复杂度 | 报告参数量 / FLOPs / MACs / 运行时间 19/37；弱点里"无复杂度 / 时延分析"≥15/37 | 参数量 + FLOPs（或 MACs）+ 编解码时间；生成式方法报采样步数与时延 |
| 数字兼容 | 14/37 的输出可直接接到数字链路 | 模拟方案在引言或讨论里交代部署路径 |
| 硬件 / 空口 | 0/37 | 有条件就做 SDR 实验，是明确的差异化点 |
| 开源 | 1/37（SwinJSCC tccn.2024.3424842） | 开源能提高可复现性，也是差异化点 |
| 理论 | `code.theory_role` 非 none 16/37（supporting 12，central 4）；`semcom.theory` 非 none 12/37 | 至少一个可检验的理论结论或机理分析 |

## 2. 基准怎么搭（卡片里的做法）

- **分离式基准**：信源用 JPEG / JPEG2000 / BPG（图像）、H.264 / H.265（视频）、Huffman / Brotli（文本）；
  信道用实际 LDPC（遍历码率与调制取最优包络，如 DeepJSCC-Q jsait.2022.3231042、DVST jsac.2022.3221977）
  加容量界（理想信道码，作为分离方案的上界）。只给容量界、不给实际码，会让模拟 JSCC 的优势被低估或被质疑。
- **学习型基准**：同一骨干、同样信道使用数；必要时复现（jsac.2023.3288249 复现了未开源的 PGM；twc.2022.3191118 按相同设置复现了已有方法）。
- **"每点单训"上界**：自适应类方法要和"每个 SNR / 速率单独训练的模型"比，才能说明单模型的代价有多小。
- **消融**：去掉每个新模块各一次，保持参数量接近；骨干替换类工作要有同参数量对照。
- **两步式结果**：DVST 用 BD-rate 汇总带宽节省，RL-ASC 借鉴 BD-rate 提出 BD-mIoU——一个"单数字"汇总指标便于摘要和结论引用。

## 3. 公平性陷阱

1. **信道使用数不一致**：比较必须在相同 CBR（或相同 bpp + 相同信道码率换算）下进行。RL-ASC 的写法：
   "… the proposed RL-ASC encodes the image at a bitrate 0.33 bpp while the baselines encode the image at a bitrate equal to or higher than 0.33 bpp."（jsac.2022.3221999）
2. **训练设置不一致**：每个 SNR 重训的系统要说明；CDDM 的写法：
   "It is worth emphasizing that in the event of a change in channel SNR, all systems undergo retraining to optimize their performance under the specific SNR condition."（twc.2024.3379244）
3. **指标偏向**：新方法用感知 / 语义指标训练，在 PSNR / SSIM 上可能输给为 PSNR 优化的基准——要坦白并解释。
   "As shown in Fig. 11, the baselines achieve better performance since they are optimized with the PSNR or SSIM metric."（jsac.2022.3221999）
4. **信息泄漏到接收端**：接收端用了额外边信息（共享照片、知识库、LLM 生成文本）时，要计入其开销或说明其一次性。
5. **完美 CSI / 完美同步**：多数论文假设完美 CSI；至少加一组估计误差实验（CDDM、IB 边缘推理都做了）。
6. **只在窄分布上验证**：人脸（GenerativeJSCC）、街景（RL-ASC）、MNIST 级小图——要么补通用数据集，要么在标题 / 摘要里限定场景。
7. **抽象语义模型**：系统级论文用拟合曲线代替语义模型时，至少用一个真实模型做端到端验证（networking 线 3/3 篇缺这一步）。

## 4. 机理证据（高引论文几乎都有一张"为什么有效"的图）
- 速率 / 带宽分配可视化：NTSCC（jsac.2022.3180802）、DVST（jsac.2022.3221977 最高熵潜变量）。
- 星座 / 码字使用分布：DeepJSCC-Q（jsait.2022.3231042）、JCM（tcomm.2024.3386577）。
- 注意力或权重可视化：MIMO JSCC（twc.2024.3422794）、视频会议 CSI 权重（jsac.2022.3221968）。
- 相关矩阵 / 特征可视化：DeepMA（tccn.2023.3326302）、IB 边缘推理 t-SNE（jsac.2021.3126087）。
- 理论假设的数值验证：CDDM 用 Monte Carlo 验证假设（twc.2024.3379244）、D²-JSCC 验证特征分布近似（jsac.2025.3531546）。

## 5. 标准结果节结构（image-jscc / digital / generative 线最常见）
1. Setup：数据集（训练 / 测试）、基准（编号或命名）、指标（为什么选这些）、训练细节（优化器、学习率、轮数、SNR 采样范围）。
2. 主结果：指标 vs SNR（AWGN、衰落各一组）→ 指标 vs CBR。
3. 鲁棒性：SNR 失配、信道估计误差、调制阶数 / 数据集失配。
4. 机理：可视化 + 消融。
5. 代价：参数量、FLOPs、时延；与基准对比的表。
6. 视觉 / 样例对比（图像重建、句子、语音谱图）。
