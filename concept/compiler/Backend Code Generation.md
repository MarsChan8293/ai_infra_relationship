---
type: concept
name: Backend Code Generation
aliases:
  - Target Code Generation
  - Codegen
  - Backend Codegen
  - 后端代码生成
domain: compiler
topic: kernel-compilation
parent_concepts:
  - Kernel Compiler Pipeline
related_concepts:
  - Compiler Lowering
  - Kernel DSL
projects:
  - NineToothed
  - TileLang
  - Triton
  - FlagTree
last_verified: 2026-09
---

# Backend Code Generation

## 一句话定义

Backend Code Generation 把已经 lower 到目标相关表示的 kernel 程序转换为 CUDA/HIP/vendor source、PTX/ISA、object 或可加载 binary。

## 解决的问题

同一上层算子想运行在 NVIDIA、AMD、Ascend、Cambricon 等不同设备时，最终 instruction set、runtime ABI、memory model 和 compiler toolchain 都不同。backend codegen 是“统一上层表达”落到具体硬件的最后桥梁。

## 核心职责

一个 backend 通常需要处理：

- target architecture 与 capability；
- instruction / intrinsic selection；
- address space 和 memory scope；
- thread/block launch metadata；
- host stub / launcher；
- binary compile、link 与 load；
- runtime ABI。

## 与 Hardware Abstraction 的关系

多 backend compiler 的价值不是让所有硬件“长得一样”，而是在共享 IR/pass 的同时允许 backend 保留硬件特化。否则 portability 很容易以牺牲性能为代价。

## 项目实现

[[community/InfiniTensor/NineToothed|NineToothed]] 提供 Triton、CUDA、TileLang 与 vendor backend registry；[[community/tile-ai/TileLang/TileLang|TileLang]] 明确拆分 device_codegen、host_codegen 与 execution backend；[[community/triton-lang/Triton/Triton|Triton]] 将 MLIR pipeline 输出为 NVIDIA/AMD 等 GPU target code；[[community/flagos-ai/FlagTree/FlagTree|FlagTree]] 的核心定位就是把 Triton 风格上层程序扩展到多种国产/异构 AI 芯片 backend。

## Sources

- https://github.com/InfiniTensor/ninetoothed
- https://tilelang.com/autoapi/
- https://triton-lang.org/main/index.html
- https://github.com/flagos-ai/FlagTree
