---
type: concept
name: JIT Kernel Compilation
aliases:
  - JIT Compilation
  - Runtime Kernel Compilation
  - Just-in-Time Kernel Compilation
  - Kernel JIT
  - 算子即时编译
domain: compiler
topic: kernel-programming
related_concepts:
  - Kernel DSL
  - Kernel Fusion
  - GEMM
projects:
  - DeepJIT
  - DeepGEMM
  - Triton
  - TileLang
  - CUTLASS
  - FlashInfer
last_verified: 2026-09
---

# JIT Kernel Compilation

## 一句话定义

JIT Kernel Compilation 在运行前或运行时根据实际硬件、shape、dtype 和配置生成并编译专用 kernel，而不是只依赖安装阶段预编译的一组固定 binary。

## 解决的问题

LLM kernel 的有效配置空间很大：GPU architecture、M/N/K、head dimension、quantization format、MoE group size 和 fused epilogue 都可能改变最优实现。预编译所有组合会让 binary 膨胀，也难以及时支持新硬件和新 shape。

## 核心机制

典型 JIT 流程是：

1. 根据输入 shape / dtype / device 构造 specialization key。
2. 生成 DSL / CUDA / IR kernel。
3. 调用 compiler toolchain 编译为 device code。
4. 缓存 artifact。
5. 后续相同 key 直接命中 cache，避免重复编译。

系统还可以在候选配置间 autotune，再把最佳配置与 compiled artifact 一起缓存。

## 收益与代价

JIT 可以获得更强的 shape/hardware specialization，并缩短新 kernel 的交付路径；代价是首次请求会付编译延迟，cache key、并发编译、binary cache、容器只读文件系统和 compiler 依赖都需要工程治理。

## 与 Kernel DSL 的关系

[[Kernel DSL]] 定义“如何表达 kernel”；JIT 定义“何时、针对什么配置把 kernel 编译出来”。Triton、TileLang、CuTe DSL 等经常把二者结合，但二者不是同义词。

## 项目实现

[[community/deepseek-ai/DeepSeek-Infra/DeepJIT|DeepJIT]] 是独立 xPU kernel JIT/runtime 层；[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 当前所有 kernel 通过 DeepJIT 在运行时编译；[[community/triton-lang/Triton/Triton|Triton]] 以 JIT specialization 作为核心执行模式；[[community/tile-ai/TileLang/TileLang|TileLang]] 提供 `tilelang.jit`；[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]] Python DSL 支持 JIT kernel compilation；[[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] 也提供 JIT/custom kernel 生成能力。

## Sources

- https://github.com/deepseek-ai/DeepJIT
- https://github.com/deepseek-ai/DeepGEMM
- https://triton-lang.org/main/index.html
- https://tilelang.com/autoapi/tilelang/jit/index.html
- https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/overview.html
- https://docs.flashinfer.ai/
