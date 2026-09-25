---
type: concept
name: Layout Optimization
aliases:
  - Data Layout Optimization
  - Memory Layout Optimization
  - Tensor Layout Optimization
  - 布局优化
domain: compiler
topic: kernel-optimization
related_concepts:
  - Compiler Lowering
  - Autotuning
  - Kernel DSL
  - Data Movement
projects:
  - TileLang
  - CUTLASS
  - NineToothed
last_verified: 2026-09
---

# Layout Optimization

## 一句话定义

Layout Optimization 决定逻辑 tensor / thread 坐标如何映射到物理 memory offset、register fragment 和执行线程，使数据访问尽量连续、避免 bank conflict，并匹配 tensor-core / copy instruction。

## 解决的问题

同一份数学 tensor 可以有很多物理布局。错误布局可能导致：

- global memory 不合并访问；
- shared-memory bank conflict；
- 多余 transpose / copy；
- tensor-core operand 不匹配；
- thread 间数据交换开销增大。

因此 layout 往往和 tile size 一样，是 kernel 性能的一等公民。

## 核心机制

编译器/DSL 可以显式或自动决定：

- row/column-major、swizzle；
- thread → data mapping；
- shared-memory / TMEM layout；
- fragment layout；
- vectorization / contiguous dimension；
- producer/consumer stage 之间的 layout conversion。

## 与 Layout Inference 的关系

一些系统允许开发者手写 layout；另一些会根据 operator semantics 和 target 自动推导。[[community/tile-ai/TileLang/TileLang|TileLang]] 把 Layout Inference 作为核心优化技术之一，可根据 tile-op 自动推导 buffer shape 和最佳布局。

## 项目实现

[[community/tile-ai/TileLang/TileLang|TileLang]] 提供显式 Layout/Fragment abstraction 和 compiler layout inference；[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]] / CuTe 用 `Layout<Shape, Stride>` 与 layout algebra 表达 thread/data mapping，并把 layout 作为主要性能调优点；[[community/InfiniTensor/NineToothed|NineToothed]] 的 Triton/layout compiler 路线持续处理 layout/reduction/runtime optimization。

## Sources

- https://tilelang.com/tools/layout_visualization.html
- https://tilelang.com/deeplearning_operators/deepseek_mla.html
- https://docs.nvidia.com/cutlass/latest/media/docs/cpp/cutlass_3x_design.html
- https://github.com/InfiniTensor/ninetoothed
