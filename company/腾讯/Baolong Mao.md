---
type: person
name: Baolong Mao
aliases: ["Baolong Ma", "maobaolong", "baoloongmao"]
current_affiliations: ["腾讯"]
public_email: baoloongmao@tencent.com
communities: [LMCache, vLLM]
roles: [LMCache Committer, Component Owner]
linked_companies:
  - "company/腾讯/腾讯"
areas: [kv-cache, distributed-kv-cache, storage-backend, platform, vllm-integration, p2p]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/腾讯/Chunxiao Zheng","type":["coworker","open-source-collaboration","technical-collaboration"],"project":"LMCache","company":"腾讯","start":"2025","confidence":"high","evidence":["https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md","https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS","https://blog.lmcache.ai/en/2026/01/21/p2p-1/"]}'
  - '{"target":"community/LMCache/LMCache/Samm Shen","type":["open-source-collaboration","technical-collaboration","community-maintainer"],"project":"LMCache","start":"2025","confidence":"high","evidence":["https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS","https://blog.lmcache.ai/en/2026/01/21/p2p-1/"]}'
---
# Baolong Mao

当前：[[company/腾讯/腾讯|腾讯（Tencent）]]；LMCache Committer、核心组件 CODEOWNER。

## LMCache / vLLM 位置
LMCache 官方 `MAINTAINERS.md` 将其列为 Tencent Committer。当前 `CODEOWNERS` 显示 `@maobaolong` 负责或共同负责 cache controller、offload server、distributed / L2、platform、lookup client、storage backends，以及 `lmcache/integration/vllm/` 等核心路径。

他同时直接向 vLLM 提交 LMCache KV Connector / multiprocess 相关修复，包括 2026 年 prefix cache、MLA lookup、LMCacheMPConnector 等路径，因此这里记录为 LMCache ↔ vLLM 的直接开源桥，而不是仅凭两个项目邻接推断。

公开 LMCache commit 使用 `baoloongmao@tencent.com`，因此现在也能通过职业邮箱机制独立验证腾讯组织关联。

## Mooncake 连接
LMCache 仓库中的 `mooncake_store_l2_adapter.py`、`mooncake_lookup_client.py` 等路径由 `@maobaolong` 直接 ownership，说明他负责 LMCache 侧 Mooncake Store 集成。这里记录为技术集成上下文，不等价于 Mooncake 项目 maintainer 身份。

## 人物关系
- [[company/腾讯/Chunxiao Zheng|Chunxiao Zheng]]：腾讯同事 + LMCache P2P / distributed cache 直接工程协作者。2026-01 LMCache 官方文章明确记录两位 Tencent 作者参与 multi-node CPU P2P KV sharing 的 productionization。
- [[community/LMCache/LMCache/Samm Shen|Samuel Shen]]：LMCache 维护与 P2P 工程协作者；二人在同一官方 P2P 文章和 CODEOWNERS 路径中有直接技术交集，但分属 Tencent / TensorMesh，不写成同事关系。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://blog.lmcache.ai/en/2026/01/21/p2p-1/
- https://github.com/LMCache/LMCache/commit/5e69770cd46be1763ff65bc4e05ea2fd1d9645b9
- https://github.com/vllm-project/vllm/commit/b58e082d95ffad57a6a9aaffa8b76c862b3bbcf3
- https://github.com/vllm-project/vllm/commit/b2f749dc97d59e3eb808499e88a29663f2143aa1

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/腾讯/腾讯|腾讯]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
