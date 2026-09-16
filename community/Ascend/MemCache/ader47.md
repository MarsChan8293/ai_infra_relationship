---
type: person
name: ader47
english_name: Feng Liu
aliases: ["@ader47", "F.Liu"]
current_affiliations: ["华为"]
public_email: liufeng248@huawei.com
email_affiliations:
  - "华为"
linked_companies:
  - "company/华为/华为"
projects: [MemCache, vLLM-Ascend]
roles: [Layerwise KV Pool Co-author]
areas: [kv-cache, layerwise-kv, gva, distributed-serving, ascend]
confidence: high
last_verified: "2026-09"
---
# ader47

项目：[[MemCache]] · [[vLLM-Ascend]]

## 身份核验
vLLM-Ascend 的公开提交同时出现 `ader47`、`F.Liu` / `Feng Liu` 与 `liufeng248@huawei.com`，并在同一提交中保留 `46866849+ader47@users.noreply.github.com`，因此可以可靠把该 handle 与 Feng Liu 及华为职业邮箱归并到同一开源身份。当前不据英文名进一步猜中文名或具体职级。

公开职业邮箱：`liufeng248@huawei.com`。

## vLLM-Ascend × MemCache
- 是 2026 年 layerwise KV Pool + MemCache backend 实现的直接共同贡献者。
- v0.23.0 回移 PR #11585 明确列出 `Co-authored-by: ader47`；相关 feature branch 也来自 ader47 fork。
- 该实现重点包括 MemCache GVA 分配、按层 batch copy、命中块跳过、lease 生命周期与错误处理等，将 KV 数据传输与 attention 计算进行受控重叠。

## 人物关系
- [[tyy0829]]：PR #11585 明确共同署名，属于有直接提交证据的开源协作。

## Sources
- https://github.com/vllm-project/vllm-ascend/pull/11444
- https://github.com/vllm-project/vllm-ascend/pull/11585
- https://github.com/vllm-project/vllm-ascend/commit/03a18ad6fd590b246d801ac0e77ec980cc74b831

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/华为/华为|华为]]：当前 affiliation + 公开职业邮箱域名双重证据。

<!-- END AUTO PERSON COMPANIES -->
