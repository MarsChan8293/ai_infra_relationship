# Recent GitHub DISCOVER + EXPAND — 2026-10-03

本轮由用户直接触发，对 2026-09-02 以来新开源 AI Infra GitHub repository 做 frontier DISCOVER，并将确认的 13 个项目 canonicalize 后执行 systems-first EXPAND。

## 新增 canonical projects

1. AgentInfer
2. TIRx Harness
3. TIRx Kernels
4. ModelSphere
5. llm-d-resiliency-manager
6. TritonAscendBench
7. Edge0
8. Splash
9. vllm-rlt
10. agentperf-local
11. LoopSpec
12. OmniKVQuant
13. VeriTile

## 新增 concepts

- Inference Fault Tolerance
- Kernel Formal Verification

## 主要 frontier

### Agentic inference control plane
AgentInfer 把 agent-aware routing / scheduling 与 KV cache lifecycle、vLLM 和 Ascend NPU cache path 连接起来。

### Agentic kernel engineering
TIRx Harness + TIRx Kernels 补入 agent-facing compiler harness、remote execution、benchmark contract 与新一代 kernel portfolio；TritonAscendBench 补入 production Triton → Ascend 910B migration correctness benchmark；VeriTile 补入 formal kernel verification。

### Serving control plane / M-H-E
ModelSphere 补入 heterogeneous accelerator + vLLM/SGLang + P/D + L3 KV pool + autoscaling / autotuning 的 Kubernetes serving platform。

### Reliability
llm-d-resiliency-manager 补入 llm-d/vLLM/LWS 之间的 rank-level failure recovery responsibility split；当前仍为 experimental / proposed incubation。

### Local / recurrent inference
Edge0 与 Splash 分别补入 SSD expert streaming 和 Apple Silicon DFlash2/Metal serving；vllm-rlt 与 LoopSpec 补入 recurrent model 的 loop-level scheduling / KV 与 self-speculative decoding。

### Benchmark / KV optimization
agentperf-local 补入 real agent trajectory replay；OmniKVQuant 补入 Omni-LLM 2-bit KV quantization。

## Evidence boundary

- repository namespace 不自动推断公司 ownership / 雇佣。
- contributor 不自动升级为 maintainer。
- source provenance 不自动升级为 runtime integration。
- research-preview / experimental 能力在项目页保留明确边界。
- 本次为用户直接触发的 targeted DISCOVER + EXPAND，不追加 planner action-history。
