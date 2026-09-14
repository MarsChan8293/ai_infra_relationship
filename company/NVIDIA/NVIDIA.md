---
type: company
name: NVIDIA
projects: [Dynamo, NIXL, TensorRT-LLM, Triton Inference Server, HAMi, TokenSpeed]
---
# NVIDIA

## 公司简介
NVIDIA 是当前 AI 计算基础设施最核心的 GPU、互联与软件平台厂商，CUDA、NCCL、TensorRT 等构成大量模型训练与推理系统的底座。其 AI Infra 版图已经从芯片/kernel 扩展到 LLM runtime、data movement 与集群级 inference orchestration。

## 主要贡献的社区项目
- [[community/Dynamo/Dynamo|Dynamo]]：**发起 / 主导**，数据中心级 distributed inference orchestration。
- [[community/NIXL/NIXL|NIXL]]：**发起 / 主导**，inference data movement / memory abstraction。
- [[community/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]]：**公司主导维护**的 LLM runtime / kernel stack。
- [[community/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]]：**公司主导维护**的 production inference server。
- [[community/HAMi/HAMi|HAMi]]：**跨公司 maintainer / accelerator ecosystem contributor**，不是 NVIDIA 独占项目。
- [[community/TokenSpeed/TokenSpeed|TokenSpeed]]：LightSeek Foundation 治理下的**共同创建/工程协作方**，并通过 Dynamo 提供 day-0 backend 支持。

## 图谱中的连接
[[TensorRT-LLM]] · [[Triton Inference Server]] · [[Dynamo]] · [[NIXL]] · [[FlashInfer]] · [[vLLM]] · [[SGLang]]。其中 TensorRT-LLM/Triton 是 NVIDIA 主导项目，Dynamo/NIXL 在 ai-dynamo 组织开放开发；与 vLLM/SGLang 的关系则更多是生态适配与合作，需按人物证据单独建边。
