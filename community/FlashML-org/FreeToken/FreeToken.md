---
type: project
name: FreeToken
organization: FlashML
repository: https://github.com/FlashML-org/FreeToken
open_source: true
layer: edge-moe-serving
areas: [llm-inference, moe-inference, edge-inference, cpu-gpu-coexecution, expert-caching, kv-cache, memory-management, quantization, cuda-kernels, agent-serving]
linked_people:
  - "university/UC Berkeley/Shuo Yang"
  - "university/上海交通大学/Xiaoze Fan"
  - "company/Inferact/Ion Stoica"
last_verified: "2026-09"
---
# FreeToken

## 项目定位

FreeToken 是 FlashML-org 于 2026 年开源的 **edge-native Mixture-of-Experts (MoE) serving engine**，目标是在个人电脑、游戏桌面和单工作站 GPU 上运行远大于显存容量的前沿开源 MoE 模型。

它不是 LMCache / Mooncake 那种数据中心 KV cache / memory-pool 组件，而是更靠近完整 inference runtime：把 GPU、CPU、host DRAM 与 PCIe 看成一个统一、动态重平衡的执行平台。

对应论文：**FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution**（arXiv:2608.16157，2026-08-17）。论文作者包括 Shuo Yang、Xiaoze Fan、Melissa Pan、Haocheng Xi、Zhe Wang、Shanlin Sun、Kurt Keutzer、Song Han、Matei Zaharia、Chenfeng Xu、Ion Stoica。

## 关键技术

### Bandwidth-adaptive CPU–GPU co-execution
- 根据本机 GPU / CPU / host-memory / PCIe 带宽动态决定 MoE expert 的执行与驻留策略，而不是固定比例 offload。
- 论文将这一策略描述为 bandwidth-adaptive execution / q* policy。

### Expert residency / cache
- 将 routed experts 放在 host memory 与 GPU 间动态调度；
- 使用 global LRU expert caching；
- 支持按 layer 的 host-bank residency 与运行时显存预算调整。

### Prefill streaming
- full-layer double-buffered prefill streaming，在 host→GPU 权重传输与计算之间做 overlap，降低大模型 prefill 时因权重流式加载导致的停顿。

### FTW fast weight format
- FreeToken 自有 FTW checkpoint / weight format，面向快速加载、流式权重与量化模型 serving；
- 2026-09 仍在快速演进，包括 NVFP4 / FP8 / BF16、多模态 vision tower 和旧 checkpoint repair。

### Semantic-aware / agentic state reuse
- FreeToken 不只做普通 prefix KV cache，也强调 semantic anchor checkpoint，用于 agent workload 中 tool call / thinking block / context edit 后减少重复计算。

### Dynamic memory management
- runtime 可在 expert cache、KV memory 等用途之间动态重新分配 VRAM，而不要求 engine restart / reload weights。

## 模型与硬件范围

论文和官方文档报告支持 20+ MoE 模型，并覆盖从 8GB laptop GPU 到单工作站 GPU 的本地推理；典型目标包括 Qwen、DeepSeek、GLM、MiniMax 等大型 MoE checkpoint。

截至 2026-09，官方安装要求的主线是 Linux x86_64 + NVIDIA GPU / CUDA 13；Windows 通过 Desktop app 支持。AMD、macOS、aarch64 / DGX Spark 等仍在 roadmap，不能写成已成熟支持。

## SGLang / mini-SGLang 关系

FreeToken 官方 README 明确写明：项目 **deeply inspired by mini-SGLang**，并学习 / 复用了 SGLang、vLLM、FlashInfer、flash-linear-attention、LightLLM 和 llama.cpp 的设计或代码。

这条关系里最重要的人物桥是 [[university/上海交通大学/Xiaoze Fan|Xiaoze Fan（范晓泽）]]：
- FreeToken 论文共同一作；
- mini-SGLang 的核心作者 / 开发者；
- 本人主页将 mini-SGLang 列为主要项目，并说明其在 UC Berkeley Sky Computing Lab 从事 ML systems / LLM serving 研究。

因此可以建立：

`SGLang → mini-SGLang → Xiaoze Fan → FreeToken`

这比简单写“FreeToken inspired by SGLang”更能解释真实的人才与代码传播路径。

## Berkeley Sky / LMSYS 关系

[[university/UC Berkeley/Shuo Yang|Shuo Yang]] 是 UC Berkeley EECS 博士生、Sky Computing Lab / LMSYS 成员，由 [[company/Inferact/Ion Stoica|Ion Stoica]] 指导。其研究覆盖 LLM serving、GPU kernel、sparse attention、multimodal systems 与 algorithm-system co-design。

[[university/上海交通大学/Xiaoze Fan|Xiaoze Fan]] 是上海交通大学 ACM Honors Class 本科生，2026 年作为 Visiting Student Researcher 加入 Berkeley Sky Computing Lab；其主页明确写明由 Ion Stoica supervised、Shuo Yang mentored。

因此 FreeToken 也应放进现有的 **Berkeley Sky / LMSYS inference systems** 人才网络，而不是作为孤立的“桌面端模型工具”。

## 与现有图谱项目的关系

- **SGLang / mini-SGLang**：直接设计与代码传承；Xiaoze Fan 是关键人物桥。
- **vLLM**：官方明确列为学习 / 复用来源；当前只记录项目级技术来源，不自动推断 FreeToken 作者与所有 vLLM maintainer 存在人际强边。
- **FlashInfer**：用于高性能 GPU inference kernel 生态；同样先记录 project-level technical dependency / reuse。
- **LMCache / Mooncake**：技术关注点相邻但层级不同。FreeToken 更偏单机异构 MoE execution + expert/KV memory orchestration；LMCache / Mooncake 更偏跨 engine / 跨节点 KV storage / transfer。除非出现共同 PR / integration，不建立人物关系。
- **MoE-Lightning / Jenga**：都研究受限内存与异构硬件上的大模型 serving，但当前只作为研究主题邻接，不凭主题相似建立作者强边。

## 关键人物

- [[university/UC Berkeley/Shuo Yang|Shuo Yang]]：FreeToken 共同一作 / Berkeley Sky systems researcher；项目代码核心贡献者之一。
- [[university/上海交通大学/Xiaoze Fan|Xiaoze Fan（范晓泽）]]：FreeToken 共同一作；mini-SGLang 核心开发者；FreeToken ↔ SGLang 生态最重要的桥节点之一。
- [[company/Inferact/Ion Stoica|Ion Stoica]]：论文作者、Shuo Yang 博士导师、Xiaoze Fan 在 Berkeley Sky 访问研究的 supervisor。
- Melissa Pan、Haocheng Xi、Zhe Wang、Shanlin Sun、Kurt Keutzer、Song Han、Matei Zaharia、Chenfeng Xu：论文共同作者；本轮先保留 paper-author 证据，不因共同署名自动建立所有两两人物边。

## 当前活跃度

截至 2026-09-16：
- GitHub 仓库仍处于高频开发；
- v0.1.3 于 2026-09-16 发布；
- 近期主线包括 multimodal image serving、Qwen3.8 / GLM-5.3、quantization refactor、FTW checkpoint repair、MoE residency 与 consumer-GPU compatibility。

## Sources
- https://github.com/FlashML-org/FreeToken
- https://arxiv.org/abs/2608.16157
- https://www.flashml.ai/
- https://andy-yang-1.github.io/
- https://jasonfxz.top/
- https://sky.cs.berkeley.edu/people/
- https://github.com/sgl-project/mini-sglang
