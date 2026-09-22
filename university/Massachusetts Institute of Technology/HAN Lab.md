---
type: research-institution
name: "HAN Lab"
aliases: ["MIT HAN Lab"]
organization: "Massachusetts Institute of Technology"
linked_people: []
people:
  - "university/Massachusetts Institute of Technology/Song Han"
  - "university/Massachusetts Institute of Technology/Qinghao Hu"
  - "university/Massachusetts Institute of Technology/Junxian Guo"
  - "university/Massachusetts Institute of Technology/Shang Yang"
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

## 关键人物

- [[university/Massachusetts Institute of Technology/HAN Lab/Song Han|Song Han]]：Principal Investigator；MIT EECS Associate Professor。
- [[university/Massachusetts Institute of Technology/HAN Lab/Qinghao Hu|Qinghao Hu]]：Postdoctoral researcher；公开方向直接覆盖 foundation-model training / serving / scheduling。
- [[university/Massachusetts Institute of Technology/HAN Lab/Junxian Guo|Junxian Guo]]：PhD student；研究 long-context model systems / algorithms。
- [[university/Massachusetts Institute of Technology/HAN Lab/Xingyang Li|Xingyang Li]]：PhD student；研究 generative AI 的 low-bit quantization / sparsity acceleration。

本轮优先选当前 team 页面仍列为活跃成员、且与 inference optimization / systems 直接相关的人物；不把历史 alumni 混入 current key_people coverage。

## 当前关键人物

- [[university/Massachusetts Institute of Technology/Song Han|Song Han]]：Principal Investigator；MIT EECS Associate Professor。
- [[university/Massachusetts Institute of Technology/Qinghao Hu|Qinghao Hu]]：Postdoctoral；研究 foundation-model training、serving 与 scheduling。
- [[university/Massachusetts Institute of Technology/Junxian Guo|Junxian Guo]]：PhD student；研究 long-context model systems / algorithms。
- [[university/Massachusetts Institute of Technology/Shang Yang|Shang Yang]]：PhD student；QServe、LServe、AWQ 等高效 LLM systems 项目核心作者之一。

以上身份来自 HAN Lab 当前 Team 页面；这里只记录实验室 affiliation 与公开研究方向，不从共同实验室身份自动推断任意两人的直接合作。

## Sources
- https://hanlab.mit.edu/
- https://hanlab.mit.edu/team
- https://hanlab.mit.edu/songhan
