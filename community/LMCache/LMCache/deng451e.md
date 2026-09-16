---
type: person
name: deng451e
aliases: ["@deng451e"]
communities: [LMCache]
roles: [vLLM Integration Owner, CacheBlend Contributor]
areas: [kv-cache, cacheblend, vllm-integration, sparse-prefetch, observability, multimodal-inference]
confidence: high
last_verified: "2026-09"
---
# deng451e

当前 LMCache `CODEOWNERS` 将 `@deng451e` 放在 vLLM integration、tests、getting-started / developer docs、CI / packaging 等路径；2026-09 仍持续推进 CacheBlend 主线。

## LMCache 角色
近期提交集中在 CacheBlend 的模块化重构、sparse-prefetch read lock、fused-KV / RoPE geometry 与 blend-rate correctness。尤其 MiniMax-M3 mixed KV group 的 fused packing 修复直接关系到 CacheBlend 是否真正命中并减少重算。

因此该节点是 `CacheBlend → vLLM integration → sparse KV reuse` 的高价值工程节点。当前没有足够一手证据确认真实姓名或公司，保留 GitHub handle 作为 canonical name。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/LMCache/LMCache/commit/2a07cc2e94411355fc86d2ea1215139731406645
- https://github.com/LMCache/LMCache/commit/c6965abba3fc5a1436bdc6c839b13871877444b7
- https://github.com/LMCache/LMCache/commit/d589e72cd5fa0357a42aceb6ce739b637d775d9e
