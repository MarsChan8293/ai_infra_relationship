---
type: person
name: 程翊华
english_name: Yihua Cheng
aliases: [Yihua Cheng, 程翊华]
current_affiliations: ["TensorMesh"]
schools:
  - "University of Chicago"
  - "北京大学"
communities: [LMCache, vLLM]
roles: [Co-Founder, CTO]
linked_companies:
  - "company/TensorMesh/TensorMesh"
areas: ["kv-cache","llm-inference"]
last_verified: "2026-09"
relations:
  - '{"target":"company/TensorMesh/杜昆泰 Kuntai Du","type":["cofounder","research-collaboration"],"confidence":"high","evidence":["https://ceca.pku.edu.cn/en/people_/alumni_undergrad_/index.htm","https://apostac.github.io/about.html"]}'
  - '{"target":"company/TensorMesh/Junchen Jiang","type":["advisor","paper-coauthor","research-collaboration"],"project":"LMCache","end":"2025","confidence":"high","evidence":["https://knowledge.uchicago.edu/records/d037a-62j32","https://people.cs.uchicago.edu/~junchenj/"]}'
  - '{"target":"company/TensorMesh/Junchen Jiang","type":["cofounder"],"company":"TensorMesh","start":"2025","confidence":"high","evidence":["https://www.tensormesh.ai/about","https://www.tensormesh.ai/team-members/yihua-cheng","https://www.tensormesh.ai/team-members/junchen-jiang"]}'
---
# 程翊华（Yihua Cheng）

[[TensorMesh]] 联合创始人、CTO，[[LMCache]] 核心开发者，同时参与 [[vLLM]] 的 KV Connector、offloading 与缓存生态建设。

## 教育经历
- [[北京大学]]：本科，2020；北京大学高能效计算与应用中心校友页明确列为“程翊华 Yihua Cheng”
- [[University of Chicago]]：计算机博士；导师 [[Junchen Jiang]]

## 研究与工作经历
- 研究方向覆盖实时视频流、数据流系统、KV cache compression / streaming 与 LLM serving
- [[LMCache]]：KV cache offloading、connector、分层缓存与传输
- [[TensorMesh]]：联合创始人、CTO
- [[vLLM]]：KV Connector / offloading 生态的重要贡献者

## 人物关系
- [[TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：**共同创业 + 长期研究/开源合作者**。两人都来自 University of Chicago 的 LLM systems / cache 研究网络，并共同参与 [[LMCache]]；截至 2026-09 均为 [[TensorMesh]] 联合创始团队成员。公开来源没有给出公司成立的精确月份，因此只记录到年份/当前状态。
- [[Junchen Jiang]]：**University of Chicago 博士导师 + TensorMesh 联合创始人**。UChicago dissertation 记录明确把 Junchen Jiang 列为程翊华的 advisor；两人长期合著系统论文，并把 KV cache / distributed inference 研究延伸到 [[LMCache]] 与 TensorMesh。公司官网同时将 Junchen 列为 CEO/Co-Founder、程翊华列为 CTO/Co-Founder，因此学术指导与共同创业分成两条 typed relation，避免把时间语义混在一个标签里。
- [[community/vllm-project/vLLM/Nick Hill|Nick Hill]]：**候选 KV Connector 关联，暂缓结构化**。两人在 vLLM KV Connector / distributed serving 邻域均有贡献，但当前公开材料不足以证明可单独归因的直接人物关系；Nick 属 Inferact、程翊华属 TensorMesh。
- [[community/vllm-project/vLLM/Robert Shaw|Robert Shaw]]：**候选 offloading / disaggregation 关联，暂缓结构化**。两人在 vLLM KV Connector、offloading 与 disaggregated serving 方向存在模块邻接，但当前证据不足以建立强人物边；Robert 属 Red Hat、程翊华属 TensorMesh。

## Sources
- https://ceca.pku.edu.cn/en/people_/alumni_undergrad_/index.htm
- https://apostac.github.io/about.html
- https://knowledge.uchicago.edu/records/d037a-62j32
- https://people.cs.uchicago.edu/~junchenj/
- https://www.tensormesh.ai/about
- https://www.tensormesh.ai/team-members/yihua-cheng
- https://www.tensormesh.ai/team-members/junchen-jiang

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/TensorMesh/TensorMesh|TensorMesh]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
