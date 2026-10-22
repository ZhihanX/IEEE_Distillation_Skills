# Idea 怎么提出、怎么在引言里立住

统计口径同 `structure.md`：72 篇研究论文；"≥k/72" 为卡片笔记关键词计数（下限）。例句后为 DOI 后缀。

## 1. 空白类型

| 类型 | 论文数 | 含义 |
|---|---|---|
| limitation | 45/72 | 已有方法有具体缺陷：假设过强、复杂度高、只覆盖简单设定 |
| new-scenario | 27/72 | 新场景还没人研究，或已有结论在新场景下不成立 |
| practicality | 17/72 | 已有工作用了不现实的假设（完美 CSI、理想相移、连续相位） |
| combination | 16/72 | A、B 各有研究，但还没有结合 |
| new-architecture | 16/72 | 提出新硬件 / 新架构（可移动天线、STAR-RIS、夹持天线） |
| theory-gap | 11/72 | 缺少解析结果、最优结构或基本性能极限 |
| tool-transfer | 10/72 | 把其他领域的工具引入通信（DRL、联邦学习、LLM、EVT） |
| unification | 4/72 | 用一个框架统一多个问题或多种任务 |
| comparison | 3/72 | A 与 B 孰优尚无定论 |
| scalability | 1/72 | 已有方案无法扩展到大规模 |

- **组合**：62/72 篇同时用两种空白，8/72 用三种，只用一种的仅 2/72。最常见的组合：
  limitation + new-architecture 9/72，limitation + combination 8/72，limitation + new-scenario 8/72，
  limitation + tool-transfer 5/72，limitation + practicality 5/72。
- **年代变化**：2016–2018 年段 new-scenario（12/24）和 combination（9/24）多；2022–2025 年段 limitation（18/24）
  和 new-architecture（9/24）多。新硬件论文的写法见第 2 节 B、F。
- **期刊差异**：JSAC 的 new-scenario（12/24）、combination（8/24）、tool-transfer（6/24）较多；TWC 的 new-architecture 较多（8/24）。

**每类空白的写法与例句**

- limitation：点出已有工作的设定上限。
  "However, the above-mentioned papers only studied the single-cell scenario, whilst there is a paucity of investigations on the multicell scenario in the existing literature."（twc.2020.2990766）
- new-scenario：明确说"这个场景还没被研究"。
  "The research on using terrestrial networked ISAC systems to support LAE has not been investigated in the literature yet."（tcomm.2025.3541027）
- practicality：先指出整批文献共享的理想假设，再说它不现实。
  "However, the above prior works as well as many others … on IRS have all assumed the ideal phase shift model with full signal reflection, …"（tcomm.2020.3001125）
- combination：说清是哪几项技术"各自有研究、还没放在一起"。
  "However, at present, most of the existing work on ultra dense network and mobile edge computing are separate."（jsac.2018.2815360）
- new-architecture：先讲旧架构的根本局限，再提出新架构。
  "To overcome this limitation, we propose a new antenna architecture, namely movable antenna (MA), for exploiting the DoFs in the continuous spatial domain more efficiently."（twc.2023.3330887）
- theory-gap：指出"已有工作有算法、没有洞见或极限"。
  "Prior work on MECO resource allocation focuses on complex algorithmic designs and yields little insight into the optimal policy structures."（twc.2016.2633522）
- tool-transfer：说明为什么这个工具适合，以及为什么不能直接搬。
  "However, it is not straightforward to solve the UAV control problem using DRL."（jsac.2018.2864373）
- comparison：把"孰优"写成本文要回答的问题。
  "Thus, as far as EE is concerned, it is not clear if a RIS-based system is more convenient than traditional AF relay-based systems."（twc.2019.2922609）

## 2. 引言论证链（常见套路）

**A. 归纳共同假设 → 本文打破（≥ 15/72）**。先概括一批工作的共同前提，再说明这个前提限制了什么。
"Although the above MIMO technologies have been extensively studied in the literature, they are all based on the traditional fixed-position antennas (FPAs) that cannot change positions once deployed."（twc.2024.3492195）
"The URLLC aspects of this prior art … are captured by either improving the average latencies or imposing a probabilistic constraint to maintain small queue lengths."（tcomm.2019.2956472）

**B. 代价链：已有技术 → 代价 → 新技术（≥ 19/72）**。先承认主流方案有效，再给出它的代价（硬件、功耗、复杂度、时延，最好带数字），引出替代方案。
"However, escalating signal processing complexity, increased hardware costs as well as high power consumption are incurred by …"（twc.2020.2990766）
"As a remedy, intelligent reflecting surface (IRS) has been proposed as a revolutional technique of …"（twc.2020.2990766）
带数字的代价："… whose energy consumption is a large part (about 250 mW per RF chain [9]) of the total energy consumption at mmWave frequencies …"（jsac.2016.2549418）

**C. 新挑战三连 First / Second / Third（≥ 19/72）**。说明新场景或新架构为什么让问题变难，每个挑战对应后文一个设计。
"However, employing the SAGIN in IoT computing offloading introduces several challenging issues."（jsac.2019.2906789）
"Compared to the previous studies …, the presence of an aerial UAV base station along with D2D links introduces new challenges."（twc.2016.2531652）

**D. 不能直接套用（≥ 14/72）**。已有方法或结论为什么不能直接用于本文问题，要给出具体原因（约束变了、模型变了、耦合更强）。
"However, the above results for fixed-wing UAVs cannot be applied for rotary-wing UAVs, due to their fundamentally different mechanical designs and hence drastically different propulsion energy models."（twc.2019.2902559）
"Existing algorithms in [14]–[19] cannot be straightforwardly applied to address these challenges."（jsac.2023.3287540）

**E. 开放问题 / 设问（≥ 12/72）**。把空白写成一个读者也想知道答案的问题，本文负责回答。
"Therefore, it remains unknown whether mobile UAVs are still able to provide throughput gains over static UAVs/ground BSs, when …"（tcomm.2018.2865922）
"Based on the proposed protocol and the considered stochastic geometric model, a natural question arises: which near NOMA user should help which far NOMA user?"（jsac.2016.2549378）

**F. 例子驱动（≥ 16/72）**。用一个具体场景或数字让问题"看得见"，常配 Fig. 1。
"… whenever a mobile user moves to a new cell, its requested content may not be available at the new base station and, consequently, the users cannot be serviced properly."（jsac.2017.2680898）
"Imagine a coverage area with many wireless access points that cooperate to jointly serve the users, instead of creating autonomous cells."（tcomm.2020.2987311）

**G. 现象 → 根因 → 方案**。先描述可观测的性能现象，再归因，方案直接对准根因（jsac.2022.3180802）。
"This phenomenon stems from the inherent defect of standard deep JSCC that cannot identify the source distribution …"（jsac.2022.3180802）

**H. 形似神异（≥ 7/72 写明与相近问题 / 技术的本质区别）**。问题看起来像已有问题，要说明本质差别在哪里。
"The formulated problem looks mathematically similar to the WSR maximization problem in the hybrid digital/analog precoding …"（twc.2020.2970061）
"It is worth noting that the proposed IRS differs significantly from other related existing technologies such as …"（twc.2019.2936025）

**I. 收束到本文**：用一句话把上面的论证接到 "In this paper"（"motivates this work" 类句式 ≥ 10/72）。
"However, the research on IRS design … is still in its infancy, which thus motivates this work."（twc.2019.2936025）
"Motivated by such an open question, we study in this paper …"（tcomm.2018.2865922）

**选择建议**（按空白类型）：
- limitation / practicality → A + D + I
- new-architecture → B + C + I，并在引言给出新旧架构对比表（如 twc.2024.3492195 的 Table I；引言含对比表 ≥ 5/72）
- new-scenario → F + C + D
- theory-gap / comparison → E + I
- tool-transfer → B（旧工具的局限）+ D（新工具不能直接用）+ I

## 3. 与最相近工作的区分

- 指出最接近的一两篇工作，逐条写区别："However, it is worth noting that our work substantially differs from and complements to [26] in at least the following three aspects: …"（jsac.2018.2869954）
- 借用已有构件时写清差异："Different from [23] where the codebook is for a specific task with single modality, we design a unified codebook for multimodal data."（tcomm.2024.3364990）
- 预先回应"增量太小"的质疑："While parts of our technical derivations build upon design algorithms proposed for far-field communications, we demonstrate that the incorporation of the near-field characteristics results in fundamentally different beam patterns …"（twc.2022.3158894）
- 声明本文模型是已有模型的推广："6DMA is a general model that includes the existing FAS/2DMA models with antenna position adjustments as special cases."（twc.2024.3492195）
- 扩展自己的会议版或前作时要说明增量（≥ 17/72 提到前作）："This work significantly extends the preliminary work [1]."（jsac.2018.2869954）

## 4. 首创声明

- 出现率：33/72（TWC 13/24，JSAC 14/24，TCOM 6/24；2016–2018 年段 11/24，2019–2021 年段 13/24，2022–2025 年段 9/24）。
- 常见形式：
  - 标准式："To the best of our knowledge, this is the first study of task offloading for mobile edge computing in SD-UDN."（jsac.2018.2815360）
  - 否定式（说"没人研究过"而不是"我们第一"）："To the best of the authors' knowledge, the design of robust and secure IRS-assisted wireless communication systems with multi-antenna eavesdroppers has not been studied in the literature, yet."（jsac.2020.3007043）
  - 弱化式："To our best knowledge, this paper is one of the first comprehensive studies on …"（twc.2017.2751045）；"This paper is a very early attempt to formulate a framework that incorporates …"（jsac.2020.3000835）
  - 带例外："To the best of our knowledge, with the exception of [1], no work has studied the use of federated learning in the context of URLLC."（tcomm.2019.2956472）
  - 实验首创："We report the world's first experimental results that assess and validate the path loss of RIS-assisted wireless communications."（twc.2020.3024887）
- 写法要求：首创的对象必须足够具体（场景 + 问题 + 方法中至少两项），否则不可信；不确定时用否定式或弱化式。

## 5. 标题

- 长度：10 词 [8–12]；2016–2018 年段 10.5，之后 9。
- 结构频率：X-for-Y 42/72，colon-subtitle 22/72，X-with-Y 14/72，X-aided-Y 13/72，X-in-Y 11/72，X-via-Y 7/72，noun-phrase 4/72，question 2/72，versus 2/72，verb-ing 2/72，toward 1/72。只用 X-for-Y 一种结构的有 19/72。
- 常见写法：
  - **目标 + for/in + 系统**："Throughput Maximization for UAV-Enabled Mobile Relaying Systems"（tcomm.2016.2611512）、"Weighted Sum-Rate Maximization for Reconfigurable Intelligent Surface Aided Wireless Networks"（twc.2020.2970061）。
  - **技术 + for + 场景**："Massive MIMO Transmission for LEO Satellite Communications"（jsac.2020.3000803）。
  - **新架构: 建模 + 优化 / 分析**（5/72，均为新器件或实用模型论文）："Modeling and Beamforming Optimization for Pinching-Antenna Systems"（tcomm.2025.3621049）、"6D Movable Antenna Based on User Distribution: Modeling and Optimization"（twc.2024.3492195）。
  - **问题 + ": A … Approach"**（4/72，多为学习方法）："Energy-Efficient UAV Control for Effective and Fair Communication Coverage: A Deep Reinforcement Learning Approach"（jsac.2018.2864373）。
  - **问句 / 对比**（3/72，用于 comparison 或二选一型问题）："Active RIS vs. Passive RIS: Which Will Prevail in 6G?"（tcomm.2022.3231893）、"Channel Estimation for Extremely Large-Scale MIMO: Far-Field or Near-Field?"（tcomm.2022.3146400）、"Cell-Free Massive MIMO Versus Small Cells"（twc.2017.2655515）。
  - **吸睛主标题 + 说明副标题**（2/72）："Caching in the Sky: …"（jsac.2017.2680898）、"Follow Me at the Edge: …"（jsac.2018.2869954）。
- 标题里的限定词最好就是本文相对已有工作的差异，例如 "Frequency Selective … for Limited Feedback …" 对应已有工作的"窄带、完美 CSI"（tcomm.2016.2549517）。
