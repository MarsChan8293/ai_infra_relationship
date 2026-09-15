---
type: person
name: Nick Hill
current_affiliations: ["Inferact"]
schools:
  - "University of Warwick"
communities: [vLLM]
areas: [scheduler, distributed-inference, kv-cache, api-server, ci]
roles: [Founding Engineer, Core Maintainer]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/Inferact/Woosuk Kwon","type":["coworker","open-source-collaboration"],"project":"vLLM","company":"Inferact","confidence":"high","evidence":["https://docs.vllm.ai/en/latest/governance/process/","https://vllm.ai/blog/2026-07-16-keeping-vllm-production-quality","https://www.linkedin.com/posts/nickhillprofile_im-excited-to-share-that-ive-joined-inferact-activity-7420171751466143744-S6_-"]}'
  - '{"target":"community/vllm-project/vLLM/Simon Mo","type":["coworker","open-source-collaboration"],"project":"vLLM","company":"Inferact","confidence":"high","evidence":["https://docs.vllm.ai/en/latest/governance/process/","https://vllm.ai/blog/2026-07-16-keeping-vllm-production-quality","https://www.linkedin.com/posts/nickhillprofile_im-excited-to-share-that-ive-joined-inferact-activity-7420171751466143744-S6_-"]}'
  - '{"target":"community/vllm-project/vLLM/Robert Shaw","type":["open-source-collaboration","technical-collaboration"],"project":"vLLM","confidence":"high","evidence":["https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1","https://docs.vllm.ai/en/latest/governance/committers/"]}'
---
# Nick Hill

社区：[[vLLM]]
当前：[[Inferact]] 核心工程团队

## 教育经历
- [[University of Warwick]]：本科，一等荣誉

## 工作经历
- 长期从事系统软件和推理基础设施
- 曾参与 Red Hat 侧 vLLM 工程
- [[Inferact]]：核心工程团队；截至 2026-09 为 vLLM Project Lead

## 社区贡献
Project Lead，负责 scheduler、AsyncLLM、distributed、API server、KV Connector 与 CI。

## 人物关系
- [[Inferact/Woosuk Kwon|Woosuk Kwon]]：**Inferact 同事 + vLLM 共同维护者**。截至 2026-09 同属 Inferact；Woosuk 负责 engine core / attention，Nick 负责 scheduler、distributed、API/KV Connector。Nick 加入 Inferact 的精确月份公开来源未确认。
- [[community/vllm-project/vLLM/Simon Mo|Simon Mo]]：**Inferact 同事 + vLLM 共同维护者**。截至 2026-09 同属 Inferact；Simon 偏 API / serving / governance，Nick 偏 scheduler / distributed / KV Connector。
- [[community/vllm-project/vLLM/Robert Shaw|Robert Shaw]]：**vLLM distributed / disaggregated serving 开源协作者**。截至 2026-09 两人分属 Inferact 与 [[Red Hat]]；2025 DeepSeek-R1 优化工作由 Red Hat 官方同时署名二人，并且两人在 distributed / KV Connector 维护边界持续交叉，因此保留结构化边。
- [[TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：**候选 KV Connector / LMCache 关联，暂缓结构化**。两人在同一 vLLM KV Connector 与 cache integration 邻域出现，但当前证据不足以单独证明直接协作。
- [[TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]：**候选 KV Connector / offloading 关联，暂缓结构化**。两人在同一模块邻域出现，但当前证据不足以建立强人物边。

## Sources
- https://docs.vllm.ai/en/latest/governance/process/
- https://docs.vllm.ai/en/latest/governance/committers/
- https://vllm.ai/events/vllm-conference/2026
- https://vllm.ai/blog/2026-07-16-keeping-vllm-production-quality
- https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1
- https://www.linkedin.com/in/nickhillprofile
- https://www.linkedin.com/posts/nickhillprofile_im-excited-to-share-that-ive-joined-inferact-activity-7420171751466143744-S6_-
