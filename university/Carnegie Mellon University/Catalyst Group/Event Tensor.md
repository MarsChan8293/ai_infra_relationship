---
type: project
name: "Event Tensor"
linked_people: []
linked_concepts:
  - "concept/compiler/Kernel Compiler Pipeline"
layer: "compiler-runtime"
status: research
docs: https://arxiv.org/abs/2604.13327
areas:
  - "dynamic-megakernel"
  - "persistent-kernel"
  - "dynamic-shapes"
  - "data-dependent-computation"
  - "compiler"
  - "llm-inference"
last_verified: "2026-10"
linked_companies: []
---

# Event Tensor

Event Tensor 是面向 **dynamic megakernel** 的 compiler abstraction。它解决 persistent / mega-kernel 在真实 LLM workload 中遇到的核心问题：shape-dependent dynamism 与 data-dependent computation。

## 核心机制

Event Tensor 通过 tiled task 之间的 event dependency 表达执行约束，并在此基础上构建 Event Tensor Compiler（ETC）。ETC 可以执行 static 与 dynamic scheduling transformation，生成适用于动态 workload 的 high-performance persistent kernel。

它与 [[university/Carnegie Mellon University/Catalyst Group/Mirage Persistent Kernel|Mirage Persistent Kernel]] 的关系可以理解为：

```text
MPK
Tensor Program
  ↓
SM-level graph / persistent runtime
  ↓
MegaKernel

Event Tensor / ETC
Dynamic workload
  ↓
Event dependency between tiled tasks
  ↓
Static + Dynamic Scheduling
  ↓
Dynamic MegaKernel
```

前者强调 end-to-end mega-kernelization 与 SM-level runtime；Event Tensor 进一步把动态 shape 和数据依赖变成 compiler 可表达、可调度的对象。

## 研究归属证据

论文发表于 MLSys 2026。CMU Catalyst Research Summit 2026 的项目议程明确列出 “TIRX and Event Tensor: Bringing ML Compiler for Frontier Kernel Programming”，因此本节点挂在 Catalyst Group 下；这表示公开研究关联，不推断单一组织对全部作者或实现拥有所有权。

## Sources

- https://arxiv.org/abs/2604.13327
- https://proceedings.mlsys.org/paper_files/paper/2026/hash/53d3f45797970d323bd8a0d379c525aa-Abstract-Conference.html
- https://catalyst.cs.cmu.edu/summit.html

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/compiler/Kernel Compiler Pipeline|Kernel Compiler Pipeline]]

<!-- END AUTO PROJECT CONCEPTS -->
