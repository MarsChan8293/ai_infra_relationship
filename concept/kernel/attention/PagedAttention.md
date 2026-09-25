---
type: concept
name: PagedAttention
aliases:
  - Paged Attention
  - 分页注意力
domain: kernel
topic: attention
parent_concepts:
  - Attention Kernel
related_concepts:
  - KV Cache
  - KV Cache Management
projects:
  - vLLM
  - FlashInfer
last_verified: 2026-09
---

# PagedAttention

## 一句话定义

PagedAttention 是让 attention kernel 直接通过 block table 访问分页/分块 KV cache 的 serving 机制，使一个请求的逻辑连续 KV 不必在物理显存中连续存放。

## 解决的问题

在线 serving 中请求长度动态变化，若每个请求都预留一块连续 KV buffer，会产生内部碎片、扩容困难和低利用率。把 KV 切成固定-size blocks 后，物理 block 可以按需分配，但 attention kernel 必须能够根据 page/block table 找到真实 K/V。

## 核心机制

请求维护逻辑 token block → physical KV block 的映射。执行 attention 时，kernel 根据 block table、context length、last page length 等 metadata 遍历实际 KV pages，完成 QK 和 value 聚合。

这把“KV 内存管理”与“attention 计算”连接起来：[[KV Cache Management]] 管理 blocks，PagedAttention 消费这些 blocks。

## 与 FlashAttention 的区别

- [[FlashAttention]]：重点是减少 attention 中间结果的 HBM IO。
- PagedAttention：重点是让 attention 支持非连续的 paged KV layout。

现代 serving kernel 可以同时具有二者特征，或者由不同 backend 根据 shape/hardware 自动选择。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 从 PagedAttention 起家，当前 V1 仍维护 paged attention / paged KV 相关 kernel；[[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] 提供 BatchDecode/BatchPrefill with Paged KV Cache 等 API，并明确其 paged KV cache 设计来自 vLLM。

## Sources

- https://docs.vllm.ai/en/latest/design/paged_attention/
- https://docs.vllm.ai/en/stable/api/vllm/v1/attention/ops/paged_attn/
- https://docs.flashinfer.ai/api/attention.html
