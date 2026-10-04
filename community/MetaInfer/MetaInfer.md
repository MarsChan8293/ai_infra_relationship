---
type: project
name: MetaInfer
linked_people:
  - "community/MetaInfer/Chen Hu"
  - "community/MetaInfer/Honglin Wang"
  - "community/MetaInfer/Mingheng Mi"
  - "community/MetaInfer/Pu Wang"
  - "community/MetaInfer/Tian Chen"
  - "community/MetaInfer/Zhenwen Miao"
  - "university/琶洲实验室（黄埔）/张海 Hai Zhang"
linked_concepts:
  - "concept/inference/optimization/Agentic Inference Optimization"
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/MetaInfer/MetaInfer
areas: [llm-inference, inference-framework-generation, ai-infra-agent, kernel-optimization, model-porting, performance-optimization, heterogeneous-compute, model-hardware-co-adaptation]
hardware: [nvidia, hygon]
last_verified: 2026-10
linked_companies: []
code_availability: public
---
# MetaInfer

MetaInfer 是一个由 LLM / coding agent 驱动的 AI Infra 优化工具箱。项目早期重点是根据模型、硬件、并行、量化以及吞吐/时延约束自动生成紧凑的专用 LLM inference framework；截至 arXiv v3，其研究表述进一步扩展为 **model-framework-kernel-hardware co-adaptation**：把模型语义、framework dispatch、kernel、硬件能力、运行证据与 serving objective 组织成可搜索、可修复、可优化的执行适配路径。

## 推理优化方向

- **Inference framework generation**：内置 `gen-infer-framework` 任务，可生成带 OpenAI-compatible HTTP API 的模型特定推理服务，并通过固定 prompt 与 LLM judge 做正确性验证。
- **AI-assisted kernel optimization**：围绕目标 kernel 运行自动化的 optimize → benchmark 循环。
- **Model porting / co-adaptation**：把新模型能力移植到既有 GPU / accelerator 软件栈，并通过补丁、验证与 profiling 恢复或降低执行路径成本。
- **Performance modeling**：`calc-theoretical-value` 可计算单次 LLM forward 的理论 FLOPs 与 memory traffic。
- **Agent-driven infra engineering**：通过 `SubAgentManager` 调度 coding agent；README 当前列出 Claude/ccb、Codex 与 pi backend。
- **异构验证**：arXiv v3 公开案例覆盖 NVIDIA A800 与 Hygon K100AI DCU，说明项目已从单一 NVIDIA 优化工具箱扩展到异构 accelerator 适配问题。

## 论文版本演进

MetaInfer 对应的 arXiv 条目为 **2607.12875**。该条目在 2026 年发生了明显的题目与作者变化，因此不能只记录一个静态标题。

### v1 — 2026-07-14

**MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox**

Authors:
- [[Zhenwen Miao]]
- [[Honglin Wang]]
- [[Mingheng Mi]]

这一版提出“LLM-as-Compiler”与 contract knowledge base（CKB），重点验证在知识约束下自动生成定制 inference engine。

### v2 — 2026-08-19

题目仍为 **MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox**，作者扩展为：
- [[Zhenwen Miao]]
- [[Honglin Wang]]
- [[Mingheng Mi]]
- [[Pu Wang]]
- [[Chen Hu]]
- [[university/琶洲实验室（黄埔）/张海 Hai Zhang|张海（Hai Zhang）]]

### v3 — 2026-09-01（当前 arXiv 版本）

题目更新为 **Automatic Model-Hardware Co-Adaptation for Heterogeneous AI Accelerators**。

Authors:
- [[Tian Chen]]
- [[Mingheng Mi]]
- [[Pu Wang]]
- [[Chen Hu]]
- [[university/琶洲实验室（黄埔）/张海 Hai Zhang|张海（Hai Zhang）]]

v3 仍明确把 **MetaInfer** 作为核心系统，但研究问题从“知识驱动生成 inference engine”扩展为“模型—框架—kernel—硬件协同适配”。公开案例包括 DeepSeek V4 Flash on NVIDIA A800、GLM 5.3 Flash on NVIDIA A800，以及 DeepSeek V4 Flash on Hygon K100AI DCU。

> 注意：MetaInfer GitHub README 截至本次核验仍主要引用 v1 的旧标题与三位作者；arXiv 当前元数据已经更新到 v3。仓库图谱因此同时保留 v1 历史来源和 v3 当前状态。

## 与琶洲实验室（黄埔）的关系

[[university/琶洲实验室（黄埔）/琶洲实验室（黄埔）|琶洲实验室（黄埔）]]（Pazhou Laboratory (Huangpu)）已作为独立 research-institution 节点纳入图谱。

- 当前论文索引将 arXiv:2607.12875 / MetaInfer 与 **Pazhou Laboratory (Huangpu)** affiliation 联系起来。
- v2/v3 作者 [[university/琶洲实验室（黄埔）/张海 Hai Zhang|张海（Hai Zhang）]] 的实验室身份可由琶洲实验室（黄埔）官方页面独立验证；2026 年官方信息列其为实验室常务副主任。
- 这足以建立“**研究机构 ↔ 人物 ↔ MetaInfer**”的直接研究关系，但不足以把琶洲实验室（黄埔）写成 `MetaInfer/MetaInfer` GitHub organization 的 owner、唯一发起方或仓库治理主体。
- v1 作者 Zhenwen Miao、Honglin Wang，以及其他 v2/v3 作者，不因为同一论文出现机构 affiliation 就自动写入实验室 current affiliation；没有独立身份映射证据的，人物页只保留 paper/project credit。

## Repository identity

用户最初发现入口为 `HuangPuStar/MetaInfer`。截至 2026-10 核验，项目 README 中给出的 canonical clone / project URL 为 `MetaInfer/MetaInfer`，因此本图谱只建立一个 canonical **MetaInfer** 项目节点，以避免 namespace 变化产生重复项目。

## 图谱价值

MetaInfer 位于 **AI-for-AI-Infra / inference optimization automation** 这一新方向：它不是单纯 serving runtime，而是让 coding agent / LLM 参与 inference framework generation、kernel optimization、模型移植和异构软硬件 co-adaptation。它因此同时连接：

- [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]
- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]
- inference engine generation
- heterogeneous accelerator adaptation
- AI Infra 人才 / 研究机构网络

## Sources

- https://github.com/MetaInfer/MetaInfer
- https://github.com/HuangPuStar/MetaInfer
- https://arxiv.org/abs/2607.12875
- https://arxiv.org/abs/2607.12875v1
- https://www.pazhoulab-huangpu.com/
- https://iacc.pazhoulab-huangpu.com/intro/
- https://thelatestinai.com/topics/llm-driven

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]
- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/MetaInfer/Chen Hu|Chen Hu]]：项目关联；人物页已明确记录该项目。
- [[community/MetaInfer/Honglin Wang|Honglin Wang]]：arXiv:2607.12875 v1（2026-07-14）作者之一，论文题为 **MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox**。
- [[community/MetaInfer/Mingheng Mi|Mingheng Mi]]：v1（2026-07-14）：**MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox** 作者之一。
- [[community/MetaInfer/Pu Wang|Pu Wang]]：项目关联；人物页已明确记录该项目。
- [[community/MetaInfer/Tian Chen|Tian Chen]]：项目关联；人物页已明确记录该项目。
- [[community/MetaInfer/Zhenwen Miao|Zhenwen Miao]]：arXiv:2607.12875 v1（2026-07-14）作者之一，论文题为 **MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox**。
- [[university/琶洲实验室（黄埔）/张海 Hai Zhang|张海（Hai Zhang）]]：[[community/MetaInfer/MetaInfer|MetaInfer]]：arXiv:2607.12875 v2/v3 作者。v3（2026-09-01）题为 **Automatic Model-Hardware Co-Adaptation for Heterogeneous AI Accelerators**。

<!-- END AUTO PROJECT PEOPLE -->
