---
type: project
name: "AscendCraft"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: unknown
maturity: research-prototype
docs: https://arxiv.org/abs/2601.22760
organization: "南京大学"
areas: ["agentic-kernel-optimization", "ascendc", "dsl", "transcompilation", "kernel-generation", "constraint-guided-lowering"]
hardware: ["ascend"]
companies: ["华为"]
last_verified: "2026-10"
linked_companies:
  - "company/华为/华为"
code_availability: unconfirmed
---

# AscendCraft

AscendCraft 是南京大学与 Huawei Software Engineering Application Technology Laboratory 合作的 Ascend NPU kernel generation 研究系统。

## 核心机制

直接让 LLM 生成 AscendC 的可行性较低，因此 AscendCraft 先让模型生成一个显式表达 Ascend execution semantics 的轻量 DSL，再通过结构化、constraint-driven lowering 把 DSL 转成 AscendC。

该路线把复杂 NPU 编程模型拆成“Agent-friendly representation → deterministic/structured lowering”，适合作为 Agentic Kernel Optimization 的中间表示参考。

## Sources

- https://arxiv.org/abs/2601.22760

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
