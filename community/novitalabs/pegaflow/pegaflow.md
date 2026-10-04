---
type: project
name: PegaFlow
status: active
repository: https://github.com/novitalabs/pegaflow
docs: https://github.com/novitalabs/pegaflow/tree/master/docs
last_verified: "2026-10"
companies: ["Novita AI"]
company_relation: company-led
layer: data-plane
areas: [kv-cache, kv-offloading, tiered-cache, rdma, ssd-cache, host-memory, p-d-disaggregation, observability]
hardware: [nvidia]
integrations: [vLLM, SGLang, NIXL]
linked_companies:
  - "company/Novita AI/Novita AI"
linked_concepts:
  - "concept/inference/kv-cache/KV Cache"
  - "concept/inference/kv-cache/KV Cache Offloading"
  - "concept/inference/kv-cache/Tiered KV Cache"
  - "concept/storage/SSD-Backed KV Cache"
  - "concept/memory/Host Memory"
  - "concept/memory/NUMA"
  - "concept/communication/data-movement/RDMA"
  - "concept/communication/data-movement/GPUDirect RDMA"
  - "concept/inference/serving/P-D Disaggregation"
---
# PegaFlow

PegaFlow 是 Novita AI 开源的高性能 external KV cache storage engine。它把 KV cache 生命周期从推理引擎进程中解耦出来，由独立 Rust service 管理 pinned host memory、SSD cache、RDMA 资源、索引与后台任务。

## 架构定位

PegaFlow 不替代 [[community/vllm-project/vLLM/vLLM|vLLM]] / [[community/sgl-project/SGLang/SGLang|SGLang]] 的 scheduler 和 model execution，而是位于它们旁边的数据平面：

GPU KV ↔ pinned host memory ↔ SSD / remote RDMA memory

它通过 vLLM external KV connector 接口接入，因此 engine crash、滚动升级或模型切换时，host-side KV pool 可以继续存活。

## 关键能力

- GPU KV cache offload 到 host memory 或 SSD。
- 多 inference instance 共享同一 host KV pool。
- 通过 RDMA 跨节点共享 KV。
- NUMA-aware pinned memory 与 layer-wise DMA。
- Rust / Tokio 数据路径，减少 Python GIL 与 GC 对尾延迟的影响。
- Prometheus / OTLP 可观测性。
- P/D deployment、NIXL 与 MultiConnector 相关部署文档。

## 与其他 KV 系统的关系

它和 [[community/LMCache/LMCache/LMCache|LMCache]]、[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 属于相邻的 external / distributed KV cache 基础设施赛道，但 PegaFlow 当前公开设计尤其强调“独立进程持有 KV 生命周期”和 host/SSD/RDMA 三层缓存。

## 公开性能线索

vLLM 与 Novita AI 2026-05-18 的联合文章报告：在固定 500 GiB host KV 预算下，多实例共享测试相对进程内隔离缓存提升吞吐；DeepSeek-V3.2 MLA TP8 场景通过 logical KV deduplication 提升有效缓存容量；内部 RDMA 集群还报告了大块 remote KV read 的高带宽结果。应把这些数值视作对应测试环境下的 production-oriented measurement，而非跨硬件的固定保证。

## Sources

- https://github.com/novitalabs/pegaflow
- https://vllm.ai/blog/2026-05-18-pegaflow
