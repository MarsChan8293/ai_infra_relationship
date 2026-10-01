---
type: project
name: "KernelBlaster"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/NVlabs/KernelBlaster
areas: ["agentic-kernel-optimization", "memory-augmented-icl", "reinforcement-learning", "cuda", "profiling", "replay-memory", "optimization-knowledge-base"]
hardware: ["nvidia"]
companies: ["NVIDIA"]
last_verified: "2026-10"
linked_companies:
  - "company/NVIDIA/NVIDIA"
---

# KernelBlaster

KernelBlaster 是 NVLabs 的 Memory-Augmented In-context Reinforcement Learning（MAIC-RL）CUDA 优化框架。它把 profiler feedback、持久化 CUDA 优化知识库和 replay-driven exploration 组合起来，使不同 kernel 与不同 GPU 代际之间的优化经验能够复用。

## 图谱价值

相较只保存 best kernel 的 Agent，KernelBlaster 更强调：

- profiling-guided state；
- persistent optimization database；
- replay / historical reward；
- 跨 task 经验累积；
- verification 与 reproducible evaluation。

它适合作为 Agentic Kernel Optimization 中 **Recipe / Optimization Memory** 层的直接参考。

## Sources

- https://github.com/NVlabs/KernelBlaster
- https://arxiv.org/abs/2602.14293

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
