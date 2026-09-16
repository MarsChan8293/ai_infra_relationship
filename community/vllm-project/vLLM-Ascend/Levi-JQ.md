---
type: person
name: Levi-JQ
aliases: ["@Levi-JQ"]
public_email: yujinqi2@huawei.com
projects: [vLLM-Ascend]
roles: [DSpark Contributor, Communication Performance Contributor]
areas: [speculative-decoding, dspark, kimi-k3, tensor-parallelism, moe, communication, ascend]
confidence: high
last_verified: "2026-09"
---
# Levi-JQ

项目：[[vLLM-Ascend]]

## 身份与组织证据
vLLM-Ascend 的公开提交长期稳定使用 `Levi-JQ <yujinqi2@huawei.com>`。因此记录公开职业邮箱，并由邮箱域名机制生成华为组织关联；不据邮箱 local-part 推断实名。

## vLLM-Ascend
- 在 Kimi K3 **DSpark speculative decoding** 路线中优化 Markov head，将其改为 replicated group，移除 TP 下每个 draft step 的高延迟 collective。
- 将 `context_proj` 改为 tensor-parallel sharding，减少 decode 阶段每 rank 的 HBM 权重读取压力。
- 优化 MoE prepare/finalize 的 padding / communication kernel 开销，并长期参与 FlashComm / layer sharding 路径。

## 图谱价值
连接 `speculative decoding -> tensor parallelism -> MoE communication -> HBM bandwidth`，是 vLLM-Ascend 性能工程层的高价值节点。

## Sources
- https://github.com/vllm-project/vllm-ascend/commit/ce9e24a28131b59c6df27470ac42aee742a711ad
- https://github.com/vllm-project/vllm-ascend/commit/b246529ec3ccb754e141d10018d70643a646992a
- https://github.com/vllm-project/vllm-ascend/commit/616f872747bdc89de9b1c410b4b30888cd834705
