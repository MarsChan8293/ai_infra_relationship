---
type: concept
name: Expert Parallelism
aliases:
  - EP
  - MoE Expert Parallelism
  - 专家并行
domain: inference
topic: parallelism
parent_concepts:
  - Parallelism
related_concepts:
  - Data Parallelism
  - Tensor Parallelism
projects:
  - vLLM
  - DeepEP
last_verified: 2026-09
---

# Expert Parallelism

## 一句话定义

Expert Parallelism（EP）把 Mixture-of-Experts 模型中的不同 experts 分布到不同设备 / rank，token 根据 router 结果被 dispatch 到拥有目标 expert 的位置执行，再 combine 回原计算流。

## 解决的问题

MoE 模型的总 expert 参数量很大，但每个 token 只激活少量 expert。若每个设备复制全部 experts 会浪费显存；EP 通过分片 expert 参数扩大可部署模型规模。

## 核心机制

Router 先计算 token-to-expert assignment。随后 token hidden states 按目标 expert 在 rank 间重新分布，常见数据面是 All-to-All / dispatch-combine。每个 rank 只执行本地 experts，再把结果传回原 token 顺序。

## 与相邻概念的区别

- [[Tensor Parallelism]] 切单个 expert / dense layer 内部张量，EP 切 expert 集合。
- [[Data Parallelism]] 复制 serving replica，EP 则在一个 MoE 执行域内分布 experts。
- EP 与 DP 可以组合，例如不同 DP group 共享/复制不同 expert group。

## 代价与适用边界

EP 的关键瓶颈不是只有 expert GEMM，还包括 token dispatch、All-to-All 带宽、expert 负载不均和跨节点拓扑。热门 expert 可能形成热点。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 提供 Expert Parallel Deployment，并包含 EPLB / expert load balancing 相关能力。

## 通信实现

[[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] 是面向 MoE Expert Parallel 的专用通信库，以 [[All-to-All]] 语义实现 token dispatch / combine，并针对训练、Prefill 与低延迟 Decode 提供不同通信路径。

## Sources

- https://github.com/deepseek-ai/DeepEP

- https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/
- https://docs.vllm.ai/en/latest/api/vllm/config/parallel/
- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
