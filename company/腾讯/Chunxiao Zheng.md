---
type: person
name: Chunxiao Zheng
aliases: ["chunxiaozheng", "idellzheng"]
current_affiliations: ["腾讯"]
public_email: idellzheng@tencent.com
communities: [LMCache, SGLang]
roles: [LMCache Committer, Component Owner, UnifiedRadixCache Integration Author]
linked_companies:
  - "company/腾讯/腾讯"
areas: [kv-cache, distributed-kv-cache, memory-management, storage-backend, gds, p2p, sglang-integration, unified-radix-cache]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/腾讯/Baolong Mao","type":["coworker","open-source-collaboration","technical-collaboration"],"project":"LMCache","company":"腾讯","start":"2025","confidence":"high","evidence":["https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md","https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS","https://blog.lmcache.ai/en/2026/01/21/p2p-1/"]}'
---
# Chunxiao Zheng

当前：[[company/腾讯/腾讯|腾讯（Tencent）]]；LMCache Committer、核心组件 CODEOWNER。

## LMCache 角色
LMCache 官方 `MAINTAINERS.md` 将 Chunxiao Zheng 列为 Tencent Committer。当前 `CODEOWNERS` 显示其负责或共同负责 cache controller、memory management、distributed / L2、GDS memory manager、storage backend 与 MooncakeStore connector 等路径。

2026-01 LMCache 官方 P2P 文章明确记录 Tencent 与 LMCache 团队在两个月内共同实现 production-grade multi-node CPU P2P KV sharing，Chunxiao Zheng 与 Baolong Mao 作为 Tencent 作者出现。

公开 LMCache commit 将 `chunxiaozheng` / `idellzheng` 与 `idellzheng@tencent.com` 直接对应，因此腾讯组织关系现在也有职业邮箱这一层独立证据。

## SGLang UnifiedRadixCache 桥
截至 2026-09-16，Chunxiao Zheng 同时发起：
- LMCache #4828：为 MP 模式加入 Unified LMCache Radix Cache connector；
- SGLang #38652：在 `UnifiedRadixCache` 中接入 LMCache external KV-cache backend。

两个 PR 当前均为 open，因此这里记录为 **active cross-project integration**，而不是已发布能力。其公开验证覆盖 shared-prefix reuse、warm path、flush/cold fallback、GSM8K accuracy 和 filesystem-hit benchmark。

## 人物关系
- [[company/腾讯/Baolong Mao|Baolong Mao]]：腾讯同事 + LMCache P2P / distributed cache 直接工程协作者，关系由官方 maintainer、CODEOWNERS 和 P2P 技术文章共同支撑。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://blog.lmcache.ai/en/2026/01/21/p2p-1/
- https://github.com/LMCache/LMCache/commit/b679822880b7b368ab4261c13ca0c35c5ff5739f
- https://github.com/LMCache/LMCache/pull/4828
- https://github.com/sgl-project/sglang/pull/38652

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/腾讯/腾讯|腾讯]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
