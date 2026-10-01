---
type: project
name: KDA
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/NVlabs/kda
docs: https://nvlabs.github.io/kda/
areas:
  - "agentic-kernel-optimization"
  - "cuda-kernel"
  - "profiling"
  - "benchmarking"
  - "performance-engineering"
hardware:
  - "nvidia"
integrations:
  - "CUTLASS"
  - "FlashInfer"
  - "SGLang"
  - "vLLM"
  - "DeepGEMM"
companies: ["NVIDIA"]
last_verified: "2026-09"
linked_companies:
  - "company/NVIDIA/NVIDIA"
---
# KDA (Kernel Design Agents)

> NVIDIA / NVLabs 的 agent-centric CUDA kernel 优化工作流：让 coding agents 围绕性能敏感 kernel 执行研究、实现、正确性验证、profiling / benchmark 与迭代优化。

## 定位

KDA 当前是 early research prototype，而不是通用 LLM serving runtime。它关注的是 AI Infra 更底层的 kernel performance engineering：把 kernel 任务定义、候选实现、验证、性能测量和最终 promotion decision 组织成可重复的 agent workflow。

官方最小流程强调：

1. 为目标 kernel 建立独立 implementation workspace；
2. 明确 objective、constraints、validation command 与 promotion criteria；
3. 由 agent 先研究并形成可执行计划；
4. 小步实现，每次有意义的修改后进行验证；
5. 保存候选、benchmark / evaluation、profiling evidence 和最终选择依据。

## AI Infra 价值

KDA 把“CUDA kernel 优化”进一步转化为可由 coding agent 持续执行的闭环，因此处在以下交叉点：

- CUDA / GPU kernel performance engineering
- AI coding agents
- profiling 与 benchmark-driven optimization
- LLM inference kernel ecosystem

这使它与传统 kernel library（如 CUTLASS）不同：KDA 的核心不是提供一组固定 kernel，而是提供自动研究和优化 kernel 的 agentic workflow。

## 生态连接

- [[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：KDA 发布材料包含 CUTLASS 来源的 kernel / reference artifacts；两者共同位于 NVIDIA CUDA kernel 生态。
- [[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]]：KDA 分发的研究/参考材料包含 FlashInfer 来源内容；README 同时指向 MLSys 2026 FlashInfer Kernel Contest 的性能复现。
- [[community/sgl-project/SGLang/SGLang|SGLang]]：KDA 的第三方研究/参考材料包含 SGLang 来源内容。
- [[vLLM]]：KDA 的第三方研究/参考材料包含 vLLM 来源内容。
- [[DeepGEMM]]：KDA 的第三方研究/参考材料包含 DeepGEMM 来源内容。
- KernelWiki / ncu-report-skill：README 将两者作为 agent workflow 的技能依赖，其中 KernelWiki 以 pinned submodule 形式集成。

注意：上述 integrations 表示 KDA 有直接可核验的软件/材料集成或依赖关系，不意味着 KDA 对这些上游项目拥有治理关系。

## 硬件边界

核心 workflow 本身被描述为不绑定单一 benchmark harness 或 hardware target；但官方 Community Kernel Wishlist 截至 2026-09 明确只支持 NVIDIA B200 / B300 请求。因此本页 hardware 记录为 NVIDIA，不外推 AMD / Ascend 等后端。

## 社区机制

KDA 提供 Community Kernel Wishlist。社区可以通过 wishlist 分支 PR 提交需要优化的 kernel，并要求给出：

- 可复现的任务定义
- representative workloads
- best-known baseline implementation
- correctness / validation 信息

该机制使 KDA 不只是内部实验代码，也形成了“真实 kernel 请求 → agent 优化 → benchmark / profiling 证据”的公开入口。

## 图谱关系

- [[company/NVIDIA/NVIDIA|NVIDIA]]：KDA 位于 NVlabs GitHub namespace，项目网站位于 NVLabs Pages；本图谱按 NVIDIA / NVLabs 项目记录。
- [[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：kernel infrastructure / reference ecosystem。
- [[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]]：inference kernel workload / reference ecosystem。
- [[community/sgl-project/SGLang/SGLang|SGLang]]：LLM serving 下游 workload / reference ecosystem。

人物层暂不因博客作者名单自动建立“核心 maintainer”关系；后续应以 repository commits、公开作者页、upstream PR 和明确 affiliation 证据做 BFS，避免把论文/博客署名误写为项目治理角色。

## Sources

- https://github.com/NVlabs/kda
- https://github.com/NVlabs/kda/blob/main/README.md
- https://github.com/NVlabs/kda/blob/main/THIRD_PARTY_NOTICES.md
- https://nvlabs.github.io/kda/

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->
