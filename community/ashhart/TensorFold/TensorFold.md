---
type: project
name: TensorFold
linked_concepts:
  - "concept/inference/decoding/Multi-token Prediction"
  - "concept/inference/kv-cache/Prefix Caching"
  - "concept/inference/decoding/Speculative Decoding"
status: active
linked_people: []
open_source: true
license: MIT
repository: https://github.com/ashhart/TensorFold
last_verified: "2026-09"
layer: inference-engine
areas:
  - "local-inference"
  - "openai-compatible-api"
  - "model-specific-kernels"
  - "speculative-decoding"
  - "multi-token-prediction"
  - "tensor-parallel"
  - "prompt-caching"
  - "weight-only-quantization"
hardware:
  - "apple-silicon"
  - "nvidia"
linked_companies: []
code_availability: public
---
# TensorFold

## 项目定位

TensorFold 是开源 LLM inference runtime / model server，面向 Apple Silicon 与 NVIDIA GPU 提供 OpenAI-compatible serving。它不是以“最大模型覆盖面”为首要目标，而是为有限的模型族实现专用 Metal / CUDA kernel，并围绕 speculative decoding、MTP、lane batching 和 exact decoding 做深度优化。

因此在本图谱中将它归到 **Inference Engine**，但更准确的标签是 **specialized inference runtime**：与 [[community/vllm-project/vLLM/vLLM|vLLM]]、[[community/sgl-project/SGLang/SGLang|SGLang]] 同处推理执行层，但 TensorFold 当前的模型/硬件覆盖更窄，模型族与 kernel 的绑定更强。

## GitHub

https://github.com/ashhart/TensorFold

MIT License。

## 核心架构

TensorFold 根据 checkpoint 的 `config.json` 选择对应 model family 的实现。每个模型族拥有自己的 kernel / forward / draft 路径：

- Apple Silicon：MLX + Metal kernel；
- NVIDIA GPU：PyTorch / Triton / CUDA kernel；
- HTTP 层提供 `/v1/chat/completions` OpenAI-compatible endpoint；
- speculative decoding 支持 MTP head 与独立 drafter；
- 通过 row-exact / lane decoding 约束，使 drafted decoding 与自身 serial decoding 保持 byte-identical；
- prompt cache 按固定 token 网格缓存会话前缀，并可将部分 prefix snapshot 跨进程重启保存。

这条路线更接近“针对模型族做定制执行引擎”，而不是单套通用 backend 覆盖大量 Hugging Face architecture。

## 当前模型覆盖

截至 2026-09，README 重点列出的已构建/测试模型包括：

- NVIDIA Nemotron 3.5 Lightning 30B-A3B；
- Qwen3.8-27B + DFlash2 drafter；
- Qwen3.8 Flash Next + MTP；
- GLM-5.3-Flash：CUDA / 双 DGX Spark 路径，部分权重格式属于 experimental 支持。

模型支持不是“任意 Hugging Face 模型直接兼容”。`tensorfold info MODEL` 会根据 `config.json` 判断当前 engine 是否能读取该 checkpoint；没有 recipe 的模型/权重格式会直接拒绝。

## 多机与并行

NVIDIA CUDA 路径支持 `--tp 2 --rank R --master HOST`，目前 README 展示的是两台 DGX Spark、一机一卡，通过 NCCL 和直连网络共同切分一个模型。rank 0 提供 HTTP 服务。

这意味着 TensorFold 已具有基础 Tensor Parallel 多机推理能力，但它当前不是像 vLLM / SGLang 那样面向大规模多节点、多并行维度、通用模型 serving 的分布式引擎。

## M × N × K 配置管理视角

这里按仓库常用的 **M（模型）× N（硬件）× K（推理引擎版本）** 视角记录：

### M：模型

TensorFold 的模型兼容关系是强约束的。model family、checkpoint conversion、quantization group size、MTP head / drafter 与 kernel 实现之间存在明确绑定。

例如同属 Qwen3.8，不同模型会走不同 family/kernel；某些模型需要指定 4-bit group size 或附带 MTP head，不能只按“architecture 名称相同”视为兼容。

因此 TensorFold 的 M 管理特点是：

`model family -> checkpoint format -> quantization layout -> draft/MTP artifact -> kernel recipe`

而不是单纯 `model name -> engine`。

### N：硬件

当前官方路径主要是：

`Apple Silicon -> MLX/Metal`

`NVIDIA GPU -> PyTorch/Triton/CUDA`

其中部分优化还依赖具体 Apple GPU generation，CUDA 多机路径目前以 DGX Spark 为重点示例。

### K：引擎 / 依赖版本

TensorFold 对运行时版本有较强兼容约束。例如 README 记录了特定 MLX 版本会影响 Nemotron draft correctness check；启动时会验证 drafted rows 是否与 serial path 一致，不满足时会关闭 drafts 而保留正确性。

因此 K 不能只记录 TensorFold 自身版本，还至少应联合记录：

- TensorFold version；
- MLX / PyTorch / Triton / CUDA version；
- model family kernel recipe version；
- checkpoint conversion / quantization format；
- drafter / MTP artifact。

从配置管理角度看，TensorFold 是一个很典型的“**M × N × K 强耦合**”案例。

## Ascend / 昇腾支持

截至 2026-09，官方仓库和 README 没有给出 Ascend / CANN / torch-npu / vLLM-Ascend 类 backend。当前公开 backend 是 MLX/Metal 与 CUDA。

因此本图谱暂不标记 Ascend 支持。若后续出现 Ascend backend，应单独核验其 model-family kernel、量化格式和 speculative decoding 路径，而不能仅因为 Python 层可运行就视为完整支持。

## 与现有项目的关系

- [[community/vllm-project/vLLM/vLLM|vLLM]]：同属 inference engine；vLLM 更强调通用模型生态、调度、KV 管理与生产 serving，TensorFold 更强调少量模型族的专用 kernel / exact speculative decoding。
- [[community/sgl-project/SGLang/SGLang|SGLang]]：同属高性能 LLM serving/runtime；SGLang 覆盖面和分布式 serving 能力更广，TensorFold 当前更偏模型特化优化。
- [[community/ollama/Ollama/Ollama|Ollama]]：都覆盖 Apple Silicon 本地推理，但 Ollama 更靠近本地模型平台、模型管理与开发者体验；TensorFold 更靠近执行引擎与 kernel 优化。
- [[concept/inference/decoding/Multi-token Prediction|Multi-token Prediction]] / [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]]：TensorFold 的性能路线核心。
- [[concept/inference/parallelism/Tensor Parallelism|Tensor Parallelism]]：CUDA 路径当前公开支持两节点 / 两 GPU 的 TP=2。

## Sources

- https://github.com/ashhart/TensorFold
- https://github.com/ashhart/TensorFold/blob/main/README.md
- https://github.com/ashhart/TensorFold/tree/main/docs/recipes

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/decoding/Multi-token Prediction|Multi-token Prediction]]
- [[concept/inference/kv-cache/Prefix Caching|Prefix Caching]]
- [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]]

<!-- END AUTO PROJECT CONCEPTS -->
