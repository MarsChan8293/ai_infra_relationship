---
type: person
name: chengruiqi
aliases: ["chengruiqi (C)", "@chengruiqi"]
public_email: c00913489@china.huawei.com
email_affiliations:
  - "华为"
linked_companies:
  - "company/华为/华为"
projects: [vLLM-Ascend, MemCache]
roles: [KVPP Contributor, MemCache Integration Contributor]
areas: [kv-cache, kvpp, kv-pooling, memcache, pcp, pd-disaggregation, ascend]
confidence: high
last_verified: "2026-09"
---
# chengruiqi

项目：[[vLLM-Ascend]] · [[community/Ascend/MemCache/MemCache|MemCache]]

## 身份与组织证据
vLLM-Ascend 公开提交使用 `chengruiqi (C)`，并直接出现 `c00913489@china.huawei.com`。`china.huawei.com` 由仓库规则继承 `huawei.com -> 华为`；这里只确认公开职业邮箱对应的组织关联，不猜中文实名或职级。

## KVPP × MemCache
- 主导/直接贡献 **KV layer parallelism (KVPP)**：把目标层 KV cache 分布到 TP ranks，通过 full-layer broadcast 扩大可用 KV 容量。
- 后续将 KVPP 扩展到 **P/D disaggregation、PCP 与 KV pooling**。
- 该实现明确使用 `AscendStoreConnector` + **MemCache backend**，并验证 MTP、prefix caching 与多前缀 pooled prefill workload，是 MemCache 与 vLLM-Ascend 当前非常直接的工程桥。

## 图谱价值
这是 `MemCache storage backend -> AscendStoreConnector -> KV pooling -> KVPP/PCP -> P/D serving` 的强集成节点，比仅共享华为 affiliation 更有价值。

## Sources
- https://github.com/vllm-project/vllm-ascend/commit/45b74a6904a2ea7b90c4f441da014003984099d2
- https://github.com/vllm-project/vllm-ascend/commit/cafae11ebbb0f7b8c7818b7ba7db0ed9382bbd82

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/华为/华为|华为]]：公开职业邮箱域名证据；表示组织关联，不单独证明当前任职。

<!-- END AUTO PERSON COMPANIES -->
