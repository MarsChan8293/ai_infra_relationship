---
type: project
name: InfiniLM
layer: inference-engine
open_source: true
repository: https://github.com/InfiniTensor/InfiniLM
areas: [llm-inference, paged-attention, cuda-graph, tensor-parallel, pipeline-parallel, moe, quantization, heterogeneous-compute]
people:
  - "university/启元实验室/王豪杰 Haojie Wang"
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
  - "university/启元实验室/潘泽众 Zezhong Pan"
  - "community/InfiniTensor/zhangyue207"
  - "community/InfiniTensor/baominghelly"
  - "community/InfiniTensor/qinyiqun"
  - "community/InfiniTensor/wooway777"
last_verified: "2026-09"
---
# InfiniLM

InfiniLM 是当前 InfiniTensor / 九源生态中更明确的现代大模型推理框架节点。它建立在 [[InfiniCore]] 及其 runtime / operator / communication 能力之上，而原始 [[InfiniTensor]] 仓库继续承担旧引擎与研究验证语义。

## 推理能力
公开 README / PR 路线覆盖：
- Tensor Parallel / Pipeline Parallel；
- Paged Attention、FlashAttention、CUDA Graph；
- MoE inference / Expert Parallel；
- quantized inference；
- 多模态与 OpenAI-compatible serving 路线；
- NVIDIA、Ascend、MetaX、Moore Threads、Hygon、Kunlun 等多后端。

## 高价值人物边
- [[university/启元实验室/王豪杰 Haojie Wang|王豪杰]]：推进 KTransformers CPU-GPU MoE offload / FusedMoE 与 out-of-tree model plugin。
- [[university/启元实验室/潘泽众 Zezhong Pan|潘泽众]]：Kimi-K3、cross-node PP + intra-node TP、Qwen3-next 等。
- [[qinyiqun]]：MoE inference / Expert Parallel、Qwen MoE、quant / Marlin 等。
- [[wooway777]]：多硬件 graph、GLM / Qwen / multimodal 与 serving 适配。
- [[baominghelly]]：Ascend TP/HCCL 与 graph-safe operator 路径。

## Sources
- https://github.com/InfiniTensor/InfiniLM
- https://github.com/InfiniTensor/InfiniLM/pull/444
- https://github.com/InfiniTensor/InfiniLM/pull/548
- https://github.com/InfiniTensor/InfiniLM/pull/522
- https://github.com/InfiniTensor/InfiniLM/pull/574
