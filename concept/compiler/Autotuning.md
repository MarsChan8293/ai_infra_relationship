---
type: concept
name: Autotuning
aliases:
  - Auto-Tuning
  - Kernel Autotuning
  - Auto Tuning
  - 自动调优
domain: compiler
topic: kernel-optimization
related_concepts:
  - Kernel Compiler Pipeline
  - JIT Kernel Compilation
  - Layout Optimization
projects:
  - Triton
  - TileLang
  - NineToothed
last_verified: 2026-09
---

# Autotuning

## 一句话定义

Autotuning 自动搜索 block size、warp/thread 数、pipeline stage、tile shape 等 kernel 配置，并通过编译 + benchmark 选择在特定 shape / hardware 上表现最好的实现。

## 解决的问题

GPU kernel 的性能空间往往高度非线性。同一个 GEMM/attention，在不同 M/N/K、head dimension、GPU generation 下的最佳 tile、warp 和 stage 配置可能完全不同，手工为所有组合调参既昂贵又容易过时。

## 核心机制

典型 autotuner 包含：

1. 定义候选 configuration space。
2. 对每个候选生成/编译 kernel。
3. 校验正确性。
4. warmup + benchmark。
5. 选择最低延迟或最高吞吐配置。
6. 根据 shape/device/key 缓存最佳结果。

系统还可以利用 performance model 或 early pruning 减少实际 benchmark 数量。

## 与 JIT 的关系

[[JIT Kernel Compilation]] 负责“按当前配置编译”；Autotuning 负责“在多个配置中找哪个好”。二者经常一起使用，但 JIT 并不自动等于 autotuning。

## 项目实现

[[community/triton-lang/Triton/Triton|Triton]] 提供 `triton.autotune`，按 key 变化评估候选 `triton.Config`；[[community/tile-ai/TileLang/TileLang|TileLang]] 内置 autotuner，可并行编译、校验、benchmark 并缓存最佳 artifact；[[community/InfiniTensor/NineToothed|NineToothed]] 的 2026 compiler pipeline 已明确包含 architecture-aware caching / AOT / autotuning 路径。

## Sources

- https://triton-lang.org/main/python-api/generated/triton.autotune.html
- https://tilelang.com/programming_guides/autotuning.html
- https://github.com/InfiniTensor/ninetoothed
