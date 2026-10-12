---
type: project
name: InferNex
status: active
last_verified: "2026-10"
layer: serving-platform
areas: [distributed-inference, inference-scheduling, kv-aware-routing, autoscaling, ascend-inference]
hardware: [ascend]
repository: https://gitcode.com/openFuyao/InferNex
code_availability: public
linked_concepts:
  - "concept/inference/serving/P-D Disaggregation"
  - "concept/inference/scheduling/KV-Aware Routing"
  - "concept/inference/scheduling/Autoscaling"
  - "concept/inference/scheduling/Inference Scheduling"
---
# InferNex

openFuyao 社区的 K8s-native 分布式 LLM 推理加速套件，不是独立模型执行引擎。

## 主要组件与能力
- Hermes-router：KV Cache aware / 时延预测路由，支持 Kubernetes Gateway API Inference Extension。
- PD-Orchestrator：动态 Prefill/Decode 分离编排。
- Elastic Scaler：PD 组及组内弹性伸缩。
- Mooncake / cache-indexer：分布式分级 KV Cache 管理和命中索引。
- Eagle-eye：推理系统及设备可观测。
- 权重分发、LeaderWorkerSet 部署、KServe 桥接（v26.06 发布说明）。

## M × H × E 配置管理评估
- M（模型）：模型规格、权重位置、部署模板及模型版本兼容性待验证。
- H（硬件）：Ascend 910B/910C、NPU DRA、拓扑与网络资源声明需分版本核实。
- E（引擎）：已公布 vLLM-Ascend 多版本验证矩阵；需核验同时管理多引擎版本、升级回滚及灰度策略。
- 重点对比 [[MindIE-Motor]]、[[AIBrix]]、[[llm-d]]、[[KServe]]：KV 路由、PD 调度、故障恢复、权重加载、弹性伸缩与 LWS。

## 官方资料
- https://www.openfuyao.cn/zh/project/infernex.html
- https://gitcode.com/openFuyao/InferNex
- https://www.openfuyao.cn/zh/blogs/blogsList/openFuyao-26-03-released/
- https://www.openfuyao.cn/zh/blogs/blogsList/openFuyao-26-06-released/

说明：性能收益为官方特定测试场景结果，不代表普遍部署效果。
