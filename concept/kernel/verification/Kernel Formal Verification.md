---
type: concept
name: Kernel Formal Verification
aliases:
  - Formal Kernel Verification
  - Verified GPU Kernels
  - GPU Kernel Proof
  - 算子形式化验证
domain: kernel
topic: verification
related_concepts:
  - Kernel DSL
  - Agentic Kernel Optimization
projects:
  - "VeriTile"
last_verified: 2026-10
---

# Kernel Formal Verification

## 一句话定义

Kernel Formal Verification 使用形式化语义、数学规格与机器可检查证明来验证 kernel 的功能正确性或 refinement，而不是只依赖有限输入上的数值测试。

## 在 AI Kernel Agent 中的价值

Agent 自动生成或改写 CUDA / Triton / DSL kernel 时，benchmark 只能证明有限 workload 上的表现。形式化验证可以把 correctness gate 提升为可证明的语义约束，尤其适合验证融合、重写、数值算法等价性和 memory write footprint。

## 当前边界

形式化模型通常不会自动覆盖真实 GPU 的全部 IEEE-754、PTX、TMA、异步 copy、并发或硬件 memory model，因此必须明确“证明覆盖什么”和“仍由外部测试覆盖什么”。

## 项目实现

[[community/Lizn-zn/VeriTile/VeriTile|VeriTile]] 在 Lean 4 中嵌入 typed Triton-style DSL，提供 kernel-vs-spec correctness 与 kernel-vs-kernel refinement theorem surface，并公开记录浮点、PTX/TMA 与部分并发语义的边界。

## Sources

- https://github.com/Lizn-zn/VeriTile
