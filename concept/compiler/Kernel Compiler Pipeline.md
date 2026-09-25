---
type: concept
name: Kernel Compiler Pipeline
aliases:
  - Kernel Compilation Pipeline
  - GPU Kernel Compiler Pipeline
  - 算子编译流水线
domain: compiler
topic: kernel-compilation
related_concepts:
  - Kernel DSL
  - Compiler Lowering
  - Backend Code Generation
  - JIT Kernel Compilation
  - Ahead-of-Time Compilation
projects:
  - NineToothed
  - TileLang
  - Triton
  - FlagTree
last_verified: 2026-09
---

# Kernel Compiler Pipeline

## 一句话定义

Kernel Compiler Pipeline 是把上层 kernel/DSL 表达逐步转换为目标 GPU/NPU 可执行代码的一系列 IR、pass、lowering、codegen 与 runtime materialization 阶段。

## 解决的问题

高性能 kernel 很少能从一个 Python/DSL AST 一步变成机器码。不同抽象层需要分别处理 shape、layout、memory scope、thread mapping、tensor-core instruction、backend capability 和 target architecture。

因此现代 kernel compiler 往往采用多阶段 pipeline，让每一层只解决一类问题。

## 典型阶段

1. **Frontend / AST / DSL capture**：读取 [[Kernel DSL]] 程序。
2. **High-level IR**：保留 tile、tensor、layout 等语义。
3. **[[Compiler Lowering]]**：逐步显式化循环、memory、thread、instruction。
4. **Optimization passes**：fusion、layout、pipeline、vectorization、canonicalization。
5. **[[Backend Code Generation]]**：生成 CUDA、HIP、Triton、TileLang backend 或 vendor-specific code。
6. **Materialization**：通过 [[JIT Kernel Compilation]] 或 [[Ahead-of-Time Compilation]] 生成 binary / executable artifact。

## 为什么要分层

过早降低到低层 IR 会丢失高层语义，过晚暴露硬件细节又难以做到极致优化。多级 IR 的价值就是在“可分析性”和“硬件可控性”之间逐层过渡。

## 项目实现

[[community/InfiniTensor/NineToothed|NineToothed]] 已公开 SSA compiler pipeline、pass/backend registry 和 multi-backend runtime；[[community/tile-ai/TileLang/TileLang|TileLang]] 在 TVM 基础上具有 frontend、layout inference、pass pipeline 和 device/host codegen；[[community/triton-lang/Triton/Triton|Triton]] 通过 Triton/MLIR dialect 逐层 lower 到 GPU code；[[community/flagos-ai/FlagTree/FlagTree|FlagTree]] 基于 Triton 体系扩展多后端 code generation。

## Sources

- https://github.com/InfiniTensor/ninetoothed
- https://tilelang.com/
- https://triton-lang.org/main/index.html
- https://github.com/flagos-ai/FlagTree
