---
type: project
name: agentperf-local
linked_people: []
layer: benchmark
status: active
repository: https://github.com/ArtificialAnalysis/aa-agentperf-local
docs: https://github.com/ArtificialAnalysis/aa-agentperf-local
areas:
  - "agentic-workload"
  - "inference-benchmark"
  - "trajectory-replay"
  - "latency"
  - "throughput"
  - "local-inference"
  - "reproducible-recipes"
hardware:
  - "nvidia"
  - "apple-silicon"
integrations:
  - "llama.cpp"
  - "vLLM"
  - "SGLang"
  - "Ollama"
  - "Splash"
last_verified: "2026-10"
linked_companies: []
code_availability: public
---
# agentperf-local
## 项目定位

agentperf-local 是 Artificial Analysis 开源的本地 Agent serving benchmark。它与单 prompt / synthetic token benchmark 的主要区别是：重放记录下来的真实 agent conversation，每一轮请求携带到当前为止的完整 conversation，从而测量长会话、多轮 context replay 对 inference system 的实际压力。

## Benchmark contract

默认 replay `agentperf-default-v1` 包含 8 个 recorded agent task、168 个 model turn；完整可比 run 要求 65,536 token context。工具同时记录 throughput 与 latency，但明确 **不测输出质量**。

`exact` output policy 会要求 server 生成记录中的 token 数；如果 backend 无法 honor `ignore_eos`，结果会降级为 recorded policy 并标记不可直接横向比较。

## Serving integrations

项目可以附着或管理启动：

- [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]]
- [[community/vllm-project/vLLM/vLLM|vLLM]]
- [[community/sgl-project/SGLang/SGLang|SGLang]]
- [[community/ollama/Ollama/Ollama|Ollama]]
- [[community/incoai/Splash/Splash|Splash]]

这使它适合作为 Agentic Inference 场景下 M-H-E 组合的统一 workload replay 层。

## 与传统 benchmark 的边界

它测的是 serving speed，不自动证明模型质量、agent task success rate 或不同 backend 的数值完全一致。不同 output policy、context window 和 server capability 会影响可比性，项目自身也显式记录这些限制。

## Sources

- https://github.com/ArtificialAnalysis/aa-agentperf-local
