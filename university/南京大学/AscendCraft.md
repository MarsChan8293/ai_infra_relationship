---
type: project
name: "AscendCraft"
linked_people: []
layer: optimization
status: research
docs: https://arxiv.org/abs/2601.22760
organization: "南京大学"
areas: ["agentic-kernel-optimization", "ascendc", "dsl", "transcompilation", "kernel-generation", "constraint-guided-lowering"]
hardware: ["ascend"]
companies: ["华为"]
last_verified: "2026-10"
---

# AscendCraft

AscendCraft 是南京大学与 Huawei Software Engineering Application Technology Laboratory 合作的 Ascend NPU kernel generation 研究系统。

## 核心机制

直接让 LLM 生成 AscendC 的可行性较低，因此 AscendCraft 先让模型生成一个显式表达 Ascend execution semantics 的轻量 DSL，再通过结构化、constraint-driven lowering 把 DSL 转成 AscendC。

该路线把复杂 NPU 编程模型拆成“Agent-friendly representation → deterministic/structured lowering”，适合作为 Agentic Kernel Optimization 的中间表示参考。

## Sources

- https://arxiv.org/abs/2601.22760
