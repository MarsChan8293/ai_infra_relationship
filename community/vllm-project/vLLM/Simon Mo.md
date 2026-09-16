---
type: person
name: Simon Mo
current_affiliations: ["Inferact"]
schools:
  - "UC Berkeley"
communities: [vLLM, "Ray Serve"]
linked_companies:
  - "company/Inferact/Inferact"
areas: [serving-systems, api, benchmarking, observability, community-governance]
roles: [Cofounder, CEO, Core Maintainer]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/Inferact/Woosuk Kwon","type":["cofounder","coworker","open-source-collaboration"],"project":"vLLM","company":"Inferact","confidence":"high","evidence":["https://inferact.ai/","https://docs.vllm.ai/en/latest/governance/process/","https://vllm.ai/events/vllm-conference/2026"]}'
  - '{"target":"community/vllm-project/vLLM/游凯超 Kaichao You","type":["cofounder","coworker","open-source-collaboration"],"project":"vLLM","company":"Inferact","confidence":"high","evidence":["https://inferact.ai/","https://docs.vllm.ai/en/latest/governance/process/","https://vllm.ai/blog/2026-07-16-keeping-vllm-production-quality"]}'
  - '{"target":"community/vllm-project/vLLM/Roger Wang","type":["coworker","open-source-collaboration"],"project":"vLLM","company":"Inferact","confidence":"high","evidence":["https://inferact.ai/","https://docs.vllm.ai/en/latest/governance/process/","https://vllm.ai/blog/2026-07-16-keeping-vllm-production-quality"]}'
  - '{"target":"community/vllm-project/vLLM/Nick Hill","type":["coworker","open-source-collaboration"],"project":"vLLM","company":"Inferact","confidence":"high","evidence":["https://docs.vllm.ai/en/latest/governance/process/","https://vllm.ai/blog/2026-07-16-keeping-vllm-production-quality","https://www.linkedin.com/posts/nickhillprofile_im-excited-to-share-that-ive-joined-inferact-activity-7420171751466143744-S6_-"]}'
  - '{"target":"community/vllm-project/vLLM/李卓翰 Zhuohan Li","type":["open-source-collaboration","research-collaboration"],"confidence":"high","evidence":["https://sky.cs.berkeley.edu/events/dissertation-talk-building-open-source-inference-serving-systems-simon-mo/","https://inferact.ai/","https://docs.vllm.ai/en/latest/governance/process/"]}'
  - '{"target":"company/Inferact/Ion Stoica","type":["advisor"],"end":"2026","confidence":"high","evidence":["https://www2.eecs.berkeley.edu/Pubs/TechRpts/2026/EECS-2026-206.html","https://sky.cs.berkeley.edu/events/dissertation-talk-building-open-source-inference-serving-systems-simon-mo/"]}'
  - '{"target":"company/Inferact/Joseph Gonzalez","type":["advisor"],"end":"2026","confidence":"high","evidence":["https://www2.eecs.berkeley.edu/Pubs/TechRpts/2026/EECS-2026-206.html","https://sky.cs.berkeley.edu/events/dissertation-talk-building-open-source-inference-serving-systems-simon-mo/"]}'
---
# Simon Mo

社区：[[vLLM]] · [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]]
当前：[[Inferact]] 联合创始人、CEO

## 教育经历
- [[UC Berkeley]]：计算机博士；2026 dissertation《Building Open Source Inference Serving Systems》，导师 [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]]、[[company/Inferact/Ion Stoica|Ion Stoica]]

## 工作经历
- [[university/UC Berkeley/UC Berkeley|UC Berkeley RISELab]] / Sky Computing Lab：学生研究者，长期研究 serving systems
- [[Anyscale]]：Software Engineer，参与 [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]]
- Character.AI：serving systems 相关经历
- [[Inferact]]：联合创始人、CEO，2025–至今

## 社区贡献
vLLM Lead Maintainer；公开资料显示自 2023 起 co-lead vLLM community，负责 API entrypoints、batch serving、benchmark、observability 与社区治理。其早期 Ray Serve 经历提供了 `Ray Serve → vLLM → Inferact` 的 serving systems 职业/技术桥。

## 人物关系
- [[company/Inferact/Ion Stoica|Ion Stoica]]：**UC Berkeley 博士共同导师**。Simon 的 2026 Berkeley technical report 与 Sky Lab dissertation talk 均明确列 Ion Stoica 为 advisor，因此结构化为 `advisor`，不是泛化的 mentor-network。
- [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]]：**UC Berkeley 博士共同导师**。Simon 的 2026 Berkeley technical report 与 Sky Lab dissertation talk 均明确列 Joseph Gonzalez 为 advisor，因此结构化为 `advisor`。
- [[Inferact/Woosuk Kwon|Woosuk Kwon]]：**Berkeley 系统研究合作者 + vLLM 社区共同领导者 + Inferact 联合创始人**。2023–2025 共同建设 vLLM；2025–至今在 [[Inferact]] 共事，Simon 任 CEO、Woosuk 任 CTO。
- [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超（Kaichao You）]]：**vLLM 共同维护者 + Inferact 联合创始人**。游凯超自 2024 起参与 vLLM，并在 2024 UC Berkeley Sky Lab 访问期间进入同一 Berkeley/vLLM 技术圈；2025–至今两人在 [[Inferact]] 共事，分别任 CEO 与 Chief Scientist。
- [[community/vllm-project/vLLM/李卓翰 Zhuohan Li|李卓翰（Zhuohan Li）]]：**vLLM 早期共同建设者 / Lead Maintainer**。两人在 2023 起共同参与 vLLM 的 Berkeley 开源 serving 系统环境；李卓翰 2024 后离开 Berkeley，当前在 [[Meta]]，因此关系是跨公司开源协作而非当前同事。
- [[community/vllm-project/vLLM/Roger Wang|Roger Wang]]：**vLLM 社区协作 + Inferact founding team 同事**。2025–至今同属 [[Inferact]]，Roger 偏 multimodality / benchmark，Simon 偏 API / serving / governance。
- [[community/vllm-project/vLLM/Nick Hill|Nick Hill]]：**Inferact 同事 + vLLM 共同维护者**。截至 2026-09 两人在 Inferact/vLLM 共事；Nick 偏 scheduler/distributed/KV Connector，Simon 偏 API/benchmark/community。Nick 加入 Inferact 的精确月份公开未确认。

## Sources
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2026/EECS-2026-206.html
- https://sky.cs.berkeley.edu/events/dissertation-talk-building-open-source-inference-serving-systems-simon-mo/
- https://inferact.ai/
- https://docs.vllm.ai/en/latest/governance/process/
- https://vllm.ai/blog/2026-07-16-keeping-vllm-production-quality

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/Inferact/Inferact|Inferact]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
