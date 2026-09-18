---
type: research-institution
name: "HAN Lab"
aliases: ["MIT HAN Lab"]
organization: "Massachusetts Institute of Technology"
linked_people: []
areas: [efficient-ai, llm-serving, gpu-systems, quantization, sparse-attention, long-context-inference]
website: https://hanlab.mit.edu/
country: "USA"
city: "Cambridge, MA"
last_verified: "2026-09"
---
# HAN Lab

MIT HAN Lab 由 Song Han 领导，核心特色是 algorithm-system-hardware co-design。对于本仓库，它最有价值的不是一般“高效 AI”标签，而是已经延伸成完整的 LLM inference optimization 链条。

## AI Infra 主线

- **SmoothQuant / AWQ**：低比特量化与部署基础。
- **QServe**：W4A8KV4 的大规模 LLM serving。
- **StreamingLLM**：固定内存预算下的长序列生成。
- **Quest / DuoAttention / LServe**：围绕 long-context KV cache、稀疏 attention 与 serving 的系统优化。
- HAN Lab 当前成员中，Jiaming Tang、Junxian Guo、Qinghao Hu 等公开研究方向直接涉及 foundation-model serving、long-context systems 与 scheduling。

这些项目和 SGLang、vLLM、TensorRT-LLM 等工程生态存在明确集成或采用关系；集成关系本身不被提升为共同治理关系。

## Sources
- https://hanlab.mit.edu/
- https://hanlab.mit.edu/team
- https://hanlab.mit.edu/songhan
