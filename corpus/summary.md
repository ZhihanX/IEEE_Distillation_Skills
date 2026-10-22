# 卡片汇总

卡片 80 张：研究论文 72，综述 / 教程 8。
由 `pipeline/aggregate_cards.py` 生成，不要手改。

## 研究论文（n = 72）

### 数值（中位数 [四分位距]）

| 字段 | 全部 | TWC | JSAC | TCOM | 2016-2018 | 2019-2021 | 2022-2025 |
|---|---|---|---|---|---|---|---|
| words_total | 7750 [6838.75–8738.25] | 7871 [6971–8811] | 7292 [6477.75–8590.25] | 7761 [6867.5–8905] | 7415.5 [6838.75–8633.25] | 7617.5 [6436.75–8698] | 8318 [7183.5–8935.75] |
| n_sections | 6 [6–7] | 6 [5–7] | 6 [6–7] | 6.5 [6–8] | 7 [6–7] | 6 [6–6.75] | 6 [5–7] |
| n_subsections | 15.5 [11.25–21.75] | 15 [11.5–24.5] | 17.5 [12.5–21.75] | 14 [9.5–20.75] | 13.5 [9–21.75] | 14 [10.25–19.5] | 18.5 [14–25] |
| n_figures | 10 [8–12] | 11 [9–13.75] | 10 [7.25–11.75] | 10 [8–11.75] | 9 [7–11] | 10 [8.25–11.75] | 11.5 [9.25–13] |
| n_tables | 1 [0.25–2] | 1.5 [1–2] | 1 [1–2] | 1 [0–2] | 1.5 [1–2] | 1 [1–2] | 1 [0–2] |
| n_display_eq | 41.5 [32.25–54.75] | 44 [37–61.5] | 31.5 [24.5–50.25] | 46.5 [35.5–50.75] | 39 [32.75–54] | 41.5 [32.25–59.25] | 47 [32.25–57] |
| n_algorithms | 2 [1–3] | 2 [1–3] | 2 [1–2] | 2 [1–3] | 2 [1–3] | 2 [1–3] | 2 [1–3] |
| n_appendix | 1 [0–1] | 0.5 [0–1] | 0 [0–1.75] | 1 [0–2] | 1 [0–2] | 0.5 [0–1.75] | 0 [0–1] |
| mean_sentence_words | 26.5 [24.525–28.3] | 26.95 [23.425–28.725] | 25.6 [23.975–27.05] | 26.65 [25.2–28] | 24.75 [22.925–27] | 26.8 [25–29.025] | 26.5 [25.225–28.8] |
| we_per_1k | 9.9 [6.95–12.675] | 9.1 [6.675–11.75] | 11.05 [6.625–13.275] | 9.9 [7.725–13.075] | 11.95 [7.75–14.125] | 9.55 [7.625–11.375] | 8.95 [5.725–11.875] |
| title_words | 10 [8–12] | 10 [8–11] | 10 [9–12.75] | 9 [8–11.75] | 10.5 [9.25–13] | 9 [8–11.75] | 9 [7.25–11.5] |
| abstract_words | 220 [197–253.25] | 233.5 [197–260.5] | 223.5 [204.5–248.75] | 208 [183.75–243] | 212 [183–248.25] | 219 [197–242] | 222 [205–258.25] |
| abstract_sentences | 8 [8–9] | 8.5 [8–9] | 8 [8–10] | 8 [7–9] | 8.5 [8–10] | 8 [7–9] | 8 [8–9] |
| intro_paragraphs | 7 [6–8] | 7 [6–8] | 7.5 [6–9] | 7 [6–8] | 7 [6–8] | 7 [5–8] | 8 [7–9] |
| contrib_n | 4 [3–4] | 4 [3–4] | 4 [3–4] | 4 [3–4.75] | 3.5 [3–4] | 4 [3–4.75] | 4 [3–4] |
| baselines_n | 3 [2–4] | 3 [2–4] | 3 [2.25–4] | 3 [2–3] | 3 [2–3] | 3 [2–4] | 3 [2.25–4] |
| conclusion_paragraphs | 1 [1–1] | 1 [1–1.75] | 1 [1–1] | 1 [1–2] | 1 [1–1] | 1 [1–1.75] | 1 [1–1] |

含定理类陈述的论文数：proof 51/72, remark 33/72, lemma 31/72, proposition 30/72, theorem 29/72, corollary 8/72, definition 7/72, assumption 3/72, constraint 1/72, example 1/72, remarks 1/72

### 编码字段（含该值的论文数 / n）

- **title_pattern**：X-for-Y 42/72, colon-subtitle 22/72, X-with-Y 14/72, X-aided-Y 13/72, X-in-Y 11/72, X-via-Y 7/72, noun-phrase 4/72, verb-ing 2/72, question 2/72, versus 2/72, toward 1/72
  - 按期刊：TWC: X-for-Y 13/24, X-with-Y 6/24, colon-subtitle 5/24, X-aided-Y 5/24; JSAC: X-for-Y 15/24, colon-subtitle 7/24, X-aided-Y 6/24, X-with-Y 5/24; TCOM: X-for-Y 14/24, colon-subtitle 10/24, X-in-Y 5/24, X-with-Y 3/24
  - 按年份段：2016-2018: X-for-Y 14/24, X-with-Y 8/24, colon-subtitle 7/24, X-in-Y 5/24; 2019-2021: X-for-Y 15/24, X-aided-Y 7/24, colon-subtitle 4/24, X-in-Y 3/24; 2022-2025: X-for-Y 13/24, colon-subtitle 11/24, X-aided-Y 6/24, X-in-Y 3/24
- **abstract_moves**：result 72/72, method 71/72, aim 69/72, context 52/72, theory 33/72, gap 27/72, implication 4/72, prior 2/72
  - 按期刊：TWC: result 24/24, method 24/24, aim 22/24, context 18/24; JSAC: aim 24/24, result 24/24, method 23/24, context 18/24; TCOM: result 24/24, method 24/24, aim 23/24, context 16/24
  - 按年份段：2016-2018: result 24/24, method 24/24, aim 22/24, context 17/24; 2019-2021: result 24/24, aim 24/24, method 23/24, context 18/24; 2022-2025: result 24/24, method 24/24, aim 23/24, context 17/24
- **abstract_has_numbers**：false 59/72, true 13/72
  - 按期刊：TWC: false 18/24, true 6/24; JSAC: false 20/24, true 4/24; TCOM: false 21/24, true 3/24
  - 按年份段：2016-2018: false 19/24, true 5/24; 2019-2021: false 19/24, true 5/24; 2022-2025: false 21/24, true 3/24
- **abstract_anchor**：in-this-paper 52/72, this-paper-verb 10/72, we-verb 6/72, none 4/72
  - 按期刊：TWC: in-this-paper 18/24, none 3/24, this-paper-verb 2/24, we-verb 1/24; JSAC: in-this-paper 19/24, we-verb 2/24, this-paper-verb 2/24, none 1/24; TCOM: in-this-paper 15/24, this-paper-verb 6/24, we-verb 3/24
  - 按年份段：2016-2018: in-this-paper 18/24, we-verb 2/24, this-paper-verb 2/24, none 2/24; 2019-2021: in-this-paper 21/24, none 1/24, we-verb 1/24, this-paper-verb 1/24; 2022-2025: in-this-paper 13/24, this-paper-verb 7/24, we-verb 3/24, none 1/24
- **intro_moves**：contrib 67/72, gap 67/72, roadmap 62/72, field 62/72, prior 57/72, aim 43/72, tech 43/72, notation 43/72, solution 16/72, approach 11/72, reproducibility 1/72
  - 按期刊：TWC: gap 23/24, contrib 22/24, prior 22/24, roadmap 21/24; JSAC: contrib 22/24, gap 22/24, roadmap 21/24, field 21/24; TCOM: contrib 23/24, gap 22/24, prior 21/24, field 20/24
  - 按年份段：2016-2018: roadmap 22/24, field 21/24, gap 21/24, contrib 20/24; 2019-2021: contrib 23/24, gap 22/24, field 19/24, prior 18/24; 2022-2025: gap 24/24, contrib 24/24, roadmap 22/24, field 22/24
- **related_work**：in-intro 47/72, in-intro-subsection 16/72, separate-section 9/72
  - 按期刊：TWC: in-intro 18/24, in-intro-subsection 6/24; JSAC: in-intro 10/24, separate-section 8/24, in-intro-subsection 6/24; TCOM: in-intro 19/24, in-intro-subsection 4/24, separate-section 1/24
  - 按年份段：2016-2018: in-intro 13/24, in-intro-subsection 7/24, separate-section 4/24; 2019-2021: in-intro 18/24, separate-section 3/24, in-intro-subsection 3/24; 2022-2025: in-intro 16/24, in-intro-subsection 6/24, separate-section 2/24
- **contrib_format**：bullets 44/72, paragraph 18/72, numbered 10/72
  - 按期刊：TWC: bullets 13/24, paragraph 9/24, numbered 2/24; JSAC: bullets 14/24, numbered 7/24, paragraph 3/24; TCOM: bullets 17/24, paragraph 6/24, numbered 1/24
  - 按年份段：2016-2018: bullets 13/24, paragraph 8/24, numbered 3/24; 2019-2021: bullets 13/24, paragraph 7/24, numbered 4/24; 2022-2025: bullets 18/24, numbered 3/24, paragraph 3/24
- **contrib_verbs**：propose 44/72, formulate 24/72, derive 23/72, develop 17/72, show 16/72, analyze 10/72, present 9/72, extend 9/72, investigate 8/72, introduce 7/72, demonstrate 7/72, evaluate 6/72
  - 按期刊：TWC: derive 13/24, propose 12/24, formulate 8/24, show 7/24; JSAC: propose 16/24, formulate 7/24, develop 5/24, introduce 4/24; TCOM: propose 16/24, formulate 9/24, develop 8/24, derive 7/24
  - 按年份段：2016-2018: propose 17/24, derive 11/24, show 7/24, formulate 6/24; 2019-2021: propose 14/24, formulate 9/24, develop 8/24, derive 6/24; 2022-2025: propose 13/24, formulate 9/24, develop 7/24, derive 6/24
- **contrib_quantified**：false 62/72, true 10/72
  - 按期刊：TWC: false 21/24, true 3/24; JSAC: false 20/24, true 4/24; TCOM: false 21/24, true 3/24
  - 按年份段：2016-2018: false 20/24, true 4/24; 2019-2021: false 21/24, true 3/24; 2022-2025: false 21/24, true 3/24
- **first_claim**：false 39/72, true 33/72
  - 按期刊：TWC: true 13/24, false 11/24; JSAC: true 14/24, false 10/24; TCOM: false 18/24, true 6/24
  - 按年份段：2016-2018: false 13/24, true 11/24; 2019-2021: true 13/24, false 11/24; 2022-2025: false 15/24, true 9/24
- **roadmap**：true 62/72, false 10/72
  - 按期刊：TWC: true 21/24, false 3/24; JSAC: true 21/24, false 3/24; TCOM: true 20/24, false 4/24
  - 按年份段：2016-2018: true 22/24, false 2/24; 2019-2021: true 18/24, false 6/24; 2022-2025: true 22/24, false 2/24
- **notation**：intro-end 43/72, none 14/72, table 13/72, model-start 2/72
  - 按期刊：TWC: intro-end 15/24, none 6/24, table 2/24, model-start 1/24; JSAC: intro-end 12/24, table 8/24, none 4/24; TCOM: intro-end 16/24, none 4/24, table 3/24, model-start 1/24
  - 按年份段：2016-2018: intro-end 9/24, table 7/24, none 6/24, model-start 2/24; 2019-2021: intro-end 14/24, table 6/24, none 4/24; 2022-2025: intro-end 20/24, none 4/24
- **gap_type**：limitation 45/72, new-scenario 27/72, practicality 17/72, combination 16/72, new-architecture 16/72, theory-gap 11/72, tool-transfer 10/72, unification 4/72, comparison 3/72, scalability 1/72
  - 按期刊：TWC: limitation 17/24, new-scenario 8/24, new-architecture 8/24, practicality 6/24; JSAC: limitation 13/24, new-scenario 12/24, combination 8/24, tool-transfer 6/24; TCOM: limitation 15/24, practicality 7/24, new-scenario 7/24, combination 5/24
  - 按年份段：2016-2018: limitation 13/24, new-scenario 12/24, combination 9/24, practicality 5/24; 2019-2021: limitation 14/24, new-scenario 8/24, practicality 7/24, theory-gap 6/24; 2022-2025: limitation 18/24, new-architecture 9/24, new-scenario 7/24, practicality 5/24
- **motivating_figure**：true 72/72
  - 按期刊：TWC: true 24/24; JSAC: true 24/24; TCOM: true 24/24
  - 按年份段：2016-2018: true 24/24; 2019-2021: true 24/24; 2022-2025: true 24/24
- **problem_class**：nonconvex-continuous 30/72, MINLP 12/72, analysis-only 9/72, learning 9/72, estimation 5/72, stochastic 3/72, combinatorial 2/72, convex 2/72
  - 按期刊：TWC: nonconvex-continuous 13/24, analysis-only 3/24, MINLP 3/24, convex 2/24; JSAC: nonconvex-continuous 8/24, learning 7/24, MINLP 4/24, analysis-only 2/24; TCOM: nonconvex-continuous 9/24, MINLP 5/24, analysis-only 4/24, estimation 3/24
  - 按年份段：2016-2018: MINLP 8/24, nonconvex-continuous 6/24, analysis-only 2/24, stochastic 2/24; 2019-2021: nonconvex-continuous 12/24, analysis-only 5/24, learning 3/24, MINLP 2/24; 2022-2025: nonconvex-continuous 12/24, learning 5/24, MINLP 2/24, estimation 2/24
- **solution**：closed-form 33/72, AO 19/72, SCA 16/72, reformulation 13/72, heuristic 12/72, SDR 12/72, DNN 10/72, decomposition 9/72, bisection 9/72, relaxation 9/72, penalty 9/72, lagrangian-dual 8/72
  - 按期刊：TWC: closed-form 13/24, SCA 6/24, reformulation 6/24, AO 6/24; JSAC: DNN 9/24, closed-form 8/24, AO 6/24, DRL 6/24; TCOM: closed-form 12/24, AO 7/24, SDR 6/24, reformulation 5/24
  - 按年份段：2016-2018: closed-form 14/24, lagrangian-dual 6/24, SCA 6/24, decomposition 5/24; 2019-2021: closed-form 11/24, AO 8/24, heuristic 5/24, SCA 5/24; 2022-2025: AO 8/24, closed-form 8/24, reformulation 7/24, SDR 6/24
- **theory_role**：supporting 36/72, central 19/72, none 17/72
  - 按期刊：TWC: supporting 10/24, central 7/24, none 7/24; JSAC: supporting 11/24, none 8/24, central 5/24; TCOM: supporting 15/24, central 7/24, none 2/24
  - 按年份段：2016-2018: supporting 11/24, central 10/24, none 3/24; 2019-2021: supporting 13/24, central 7/24, none 4/24; 2022-2025: supporting 12/24, none 10/24, central 2/24
- **proofs_location**：appendix 21/72, none 20/72, body 16/72, mixed 14/72, external 1/72
  - 按期刊：TWC: none 9/24, appendix 6/24, body 5/24, mixed 4/24; JSAC: none 8/24, appendix 6/24, body 6/24, mixed 3/24; TCOM: appendix 9/24, mixed 7/24, body 5/24, none 3/24
  - 按年份段：2016-2018: appendix 8/24, mixed 7/24, body 5/24, none 3/24; 2019-2021: appendix 9/24, body 7/24, none 6/24, mixed 2/24; 2022-2025: none 11/24, mixed 5/24, body 4/24, appendix 4/24
- **complexity_analysis**：true 45/72, false 27/72
  - 按期刊：TWC: true 16/24, false 8/24; JSAC: true 14/24, false 10/24; TCOM: true 15/24, false 9/24
  - 按年份段：2016-2018: true 14/24, false 10/24; 2019-2021: true 16/24, false 8/24; 2022-2025: true 15/24, false 9/24
- **convergence_analysis**：false 42/72, true 30/72
  - 按期刊：TWC: true 13/24, false 11/24; JSAC: false 17/24, true 7/24; TCOM: false 14/24, true 10/24
  - 按年份段：2016-2018: false 16/24, true 8/24; 2019-2021: true 14/24, false 10/24; 2022-2025: false 16/24, true 8/24
- **sim_param_table**：false 44/72, true 28/72
  - 按期刊：TWC: true 12/24, false 12/24; JSAC: false 14/24, true 10/24; TCOM: false 18/24, true 6/24
  - 按年份段：2016-2018: false 14/24, true 10/24; 2019-2021: false 13/24, true 11/24; 2022-2025: false 17/24, true 7/24
- **baseline_naming**：descriptive 55/72, acronym 15/72, none 2/72
  - 按期刊：TWC: descriptive 17/24, acronym 5/24, none 2/24; JSAC: descriptive 19/24, acronym 5/24; TCOM: descriptive 19/24, acronym 5/24
  - 按年份段：2016-2018: descriptive 21/24, acronym 2/24, none 1/24; 2019-2021: descriptive 18/24, acronym 5/24, none 1/24; 2022-2025: descriptive 16/24, acronym 8/24
- **x_axes**：iterations 27/72, SNR 17/72, number-of-users 17/72, transmit-power 14/72, number-of-elements 14/72, distance 11/72, number-of-antennas 8/72, time 7/72, CDF 6/72, SINR-target 6/72, trajectory-plot 5/72, CSI-error 5/72
  - 按期刊：TWC: iterations 12/24, number-of-users 7/24, transmit-power 6/24, number-of-elements 5/24; JSAC: SNR 8/24, number-of-users 6/24, iterations 6/24, transmit-power 5/24; TCOM: iterations 9/24, distance 7/24, SNR 6/24, number-of-users 4/24
  - 按年份段：2016-2018: iterations 10/24, number-of-users 6/24, SNR 5/24, time 5/24; 2019-2021: number-of-elements 9/24, iterations 7/24, transmit-power 7/24, number-of-users 5/24; 2022-2025: iterations 10/24, SNR 8/24, number-of-users 6/24, number-of-antennas 6/24
- **fig1_role**：system-model 45/72, architecture 16/72, framework 7/72, scenario 3/72, result 1/72
  - 按期刊：TWC: system-model 17/24, architecture 6/24, result 1/24; JSAC: system-model 10/24, architecture 6/24, framework 5/24, scenario 3/24; TCOM: system-model 18/24, architecture 4/24, framework 2/24
  - 按年份段：2016-2018: system-model 18/24, architecture 4/24, scenario 2/24; 2019-2021: system-model 18/24, architecture 4/24, framework 2/24; 2022-2025: system-model 9/24, architecture 8/24, framework 5/24, scenario 1/24
- **caption_style**：short-label 40/72, descriptive 31/72, self-contained-conclusion 1/72
  - 按期刊：TWC: short-label 17/24, descriptive 7/24; JSAC: descriptive 12/24, short-label 12/24; TCOM: descriptive 12/24, short-label 11/24, self-contained-conclusion 1/24
  - 按年份段：2016-2018: descriptive 12/24, short-label 12/24; 2019-2021: short-label 14/24, descriptive 10/24; 2022-2025: short-label 14/24, descriptive 9/24, self-contained-conclusion 1/24
- **prototype_or_measurement**：false 68/72, true 4/72
  - 按期刊：TWC: false 23/24, true 1/24; JSAC: false 22/24, true 2/24; TCOM: false 23/24, true 1/24
  - 按年份段：2016-2018: false 23/24, true 1/24; 2019-2021: false 22/24, true 2/24; 2022-2025: false 23/24, true 1/24
- **code_released**：false 71/72, true 1/72
  - 按期刊：TWC: false 24/24; JSAC: false 24/24; TCOM: false 23/24, true 1/24
  - 按年份段：2016-2018: false 24/24; 2019-2021: false 23/24, true 1/24; 2022-2025: false 24/24
- **conclusion_has_numbers**：false 66/72, true 6/72
  - 按期刊：TWC: false 22/24, true 2/24; JSAC: false 21/24, true 3/24; TCOM: false 23/24, true 1/24
  - 按年份段：2016-2018: false 23/24, true 1/24; 2019-2021: false 22/24, true 2/24; 2022-2025: false 21/24, true 3/24
- **conclusion_future_work**：false 36/72, true 36/72
  - 按期刊：TWC: false 17/24, true 7/24; JSAC: false 12/24, true 12/24; TCOM: true 17/24, false 7/24
  - 按年份段：2016-2018: false 12/24, true 12/24; 2019-2021: true 14/24, false 10/24; 2022-2025: false 14/24, true 10/24

### 短语（至少出现一次的论文数）

inThisPaper 72/72, however 71/72, transition 71/72, observe 67/72, toAddress 65/72, intensifier 62/72, contrast 62/72, roadmap 61/72, weProposeFirst 59/72, figVerb 58/72, contribList 57/72, resultsShow 53/72, outperform 50/72, nonconvex 46/72, promising 45/72, tradeoff 43/72, gen 40/72, thisIsBecause 39/72, motivatedBy 37/72, wlog 37/72, insight 36/72, closedForm 35/72, novel 35/72, worthNoting 34/72, asExpected 22/72, toTheBest 19/72, gapWord 15/72, npHard 10/72, firstTime 10/72, prototype 10/72, code 2/72

### 方法关键词（至少出现一次的论文数）

complexity 63/72, convergence 57/72, convexOpt 36/72, AO 20/72, DNN 18/72, lagrange 18/72, penalty 17/72, SCA 16/72, bisection 15/72, KKT 15/72, SDR 14/72, monteCarlo 10/72, DRL 10/72, manifold 10/72, FP 10/72, compressedSensing 8/72, gameTheory 7/72, BCD 7/72, lyapunov 6/72, MM 5/72, CRB 4/72, stochGeom 3/72, WMMSE 3/72, BnB 3/72, ADMM 2/72, randomMatrix 1/72

## 综述 / 教程 / 展望（n = 8）

### 数值（中位数 [四分位距]）

| 字段 | 全部 | TWC | JSAC | TCOM | 2016-2018 | 2019-2021 | 2022-2025 |
|---|---|---|---|---|---|---|---|
| words_total | 14991.5 [9939.75–22827.5] | - | 15979 [8177.25–39821.8] | 14991.5 [12853–21039] | 8493.5 | 19264 [13214.2–39817.2] | 18550.5 |
| n_sections | 9 [9–9] | - | 9 [9–9.75] | 9 [7.5–9] | 9.5 | 9 [7.5–9] | 9 |
| n_subsections | 36.5 [27.5–55] | - | 41.5 [19.5–83] | 36.5 [30.75–48.25] | 22 | 44.5 [31–55] | 64 |
| n_figures | 12.5 [7.25–25.5] | - | 13.5 [6–31.5] | 12.5 [11.25–23.5] | 6 | 20 [12.25–33] | 16 |
| n_tables | 2.5 [0.25–4] | - | 0.5 [0–3.25] | 4 [1.75–5.5] | 0 | 2.5 [1–4] | 5 |
| n_display_eq | 34.5 [3.5–72] | - | 32.5 [3.5–72] | 34.5 [7.25–73.75] | 7 | 45.5 [31.75–76.5] | 39.5 |
| n_algorithms | 0 [0–0] | - | 0 [0–0] | 0 [0–2.25] | 0 | 0 [0–2.25] | 0 |
| n_appendix | 0 [0–0] | - | 0 [0–0] | 0 [0–1.5] | 0 | 0 [0–1.5] | 0 |
| mean_sentence_words | 26.05 [24.175–29.3] | - | 25.2 | 26.9 | 25.2 | 26.9 | 25.65 |
| we_per_1k | 4.6 [2.075–6.675] | - | 2.4 | 6.2 | 1.1 | 4.3 | 5.55 |
| title_words | 11.5 [7–14] | - | 13 [5.25–17] | 9 [7–13.25] | 8.5 | 9 [7–16.25] | 13 |
| abstract_words | 210 [145.5–275.75] | - | 231 | 189 | 123 | 245 | 210 |
| abstract_sentences | 6.5 [6–8.75] | - | 6.5 [6–8.5] | 7 [5.25–11.75] | 6 | 6.5 [5.25–11.5] | 8.5 |
| intro_paragraphs | 7 [5–18.25] | - | 6.5 [5–17] | 9.5 [4.5–19.75] | 6.5 | 9 [4.25–19.75] | 13 |
| contrib_n | 0 [0–0] | - | 0 [0–0] | 0 [0–0] | 0 | 0 [0–0] | 0 |
| baselines_n | 0 [0–0] | - | 0 [0–0] | 0 [0–0] | 0 | 0 [0–0] | 0 |
| conclusion_paragraphs | 2.5 [1.25–4.5] | - | 2.5 [1.25–4.5] | 2.5 [1.25–5.25] | 2 | 2.5 [1.25–5.25] | 3.5 |

含定理类陈述的论文数：proposition 2/8, remark 2/8, proof 2/8, example 1/8

### 编码字段（含该值的论文数 / n）

- **title_pattern**：colon-subtitle 6/8, noun-phrase 1/8, toward 1/8, X-in-Y 1/8, X-aided-Y 1/8
  - 按期刊：JSAC: colon-subtitle 3/4, noun-phrase 1/4, toward 1/4; TCOM: colon-subtitle 3/4, X-in-Y 1/4, X-aided-Y 1/4
  - 按年份段：2016-2018: noun-phrase 1/2, colon-subtitle 1/2; 2019-2021: colon-subtitle 3/4, X-in-Y 1/4, X-aided-Y 1/4; 2022-2025: colon-subtitle 2/2, toward 1/2
- **abstract_moves**：context 8/8, aim 8/8, implication 4/8, gap 2/8, result 1/8, method 1/8, prior 1/8
  - 按期刊：JSAC: context 4/4, aim 4/4, implication 1/4; TCOM: context 4/4, aim 4/4, implication 3/4, gap 2/4
  - 按年份段：2016-2018: context 2/2, aim 2/2; 2019-2021: context 4/4, aim 4/4, implication 3/4, gap 2/4; 2022-2025: context 2/2, aim 2/2, implication 1/2, prior 1/2
- **abstract_has_numbers**：false 8/8
  - 按期刊：JSAC: false 4/4; TCOM: false 4/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 4/4; 2022-2025: false 2/2
- **abstract_anchor**：this-paper-verb 4/8, in-this-paper 4/8
  - 按期刊：JSAC: this-paper-verb 2/4, in-this-paper 2/4; TCOM: this-paper-verb 2/4, in-this-paper 2/4
  - 按年份段：2016-2018: this-paper-verb 2/2; 2019-2021: in-this-paper 3/4, this-paper-verb 1/4; 2022-2025: in-this-paper 1/2, this-paper-verb 1/2
- **intro_moves**：field 8/8, tech 6/8, prior 6/8, roadmap 5/8, aim 5/8, gap 2/8, solution 1/8, notation 1/8
  - 按期刊：JSAC: field 4/4, roadmap 3/4, tech 3/4, prior 3/4; TCOM: field 4/4, aim 3/4, prior 3/4, tech 3/4
  - 按年份段：2016-2018: roadmap 2/2, field 2/2, tech 2/2, gap 1/2; 2019-2021: field 4/4, aim 3/4, prior 3/4, roadmap 2/4; 2022-2025: aim 2/2, tech 2/2, prior 2/2, field 2/2
- **related_work**：separate-section 3/8, table 3/8, none 2/8
  - 按期刊：JSAC: none 2/4, separate-section 1/4, table 1/4; TCOM: separate-section 2/4, table 2/4
  - 按年份段：2016-2018: none 2/2; 2019-2021: separate-section 3/4, table 1/4; 2022-2025: table 2/2
- **contrib_format**：none 5/8, paragraph 2/8, bullets 1/8
  - 按期刊：JSAC: none 4/4; TCOM: paragraph 2/4, none 1/4, bullets 1/4
  - 按年份段：2016-2018: none 2/2; 2019-2021: none 2/4, paragraph 2/4; 2022-2025: none 1/2, bullets 1/2
- **contrib_verbs**：
  - 按期刊：JSAC: ; TCOM: 
  - 按年份段：2016-2018: ; 2019-2021: ; 2022-2025: 
- **contrib_quantified**：false 8/8
  - 按期刊：JSAC: false 4/4; TCOM: false 4/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 4/4; 2022-2025: false 2/2
- **first_claim**：false 6/8, true 2/8
  - 按期刊：JSAC: false 4/4; TCOM: false 2/4, true 2/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 2/4, true 2/4; 2022-2025: false 2/2
- **roadmap**：true 8/8
  - 按期刊：JSAC: true 4/4; TCOM: true 4/4
  - 按年份段：2016-2018: true 2/2; 2019-2021: true 4/4; 2022-2025: true 2/2
- **notation**：none 5/8, table 2/8, intro-end 1/8
  - 按期刊：JSAC: none 3/4, table 1/4; TCOM: none 2/4, table 1/4, intro-end 1/4
  - 按年份段：2016-2018: none 2/2; 2019-2021: table 2/4, none 1/4, intro-end 1/4; 2022-2025: none 2/2
- **gap_type**：unification 6/8, new-scenario 1/8, theory-gap 1/8, new-architecture 1/8
  - 按期刊：JSAC: unification 3/4, new-scenario 1/4; TCOM: unification 3/4, theory-gap 1/4, new-architecture 1/4
  - 按年份段：2016-2018: new-scenario 1/2, unification 1/2; 2019-2021: unification 3/4, theory-gap 1/4, new-architecture 1/4; 2022-2025: unification 2/2
- **motivating_figure**：true 7/8, false 1/8
  - 按期刊：JSAC: true 3/4, false 1/4; TCOM: true 4/4
  - 按年份段：2016-2018: true 1/2, false 1/2; 2019-2021: true 4/4; 2022-2025: true 2/2
- **problem_class**：none 8/8
  - 按期刊：JSAC: none 4/4; TCOM: none 4/4
  - 按年份段：2016-2018: none 2/2; 2019-2021: none 4/4; 2022-2025: none 2/2
- **solution**：
  - 按期刊：JSAC: ; TCOM: 
  - 按年份段：2016-2018: ; 2019-2021: ; 2022-2025: 
- **theory_role**：none 8/8
  - 按期刊：JSAC: none 4/4; TCOM: none 4/4
  - 按年份段：2016-2018: none 2/2; 2019-2021: none 4/4; 2022-2025: none 2/2
- **proofs_location**：none 8/8
  - 按期刊：JSAC: none 4/4; TCOM: none 4/4
  - 按年份段：2016-2018: none 2/2; 2019-2021: none 4/4; 2022-2025: none 2/2
- **complexity_analysis**：false 8/8
  - 按期刊：JSAC: false 4/4; TCOM: false 4/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 4/4; 2022-2025: false 2/2
- **convergence_analysis**：false 8/8
  - 按期刊：JSAC: false 4/4; TCOM: false 4/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 4/4; 2022-2025: false 2/2
- **sim_param_table**：false 8/8
  - 按期刊：JSAC: false 4/4; TCOM: false 4/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 4/4; 2022-2025: false 2/2
- **baseline_naming**：none 8/8
  - 按期刊：JSAC: none 4/4; TCOM: none 4/4
  - 按年份段：2016-2018: none 2/2; 2019-2021: none 4/4; 2022-2025: none 2/2
- **x_axes**：
  - 按期刊：JSAC: ; TCOM: 
  - 按年份段：2016-2018: ; 2019-2021: ; 2022-2025: 
- **fig1_role**：framework 6/8, architecture 1/8, scenario 1/8
  - 按期刊：JSAC: framework 2/4, architecture 1/4, scenario 1/4; TCOM: framework 4/4
  - 按年份段：2016-2018: architecture 1/2, scenario 1/2; 2019-2021: framework 4/4; 2022-2025: framework 2/2
- **caption_style**：short-label 7/8, descriptive 1/8
  - 按期刊：JSAC: short-label 4/4; TCOM: short-label 3/4, descriptive 1/4
  - 按年份段：2016-2018: short-label 2/2; 2019-2021: short-label 3/4, descriptive 1/4; 2022-2025: short-label 2/2
- **prototype_or_measurement**：false 8/8
  - 按期刊：JSAC: false 4/4; TCOM: false 4/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 4/4; 2022-2025: false 2/2
- **code_released**：false 8/8
  - 按期刊：JSAC: false 4/4; TCOM: false 4/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 4/4; 2022-2025: false 2/2
- **conclusion_has_numbers**：false 8/8
  - 按期刊：JSAC: false 4/4; TCOM: false 4/4
  - 按年份段：2016-2018: false 2/2; 2019-2021: false 4/4; 2022-2025: false 2/2
- **conclusion_future_work**：true 6/8, false 2/8
  - 按期刊：JSAC: true 2/4, false 2/4; TCOM: true 4/4
  - 按年份段：2016-2018: true 1/2, false 1/2; 2019-2021: true 3/4, false 1/4; 2022-2025: true 2/2

### 短语（至少出现一次的论文数）



### 方法关键词（至少出现一次的论文数）



