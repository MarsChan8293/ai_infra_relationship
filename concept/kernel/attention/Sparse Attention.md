---
type: concept
name: Sparse Attention
aliases:
  - Sparse Attention Kernel
  - 稀疏注意力
domain: kernel
topic: attention
parent_concepts:
  - Attention Kernel
related_concepts:
  - KV Cache
projects:
  - FlashMLA
  - TileLang-Ascend
  - "TIRx Kernels"
last_verified: 2026-10
---
# Sparse Attention

## 一句话定义
Sparse Attention 只让每个 query 访问完整 KV 集合中的一个子集，从而把 attention 的计算量与内存访问从“全部历史 token”压缩到 selector / indexer 选中的 token 或 block。

## 核心路径
典型执行先由 indexer / selector 产生 top-k token 或 block indices，再由 sparse attention kernel gather 对应 KV、计算 score / softmax / value aggregation。selector 本身快并不等于最终 attention 快，真正收益取决于 index 生成、gather、KV layout、kernel tiling 与稀疏度共同作用。

## DeepSeek 路径
[[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]] 在 2026-09-30 开源 Ascend 950 的 DeepSeek Sparse Attention prefill/decode kernels，并给出典型 DeepSeek V4.1 工况的 410 / 360 TFLOPS。[[community/deepseek-ai/DeepSeek-Infra/DeepSelect|DeepSelect]] 位于前级 TopK / Lightning Indexer 选择路径，两者是上下游而不是同一个 kernel。[[community/tile-ai/TileLang/TileLang-Ascend|TileLang-Ascend]] 在 A2/A3 adapter 中公开 Sparse Flash Attention、Lightning Indexer 与 TopK Selector，为同类稀疏注意力热路径提供 DSL/compiler 实现。

## Sources
- https://github.com/deepseek-ai/FlashMLA
- https://github.com/deepseek-ai/DeepSelect
