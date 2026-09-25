---
type: project
name: Triton
linked_people: []
linked_concepts:
  - "concept/compiler/Autotuning"
  - "concept/compiler/Backend Code Generation"
  - "concept/compiler/Compiler Lowering"
  - "concept/kernel/gemm/GEMM"
  - "concept/kernel/programming/JIT Kernel Compilation"
  - "concept/compiler/Kernel Compiler Pipeline"
  - "concept/kernel/programming/Kernel DSL"
layer: compiler
status: active
repository: https://github.com/triton-lang/triton
docs: https://triton-lang.org/main/index.html
areas:
  - "gpu-kernel-dsl"
  - "compiler"
  - "jit"
  - "mlir"
hardware:
  - "nvidia"
  - "amd"
integrations:
last_verified: "2026-09"
linked_companies: []
---
# Triton

> 用于编写高性能并行计算与深度学习 kernel 的语言和编译器。

## 核心能力

| 能力 | 说明 |
|---|---|
| Python DSL | 用 Python 风格语言描述 GPU kernel |
| Compiler | 把 Triton 程序编译到底层 GPU 代码 |
| JIT | 支持运行时特化与编译 |
| MLIR | 使用 Triton MLIR dialect 表达和优化程序 |

## 边界

Triton 是 kernel 开发与编译层，不负责模型 serving 或集群编排。它与 Triton Inference Server 名称相近，但后者是模型服务服务器，职责完全不同。

## 集成与后端

V0.1 暂不把“项目内部存在 Triton kernel”自动升级为强集成关系。

## 关联项目

- 上层推理：vLLM、SGLang。
- Kernel 库：FlashInfer、FlashAttention、CUTLASS、DeepGEMM。
- DSL / Compiler 对照：TileLang、DeepJIT、FlagTree。
- 名称辨析：Triton Inference Server。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方资料为快照。

## 直接来源

- https://triton-lang.org/main/index.html
- https://github.com/triton-lang/triton

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/compiler/Autotuning|Autotuning]]
- [[concept/compiler/Backend Code Generation|Backend Code Generation]]
- [[concept/compiler/Compiler Lowering|Compiler Lowering]]
- [[concept/kernel/gemm/GEMM|GEMM]]
- [[concept/kernel/programming/JIT Kernel Compilation|JIT Kernel Compilation]]
- [[concept/compiler/Kernel Compiler Pipeline|Kernel Compiler Pipeline]]
- [[concept/kernel/programming/Kernel DSL|Kernel DSL]]

<!-- END AUTO PROJECT CONCEPTS -->
