# IEEE 期刊惯例（在语料中观察到的写法）

本文件记录 72 篇研究论文里反复出现的格式与行文惯例。格式细节（字体、页数、参考文献格式）以目标期刊当年的
作者指南和 IEEE 模板为准；这里只列在语料中能看到证据的做法。DOI 省略 `10.1109/`。

## 1. 章节与编号

- 一级节用罗马数字，正文和路线图里写 "Section II"：
  "Section II presents the networked ISAC model for LAE and formulates the problem."（tcomm.2025.3541027）
- 二级小节用 "A. / B. / C."；三级用 "1) / 2) / 3)"，常写成段首小标题（run-in heading），如 jsac.2020.3000803 的
  "B. DL Channel Model" 下分 "1) Doppler: / 2) Delay: / 3) Angle: / 4) Gain:"。
- 引言也可以分小节："A. Related Works / B. Contributions / C. Organization and Notations"（twc.2020.2970061；引言内小节共 16/72）。
- 附录用字母编号，标题写证明对象："Appendix A Proof of Proposition 2"（jsac.2020.3000803）。

## 2. 记号说明

- 位置：引言末 43/72，记号表 13/72，模型节开头 2/72，没有 14/72。
- 写法：以 "Notations:" 起段，先说字体约定，再逐个列运算符。
  "Notations: Lowercase and uppercase letters with boldface refer to vectors and matrices, respectively."（tcomm.2025.3541027）
- 常见条目（tcomm.2016.2549517、twc.2020.2970061、tcomm.2025.3541027 等）：粗体小写为向量、粗体大写为矩阵、花体为集合；
  转置 (·)^T、共轭转置 (·)^H、逆、伪逆；‖·‖ 与 Frobenius 范数；diag(·)；单位阵 I_M；Hadamard 积；期望 E[·]；
  圆对称复高斯 CN(μ, σ²)；tr(·)；复数空间 C^{x×y}。
- 变量多时用表（"TABLE I Variable list"，jsac.2020.3000803；JSAC 用记号表 8/24）。

## 3. 定理类环境与证明

- 用 Proposition / Theorem / Lemma / Corollary / Remark / Definition 环境；各类出现率：remark 33/72，lemma 31/72，proposition 30/72，theorem 29/72，corollary 8/72，definition 7/72。
- 编号可以按类型分别编号，也可以共用一个序列（如 tcomm.2016.2549517 的 Proposition 1、Corollary 2、Proposition 3、Proposition 4、Lemma 5）。
- 正文的定理后留证明或一句指向附录的说明；长证明放附录（附录 21/72，附录 + 正文 14/72）。
- 证明省略要说明理由："… can be readily proved based on the proof for Theorem 1. Thus this proof is omitted for the sake of saving space."（jsac.2018.2864426）

## 4. 优化问题与公式

- 问题编号用 (P1)、(P1.1)、(P1.2) 等，子问题和迭代近似问题在原编号上扩展（如 tcomm.2025.3541027 的 "(P1.3.o)"、"(SDR 1.3.o)"）；约束编号随公式编号加字母，如 (16a)、(16b)。
- 公式是句子的一部分：公式后接 "where … denotes …" 解释符号；正文引用公式只写括号编号。
  "From (23) and (30), we can obtain the DL-UL duality between the proposed sCSI based DL precoder and UL receiver."（jsac.2020.3000803）
- 数值和单位写在数学环境里，单位与数字之间留空格："P_T = 5 dBm"、"N = 100"（twc.2020.2970061）。

## 5. 引用文献的写法

- 编号引用，连续区间用 en dash："[11]–[14]"；并列用逗号："[4], [5]"。
- 文献作主语的常见句式：
  - "In [21] and [22], the transmit power of the AP is minimized by decomposing the joint optimization problem into two subproblems: …"（twc.2020.2970061）
  - "The authors in [11] exploited the cellular-connected UAV to enable bi-static sensing with GBS."（tcomm.2025.3541027）
  - "The work in [16] proposed a power efficient deployment and cell association for multiple UAVs in downlink transmissions."（twc.2016.2531652）
- 用文献支撑假设："Similar to [24], [26], [27], assume that the ground UEs can communicate with their serving UAV via the orthogonal frequency-division multiple access."（twc.2022.3153316）
- "e.g.," 后直接接文献："It is worth noting that most of the existing works on downlink (DL) precoding in multibeam satellite communications, e.g., [4], [5], rely on precise instantaneous channel state information (iCSI)."（jsac.2020.3000803）

## 6. 缩写与命名

- 缩写在摘要中首次出现时定义，进入正文后再定义一次（如 jsac.2020.3000803 在摘要和引言里都写了 "Low earth orbit (LEO)"）。
- 新方法、新系统要命名，并在命名句里给出缩写：
  - "In this paper, we study a new relaying technique, termed mobile relaying, where …"（tcomm.2016.2611512）
  - "Therefore, we call this system 'Cell-Free Massive MIMO'."（twc.2017.2655515）
  - "We integrate both the advantages of NTC and classical deep JSCC, which is collected under the name nonlinear transform source-channel coding (NTSCC)."（jsac.2022.3180802）
- 基准方案命名：描述性名称 55/72（"Random Phase"、"Without RIS"），缩写 15/72（"MATD3-FP"、"IntF"）；首次出现时用一句话定义。

## 7. 人称、时态与语态

- 第一人称复数 "we" 是常态（每千词中位数 9.9 [7.0–12.7]）；"In this paper/work" 每篇中位数出现 4 次。
- 也有高引论文几乎全用被动语态（twc.2022.3153316 每千词 3.7、tcomm.2019.2956472 每千词 4.2），摘要锚点写成
  "In this paper, the problem of … is studied."（tcomm.2019.2956472）。选定一种后全文保持一致。
- 描述本文工作用一般现在时（"In this paper, we propose …"）；结论开头常用现在完成时（"In this paper, we have investigated …"，jsac.2020.3000803），之后可转一般过去时复述。
- 平均句长中位数 26.5 词 [24.5–28.3]；英式拼写也可以（"favourable"、"whilst"，twc.2020.2990766），但全文一致。

## 8. 前作与会议版

- 扩展自己的会议论文或前作很常见（卡片中提到前作的 ≥ 17/72），要说明增量：
  - "This work significantly extends the preliminary work [1]."（jsac.2018.2869954）
  - "Part of the results have been presented in our previous work, which investigates …"（tcomm.2016.2599530）
- 批评自己的前作同样可以作为空白来源："In [33], we investigated the FL loss function minimization problem …."（twc.2020.3037554），后接 "However, this prior work ignored the computation delay of local FL model."

## 9. 可复现性

- 公开代码在语料里很少（1/72）："All the simulation results can be reproduced using the Matlab code and data files available at: …"（tcomm.2020.2987311）。
- 参数来源写清楚（参数表 28/72，或在正文注明 "similar to [24]"、3GPP 模型），蒙特卡洛平均次数写在仿真节第一段。
