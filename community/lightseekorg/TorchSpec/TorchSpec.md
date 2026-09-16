---
type: project
name: TorchSpec
linked_people: []
layer: speculative-decoding-training
open_source: true
repository: https://github.com/lightseekorg/TorchSpec
areas: [speculative-decoding, distributed-training, hidden-state-transfer, vllm, sglang, tensorrt-llm]
governance: LightSeek Foundation ecosystem
last_verified: "2026-09"
linked_companies: []
---
# TorchSpec

## 项目简介
TorchSpec 是 torch-native speculative decoding training framework，由 LightSeek Foundation 生态维护。它把 inference 与 draft-model training 完全解耦，让 inference engine 生成的 hidden states 直接流向分布式训练 worker。

## Mooncake 关系
TorchSpec 官方 README 明确使用 [[community/kvcache-ai/Mooncake/Mooncake|Mooncake Store]] 作为 inference ↔ training 的 hidden-state 数据平面，从而避免把大规模 hidden states 先落盘再训练。该路径支持 vLLM，并扩展到 SGLang、TensorRT-LLM 等 inference backend。

因此 TorchSpec 是 Mooncake 从 serving KV cache 扩展到 speculative decoding / post-training pipeline 的关键节点。

## 生态关系
[[community/lightseekorg/LightSeek-Foundation/LightSeek-Foundation|LightSeek Foundation]] · [[TokenSpeed]] · [[vLLM]] · [[SGLang]] · [[TensorRT-LLM]] · [[Mooncake]]。

## Sources
- https://github.com/lightseekorg/TorchSpec
- https://pytorch.org/blog/torchspec-speculative-decoding-training-at-scale/
- https://github.com/kvcache-ai/Mooncake
