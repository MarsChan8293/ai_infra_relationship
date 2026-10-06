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
  - "Kernel DSL"
  - "Compiler Lowering"
  - "JIT Kernel Compilation"
  - "Autotuning"
  - "Layout Optimization"
projects:
  - "NineToothed"
  - "TileLang"
  - "TileLang-Ascend"
  - "TileLang-MLIR-Ascend"
  - "Triton"
  - "FlagTree"
  - "CAKE"
  - "Event Tensor"
  - "Mirage Persistent Kernel"
  - "CANNBot-DSL"
last_verified: 2026-10
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
5. **Backend code generation**：生成 CUDA/HIP、PTX/ISA、Ascend/vendor code、host launcher 或其他 target artifact。
6. **Materialization**：可以运行时 [[JIT Kernel Compilation]]，也可以在构建/部署阶段 AOT 生成 cubin/hsaco/object/shared library。

Backend codegen 与 AOT/JIT 都是 compiler pipeline 的阶段/执行模式，本仓库不再把“codegen”或“AOT”作为单独 canonical concept。

## 为什么要分层

过早降低到低层 IR 会丢失高层语义，过晚暴露硬件细节又难以做到极致优化。多级 IR 的价值就是在“可分析性”和“硬件可控性”之间逐层过渡。

## 项目实现

[[community/InfiniTensor/NineToothed|NineToothed]] 已公开 SSA compiler pipeline、pass/backend registry、AOT 与 architecture-aware artifact caching；[[community/tile-ai/TileLang/TileLang|TileLang]] 具有 frontend、layout inference、pass pipeline 和 device/host codegen；[[community/tile-ai/TileLang/TileLang-Ascend|TileLang-Ascend]] 与 [[community/tile-ai/TileLang/TileLang-MLIR-Ascend|TileLang-MLIR-Ascend]] 把同类 pipeline lower/codegen 到 AscendC/PTO/NPU IR 与 MLIR/AscendNPU IR；[[community/triton-lang/Triton/Triton|Triton]] 通过 Triton/MLIR dialect 逐层 lower 到 GPU code；[[community/flagos-ai/FlagTree/FlagTree|FlagTree]] 扩展多后端 code generation。

[[community/research/CAKE/CAKE|CAKE]] 展示 Agent-facing compiler pipeline；[[university/Carnegie Mellon University/Catalyst Group/Mirage Persistent Kernel|Mirage Persistent Kernel]] 与 [[university/Carnegie Mellon University/Catalyst Group/Event Tensor|Event Tensor]] 展示 dynamic/persistent kernel lowering；[[community/Ascend/CANNBot-DSL/CANNBot-DSL|CANNBot-DSL]] 在 Ascend 侧公开 compiler backend、AOT 与 Native package materialization。

## Sources

- https://github.com/InfiniTensor/ninetoothed
- https://tilelang.com/
- https://triton-lang.org/main/index.html
- https://github.com/flagos-ai/FlagTree
- https://arxiv.org/abs/2608.12629
- https://github.com/mirage-project/mirage
- https://arxiv.org/abs/2604.13327
- https://gitcode.com/cann/cannbot-dsl
