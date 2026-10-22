# 图、表与算法框

统计口径：72 篇研究论文；DOI 省略 `10.1109/`。

## 1. 数量

| 指标 | 全部 | TWC | JSAC | TCOM | 2016–2018 | 2019–2021 | 2022–2025 |
|---|---|---|---|---|---|---|---|
| 图 | 10 [8–12] | 11 | 10 | 10 | 9 | 10 | 11.5 |
| 表 | 1 [0–2] | 1.5 | 1 | 1 | 1.5 | 1 | 1 |
| 算法框 | 2 [1–3] | 2 | 2 | 2 | 2 | 2 | 2 |

- 中间 80% 的论文有 7–14 张图（最少 3 张，最多 17 张）。理论很重的论文可以只有很少的结果图（jsac.2020.3000803：4 张图、69 个公式）。
- 一般结构：1–3 张示意图（系统、协议 / 帧结构、算法流程），其余是结果图。

## 2. Fig. 1

| Fig. 1 的角色 | 全部 | TWC | JSAC | TCOM | 2022–2025 |
|---|---|---|---|---|---|
| 系统模型图 | 45/72 | 17/24 | 10/24 | 18/24 | 9/24 |
| 新架构 / 硬件图 | 16/72 | 6/24 | 6/24 | 4/24 | 8/24 |
| 框架 / 流程图 | 7/72 | 0 | 5/24 | 2/24 | 5/24 |
| 场景示意 | 3/72 | 0 | 3/24 | 0 | 1/24 |
| 结果图 | 1/72 | 1/24 | 0 | 0 | 0 |

- 默认画系统模型图：节点、链路、关键变量（信道符号、轨迹、部署位置），放在引言末或系统模型节开头。
- 提出新架构或新硬件时，Fig. 1 画架构图，并尽量在引言就给出（如 twc.2024.3492195 的 6DMA 概念图，配新旧架构对比表）。
- 学习类论文常用框架图（JSAC 5/24），显示数据流和各个网络模块。
- 例句（caption）：
  - "Illustration of the LEO satellite communication system setup."（jsac.2020.3000803）
  - "Network model including a UAV, downlink users and D2D."（twc.2016.2531652）
  - "Illustration of networked ISAC for communicating with authorized UAVs and monitoring of unauthorized objects in 3D space."（tcomm.2025.3541027）

## 3. 结果图

- **横轴**（出现篇数）：迭代次数 27/72，SNR 17/72，用户数 17/72，发射功率 14/72，反射 / 天线元件数 14/72，距离或位置 11/72，天线数 8/72，时间 7/72，CDF 6/72，SINR 门限 6/72，轨迹图 5/72，CSI 误差 5/72，训练回合 4/72。
- **默认图组**（按出现顺序）：
  1. 收敛曲线（用 AO / BCD / SCA / MM / FP 等迭代算法的 37 篇中有 25 篇画了迭代或训练曲线）；
  2. 主性能 vs 发射功率或 SNR，所有基准同图；
  3. 主性能 vs 规模（用户数、元件数、天线数）；
  4. 与本文设计相关的参数（部署位置、距离、门限、权重）；
  5. 鲁棒性（CSI 误差）或可视化（轨迹、波束图、热图）。
- 权衡类结论用双指标曲线（如时延-成本、覆盖-时延、感知-通信），而不是两张独立的图。
- 同一设定的两个指标可用 (a)/(b) 子图并排（如 tcomm.2019.2956472 的功率 + 平均队列长度）。

## 4. Caption

| 风格 | 全部 | TWC | JSAC | TCOM |
|---|---|---|---|---|
| 短标签（"Y versus X."） | 40/72 | 17/24 | 12/24 | 11/24 |
| 描述型（交代比较对象、参数、图例） | 31/72 | 7/24 | 12/24 | 12/24 |
| 自含结论 | 1/72 | 0 | 0 | 1/24 |

- 短标签格式："[纵轴量] versus [横轴量][, 固定参数]."
  - "Achievable WSR versus the location of the IRS x_IRS."（twc.2020.2990766）
  - "WSR versus N, when P_T = 5 dBm."（twc.2020.2970061）
  - "Coverage probability vs. UAV altitude."（twc.2016.2531652）
- 描述型：写出比较对象和关键参数，读者不看正文也能知道这张图怎么来的。
  - "The performance of the approximate Gram-Schmidt hybrid precoding design in Algorithm 2 for different codebook sizes, compared with the unconstrained SVD solution, …"（tcomm.2016.2549517）
  - 解释图例："… the carmine '+' denote the authorized UAVs location of this time slot, and the arrow associated with each authorized UAV and GBS correspond to their association relationship."（tcomm.2025.3541027）
- 自含结论（少见，可用于关键结果图）："The proposed JSC optimization provides a significant gain for sensing while satisfying the best communication SINR."（tcomm.2024.3490740）
- TWC 偏短标签；JSAC、TCOM 两种各半。同一篇论文内保持一种风格。

## 5. 正文如何引用图

- 句首 "Fig. N shows / illustrates / plots / depicts / compares …"：58/72。用 "Fig." 缩写，句首也可写 "Fig."；全拼 "Figure" 的少见（如 twc.2016.2531652）。
- 每张结果图至少一段分析：图展示什么 → 现象 → 原因 → 启示（例句见 `phrasebank.md` 第 14 节）。

## 6. 表

- 表的中位数为 1 张（TWC 1.5）。常见用途：
  - 仿真参数表：28/72（TWC 12/24，JSAC 10/24，TCOM 6/24）；
  - 记号 / 变量表：13/72（JSAC 8/24），如 jsac.2020.3000803 的 "Variable list"；
  - 引言里的新旧对比表（≥ 5/72），如 twc.2024.3492195 对比 FPA / FAS / 6DMA；
  - 复杂度对比表，如 twc.2020.2990766、twc.2024.3492195；
  - 结果汇总表：用一个数字概括增益（如 jsac.2022.3180802 的 BD-rate 表），或开销汇总（如 tcomm.2016.2549517 的反馈开销表）。
- 表题为 "TABLE" + 罗马数字 + 名词短语，如 "TABLE I Simulation Parameters"、"TABLE I Variable list"（jsac.2020.3000803）。

## 7. 算法框

- 中位数 2 个 [1–3]。迭代算法给出初始化、循环体、收敛判据、输出；主算法调用子算法时分开写（如 twc.2020.2970061 有 4 个算法框）。
- 算法框后用一段话给出收敛性和复杂度（见 `methodology.md` 第 4 节）。

## 8. 综述 / 教程（n = 8）

- Fig. 1 多为框架或全景图（6/8）；可以有一张"论文结构图"（jsac.2022.3156632、tcomm.2022.3171800）。
- 表格用于汇总已有工作（相关综述、代表性工作、测试床、产业样机），每个技术节可配一张汇总表（tcomm.2021.3051897）。
- 复用他人图片时在 caption 写明来源（"reproduced from [5]"，jsac.2020.3007211）。
