---
type: concept
name: Disaggregated Serving
aliases:
  - Disaggregated Inference Serving
  - 分离式推理服务
domain: inference
topic: serving
related_concepts:
  - P-D Disaggregation
  - KV Cache Transfer
projects:
  - Dynamo
  - Mooncake
  - vLLM
  - SGLang
  - llm-d
  - MindIE-Motor
last_verified: 2026-09
---

# Disaggregated Serving

## 一句话定义

Disaggregated Serving 把原本由一个统一推理 worker 完成的阶段或状态拆到不同资源池中运行，并通过网络、共享存储和调度器把它们重新组合成一次完整请求。

## 解决的问题

LLM serving 的不同阶段往往具有不同的计算、内存和通信特征。如果强制由同一组 GPU 承担全部阶段，资源配置和扩缩容只能取折中值。Disaggregation 让不同阶段可以独立放置、扩缩、并行化和优化。

## 核心机制

系统把请求路径切成多个角色，由 router/orchestrator 决定请求在哪个 worker 执行，并显式传递后续阶段所需的状态。对 autoregressive LLM 最典型的实例是 [[P-D Disaggregation]]：prefill 生成 KV，随后通过 [[KV Cache Transfer]] 交给 decode。

## 与相邻概念的区别

Disaggregated Serving 是更宽的系统架构概念，并不只等于 P/D。未来 encode、prefill、decode、多模态 encoder、KV storage 乃至其他 service role 都可能独立拆分。

## 代价与适用边界

拆分能带来独立扩缩容和资源异构，但也引入跨阶段传输、服务发现、路由、故障处理和容量匹配。低并发、短输入或慢网络环境中，统一 worker 往往更简单。

## 项目实现

[[community/ai-dynamo/Dynamo/Dynamo|Dynamo]] 把 disaggregated serving 作为核心部署模式，可独立管理 prefill/decode worker pool。[[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 从 KVCache-centric disaggregated architecture 出发拆分 prefill/decode cluster。[[community/vllm-project/vLLM/vLLM|vLLM]] 和 [[community/sgl-project/SGLang/SGLang|SGLang]] 均提供 P/D disaggregation 能力。[[community/llm-d/llm-d/llm-d|llm-d]] 在 Kubernetes serving 层实现 disaggregated serving；[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] 则在昇腾集群控制面提供 PD 分离/混部部署与调度。

## Sources

- https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving
- https://kvcache-ai.github.io/Mooncake/
- https://docs.vllm.ai/en/latest/features/disagg_prefill/
- https://docs.sglang.ai/backend/pd_disaggregation.html
- https://llm-d.ai/docs/dev/architecture/advanced/disaggregation
- https://gitcode.com/Ascend/MindIE-Motor
