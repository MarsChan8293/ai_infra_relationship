---
type: project
name: LiteLLM
linked_people:
  - "community/BerriAI/LiteLLM/kerry-berri"
  - "community/BerriAI/LiteLLM/mateo-berri"
  - "community/BerriAI/LiteLLM/ryan-crabbe-berri"
  - "community/BerriAI/LiteLLM/yuneng-berri"
layer: distributed-serving
status: active
repository: https://github.com/BerriAI/litellm
docs: https://docs.litellm.ai/
areas:
  - "llm-gateway"
  - "provider-routing"
  - "rate-limiting"
  - "cost-tracking"
  - "openai-compatible-proxy"
integrations:
last_verified: "2026-09"
linked_companies: []
---
# LiteLLM

> 面向多模型、多提供商的 OpenAI-compatible LLM Gateway 与统一客户端层。

## 核心能力

| 能力 | 说明 |
|---|---|
| 统一 API | 用统一 OpenAI 风格接口调用多类模型提供方 |
| Proxy / Gateway | 自托管模型网关与路由 |
| 治理能力 | 支持认证、限流、成本跟踪和日志钩子 |
| Fallback / Routing | 在多个 deployment/provider 间路由和回退 |

## 边界

LiteLLM 主要管理 API 与模型提供方流量，不负责 GPU kernel、KV Cache 或 Kubernetes 设备资源。

## 集成与后端

V0.1 暂不把通用 OpenAI-compatible endpoint 兼容自动视作“项目级强集成”。

## 关联项目

- Kubernetes inference routing：Gateway API Inference Extension。
- 通用模型服务：BentoML。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方文档为快照。

## Governance / Code Owners

LiteLLM 官方仓库存在路径级 CODEOWNERS，但当前没有发现覆盖全仓的 MAINTAINERS roster。以下人物只按 CODEOWNERS 的精确 scope 记录，不把路径所有权外推成全仓 maintainer：

- [[community/BerriAI/LiteLLM/yuneng-berri|@yuneng-berri]]：UI、experimental proxy output、migration 与 CODEOWNERS 文件自身的 owner。
- [[community/BerriAI/LiteLLM/ryan-crabbe-berri|@ryan-crabbe-berri]]：UI / proxy output，以及 model price metadata 的共同 owner。
- [[community/BerriAI/LiteLLM/mateo-berri|@mateo-berri]]：model price metadata 共同 owner。
- [[community/BerriAI/LiteLLM/kerry-berri|@kerry-berri]]：model price metadata 共同 owner。

这里的关系强度是“path-level code ownership”，而不是未经证明的全仓 maintainer 身份。

## 直接来源

- https://docs.litellm.ai/
- https://github.com/BerriAI/litellm

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/BerriAI/LiteLLM/kerry-berri|kerry-berri]]：[[community/BerriAI/LiteLLM/LiteLLM|LiteLLM]]：path-level CODEOWNERS 治理关系。
- [[community/BerriAI/LiteLLM/mateo-berri|mateo-berri]]：[[community/BerriAI/LiteLLM/LiteLLM|LiteLLM]]：path-level CODEOWNERS 治理关系。
- [[community/BerriAI/LiteLLM/ryan-crabbe-berri|ryan-crabbe-berri]]：[[community/BerriAI/LiteLLM/LiteLLM|LiteLLM]]：path-level CODEOWNERS 治理关系。
- [[community/BerriAI/LiteLLM/yuneng-berri|yuneng-berri]]：[[community/BerriAI/LiteLLM/LiteLLM|LiteLLM]]：path-level CODEOWNERS 治理关系。

<!-- END AUTO PROJECT PEOPLE -->

## Governance snapshot

LiteLLM 当前仓库存在 `.github/CODEOWNERS`，但规则是**路径级**而不是全仓 maintainer 声明：

- `@yuneng-berri`、`@ryan-crabbe-berri`：UI / experimental proxy 等路径的 code owners。
- `@mateo-berri`、`@ryan-crabbe-berri`、`@kerry-berri`：model price/context-window 数据路径的 code owners。
- `@yuneng-berri`：CODEOWNERS 文件自身 owner。

因此本轮只把这些账号记为 scoped ownership 证据，不升级为 LiteLLM 全仓 maintainer 人物边。若未来出现 repo-wide CODEOWNERS、MAINTAINERS 或官方 governance 文档，再进行 VERIFY。

- https://github.com/BerriAI/litellm/blob/main/.github/CODEOWNERS
