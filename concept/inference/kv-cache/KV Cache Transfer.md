---
type: concept
name: KV Cache Transfer
aliases:
  - KV Transfer
  - KV缓存传输
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - KV Cache Offloading
  - KV Cache Sharing
  - P-D Disaggregation
projects:
  - vLLM
  - LMCache
  - Mooncake
last_verified: 2026-09
---

# KV Cache Transfer

## 一句话定义

KV Cache Transfer 是在设备、worker、serving instance 或存储层之间移动已经计算好的 KV 状态，使另一位置可以直接继续使用它。

## 解决的问题

只要 KV 的生产者和消费者不是同一个本地 KV 空间，就需要 transfer。典型场景包括 [[P-D Disaggregation]]、P2P cache sharing、GPU ↔ CPU offload，以及从远端 KV store 恢复缓存。

## 核心机制

数据面一般包含 KV block 定位、源/目标内存注册、传输描述符、异步 copy/read/write 和完成通知。高性能实现会利用 NVLink、RDMA、GPUDirect 或专用 transfer library，并尽量让 KV 搬运和 GPU forward 重叠。

## 与相邻概念的区别

- [[KV Cache Offloading]] 关注把 KV 放到较慢/更便宜的层，transfer 是实现动作。
- [[KV Cache Sharing]] 关注多个实例是否能复用同一份已计算 KV，通常需要 transfer 或共享 store。
- [[P-D Disaggregation]] 规定 prefill 生产 KV、decode 消费 KV，因此 KV transfer 是关键数据通路。

## 代价与适用边界

KV 很大时，网络或 PCIe 带宽会直接影响 TTFT。传输前还需要保证模型、KV layout、block size、dtype 等消费者可解释的状态兼容。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 提供 KV Connector 抽象和 NIXL/Mooncake/LMCache 等 connector。[[community/LMCache/LMCache/LMCache|LMCache]] 可通过 NIXL 在 NVLink、RDMA 或 TCP 上传输 KV。[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] Transfer Engine 提供跨 DRAM/VRAM/NVMe-oF 的高性能数据传输能力。

## Sources

- https://docs.vllm.ai/en/latest/features/disagg_prefill/
- https://docs.lmcache.ai/getting_started/quickstart/disaggregated_prefill.html
- https://kvcache-ai.github.io/Mooncake/design/transfer-engine/
