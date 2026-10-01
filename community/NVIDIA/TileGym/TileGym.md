---
type: project
name: "TileGym"
linked_people: []
layer: optimization
status: active
repository: https://github.com/NVIDIA/TileGym
areas: ["agentic-kernel-development", "agent-skills", "cutile", "kernel-autotuning", "benchmarking", "kernel-generation", "transformers-integration"]
hardware: ["nvidia"]
companies: ["NVIDIA"]
last_verified: "2026-10"
---

# TileGym

TileGym 是 NVIDIA 官方的 CUDA Tile kernel library / playground，同时正在形成面向 coding agent 的 kernel development Skill 与评测工作流。

## Agentic 价值

NVIDIA Skills 已公开 TileGym 相关能力，例如：

- adding cuTile kernel；
- cuTile autotuning；
- improve kernel performance；
- cross-framework conversion；
- monkey-patch kernels into Transformers。

其贡献流程将新 kernel 的 implementation、correctness test 和 performance benchmark 绑定在一起。它不是完整 autonomous search system，但适合作为 NVIDIA 侧 **Agent Skill + Kernel Evaluation Harness** 参考。

## Sources

- https://github.com/NVIDIA/TileGym
- https://github.com/NVIDIA/skills
