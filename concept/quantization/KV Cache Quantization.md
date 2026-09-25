---
type: concept
name: KV Cache Quantization
aliases:
  - Quantized KV Cache
  - KV Quantization
  - KV缓存量化
domain: quantization
topic: kv-cache
parent_concepts:
  - Quantization
related_concepts:
  - KV Cache
  - KV Cache Management
  - FP8 Quantization
projects:
  - vLLM
  - LMDeploy
last_verified: 2026-09
---

# KV Cache Quantization

## 一句话定义

KV Cache Quantization 把 attention 的 K/V 历史状态从 FP16/BF16 压到 FP8 或更低精度，直接降低每个 token 占用的 KV 内存和 KV 读带宽。

## 解决的问题

长上下文和高并发下，[[KV Cache]] 往往比权重更快成为容量瓶颈。与权重量化不同，KV 会随着请求长度动态增长，因此降低 KV 每 token 字节数可以近似线性增加可容纳 token 数。

## 核心机制

写入 KV 时把 K/V 按 scale 量化存储；attention kernel 读取时进行 dequant，或在支持的 backend 中直接用低精度 Q/K/V 计算。常见 scale 粒度包括：

- per-tensor。
- per-head / per-KV-head。
- per-block / per-token。

scale 可以固定为默认值，也可以通过 calibration 得到。

## 与模型量化的区别

Weight quantization 减少固定模型参数体积；KV quantization 减少随上下文和并发增长的动态状态。两者可以独立启用，也可以组合。

## 与 KV Offloading 的关系

[[KV Cache Offloading]] 通过把 KV 移到 CPU/SSD/remote tier 扩容量；KV Quantization 通过减少每个 KV block 的字节数扩容量。两者可以叠加，但量化还会改变 attention kernel 的 dtype 和精度行为。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 支持 FP8 KV Cache，包括 per-tensor、per-attention-head scale 和 layer skip 等路径；[[community/InternLM/LMDeploy/LMDeploy|LMDeploy]] 也提供 KV quantization / compressed cache 相关推理路径。

## Sources

- https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/
- https://github.com/InternLM/lmdeploy
