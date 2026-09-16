---
type: person
name: Jiayi Yao
aliases: ["YaoJiayi"]
current_affiliations: ["TensorMesh"]
schools:
  - "University of Chicago"
communities: [LMCache, vLLM]
roles: [LMCache Committer, CacheBlend First Author]
linked_companies:
  - "company/TensorMesh/TensorMesh"
areas: [kv-cache, rag, cache-reuse, vllm-integration, distributed-storage]
confidence: verified
last_verified: "2026-09"
---
# Jiayi Yao

当前：[[company/TensorMesh/TensorMesh|TensorMesh]] / University of Chicago 研究网络；LMCache Committer，CacheBlend 第一作者。

## LMCache / CacheBlend
LMCache 官方 `MAINTAINERS.md` 将 Jiayi Yao 列为 Committer。LMCache 官方 CacheBlend 文章明确写明其为 EuroSys 2025 Best Paper 第一作者；CacheBlend 已进入 LMCache 与 vLLM Production Stack，用于突破纯 prefix caching 对 RAG 非前缀复用的限制。

## vLLM 直接贡献
Jiayi Yao 不是只在 LMCache 一侧维护 connector。vLLM 官方仓库存在其直接提交：
- 2025-03：为 LMCache connector 增加 chunked prefill 支持；
- 2025-06：更新 LMCache connector 以适配最新 connector API。

因此这里将其记录为 `LMCache ↔ vLLM` 的直接跨项目工程桥。

## TensorMesh
Google / LMCache 的 GKE 分层 KV cache 合作材料明确点名 Kuntai Du、Jiayi Yao、Yihua Cheng，并说明他们在合作开发 LMCache 后成立 TensorMesh。这里据此记录 TensorMesh 当前 affiliation，不从同公司关系自动推断所有人物之间的 coworker 强边。


## 学校关联
- [[university/University of Chicago/University of Chicago|University of Chicago]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://blog.lmcache.ai/en/2025/03/31/cacheblend-best-paper-acm-eurosys25-enabling-100-kv-cache-hit-rate-in-rag/
- https://blog.lmcache.ai/zh/2025/10/23/gke-lmcache/
- https://github.com/vllm-project/vllm/commit/6d7f037748b2e7df64f3318e54101a1c80016f3c
- https://github.com/vllm-project/vllm/commit/cda92307c145e7722cdc33e6d26e105eeb22b882

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/TensorMesh/TensorMesh|TensorMesh]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
