# 语义通信 / JSCC 卡片的附加部分

语义通信子语料（`corpus/semcom/selected.csv`）的卡片 = 通用卡片（`pipeline/card_template.md` 的 YAML 头 + 正文 1–9 节）
\+ 下面的 `semcom:` 块 + 正文第 10 节。新卡片存 `corpus/semcom/cards/<JOURNAL>_<doi 后缀>.md`；
主语料里已有卡片的论文（`has_main_card = 1`）直接在原卡片里补这两部分，不另建卡片。

`auto.domain` 抄提取器输出的 `domain` 计数（每个术语出现的句子数），只作参考；`semcom:` 下的字段要读正文后人工判断，
拿不准写 `unclear`。词表外的取值可以用（如 `adversarial-training`、`MISO`），但同义写法要在
`pipeline/aggregate_semcom.py` 的 `ALIAS` 里归并。

```yaml
semcom:
  category: image-jscc        # selected.csv 的类别：image-jscc / digital / generative / modality / task-multiuser /
                              # networking / theory-security
  source: [image]             # image / video / text / speech / multimodal / feature（边缘推理的中间特征）/ point-cloud /
                              # sensing-data / control-state / generic
  task: [reconstruction]      # reconstruction / classification / retrieval / detection / segmentation / QA / translation /
                              # recognition（ASR 等）/ multi-task / generation / control / estimation
  paradigm: analog-jscc       # analog-jscc（端到端学习，连续值信道符号）/ digital-jscc（量化 / 码本 / 星座约束）/
                              # separate-learned（学习型信源编码 + 传统信道编码）/ task-feature（只传任务相关特征）/
                              # knowledge-based（知识库 / 知识图谱 / 概率语义）/ system-level（把语义模型当黑盒的资源分配等）/
                              # theory（信息论 / 率失真刻画）
  architecture: [CNN]         # CNN / transformer / swin / VAE / VQ / GAN / diffusion / LLM / GNN / RNN / MLP / none
  channel: [AWGN, Rayleigh]   # AWGN / Rayleigh / Rician / MIMO / OFDM / multi-user / broadcast / relay / feedback /
                              # erasure-packet / interference / real-measured / abstract（只有速率或误码率模型）
  adaptivity: [SNR]           # SNR / bandwidth-rate / CSI / content（按内容分配速率）/ task / modulation / none
  training: [end-to-end]      # end-to-end / multi-stage / pretrained-frozen / RL / federated / fine-tune / none
  metrics: [PSNR, MS-SSIM]    # PSNR / SSIM / MS-SSIM / LPIPS / FID / accuracy / BLEU / sentence-similarity / PESQ / WER /
                              # mIoU / semantic-similarity / AoI / energy / latency / sum-rate / custom
  datasets: [CIFAR-10, Kodak]
  baselines: [separate, DeepJSCC]
                              # separate（JPEG/BPG/H.264/文本压缩 + LDPC/polar/turbo/容量界）/ DeepJSCC / DeepSC /
                              # NTSCC / own-ablation / optimization（随机、等分配等资源分配基准）/ other-learned
  snr_mismatch_test: true     # 训练与测试 SNR 不同的鲁棒性实验
  complexity_reported: true   # 报告参数量、FLOPs、运行时间或编解码时延
  digital_compatible: false   # 输出能否直接接到现有数字链路（比特或标准星座）
  hardware_validation: false  # 有 SDR / 原型 / 空口实验
  theory: none                # none / information-theoretic / rate-distortion / information-bottleneck / optimization /
                              # convergence / game / performance-bound
  idea_delta: [new-component] # 相对所继承基线的增量（可多选）：new-paradigm（首次把端到端学习 / 新范式用于该问题）/ new-modality / new-component（网络模块或结构）/
                              # new-channel（新信道或新系统设定）/ new-task / digitalization / adaptivity / generative-prior /
                              # theory / system-optimization / security-privacy / multi-user / knowledge-base / new-metric /
                              # feedback-retransmission / robustness
  builds_on: [DeepJSCC]       # 直接继承或改造的基线方法（用论文里的名字）
  open_problems_n: 3          # 第 10 节列出的开放问题条数
```

## 10. Idea 拆解（正文最后一节）
- **基线**：本文建立在哪个已有方法 / 系统之上（名称 + DOI 或引用号）。
- **增量**：一句话说清本文改了什么（对应 `idea_delta`）。
- **为什么有效**：作者给出的机理解释（摘一句原文，≤ 30 词）。
- **证据**：最关键的一张图或一个数字（数据集、指标、对比对象、增益）。
- **弱点**：评测或设定上的薄弱处（只用 AWGN、没有 SNR 失配、没有复杂度、基准不全、只在小图上验证等）。
- **开放问题**：作者自己写的局限与未来工作（摘原句，≤ 30 词），再加上从弱点推出的、作者没写的问题（标"推断"）。
