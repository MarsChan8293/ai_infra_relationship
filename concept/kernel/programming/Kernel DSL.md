---
type: concept
name: Kernel DSL
aliases:
  - GPU Kernel DSL
  - Kernel Domain-Specific Language
  - 算子DSL
  - Kernel编程语言
domain: compiler
topic: kernel-programming
related_concepts:
  - JIT Kernel Compilation
  - Kernel Fusion
  - GEMM
  - Attention Kernel
projects:
  - Triton
  - TileLang
  - CUTLASS
  - FlagTree
last_verified: 2026-09
---

# Kernel DSL

## 一句话定义

Kernel DSL 是专门用于描述 GPU/NPU 高性能算子的领域专用语言，让开发者用比 CUDA/C++ 更高层的抽象表达 tiling、memory movement、layout 和并行映射。

## 解决的问题

手写 CUDA kernel 能获得很强的硬件控制，但开发成本高、可移植性差。通用 tensor graph 又常隐藏太多硬件细节。Kernel DSL 试图在两者之间提供一个“可编程但仍能控制性能关键路径”的层。

## 核心抽象

不同 DSL 语法不同，但通常会暴露：

- tile / block / thread 的工作切分。
- global / shared / register / tensor memory 的数据放置。
- async copy 与 software pipeline。
- tensor-core / MMA 等硬件计算原语。
- layout、swizzle、vectorization 和 synchronization。
- autotuning、specialization 与 [[JIT Kernel Compilation]]。

## 与普通编译器 IR 的区别

Kernel DSL 面向 kernel 作者，强调“如何写一个高性能算子”；编译器 IR 更偏向编译器内部表示。很多系统内部会把 DSL lowering 到 MLIR、TVM IR 或自有 IR，再生成 CUDA / HIP / NPU code。

## 项目实现

[[community/triton-lang/Triton/Triton|Triton]] 用 Python 风格 DSL 编写 GPU kernel；[[community/tile-ai/TileLang/TileLang|TileLang]] 暴露 tile-level memory/dataflow 编程模型；[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]] 4.x 提供 CuTe/CUTLASS Python DSL；[[community/flagos-ai/FlagTree/FlagTree|FlagTree]] 在 Triton 体系上扩展面向多后端的 kernel 编程/代码生成抽象。

## Sources

- https://triton-lang.org/main/index.html
- https://tilelang.com/
- https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/overview.html
- https://github.com/flagos-ai/FlagTree
