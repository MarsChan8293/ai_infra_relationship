---
type: project
name: DeepInfer
status: active
maturity: unknown
code_availability: public
layer: inference-engine
repository: https://github.com/deepseek-ai/DeepInfer
docs: https://github.com/deepseek-ai/DeepInfer/blob/main/README.md
companies:
  - "深度求索"
hardware:
  - nvidia
  - ascend
areas:
  - deepseek-v4.1-flash
  - llm-inference
  - attention-data-parallel
  - context-parallelism
  - expert-parallelism
  - expert-load-balancing
  - speculative-decoding
  - swa-bounded-replay
  - asynchronous-scheduling
  - deterministic-sampling
  - structured-output
integrations:
  - FlashMLA
  - DeepGEMM
  - DeepEP
  - TileKernels
  - DeepSelect
last_verified: "2026-10"
---
# DeepInfer

## 项目简介

DeepInfer 是 [[company/深度求索/深度求索|深度求索]] 开源的 DeepSeek 模型专用高性能推理引擎。官方表示其内部生产版支撑大规模推理服务；但 **2026-10 当前公开代码主要提供离线推理与构建完整 serving 所需的核心执行能力**，并不代表完整在线系统已经对外开放。

- GitHub：https://github.com/deepseek-ai/DeepInfer
- 许可证：Apache-2.0。
- 当前支持模型：**DeepSeek-V4.1-Flash**；官方离线示例默认权重为 `deepseek-ai/DeepSeek-V4.1-Flash-1017`。
- 官方明确支持硬件：**NVIDIA SM100 GPU** 与 **Huawei Ascend 950 NPU**。不能由平台大类推断现已支持 H800、RTX Pro 5000 或 910B/910C。
- 依赖：Linux、GCC >=13、Python 3.12、NVIDIA CUDA 13 或 Ascend CANN 9.2。

## 核心技术

1. **Attention DP / Balanced CP、MoE EP + EPLB**：面向长上下文和 MoE 负载的分布式执行。
2. **DSpark / confidence-scheduled verification**：使用 draft token 和置信度调度验证，`DEEPINFER_ENABLE_MTP_VARLEN=1` 可启用变长 MTP，`DEEPINFER_USE_NEXTN_DECODE` 控制最大 draft 长度（默认 5）。
3. **Decoder SWA bounded replay**：只重放受限的序列后缀以降低 Decoder Prefill 成本。V4.1 默认建议 `DEEPINFER_YOCO_PREFILL_TRUNCATION_MODE=compact`、`DEEPINFER_YOCO_PREFILL_KEEP_TOKENS=140`；保留长度必须覆盖 SWA Window 与最大回溯长度。
4. **异步调度**：CPU batch scheduling 与设备执行重叠，默认开启。
5. **正确性与输出约束**：支持 batch-invariant inference、确定性采样（这两项仅 NVIDIA）及 Regex / JSON Schema / EBNF 输出约束。

相关概念：[[concept/inference/decoding/Speculative Decoding|Speculative Decoding]]、[[concept/inference/parallelism/Expert Parallelism|Expert Parallelism]]、[[concept/inference/parallelism/Context Parallelism|Context Parallelism]]、[[concept/inference/parallelism/Data Parallelism|Data Parallelism]]。复用现有 Concept，避免创建重复分类。

## 生态与上游

- **技术基底**：官方 README 承认该引擎最初主要基于 [[community/vllm-project/vLLM/vLLM|vLLM]]，并受 [[community/sgl-project/SGLang/SGLang|SGLang]]、[[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] 启发；是设计/代码继承，非这几个项目的运行时直接 integration。
- **实际内核/通信组件**：官方列明 [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]]、[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]]、[[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]]、[[community/deepseek-ai/DeepSeek-Infra/TileKernels|TileKernels]]、[[community/deepseek-ai/DeepSeek-Infra/DeepSelect|DeepSelect]] 及自研 TileLang kernels。
- **Speculative 技术线**：[[community/deepseek-ai/DeepSpec/DeepSpec|DeepSpec]] 覆盖 DSpark/DFlash draft-model 工具；DeepInfer 在 inference runtime 实现 DSpark 与 confidence scheduling。技术上下游关系不必然构成直接安装依赖。
- **API 协议邻接层**：[[community/deepseek-ai/DeepSeek-Infra/deepseek-recipe|deepseek-recipe]] 负责 DeepSeek API/prompt/response 编解码；公开证据不足以把它和 DeepInfer 视为已打包完成的 HTTP 服务。
- **所属系统生态**：[[community/deepseek-ai/DeepSeek-Infra/DeepSeek-Infra|DeepSeek Infra]]；DeepInfer 以独立 inference-engine 节点收录。

## 当前开源边界

官方明确列出：构成一个完整在线推理服务仍需要**单独的 KV Cache 系统**、**VE/Prefill/Decode 分离式服务集成**（引擎内部多数必需功能已实现）、以及 **Prefill 和 Decode DP 副本的负载均衡**。

所以目前不能把 DeepInfer 直接等同于具有现成 OpenAI API、KV 卸载、PD 控制面及全栈运维能力的 [[vLLM]]、[[SGLang]] 或 [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]]。也不能把 Ascend 950 支持外推至 910C。

## Benchmark 与正确性验证

官方 Prefill Benchmark 为 **4 张 SM100 GPU**，Decode Benchmark 为 **64 张 SM100 GPU**（各自在一个 scale-up domain）。示例 Decode 吞吐公式 `avg_SPS × decode_num_requests × (1 + nextn) / cp` 采用**全部 draft 接受**的口径，因此还需实测有效 output tokens/s、acceptance rate、TTFT、TPOT。

公开测试有 PPL baseline、结构化输出检测与 YoCo mask/compact 等价性验证（teacher-forcing logprob / Top-K 比较），适用于研究专用引擎自优化后的 correctness gate。

## Sources

- https://github.com/deepseek-ai/DeepInfer
- https://github.com/deepseek-ai/DeepInfer/blob/main/README.md
- https://github.com/deepseek-ai/DeepInfer/blob/main/examples/README.md
- https://github.com/deepseek-ai/DeepInfer/blob/main/examples/yoco/README.md
