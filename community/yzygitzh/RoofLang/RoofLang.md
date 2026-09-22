---
type: project
name: RoofLang
status: active
repository: https://github.com/yzygitzh/rooflang
docs: https://yzygitzh.github.io/rooflang/
layer: optimization
areas:
  - inference-optimization
  - system-architecture-search
  - graph-ir
  - roofline-modeling
  - discrete-event-simulation
  - placement
  - parallelism
  - kv-cache
  - agentic-optimization
hardware:
  - nvidia
  - ascend
last_verified: "2026-09"
---
# RoofLang

## 项目简介

RoofLang 是面向 **AI-driven LLM inference system architecting** 的领域特定语言（DSL）。它不绑定某个现有 serving engine，而是把 LLM workload 与 hardware 都表示成图，通过受约束、保持语义的 graph transformation 与 placement primitive 改写系统架构，再用 roofline-based discrete-event simulator 评估候选设计。

它的研究目标不是继续在固定软件栈里做局部 profiling / tuning，而是把「系统架构本身」变成 AI agent 可以搜索、验证和迭代的对象。

## 核心结构

- **Workload / compute graph**：描述算子、tensor、依赖以及 FLOPs / data movement 等分析属性。
- **Hardware graph**：描述 accelerator、CPU、NIC、memory 与 PCIe / NVLink / Ethernet 等 fabric。
- **Semantics-preserving transformations**：支持 kernel fuse/split/dup/dedup、通信合并以及控制依赖变换。
- **Placement**：把 operator 映射到 compute device，把 tensor 映射到 memory device。
- **Simulator**：以 topology-aware discrete-event simulation 估算 compute、memory、network、contention、lifetime 与 capacity。
- **Persistent optimizer agent**：在可验证 action space 上持续搜索 throughput / interactivity Pareto frontier。

论文明确指出 RoofLang 可以表达 PD disaggregation、KV-cache lifecycle，以及 TP / CP / DP / EP / PP 等典型 inference architecture choices。

## 当前模型与硬件覆盖

仓库当前包含 DeepSeek V4 Flash、DeepSeek V4 Pro、GLM-5.3、Kimi K3 等模型声明，并提供 NVIDIA H200 / GH200 / B300 / GB300 / RTX 6000D 以及 Ascend 950DT 等 hardware presets。

arXiv v2 的正式评估使用 NVIDIA H200、GH200、B300、GB300。项目主页特别说明这些结果属于用于设计比较的 analytical estimates，不应直接当作真实部署性能预测。

## 作者与组织

RoofLang v2 明确列出四位作者：

- [[community/yzygitzh/RoofLang/Ziyue Yang|Ziyue Yang]]：Shanghai Xingyunzhili Artificial Intelligence Institute；通讯作者。公开仓库当前代码/文档提交也主要可见其直接贡献。
- [[community/yzygitzh/RoofLang/Yuting Jiang|Yuting Jiang]]：Shanghai Xingyunzhili Artificial Intelligence Institute。
- [[community/yzygitzh/RoofLang/Lei Qu|Lei Qu]]：Shanghai Xingyunzhili Artificial Intelligence Institute。
- [[community/yzygitzh/RoofLang/Peng Cheng|Peng Cheng]]：Microsoft Research。

这里把论文 authorship 与仓库直接贡献分开：论文共同作者不自动升级为 repository maintainer。

## AI Infra 人才桥

RoofLang 的四位作者不是临时拼出的组合。四人此前共同参与 **SuperBench**（USENIX ATC 2024 Best Paper），把研究重点放在大规模 cloud AI infrastructure 的 proactive validation；四人又共同出现在 2025 年 **SIGMA** 训练栈论文中。RoofLang 因此形成一条清晰的研究迁移路径：

**AI infrastructure reliability / observability → heterogeneous training stack → LLM inference architecture modeling and autonomous search**。

这条连续作者网络比“共同机构”更强，适合作为后续人物关系验证的 evidence seed。

## 图谱边界

- 不把论文中引用、比较或建模的 vLLM / DistServe / 其他 serving systems 记为 `integrations`。
- 不因为 repo 中存在某种 hardware preset，就推断对应芯片厂商与项目存在组织级合作。
- 不把四位论文作者都标成 maintainer；当前只记录可直接核验的 authorship / repository contribution。
- SuperBench 与 SIGMA 是高价值后续 frontier，但本轮不递归创建，避免一次 targeted discovery 无限扩张。

## Sources

- https://github.com/yzygitzh/rooflang
- https://yzygitzh.github.io/rooflang/
- https://arxiv.org/abs/2609.12551
- https://arxiv.org/html/2609.12551v2
- https://www.usenix.org/conference/atc24/presentation/xiong
- https://arxiv.org/abs/2512.13488
