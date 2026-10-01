---
type: project
name: "Compiler-Grounded Hierarchical Diagnosis"
linked_people: []
layer: optimization
status: research
docs: https://arxiv.org/abs/2607.23089
areas: ["agentic-kernel-optimization", "triton-ascend", "compiler-feedback", "ir-diagnosis", "profiling", "hierarchical-diagnosis"]
hardware: ["ascend"]
companies: ["华为"]
last_verified: "2026-10"
---

# Compiler-Grounded Hierarchical Diagnosis

这是 Huawei Technologies 公开的 LLM-based Triton kernel optimization research system，重点解决“profiler 知道慢，但 Agent 不知道 compiler 为什么没有实现预期优化”的问题。

## 核心机制

系统按层级逐步升级诊断：

`pattern triage → profiling diagnosis → IR attribution → compiler-grounded analysis → source rewrite`

它把 runtime symptom、IR structure 和 backend compiler behavior 串成证据链，再让 Agent 做 source-level rewrite。该思路非常适合作为 Ascend 侧 **Compiler Agent / IR diagnosis** 层参考。

## Sources

- https://arxiv.org/abs/2607.23089
