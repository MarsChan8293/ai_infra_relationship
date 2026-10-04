---
type: company
name: Novita AI
aliases: ["Novita Labs", "novitalabs"]
areas: [ai-infrastructure, gpu-cloud, llm-inference, kv-cache, inference-optimization, agent-sandbox]
projects:
  - Chord
  - PegaFlow
  - LLM Autotuner
  - NovitaBox
last_verified: "2026-10"
---
# Novita AI

Novita AI / Novita Labs 是围绕 GPU cloud、模型 API 与生产级 AI infrastructure 构建服务的团队。对本知识图谱更重要的不是其通用 API SDK，而是 2026 年开始形成的一组 inference / data-plane / agent-runtime 开源项目。

## AI Infra 开源主线

- [[community/novitalabs/chord/chord|Chord]]：面向 Kimi K2.x serving shape 的 W4A16 MoE CUDA kernel，覆盖 H200 与 B200/B300。
- [[community/novitalabs/pegaflow/pegaflow|PegaFlow]]：独立于推理进程的 external KV cache 服务，覆盖 host memory、SSD、RDMA 与跨实例共享。
- [[community/novitalabs/autotuner/autotuner|LLM Autotuner]]：针对 vLLM / SGLang 的 SLO-aware 参数自动调优。
- [[community/novitalabs/NovitaBox/NovitaBox|NovitaBox]]：面向 AI Agent 的本地 sandbox runtime，支持 Firecracker、gVisor、Cloud Hypervisor 与 NVIDIA GPU。

这几条线分别落在 kernel、KV/data plane、serving configuration optimization 和 agent execution isolation 四个层面，说明 Novita AI 的开源重心已经从“模型 API 接入”扩展到实际的推理基础设施栈。

## 与 vLLM 的协作

2026 年 5 月 18 日，Novita AI 与 vLLM 团队联合介绍 PegaFlow external KV cache；2026 年 9 月 15 日又联合介绍 Chord W4A16 MoE kernel。两者都不是替代 vLLM，而是分别通过 KV connector 与 Humming-compatible MoE backend 接入 vLLM。

## Sources

- https://github.com/novitalabs
- https://vllm.ai/blog/2026-05-18-pegaflow
- https://vllm.ai/blog/2026-09-15-novita-chord-w4a16-moe
