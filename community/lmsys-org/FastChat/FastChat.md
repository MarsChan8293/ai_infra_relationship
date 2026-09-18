---
type: project
name: FastChat
companies: []
company_relation: community-led
layer: llm-serving
open_source: true
repository: https://github.com/lm-sys/FastChat
areas: [llm-serving, openai-compatible-api, model-serving, distributed-serving, evaluation]
people:
  - "community/sgl-project/SGLang/郑连民 Lianmin Zheng"
  - "company/RadixArk/盛颖 Ying Sheng"
  - "community/vllm-project/vLLM/李卓翰 Zhuohan Li"
  - "university/UC Berkeley/Shuo Yang"
  - "company/Inferact/Joseph Gonzalez"
  - "company/Inferact/Ion Stoica"
governance: LMSYS project
last_verified: "2026-09"
---
# FastChat

FastChat 是 LMSYS 早期的大模型训练、服务与评测平台，也是 Vicuna / Chatbot Arena 早期生态的重要运行底座。对本图谱而言，最有价值的部分是它把 Berkeley distributed systems / model-serving 人才网络连接到后来的 SGLang 与 vLLM 时代。

## AI Infra 价值
- 提供多模型 serving、controller / worker 架构以及 OpenAI-compatible API server。
- 早期把研究模型部署、在线对话服务与 evaluation 工具放进同一开源栈，为后续更专门化的高性能 serving runtime 提供了人才和工程经验。
- Shuo Yang / Siyuan Zhuang 的官方文章进一步扩展了 OpenAI-compatible server 路径，说明 FastChat 不只是模型 demo，而是可被上层应用直接调用的 serving interface。

## 技术与人才血缘
- [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|Lianmin Zheng]] 的 Berkeley 系统路线从 Alpa / FastChat 延续到 [[community/sgl-project/SGLang/SGLang|SGLang]]。
- [[company/Inferact/Ion Stoica|Ion Stoica]] 与 [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]] 位于这条 Berkeley systems / model-serving 指导网络上。
- FastChat 与后来的 SGLang / vLLM 不应简单写成同一项目或直接替代关系，但它是 LMSYS serving 生态的重要前史节点。

## Sources
- https://github.com/lm-sys/FastChat
- https://www.lmsys.org/projects/
- https://www.lmsys.org/blog/2023-03-30-vicuna/
- https://www.lmsys.org/blog/2023-11-04-openai-api/
