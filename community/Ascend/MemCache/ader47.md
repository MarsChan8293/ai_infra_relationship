---
type: person
name: ader47
aliases: ["@ader47"]
projects: [MemCache, vLLM-Ascend]
roles: [Layerwise KV Pool Co-author]
areas: [kv-cache, layerwise-kv, gva, distributed-serving, ascend]
confidence: project-credit
last_verified: "2026-09"
---
# ader47

项目：[[MemCache]] · [[vLLM-Ascend]]

## vLLM-Ascend × MemCache
- 是 2026 年 layerwise KV Pool + MemCache backend 实现的直接共同贡献者。
- v0.23.0 回移 PR #11585 明确列出 `Co-authored-by: ader47`；相关 feature branch 也来自 ader47 fork。
- 该实现重点包括 MemCache GVA 分配、按层 batch copy、命中块跳过、lease 生命周期与错误处理等，将 KV 数据传输与 attention 计算进行受控重叠。

## 人物关系
- [[tyy0829]]：PR #11585 明确共同署名，属于有直接提交证据的开源协作。

## Sources
- https://github.com/vllm-project/vllm-ascend/pull/11444
- https://github.com/vllm-project/vllm-ascend/pull/11585
