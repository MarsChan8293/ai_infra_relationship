---
type: person
name: Danny Harnik
current_affiliations: ["IBM"]
schools:
  - "UCLA"
communities: [llm-d]
roles: [Senior Technical Staff Member, KV-Disaggregation SIG Lead]
areas: [kv-cache, cloud-storage, distributed-storage, disaggregated-inference]
last_verified: "2026-09"
relations:
  - '{"target":"community/llm-d/llm-d/Maroon Ayoub","type":["research-collaboration"],"confidence":"medium","evidence":["https://llm-d.ai/community/sigs","https://research.ibm.com/people/danny-harnik","https://llm-d.ai/blog/native-kv-cache-offloading-to-any-file-system-with-llm-d"]}'
---
# Danny Harnik

## 当前关系
- [[IBM]]：IBM Research 官方人物页列为 Senior Technical Staff Member / Cloud Storage，长期研究 cloud storage 与大规模存储系统。
- [[llm-d]]：KV-Disaggregation SIG Lead。

## 教育与研究经历
- Weizmann Institute of Science：密码学博士，2006；导师 Moni Naor。
- 博士后阶段曾在 Technion 与 UCLA/IPAM。
- IBM Haifa Labs：长期从事 cloud storage、compression/deduplication 与 large-scale storage systems，近年将存储系统经验延伸到 LLM KV cache / distributed inference。

## 技术方向
KV cache、memory hierarchy、远端缓存与共享存储、filesystem offloading、hybrid-model cache layout、distributed inference。2026 llm-d filesystem KV offloading 与 hybrid-model serving 工作均有直接作者署名。

## 人物关系
- [[Maroon Ayoub]]：**llm-d KV-Disaggregation SIG 共同负责人 + IBM 历史研究网络**。二人共同负责 distributed KV cache、prefix sharing 与 remote storage 路线；Maroon 2026 年已转入 Red Hat，因此当前不是同事。
- [[Nili Guy]]：**IBM / llm-d Router ↔ KV cache 邻接协作网络**。两条 SIG 在 cache-aware routing 与 P2P KV sharing 上技术耦合，但人物直接共同项目需按具体论文/文章核验。

## 相关社区
[[vLLM]] · [[LMCache]] · [[NIXL]] · [[Mooncake]]


## 学校关联
- [[university/UCLA/UCLA|UCLA]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://llm-d.ai/community/sigs
- https://research.ibm.com/people/danny-harnik
- https://llm-d.ai/blog/native-kv-cache-offloading-to-any-file-system-with-llm-d
- https://llm-d.ai/blog/serving-hybrid-models-at-scale-in-llm-d
