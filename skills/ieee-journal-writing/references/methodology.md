# 科研方法：问题、求解、理论、仿真

统计口径：72 篇研究论文；"≥k/72" 为卡片笔记关键词计数（下限）。DOI 省略 `10.1109/`。

## 1. 问题类型

| 类型 | 全部 | TWC | JSAC | TCOM |
|---|---|---|---|---|
| 非凸连续优化 | 30/72 | 13/24 | 8/24 | 9/24 |
| 混合整数（MINLP） | 12/72 | 3/24 | 4/24 | 5/24 |
| 纯分析（性能分析 / 极限） | 9/72 | 3/24 | 2/24 | 4/24 |
| 学习方法 | 9/72 | 1/24 | 7/24 | 1/24 |
| 估计（信道 / 参数） | 5/72 | 2/24 | 0/24 | 3/24 |
| 随机 / 长期优化 | 3/72 | 0/24 | 2/24 | 1/24 |
| 组合优化 | 2/72 | 0/24 | 1/24 | 1/24 |
| 凸优化 | 2/72 | 2/24 | 0/24 | 0/24 |

- 年代变化：2016–2018 年段 MINLP 最多（8/24，计算卸载、资源分配类）；2019–2025 年段非凸连续优化各 12/24
  （RIS、波束成形、可移动天线类）；学习方法从 1/24 增加到 5/24。
- 学习方法高度集中在 JSAC（DNN 9/24，DRL 6/24），TWC 和 TCOM 各只有 1 篇。

## 2. 求解路线

**方法出现率**：closed-form 33/72，AO 19/72，SCA 16/72，reformulation 13/72，heuristic 12/72，SDR 12/72，
DNN 10/72，decomposition / bisection / relaxation / penalty 各 9/72，Lagrangian dual / BCD / FP / gradient 各 8/72，
DRL 7/72，bound-surrogate 5/72，MM / exhaustive search / manifold 各 4/72，stochastic geometry / Lyapunov / KKT / WMMSE 各 3/72。

**组合**：每篇用 3 种 [2–4] 技术。最常见的搭配是 AO + 闭式解 10/72，AO + SCA 8/72，闭式解 + 分解 7/72，AO + SDR 7/72，SCA + SDR 6/72，FP + SCA 5/72。

**路线 A：分块交替（AO / BCD）+ 子问题各个击破**（用 AO 或 BCD 的共 26/72，最常见）
1. 写出 (P1)，声明非凸及原因（变量耦合、单模约束、整数变量）。
2. 按变量分块；每块要么有闭式解（拉格朗日 / KKT + 二分搜索乘子），要么用 SCA（一阶 Taylor 下界）、SDR（加高斯随机化或构造秩一解）、MM、流形优化。
3. 目标函数单调不减且有上界，从而收敛；给出每次迭代的复杂度。
- 例：tcomm.2025.3541027（关联变量利用结构求最优 → 波束 SCA + SDR，用 Proposition 证明可构造秩一解 → 轨迹一阶 Taylor + 信任域）；
  twc.2020.2990766（BCD：预编码由拉格朗日乘子 + 二分搜索得闭式解，相位用 MM 或复圆流形）；
  twc.2020.2970061（FP 把和对数比问题拆成四块 → 非凸 BCD → prox-linear 更新避免矩阵求逆）。
- 写法："In fact, AO is a widely applicable and empirically efficient approach for handling optimization problems involving coupled optimization variables."（jsac.2020.3007043）

**路线 B：最优解 + 低复杂度次优解（≥ 5/72）**：先给全局最优（单调优化、分支定界、穷举）作为性能基准，再给多项式复杂度的次优算法，并在仿真里比较两者的差距。
- 例：tcomm.2017.2650992（单调优化求最优 + SCA 次优）、tcomm.2019.2958916（最优解 + successive refinement）、twc.2016.2633522、twc.2023.3338626、tcomm.2017.2787700。
- "To reduce the computational complexity for the optimal solution, we further propose a low-complexity successive refinement algorithm …"（tcomm.2019.2958916）

**路线 C：先研究特例得到结构，再推广（≥ 11/72）**：先研究单用户 / 单小区 / 简单轨迹，拿到闭式解或最优结构，再用这个结构设计一般情形的算法。
- "In this section, we consider the special case with a single user to draw important insights into the beamforming design."（tcomm.2020.3001125）
- 例：tcomm.2016.2549517 由最优基带预编码的分解结构推出码本设计与"只反馈 RF 索引"的结论；jsac.2020.3000803 由上界取得条件（信道方向正交）设计用户分组。

**路线 D：解析 / 极限分析（纯分析 9/72；定理是主要贡献的 19/72）**：随机几何下的覆盖与中断分析（twc.2016.2531652、jsac.2016.2549378）、调度策略的收敛分析（tcomm.2019.2944169）、闭式设计 + 渐近界（jsac.2020.3000803）、路损建模 + 实测验证（twc.2020.3024887）。仿真的首要作用是验证解析式。

**路线 E：长期随机优化用 Lyapunov（3/72）**：长期平均约束 → 虚拟队列 → 漂移加罚 → 每时隙求解（jsac.2016.2611964、jsac.2018.2869954、tcomm.2019.2956472）。

**路线 F：学习方法（9/72，集中在 JSAC 和 2022–2025 年段）**
- DRL：把问题写成 MDP，逐项定义智能体、状态、动作、奖励（约束违反用惩罚项），再说明为什么选这个算法（twc.2022.3153316、jsac.2018.2864373、jsac.2023.3240707）。
- 学习方法也要与优化方法对照，并承认学习方法不保证最优："Nevertheless, the optimality of the DRL-based approaches is not guaranteed, which is required to be evaluated by the optimization approaches."（jsac.2023.3240707）
- DNN / 语义通信：用变分或信息论框架给出训练目标，交代数据集、网络结构、训练超参数，并做消融实验（jsac.2022.3180802、jsac.2021.3087240、tcomm.2024.3364990）。

## 3. 理论结果

- 理论的作用：supporting 36/72（命题、引理服务于算法），central 19/72（定理本身就是主要贡献），none 17/72。2022–2025 年段 none 为 10/24。
- 定理类陈述（theorem / lemma / proposition / corollary）每篇中位数 2.5 个，18/72 篇没有。各类出现率：proof 51/72，remark 33/72，lemma 31/72，proposition 30/72，theorem 29/72，corollary 8/72，definition 7/72。
- 用 Remark 讨论定理的含义、特例、与已有结果的关系（33/72）；每个定理后都要有一句解读（"Theorem 1 reveals that …"，例句见 `phrasebank.md` 第 13 节）。
- 证明位置：附录 21/72，附录 + 正文 14/72，正文 16/72，无 20/72；引用技术报告 1/72（jsac.2018.2869954）。TCOM 放附录或附录 + 正文的最多（16/24）。

## 4. 复杂度与收敛

- 复杂度分析 45/72；收敛性论证 30/72（TWC 13/24，JSAC 7/24）。两者都有 26/72，都没有 23/72（多为纯分析或学习论文）。
- 复杂度：给出每次迭代的 O(·) 和总复杂度；需要时用表格与基准方法对比（如 twc.2020.2990766 的 Table I、twc.2024.3492195 的 Table III）。复杂度更高时要坦白并说明换来了什么。
- 收敛：交替优化类用"目标值单调不减 + 有上界"论证；只画迭代曲线不算收敛分析，但迭代曲线本身很常见（27/72）。
- 用最优解或上界衡量次优算法的差距："Despite its low-complexity, the proposed algorithm is illustrated to achieve a similar performance compared with the optimal hybrid precoding design …"（tcomm.2016.2549517）

## 5. 仿真设置

- **参数**：参数表 28/72（TWC 12/24，JSAC 10/24，TCOM 6/24），其余写在仿真节第一段；注明参数来源（"almost the same as those in [24]"，twc.2020.2970061；路损按 3GPP）和蒙特卡洛平均次数。
- **基准**：每篇 3 个 [2–4]；描述性命名 55/72（"Random phase"、"Without RIS"、"Fixed power"），缩写命名 15/72（2022–2025 年段 8/24）。用 bullet 或编号逐个定义。
- **基准的类型**（组合使用）：
  - 上界或理想参照：最优解、完美 CSI、genie-aided、无干扰（≥ 19/72）；
  - 去掉本文关键设计的版本（无 RIS、随机相位、固定位置、固定功率、固定高度）；
  - 已有文献的代表方法，标出引用；
  - 学习论文：消融变体（去掉某模块）。
- **公平比较**要写明对齐了什么（总功率、物理孔径、比特率），例句见 `phrasebank.md` 第 15 节。
- **横轴**：iterations 27/72，SNR 17/72，用户数 17/72，发射功率 14/72，反射 / 天线元件数 14/72，距离或位置 11/72，天线数 8/72，时间 7/72，CDF 6/72，SINR 门限 6/72，轨迹图 5/72，CSI 误差 5/72。
  典型组合：收敛曲线 + 性能 vs 发射功率 / SNR + 性能 vs 规模（用户数、元件数、天线数）+ 一个与本文设计相关的参数（位置、距离、门限）+ 鲁棒性（CSI 误差）。
- **实测 / 原型**：4/72（jsac.2017.2680898 用真实移动数据，jsac.2019.2904348 有实验平台，tcomm.2022.3231893 有原型测量，twc.2020.3024887 有路损实测）。
- **公开代码**：1/72（tcomm.2020.2987311："All the simulation results can be reproduced using the Matlab code and data files available at: …"）。

## 6. 结果分析

- 每张图的分析按"图展示什么 → 现象 → 原因（"This is because"，39/72）→ 设计启示"组织；对比基准时说明增益从哪里来。
- 主动给出设计建议或工程洞见（卡片中提到 insight 的论文 ≥ 28/72）：
  "Furthermore, the location of IRS should be carefully chosen to guarantee a favourable BS-IRS link and IRS-user link."（twc.2020.2990766）
- 反直觉的结果要单独解释（≥ 4/72），例句见 `phrasebank.md` 第 14 节。
- 权衡曲线（"trade-off" 43/72）：给出一个指标随另一个指标变化的曲线，例如时延-代价（jsac.2018.2869954）、覆盖-时延（twc.2016.2531652）、感知-通信（tcomm.2025.3541027）。
- 方案不占优的区域也要报告并解释："As shown in Fig. 11, the baselines achieve better performance since they are optimized with the PSNR or SSIM metric."（jsac.2022.3221999）
