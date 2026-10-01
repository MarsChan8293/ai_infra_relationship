---
type: project
name: "Atrex Kernel Agent"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/alibaba/atrex-kernel-agent
areas: ["agentic-kernel-optimization", "mechanical-supervisor", "profiling", "correctness-gate", "performance-gate", "git-isolation", "production-kernel"]
hardware: ["nvidia", "amd", "t-head-ppu"]
companies: ["阿里巴巴"]
last_verified: "2026-10"
linked_companies:
  - "company/阿里巴巴/阿里巴巴"
---

# Atrex Kernel Agent

Atrex Kernel Agent（AKA）是 Alibaba 开源的生产导向 GPU kernel optimization Agent。它把 coding agent、GPU profiling、correctness、performance verification、Git worktree isolation、recovery 与最终 promotion 放在一个机械化 supervisor 控制面下。

## 核心原则

Agent session 负责提出与实现修改；orchestrator 对 budget、状态迁移、sandbox、correctness/performance gate、rollback、aggregation 和最终 packaging 保持最终控制权。

公开实现支持 Triton、CuteDSL、CUDA、FlyDSL、TileLang，并提供 NVIDIA NCU 与 AMD rocprof 路径。

## Sources

- https://github.com/alibaba/atrex-kernel-agent
- https://arxiv.org/abs/2607.14541

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/阿里巴巴/阿里巴巴|阿里巴巴]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
