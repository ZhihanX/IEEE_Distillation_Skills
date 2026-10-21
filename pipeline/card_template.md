# 单篇蒸馏卡片模板

每篇论文一张卡片，存为 `corpus/cards/<journal>_<doi 后缀>.md`。
引用原文只摘短句（单句、≤ 30 词），用于说明句式；不要复制段落。

```yaml
doi:
journal:          # TWC / JSAC / TCOM
year:
cites:            # Crossref 引用数（记录抓取日期）
article_type:     # research / survey / tutorial / magazine-style
topic:            # 如 RIS、cell-free、ISAC、UAV、NOMA、FL over wireless …
source:           # IEEE Xplore 正式版 / arXiv 预印本
```

## 1. 标题
- 结构模式（如 "X for Y: Z"、"X Versus Y"、问句、"Toward …"）、词数

## 2. 摘要（按句拆 move）
- 每句的功能：背景 / 空白 / 本文方法 / 关键技术 / 量化结果 / 意义
- 是否给出具体数字；是否出现 "In this paper" 类锚点句

## 3. 引言逻辑
- 段落序列：每段一句话概括其作用（建立领域 → 现有工作 → 空白 → 本文）
- 相关工作的组织方式（按方法分组 / 按场景分组 / 表格对比）
- 贡献列表：条数、每条的开头动词、是否带量化
- 是否有 "The rest of this paper is organized as follows"
- 记号说明段（Notation）位置

## 4. Idea 是怎么提出的
- 空白类型：现有方法局限 / 新场景新硬件 / 理论缺口 / 反直觉观察 / 统一框架
- 核心洞见句（摘一句）
- 有没有 motivating example 或开篇示意图

## 5. 科研方法
- 系统模型：场景图、信道模型、假设
- 问题形式化：目标函数、约束、是否非凸
- 求解路线：AO / SCA / SDR / BCD / 拉格朗日对偶 / 闭式解 / 深度学习 / 随机几何
- 理论结果：定理、引理、命题数量，证明放附录还是正文
- 复杂度 / 收敛性分析

## 6. 仿真与实验
- 仿真参数表、baseline 数量与命名方式、横轴变量
- 是否有实测 / 原型；是否开源代码
- 结果段的写法：现象 → 原因解释 → 启示

## 7. 图表
- 图表总数、Fig. 1 的角色（系统模型 / 框架 / 问题示意）
- 结果图类型（性能 vs SNR / 天线数 / 用户数 / 迭代次数的收敛曲线 …）
- caption 风格：长短、是否自含结论
- 表格：参数表 / 对比表 / 符号表

## 8. 句式库（按功能，各摘 1–2 句）
- 指出空白、陈述贡献、对比 baseline、解释结果、承认局限、展望未来

## 9. 结论
- 结构：总结 → 主要发现 → 未来工作；是否重复数字
