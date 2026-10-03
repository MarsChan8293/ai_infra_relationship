---
type: project
name: OmniKVQuant
linked_people: []
linked_concepts:
  - "concept/quantization/KV Cache Quantization"
layer: optimization
status: active
repository: https://github.com/kaistmm/OmniKVQuant
docs: https://github.com/kaistmm/OmniKVQuant
areas:
  - "kv-cache-quantization"
  - "omni-llm"
  - "2bit-kv-cache"
  - "training-free"
  - "triton-kernel"
  - "multimodal-inference"
hardware:
  - "nvidia"
last_verified: "2026-10"
linked_companies: []
---
# OmniKVQuant
## 项目定位

OmniKVQuant 是面向 Omni-LLM 的 training-free KV cache quantization 方法官方实现。当前 release 提供 calibrated value rotation、packed 2-bit KV cache、fused Triton decode kernel 和 TurboQuant baseline。

## 技术意义

普通 [[concept/quantization/KV Cache Quantization|KV Cache Quantization]] 多从 text LLM 的 attention/KV dtype 出发；OmniKVQuant 面向包含视频/音频等长多模态 context 的 Omni-LLM，目标是在极低位宽下减小动态 KV state，同时保持下游 WorldSense 等任务能力。

仓库实现直接以 Qwen2.5-Omni 为实验对象，并复用/参考 vLLM TurboQuant primitives，但当前不是一个独立 serving engine。

## 当前边界

公开代码的主验证路径使用 NVIDIA CUDA / PyTorch / FlashAttention/Triton。项目的 2-bit cache 与 calibration checkpoint 是特定模型/实验设置，不应泛化为“任意 Omni model 直接 2-bit 无损”。

## 论文作者

README citation 列出 Suho Yoo、Hyunjong Ok、Jongmin Choi、Jihoo Jung、Joon Son Chung。这里只记录论文/实现作者，不自动推断 maintainer 或当前雇佣关系。

## Sources

- https://github.com/kaistmm/OmniKVQuant
- https://arxiv.org/abs/2609.11582

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/quantization/KV Cache Quantization|KV Cache Quantization]]

<!-- END AUTO PROJECT CONCEPTS -->
