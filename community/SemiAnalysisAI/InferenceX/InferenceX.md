---
type: project
name: InferenceX
aliases: ["InferenceMAX"]
layer: benchmark
status: active
repository: https://github.com/SemiAnalysisAI/InferenceX
docs: https://inferencex.semianalysis.com/
areas:
  - "llm-inference"
  - "agentic-inference"
  - "continuous-benchmarking"
  - "performance-per-dollar"
  - "performance-per-watt"
  - "serving-frameworks"
  - "reproducible-benchmarking"
hardware:
  - "nvidia"
  - "amd"
  - "google-tpu"
  - "openai-accelerator"
integrations:
  - "SGLang"
  - "vLLM"
  - "TensorRT-LLM"
  - "NVIDIA Dynamo"
companies: ["SemiAnalysis"]
last_verified: "2026-09"
---
# InferenceX

InferenceX（原 InferenceMAX）是 SemiAnalysis 构建的开源持续推理 benchmark 与研究平台。它的价值在于把“硬件峰值”拆回真实 serving 场景，持续跟踪模型、推理框架、驱动 / kernel 与硬件组合的性能变化，并公开运行 recipe、日志和历史数据。

## 核心能力

- **持续 benchmark**：软件版本、driver、模型或配置变化后重新跑测，而不是只保留一次性榜单。
- **真实 serving stack**：覆盖 [[community/sgl-project/SGLang/SGLang|SGLang]]、[[community/vllm-project/vLLM/vLLM|vLLM]]、[[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]]、[[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] 等。
- **多硬件比较**：公开结果覆盖 NVIDIA Hopper / Blackwell / Rubin、AMD Instinct、Google TPU，以及其他新加速器。
- **成本维度**：除 tokens/s 外，强调 tokens/s/user、cost per million tokens、performance-per-dollar 与 performance-per-watt。
- **AgentX**：面向长上下文、多轮 agentic coding 的 inference workload，补足固定 8K/1K 这类传统 benchmark 对真实 agent 流量的不足。
- **可审计性**：benchmark recipe、GitHub Actions run、日志与数据快照公开，结果可以回溯到具体运行。

## 与现有图谱的连接

- [[community/sgl-project/SGLang/SGLang|SGLang]]：InferenceX 的主要被测 serving engine 之一。
- [[community/vllm-project/vLLM/vLLM|vLLM]]：主要被测 serving engine 之一。
- [[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]]：NVIDIA 栈的重要被测 runtime。
- [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]]：用于部分 disaggregated / Blackwell serving 配置。

这里的“integration”表示 InferenceX 具有直接 runner / benchmark 配置与可复现实测路径，不表示 InferenceX 参与这些上游项目的治理。

## 人物

- [[Dylan Patel]]：SemiAnalysis Founder / CEO / Chief Analyst，并参与 InferenceX 相关研究。
- [[Kimbo Chen]]：参与 GPU architecture、serving performance 与 InferenceX 研究。
- [[Bryan Shan]]：持续参与 InferenceX、DeepSeek / Kimi 等模型推理与硬件 benchmark。
- [[Cam Quilici]]：持续参与 InferenceX / AgentX benchmark 与分析。

## 重要边界

- CoreWeave、Crusoe、Nebius、Oracle、Together AI 等公开被列为算力支持方；**算力支持不自动写成项目归属或公司共建**。
- OpenAI、Meta、Microsoft 等“trusted by / used by”描述不等于 maintainer、owner 或 engineering co-development 关系。
- 被 benchmark 的 NVIDIA / AMD / TPU 硬件不等于 SemiAnalysis 与厂商之间存在组织级合作边。

## Sources

- https://github.com/SemiAnalysisAI/InferenceX
- https://inferencex.semianalysis.com/
- https://inferencex.semianalysis.com/about
- https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat
- https://inferencex.semianalysis.com/blog/deepseekv4-16t-day-0-to-day-43-performance
