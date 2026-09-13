---
type: company
name: Meta
---
# Meta

## 公司简介
Meta 是同时拥有 Llama foundation models、PyTorch 软件栈和超大规模推荐/AI infrastructure 的平台公司。在本图谱中，它是模型、compiler/runtime 与开源 inference engine 三条线交汇的重要产业节点。

## 关联社区与人物
[[vLLM]] · [[SGLang]] · Llama · PyTorch

[[李卓翰 Zhuohan Li]] · [[Lu Fang]] · [[Ye Charlotte Qi]] · [[Chen Zhang]] · [[Richard Zou]]

## 图谱中的连接
- [[Chen Zhang]]：大规模 RL system / RL inference；同时参与 vLLM、Jenga、PrefillOnly 等 serving systems 工作，并形成清华 → Berkeley → Meta 的人才桥。
- [[Richard Zou]]：PyTorch compiler / torch.compile，通过 vLLM compile integration 连接编译器与 serving stack。
- Llama 模型生态是 vLLM/SGLang 等引擎的重要 workload，但模型支持不自动推断人物直接合作。
