---
type: person
name: weiguihua2
aliases: ["@weiguihua2"]
public_email: weiguihua2@huawei.com
projects: [vLLM-Ascend]
roles: [DCP Contributor, Speculative Decoding Contributor]
areas: [dcp, pcp, speculative-decoding, dspark, sfa, mla, kv-cache, ascend]
confidence: high
last_verified: "2026-09"
---
# weiguihua2

项目：[[vLLM-Ascend]]

## 身份与组织证据
2026-09 的 vLLM-Ascend 提交同时出现个人 QQ 邮箱与 `weiguihua2@huawei.com`。按照仓库规则，canonical `public_email` 优先使用公开职业邮箱，个人邮箱只保留为提交证据，不作为默认联系方式。

## vLLM-Ascend
- 推进 **SFA PCP + DCP** 组合并行，处理 KV cache slot mapping、block table 与 metadata builder。
- 推进 **Kimi K3 DSpark + DCP**，包括 query slot mapping、draft query metadata、MTP causal mask 与 graph metadata。
- 处理 **DCP + P/D disaggregated recomputation** 的 shape mismatch，并推进 MLA + DCP + speculation 的 chunk-prefill tiling。

## 图谱价值
连接 `context parallelism -> KV metadata -> speculative decoding -> P/D disaggregation`，与 leolee 的 PCP/KV pooling 路线形成互补的 context-parallel 工程支路。

## Sources
- https://github.com/vllm-project/vllm-ascend/commit/3d84be3ce62206223b39204722649b66c21033dd
- https://github.com/vllm-project/vllm-ascend/commit/9b2871baeaf2149f3f8126f5fd2bc9ff2fb0958a
- https://github.com/vllm-project/vllm-ascend/commit/cdad5a32e0a0cc0232ae29ded29636162f4fb690
- https://github.com/vllm-project/vllm-ascend/commit/cab37196df6366edd0eb38a0e35f15c9dc1e4f15
