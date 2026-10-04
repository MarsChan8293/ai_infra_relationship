---
type: project
name: "Hyperloom"
linked_people: []
linked_concepts:
  - "concept/inference/optimization/Agentic Inference Optimization"
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/AMD-AGI/Hyperloom
docs: https://rocm.docs.amd.com/projects/hyperloom/
areas: ["agentic-inference-optimization", "agentic-kernel-optimization", "multi-agent", "e2e-validation", "recipe-memory", "vllm", "sglang", "xdit"]
hardware: ["amd"]
companies: ["AMD"]
last_verified: "2026-10"
linked_companies:
  - "company/AMD/AMD"
code_availability: public
---

# Hyperloom

ROCm Hyperloom 是 AMD-AGI 的多 Agent 推理优化 Harness，目标是自动优化 AMD Instinct 上的推理 workload。公开实现覆盖 vLLM、SGLang 与 xDiT，并把 framework optimization、kernel optimization、sweep、端到端 validation 与跨 session Recipe Knowledge Base 组织成闭环。

## 核心机制

典型阶段为：

`PRELUDE → ENABLEMENT → FRAMEWORK_AGENT → KERNEL_AGENT → SWEEP → CLOSE`

Hyperloom 强调局部 kernel speedup 不能直接视为成功；候选必须重新回到真实 workload 做端到端验证。KEEP / REVERT、baseline anchor 和 Recipe KB 使优化过程可审计、可复用。

## Sources

- https://github.com/AMD-AGI/Hyperloom
- https://rocm.docs.amd.com/projects/hyperloom/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]
- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/AMD/AMD|AMD]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
