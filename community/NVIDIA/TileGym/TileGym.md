---
type: project
name: "TileGym"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/NVIDIA/TileGym
areas: ["agentic-kernel-development", "agent-skills", "cutile", "kernel-autotuning", "benchmarking", "kernel-generation", "transformers-integration"]
hardware: ["nvidia"]
companies: ["NVIDIA"]
last_verified: "2026-10"
linked_companies:
  - "company/NVIDIA/NVIDIA"
code_availability: public
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
