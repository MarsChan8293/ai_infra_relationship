---
type: project
name: Splash
linked_people: []
linked_concepts:
  - "concept/inference/serving/Continuous Batching"
  - "concept/inference/kv-cache/KV Cache Offloading"
  - "concept/quantization/KV Cache Quantization"
  - "concept/inference/kv-cache/Prefix Caching"
  - "concept/inference/decoding/Speculative Decoding"
  - "concept/memory/SSD-NVMe Tier"
layer: inference-engine
status: active
repository: https://github.com/incoai/splash
docs: https://inco.ai/blog/splash/
areas:
  - "local-inference"
  - "apple-silicon"
  - "metal-kernels"
  - "speculative-decoding"
  - "continuous-batching"
  - "prefix-caching"
  - "kv-cache-quantization"
  - "ssd-offload"
  - "openai-compatible-api"
  - "anthropic-compatible-api"
hardware:
  - "apple-silicon"
last_verified: "2026-10"
linked_companies: []
---
# Splash
## 项目定位

Splash 是面向 Apple Silicon 的本地 inference engine，围绕少量模型族做 model-specific execution：DFlash 2 speculative decoding、专用 Metal kernel、自动 memory planning、prefix reuse 和 concurrent batching 共同组成 serving path。

## 关键机制

- [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]]：每个支持模型配套训练好的 DFlash2 draft。
- [[concept/inference/serving/Continuous Batching|Continuous Batching]]：并发 request 自动 batch。
- [[concept/inference/kv-cache/Prefix Caching|Prefix Caching]]：跨请求复用 cached prefix。
- 默认 KV 为 8-bit，并可切换 BF16，对应 [[concept/quantization/KV Cache Quantization|KV Cache Quantization]]。
- `--max-cache-disk` 可把 KV cache 与 GDN state 下沉到 SSD，对应 [[concept/inference/kv-cache/KV Cache Offloading|KV Cache Offloading]] 与 [[concept/memory/SSD-NVMe Tier|SSD/NVMe Tier]]。

## 与 TensorFold / llama.cpp 的关系

[[community/ashhart/TensorFold/TensorFold|TensorFold]] 同样强调 Apple Silicon + model-specific kernel / speculative path；llama.cpp 更强调通用 GGUF/local ecosystem。Splash 当前更像为特定现代模型组合做的深度优化 serving engine，而不是任意 HF architecture 的通用 runtime。

## 当前边界

官方 quick start 要求 Apple M3 或更新平台和 macOS 26.4+。README 的性能数字来自特定 M5 Pro / M3 Max workload，不能直接外推到所有 Apple Silicon 或模型。

## Sources

- https://github.com/incoai/splash
- https://inco.ai/blog/splash/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/serving/Continuous Batching|Continuous Batching]]
- [[concept/inference/kv-cache/KV Cache Offloading|KV Cache Offloading]]
- [[concept/quantization/KV Cache Quantization|KV Cache Quantization]]
- [[concept/inference/kv-cache/Prefix Caching|Prefix Caching]]
- [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]]
- [[concept/memory/SSD-NVMe Tier|SSD/NVMe Tier]]

<!-- END AUTO PROJECT CONCEPTS -->
