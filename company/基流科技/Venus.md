---
type: project
name: Venus
layer: scheduler
status: active
areas:
  - cluster-scheduling
  - inference-serving
  - post-training
  - elastic-scaling
  - fault-tolerance
  - cache-management
  - workload-orchestration
companies: ["基流科技"]
last_verified: "2026-09"
---
# Venus

Venus 是基流科技面向 AI 算力集群的操作系统 / 运行管理平台。它覆盖调度、通信、缓存、隔离、监控、故障诊断、恢复与 workload acceleration，并同时服务 pre-training、post-training、inference 和 agentic workload。

## Inference 能力
基流科技 2026 年香港上市申请材料明确描述了 Venus 的 inference task management：

- 可从统一模型仓库选择模型并选择适配的 inference framework。
- 支持 distributed inference，使单个 inference instance 跨多个计算节点协同运行。
- 支持配置多个 inference replicas，以扩展吞吐。
- 支持根据请求流量动态增加或减少 active inference instances，实现 elastic scaling。
- 提供任务级 GPU 利用率、温度、运行状态等可视化监控。

这使 Venus 成为基流科技图谱中比“GPU 集群交付”更接近 inference platform / serving control plane 的节点。

## Post-training / RL
Venus 还支持 LoRA、RLHF 等 post-training workflow，统一管理 fine-tuning、inference、validation 与 iterative optimization。

招股材料进一步披露 VenusRL：通过 asynchronous input/output orchestration，在 inference validation 阶段把低优先级任务调度到暂时空闲的 inference GPU 上，并在 validation 完成后抢占释放；同时结合轻量级 VenusBox 管理隔离执行环境。公司材料称，相比其所定义的传统 post-training 实现方式，该架构整体任务效率提升 37%。

## 基础设施能力
Venus 同时覆盖 topology / communication、cache、multi-tenant isolation、fault detection、checkpoint recovery 与跨地域 compute scheduling，因此它位于：
cluster operations → scheduler / runtime → post-training / inference serving
这一层级交界处。

## Sources
- https://www1.hkexnews.hk/app/sehk/2026/108484/documents/sehk26042906017.pdf
