---
type: person
name: Bingyang Wu
current_affiliations: ["Peking University"]
schools:
  - "北京大学"
public_email: bingyangwu@pku.edu.cn
projects: [LoongServe]
areas: [llm-serving, distributed-systems, moe-serving, scheduling, long-context]
roles: [PhD Candidate]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://bingyangwu.github.io/","https://arxiv.org/abs/2404.09526","https://interestinglsy.github.io/"]}'
  - '{"target":"university/北京大学/Xin Jin","type":["advisor","research-collaboration"],"confidence":"high","evidence":["https://bingyangwu.github.io/"]}'
---
# Bingyang Wu

北京大学计算机学院博士生，导师为 [[university/北京大学/Xin Jin|Xin Jin]]，研究集中于 machine learning systems、distributed systems 与 LLM serving。

## 与刘胜与的关系
[[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与（Shengyu Liu）]] 与 Bingyang Wu 共同参与 LoongServe、FastServe、RLHFuse 等多项系统研究。LoongServe 中两人直接共同构建 elastic sequence parallelism 路线，连接 long-context serving、KV-cache migration 与动态并行。

## 后续技术路线
Bingyang Wu 后续继续推进 MoE serving 与通信/调度方向，包括 ExpertPlex、UltraEP 等。这条支线与刘胜与进入 DeepSeek 后的 DeepGEMM / FlashMLA kernel 路线在 MoE inference stack 上具有明显技术邻接，但不把邻接自动写成直接协作。

## Sources
- https://bingyangwu.github.io/
- https://arxiv.org/abs/2404.09526
- https://interestinglsy.github.io/
