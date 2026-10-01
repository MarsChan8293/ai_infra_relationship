---
type: project
name: "Atrex Kernel Agent"
linked_people: []
layer: optimization
status: active
repository: https://github.com/alibaba/atrex-kernel-agent
areas: ["agentic-kernel-optimization", "mechanical-supervisor", "profiling", "correctness-gate", "performance-gate", "git-isolation", "production-kernel"]
hardware: ["nvidia", "amd", "t-head-ppu"]
companies: ["阿里巴巴"]
last_verified: "2026-10"
---

# Atrex Kernel Agent

Atrex Kernel Agent（AKA）是 Alibaba 开源的生产导向 GPU kernel optimization Agent。它把 coding agent、GPU profiling、correctness、performance verification、Git worktree isolation、recovery 与最终 promotion 放在一个机械化 supervisor 控制面下。

## 核心原则

Agent session 负责提出与实现修改；orchestrator 对 budget、状态迁移、sandbox、correctness/performance gate、rollback、aggregation 和最终 packaging 保持最终控制权。

公开实现支持 Triton、CuteDSL、CUDA、FlyDSL、TileLang，并提供 NVIDIA NCU 与 AMD rocprof 路径。

## Sources

- https://github.com/alibaba/atrex-kernel-agent
- https://arxiv.org/abs/2607.14541
