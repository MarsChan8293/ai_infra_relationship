---
type: project
name: "Compiler-Grounded Hierarchical Diagnosis"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: unknown
maturity: research-prototype
docs: https://arxiv.org/abs/2607.23089
areas: ["agentic-kernel-optimization", "triton-ascend", "compiler-feedback", "ir-diagnosis", "profiling", "hierarchical-diagnosis"]
hardware: ["ascend"]
companies: ["华为"]
last_verified: "2026-10"
linked_companies:
  - "company/华为/华为"
code_availability: unconfirmed
---

# Compiler-Grounded Hierarchical Diagnosis

这是 Huawei Technologies 公开的 LLM-based Triton kernel optimization research system，重点解决“profiler 知道慢，但 Agent 不知道 compiler 为什么没有实现预期优化”的问题。

## 核心机制

系统按层级逐步升级诊断：

`pattern triage → profiling diagnosis → IR attribution → compiler-grounded analysis → source rewrite`

它把 runtime symptom、IR structure 和 backend compiler behavior 串成证据链，再让 Agent 做 source-level rewrite。该思路非常适合作为 Ascend 侧 **Compiler Agent / IR diagnosis** 层参考。

## Sources

- https://arxiv.org/abs/2607.23089

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
