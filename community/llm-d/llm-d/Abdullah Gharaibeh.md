---
type: person
name: Abdullah Gharaibeh
current_affiliations: ["Google"]
schools:
  - "University of British Columbia"
communities: [llm-d]
education: [University of British Columbia]
roles: [Senior Staff Software Engineer, Project Leadership, Router SIG Lead]
areas: [llm-routing, scheduling, kv-cache-affinity, kubernetes]
last_verified: "2026-09"
relations:
  - '{"target":"community/llm-d/llm-d/Nili Guy","type":["coworker"],"confidence":"high","evidence":["https://llm-d.ai/community/sigs","https://llm-d.ai/blog/predicted-latency-based-scheduling-for-llms","https://llm-d.ai/blog/sticky-until-saturated-token-aware-routing"]}'
  - '{"target":"community/llm-d/llm-d/Vita Bortnikov","type":["coworker"],"confidence":"high","evidence":["https://llm-d.ai/community/sigs","https://llm-d.ai/blog/predicted-latency-based-scheduling-for-llms","https://llm-d.ai/blog/sticky-until-saturated-token-aware-routing"]}'
  - '{"target":"community/llm-d/llm-d/Clayton Coleman","type":["coworker"],"confidence":"high","evidence":["https://llm-d.ai/community/sigs","https://llm-d.ai/blog/predicted-latency-based-scheduling-for-llms","https://llm-d.ai/blog/sticky-until-saturated-token-aware-routing"]}'
---
# Abdullah Gharaibeh

## 当前关系
- [[Google]]：截至 2026-08，llm-d 官方技术文章列为 Senior Staff Software Engineer, Google。
- [[llm-d]]：项目治理网络成员、Router SIG Lead。

## 教育经历
- [[University of British Columbia]]：Electrical and Computer Engineering 博士；其 UBC 个人主页同时记录了此前在 UBC 完成的 Master of Applied Science。

## 技术方向
负责/推动 LLM 请求路由与 scheduling，包括 KV-cache affinity、token load、predicted-latency scheduling，以及 Kubernetes Gateway API / Inference Gateway 与推理后端之间的调度路径。2026-03 的 predicted-latency scheduling 与 2026-08 的 token-aware routing 均有其直接作者署名。

## 人物关系
- [[Nili Guy]]、[[Vita Bortnikov]]：**llm-d Router SIG 共同负责人；截至 2026-09**。三人共同负责 routing、load balancing、traffic management；这是明确的社区技术领导协作，不推断公司同事关系。Nili / Vita 属 IBM 网络，Abdullah 属 Google。
- [[Clayton Coleman]]：**Google 同公司 + llm-d 技术领导网络**。Clayton 是 llm-d founding / project leadership 网络人物，Abdullah 当前负责 Router SIG；公开来源不足以确认直属汇报关系。
- [[Robert Shaw]]、[[Carlos Costa]]：**llm-d 跨公司项目治理/技术上下游协作**。Router 是 production serving well-lit paths 的核心组件，与项目级 architecture / disaggregation 路线持续交叉。

## Sources
- https://people.ece.ubc.ca/abdullah
- https://www.linkedin.com/in/abdullah-gharaibeh-422996b
- https://llm-d.ai/community/sigs
- https://llm-d.ai/blog/predicted-latency-based-scheduling-for-llms
- https://llm-d.ai/blog/sticky-until-saturated-token-aware-routing
