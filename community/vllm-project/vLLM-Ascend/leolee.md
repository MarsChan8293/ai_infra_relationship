---
type: person
name: leolee
aliases: ["@leolee", "li1how"]
public_email: yihao.li@huawei.com
projects: [vLLM-Ascend]
roles: [KV Pool Contributor, PCP Contributor, Speculative Decoding Contributor]
areas: [kv-cache, kv-pooling, pcp, pd-disaggregation, speculative-decoding, dspark, ascend]
confidence: high
last_verified: "2026-09"
---
# leolee

项目：[[vLLM-Ascend]]

## 身份与组织证据
2026-09 的多个 vLLM-Ascend 提交稳定使用 `leolee`，并直接以 `yihao.li@huawei.com` Signed-off-by；这里据此记录公开职业邮箱，组织关系由邮箱域名机制自动生成，不据邮箱反推中文实名或职级。

## vLLM-Ascend
- 推进 **MRV2 PCP + KV cache pooling**，将 KV pool 适配到 PCP replicated KV cache，并支持兼容 PCP 配置间的缓存共享。
- 推进 **PCP + P/D disaggregation** 的 KV transfer，使 prefill PCP 能与 decode 侧不同并行配置协同。
- 在 DeepSeek-V4 的 DSA PCP、MTP / DSpark speculative decoding、ACLGraph replay 等路径持续贡献。

## 图谱价值
这是 `context parallelism -> KV cache pooling -> P/D disaggregation -> speculative decoding` 的交叉节点，适合作为 vLLM-Ascend KV 数据路径继续 BFS 的高价值入口。

## Sources
- https://github.com/vllm-project/vllm-ascend/commit/92995fbbf30301b6f4b702fdb375a888608c1e20
- https://github.com/vllm-project/vllm-ascend/commit/84b7f79573bbdc7f97ee7f74f659e26393dd4eea
- https://github.com/vllm-project/vllm-ascend/commit/00ce2f026cb69a1fd1ac9c5f54b99602ff7c9566
