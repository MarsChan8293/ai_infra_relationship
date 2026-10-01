---
type: project
name: "KernelEvolve"
linked_people: []
layer: optimization
status: research
docs: https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/
areas: ["agentic-kernel-optimization", "tree-search", "evolutionary-search", "optimization-memory", "production-kernels", "heterogeneous-hardware"]
hardware: ["nvidia", "amd", "mtia", "cpu"]
companies: ["Meta"]
last_verified: "2026-10"
---

# KernelEvolve

KernelEvolve 是 Meta 公开介绍的生产级 agentic kernel authoring system，用于在训练和推理场景中自动搜索、生成并优化高性能 kernel。

## 设计特点

公开材料将 kernel optimization 视为长程搜索问题，而不是一次代码生成。系统结合候选搜索、执行验证、硬件知识和优化记忆，探索大量实现，再把通过验证的结果用于真实生产 workload。

核心实现当前没有以完整开源仓库形式发布，因此本节点记录的是 **公开生产系统 / research system**，不把它误写成可直接 fork 的开源 Harness。

## Sources

- https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/
