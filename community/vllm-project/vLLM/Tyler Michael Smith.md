---
type: person
name: Tyler Michael Smith
current_affiliations: ["Red Hat"]
schools:
  - "University of Texas at Austin"
communities: [vLLM, llm-d]
roles: [Chief Architect, Core Maintainer, PD-Disaggregation SIG Lead]
areas: [distributed-inference, kernels, disaggregation, moe, collectives]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"community/vllm-project/vLLM/Robert Shaw","type":["coworker","open-source-collaboration","technical-collaboration"],"project":"llm-d","company":"Red Hat","start":"2025","confidence":"high","evidence":["https://llm-d.ai/community/sigs","https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1"]}'
  - '{"target":"community/vllm-project/vLLM/Michael Goin","type":["coworker","open-source-collaboration","technical-collaboration"],"project":"vLLM","confidence":"high","evidence":["https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community","https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1"]}'
  - '{"target":"community/llm-d/llm-d/Maroon Ayoub","type":["coworker","technical-collaboration"],"project":"llm-d","company":"Red Hat","confidence":"high","evidence":["https://llm-d.ai/blog/kvcache-wins-you-can-see","https://llm-d.ai/blog/serving-glm-5-2-agentic-workloads-on-llm-d"]}'
---
# Tyler Michael Smith

社区：[[vLLM]] · [[llm-d]]
当前：[[Red Hat]] Chief Architect, Inference Engineering（llm-d 官方作者资料，截至 2026-09）

## 教育经历
- [[University of Texas at Austin]]：计算机博士，研究高性能稠密线性代数、microkernels、并行与数据移动下界

## 工作经历
- [[Neural Magic]]：推理性能、编译与稀疏模型系统
- [[Red Hat]]：Neural Magic 于 2025 年初并入 Red Hat 后继续从事大规模 LLM inference；当前公开资料将其列为 Chief Architect, Inference Engineering。

## 社区贡献
- [[vLLM]]：Project Lead，负责 CUDA kernels、Fused MoE、collectives、distributed 与 disaggregated inference。
- [[llm-d]]：PD-Disaggregation SIG Lead，与 [[Robert Shaw]] 共同负责 prefill/decode separation、跨实例通信、异构资源利用与 distributed serving。

## 人物关系
- [[Robert Shaw]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 共同维护者 + llm-d PD-Disaggregation SIG 共同负责人**。至少在 2025-02，两人共同被 Red Hat 官方列为 DeepSeek MLA / FP8 vLLM 优化贡献者；截至 2026-09 又共同领导 llm-d PD-Disaggregation 技术域。这里有明确 SIG 共同负责人和共同工程产出证据。
- [[Michael Goin]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 性能工程合作者**。2024 FP8 支持与 2025 DeepSeek-R1 优化均有官方共同署名，技术协作早于 Red Hat 收购并在 2025 后延续。
- [[community/llm-d/llm-d/Maroon Ayoub|Maroon Ayoub]]：**Red Hat inference engineering 同事 + llm-d 技术协作者**。两人共同署名 2025 KV-cache aware scheduling 工作；2026 GLM-5.2 agentic-serving 官方文章再次共同署名，并同时列为 Red Hat inference engineering。Tyler 负责 vLLM / PD-disaggregation，Maroon 负责 KV-disaggregation / agentic serving，因此这条强边连接了 engine/performance、PD 与 KV/agentic serving 网络。
- [[Lucas Wilkinson]]：**候选 GPU kernel 协作**。2025 DeepSeek-R1 优化中 Tyler 与 Lucas 均被官方 credit，信号较强，但本轮先不把同一贡献团队直接升级为强人物边，留待核验具体共同模块 / PR / review。
- [[Matthew Bonanni]]：**候选 Red Hat / vLLM 关系，暂缓结构化**。同属 Red Hat/vLLM inference engineering 网络不足以自动推断直接强关系。
- [[Wentao Ye]]：**候选 Red Hat / vLLM 关系，暂缓结构化**。两人在 MoE / distributed performance 邻域有交叉，但需要 pair-specific 工程证据后再结构化。

## Sources
- https://llm-d.ai/community/sigs
- https://llm-d.ai/blog/authors
- https://llm-d.ai/blog/kvcache-wins-you-can-see
- https://llm-d.ai/blog/serving-glm-5-2-agentic-workloads-on-llm-d
- https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community
- https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1
- https://www.redhat.com/en/blog/enhancing-deepseek-models-mla-and-fp8-optimizations-vllm
- https://www.redhat.com/en/blog/bringing-nemotron-models-red-hat-ai-factory-nvidia
