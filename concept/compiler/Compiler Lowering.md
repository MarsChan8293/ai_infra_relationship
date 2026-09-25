---
type: concept
name: Compiler Lowering
aliases:
  - IR Lowering
  - Kernel Lowering
  - 编译降级
  - IR降级
domain: compiler
topic: kernel-compilation
parent_concepts:
  - Kernel Compiler Pipeline
related_concepts:
  - Backend Code Generation
  - Layout Optimization
projects:
  - NineToothed
  - TileLang
  - Triton
  - FlagTree
last_verified: 2026-09
---

# Compiler Lowering

## 一句话定义

Compiler Lowering 是把高层、语义丰富的 IR 逐步转换成更接近硬件执行模型的低层 IR，同时显式化 memory、thread、layout 和 instruction 细节。

## 解决的问题

上层 DSL 可能只写“做一个 GEMM”或“copy 一个 tile”，但硬件真正需要的是：

- 哪个 thread/warp/CTA 处理哪部分数据；
- 数据放 global/shared/register/TMEM 的哪一层；
- 如何同步与 pipeline；
- 用哪条 MMA / copy / vector instruction；
- 最终生成什么 target code。

Lowering 就是把这些隐含决策逐步变成可执行细节。

## 为什么不是一次性翻译

如果一步直接从 DSL 生成 PTX/ISA，编译器很难在中间进行 layout inference、fusion、canonicalization、target-independent optimization。分阶段 lowering 保留了在合适抽象层做优化的机会。

## 与 Code Generation 的区别

[[Backend Code Generation]] 更接近最终目标代码输出；Lowering 是更广的转换过程，可以发生多次，例如：

`Tile IR → loop/memory IR → GPU IR → LLVM/PTX`

## 项目实现

[[community/InfiniTensor/NineToothed|NineToothed]] 的 2026 pipeline 已转向 SSA + lowering/pass 结构；[[community/tile-ai/TileLang/TileLang|TileLang]] 对 tile operator 执行 layout inference 和 lowering，例如把 Blackwell GEMM tile-op lower 到具体 TCGEN5 MMA 调用；[[community/triton-lang/Triton/Triton|Triton]] 使用多级 MLIR dialect lowering；[[community/flagos-ai/FlagTree/FlagTree|FlagTree]] 在 Triton compiler 路线上做多 backend lowering/codegen。

## Sources

- https://github.com/InfiniTensor/ninetoothed
- https://tilelang.com/autoapi/tilelang/cuda/op/gemm/gemm_tcgen05/
- https://triton-lang.org/main/dialects/dialects.html
- https://github.com/flagos-ai/FlagTree
