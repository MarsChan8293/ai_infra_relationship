---
type: person
name: Zhengfei He
aliases: ["zhengfeihe", "zhengfei.he", "@zhengfeihe"]
communities: [LMCache]
roles: [Distributed L2 Component Owner, Storage Backend Owner]
areas: [kv-cache, distributed-kv-cache, eviction, storage-backend, valkey, nixl, multiprocess, observability, cli, rust]
confidence: high
last_verified: "2026-09"
relations:
  - '{"target":"company/腾讯/Baolong Mao","type":["open-source-collaboration"],"project":"LMCache","confidence":"high","evidence":["https://github.com/LMCache/LMCache/commit/83692b9bd8f7f77a24f0030770caedb6e54e1b3f"]}'
---
# Zhengfei He（zhengfeihe）

当前 LMCache `CODEOWNERS` 将 Zhengfei He 放在 distributed eviction、L2 adapters、storage backend、CLI、docs 与 Rust 等路径。

## LMCache 角色
2026 年主要贡献包括：
- Valkey L2 adapter（standalone + cluster）；
- NIXL close race / deadlock 修复；
- MP transfer timing 分解到 gather / DMA / reserve 阶段；
- runtime profiling / flame graph 工具；
- IPC segment lifecycle 与 build / CI 修复。

因此他是当前 `distributed/L2 → storage backend → MP observability` 路线中比较强的 owner 节点。

## 人物关系
- [[company/腾讯/Baolong Mao|Baolong Mao]]：#4621 的 LMCache build/CI commit 有直接 co-author 证据，记录为开源协作关系。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/LMCache/LMCache/commit/cd9a0ad5325c7d52c825ed17aac6185d5c520e44
- https://github.com/LMCache/LMCache/commit/c828516e2cbee42525b8e1fda975533d5405e304
- https://github.com/LMCache/LMCache/commit/ba5c9d6ed6d7169b4a92aa9db61bfe76cd8db133
