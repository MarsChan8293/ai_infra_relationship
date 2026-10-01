---
type: project
name: "KernelEvolve"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: research
docs: https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/
areas: ["agentic-kernel-optimization", "tree-search", "evolutionary-search", "optimization-memory", "production-kernels", "heterogeneous-hardware"]
hardware: ["nvidia", "amd", "mtia", "cpu"]
companies: ["Meta"]
last_verified: "2026-10"
linked_companies:
  - "company/Meta/Meta"
---

# KernelEvolve

KernelEvolve 是 Meta 公开介绍的生产级 agentic kernel authoring system，用于在训练和推理场景中自动搜索、生成并优化高性能 kernel。

## 设计特点

公开材料将 kernel optimization 视为长程搜索问题，而不是一次代码生成。系统结合候选搜索、执行验证、硬件知识和优化记忆，探索大量实现，再把通过验证的结果用于真实生产 workload。

核心实现当前没有以完整开源仓库形式发布，因此本节点记录的是 **公开生产系统 / research system**，不把它误写成可直接 fork 的开源 Harness。

## Sources

- https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Meta/Meta|Meta]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
