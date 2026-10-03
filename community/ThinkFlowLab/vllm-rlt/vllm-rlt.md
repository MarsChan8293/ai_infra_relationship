---
type: project
name: vllm-rlt
layer: inference-engine
status: active
repository: https://github.com/ThinkFlowLab/vllm-rlt
docs: https://github.com/ThinkFlowLab/vllm-rlt/tree/main/docs
areas:
  - "recurrent-language-model"
  - "loop-level-continuous-batching"
  - "adaptive-compute"
  - "depth-aware-kv-cache"
  - "prefix-caching"
  - "pd-disaggregation"
  - "cuda-graph"
  - "chunked-prefill"
hardware:
  - "nvidia"
integrations:
  - "NIXL"
last_verified: "2026-10"
---
# vllm-rlt
## 项目定位

vllm-rlt 是面向 recurrent / looped Transformer 的独立 inference engine。虽然名称和组织方式借鉴 vLLM style，但 README 明确说明 **运行不依赖 vLLM**，因此不能因为项目名写成 vLLM integration。

## 核心调度

recurrent model 会对同一个 Transformer core 重复执行不同 loop depth。vllm-rlt 将 batch boundary 下沉到 loop 层，让处于不同 recurrence depth 的 request 仍可共享 batch，对应一种 depth-adaptive [[concept/inference/serving/Continuous Batching|Continuous Batching]]。

它还实现：

- adaptive early exit；
- depth-aware paged KV layout；
- prefix caching、incremental page allocation、priority scheduling 与 preemption；
- chunked prefill；
- CUDA Graph / multi-stream / reusable buffer；
- 单机多 GPU P/D worker pool。

## P/D 与数据移动

项目明确实现 prefill/decode disaggregation，并通过 [[community/ai-dynamo/NIXL/NIXL|NIXL]] 传输 KV，在 chunked prefill compute 与 transfer 间做 overlap。这使它直接连接 [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]]、[[concept/inference/kv-cache/KV Cache Management|KV Cache Management]] 与 [[concept/inference/kv-cache/KV Cache Transfer|KV Cache Transfer]]。

## 当前模型边界

当前主要支持 ByteDance Ouro 系列 recurrent model；项目不是通用 vLLM fork，也不应按普通 Transformer serving 的模型覆盖面衡量。

## Sources

- https://github.com/ThinkFlowLab/vllm-rlt
- https://arxiv.org/abs/2608.09444
