---
type: project
name: OmniKVQuant
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
