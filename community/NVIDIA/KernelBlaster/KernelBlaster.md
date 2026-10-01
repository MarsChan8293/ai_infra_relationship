---
type: project
name: "KernelBlaster"
linked_people: []
layer: optimization
status: active
repository: https://github.com/NVlabs/KernelBlaster
areas: ["agentic-kernel-optimization", "memory-augmented-icl", "reinforcement-learning", "cuda", "profiling", "replay-memory", "optimization-knowledge-base"]
hardware: ["nvidia"]
companies: ["NVIDIA"]
last_verified: "2026-10"
---

# KernelBlaster

KernelBlaster 是 NVLabs 的 Memory-Augmented In-context Reinforcement Learning（MAIC-RL）CUDA 优化框架。它把 profiler feedback、持久化 CUDA 优化知识库和 replay-driven exploration 组合起来，使不同 kernel 与不同 GPU 代际之间的优化经验能够复用。

## 图谱价值

相较只保存 best kernel 的 Agent，KernelBlaster 更强调：

- profiling-guided state；
- persistent optimization database；
- replay / historical reward；
- 跨 task 经验累积；
- verification 与 reproducible evaluation。

它适合作为 Agentic Kernel Optimization 中 **Recipe / Optimization Memory** 层的直接参考。

## Sources

- https://github.com/NVlabs/KernelBlaster
- https://arxiv.org/abs/2602.14293
