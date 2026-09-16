---
type: project
name: mini-SGLang
organization: sgl-project
linked_people: []
repository: https://github.com/sgl-project/mini-sglang
open_source: true
layer: llm-serving-runtime
areas: [llm-serving, radix-cache, chunked-prefill, overlap-scheduling, tensor-parallelism, flashinfer, cuda-kernels]
last_verified: "2026-09"
linked_companies: []
---
# mini-SGLang

## 项目定位

mini-SGLang 是 sgl-project 下的紧凑型高性能 LLM inference framework，目标是在较小、可读的代码规模内复现现代 serving engine 的关键机制，并作为 SGLang 的透明参考实现。

核心机制包括：
- Radix Cache；
- Chunked Prefill；
- Overlap Scheduling；
- Tensor Parallelism；
- FlashAttention / FlashInfer kernel integration。

## Xiaoze Fan

[[university/上海交通大学/Xiaoze Fan|Xiaoze Fan（范晓泽）]] 的个人主页 / GitHub 将 mini-SGLang 列为其主要项目之一，并描述为从头构建的 lightweight SGLang implementation。

因此这里把 Xiaoze Fan 作为 mini-SGLang 的核心人物节点；不因为仓库后来进入 `sgl-project` 组织就自动推断其与所有 SGLang maintainer 的人际强关系。

## 与 FreeToken 的关系

[[community/FlashML-org/FreeToken/FreeToken|FreeToken]] 官方 README 明确写明项目 **deeply inspired by mini-SGLang**，并学习 / 复用了 SGLang、vLLM、FlashInfer 等项目设计与代码。

结合 Xiaoze Fan 同时是 FreeToken 论文共同一作，形成非常清晰的传播链：

`SGLang → mini-SGLang → Xiaoze Fan → FreeToken`

这是一条有第一方项目说明 + 人物身份双重证据的 project-to-project / person bridge。

## Sources
- https://github.com/sgl-project/mini-sglang
- https://jasonfxz.top/
- https://github.com/jason-fxz
- https://github.com/FlashML-org/FreeToken
