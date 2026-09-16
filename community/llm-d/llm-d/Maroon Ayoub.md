---
type: person
name: Maroon Ayoub
current_affiliations: ["Red Hat"]
schools:
  - "Technion - Israel Institute of Technology"
communities: [llm-d]
education: [Technion - Israel Institute of Technology]
roles: [Senior Principal Machine Learning Engineer, KV-Disaggregation SIG Lead, Agentic Inference SIG Lead, Inference Payload Processor SIG Lead]
areas: [kv-cache, distributed-inference, routing, agentic-inference]
last_verified: "2026-09"
relations:
  - '{"target":"community/llm-d/llm-d/Danny Harnik","type":["research-collaboration"],"confidence":"medium","evidence":["https://llm-d.ai/community/sigs","https://llm-d.ai/blog/p2p-kv-cache-sharing-llm-d","https://llm-d.ai/blog/serving-hybrid-models-at-scale-in-llm-d"]}'
  - '{"target":"community/llm-d/llm-d/Nili Guy","type":["paper-coauthor"],"confidence":"high","evidence":["https://llm-d.ai/community/sigs","https://llm-d.ai/blog/p2p-kv-cache-sharing-llm-d","https://llm-d.ai/blog/serving-hybrid-models-at-scale-in-llm-d"]}'
  - '{"target":"community/llm-d/llm-d/Carlos Costa","type":["paper-coauthor"],"confidence":"high","evidence":["https://llm-d.ai/community/sigs","https://llm-d.ai/blog/p2p-kv-cache-sharing-llm-d","https://llm-d.ai/blog/serving-hybrid-models-at-scale-in-llm-d"]}'
  - '{"target":"community/vllm-project/vLLM/Tyler Michael Smith","type":["coworker","technical-collaboration"],"project":"llm-d","company":"Red Hat","confidence":"high","evidence":["https://llm-d.ai/blog/kvcache-wins-you-can-see","https://llm-d.ai/blog/serving-glm-5-2-agentic-workloads-on-llm-d"]}'
---
# Maroon Ayoub

## 当前关系
- [[Red Hat]]：2026-06 与 2026-07 的 llm-d 官方技术文章均列为 Senior Principal Machine Learning Engineer, Red Hat。
- IBM Research：历史研究网络。IBM Research 人物页仍列其为 Research Scientist & Architect，但时间更晚的 llm-d 官方文章已明确其当前任职为 Red Hat，因此不再保留为 `current_affiliations`。
- [[llm-d]]：KV-Disaggregation SIG Lead，同时参与 Agentic Inference 与 Inference Payload Processor SIG 领导。

## 教育与学术关联
- [[Technion - Israel Institute of Technology]]：公开职业档案列出 2019–2025 教育经历；IBM Research 人物页另明确写到其在 Technion 指导 industry-linked student projects。

## 技术方向
KV cache 分离、P2P cache sharing、cache-aware routing、跨实例传输、distributed inference memory architecture，以及 agentic / payload-aware serving。

## 人物关系
- [[Danny Harnik]]：**llm-d KV-Disaggregation SIG 共同负责人 + 早期 IBM 研究网络**。两人共同负责 distributed KV cache、prefix sharing、remote storage 与 vLLM KVConnector 集成；Danny 当前属 IBM，Maroon 2026 年已转入 Red Hat，因此当前不是同事。
- [[Nili Guy]]：**Router ↔ KV-Disaggregation 跨 SIG 协作**。2026 P2P KV cache sharing 工作共同署名，连接 endpoint routing 与 KV movement。
- [[community/vllm-project/vLLM/Tyler Michael Smith|Tyler Michael Smith]]：**Red Hat inference engineering 同事 + llm-d 技术协作者**。两人共同署名 2025 KV-cache aware scheduling 工作；2026 GLM-5.2 agentic-serving 官方文章再次共同署名，并同时列为 Red Hat inference engineering。Tyler 负责 vLLM / PD-disaggregation，Maroon 负责 KV-disaggregation / agentic serving，这条边连接了两个核心推理子系统。
- [[Carlos Costa]]：**llm-d agentic serving 跨公司协作**。2026-07 GLM-5.2 agentic workload 文章共同署名，连接 Red Hat serving engineering 与 IBM project leadership。

## 相关社区
[[vLLM]] · [[LMCache]] · [[NIXL]] · [[Mooncake]]

## Sources
- https://www.linkedin.com/in/v-maroon
- https://research.ibm.com/people/maroon-ayoub
- https://llm-d.ai/community/sigs
- https://llm-d.ai/blog/p2p-kv-cache-sharing-llm-d
- https://llm-d.ai/blog/kvcache-wins-you-can-see
- https://llm-d.ai/blog/serving-hybrid-models-at-scale-in-llm-d
- https://llm-d.ai/blog/serving-glm-5-2-agentic-workloads-on-llm-d
