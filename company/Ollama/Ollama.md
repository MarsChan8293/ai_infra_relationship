---
type: company
name: Ollama
aliases: ["Ollama"]
areas: [local-inference, hybrid-inference, open-models, developer-tools, model-serving, model-runtime]
projects: [Ollama]
people:
  - "company/Ollama/Jeffrey Morgan"
  - "company/Ollama/Michael Chiang"
headquarters: San Francisco
last_verified: "2026-09"
---
# Ollama

Ollama 是围绕 open models、local inference 与 hybrid inference 构建开发者平台的公司，也是 [[community/ollama/Ollama/Ollama|Ollama]] 开源项目的发起与核心维护组织。

## AI Infra 位置

Ollama 的核心价值不在训练 foundation model，而在把模型获取、格式兼容、硬件后端、运行时、调度、API 与开发者工具整合成统一体验。其技术栈目前横跨：
- 本地 CPU / GPU inference；
- [[community/ggml-org/ggml/ggml|GGML]] / [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] / GGUF 生态；
- Apple Silicon 上的 MLX engine；
- multimodal inference；
- local ↔ cloud hybrid inference；
- coding agents 与 tool calling。

## 创始人

- [[company/Ollama/Jeffrey Morgan|Jeffrey Morgan]]：Co-founder。
- [[company/Ollama/Michael Chiang|Michael Chiang]]：Co-founder。

两人大学时期共同创建 Kitematic，后者 2015 年被 Docker 收购。Ollama 2026 年官方文章把这段经历视为其“把复杂基础设施变得易用”的直接前史。

## 2026 公司状态

Ollama 2026-07 官方宣布已融资累计 88M 美元，投资方包括 Benchmark、Theory Ventures、8VC、Y Combinator 等，并称产品服务 8.9 million developers。这里把这些信息作为公司规模与生态背景，不据此推断具体技术治理关系。

## 项目关系

[[community/ollama/Ollama/Ollama|Ollama]] 是公司直接发起并持续开发的核心项目，因此使用 `company-originated` 强关系。员工参与其他开源项目时仍需单独证据，不能由公司关系反推。

## Sources
- https://ollama.com/blog/all-aboard-open-models
- https://www.ycombinator.com/companies/ollama
- https://github.com/ollama/ollama
