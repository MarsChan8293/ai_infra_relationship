---
type: person
name: Tony Lin
aliases: ["hlin99", "@hlin99"]
current_affiliations: ["Intel"]
public_email: tony.lin@intel.com
communities: [LMCache]
roles: [Component Owner]
email_affiliations:
  - "Intel"
linked_companies:
  - "company/Intel/Intel"
areas: [kv-cache, vllm-integration, distributed-kv-cache, eviction, gpu-connector, platform, storage-backend]
confidence: high
last_verified: "2026-09"
relations:
  - '{"target":"company/腾讯/Baolong Mao","type":["open-source-collaboration"],"project":"LMCache","confidence":"high","evidence":["https://github.com/LMCache/LMCache/commit/5e69770cd46be1763ff65bc4e05ea2fd1d9645b9"]}'
---
# Tony Lin（hlin99）

当前公开 LMCache commit 使用 `tony.lin@intel.com`；2026-05 被正式加入 LMCache `CODEOWNERS`。

## LMCache 角色
当前 `CODEOWNERS` 将 Tony Lin 放在多条关键数据路径：distributed eviction、GPU connector、platform、Redis / native storage connector、vLLM integration、non-CUDA / C extension 等，因此他是当前 LMCache 中很典型的“跨模块系统工程”节点，而不是单一路径 contributor。

## 人物关系
- [[company/腾讯/Baolong Mao|Baolong Mao]]：PR #3528 的提交说明明确记录根据 `@hlin99` review 重构 CPU/GPU KV-cache allocator，因此建立 `open-source-collaboration` 强边。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/LMCache/LMCache/commit/10ad9e42d39d513e86647519c30d93a162334c66
- https://github.com/LMCache/LMCache/commit/5e69770cd46be1763ff65bc4e05ea2fd1d9645b9

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/Intel/Intel|Intel]]：当前 affiliation + 公开职业邮箱域名双重证据。

<!-- END AUTO PERSON COMPANIES -->
