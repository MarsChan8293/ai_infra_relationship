---
type: project
name: "Evolving Infra"
layer: distributed-serving
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/mit-han-lab/EvolvingInfra
docs: https://github.com/mit-han-lab/EvolvingInfra/tree/main/docs
areas:
  - agent-adaptive-serving
  - dynamic-pd-allocation
  - inference-scheduling
  - agent-aware-kv-management
  - distributed-kv-cache
  - kv-aware-routing
hardware:
  - nvidia
last_verified: "2026-11"
---
# Evolving Infra

## 项目简介

Evolving Infra（论文 *Evolving Infra: Agent-Adaptive LLM Serving at Scale*，2026）是面向 Agent 工作负载的分布式推理服务系统。它在**无需离线 profiling**的前提下，根据 Agent 的子任务分支、上下文管理与流量特征，在线调整 Prefill/Decode (P/D) 算力配置，并优化 KV Cache 的复用、迁移和淘汰。

## GitHub / 论文

- 官方代码：https://github.com/mit-han-lab/EvolvingInfra
- 论文：https://arxiv.org/abs/2611.12304
- 主页：https://inference-rsi.com/
- 部署文档：https://github.com/mit-han-lab/EvolvingInfra/tree/main/docs
- 许可：MIT；SGLang 派生引擎、Rust router core 与部分 benchmark 代码保留 Apache-2.0 许可，详见 LICENSE / NOTICE。

## 关键技术

1. **Compute / KV 解耦**：把 KV 的生命周期从 P/D worker 角色中分离，Agent 分支仍需复用的 KV 留在共享 host-memory pool；节点无需重启即可在数秒内切换 Prefill 和 Decode 角色。
2. **Online Planner**：考虑子 Agent 和 context management 的成本模型，随负载变化调整 P:D 资源比例。
3. **Agent-aware distributed KV manager**：利用 compaction、sub-agent 完成等上下文生命周期信号，淘汰不再需要的 KV，保留将被分支复用的 KV，并驱动数据迁移。
4. **Router 与 KV directory**：协同 P/D 实例选择、负载预估和 KV 寻址，降低重复 Prefill。

## 代码结构

- `evolving_infra/engine/`：派生自 [[community/sgl-project/SGLang/SGLang|SGLang]] 的 serving engine。
- `evolving_infra/router/core/`：Rust router。
- `evolving_infra/router/indexer/`：分布式 KV directory；其他 router 模块包括 frontend、client。
- `evolving_infra/planner/`：在线 P/D Planner。
- `evolving_infra/launch/`、`examples/`：模型与硬件部署样例。
- `benchmarks/`、`tests/`、`docker/`：Agent traces、测试和镜像。

## 主要研究者 / 组织

论文作者包括 Hao Kang、Weili Xu、Ziyang Li、Zheng Du、Hanchen Li、Tian Xia、Song Bian、Tushar Krishna、Huizi Mao、Ion Stoica 和 Song Han。研究团队的机构包括 Georgia Tech、UIUC、UC Berkeley、NVIDIA、OpenAI 和 MIT。代码托管于 `mit-han-lab` GitHub 组织，与 [[university/Massachusetts Institute of Technology/HAN Lab|MIT HAN Lab]] 有直接公开联系；不因论文共同署名推断雇佣、师生或长期维护关系。

## 技术关联

- 计算引擎基于 [[community/sgl-project/SGLang/SGLang|SGLang]] 派生；这不是对上游原版引擎的无侵入插件。
- 与 [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] 为论文基准对照关系，**不是已验证的运行时集成**。
- 对应 [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]]、[[concept/inference/scheduling/Inference Scheduling|Inference Scheduling]]、[[concept/inference/kv-cache/KV Cache Management|KV Cache Management]]、[[concept/inference/scheduling/KV-Aware Routing|KV-Aware Routing]]。
- 可与 [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]、[[community/LMCache/LMCache/LMCache|LMCache]]、[[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] 做架构对比；**尚无证据表明原生互通**。

## 实验数据与工程边界（2026-11）

论文使用 GLM-5.2、Kimi K2.6，测量 coding、math、computer-use Agent，在最多 256 张 NVIDIA GB300 GPU 上对比 Dynamo，报告平均端到端延迟最高改善 4.1 倍、P95 TTFT 最高改善 14 倍、吞吐最高改善 2.7 倍。均为作者特定基准结果，非通用性能承诺。

官方部署镜像列出 H200、B300（x86_64）、GB300（aarch64）环境。**尚未确认 910B/910C、vLLM-Ascend、国产 NPU 的原生适配**。研究落地重点：在线 P:D 规划算法、Agent 分支级 KV 保留/淘汰、共享 host-memory KV 可见性，以及 role switch / KV transfer 对 TTFT、TPOT 的影响。

## Sources

- https://github.com/mit-han-lab/EvolvingInfra
- https://github.com/mit-han-lab/EvolvingInfra/blob/main/LICENSE
- https://arxiv.org/abs/2611.12304
- https://inference-rsi.com/
