---
type: person
name: Martin Hickey
aliases: ["hickeyma"]
current_affiliations: ["IBM"]
public_email: martin.hickey@ie.ibm.com
communities: [LMCache, vLLM]
roles: [LMCache Committer, Component Owner]
linked_companies:
  - "company/IBM/IBM"
email_affiliations:
  - "IBM"
areas: [kv-cache, kv-events, non-cuda, ci, packaging, vllm-integration, disaggregated-serving]
confidence: verified
last_verified: "2026-09"
---
# Martin Hickey

当前：[[company/IBM/IBM|IBM]]；LMCache Committer、组件 CODEOWNER。

公开职业邮箱：`martin.hickey@ie.ibm.com`。2026 年多个 vLLM 公共提交持续使用该 IBM 子域邮箱；仓库域名规则会将 `ie.ibm.com` 继承映射到 canonical `IBM` 节点。

## LMCache 角色
LMCache 官方 `MAINTAINERS.md` 将 Martin Hickey 列为 IBM Committer。当前 `CODEOWNERS` 显示其覆盖 non-CUDA compatibility、tests、CI / packaging，并负责 production KV cache events 文档等路径。

## vLLM 直接贡献
- 2026-01 直接向 vLLM 提交 LMCache connector KV events 修复，因此这里将其记录为 `IBM → Martin Hickey → LMCache → vLLM KV Connector` 的可验证桥梁，而不是仅因为 IBM 同时参与 llm-d 就推断项目关系。
- 2026 年继续参与 vLLM disaggregated serving frontend、endpoint plugin、KVCacheSpec / Attention metadata 与 scale-out endpoint 路径。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/vllm-project/vllm/commit/510265472cb216daf7d8e83db6fa03ce48b0f5fc
- https://github.com/vllm-project/vllm/commit/934b1fcbcbbac6e68da7a4246928ac797fe54690
- https://github.com/vllm-project/vllm/commit/0a31372e5fe7cc8bbaf96df0a3e88db9040cf8d5

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/IBM/IBM|IBM]]：当前 affiliation + 公开职业邮箱域名双重证据。

<!-- END AUTO PERSON COMPANIES -->
