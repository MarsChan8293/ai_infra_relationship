---
type: project
name: "Mirage Persistent Kernel"
linked_people: []
linked_concepts:
  - "concept/compiler/Kernel Compiler Pipeline"
layer: compiler
status: active
repository: https://github.com/mirage-project/mirage
docs: https://mirage-project.readthedocs.io/
areas: ["llm-inference", "persistent-kernel", "megakernel", "compiler", "gpu-runtime", "kernel-compiler-runtime"]
last_verified: "2026-10"
linked_companies: []
code_availability: public
---
# Mirage Persistent Kernel

Mirage Persistent Kernel（MPK）是 Catalyst 的 compiler + runtime 研究路线，用于把 LLM inference tensor programs 自动转换为高性能 megakernel。

## 核心机制

MPK 引入 SM-level graph representation，把依赖关系下沉到 streaming multiprocessor 粒度，从而支持 cross-operator software pipelining、fine-grained kernel overlap 等传统 kernel-per-operator runtime 很难表达的优化。Compiler 负责把 tensor program lower 成 SM-level task graph，in-kernel parallel runtime 则在 single megakernel 内用 decentralized scheduling 执行任务。

## AI Infra 位置

- 目标是减少多 kernel launch / synchronization 带来的 inference latency。
- 把 tensor program compilation 与 persistent-kernel runtime 连接起来。
- 论文报告相对 conventional kernel-per-operator LLM serving systems，端到端 inference latency 最多降低约 1.7×。

## 论文关系

OSDI 2026 论文作者包括 [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇]]、[[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航]]、[[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪]] 等。该关系表示论文合著，不自动扩展为所有作者对项目拥有相同治理角色。

## Sources

- https://catalyst.cs.cmu.edu/projects/mpk.html
- https://github.com/mirage-project/mirage
- https://mirage-project.readthedocs.io/
- https://arxiv.org/abs/2512.22219

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/compiler/Kernel Compiler Pipeline|Kernel Compiler Pipeline]]

<!-- END AUTO PROJECT CONCEPTS -->
