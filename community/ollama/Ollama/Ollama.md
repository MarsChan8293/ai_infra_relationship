---
type: project
name: Ollama
linked_people:
  - "company/Ollama/Jeffrey Morgan"
  - "company/Ollama/Michael Chiang"
companies: ["Ollama"]
company_relation: company-originated
layer: local-inference-platform
open_source: true
repository: https://github.com/ollama/ollama
areas: [local-inference, hybrid-inference, model-serving, model-management, gguf, ggml, llama-cpp, mlx, multimodal-inference, tool-calling, openai-compatible-api, agent-integrations]
hardware: [CPU, NVIDIA GPU, AMD GPU, Apple Silicon, Vulkan]
governance: Ollama company-led open-source project
people:
  - "company/Ollama/Jeffrey Morgan"
  - "company/Ollama/Michael Chiang"
last_verified: "2026-09"
linked_companies:
  - "company/Ollama/Ollama"
---
# Ollama

## 项目定位

Ollama 是面向 open models 的本地 / 混合推理平台，核心目标是让开发者用统一 CLI、REST API、模型库与运行时在个人电脑上运行模型，并在需要时接入 cloud model。它覆盖模型下载与管理、推理执行、GPU 调度、OpenAI / Anthropic 兼容接口、tool calling 与 coding-agent 集成，因此比单一 inference kernel 或 backend 更靠近完整 developer-facing runtime。

截至 2026-09，官方 README 的入口已经扩展到 Claude Code、Codex、Copilot、OpenCode、OpenClaw 等 agent / coding tooling；项目仍保持开源，官方仓库为 https://github.com/ollama/ollama。

## llama.cpp / GGML 关系

Ollama 与 [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] 的关系需要按时间分层理解：

- 早期 Ollama 大量依赖 llama.cpp 作为模型 inference backend；
- 2025 年 Ollama 推出自己的 multimodal engine，并明确说明直接使用 [[community/ggml-org/ggml/ggml|GGML]] tensor library 构建模型图，以提高多模态模型的模块化与可靠性；
- 2026 年 Apple Silicon 路线又加入 MLX engine；
- 2026-06 的 Ollama 0.30 官方公告同时说明，GGUF 兼容与更广硬件支持继续通过 llama.cpp 增强；
- 当前官方 README 仍将 llama.cpp 列为 supported backend。

因此现在更准确的技术图是：

`Ollama orchestration / model management`
→ `Ollama native engines + GGML`
→ `llama.cpp backend / GGUF ecosystem`
→ `MLX on Apple Silicon`

而不是简单把 Ollama 描述成“llama.cpp wrapper”。

## 本地到混合推理

Ollama 最初以 local-first 为核心，强调模型、数据和计算留在用户设备。2025–2026 项目继续扩展：
- 新 model scheduler，改善多 GPU 利用与 OOM 行为；
- cloud models / hybrid inference；
- Anthropic Messages API / OpenAI-compatible API；
- coding-agent launch flows；
- web search、tool calling、thinking、multimodal input 等能力。

2026-07 官方公司文章称 Ollama 已服务 8.9 million developers，并把下一阶段重点描述为 seamless hybrid inference 与 open model access。

## Apple Silicon / MLX

2026-03 起，Ollama 在 Apple Silicon 上预览 MLX engine，利用 Apple unified memory 与 GPU Neural Accelerators。后续 0.31 又继续围绕 MLX、multi-token prediction 和本地 coding-agent workload 做性能优化。

这使 Ollama 的 Apple 路线不再只依赖 llama.cpp / Metal，而是形成独立 MLX execution path。

## 与现有图谱项目的关系

- [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]]：历史核心 inference backend；2026 仍用于 GGUF compatibility 与广泛硬件支持。
- [[community/ggml-org/ggml/ggml|ggml]]：Ollama 自研新 engine 直接依赖的 tensor library，是更底层、持续存在的技术关系。
- [[community/FlashML-org/FreeToken/FreeToken|FreeToken]]：都面向 consumer / local hardware，但 FreeToken 更聚焦大 MoE 的 CPU↔GPU bandwidth-adaptive execution；Ollama 更偏完整 local/hybrid model platform 与开发者体验。
- [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：同样覆盖显存受限场景，但 KTransformers 更强调异构大模型执行优化，Ollama 更强调统一产品化 runtime / model distribution / API。
- [[community/vllm-project/vLLM/vLLM|vLLM]] / [[community/sgl-project/SGLang/SGLang|SGLang]]：同属 LLM inference 生态，但服务形态不同；不因功能相近自动建立人物强边。

## 公司与创始人

Ollama 公司由 [[company/Ollama/Jeffrey Morgan|Jeffrey Morgan]] 与 [[company/Ollama/Michael Chiang|Michael Chiang]] 共同创办。两人此前共同创建 Kitematic，2015 年被 Docker 收购，之后相关工作发展为 Docker Desktop。2026-07 Ollama 官方文章再次由 “Jeff & Michael” 联署并回顾了这条创业路径。

## Sources
- https://github.com/ollama/ollama
- https://ollama.com/blog/multimodal-models
- https://ollama.com/blog/mlx
- https://ollama.com/blog/improved-performance-and-model-support-with-gguf
- https://ollama.com/blog/all-aboard-open-models
- https://www.ycombinator.com/companies/ollama

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/Ollama/Jeffrey Morgan|Jeffrey Morgan]]：[[company/Ollama/Michael Chiang|Michael Chiang]]：Ollama 共同创始人；此前也是 Kitematic 共同创始人。
- [[company/Ollama/Michael Chiang|Michael Chiang]]：[[company/Ollama/Jeffrey Morgan|Jeffrey Morgan]]：Ollama 共同创始人；此前也是 Kitematic 共同创始人。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Ollama/Ollama|Ollama]]：公司页与社区/项目页均有显式记录；关系：`company-originated`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
