---
type: project
name: AgentInfer
layer: distributed-serving
status: active
repository: https://github.com/openJiuwen-ai/agent-infer
docs: https://github.com/openJiuwen-ai/agent-infer/tree/main/docs
areas:
  - "agentic-inference"
  - "agent-aware-scheduling"
  - "semantic-routing"
  - "request-routing"
  - "kv-cache-management"
  - "kv-cache-transfer"
  - "benchmarking"
hardware:
  - "nvidia"
  - "ascend"
integrations:
  - "vLLM"
last_verified: "2026-10"
---
# AgentInfer
## 项目定位

AgentInfer 是面向 agent workload 的 inference control layer，而不是新的底层模型执行引擎。它可以运行在 vLLM serving engine 内部或前方，把多轮 agent session 的 continuity、routing、cache 和 scheduling 变成一等控制对象。

## 核心结构

- **Semantic Router**：面向 heterogeneous LLM 的可编程 Mixture-of-Models routing，显式考虑多轮 session continuity，减少模型切换。
- **Agent Router**：为大规模 vLLM deployment 提供 agent-aware scheduling；官方还提供基于 vLLM Router WASM middleware 的 session-affinity 路径。
- **Agent Cache**：vLLM plugin，覆盖 request scheduling、KV cache management、pooling 与 transfer，并明确包含 Ascend NPU-native KV cache 路径。
- **AgentBench**：用真实 agent run 或 trace replay 测 serving engine 的 agentic workload 行为。

## 图谱关系

[[community/vllm-project/vLLM/vLLM|vLLM]] 是当前明确的 engine integration。项目还直接落在 [[concept/inference/scheduling/Inference Scheduling|Inference Scheduling]]、[[concept/inference/scheduling/Request Routing|Request Routing]]、[[concept/inference/kv-cache/KV Cache Management|KV Cache Management]] 与 [[concept/inference/kv-cache/KV Cache Transfer|KV Cache Transfer]] 交叉处。

这里不把“agent workload”自动等同于 [[concept/inference/agent/Agent Harness|Agent Harness]]：AgentInfer 管的是 inference-side control plane，而不是完整 agent loop/runtime。

## 当前边界

README 当前 quick start 以 vLLM 0.23.0 + CUDA GPU 为主；Ascend 能力明确出现在 Agent Cache 的 NPU-native KV 管理/传输功能中。两者应分开理解，不能把 CUDA quick-start 条件误写成“仅支持 NVIDIA”。

## Sources

- https://github.com/openJiuwen-ai/agent-infer
