---
type: project
name: "KernelAgent"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/meta-pytorch/KernelAgent
areas: ["agentic-kernel-optimization", "triton", "multi-agent", "ncu", "roofline", "correctness-verification", "benchmarking"]
hardware: ["nvidia", "intel-xpu"]
companies: ["Meta"]
last_verified: "2026-10"
linked_companies:
  - "company/Meta/Meta"
---

# KernelAgent

KernelAgent 是 Meta / PyTorch 生态公开的 autonomous GPU kernel generation & optimization 系统。它将 PyTorch 程序拆解为可融合子图，并行生成 Triton kernel，执行严格 correctness verification，再使用硬件 profiling 驱动多轮优化。

## 优化闭环

公开 pipeline 包含：

1. NCU profiling；
2. roofline / bottleneck diagnosis；
3. LLM 生成优化候选；
4. numerical correctness verification；
5. CUDA event benchmark；
6. best-so-far 与 divergence-based revert。

因此它是很直接的 **NVIDIA KernelOptimizer runtime** 参考实现。

## Sources

- https://github.com/meta-pytorch/KernelAgent
- https://pytorch.org/blog/kernelfalcon-autonomous-gpu-kernel-generation-via-deep-agents/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Meta/Meta|Meta]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
