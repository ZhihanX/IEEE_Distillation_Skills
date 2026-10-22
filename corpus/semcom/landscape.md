# 语义通信候选论文标题索引（landscape）

自动生成（`python3 pipeline/landscape_semcom.py`）。来源 `corpus/semcom/candidates.csv`：234 篇，TWC / JSAC / TCOM / TCCN / TSP / JSAIT，2018–2025，Crossref 引用 ≥ 10，标题匹配语义通信 / JSCC / 任务导向等关键词。
标签只看标题（Crossref 没有摘要），空格表示"这个池子里没有标题提到"，不等于"没人做过"；查新时必须再做实时检索（arXiv、IEEE Xplore、Google Scholar）。

## 1. 年份分布

2018: 2, 2019: 3, 2020: 5, 2021: 7, 2022: 15, 2023: 51, 2024: 69, 2025: 82

## 2. 标签计数

- 模态：(none in title) 150/234, image 35/234, feature/inference 18/234, video 17/234, multimodal 9/234, text 7/234, speech/audio 5/234, point-cloud/3D 2/234
- 主题：task/goal-oriented 53/234, (none in title) 48/234, resource allocation 37/234, multi-user/MA 28/234, JSCC 25/234, adaptive 21/234, generative/LLM 20/234, digital/modulation 19/234, security/privacy 17/234, UAV/vehicular/satellite 15/234, theory/limits 12/234, sensing/ISAC 8/234, reinforcement learning 8/234, knowledge 8/234, feedback/HARQ 7/234, MIMO 7/234, transformer/attention 6/234, RIS 6/234, relay/cooperative 4/234, OFDM 2/234

## 3. 模态 × 主题占位表（篇数）

| 模态 \ 主题 | task/goal-oriented | (none in title) | resource allocation | multi-user/MA | JSCC | adaptive | generative/LLM | digital/modulation | security/privacy | UAV/vehicular/satellite | theory/limits | sensing/ISAC | reinforcement learning | knowledge | feedback/HARQ | MIMO | transformer/attention | RIS | relay/cooperative | OFDM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (none in title) | 38 | 29 | 23 | 15 | 18 | 11 | 12 | 16 | 12 | 9 | 8 | 6 | 6 | 7 | 3 | 4 | 3 | 6 | 2 | 2 |
| image | 5 | 6 | 2 | 2 | 6 | 5 | 2 | 2 | 4 | 4 | 2 | 1 | · | · | 3 | 2 | 2 | · | 1 | · |
| feature/inference | 8 | 1 | 7 | 8 | · | 2 | 3 | 2 | · | · | 1 | 1 | · | 1 | · | · | · | · | 1 | · |
| video | 1 | 7 | 3 | 5 | · | 3 | · | · | · | 1 | · | · | 2 | · | · | · | · | · | · | · |
| multimodal | · | 4 | 3 | · | · | 1 | 2 | · | · | 1 | · | · | · | · | · | · | · | · | · | · |
| text | 1 | 1 | · | · | 1 | · | 1 | · | 1 | · | 1 | · | · | · | 1 | 1 | · | · | · | · |
| speech/audio | · | 3 | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | 1 | · | · | · |
| point-cloud/3D | 1 | 1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · |

## 4. 主题按年份（标题计数）

| 主题 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| task/goal-oriented | · | · | · | · | 3 | 16 | 17 | 17 |
| (none in title) | 1 | 1 | 1 | 3 | 3 | 15 | 12 | 12 |
| resource allocation | 1 | · | · | 1 | 1 | 5 | 13 | 16 |
| multi-user/MA | 1 | 1 | 1 | 1 | 1 | 6 | 12 | 5 |
| JSCC | · | 1 | 2 | 2 | 6 | 5 | 2 | 7 |
| adaptive | · | · | 1 | 1 | · | 3 | 7 | 9 |
| generative/LLM | · | · | · | · | · | 1 | 3 | 16 |
| digital/modulation | · | · | · | · | 1 | 4 | 4 | 10 |
| security/privacy | · | · | · | · | 1 | 4 | 5 | 7 |
| UAV/vehicular/satellite | · | · | · | 1 | 1 | 2 | 4 | 7 |
| theory/limits | · | · | · | · | 2 | 3 | 2 | 5 |
| sensing/ISAC | · | · | · | · | · | 2 | 1 | 5 |
| reinforcement learning | · | · | · | 1 | 1 | 2 | 1 | 3 |
| knowledge | · | · | · | · | · | · | 4 | 4 |
| feedback/HARQ | · | · | 1 | · | 1 | 1 | 3 | 1 |
| MIMO | · | · | · | · | · | 2 | 3 | 2 |
| transformer/attention | · | · | · | · | 1 | · | 2 | 3 |
| RIS | · | · | · | · | · | 1 | 3 | 2 |
| relay/cooperative | · | · | · | · | · | 2 | 1 | 1 |
| OFDM | · | · | · | · | 1 | · | 1 | · |

## 5. 各标签下的标题（按年均引用降序）

### topic:task/goal-oriented（53）
- Beyond Transmitting Bits: Context, Semantics, and Task-Oriented Communications — JSAC 2023, jsac.2022.3223408, cpy 216.1 [ | task/goal-oriented]
- Task-Oriented Multi-User Semantic Communications — JSAC 2022, jsac.2022.3191326, cpy 113.4 [ | task/goal-oriented, multi-user/MA]
- Task-Oriented Sensing, Computation, and Communication Integration for Multi-Device Edge AI — TWC 2024, twc.2023.3303232, cpy 94.5 [ | task/goal-oriented, multi-user/MA, sensing/ISAC]
- Learning Task-Oriented Communication for Edge Inference: An Information Bottleneck Approach — JSAC 2022, jsac.2021.3126087, cpy 72.9 [feature/inference | task/goal-oriented, theory/limits]
- Semantic Communications for Image Recovery and Classification via Deep Joint Source and Channel Coding — TWC 2024, twc.2023.3349330, cpy 70.8 [image | task/goal-oriented]
- Adaptable Semantic Compression and Resource Allocation for Task-Oriented Communications — TCCN 2024, tccn.2023.3346481, cpy 60.6 [ | task/goal-oriented, resource allocation]
- DRL-Driven Dynamic Resource Allocation for Task-Oriented Semantic Communication — TCOM 2023, tcomm.2023.3274145, cpy 58.3 [ | task/goal-oriented, resource allocation, reinforcement learning]
- Task-Oriented Communication for Multidevice Cooperative Edge Inference — TWC 2023, twc.2022.3191118, cpy 57.7 [feature/inference | task/goal-oriented, multi-user/MA, relay/cooperative]
- Personalized Saliency in Task-Oriented Semantic Communications: Image Transmission and Performance Analysis — JSAC 2023, jsac.2022.3221990, cpy 50.8 [image | task/goal-oriented]
- Beyond the Cloud: Edge Inference for Generative Large Language Models in Wireless Networks — TWC 2025, twc.2024.3497923, cpy 46.6 [feature/inference | generative/LLM, task/goal-oriented]
- Robust Information Bottleneck for Task-Oriented Communication With Digital Modulation — JSAC 2023, jsac.2023.3288252, cpy 40.9 [ | digital/modulation, task/goal-oriented, theory/limits, security/privacy]
- Task-Oriented Image Transmission for Scene Classification in Unmanned Aerial Systems — TCOM 2022, tcomm.2022.3182325, cpy 34.7 [image | task/goal-oriented, UAV/vehicular/satellite]
- Privacy-Preserving Task-Oriented Semantic Communications Against Model Inversion Attacks — TWC 2024, twc.2024.3369170, cpy 33.6 [ | task/goal-oriented, security/privacy]
- Energy-Efficient Edge Inference in Integrated Sensing, Communication, and Computation Networks — JSAC 2025, jsac.2025.3574612, cpy 32.7 [feature/inference | task/goal-oriented, sensing/ISAC, resource allocation]
- Task-Oriented Over-the-Air Computation for Multi-Device Edge AI — TWC 2024, twc.2023.3294703, cpy 32.4 [ | task/goal-oriented, multi-user/MA]
- R-ACP: Real-Time Adaptive Collaborative Perception Leveraging Robust Task-Oriented Communications — JSAC 2025, jsac.2025.3623179, cpy 31.0 [ | task/goal-oriented, security/privacy, adaptive]
- Task-Oriented Explainable Semantic Communications — TWC 2023, twc.2023.3269444, cpy 29.9 [ | task/goal-oriented]
- Feature Importance-Aware Task-Oriented Semantic Transmission and Optimization — TCCN 2024, tccn.2024.3375496, cpy 26.2 [feature/inference | task/goal-oriented, resource allocation]
- Resource Allocation for Multiuser Edge Inference With Batching and Early Exiting — JSAC 2023, jsac.2023.3242724, cpy 23.9 [feature/inference | task/goal-oriented, multi-user/MA, resource allocation]
- Task-Oriented Communication for Edge Video Analytics — TWC 2024, twc.2023.3314888, cpy 21.0 [video | task/goal-oriented]
- Computation-Aware Offloading for DNN Inference Tasks in Semantic Communication Assisted MEC Systems — TWC 2025, twc.2024.3523517, cpy 19.9 [ | task/goal-oriented]
- Task-Oriented Semantic Communication over Rate Splitting Enabled Wireless Control Systems for URLLC Services — TCOM 2024, tcomm.2023.3325901, cpy 18.7 [feature/inference | task/goal-oriented, multi-user/MA]
- End-to-End Learning for Task-Oriented Semantic Communications Over MIMO Channels: An Information-Theoretic Framework — JSAC 2025, jsac.2025.3531575, cpy 18.6 [ | task/goal-oriented, theory/limits, MIMO]
- The Role of Fidelity in Goal-Oriented Semantic Communication: A Rate Distortion Approach — TCOM 2023, tcomm.2023.3274122, cpy 17.8 [ | task/goal-oriented, theory/limits]
- Neuromorphic Wireless Cognition: Event-Driven Semantic Communications for Remote Inference — TCCN 2023, tccn.2023.3236940, cpy 17.1 [ | task/goal-oriented]
- UAV Cognitive Semantic Communications Enabled by Knowledge Graph for Robust Object Detection — TCOM 2025, tcomm.2025.3538850, cpy 17.0 [ | task/goal-oriented, knowledge, UAV/vehicular/satellite, security/privacy]
- Goal-Oriented Semantic Communications for Robotic Waypoint Transmission: The Value and Age of Information Approach — TWC 2024, twc.2024.3424493, cpy 16.3 [ | task/goal-oriented]
- Multi-Device Task-Oriented Communication via Maximal Coding Rate Reduction — TWC 2024, twc.2024.3461336, cpy 15.2 [ | task/goal-oriented, multi-user/MA]
- Tackling Distribution Shifts in Task-Oriented Communication With Information Bottleneck — JSAC 2025, jsac.2025.3559116, cpy 15.1 [ | task/goal-oriented, theory/limits]
- Curriculum Learning for Goal-Oriented Semantic Communications With a Common Language — TCOM 2023, tcomm.2023.3236671, cpy 13.1 [text | task/goal-oriented]
- Goal-Oriented Semantic Communications for Avatar-Centric Augmented Reality — TCOM 2024, tcomm.2024.3420708, cpy 12.5 [ | task/goal-oriented]
- Goal-Oriented Scheduling in Sensor Networks With Application Timing Awareness — TCOM 2023, tcomm.2023.3282256, cpy 12.0 [ | task/goal-oriented, resource allocation]
- Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design — TCOM 2025, tcomm.2025.3563657, cpy 11.9 [feature/inference | generative/LLM, task/goal-oriented]
- Resource Allocation and Common Message Selection for Task-Oriented Semantic Information Transmission With RSMA — TWC 2024, twc.2023.3327127, cpy 11.5 [ | task/goal-oriented, multi-user/MA, resource allocation]
- Task-Oriented Scene Graph-Based Semantic Communications With Adaptive Channel Coding — TWC 2024, twc.2024.3450697, cpy 11.4 [ | task/goal-oriented, adaptive]
- Multi-Scale Semantic Communication for Object Detection: Single and Cross-Domain Scenarios — TWC 2025, twc.2025.3552255, cpy 11.1 [ | task/goal-oriented]
- Goal-Oriented Semantic Communication for Wireless Visual Question Answering — JSAC 2025, jsac.2025.3623184, cpy 11.0 [image | task/goal-oriented]
- Goal-Oriented Wireless Communication Resource Allocation for Cyber-Physical Systems — TWC 2024, twc.2024.3432918, cpy 10.4 [ | task/goal-oriented, resource allocation]
- Task-Oriented Low-Label Semantic Communication With Self-Supervised Learning — TWC 2025, twc.2025.3574468, cpy 10.0 [ | task/goal-oriented]
- Task-Oriented Communication for Graph Data: A Graph Information Bottleneck Approach — TCCN 2025, tccn.2024.3465651, cpy 9.7 [ | task/goal-oriented, theory/limits]
- Task-Oriented Delay-Aware Multi-Tier Computing in Cell-Free Massive MIMO Systems — JSAC 2023, jsac.2023.3280965, cpy 9.5 [ | task/goal-oriented, MIMO]
- Task-Oriented Semantic Communication for Stereo-Vision 3D Object Detection — TCOM 2025, tcomm.2025.3545687, cpy 9.2 [image, point-cloud/3D | task/goal-oriented]
- AoI-Aware Interference Mitigation for Task-Oriented Multicasting in Multi-Cell NOMA Networks — TWC 2024, twc.2024.3381480, cpy 9.1 [ | task/goal-oriented, multi-user/MA]
- Goal-Oriented Quantization: Analysis, Design, and Application to Resource Allocation — JSAC 2023, jsac.2022.3221976, cpy 8.5 [ | digital/modulation, task/goal-oriented, resource allocation]
- Task-Oriented Cross-System Design for Timely and Accurate Modeling in the Metaverse — JSAC 2024, jsac.2023.3345398, cpy 8.1 [ | task/goal-oriented]
- Goal-Oriented Tensor: Beyond Age of Information Toward Semantics-Empowered Goal-Oriented Communications — TCOM 2024, tcomm.2024.3416864, cpy 8.1 [ | task/goal-oriented]
- Edge Learning for Large-Scale Internet of Things With Task-Oriented Efficient Communication — TWC 2023, twc.2023.3271665, cpy 7.7 [ | task/goal-oriented]
- Goal-Oriented Communication, Estimation, and Control Over Bidirectional Wireless Links — TCOM 2025, tcomm.2024.3485572, cpy 7.7 [ | task/goal-oriented]
- Task-Oriented Communication Design at Scale — TCOM 2025, tcomm.2024.3416898, cpy 6.8 [ | task/goal-oriented]
- Unified Timing Analysis for Closed-Loop Goal-Oriented Wireless Communication — TWC 2025, twc.2024.3525087, cpy 6.6 [ | task/goal-oriented]
- Dynamic Semantic Compression for CNN Inference in Multi-Access Edge Computing: A Graph Reinforcement Learning-Based Autoencoder — TWC 2025, twc.2024.3518399, cpy 6.3 [ | task/goal-oriented, reinforcement learning]
- Timeliness of Information for Computation-Intensive Status Updates in Task-Oriented Communications — JSAC 2023, jsac.2022.3229431, cpy 5.8 [ | task/goal-oriented]
- Blind Goal-Oriented Massive Access for Future Wireless Networks — TSP 2023, tsp.2023.3254140, cpy 4.8 [ | task/goal-oriented]

### topic:(none in title)（48）
- Deep Learning Enabled Semantic Communication Systems — TSP 2021, tsp.2021.3071210, cpy 308.7
- Semantic Communication Systems for Speech Transmission — JSAC 2021, jsac.2021.3087240, cpy 130.8 [speech/audio | ]
- A Unified Multi-Task Semantic Communication System for Multimodal Data — TCOM 2024, tcomm.2024.3364990, cpy 96.5 [multimodal | ]
- Deep Learning Enabled Semantic Communications With Speech Recognition and Synthesis — TWC 2023, twc.2023.3240969, cpy 91.9 [speech/audio | ]
- Toward Semantic Communications: Deep Learning-Based Image Semantic Coding — JSAC 2023, jsac.2022.3221999, cpy 91.8 [image | ]
- A Lite Distributed Semantic Communication System for Internet of Things — JSAC 2021, jsac.2020.3036968, cpy 86.3
- Wireless Deep Video Semantic Transmission — JSAC 2023, jsac.2022.3221977, cpy 74.0 [video | ]
- Wireless Semantic Communications for Video Conferencing — JSAC 2023, jsac.2022.3221968, cpy 72.1 [video | ]
- Deep Learning-Enabled Semantic Communication Systems With Task-Unaware Transmitter and Dynamic Data — JSAC 2023, jsac.2022.3221991, cpy 68.9
- Semantic-Preserved Communication System for Highly Efficient Speech Transmission — JSAC 2023, jsac.2022.3221952, cpy 59.6 [speech/audio | ]
- DeepWiVe: Deep-Learning-Aided Wireless Video Transmission — JSAC 2022, jsac.2022.3191354, cpy 52.1 [video | ]
- AI-Generated Incentive Mechanism and Full-Duplex Semantic Communications for Information Sharing — JSAC 2023, jsac.2023.3287547, cpy 39.8
- Semantic Communication System Based on Semantic Slice Models Propagation — JSAC 2023, jsac.2022.3221948, cpy 38.6
- The Age of Incorrect Information: An Enabler of Semantics-Empowered Communication — TWC 2023, twc.2022.3213227, cpy 34.2
- Contrastive Learning-Based Semantic Communications — TCOM 2024, tcomm.2024.3400912, cpy 26.9
- Semantic Communication With Memory — JSAC 2023, jsac.2023.3288236, cpy 26.1
- Visual Language Model-Based Cross-Modal Semantic Communication Systems — TWC 2025, twc.2025.3539526, cpy 25.3 [image, multimodal | ]
- Semantic-Aware Remote Estimation of Multiple Markov Sources Under Constraints — TCOM 2025, tcomm.2025.3571950, cpy 24.0
- Environment Semantics Aided Wireless Communications: A Case Study of mmWave Beam Prediction and Blockage Prediction — JSAC 2023, jsac.2023.3280966, cpy 22.4
- Neuro-Symbolic Causal Reasoning Meets Signaling Game for Emergent Semantic Communications — TWC 2024, twc.2023.3319981, cpy 21.4
- Synchronous Multi-Modal Semantic Communication System With Packet-Level Coding — TWC 2025, twc.2025.3534995, cpy 19.6 [multimodal | ]
- Imitation Learning-Based Implicit Semantic-Aware Communication Networks: Multi-Layer Representation and Collaborative Reasoning — JSAC 2023, jsac.2022.3229419, cpy 18.9
- The Semantic Communication Game — TCCN 2018, tccn.2018.2872596, cpy 18.2
- SCSC: A Novel Standards-Compatible Semantic Communication Framework for Image Transmission — TCOM 2025, tcomm.2025.3529221, cpy 17.9 [image | ]
- Semantics-Native Communication via Contextual Reasoning — TCCN 2023, tccn.2023.3250206, cpy 17.4
- Semantic Communication Enabled 6G-NTN Framework: A Novel Denoising and Gateway Hop Integration Mechanism — TWC 2025, twc.2025.3578010, cpy 17.0
- Progressive Learned Image Transmission for Semantic Communication Using Hierarchical VAE — TCCN 2025, tccn.2025.3546935, cpy 17.0 [image | ]
- ISCom: Interest-Aware Semantic Communication Scheme for Point Cloud Video Streaming on Metaverse XR Devices — JSAC 2024, jsac.2023.3345430, cpy 15.5 [video, point-cloud/3D | ]
- Beamforming Design for Semantic-Bit Coexisting Communication System — JSAC 2025, jsac.2025.3531537, cpy 15.2
- Semantic-Aware Sampling and Transmission in Real-Time Tracking Systems: A POMDP Approach — TCOM 2025, tcomm.2024.3511935, cpy 15.1
- Age of Information Versions: A Semantic View of Markov Source Monitoring — TCOM 2025, tcomm.2025.3616209, cpy 15.0
- Reasoning Over the Air: A Reasoning- Based Implicit Semantic-Aware Communication Framework — TWC 2024, twc.2023.3312115, cpy 14.8
- Image Generation With Supervised Selection Based on Multimodal Features for Semantic Communications — TCOM 2025, tcomm.2025.3615798, cpy 14.0 [image, multimodal, feature/inference | ]
- Semantic Coding for Text Transmission: An Iterative Design — TCCN 2022, tccn.2022.3192407, cpy 13.8 [text | ]
- Object-Attribute-Relation Representation-Based Video Semantic Communication — JSAC 2025, jsac.2025.3559115, cpy 12.7 [video | ]
- Toward Semantic Communication Protocols: A Probabilistic Logic Perspective — JSAC 2023, jsac.2023.3288268, cpy 11.7
- Hybrid Semantic-Shannon Communications — TWC 2024, twc.2024.3376998, cpy 10.5
- Context-Based Semantic Communication via Dynamic Programming — TCCN 2022, tccn.2022.3173056, cpy 9.8
- How to Evaluate Semantic Communications for Images With ViTScore Metric? — TCCN 2024, tccn.2024.3392803, cpy 9.0 [image | ]
- Machine Learning Enabled Heterogeneous Semantic and Bit Communication — TWC 2024, twc.2024.3397635, cpy 8.0
- Learning QoE of Mobile Video Transmission With Deep Neural Network: A Data-Driven Approach — JSAC 2019, jsac.2019.2904359, cpy 7.9 [video | ]
- Semantic Information Marketing in the Metaverse: A Learning-Based Contract Theory Framework — JSAC 2024, jsac.2023.3345402, cpy 7.7
- Semantic Filtering and Source Coding in Distributed Wireless Monitoring Systems — TCOM 2024, tcomm.2024.3362951, cpy 7.7
- Importance of Semantic Information Based on Semantic Value — TCOM 2024, tcomm.2024.3385915, cpy 7.2
- Scalable Video Transmission in Cache-Aided Device-to-Device Networks — TWC 2020, twc.2020.2981790, cpy 6.1 [video | ]
- Post-Deployment Fine-Tunable Semantic Communication — TWC 2025, twc.2024.3433479, cpy 5.7
- SC-PNC: Semantic Communication-Empowered Physical-Layer Network Coding — TCCN 2024, tccn.2024.3375506, cpy 5.5
- Reliable Extraction of Semantic Information and Rate of Innovation Estimation for Graph Signals — JSAC 2023, jsac.2022.3221950, cpy 3.2

### topic:resource allocation（37）
- Compression Ratio Allocation for Probabilistic Semantic Communication With RSMA — TCOM 2025, tcomm.2025.3548689, cpy 62.3 [ | multi-user/MA, resource allocation]
- Adaptable Semantic Compression and Resource Allocation for Task-Oriented Communications — TCCN 2024, tccn.2023.3346481, cpy 60.6 [ | task/goal-oriented, resource allocation]
- DRL-Driven Dynamic Resource Allocation for Task-Oriented Semantic Communication — TCOM 2023, tcomm.2023.3274145, cpy 58.3 [ | task/goal-oriented, resource allocation, reinforcement learning]
- Adaptive Resource Allocation for Semantic Communication Networks — TCOM 2024, tcomm.2024.3405355, cpy 57.1 [ | resource allocation, adaptive]
- Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks — TWC 2025, twc.2025.3569102, cpy 55.5 [ | resource allocation]
- Performance Optimization for Semantic Communications: An Attention-Based Reinforcement Learning Approach — JSAC 2022, jsac.2022.3191112, cpy 55.2 [ | resource allocation, reinforcement learning, transformer/attention]
- Energy Efficient Semantic Communication Over Wireless Networks With Rate Splitting — JSAC 2023, jsac.2023.3240713, cpy 52.8 [feature/inference | multi-user/MA, resource allocation]
- Resource Allocation for Multi-Modal Semantic Communication in UAV Collaborative Networks — TCOM 2025, tcomm.2025.3552303, cpy 41.2 [multimodal | UAV/vehicular/satellite, resource allocation]
- Optimization of Image Transmission in Cooperative Semantic Communication Networks — TWC 2024, twc.2023.3282906, cpy 39.6 [image | relay/cooperative, resource allocation]
- Generative Semantic Communications With Foundation Models: Perception-Error Analysis and Semantic-Aware Power Allocation — JSAC 2025, jsac.2025.3559120, cpy 38.1 [ | generative/LLM, resource allocation]
- Energy-Efficient Edge Inference in Integrated Sensing, Communication, and Computation Networks — JSAC 2025, jsac.2025.3574612, cpy 32.7 [feature/inference | task/goal-oriented, sensing/ISAC, resource allocation]
- Deep Reinforcement Learning-Based Resource Allocation for Hybrid Bit and Generative Semantic Communications in Space-Air-Ground Integrated Networks — JSAC 2025, jsac.2025.3623157, cpy 32.0 [ | generative/LLM, resource allocation, reinforcement learning]
- Optimizing Resource Allocation for Multi-Modal Semantic Communication in Mobile AIGC Networks: A Diffusion-Based Game Approach — TCCN 2025, tccn.2025.3529747, cpy 30.7 [multimodal | generative/LLM, resource allocation]
- QoE-Based Semantic-Aware Resource Allocation for Multi-Task Networks — TWC 2024, twc.2024.3386807, cpy 26.8 [ | resource allocation]
- Feature Importance-Aware Task-Oriented Semantic Transmission and Optimization — TCCN 2024, tccn.2024.3375496, cpy 26.2 [feature/inference | task/goal-oriented, resource allocation]
- Feature Allocation for Semantic Communication With Space-Time Importance Awareness — TWC 2025, twc.2025.3569320, cpy 24.8 [feature/inference | resource allocation]
- Resource Optimization for Semantic-Aware Networks With Task Offloading — TWC 2024, twc.2024.3390407, cpy 23.9 [ | resource allocation]
- Resource Allocation for Multiuser Edge Inference With Batching and Early Exiting — JSAC 2023, jsac.2023.3242724, cpy 23.9 [feature/inference | task/goal-oriented, multi-user/MA, resource allocation]
- IRS-Enhanced Secure Semantic Communication Networks: Cross-Layer and Context-Awared Resource Allocation — TWC 2025, twc.2024.3495720, cpy 22.7 [ | RIS, resource allocation, security/privacy]
- UAV-Enabled Semantic Communication in Mobile Edge Computing Under Jamming Attacks: An Intelligent Resource Management Approach — TWC 2024, twc.2024.3454073, cpy 21.8 [ | UAV/vehicular/satellite, resource allocation, security/privacy]
- Joint Semantic Transmission and Resource Allocation for Intelligent Computation Task Offloading in MEC Systems — TWC 2025, twc.2025.3568870, cpy 16.9 [ | resource allocation]
- Semantic Information Extraction and Multi-Agent Communication Optimization Based on Generative Pre-Trained Transformer — TCCN 2025, tccn.2024.3482354, cpy 15.9 [ | generative/LLM, resource allocation, transformer/attention]
- Resource Allocation for Semantic-Aware Wireless Communication Networks With Imperfect CSI — TWC 2025, twc.2025.3575444, cpy 15.0 [ | resource allocation]
- Semantic Utility Loss of Information for Energy Efficient Semantic Status Update Communications — TCCN 2025, tccn.2024.3417627, cpy 14.3 [ | resource allocation]
- Semantic Knowledge Base-Enabled Zero-Shot Multi-Level Feature Transmission Optimization — TWC 2024, twc.2023.3323380, cpy 13.6 [feature/inference | knowledge, resource allocation]
- Wireless Resource Optimization in Hybrid Semantic/Bit Communication Networks — TCOM 2025, tcomm.2024.3485582, cpy 13.3 [ | resource allocation]
- Joint URLLC Traffic Scheduling and Resource Allocation for Semantic Communication Systems — TWC 2024, twc.2023.3339239, cpy 12.4 [ | resource allocation]
- Goal-Oriented Scheduling in Sensor Networks With Application Timing Awareness — TCOM 2023, tcomm.2023.3282256, cpy 12.0 [ | task/goal-oriented, resource allocation]
- Resource Allocation and Common Message Selection for Task-Oriented Semantic Information Transmission With RSMA — TWC 2024, twc.2023.3327127, cpy 11.5 [ | task/goal-oriented, multi-user/MA, resource allocation]
- Goal-Oriented Wireless Communication Resource Allocation for Cyber-Physical Systems — TWC 2024, twc.2024.3432918, cpy 10.4 [ | task/goal-oriented, resource allocation]
- Capacity Optimizing Resource Allocation in Joint Source-Channel Coding Systems With QoS Constraints — TCOM 2025, tcomm.2024.3496714, cpy 10.4 [ | JSCC, theory/limits, resource allocation]
- Dynamic Resource Allocation for Real-Time Cloud XR Video Transmission: A Reinforcement Learning Approach — TCCN 2024, tccn.2024.3352982, cpy 9.8 [video | resource allocation, reinforcement learning]
- Goal-Oriented Quantization: Analysis, Design, and Application to Resource Allocation — JSAC 2023, jsac.2022.3221976, cpy 8.5 [ | digital/modulation, task/goal-oriented, resource allocation]
- Resource Allocation for the Training of Image Semantic Communication Networks — TWC 2025, twc.2025.3527014, cpy 7.3 [image | resource allocation]
- Semantic Feature Scheduling and Rate Control in Multi-Modal Distributed Network — TWC 2024, twc.2024.3480352, cpy 6.0 [multimodal, feature/inference | resource allocation]
- Max-Min Resource Allocation for Video Transmission in NOMA-Based Cognitive Wireless Networks — TCOM 2018, tcomm.2018.2854584, cpy 4.9 [video | multi-user/MA, resource allocation]
- Distortion-Aware Cross-Layer Power Allocation for Video Transmission Over Multi-User NOMA Systems — TWC 2021, twc.2020.3030785, cpy 3.5 [video | multi-user/MA, resource allocation]

### topic:multi-user/MA（28）
- Task-Oriented Multi-User Semantic Communications — JSAC 2022, jsac.2022.3191326, cpy 113.4 [ | task/goal-oriented, multi-user/MA]
- Task-Oriented Sensing, Computation, and Communication Integration for Multi-Device Edge AI — TWC 2024, twc.2023.3303232, cpy 94.5 [ | task/goal-oriented, multi-user/MA, sensing/ISAC]
- Compression Ratio Allocation for Probabilistic Semantic Communication With RSMA — TCOM 2025, tcomm.2025.3548689, cpy 62.3 [ | multi-user/MA, resource allocation]
- Task-Oriented Communication for Multidevice Cooperative Edge Inference — TWC 2023, twc.2022.3191118, cpy 57.7 [feature/inference | task/goal-oriented, multi-user/MA, relay/cooperative]
- Energy Efficient Semantic Communication Over Wireless Networks With Rate Splitting — JSAC 2023, jsac.2023.3240713, cpy 52.8 [feature/inference | multi-user/MA, resource allocation]
- Heterogeneous Semantic and Bit Communications: A Semi-NOMA Scheme — JSAC 2023, jsac.2022.3222000, cpy 42.6 [ | multi-user/MA]
- Task-Oriented Over-the-Air Computation for Multi-Device Edge AI — TWC 2024, twc.2023.3294703, cpy 32.4 [ | task/goal-oriented, multi-user/MA]
- Non-Orthogonal Multiple Access Enhanced Multi-User Semantic Communication — TCCN 2023, tccn.2023.3306852, cpy 29.9 [ | multi-user/MA]
- DeepMA: End-to-End Deep Multiple Access for Wireless Image Transmission in Semantic Communication — TCCN 2024, tccn.2023.3326302, cpy 28.3 [image | multi-user/MA]
- Exploiting Semantic Communication for Non-Orthogonal Multiple Access — JSAC 2023, jsac.2023.3288242, cpy 27.7 [ | multi-user/MA]
- Resource Allocation for Multiuser Edge Inference With Batching and Early Exiting — JSAC 2023, jsac.2023.3242724, cpy 23.9 [feature/inference | task/goal-oriented, multi-user/MA, resource allocation]
- Age of Incorrect Information Minimization for Semantic-Empowered NOMA System in S-IoT — TWC 2024, twc.2023.3334761, cpy 18.8 [ | multi-user/MA]
- Task-Oriented Semantic Communication over Rate Splitting Enabled Wireless Control Systems for URLLC Services — TCOM 2024, tcomm.2023.3325901, cpy 18.7 [feature/inference | task/goal-oriented, multi-user/MA]
- Multi-Device Task-Oriented Communication via Maximal Coding Rate Reduction — TWC 2024, twc.2024.3461336, cpy 15.2 [ | task/goal-oriented, multi-user/MA]
- Rate Splitting Multiple Access-Enabled Adaptive Panoramic Video Semantic Transmission — TWC 2025, twc.2025.3570465, cpy 15.0 [video, feature/inference | multi-user/MA, adaptive]
- Generative AI Empowered Semantic Feature Multiple Access (SFMA) Over Wireless Networks — TCCN 2025, tccn.2025.3529692, cpy 13.9 [feature/inference | generative/LLM, multi-user/MA]
- Adaptive Semantic Generation and NOMA-Based Interference-Aware Transmission for 6G Networks — TWC 2025, twc.2024.3520870, cpy 13.2 [ | multi-user/MA, adaptive]
- Resource Allocation and Common Message Selection for Task-Oriented Semantic Information Transmission With RSMA — TWC 2024, twc.2023.3327127, cpy 11.5 [ | task/goal-oriented, multi-user/MA, resource allocation]
- Features Disentangled Semantic Broadcast Communication Networks — TWC 2024, twc.2023.3334225, cpy 11.5 [feature/inference | multi-user/MA]
- Deep Learning-Based Superposition Coded Modulation for Hierarchical Semantic Communications Over Broadcast Channels — TCOM 2025, tcomm.2024.3447870, cpy 11.3 [ | digital/modulation, multi-user/MA]
- AoI-Aware Interference Mitigation for Task-Oriented Multicasting in Multi-Cell NOMA Networks — TWC 2024, twc.2024.3381480, cpy 9.1 [ | task/goal-oriented, multi-user/MA]
- Semantic Feature Division Multiple Access for Multi-User Digital Interference Networks — TWC 2024, twc.2024.3427675, cpy 9.0 [image, feature/inference | digital/modulation, multi-user/MA]
- Interference Suppressed NOMA for Semantic-Aware Communication Networks — TWC 2024, twc.2024.3371775, cpy 7.8 [ | multi-user/MA]
- Compression Before Fusion: Broadcast Semantic Communication System for Heterogeneous Tasks — TWC 2024, twc.2024.3483314, cpy 6.5 [ | multi-user/MA]
- Max-Min Resource Allocation for Video Transmission in NOMA-Based Cognitive Wireless Networks — TCOM 2018, tcomm.2018.2854584, cpy 4.9 [video | multi-user/MA, resource allocation]
- Distortion-Aware Cross-Layer Power Allocation for Video Transmission Over Multi-User NOMA Systems — TWC 2021, twc.2020.3030785, cpy 3.5 [video | multi-user/MA, resource allocation]
- QoE-Driven Multi-User Video Transmission Over SM-NOMA Integrated Systems — JSAC 2019, jsac.2019.2929382, cpy 2.7 [video | multi-user/MA]
- Optimal Multi-View Video Transmission in Multiuser Wireless Networks by Exploiting Natural and View Synthesis-Enabled Multicast Opportunities — TCOM 2020, tcomm.2019.2954523, cpy 2.4 [video | multi-user/MA]

### topic:JSCC（25）
- Deep Joint Source-Channel Coding for Wireless Image Transmission — TCCN 2019, tccn.2019.2919300, cpy 213.2 [image | JSCC]
- SwinJSCC: Taming Swin Transformer for Deep Joint Source-Channel Coding — TCCN 2025, tccn.2024.3424842, cpy 142.7 [ | JSCC, transformer/attention]
- Nonlinear Transform Source-Channel Coding for Semantic Communications — JSAC 2022, jsac.2022.3180802, cpy 90.1 [ | JSCC]
- DeepJSCC- <i>f</i> : Deep Joint Source-Channel Coding of Images With Feedback — JSAIT 2020, jsait.2020.2987203, cpy 75.5 [image | JSCC, feedback/HARQ]
- Generative Joint Source-Channel Coding for Semantic Image Transmission — JSAC 2023, jsac.2023.3288243, cpy 65.8 [image | JSCC, generative/LLM]
- Deep Joint Source-Channel Coding for Adaptive Image Transmission Over MIMO Channels — TWC 2024, twc.2024.3422794, cpy 58.3 [image | JSCC, MIMO, adaptive]
- Joint Source-Channel Coding for Channel-Adaptive Digital Semantic Communications — TCCN 2025, tccn.2024.3422496, cpy 49.6 [ | JSCC, digital/modulation, adaptive]
- D²-JSCC: Digital Deep Joint Source-Channel Coding for Semantic Communications — JSAC 2025, jsac.2025.3531546, cpy 46.4 [ | JSCC, digital/modulation]
- OFDM-Guided Deep Joint Source Channel Coding for Wireless Multipath Fading Channels — TCCN 2022, tccn.2022.3151935, cpy 46.1 [ | JSCC, OFDM]
- Deep Source-Channel Coding for Sentence Semantic Transmission With HARQ — TCOM 2022, tcomm.2022.3180997, cpy 44.3 [text | JSCC, feedback/HARQ]
- Bandwidth-Agile Image Transmission With Deep Joint Source-Channel Coding — TWC 2021, twc.2021.3090048, cpy 40.3 [image | JSCC, adaptive]
- DeepJSCC-Q: Constellation Constrained Deep Joint Source-Channel Coding — JSAIT 2022, jsait.2022.3231042, cpy 39.8 [ | JSCC, digital/modulation]
- Deep Joint Source-Channel Coding for CSI Feedback: An End-to-End Approach — JSAC 2023, jsac.2022.3221963, cpy 22.6 [ | JSCC, feedback/HARQ]
- Toward Adaptive Semantic Communications: Efficient Data Transmission via Online Learned Nonlinear Transform Source-Channel Coding — JSAC 2023, jsac.2023.3288246, cpy 19.5 [ | JSCC, adaptive]
- Process-and-Forward: Deep Joint Source-Channel Coding Over Cooperative Relay Networks — JSAC 2025, jsac.2025.3531579, cpy 18.6 [ | JSCC, relay/cooperative]
- Deep Joint Source-Channel Coding for Image Transmission With Visual Protection — TCCN 2023, tccn.2023.3306851, cpy 13.7 [image | JSCC]
- Universal Joint Source-Channel Coding for Modulation-Agnostic Semantic Communication — JSAC 2025, jsac.2025.3559138, cpy 12.7 [ | JSCC, digital/modulation]
- Joint Source-Channel Coding Over Additive Noise Analog Channels Using Mixture of Variational Autoencoders — JSAC 2021, jsac.2021.3078489, cpy 11.0 [ | JSCC]
- Capacity Optimizing Resource Allocation in Joint Source-Channel Coding Systems With QoS Constraints — TCOM 2025, tcomm.2024.3496714, cpy 10.4 [ | JSCC, theory/limits, resource allocation]
- Joint Component Design for the JSCC System Based on DP-LDPC Codes — TCOM 2020, tcomm.2020.3001647, cpy 7.4 [ | JSCC]
- Concatenated Spatially Coupled LDPC Codes With Sliding Window Decoding for Joint Source-Channel Coding — TCOM 2022, tcomm.2021.3126750, cpy 6.8 [ | JSCC]
- Low-Delay Analog Joint Source-Channel Coding With Deep Learning — TCOM 2023, tcomm.2022.3222874, cpy 6.7 [ | JSCC]
- Rate-Distortion-Perception Controllable Joint Source-Channel Coding for High-Fidelity Generative Semantic Communications — TCCN 2025, tccn.2024.3511960, cpy 6.6 [ | JSCC, generative/LLM, theory/limits]
- A New Joint Source-Channel Coding for Short-Packet Communications — TCOM 2024, tcomm.2023.3320699, cpy 6.5 [ | JSCC]
- Joint Code Rate Compatible Design of DP-LDPC Code Pairs for Joint Source Channel Coding Over Implant-to-External Channel — TWC 2022, twc.2022.3141729, cpy 4.5 [ | JSCC]

### topic:adaptive（21）
- Predictive and Adaptive Deep Coding for Wireless Image Transmission in Semantic Communication — TWC 2023, twc.2023.3234408, cpy 86.3 [image | adaptive]
- Deep Joint Source-Channel Coding for Adaptive Image Transmission Over MIMO Channels — TWC 2024, twc.2024.3422794, cpy 58.3 [image | JSCC, MIMO, adaptive]
- Adaptive Resource Allocation for Semantic Communication Networks — TCOM 2024, tcomm.2024.3405355, cpy 57.1 [ | resource allocation, adaptive]
- Joint Source-Channel Coding for Channel-Adaptive Digital Semantic Communications — TCCN 2025, tccn.2024.3422496, cpy 49.6 [ | JSCC, digital/modulation, adaptive]
- Bandwidth-Agile Image Transmission With Deep Joint Source-Channel Coding — TWC 2021, twc.2021.3090048, cpy 40.3 [image | JSCC, adaptive]
- SCAN: Semantic Communication With Adaptive Channel Feedback — TCCN 2024, tccn.2024.3394867, cpy 32.9 [ | feedback/HARQ, adaptive]
- R-ACP: Real-Time Adaptive Collaborative Perception Leveraging Robust Task-Oriented Communications — JSAC 2025, jsac.2025.3623179, cpy 31.0 [ | task/goal-oriented, security/privacy, adaptive]
- Digital-SC: Digital Semantic Communication With Adaptive Network Split and Learned Non-Linear Quantization — TCCN 2025, tccn.2024.3510586, cpy 27.2 [feature/inference | digital/modulation, adaptive]
- VideoQA-SC: Adaptive Semantic Communication for Video Question Answering — JSAC 2025, jsac.2025.3559160, cpy 23.0 [video | adaptive]
- Toward Adaptive Semantic Communications: Efficient Data Transmission via Online Learned Nonlinear Transform Source-Channel Coding — JSAC 2023, jsac.2023.3288246, cpy 19.5 [ | JSCC, adaptive]
- Rate-Adaptive Coding Mechanism for Semantic Communications With Multi-Modal Data — TCOM 2024, tcomm.2023.3335977, cpy 17.4 [multimodal | adaptive]
- Rate Splitting Multiple Access-Enabled Adaptive Panoramic Video Semantic Transmission — TWC 2025, twc.2025.3570465, cpy 15.0 [video, feature/inference | multi-user/MA, adaptive]
- Blind Training for Channel-Adaptive Digital Semantic Communications — TCOM 2025, tcomm.2025.3585587, cpy 14.0 [ | digital/modulation, adaptive]
- Adaptive Modulation and Retransmission Scheme for Semantic Communication Systems — TCCN 2024, tccn.2023.3315386, cpy 13.5 [ | digital/modulation, feedback/HARQ, adaptive]
- Adaptive Semantic Generation and NOMA-Based Interference-Aware Transmission for 6G Networks — TWC 2025, twc.2024.3520870, cpy 13.2 [ | multi-user/MA, adaptive]
- Semantic Prior Aided Channel-Adaptive Equalizing and De-Noising Semantic Communication System With Latent Diffusion Model — TWC 2025, twc.2025.3543167, cpy 12.7 [ | generative/LLM, adaptive]
- Adaptive Information Bottleneck Guided Joint Source and Channel Coding for Image Transmission — JSAC 2023, jsac.2023.3288238, cpy 12.6 [image | theory/limits, adaptive]
- Transmit What You Need: Task-Adaptive Semantic Communications for Visual Information — JSAC 2025, jsac.2025.3623159, cpy 12.0 [image | adaptive]
- Task-Oriented Scene Graph-Based Semantic Communications With Adaptive Channel Coding — TWC 2024, twc.2024.3450697, cpy 11.4 [ | task/goal-oriented, adaptive]
- RIS-Enhanced Semantic Communications Adaptive to User Requirements — TCOM 2024, tcomm.2024.3369697, cpy 10.2 [ | RIS, adaptive]
- Adaptive Bitrate Video Transmission Over Cognitive Radio Networks Using Cross Layer Routing Approach — TCCN 2020, tccn.2020.2990673, cpy 4.6 [video | adaptive]

### topic:generative/LLM（20）
- Generative AI-Driven Semantic Communication Networks: Architecture, Technologies, and Applications — TCCN 2025, tccn.2024.3435524, cpy 92.5 [ | generative/LLM]
- CDDM: Channel Denoising Diffusion Models for Wireless Semantic Communications — TWC 2024, twc.2024.3379244, cpy 84.1 [ | generative/LLM]
- Generative Joint Source-Channel Coding for Semantic Image Transmission — JSAC 2023, jsac.2023.3288243, cpy 65.8 [image | JSCC, generative/LLM]
- Beyond the Cloud: Edge Inference for Generative Large Language Models in Wireless Networks — TWC 2025, twc.2024.3497923, cpy 46.6 [feature/inference | generative/LLM, task/goal-oriented]
- Diffusion-Driven Semantic Communication for Generative Models With Bandwidth Constraints — TWC 2025, twc.2025.3553851, cpy 42.6 [ | generative/LLM]
- Generative Semantic Communications With Foundation Models: Perception-Error Analysis and Semantic-Aware Power Allocation — JSAC 2025, jsac.2025.3559120, cpy 38.1 [ | generative/LLM, resource allocation]
- LaMoSC: Large Language Model-Driven Semantic Communication System for Visual Transmission — TCCN 2024, tccn.2024.3401712, cpy 38.0 [image | generative/LLM]
- Deep Reinforcement Learning-Based Resource Allocation for Hybrid Bit and Generative Semantic Communications in Space-Air-Ground Integrated Networks — JSAC 2025, jsac.2025.3623157, cpy 32.0 [ | generative/LLM, resource allocation, reinforcement learning]
- Optimizing Resource Allocation for Multi-Modal Semantic Communication in Mobile AIGC Networks: A Diffusion-Based Game Approach — TCCN 2025, tccn.2025.3529747, cpy 30.7 [multimodal | generative/LLM, resource allocation]
- Semantic Satellite Communications Based on Generative Foundation Model — JSAC 2025, jsac.2025.3559113, cpy 27.8 [ | generative/LLM, UAV/vehicular/satellite]
- Latent Diffusion Model-Enabled Low-Latency Semantic Communication in the Presence of Semantic Ambiguities and Wireless Channel Noises — TWC 2025, twc.2025.3535714, cpy 27.4 [ | generative/LLM]
- Semantic Successive Refinement: A Generative AI-Aided Semantic Communication Framework — TCCN 2025, tccn.2025.3526839, cpy 27.2 [ | generative/LLM]
- A GAN-Based Semantic Communication for Text Without CSI — TWC 2024, twc.2024.3415363, cpy 21.4 [text | generative/LLM]
- Agent-Driven Generative Semantic Communication With Cross-Modality and Prediction — TWC 2025, twc.2024.3519325, cpy 18.2 [multimodal | generative/LLM]
- Semantic Information Extraction and Multi-Agent Communication Optimization Based on Generative Pre-Trained Transformer — TCCN 2025, tccn.2024.3482354, cpy 15.9 [ | generative/LLM, resource allocation, transformer/attention]
- Generative AI Empowered Semantic Feature Multiple Access (SFMA) Over Wireless Networks — TCCN 2025, tccn.2025.3529692, cpy 13.9 [feature/inference | generative/LLM, multi-user/MA]
- Semantic Prior Aided Channel-Adaptive Equalizing and De-Noising Semantic Communication System With Latent Diffusion Model — TWC 2025, twc.2025.3543167, cpy 12.7 [ | generative/LLM, adaptive]
- Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design — TCOM 2025, tcomm.2025.3563657, cpy 11.9 [feature/inference | generative/LLM, task/goal-oriented]
- Semantic Knowledge Base Empowered Generative Semantic Communication — TCOM 2025, tcomm.2025.3585683, cpy 11.0 [ | generative/LLM, knowledge]
- Rate-Distortion-Perception Controllable Joint Source-Channel Coding for High-Fidelity Generative Semantic Communications — TCCN 2025, tccn.2024.3511960, cpy 6.6 [ | JSCC, generative/LLM, theory/limits]

### topic:digital/modulation（19）
- Robust Semantic Communications With Masked VQ-VAE Enabled Codebook — TWC 2023, twc.2023.3265201, cpy 104.5 [ | digital/modulation, security/privacy]
- Joint Coding-Modulation for Digital Semantic Communications via Variational Autoencoder — TCOM 2024, tcomm.2024.3386577, cpy 69.8 [ | digital/modulation]
- Joint Source-Channel Coding for Channel-Adaptive Digital Semantic Communications — TCCN 2025, tccn.2024.3422496, cpy 49.6 [ | JSCC, digital/modulation, adaptive]
- D²-JSCC: Digital Deep Joint Source-Channel Coding for Semantic Communications — JSAC 2025, jsac.2025.3531546, cpy 46.4 [ | JSCC, digital/modulation]
- Robust Information Bottleneck for Task-Oriented Communication With Digital Modulation — JSAC 2023, jsac.2023.3288252, cpy 40.9 [ | digital/modulation, task/goal-oriented, theory/limits, security/privacy]
- DeepJSCC-Q: Constellation Constrained Deep Joint Source-Channel Coding — JSAIT 2022, jsait.2022.3231042, cpy 39.8 [ | JSCC, digital/modulation]
- OFDM-Based Digital Semantic Communication With Importance Awareness — TCOM 2024, tcomm.2024.3397862, cpy 36.3 [ | digital/modulation, OFDM]
- Digital-SC: Digital Semantic Communication With Adaptive Network Split and Learned Non-Linear Quantization — TCCN 2025, tccn.2024.3510586, cpy 27.2 [feature/inference | digital/modulation, adaptive]
- From Analog to Digital: Multi-Order Digital Joint Coding-Modulation for Semantic Communication — TCOM 2025, tcomm.2024.3511949, cpy 25.3 [ | digital/modulation]
- sDAC—Semantic Digital Analog Converter for Semantic Communications — TCOM 2025, tcomm.2025.3566976, cpy 23.0 [ | digital/modulation]
- Improving Learning-Based Semantic Coding Efficiency for Image Transmission via Shared Semantic-Aware Codebook — TCOM 2025, tcomm.2024.3450877, cpy 16.1 [image | digital/modulation]
- Blind Training for Channel-Adaptive Digital Semantic Communications — TCOM 2025, tcomm.2025.3585587, cpy 14.0 [ | digital/modulation, adaptive]
- Adaptive Modulation and Retransmission Scheme for Semantic Communication Systems — TCCN 2024, tccn.2023.3315386, cpy 13.5 [ | digital/modulation, feedback/HARQ, adaptive]
- Universal Joint Source-Channel Coding for Modulation-Agnostic Semantic Communication — JSAC 2025, jsac.2025.3559138, cpy 12.7 [ | JSCC, digital/modulation]
- Causal Semantic Communication for Digital Twins: A Generalizable Imitation Learning Approach — JSAIT 2023, jsait.2023.3336538, cpy 12.3 [ | digital/modulation]
- Deep Learning-Based Superposition Coded Modulation for Hierarchical Semantic Communications Over Broadcast Channels — TCOM 2025, tcomm.2024.3447870, cpy 11.3 [ | digital/modulation, multi-user/MA]
- Semantic Feature Division Multiple Access for Multi-User Digital Interference Networks — TWC 2024, twc.2024.3427675, cpy 9.0 [image, feature/inference | digital/modulation, multi-user/MA]
- Goal-Oriented Quantization: Analysis, Design, and Application to Resource Allocation — JSAC 2023, jsac.2022.3221976, cpy 8.5 [ | digital/modulation, task/goal-oriented, resource allocation]
- Hybrid Digital-Analog Semantic Communications — JSAC 2025, jsac.2025.3559149, cpy 7.9 [ | digital/modulation]

### topic:security/privacy（17）
- Robust Semantic Communications With Masked VQ-VAE Enabled Codebook — TWC 2023, twc.2023.3265201, cpy 104.5 [ | digital/modulation, security/privacy]
- A Robust Image Semantic Communication System With Multi-Scale Vision Transformer — JSAC 2025, jsac.2025.3531413, cpy 41.8 [image | security/privacy, transformer/attention]
- Robust Information Bottleneck for Task-Oriented Communication With Digital Modulation — JSAC 2023, jsac.2023.3288252, cpy 40.9 [ | digital/modulation, task/goal-oriented, theory/limits, security/privacy]
- A Robust Semantic Text Communication System — TWC 2024, twc.2024.3381950, cpy 38.2 [text | security/privacy]
- Privacy-Preserving Task-Oriented Semantic Communications Against Model Inversion Attacks — TWC 2024, twc.2024.3369170, cpy 33.6 [ | task/goal-oriented, security/privacy]
- R-ACP: Real-Time Adaptive Collaborative Perception Leveraging Robust Task-Oriented Communications — JSAC 2025, jsac.2025.3623179, cpy 31.0 [ | task/goal-oriented, security/privacy, adaptive]
- Physical-Layer Adversarial Robustness for Deep Learning-Based Semantic Communications — JSAC 2023, jsac.2023.3288249, cpy 29.0 [ | security/privacy]
- IRS-Enhanced Secure Semantic Communication Networks: Cross-Layer and Context-Awared Resource Allocation — TWC 2025, twc.2024.3495720, cpy 22.7 [ | RIS, resource allocation, security/privacy]
- UAV-Enabled Semantic Communication in Mobile Edge Computing Under Jamming Attacks: An Intelligent Resource Management Approach — TWC 2024, twc.2024.3454073, cpy 21.8 [ | UAV/vehicular/satellite, resource allocation, security/privacy]
- Robust Image Semantic Coding With Learnable CSI Fusion Masking Over MIMO Fading Channels — TWC 2024, twc.2024.3409735, cpy 17.4 [image | MIMO, security/privacy]
- UAV Cognitive Semantic Communications Enabled by Knowledge Graph for Robust Object Detection — TCOM 2025, tcomm.2025.3538850, cpy 17.0 [ | task/goal-oriented, knowledge, UAV/vehicular/satellite, security/privacy]
- A Physical Layer Security Framework for IRS-Assisted Integrated Sensing and Semantic Communication Systems — TCCN 2025, tccn.2025.3589577, cpy 10.9 [ | RIS, sensing/ISAC, security/privacy]
- Adversarial Attacks Against Shared Knowledge Interpretation in Semantic Communications — TCCN 2025, tccn.2025.3528891, cpy 9.9 [ | knowledge, security/privacy]
- GAI-Enhanced Robust Semantic Communication With Asymmetric Architecture — TCCN 2025, tccn.2024.3520132, cpy 7.3 [ | security/privacy]
- Disentangled Information Bottleneck Guided Privacy-Protective Joint Source and Channel Coding for Image Transmission — TCOM 2024, tcomm.2024.3406381, cpy 6.8 [image | theory/limits, security/privacy]
- Indoor Semantic Location Privacy Protection With Safe Reinforcement Learning — TCCN 2023, tccn.2023.3291364, cpy 5.7 [ | security/privacy, reinforcement learning]
- On Learning-Assisted Content-Based Secure Image Transmission for Delay-Aware Systems With Randomly-Distributed Eavesdroppers — TCOM 2022, tcomm.2021.3128423, cpy 4.9 [image | security/privacy]

### topic:UAV/vehicular/satellite（15）
- Multi-Functional RIS-Assisted Semantic Anti-Jamming Communication and Computing in Integrated Aerial-Ground Networks — JSAC 2024, jsac.2024.3459028, cpy 90.1 [ | RIS, UAV/vehicular/satellite]
- Resource Allocation for Multi-Modal Semantic Communication in UAV Collaborative Networks — TCOM 2025, tcomm.2025.3552303, cpy 41.2 [multimodal | UAV/vehicular/satellite, resource allocation]
- Task-Oriented Image Transmission for Scene Classification in Unmanned Aerial Systems — TCOM 2022, tcomm.2022.3182325, cpy 34.7 [image | task/goal-oriented, UAV/vehicular/satellite]
- Semantic Communication in Satellite-Borne Edge Cloud Network for Computation Offloading — JSAC 2024, jsac.2024.3365879, cpy 30.9 [ | UAV/vehicular/satellite]
- Semantic Satellite Communications Based on Generative Foundation Model — JSAC 2025, jsac.2025.3559113, cpy 27.8 [ | generative/LLM, UAV/vehicular/satellite]
- UAV-Aided Radio Map Construction Exploiting Environment Semantics — TWC 2023, twc.2023.3241845, cpy 23.9 [ | UAV/vehicular/satellite]
- UAV-Enabled Semantic Communication in Mobile Edge Computing Under Jamming Attacks: An Intelligent Resource Management Approach — TWC 2024, twc.2024.3454073, cpy 21.8 [ | UAV/vehicular/satellite, resource allocation, security/privacy]
- Free Space Optical Semantic Communication for Satellite Remote Sensing Image Transmission — TCOM 2025, tcomm.2025.3562356, cpy 19.8 [image | UAV/vehicular/satellite, sensing/ISAC]
- Lyapunov-Guided Deep Reinforcement Learning for Semantic-Aware AoI Minimization in UAV-Assisted Wireless Networks — TWC 2025, twc.2025.3552809, cpy 19.6 [ | UAV/vehicular/satellite, reinforcement learning]
- Semantic Image Encoding and Communication for Earth Observation With LEO Satellites — TCCN 2025, tccn.2024.3451724, cpy 17.2 [image | UAV/vehicular/satellite]
- UAV Cognitive Semantic Communications Enabled by Knowledge Graph for Robust Object Detection — TCOM 2025, tcomm.2025.3538850, cpy 17.0 [ | task/goal-oriented, knowledge, UAV/vehicular/satellite, security/privacy]
- UAV Anti-Jamming Video Transmissions With QoE Guarantee: A Reinforcement Learning-Based Approach — TCOM 2021, tcomm.2021.3087787, cpy 15.7 [video | UAV/vehicular/satellite, reinforcement learning]
- xURLLC-Aware Service Provisioning in Vehicular Networks: A Semantic Communication Perspective — TWC 2024, twc.2023.3319442, cpy 12.8 [image | UAV/vehicular/satellite]
- R-UAV-Net: Enhanced YOLOv4 With Graph-Semantic Compression for Transformative UAV Sensing in Paddy Agronomy — TCCN 2025, tccn.2024.3452053, cpy 11.9 [ | UAV/vehicular/satellite, sensing/ISAC]
- Task-Driven Semantic-Aware Green Cooperative Transmission Strategy for Vehicular Networks — TCOM 2023, tcomm.2023.3300869, cpy 6.3 [ | relay/cooperative, UAV/vehicular/satellite]

### topic:theory/limits（12）
- Learning Task-Oriented Communication for Edge Inference: An Information Bottleneck Approach — JSAC 2022, jsac.2021.3126087, cpy 72.9 [feature/inference | task/goal-oriented, theory/limits]
- Robust Information Bottleneck for Task-Oriented Communication With Digital Modulation — JSAC 2023, jsac.2023.3288252, cpy 40.9 [ | digital/modulation, task/goal-oriented, theory/limits, security/privacy]
- End-to-End Learning for Task-Oriented Semantic Communications Over MIMO Channels: An Information-Theoretic Framework — JSAC 2025, jsac.2025.3531575, cpy 18.6 [ | task/goal-oriented, theory/limits, MIMO]
- The Role of Fidelity in Goal-Oriented Semantic Communication: A Rate Distortion Approach — TCOM 2023, tcomm.2023.3274122, cpy 17.8 [ | task/goal-oriented, theory/limits]
- Tackling Distribution Shifts in Task-Oriented Communication With Information Bottleneck — JSAC 2025, jsac.2025.3559116, cpy 15.1 [ | task/goal-oriented, theory/limits]
- An Indirect Rate-Distortion Characterization for Semantic Sources: General Model and the Case of Gaussian Observation — TCOM 2022, tcomm.2022.3194978, cpy 14.2 [ | theory/limits]
- Adaptive Information Bottleneck Guided Joint Source and Channel Coding for Image Transmission — JSAC 2023, jsac.2023.3288238, cpy 12.6 [image | theory/limits, adaptive]
- Performance Limits of a Deep Learning-Enabled Text Semantic Communication Under Interference — TWC 2024, twc.2024.3370497, cpy 11.0 [text | theory/limits]
- Capacity Optimizing Resource Allocation in Joint Source-Channel Coding Systems With QoS Constraints — TCOM 2025, tcomm.2024.3496714, cpy 10.4 [ | JSCC, theory/limits, resource allocation]
- Task-Oriented Communication for Graph Data: A Graph Information Bottleneck Approach — TCCN 2025, tccn.2024.3465651, cpy 9.7 [ | task/goal-oriented, theory/limits]
- Disentangled Information Bottleneck Guided Privacy-Protective Joint Source and Channel Coding for Image Transmission — TCOM 2024, tcomm.2024.3406381, cpy 6.8 [image | theory/limits, security/privacy]
- Rate-Distortion-Perception Controllable Joint Source-Channel Coding for High-Fidelity Generative Semantic Communications — TCCN 2025, tccn.2024.3511960, cpy 6.6 [ | JSCC, generative/LLM, theory/limits]

### topic:sensing/ISAC（8）
- Task-Oriented Sensing, Computation, and Communication Integration for Multi-Device Edge AI — TWC 2024, twc.2023.3303232, cpy 94.5 [ | task/goal-oriented, multi-user/MA, sensing/ISAC]
- Energy-Efficient Edge Inference in Integrated Sensing, Communication, and Computation Networks — JSAC 2025, jsac.2025.3574612, cpy 32.7 [feature/inference | task/goal-oriented, sensing/ISAC, resource allocation]
- Free Space Optical Semantic Communication for Satellite Remote Sensing Image Transmission — TCOM 2025, tcomm.2025.3562356, cpy 19.8 [image | UAV/vehicular/satellite, sensing/ISAC]
- Semantic-Aware Sensing Information Transmission for Metaverse: A Contest Theoretic Approach — TWC 2023, twc.2022.3232565, cpy 19.5 [ | sensing/ISAC]
- Semantic Communications for Wireless Sensing: RIS-Aided Encoding and Self-Supervised Decoding — JSAC 2023, jsac.2023.3288231, cpy 18.6 [ | RIS, sensing/ISAC]
- R-UAV-Net: Enhanced YOLOv4 With Graph-Semantic Compression for Transformative UAV Sensing in Paddy Agronomy — TCCN 2025, tccn.2024.3452053, cpy 11.9 [ | UAV/vehicular/satellite, sensing/ISAC]
- A Physical Layer Security Framework for IRS-Assisted Integrated Sensing and Semantic Communication Systems — TCCN 2025, tccn.2025.3589577, cpy 10.9 [ | RIS, sensing/ISAC, security/privacy]
- Fluid Antenna-Enabled Near-Field Integrated Sensing, Computing, and Semantic Communication for Emerging Applications — TCCN 2025, tccn.2025.3592294, cpy 9.9 [ | sensing/ISAC]

### topic:reinforcement learning（8）
- DRL-Driven Dynamic Resource Allocation for Task-Oriented Semantic Communication — TCOM 2023, tcomm.2023.3274145, cpy 58.3 [ | task/goal-oriented, resource allocation, reinforcement learning]
- Performance Optimization for Semantic Communications: An Attention-Based Reinforcement Learning Approach — JSAC 2022, jsac.2022.3191112, cpy 55.2 [ | resource allocation, reinforcement learning, transformer/attention]
- Deep Reinforcement Learning-Based Resource Allocation for Hybrid Bit and Generative Semantic Communications in Space-Air-Ground Integrated Networks — JSAC 2025, jsac.2025.3623157, cpy 32.0 [ | generative/LLM, resource allocation, reinforcement learning]
- Lyapunov-Guided Deep Reinforcement Learning for Semantic-Aware AoI Minimization in UAV-Assisted Wireless Networks — TWC 2025, twc.2025.3552809, cpy 19.6 [ | UAV/vehicular/satellite, reinforcement learning]
- UAV Anti-Jamming Video Transmissions With QoE Guarantee: A Reinforcement Learning-Based Approach — TCOM 2021, tcomm.2021.3087787, cpy 15.7 [video | UAV/vehicular/satellite, reinforcement learning]
- Dynamic Resource Allocation for Real-Time Cloud XR Video Transmission: A Reinforcement Learning Approach — TCCN 2024, tccn.2024.3352982, cpy 9.8 [video | resource allocation, reinforcement learning]
- Dynamic Semantic Compression for CNN Inference in Multi-Access Edge Computing: A Graph Reinforcement Learning-Based Autoencoder — TWC 2025, twc.2024.3518399, cpy 6.3 [ | task/goal-oriented, reinforcement learning]
- Indoor Semantic Location Privacy Protection With Safe Reinforcement Learning — TCCN 2023, tccn.2023.3291364, cpy 5.7 [ | security/privacy, reinforcement learning]

### topic:knowledge（8）
- Deep Learning-Empowered Semantic Communication Systems With a Shared Knowledge Base — TWC 2024, twc.2023.3330744, cpy 31.2 [ | knowledge]
- Cognitive Semantic Communication Systems Driven by Knowledge Graph: Principle, Implementation, and Performance Evaluation — TCOM 2024, tcomm.2023.3318605, cpy 25.7 [ | knowledge]
- Knowledge-Based Ultra-Low-Latency Semantic Communications for Robotic Edge Intelligence — TCOM 2025, tcomm.2024.3511931, cpy 18.3 [ | knowledge]
- UAV Cognitive Semantic Communications Enabled by Knowledge Graph for Robust Object Detection — TCOM 2025, tcomm.2025.3538850, cpy 17.0 [ | task/goal-oriented, knowledge, UAV/vehicular/satellite, security/privacy]
- Semantic Knowledge Base-Enabled Zero-Shot Multi-Level Feature Transmission Optimization — TWC 2024, twc.2023.3323380, cpy 13.6 [feature/inference | knowledge, resource allocation]
- Knowledge Distillation-Based Semantic Communications for Multiple Users — TWC 2024, twc.2023.3336941, cpy 12.8 [ | knowledge]
- Semantic Knowledge Base Empowered Generative Semantic Communication — TCOM 2025, tcomm.2025.3585683, cpy 11.0 [ | generative/LLM, knowledge]
- Adversarial Attacks Against Shared Knowledge Interpretation in Semantic Communications — TCCN 2025, tccn.2025.3528891, cpy 9.9 [ | knowledge, security/privacy]

### topic:feedback/HARQ（7）
- DeepJSCC- <i>f</i> : Deep Joint Source-Channel Coding of Images With Feedback — JSAIT 2020, jsait.2020.2987203, cpy 75.5 [image | JSCC, feedback/HARQ]
- Deep Source-Channel Coding for Sentence Semantic Transmission With HARQ — TCOM 2022, tcomm.2022.3180997, cpy 44.3 [text | JSCC, feedback/HARQ]
- SCAN: Semantic Communication With Adaptive Channel Feedback — TCCN 2024, tccn.2024.3394867, cpy 32.9 [ | feedback/HARQ, adaptive]
- Transformer-Aided Wireless Image Transmission With Channel Feedback — TWC 2024, twc.2024.3386052, cpy 28.2 [image | feedback/HARQ, transformer/attention]
- Deep Joint Source-Channel Coding for CSI Feedback: An End-to-End Approach — JSAC 2023, jsac.2022.3221963, cpy 22.6 [ | JSCC, feedback/HARQ]
- Adaptive Modulation and Retransmission Scheme for Semantic Communication Systems — TCCN 2024, tccn.2023.3315386, cpy 13.5 [ | digital/modulation, feedback/HARQ, adaptive]
- Semantic Base Enabled Image Transmission With Fine-Grained HARQ — TWC 2025, twc.2025.3532501, cpy 9.9 [image | feedback/HARQ]

### topic:MIMO（7）
- Deep Joint Source-Channel Coding for Adaptive Image Transmission Over MIMO Channels — TWC 2024, twc.2024.3422794, cpy 58.3 [image | JSCC, MIMO, adaptive]
- End-to-End Learning for Task-Oriented Semantic Communications Over MIMO Channels: An Information-Theoretic Framework — JSAC 2025, jsac.2025.3531575, cpy 18.6 [ | task/goal-oriented, theory/limits, MIMO]
- Deep Joint Semantic Coding and Beamforming for Near-Space Airship-Borne Massive MIMO Network — JSAC 2025, jsac.2024.3460084, cpy 18.2 [ | MIMO]
- Robust Image Semantic Coding With Learnable CSI Fusion Masking Over MIMO Fading Channels — TWC 2024, twc.2024.3409735, cpy 17.4 [image | MIMO, security/privacy]
- Semantic MIMO Systems for Speech-to-Text Transmission — TWC 2024, twc.2024.3472612, cpy 16.8 [text, speech/audio | MIMO]
- Task-Oriented Delay-Aware Multi-Tier Computing in Cell-Free Massive MIMO Systems — JSAC 2023, jsac.2023.3280965, cpy 9.5 [ | task/goal-oriented, MIMO]
- Excess Distortion Exponent Analysis for Semantic-Aware MIMO Communication Systems — TWC 2023, twc.2023.3238463, cpy 4.9 [ | MIMO]

### topic:transformer/attention（6）
- SwinJSCC: Taming Swin Transformer for Deep Joint Source-Channel Coding — TCCN 2025, tccn.2024.3424842, cpy 142.7 [ | JSCC, transformer/attention]
- Performance Optimization for Semantic Communications: An Attention-Based Reinforcement Learning Approach — JSAC 2022, jsac.2022.3191112, cpy 55.2 [ | resource allocation, reinforcement learning, transformer/attention]
- A Robust Image Semantic Communication System With Multi-Scale Vision Transformer — JSAC 2025, jsac.2025.3531413, cpy 41.8 [image | security/privacy, transformer/attention]
- Transformer-Aided Wireless Image Transmission With Channel Feedback — TWC 2024, twc.2024.3386052, cpy 28.2 [image | feedback/HARQ, transformer/attention]
- Semantic Information Extraction and Multi-Agent Communication Optimization Based on Generative Pre-Trained Transformer — TCCN 2025, tccn.2024.3482354, cpy 15.9 [ | generative/LLM, resource allocation, transformer/attention]
- Speech Semantic Communication Based on Swin Transformer — TCCN 2024, tccn.2023.3345858, cpy 11.1 [speech/audio | transformer/attention]

### topic:RIS（6）
- Multi-Functional RIS-Assisted Semantic Anti-Jamming Communication and Computing in Integrated Aerial-Ground Networks — JSAC 2024, jsac.2024.3459028, cpy 90.1 [ | RIS, UAV/vehicular/satellite]
- IRS-Enhanced Secure Semantic Communication Networks: Cross-Layer and Context-Awared Resource Allocation — TWC 2025, twc.2024.3495720, cpy 22.7 [ | RIS, resource allocation, security/privacy]
- Semantic Communications for Wireless Sensing: RIS-Aided Encoding and Self-Supervised Decoding — JSAC 2023, jsac.2023.3288231, cpy 18.6 [ | RIS, sensing/ISAC]
- A Physical Layer Security Framework for IRS-Assisted Integrated Sensing and Semantic Communication Systems — TCCN 2025, tccn.2025.3589577, cpy 10.9 [ | RIS, sensing/ISAC, security/privacy]
- RIS-Enhanced Semantic Communications Adaptive to User Requirements — TCOM 2024, tcomm.2024.3369697, cpy 10.2 [ | RIS, adaptive]
- STAR-RIS Assisted Information Transmission Based on Fairness in Semantic Communication Systems — TWC 2024, twc.2024.3449414, cpy 5.7 [ | RIS]

### topic:relay/cooperative（4）
- Task-Oriented Communication for Multidevice Cooperative Edge Inference — TWC 2023, twc.2022.3191118, cpy 57.7 [feature/inference | task/goal-oriented, multi-user/MA, relay/cooperative]
- Optimization of Image Transmission in Cooperative Semantic Communication Networks — TWC 2024, twc.2023.3282906, cpy 39.6 [image | relay/cooperative, resource allocation]
- Process-and-Forward: Deep Joint Source-Channel Coding Over Cooperative Relay Networks — JSAC 2025, jsac.2025.3531579, cpy 18.6 [ | JSCC, relay/cooperative]
- Task-Driven Semantic-Aware Green Cooperative Transmission Strategy for Vehicular Networks — TCOM 2023, tcomm.2023.3300869, cpy 6.3 [ | relay/cooperative, UAV/vehicular/satellite]

### topic:OFDM（2）
- OFDM-Guided Deep Joint Source Channel Coding for Wireless Multipath Fading Channels — TCCN 2022, tccn.2022.3151935, cpy 46.1 [ | JSCC, OFDM]
- OFDM-Based Digital Semantic Communication With Importance Awareness — TCOM 2024, tcomm.2024.3397862, cpy 36.3 [ | digital/modulation, OFDM]

### modality:(none in title)（150）
- Deep Learning Enabled Semantic Communication Systems — TSP 2021, tsp.2021.3071210, cpy 308.7
- Beyond Transmitting Bits: Context, Semantics, and Task-Oriented Communications — JSAC 2023, jsac.2022.3223408, cpy 216.1 [ | task/goal-oriented]
- SwinJSCC: Taming Swin Transformer for Deep Joint Source-Channel Coding — TCCN 2025, tccn.2024.3424842, cpy 142.7 [ | JSCC, transformer/attention]
- Task-Oriented Multi-User Semantic Communications — JSAC 2022, jsac.2022.3191326, cpy 113.4 [ | task/goal-oriented, multi-user/MA]
- Robust Semantic Communications With Masked VQ-VAE Enabled Codebook — TWC 2023, twc.2023.3265201, cpy 104.5 [ | digital/modulation, security/privacy]
- Task-Oriented Sensing, Computation, and Communication Integration for Multi-Device Edge AI — TWC 2024, twc.2023.3303232, cpy 94.5 [ | task/goal-oriented, multi-user/MA, sensing/ISAC]
- Generative AI-Driven Semantic Communication Networks: Architecture, Technologies, and Applications — TCCN 2025, tccn.2024.3435524, cpy 92.5 [ | generative/LLM]
- Nonlinear Transform Source-Channel Coding for Semantic Communications — JSAC 2022, jsac.2022.3180802, cpy 90.1 [ | JSCC]
- Multi-Functional RIS-Assisted Semantic Anti-Jamming Communication and Computing in Integrated Aerial-Ground Networks — JSAC 2024, jsac.2024.3459028, cpy 90.1 [ | RIS, UAV/vehicular/satellite]
- A Lite Distributed Semantic Communication System for Internet of Things — JSAC 2021, jsac.2020.3036968, cpy 86.3
- CDDM: Channel Denoising Diffusion Models for Wireless Semantic Communications — TWC 2024, twc.2024.3379244, cpy 84.1 [ | generative/LLM]
- Joint Coding-Modulation for Digital Semantic Communications via Variational Autoencoder — TCOM 2024, tcomm.2024.3386577, cpy 69.8 [ | digital/modulation]
- Deep Learning-Enabled Semantic Communication Systems With Task-Unaware Transmitter and Dynamic Data — JSAC 2023, jsac.2022.3221991, cpy 68.9
- Compression Ratio Allocation for Probabilistic Semantic Communication With RSMA — TCOM 2025, tcomm.2025.3548689, cpy 62.3 [ | multi-user/MA, resource allocation]
- Adaptable Semantic Compression and Resource Allocation for Task-Oriented Communications — TCCN 2024, tccn.2023.3346481, cpy 60.6 [ | task/goal-oriented, resource allocation]
- DRL-Driven Dynamic Resource Allocation for Task-Oriented Semantic Communication — TCOM 2023, tcomm.2023.3274145, cpy 58.3 [ | task/goal-oriented, resource allocation, reinforcement learning]
- Adaptive Resource Allocation for Semantic Communication Networks — TCOM 2024, tcomm.2024.3405355, cpy 57.1 [ | resource allocation, adaptive]
- Energy-Efficient Probabilistic Semantic Communication Over Space-Air-Ground Integrated Networks — TWC 2025, twc.2025.3569102, cpy 55.5 [ | resource allocation]
- Performance Optimization for Semantic Communications: An Attention-Based Reinforcement Learning Approach — JSAC 2022, jsac.2022.3191112, cpy 55.2 [ | resource allocation, reinforcement learning, transformer/attention]
- Joint Source-Channel Coding for Channel-Adaptive Digital Semantic Communications — TCCN 2025, tccn.2024.3422496, cpy 49.6 [ | JSCC, digital/modulation, adaptive]
- D²-JSCC: Digital Deep Joint Source-Channel Coding for Semantic Communications — JSAC 2025, jsac.2025.3531546, cpy 46.4 [ | JSCC, digital/modulation]
- OFDM-Guided Deep Joint Source Channel Coding for Wireless Multipath Fading Channels — TCCN 2022, tccn.2022.3151935, cpy 46.1 [ | JSCC, OFDM]
- Diffusion-Driven Semantic Communication for Generative Models With Bandwidth Constraints — TWC 2025, twc.2025.3553851, cpy 42.6 [ | generative/LLM]
- Heterogeneous Semantic and Bit Communications: A Semi-NOMA Scheme — JSAC 2023, jsac.2022.3222000, cpy 42.6 [ | multi-user/MA]
- Robust Information Bottleneck for Task-Oriented Communication With Digital Modulation — JSAC 2023, jsac.2023.3288252, cpy 40.9 [ | digital/modulation, task/goal-oriented, theory/limits, security/privacy]
- AI-Generated Incentive Mechanism and Full-Duplex Semantic Communications for Information Sharing — JSAC 2023, jsac.2023.3287547, cpy 39.8
- DeepJSCC-Q: Constellation Constrained Deep Joint Source-Channel Coding — JSAIT 2022, jsait.2022.3231042, cpy 39.8 [ | JSCC, digital/modulation]
- Semantic Communication System Based on Semantic Slice Models Propagation — JSAC 2023, jsac.2022.3221948, cpy 38.6
- Generative Semantic Communications With Foundation Models: Perception-Error Analysis and Semantic-Aware Power Allocation — JSAC 2025, jsac.2025.3559120, cpy 38.1 [ | generative/LLM, resource allocation]
- OFDM-Based Digital Semantic Communication With Importance Awareness — TCOM 2024, tcomm.2024.3397862, cpy 36.3 [ | digital/modulation, OFDM]
- The Age of Incorrect Information: An Enabler of Semantics-Empowered Communication — TWC 2023, twc.2022.3213227, cpy 34.2
- Privacy-Preserving Task-Oriented Semantic Communications Against Model Inversion Attacks — TWC 2024, twc.2024.3369170, cpy 33.6 [ | task/goal-oriented, security/privacy]
- SCAN: Semantic Communication With Adaptive Channel Feedback — TCCN 2024, tccn.2024.3394867, cpy 32.9 [ | feedback/HARQ, adaptive]
- Task-Oriented Over-the-Air Computation for Multi-Device Edge AI — TWC 2024, twc.2023.3294703, cpy 32.4 [ | task/goal-oriented, multi-user/MA]
- Deep Reinforcement Learning-Based Resource Allocation for Hybrid Bit and Generative Semantic Communications in Space-Air-Ground Integrated Networks — JSAC 2025, jsac.2025.3623157, cpy 32.0 [ | generative/LLM, resource allocation, reinforcement learning]
- Deep Learning-Empowered Semantic Communication Systems With a Shared Knowledge Base — TWC 2024, twc.2023.3330744, cpy 31.2 [ | knowledge]
- R-ACP: Real-Time Adaptive Collaborative Perception Leveraging Robust Task-Oriented Communications — JSAC 2025, jsac.2025.3623179, cpy 31.0 [ | task/goal-oriented, security/privacy, adaptive]
- Semantic Communication in Satellite-Borne Edge Cloud Network for Computation Offloading — JSAC 2024, jsac.2024.3365879, cpy 30.9 [ | UAV/vehicular/satellite]
- Task-Oriented Explainable Semantic Communications — TWC 2023, twc.2023.3269444, cpy 29.9 [ | task/goal-oriented]
- Non-Orthogonal Multiple Access Enhanced Multi-User Semantic Communication — TCCN 2023, tccn.2023.3306852, cpy 29.9 [ | multi-user/MA]
- Physical-Layer Adversarial Robustness for Deep Learning-Based Semantic Communications — JSAC 2023, jsac.2023.3288249, cpy 29.0 [ | security/privacy]
- Semantic Satellite Communications Based on Generative Foundation Model — JSAC 2025, jsac.2025.3559113, cpy 27.8 [ | generative/LLM, UAV/vehicular/satellite]
- Exploiting Semantic Communication for Non-Orthogonal Multiple Access — JSAC 2023, jsac.2023.3288242, cpy 27.7 [ | multi-user/MA]
- Latent Diffusion Model-Enabled Low-Latency Semantic Communication in the Presence of Semantic Ambiguities and Wireless Channel Noises — TWC 2025, twc.2025.3535714, cpy 27.4 [ | generative/LLM]
- Semantic Successive Refinement: A Generative AI-Aided Semantic Communication Framework — TCCN 2025, tccn.2025.3526839, cpy 27.2 [ | generative/LLM]
- Contrastive Learning-Based Semantic Communications — TCOM 2024, tcomm.2024.3400912, cpy 26.9
- QoE-Based Semantic-Aware Resource Allocation for Multi-Task Networks — TWC 2024, twc.2024.3386807, cpy 26.8 [ | resource allocation]
- Semantic Communication With Memory — JSAC 2023, jsac.2023.3288236, cpy 26.1
- Cognitive Semantic Communication Systems Driven by Knowledge Graph: Principle, Implementation, and Performance Evaluation — TCOM 2024, tcomm.2023.3318605, cpy 25.7 [ | knowledge]
- From Analog to Digital: Multi-Order Digital Joint Coding-Modulation for Semantic Communication — TCOM 2025, tcomm.2024.3511949, cpy 25.3 [ | digital/modulation]
- Semantic-Aware Remote Estimation of Multiple Markov Sources Under Constraints — TCOM 2025, tcomm.2025.3571950, cpy 24.0
- UAV-Aided Radio Map Construction Exploiting Environment Semantics — TWC 2023, twc.2023.3241845, cpy 23.9 [ | UAV/vehicular/satellite]
- Resource Optimization for Semantic-Aware Networks With Task Offloading — TWC 2024, twc.2024.3390407, cpy 23.9 [ | resource allocation]
- sDAC—Semantic Digital Analog Converter for Semantic Communications — TCOM 2025, tcomm.2025.3566976, cpy 23.0 [ | digital/modulation]
- IRS-Enhanced Secure Semantic Communication Networks: Cross-Layer and Context-Awared Resource Allocation — TWC 2025, twc.2024.3495720, cpy 22.7 [ | RIS, resource allocation, security/privacy]
- Deep Joint Source-Channel Coding for CSI Feedback: An End-to-End Approach — JSAC 2023, jsac.2022.3221963, cpy 22.6 [ | JSCC, feedback/HARQ]
- Environment Semantics Aided Wireless Communications: A Case Study of mmWave Beam Prediction and Blockage Prediction — JSAC 2023, jsac.2023.3280966, cpy 22.4
- UAV-Enabled Semantic Communication in Mobile Edge Computing Under Jamming Attacks: An Intelligent Resource Management Approach — TWC 2024, twc.2024.3454073, cpy 21.8 [ | UAV/vehicular/satellite, resource allocation, security/privacy]
- Neuro-Symbolic Causal Reasoning Meets Signaling Game for Emergent Semantic Communications — TWC 2024, twc.2023.3319981, cpy 21.4
- Computation-Aware Offloading for DNN Inference Tasks in Semantic Communication Assisted MEC Systems — TWC 2025, twc.2024.3523517, cpy 19.9 [ | task/goal-oriented]
- Lyapunov-Guided Deep Reinforcement Learning for Semantic-Aware AoI Minimization in UAV-Assisted Wireless Networks — TWC 2025, twc.2025.3552809, cpy 19.6 [ | UAV/vehicular/satellite, reinforcement learning]
- Semantic-Aware Sensing Information Transmission for Metaverse: A Contest Theoretic Approach — TWC 2023, twc.2022.3232565, cpy 19.5 [ | sensing/ISAC]
- Toward Adaptive Semantic Communications: Efficient Data Transmission via Online Learned Nonlinear Transform Source-Channel Coding — JSAC 2023, jsac.2023.3288246, cpy 19.5 [ | JSCC, adaptive]
- Imitation Learning-Based Implicit Semantic-Aware Communication Networks: Multi-Layer Representation and Collaborative Reasoning — JSAC 2023, jsac.2022.3229419, cpy 18.9
- Age of Incorrect Information Minimization for Semantic-Empowered NOMA System in S-IoT — TWC 2024, twc.2023.3334761, cpy 18.8 [ | multi-user/MA]
- Semantic Communications for Wireless Sensing: RIS-Aided Encoding and Self-Supervised Decoding — JSAC 2023, jsac.2023.3288231, cpy 18.6 [ | RIS, sensing/ISAC]
- End-to-End Learning for Task-Oriented Semantic Communications Over MIMO Channels: An Information-Theoretic Framework — JSAC 2025, jsac.2025.3531575, cpy 18.6 [ | task/goal-oriented, theory/limits, MIMO]
- Process-and-Forward: Deep Joint Source-Channel Coding Over Cooperative Relay Networks — JSAC 2025, jsac.2025.3531579, cpy 18.6 [ | JSCC, relay/cooperative]
- Knowledge-Based Ultra-Low-Latency Semantic Communications for Robotic Edge Intelligence — TCOM 2025, tcomm.2024.3511931, cpy 18.3 [ | knowledge]
- Deep Joint Semantic Coding and Beamforming for Near-Space Airship-Borne Massive MIMO Network — JSAC 2025, jsac.2024.3460084, cpy 18.2 [ | MIMO]
- The Semantic Communication Game — TCCN 2018, tccn.2018.2872596, cpy 18.2
- The Role of Fidelity in Goal-Oriented Semantic Communication: A Rate Distortion Approach — TCOM 2023, tcomm.2023.3274122, cpy 17.8 [ | task/goal-oriented, theory/limits]
- Semantics-Native Communication via Contextual Reasoning — TCCN 2023, tccn.2023.3250206, cpy 17.4
- Neuromorphic Wireless Cognition: Event-Driven Semantic Communications for Remote Inference — TCCN 2023, tccn.2023.3236940, cpy 17.1 [ | task/goal-oriented]
- Semantic Communication Enabled 6G-NTN Framework: A Novel Denoising and Gateway Hop Integration Mechanism — TWC 2025, twc.2025.3578010, cpy 17.0
- UAV Cognitive Semantic Communications Enabled by Knowledge Graph for Robust Object Detection — TCOM 2025, tcomm.2025.3538850, cpy 17.0 [ | task/goal-oriented, knowledge, UAV/vehicular/satellite, security/privacy]
- Joint Semantic Transmission and Resource Allocation for Intelligent Computation Task Offloading in MEC Systems — TWC 2025, twc.2025.3568870, cpy 16.9 [ | resource allocation]
- Goal-Oriented Semantic Communications for Robotic Waypoint Transmission: The Value and Age of Information Approach — TWC 2024, twc.2024.3424493, cpy 16.3 [ | task/goal-oriented]
- Semantic Information Extraction and Multi-Agent Communication Optimization Based on Generative Pre-Trained Transformer — TCCN 2025, tccn.2024.3482354, cpy 15.9 [ | generative/LLM, resource allocation, transformer/attention]
- Multi-Device Task-Oriented Communication via Maximal Coding Rate Reduction — TWC 2024, twc.2024.3461336, cpy 15.2 [ | task/goal-oriented, multi-user/MA]
- Beamforming Design for Semantic-Bit Coexisting Communication System — JSAC 2025, jsac.2025.3531537, cpy 15.2
- Tackling Distribution Shifts in Task-Oriented Communication With Information Bottleneck — JSAC 2025, jsac.2025.3559116, cpy 15.1 [ | task/goal-oriented, theory/limits]
- Semantic-Aware Sampling and Transmission in Real-Time Tracking Systems: A POMDP Approach — TCOM 2025, tcomm.2024.3511935, cpy 15.1
- Resource Allocation for Semantic-Aware Wireless Communication Networks With Imperfect CSI — TWC 2025, twc.2025.3575444, cpy 15.0 [ | resource allocation]
- Age of Information Versions: A Semantic View of Markov Source Monitoring — TCOM 2025, tcomm.2025.3616209, cpy 15.0
- Reasoning Over the Air: A Reasoning- Based Implicit Semantic-Aware Communication Framework — TWC 2024, twc.2023.3312115, cpy 14.8
- Semantic Utility Loss of Information for Energy Efficient Semantic Status Update Communications — TCCN 2025, tccn.2024.3417627, cpy 14.3 [ | resource allocation]
- An Indirect Rate-Distortion Characterization for Semantic Sources: General Model and the Case of Gaussian Observation — TCOM 2022, tcomm.2022.3194978, cpy 14.2 [ | theory/limits]
- Blind Training for Channel-Adaptive Digital Semantic Communications — TCOM 2025, tcomm.2025.3585587, cpy 14.0 [ | digital/modulation, adaptive]
- Adaptive Modulation and Retransmission Scheme for Semantic Communication Systems — TCCN 2024, tccn.2023.3315386, cpy 13.5 [ | digital/modulation, feedback/HARQ, adaptive]
- Wireless Resource Optimization in Hybrid Semantic/Bit Communication Networks — TCOM 2025, tcomm.2024.3485582, cpy 13.3 [ | resource allocation]
- Adaptive Semantic Generation and NOMA-Based Interference-Aware Transmission for 6G Networks — TWC 2025, twc.2024.3520870, cpy 13.2 [ | multi-user/MA, adaptive]
- Knowledge Distillation-Based Semantic Communications for Multiple Users — TWC 2024, twc.2023.3336941, cpy 12.8 [ | knowledge]
- Semantic Prior Aided Channel-Adaptive Equalizing and De-Noising Semantic Communication System With Latent Diffusion Model — TWC 2025, twc.2025.3543167, cpy 12.7 [ | generative/LLM, adaptive]
- Universal Joint Source-Channel Coding for Modulation-Agnostic Semantic Communication — JSAC 2025, jsac.2025.3559138, cpy 12.7 [ | JSCC, digital/modulation]
- Goal-Oriented Semantic Communications for Avatar-Centric Augmented Reality — TCOM 2024, tcomm.2024.3420708, cpy 12.5 [ | task/goal-oriented]
- Joint URLLC Traffic Scheduling and Resource Allocation for Semantic Communication Systems — TWC 2024, twc.2023.3339239, cpy 12.4 [ | resource allocation]
- Causal Semantic Communication for Digital Twins: A Generalizable Imitation Learning Approach — JSAIT 2023, jsait.2023.3336538, cpy 12.3 [ | digital/modulation]
- Goal-Oriented Scheduling in Sensor Networks With Application Timing Awareness — TCOM 2023, tcomm.2023.3282256, cpy 12.0 [ | task/goal-oriented, resource allocation]
- R-UAV-Net: Enhanced YOLOv4 With Graph-Semantic Compression for Transformative UAV Sensing in Paddy Agronomy — TCCN 2025, tccn.2024.3452053, cpy 11.9 [ | UAV/vehicular/satellite, sensing/ISAC]
- Toward Semantic Communication Protocols: A Probabilistic Logic Perspective — JSAC 2023, jsac.2023.3288268, cpy 11.7
- Resource Allocation and Common Message Selection for Task-Oriented Semantic Information Transmission With RSMA — TWC 2024, twc.2023.3327127, cpy 11.5 [ | task/goal-oriented, multi-user/MA, resource allocation]
- Task-Oriented Scene Graph-Based Semantic Communications With Adaptive Channel Coding — TWC 2024, twc.2024.3450697, cpy 11.4 [ | task/goal-oriented, adaptive]
- Deep Learning-Based Superposition Coded Modulation for Hierarchical Semantic Communications Over Broadcast Channels — TCOM 2025, tcomm.2024.3447870, cpy 11.3 [ | digital/modulation, multi-user/MA]
- Multi-Scale Semantic Communication for Object Detection: Single and Cross-Domain Scenarios — TWC 2025, twc.2025.3552255, cpy 11.1 [ | task/goal-oriented]
- Joint Source-Channel Coding Over Additive Noise Analog Channels Using Mixture of Variational Autoencoders — JSAC 2021, jsac.2021.3078489, cpy 11.0 [ | JSCC]
- Semantic Knowledge Base Empowered Generative Semantic Communication — TCOM 2025, tcomm.2025.3585683, cpy 11.0 [ | generative/LLM, knowledge]
- A Physical Layer Security Framework for IRS-Assisted Integrated Sensing and Semantic Communication Systems — TCCN 2025, tccn.2025.3589577, cpy 10.9 [ | RIS, sensing/ISAC, security/privacy]
- Hybrid Semantic-Shannon Communications — TWC 2024, twc.2024.3376998, cpy 10.5
- Goal-Oriented Wireless Communication Resource Allocation for Cyber-Physical Systems — TWC 2024, twc.2024.3432918, cpy 10.4 [ | task/goal-oriented, resource allocation]
- Capacity Optimizing Resource Allocation in Joint Source-Channel Coding Systems With QoS Constraints — TCOM 2025, tcomm.2024.3496714, cpy 10.4 [ | JSCC, theory/limits, resource allocation]
- RIS-Enhanced Semantic Communications Adaptive to User Requirements — TCOM 2024, tcomm.2024.3369697, cpy 10.2 [ | RIS, adaptive]
- Task-Oriented Low-Label Semantic Communication With Self-Supervised Learning — TWC 2025, twc.2025.3574468, cpy 10.0 [ | task/goal-oriented]
- Adversarial Attacks Against Shared Knowledge Interpretation in Semantic Communications — TCCN 2025, tccn.2025.3528891, cpy 9.9 [ | knowledge, security/privacy]
- Fluid Antenna-Enabled Near-Field Integrated Sensing, Computing, and Semantic Communication for Emerging Applications — TCCN 2025, tccn.2025.3592294, cpy 9.9 [ | sensing/ISAC]
- Context-Based Semantic Communication via Dynamic Programming — TCCN 2022, tccn.2022.3173056, cpy 9.8
- Task-Oriented Communication for Graph Data: A Graph Information Bottleneck Approach — TCCN 2025, tccn.2024.3465651, cpy 9.7 [ | task/goal-oriented, theory/limits]
- Task-Oriented Delay-Aware Multi-Tier Computing in Cell-Free Massive MIMO Systems — JSAC 2023, jsac.2023.3280965, cpy 9.5 [ | task/goal-oriented, MIMO]
- AoI-Aware Interference Mitigation for Task-Oriented Multicasting in Multi-Cell NOMA Networks — TWC 2024, twc.2024.3381480, cpy 9.1 [ | task/goal-oriented, multi-user/MA]
- Goal-Oriented Quantization: Analysis, Design, and Application to Resource Allocation — JSAC 2023, jsac.2022.3221976, cpy 8.5 [ | digital/modulation, task/goal-oriented, resource allocation]
- Task-Oriented Cross-System Design for Timely and Accurate Modeling in the Metaverse — JSAC 2024, jsac.2023.3345398, cpy 8.1 [ | task/goal-oriented]
- Goal-Oriented Tensor: Beyond Age of Information Toward Semantics-Empowered Goal-Oriented Communications — TCOM 2024, tcomm.2024.3416864, cpy 8.1 [ | task/goal-oriented]
- Machine Learning Enabled Heterogeneous Semantic and Bit Communication — TWC 2024, twc.2024.3397635, cpy 8.0
- Hybrid Digital-Analog Semantic Communications — JSAC 2025, jsac.2025.3559149, cpy 7.9 [ | digital/modulation]
- Interference Suppressed NOMA for Semantic-Aware Communication Networks — TWC 2024, twc.2024.3371775, cpy 7.8 [ | multi-user/MA]
- Edge Learning for Large-Scale Internet of Things With Task-Oriented Efficient Communication — TWC 2023, twc.2023.3271665, cpy 7.7 [ | task/goal-oriented]
- Semantic Information Marketing in the Metaverse: A Learning-Based Contract Theory Framework — JSAC 2024, jsac.2023.3345402, cpy 7.7
- Semantic Filtering and Source Coding in Distributed Wireless Monitoring Systems — TCOM 2024, tcomm.2024.3362951, cpy 7.7
- Goal-Oriented Communication, Estimation, and Control Over Bidirectional Wireless Links — TCOM 2025, tcomm.2024.3485572, cpy 7.7 [ | task/goal-oriented]
- Joint Component Design for the JSCC System Based on DP-LDPC Codes — TCOM 2020, tcomm.2020.3001647, cpy 7.4 [ | JSCC]
- GAI-Enhanced Robust Semantic Communication With Asymmetric Architecture — TCCN 2025, tccn.2024.3520132, cpy 7.3 [ | security/privacy]
- Importance of Semantic Information Based on Semantic Value — TCOM 2024, tcomm.2024.3385915, cpy 7.2
- Concatenated Spatially Coupled LDPC Codes With Sliding Window Decoding for Joint Source-Channel Coding — TCOM 2022, tcomm.2021.3126750, cpy 6.8 [ | JSCC]
- Task-Oriented Communication Design at Scale — TCOM 2025, tcomm.2024.3416898, cpy 6.8 [ | task/goal-oriented]
- Low-Delay Analog Joint Source-Channel Coding With Deep Learning — TCOM 2023, tcomm.2022.3222874, cpy 6.7 [ | JSCC]
- Unified Timing Analysis for Closed-Loop Goal-Oriented Wireless Communication — TWC 2025, twc.2024.3525087, cpy 6.6 [ | task/goal-oriented]
- Rate-Distortion-Perception Controllable Joint Source-Channel Coding for High-Fidelity Generative Semantic Communications — TCCN 2025, tccn.2024.3511960, cpy 6.6 [ | JSCC, generative/LLM, theory/limits]
- Compression Before Fusion: Broadcast Semantic Communication System for Heterogeneous Tasks — TWC 2024, twc.2024.3483314, cpy 6.5 [ | multi-user/MA]
- A New Joint Source-Channel Coding for Short-Packet Communications — TCOM 2024, tcomm.2023.3320699, cpy 6.5 [ | JSCC]
- Dynamic Semantic Compression for CNN Inference in Multi-Access Edge Computing: A Graph Reinforcement Learning-Based Autoencoder — TWC 2025, twc.2024.3518399, cpy 6.3 [ | task/goal-oriented, reinforcement learning]
- Task-Driven Semantic-Aware Green Cooperative Transmission Strategy for Vehicular Networks — TCOM 2023, tcomm.2023.3300869, cpy 6.3 [ | relay/cooperative, UAV/vehicular/satellite]
- Timeliness of Information for Computation-Intensive Status Updates in Task-Oriented Communications — JSAC 2023, jsac.2022.3229431, cpy 5.8 [ | task/goal-oriented]
- STAR-RIS Assisted Information Transmission Based on Fairness in Semantic Communication Systems — TWC 2024, twc.2024.3449414, cpy 5.7 [ | RIS]
- Post-Deployment Fine-Tunable Semantic Communication — TWC 2025, twc.2024.3433479, cpy 5.7
- Indoor Semantic Location Privacy Protection With Safe Reinforcement Learning — TCCN 2023, tccn.2023.3291364, cpy 5.7 [ | security/privacy, reinforcement learning]
- SC-PNC: Semantic Communication-Empowered Physical-Layer Network Coding — TCCN 2024, tccn.2024.3375506, cpy 5.5
- Excess Distortion Exponent Analysis for Semantic-Aware MIMO Communication Systems — TWC 2023, twc.2023.3238463, cpy 4.9 [ | MIMO]
- Blind Goal-Oriented Massive Access for Future Wireless Networks — TSP 2023, tsp.2023.3254140, cpy 4.8 [ | task/goal-oriented]
- Joint Code Rate Compatible Design of DP-LDPC Code Pairs for Joint Source Channel Coding Over Implant-to-External Channel — TWC 2022, twc.2022.3141729, cpy 4.5 [ | JSCC]
- Reliable Extraction of Semantic Information and Rate of Innovation Estimation for Graph Signals — JSAC 2023, jsac.2022.3221950, cpy 3.2

### modality:image（35）
- Deep Joint Source-Channel Coding for Wireless Image Transmission — TCCN 2019, tccn.2019.2919300, cpy 213.2 [image | JSCC]
- Toward Semantic Communications: Deep Learning-Based Image Semantic Coding — JSAC 2023, jsac.2022.3221999, cpy 91.8 [image | ]
- Predictive and Adaptive Deep Coding for Wireless Image Transmission in Semantic Communication — TWC 2023, twc.2023.3234408, cpy 86.3 [image | adaptive]
- DeepJSCC- <i>f</i> : Deep Joint Source-Channel Coding of Images With Feedback — JSAIT 2020, jsait.2020.2987203, cpy 75.5 [image | JSCC, feedback/HARQ]
- Semantic Communications for Image Recovery and Classification via Deep Joint Source and Channel Coding — TWC 2024, twc.2023.3349330, cpy 70.8 [image | task/goal-oriented]
- Generative Joint Source-Channel Coding for Semantic Image Transmission — JSAC 2023, jsac.2023.3288243, cpy 65.8 [image | JSCC, generative/LLM]
- Deep Joint Source-Channel Coding for Adaptive Image Transmission Over MIMO Channels — TWC 2024, twc.2024.3422794, cpy 58.3 [image | JSCC, MIMO, adaptive]
- Personalized Saliency in Task-Oriented Semantic Communications: Image Transmission and Performance Analysis — JSAC 2023, jsac.2022.3221990, cpy 50.8 [image | task/goal-oriented]
- A Robust Image Semantic Communication System With Multi-Scale Vision Transformer — JSAC 2025, jsac.2025.3531413, cpy 41.8 [image | security/privacy, transformer/attention]
- Bandwidth-Agile Image Transmission With Deep Joint Source-Channel Coding — TWC 2021, twc.2021.3090048, cpy 40.3 [image | JSCC, adaptive]
- Optimization of Image Transmission in Cooperative Semantic Communication Networks — TWC 2024, twc.2023.3282906, cpy 39.6 [image | relay/cooperative, resource allocation]
- LaMoSC: Large Language Model-Driven Semantic Communication System for Visual Transmission — TCCN 2024, tccn.2024.3401712, cpy 38.0 [image | generative/LLM]
- Task-Oriented Image Transmission for Scene Classification in Unmanned Aerial Systems — TCOM 2022, tcomm.2022.3182325, cpy 34.7 [image | task/goal-oriented, UAV/vehicular/satellite]
- DeepMA: End-to-End Deep Multiple Access for Wireless Image Transmission in Semantic Communication — TCCN 2024, tccn.2023.3326302, cpy 28.3 [image | multi-user/MA]
- Transformer-Aided Wireless Image Transmission With Channel Feedback — TWC 2024, twc.2024.3386052, cpy 28.2 [image | feedback/HARQ, transformer/attention]
- Visual Language Model-Based Cross-Modal Semantic Communication Systems — TWC 2025, twc.2025.3539526, cpy 25.3 [image, multimodal | ]
- Free Space Optical Semantic Communication for Satellite Remote Sensing Image Transmission — TCOM 2025, tcomm.2025.3562356, cpy 19.8 [image | UAV/vehicular/satellite, sensing/ISAC]
- SCSC: A Novel Standards-Compatible Semantic Communication Framework for Image Transmission — TCOM 2025, tcomm.2025.3529221, cpy 17.9 [image | ]
- Robust Image Semantic Coding With Learnable CSI Fusion Masking Over MIMO Fading Channels — TWC 2024, twc.2024.3409735, cpy 17.4 [image | MIMO, security/privacy]
- Semantic Image Encoding and Communication for Earth Observation With LEO Satellites — TCCN 2025, tccn.2024.3451724, cpy 17.2 [image | UAV/vehicular/satellite]
- Progressive Learned Image Transmission for Semantic Communication Using Hierarchical VAE — TCCN 2025, tccn.2025.3546935, cpy 17.0 [image | ]
- Improving Learning-Based Semantic Coding Efficiency for Image Transmission via Shared Semantic-Aware Codebook — TCOM 2025, tcomm.2024.3450877, cpy 16.1 [image | digital/modulation]
- Image Generation With Supervised Selection Based on Multimodal Features for Semantic Communications — TCOM 2025, tcomm.2025.3615798, cpy 14.0 [image, multimodal, feature/inference | ]
- Deep Joint Source-Channel Coding for Image Transmission With Visual Protection — TCCN 2023, tccn.2023.3306851, cpy 13.7 [image | JSCC]
- xURLLC-Aware Service Provisioning in Vehicular Networks: A Semantic Communication Perspective — TWC 2024, twc.2023.3319442, cpy 12.8 [image | UAV/vehicular/satellite]
- Adaptive Information Bottleneck Guided Joint Source and Channel Coding for Image Transmission — JSAC 2023, jsac.2023.3288238, cpy 12.6 [image | theory/limits, adaptive]
- Transmit What You Need: Task-Adaptive Semantic Communications for Visual Information — JSAC 2025, jsac.2025.3623159, cpy 12.0 [image | adaptive]
- Goal-Oriented Semantic Communication for Wireless Visual Question Answering — JSAC 2025, jsac.2025.3623184, cpy 11.0 [image | task/goal-oriented]
- Semantic Base Enabled Image Transmission With Fine-Grained HARQ — TWC 2025, twc.2025.3532501, cpy 9.9 [image | feedback/HARQ]
- Task-Oriented Semantic Communication for Stereo-Vision 3D Object Detection — TCOM 2025, tcomm.2025.3545687, cpy 9.2 [image, point-cloud/3D | task/goal-oriented]
- Semantic Feature Division Multiple Access for Multi-User Digital Interference Networks — TWC 2024, twc.2024.3427675, cpy 9.0 [image, feature/inference | digital/modulation, multi-user/MA]
- How to Evaluate Semantic Communications for Images With ViTScore Metric? — TCCN 2024, tccn.2024.3392803, cpy 9.0 [image | ]
- Resource Allocation for the Training of Image Semantic Communication Networks — TWC 2025, twc.2025.3527014, cpy 7.3 [image | resource allocation]
- Disentangled Information Bottleneck Guided Privacy-Protective Joint Source and Channel Coding for Image Transmission — TCOM 2024, tcomm.2024.3406381, cpy 6.8 [image | theory/limits, security/privacy]
- On Learning-Assisted Content-Based Secure Image Transmission for Delay-Aware Systems With Randomly-Distributed Eavesdroppers — TCOM 2022, tcomm.2021.3128423, cpy 4.9 [image | security/privacy]

### modality:feature/inference（18）
- Learning Task-Oriented Communication for Edge Inference: An Information Bottleneck Approach — JSAC 2022, jsac.2021.3126087, cpy 72.9 [feature/inference | task/goal-oriented, theory/limits]
- Task-Oriented Communication for Multidevice Cooperative Edge Inference — TWC 2023, twc.2022.3191118, cpy 57.7 [feature/inference | task/goal-oriented, multi-user/MA, relay/cooperative]
- Energy Efficient Semantic Communication Over Wireless Networks With Rate Splitting — JSAC 2023, jsac.2023.3240713, cpy 52.8 [feature/inference | multi-user/MA, resource allocation]
- Beyond the Cloud: Edge Inference for Generative Large Language Models in Wireless Networks — TWC 2025, twc.2024.3497923, cpy 46.6 [feature/inference | generative/LLM, task/goal-oriented]
- Energy-Efficient Edge Inference in Integrated Sensing, Communication, and Computation Networks — JSAC 2025, jsac.2025.3574612, cpy 32.7 [feature/inference | task/goal-oriented, sensing/ISAC, resource allocation]
- Digital-SC: Digital Semantic Communication With Adaptive Network Split and Learned Non-Linear Quantization — TCCN 2025, tccn.2024.3510586, cpy 27.2 [feature/inference | digital/modulation, adaptive]
- Feature Importance-Aware Task-Oriented Semantic Transmission and Optimization — TCCN 2024, tccn.2024.3375496, cpy 26.2 [feature/inference | task/goal-oriented, resource allocation]
- Feature Allocation for Semantic Communication With Space-Time Importance Awareness — TWC 2025, twc.2025.3569320, cpy 24.8 [feature/inference | resource allocation]
- Resource Allocation for Multiuser Edge Inference With Batching and Early Exiting — JSAC 2023, jsac.2023.3242724, cpy 23.9 [feature/inference | task/goal-oriented, multi-user/MA, resource allocation]
- Task-Oriented Semantic Communication over Rate Splitting Enabled Wireless Control Systems for URLLC Services — TCOM 2024, tcomm.2023.3325901, cpy 18.7 [feature/inference | task/goal-oriented, multi-user/MA]
- Rate Splitting Multiple Access-Enabled Adaptive Panoramic Video Semantic Transmission — TWC 2025, twc.2025.3570465, cpy 15.0 [video, feature/inference | multi-user/MA, adaptive]
- Image Generation With Supervised Selection Based on Multimodal Features for Semantic Communications — TCOM 2025, tcomm.2025.3615798, cpy 14.0 [image, multimodal, feature/inference | ]
- Generative AI Empowered Semantic Feature Multiple Access (SFMA) Over Wireless Networks — TCCN 2025, tccn.2025.3529692, cpy 13.9 [feature/inference | generative/LLM, multi-user/MA]
- Semantic Knowledge Base-Enabled Zero-Shot Multi-Level Feature Transmission Optimization — TWC 2024, twc.2023.3323380, cpy 13.6 [feature/inference | knowledge, resource allocation]
- Over-the-Air Edge Inference for Low-Altitude Airspace: Generative AI-Aided Multi-Task Batching and Beamforming Design — TCOM 2025, tcomm.2025.3563657, cpy 11.9 [feature/inference | generative/LLM, task/goal-oriented]
- Features Disentangled Semantic Broadcast Communication Networks — TWC 2024, twc.2023.3334225, cpy 11.5 [feature/inference | multi-user/MA]
- Semantic Feature Division Multiple Access for Multi-User Digital Interference Networks — TWC 2024, twc.2024.3427675, cpy 9.0 [image, feature/inference | digital/modulation, multi-user/MA]
- Semantic Feature Scheduling and Rate Control in Multi-Modal Distributed Network — TWC 2024, twc.2024.3480352, cpy 6.0 [multimodal, feature/inference | resource allocation]

### modality:video（17）
- Wireless Deep Video Semantic Transmission — JSAC 2023, jsac.2022.3221977, cpy 74.0 [video | ]
- Wireless Semantic Communications for Video Conferencing — JSAC 2023, jsac.2022.3221968, cpy 72.1 [video | ]
- DeepWiVe: Deep-Learning-Aided Wireless Video Transmission — JSAC 2022, jsac.2022.3191354, cpy 52.1 [video | ]
- VideoQA-SC: Adaptive Semantic Communication for Video Question Answering — JSAC 2025, jsac.2025.3559160, cpy 23.0 [video | adaptive]
- Task-Oriented Communication for Edge Video Analytics — TWC 2024, twc.2023.3314888, cpy 21.0 [video | task/goal-oriented]
- UAV Anti-Jamming Video Transmissions With QoE Guarantee: A Reinforcement Learning-Based Approach — TCOM 2021, tcomm.2021.3087787, cpy 15.7 [video | UAV/vehicular/satellite, reinforcement learning]
- ISCom: Interest-Aware Semantic Communication Scheme for Point Cloud Video Streaming on Metaverse XR Devices — JSAC 2024, jsac.2023.3345430, cpy 15.5 [video, point-cloud/3D | ]
- Rate Splitting Multiple Access-Enabled Adaptive Panoramic Video Semantic Transmission — TWC 2025, twc.2025.3570465, cpy 15.0 [video, feature/inference | multi-user/MA, adaptive]
- Object-Attribute-Relation Representation-Based Video Semantic Communication — JSAC 2025, jsac.2025.3559115, cpy 12.7 [video | ]
- Dynamic Resource Allocation for Real-Time Cloud XR Video Transmission: A Reinforcement Learning Approach — TCCN 2024, tccn.2024.3352982, cpy 9.8 [video | resource allocation, reinforcement learning]
- Learning QoE of Mobile Video Transmission With Deep Neural Network: A Data-Driven Approach — JSAC 2019, jsac.2019.2904359, cpy 7.9 [video | ]
- Scalable Video Transmission in Cache-Aided Device-to-Device Networks — TWC 2020, twc.2020.2981790, cpy 6.1 [video | ]
- Max-Min Resource Allocation for Video Transmission in NOMA-Based Cognitive Wireless Networks — TCOM 2018, tcomm.2018.2854584, cpy 4.9 [video | multi-user/MA, resource allocation]
- Adaptive Bitrate Video Transmission Over Cognitive Radio Networks Using Cross Layer Routing Approach — TCCN 2020, tccn.2020.2990673, cpy 4.6 [video | adaptive]
- Distortion-Aware Cross-Layer Power Allocation for Video Transmission Over Multi-User NOMA Systems — TWC 2021, twc.2020.3030785, cpy 3.5 [video | multi-user/MA, resource allocation]
- QoE-Driven Multi-User Video Transmission Over SM-NOMA Integrated Systems — JSAC 2019, jsac.2019.2929382, cpy 2.7 [video | multi-user/MA]
- Optimal Multi-View Video Transmission in Multiuser Wireless Networks by Exploiting Natural and View Synthesis-Enabled Multicast Opportunities — TCOM 2020, tcomm.2019.2954523, cpy 2.4 [video | multi-user/MA]

### modality:multimodal（9）
- A Unified Multi-Task Semantic Communication System for Multimodal Data — TCOM 2024, tcomm.2024.3364990, cpy 96.5 [multimodal | ]
- Resource Allocation for Multi-Modal Semantic Communication in UAV Collaborative Networks — TCOM 2025, tcomm.2025.3552303, cpy 41.2 [multimodal | UAV/vehicular/satellite, resource allocation]
- Optimizing Resource Allocation for Multi-Modal Semantic Communication in Mobile AIGC Networks: A Diffusion-Based Game Approach — TCCN 2025, tccn.2025.3529747, cpy 30.7 [multimodal | generative/LLM, resource allocation]
- Visual Language Model-Based Cross-Modal Semantic Communication Systems — TWC 2025, twc.2025.3539526, cpy 25.3 [image, multimodal | ]
- Synchronous Multi-Modal Semantic Communication System With Packet-Level Coding — TWC 2025, twc.2025.3534995, cpy 19.6 [multimodal | ]
- Agent-Driven Generative Semantic Communication With Cross-Modality and Prediction — TWC 2025, twc.2024.3519325, cpy 18.2 [multimodal | generative/LLM]
- Rate-Adaptive Coding Mechanism for Semantic Communications With Multi-Modal Data — TCOM 2024, tcomm.2023.3335977, cpy 17.4 [multimodal | adaptive]
- Image Generation With Supervised Selection Based on Multimodal Features for Semantic Communications — TCOM 2025, tcomm.2025.3615798, cpy 14.0 [image, multimodal, feature/inference | ]
- Semantic Feature Scheduling and Rate Control in Multi-Modal Distributed Network — TWC 2024, twc.2024.3480352, cpy 6.0 [multimodal, feature/inference | resource allocation]

### modality:text（7）
- Deep Source-Channel Coding for Sentence Semantic Transmission With HARQ — TCOM 2022, tcomm.2022.3180997, cpy 44.3 [text | JSCC, feedback/HARQ]
- A Robust Semantic Text Communication System — TWC 2024, twc.2024.3381950, cpy 38.2 [text | security/privacy]
- A GAN-Based Semantic Communication for Text Without CSI — TWC 2024, twc.2024.3415363, cpy 21.4 [text | generative/LLM]
- Semantic MIMO Systems for Speech-to-Text Transmission — TWC 2024, twc.2024.3472612, cpy 16.8 [text, speech/audio | MIMO]
- Semantic Coding for Text Transmission: An Iterative Design — TCCN 2022, tccn.2022.3192407, cpy 13.8 [text | ]
- Curriculum Learning for Goal-Oriented Semantic Communications With a Common Language — TCOM 2023, tcomm.2023.3236671, cpy 13.1 [text | task/goal-oriented]
- Performance Limits of a Deep Learning-Enabled Text Semantic Communication Under Interference — TWC 2024, twc.2024.3370497, cpy 11.0 [text | theory/limits]

### modality:speech/audio（5）
- Semantic Communication Systems for Speech Transmission — JSAC 2021, jsac.2021.3087240, cpy 130.8 [speech/audio | ]
- Deep Learning Enabled Semantic Communications With Speech Recognition and Synthesis — TWC 2023, twc.2023.3240969, cpy 91.9 [speech/audio | ]
- Semantic-Preserved Communication System for Highly Efficient Speech Transmission — JSAC 2023, jsac.2022.3221952, cpy 59.6 [speech/audio | ]
- Semantic MIMO Systems for Speech-to-Text Transmission — TWC 2024, twc.2024.3472612, cpy 16.8 [text, speech/audio | MIMO]
- Speech Semantic Communication Based on Swin Transformer — TCCN 2024, tccn.2023.3345858, cpy 11.1 [speech/audio | transformer/attention]

### modality:point-cloud/3D（2）
- ISCom: Interest-Aware Semantic Communication Scheme for Point Cloud Video Streaming on Metaverse XR Devices — JSAC 2024, jsac.2023.3345430, cpy 15.5 [video, point-cloud/3D | ]
- Task-Oriented Semantic Communication for Stereo-Vision 3D Object Detection — TCOM 2025, tcomm.2025.3545687, cpy 9.2 [image, point-cloud/3D | task/goal-oriented]

