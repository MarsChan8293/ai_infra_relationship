---
type: person
name: 尹沛骐
english_name: Peiqi Yin
aliases: ["Peiqi Yin", "Yin Peiqi"]
current_affiliations: ["香港中文大学"]
schools:
  - "香港中文大学"
projects: ["vLLM-Omni", "LiveServe"]
areas: [multimodal-serving, distributed-serving, realtime-serving, sparse-attention, disaggregation]
roles: [PhD Candidate, vLLM-Omni First Author]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"university/香港中文大学/James Cheng","type":["advisor"],"confidence":"high","evidence":["https://yinpeiqi.github.io/"]}'
---
# 尹沛骐（Peiqi Yin）

## 当前身份
截至 2026-09，尹沛骐是香港中文大学 CSE 博士候选人，个人主页给出的博士阶段为 2022-08 至 2026-10，导师为 [[university/香港中文大学/James Cheng|James Cheng]]。

## AI Infra 主线
- [[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]]：2026 论文第一作者。该系统把复杂 any-to-any multimodal model 拆成 stage graph，并通过独立 stage serving、动态资源分配与统一 connector 做 fully-disaggregated serving。
- [[university/香港中文大学/LiveServe|LiveServe]]：共同第一作者；面向 realtime omni-modal LLM 的 interaction-aware serving，聚焦 barge-in、first-audio latency、KV eviction 与 preload。
- 个人主页还公开列出 SparseServe / Progressive Sparse Attention 等 LLM serving 工作，说明其研究主线并不只限于 multimodal model support，而是持续围绕 serving systems 与资源调度展开。

## 学术网络
- [[university/香港中文大学/James Cheng|James Cheng]]：博士导师；两人共同参与 vLLM-Omni、LiveServe 等 systems 工作。


## 学校关联
- [[university/香港中文大学/香港中文大学|香港中文大学]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://yinpeiqi.github.io/
- https://arxiv.org/abs/2602.02204
- https://arxiv.org/abs/2606.22983
