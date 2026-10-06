---
type: project
name: LoopSpec
linked_people: []
linked_concepts:
  - "concept/inference/decoding/Self-Speculative Decoding"
  - "concept/inference/decoding/Speculative Decoding"
layer: optimization
status: active
repository: https://github.com/kaist-flexml-lab/loopspec
docs: https://github.com/kaist-flexml-lab/loopspec
areas:
  - "self-speculative-decoding"
  - "recurrent-language-model"
  - "looped-transformer"
  - "pipelined-decoding"
  - "lossless-decoding"
  - "serving"
hardware:
  - "nvidia"
integrations:
  - "SGLang"
last_verified: "2026-10"
linked_companies: []
code_availability: public
---
# LoopSpec
## 项目定位

LoopSpec 是面向 looped/recurrent Transformer 的 pipelined self-speculative decoding 实现。它直接利用模型在中间 recurrent step 的预测作为 draft，不需要额外 draft model 或重新训练 checkpoint。

## 核心机制

对于 Ouro / Raven 这类反复执行共享 Transformer core 的模型，LoopSpec 在验证较早 token 的同时，从中间 depth 提前 draft 后续 token，把 recurrent step 之间的空闲并行性转化为 decode speedup。

该机制属于 [[concept/inference/decoding/Self-Speculative Decoding|Self-Speculative Decoding]]。官方同时声明支持 greedy 与 sampling，并以保持 target model behavior 为目标。

## Serving 路径

仓库内含基于 [[community/sgl-project/SGLang/SGLang|SGLang]] 的 inference server、streaming demo 与 benchmark runner。当前环境要求 Linux x86-64 + NVIDIA GPU。

## 与 vllm-rlt 的互补关系

[[community/ThinkFlowLab/vllm-rlt/vllm-rlt|vllm-rlt]] 主要从 scheduler/KV/P-D 层适配 recurrent model；LoopSpec 从 decoding algorithm 层挖掘 recurrent step 的自推测并行性。二者对应“系统调度”与“解码算法”两条优化轴。

## Sources

- https://github.com/kaist-flexml-lab/loopspec

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/decoding/Self-Speculative Decoding|Self-Speculative Decoding]]
- [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]]

<!-- END AUTO PROJECT CONCEPTS -->
