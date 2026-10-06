---
type: concept
name: Speculative Decoding
aliases:
  - Speculative Sampling
  - Spec Decode
  - 投机解码
  - 投机推理
domain: inference
topic: decoding
related_concepts:
  - "N-gram Speculation"
  - "Self-Speculative Decoding"
  - "Multi-token Prediction"
projects:
  - "vLLM"
  - "SGLang"
  - "Splash"
  - "SpecForge"
  - "Speculators"
  - "TorchSpec"
  - "Transformers"
  - "LoopSpec"
  - "Lookahead Decoding"
  - "DeepSpec"
  - "TensorRT-LLM"
  - "TensorFold"
  - "OpenVINO GenAI"
last_verified: 2026-10
---

# Speculative Decoding

## 一句话定义

Speculative Decoding 先用更便宜的方法一次提出多个候选 token，再由目标模型并行验证，从而减少“每个输出 token 都必须单独跑一次昂贵 target forward”的串行瓶颈。

## 解决的问题

普通 autoregressive decode 每轮只确认一个 token，GPU 在低到中等 QPS、memory-bound 场景下常无法充分利用算力。投机解码把多步串行 decode 变成“快速 proposal + 一次批量 verification”。

## 核心机制

一个迭代通常包含：

1. proposer 生成若干 draft token。
2. target model 一次计算这些候选位置的 logits。
3. 按验证规则接受连续正确候选，并在第一个不接受的位置恢复到 target 分布。
4. 从新的已确认前缀继续下一轮。

关键性能变量是 proposer 成本、一次提出多少 token、acceptance rate 和 verification 开销。

## 主要细分

- **Draft model + target verification**：最常见路线，独立或专门训练的 proposer 先生成候选，再由 target 批量验证；EAGLE、DFlash、DSpark 等属于这一工程族，不再单独建立中间 taxonomy 节点。
- [[N-gram Speculation]]：从 prompt / 已有 token 模式中直接提出候选，无需额外神经网络。
- [[Self-Speculative Decoding]]：使用 target 模型自身的较便宜路径产生 draft。
- [[Multi-token Prediction]]：模型原生预测多个未来 token，可作为 speculative proposer。
- Lookahead/Jacobi 等路线同样属于“廉价 proposal + target verification/acceptance”的并行解码族。

## 代价与适用边界

投机解码不是“候选越多越快”。当 proposer 太慢、acceptance rate 太低、batch/QPS 很高或 target verification 本身成为瓶颈时，收益会下降甚至为负。

## 项目实现

Serving/runtime 侧，[[community/vllm-project/vLLM/vLLM|vLLM]]、[[community/sgl-project/SGLang/SGLang|SGLang]]、[[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]]、[[community/huggingface/Transformers/Transformers|Transformers]]、[[community/ashhart/TensorFold/TensorFold|TensorFold]]、[[company/Intel/OpenVINO GenAI|OpenVINO GenAI]] 和 [[community/incoai/Splash/Splash|Splash]] 都公开支持 speculative / assisted decoding 路径。

训练与专用优化侧，[[community/sgl-project/SpecForge/SpecForge|SpecForge]]、[[community/vllm-project/Speculators/Speculators|Speculators]]、[[community/lightseekorg/TorchSpec/TorchSpec|TorchSpec]]、[[community/deepseek-ai/DeepSpec/DeepSpec|DeepSpec]] 覆盖 draft-model training / deployment；[[community/kaist-flexml-lab/LoopSpec/LoopSpec|LoopSpec]] 提供 self-speculation；[[community/lmsys-org/Lookahead-Decoding/Lookahead-Decoding|Lookahead Decoding]] 以 Jacobi/n-gram trajectory 做 exact parallel decoding。

## Sources

- https://docs.vllm.ai/en/latest/features/spec_decode/
- https://docs.vllm.ai/projects/speculators/en/stable/user_guide/getting_started/
- https://docs.sglang.ai/SpecForge/
