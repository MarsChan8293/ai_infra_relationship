---
type: concept
name: Conditional Memory
aliases:
  - Conditional Lookup Memory
  - Scalable Lookup Memory
  - 条件记忆
domain: memory
topic: memory-hierarchy
related_concepts:
  - Host Memory
  - Memory Hierarchy
projects:
  - Engram
last_verified: "2026-10"
---
# Conditional Memory

## 一句话定义
Conditional Memory 把一部分模型容量组织为可按输入条件直接 lookup 的大规模静态 memory，而不是让每个 token 都通过完整 neural computation 读取全部容量。

## Engram
[[community/deepseek-ai/Engram/Engram|Engram]] 用 N-gram based deterministic addressing 实例化该机制，并把 lookup table 与动态 hidden state 融合。其系统意义在于地址可预测、访问模式明确，因此大表可以进一步放到 [[Host Memory]] 或远端 memory tier。

## 与 MoE 的区别
MoE 是 conditional **computation**：router 选择 expert 后仍执行神经网络计算；Conditional Memory 是 conditional **lookup**：容量更多体现在静态表项以及 memory bandwidth / latency。两者可以互补，而不是相互替代。

## Sources
- https://github.com/deepseek-ai/Engram
