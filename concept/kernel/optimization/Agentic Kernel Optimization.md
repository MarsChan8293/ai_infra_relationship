---
type: concept
name: Agentic Kernel Optimization
aliases:
  - Kernel Optimization Agent
  - Autonomous Kernel Optimization
  - Agentic Kernel Tuning
  - 智能体算子优化
domain: kernel
topic: optimization
related_concepts:
  - Agentic Inference Optimization
  - Autotuning
  - Kernel Fusion
  - Kernel Compiler Pipeline
  - Backend Code Generation
projects:
  - "KDA"
  - "MetaInfer"
  - "Croqtile"
  - "GEAK"
  - "Hyperloom"
  - "KernelAgent"
  - "KernelEvolve"
  - "Atrex Kernel Agent"
  - "KernelBlaster"
  - "CUDA-Agent"
  - "K-Search"
  - "AdaExplore"
  - "Astra"
  - "CUDAMaster"
  - "CANNBot"
  - "Ascend Agent Skills"
  - "AKG Agents"
  - "AscendOptimizer"
  - "AgenticCANN"
  - "AscendCraft"
  - "Compiler-Grounded Hierarchical Diagnosis"
  - "AVO"
  - "TileGym"
last_verified: 2026-10
---

# Agentic Kernel Optimization

## 一句话定义

Agentic Kernel Optimization 让 AI agent 围绕一个可测量的 kernel 任务持续执行代码生成或修改、编译、正确性验证、profiling、benchmark 与迭代搜索，并由外部 Harness 根据真实硬件测量决定候选是否保留。

## 核心闭环

```text
Kernel Task / Reference
        ↓
Generate / Modify
        ↓
Compile
        ↓
Correctness
        ↓
Profile / Benchmark
        ↓
Diagnose Bottleneck
        ↓
Generate Next Candidate
        ↓
Keep / Revert / Explore
        ↓
Optimization Memory
```

一个完整任务通常需要显式定义：

- objective；
- constraints；
- representative shapes / workloads；
- baseline implementation；
- correctness command / tolerance；
- benchmark command；
- promotion criteria；
- editable / forbidden files；
- iteration / time / hardware budget。

## 搜索空间

Agent 可以优化的对象不只包括源码文本，还包括：

- tiling / block / warp / pipeline 参数；
- data movement 与 memory hierarchy；
- register / shared memory / UB / L1 / L0 等资源使用；
- vector / tensor core / cube unit 映射；
- fusion；
- launch / host runtime overhead；
- compiler / IR transformation；
- CUDA / Triton / CuTe / Tile DSL；
- AscendC / Triton-Ascend 等 NPU kernel 实现。

## Profiler 与 Compiler 反馈

高质量 Kernel Agent 不应只依赖自然语言推理。它应把 profiler 与 compiler 变成结构化 observation：

```text
Source
  ↓
Compiler / IR
  ↓
Runtime profile
  ↓
Hardware counters
  ↓
Bottleneck state
  ↓
Agent action
```

NVIDIA 路径通常可使用 NCU / NSYS、PTX / SASS / Triton IR 等信息；Ascend 路径则需要同时考虑 host-side tiling、AscendC pipeline、片上存储和 CANN / profiler / compiler 反馈。

## 与传统 Kernel Library 的区别

CUTLASS、FlashInfer、DeepGEMM 等主要提供高性能实现；Agentic Kernel Optimization 提供的是“如何自动发现下一版实现”的搜索与验证控制环。Kernel library 可以作为 baseline、reference、知识源和候选实现来源，但不等于 Agent Harness。

## 与 Autotuning 的区别

[[Autotuning]] 通常搜索一个人为预定义的参数空间；Agentic Kernel Optimization 可以修改算法、代码结构、数据路径、融合方式乃至实现语言。实践中二者往往组合使用：Agent 决定搜索方向，Autotuner 在局部连续/离散参数空间内高效扫点。

## 项目实现

[[community/NVIDIA/KDA/KDA|KDA]] 把 CUDA kernel performance engineering 组织成可重复的 agent workflow，强调 objective、constraints、validation command、promotion criteria、profiling evidence 和候选保存。

[[community/MetaInfer/MetaInfer|MetaInfer]] 提供 AI-assisted kernel optimization 的 optimize → benchmark 循环，并把 kernel 优化与 inference framework generation 放在同一个 AI Infra toolbox 中。

[[community/LancerLab/Croqtile/Croqtile|Croqtile]] 是面向 AI agent 的 kernel DSL / compiler，其结构化编译器诊断和 croqtile-tuner 把 autotuning harness 直接纳入 agent-native kernel programming workflow。

## 设计原则

- correctness gate 必须早于性能比较；
- benchmark 应固定 workload、环境和硬件；
- 保留 best-so-far，同时允许 branch / tree exploration；
- 保存失败原因，而不只保存成功候选；
- microbenchmark 提升不能替代 E2E inference validation；
- backend-specific optimization knowledge 与通用 orchestration 分层。

## Sources

- https://github.com/NVlabs/kda
- https://nvlabs.github.io/kda/
- https://github.com/MetaInfer/MetaInfer
- https://github.com/LancerLab/croqtile
