---
type: project
name: "CUDA-Agent"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/BytedTsinghua-SIA/CUDA-Agent
docs: https://cuda-agent.github.io/
areas: ["agentic-kernel-optimization", "agentic-rl", "cuda", "kernel-generation", "correctness-verification", "profiling"]
hardware: ["nvidia"]
companies: ["字节跳动"]
last_verified: "2026-10"
linked_companies:
  - "company/字节跳动/字节跳动"
code_availability: public
---

# CUDA-Agent

CUDA-Agent 是 ByteDance Seed × 清华 AIR 联合 SIA-Lab 公开的高性能 CUDA kernel generation 工作。项目把 agentic RL 与可执行 kernel 环境结合，并公开了训练数据、SKILL 和标准化 agent workspace。

## Agent Harness

`agent_workdir` 明确提供完整执行闭环：

`implement CUDA → compile → verify correctness → profile performance → iterate`

其中包含 baseline model、优化后的 custom CUDA extension、编译脚本、correctness verifier 与 profiler。

该项目同时连接了 **Agent Harness** 与 **Agentic RL / trajectory training** 两条路线，对长期把优化轨迹用于模型训练很有参考价值。

## Sources

- https://github.com/BytedTsinghua-SIA/CUDA-Agent
- https://cuda-agent.github.io/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/字节跳动/字节跳动|字节跳动]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
