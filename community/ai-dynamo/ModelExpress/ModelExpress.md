---
type: project
name: ModelExpress
layer: distributed-serving
status: active
code_availability: public
repository: https://github.com/ai-dynamo/modelexpress
docs: https://github.com/ai-dynamo/modelexpress/tree/main/docs
areas:
  - weight-loading
  - model-startup
  - p2p-rdma
  - jit-cache-transfer
  - gpudirect-storage
  - model-distribution
hardware:
  - nvidia
integrations:
  - "NIXL"
  - "Dynamo"
  - "vLLM"
  - "SGLang"
  - "TensorRT-LLM"
companies:
  - NVIDIA
last_verified: "2026-10"
---

# ModelExpress

## 项目简介
ModelExpress（仓库 `ai-dynamo/modelexpress`）是 NVIDIA/ai-dynamo 生态的 **模型权重加载与分发加速系统**，目标是缩短 Replica 冷启动以及重复 JIT 编译开销。它不是 Token/KV 推理执行引擎，也不是 KV Cache 池。

## 关键实现
- 利用 [[NIXL]] / GPUDirect RDMA 在已有模型副本与新增副本之间 P2P 传输模型权重；配置可用时复用代码生成或 JIT 缓存。
- 支持 ModelStreamer、GPUDirect Storage、CPU Staging 和原生 Loader 兜底；按兼容能力选择传输策略。
- 控制面使用 Redis/Kubernetes 等发布、查询源副本；真实大规模权重走独立数据路径。
- README 列出 [[vLLM]]、[[SGLang]]、[[TensorRT-LLM]] 和 [[Dynamo]] 的不同集成；各引擎功能成熟度/传输协议并不完全相同。

## 与 RTX PRO 5000 场景的价值
对于多节点相同模型的弹性扩容与推理 Engine 崩溃恢复，重点验证 **权重 Ready 时间、JIT Cache 复用、GPU P2P/RDMA 可达性、失败兜底**。同节点 PCIe/跨节点 200GbE 场景不能直接套用上游 8×B200 高速网络示例指标。

## 技术边界
- 加速权重/编译产物路径，不解决 Agent 的完整 KV State 生命周期。
- 业务收益高度依赖网络设备、DMA 支持、版本配套及实际模型大小。

## 关联
[[NIXL]] · [[Dynamo]] · [[vLLM]] · [[SGLang]] · [[TensorRT-LLM]] · [[Mooncake]]

## Sources
- https://github.com/ai-dynamo/modelexpress
- https://github.com/ai-dynamo/modelexpress/blob/main/README.md
- https://github.com/ai-dynamo/modelexpress/tree/main/docs
