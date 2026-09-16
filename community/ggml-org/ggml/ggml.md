---
type: project
name: ggml
companies: ["Hugging Face"]
company_relation: joined-hugging-face-maintainer-team
layer: tensor-runtime
open_source: true
repository: https://github.com/ggml-org/ggml
areas: [tensor-runtime, local-inference, edge-inference, quantization, gguf, cpu, gpu, npu, multi-backend, c-cpp]
hardware: [CPU, NVIDIA GPU, AMD GPU, Apple Silicon, Intel GPU, Intel NPU, Ascend NPU, RISC-V, WebAssembly]
governance: ggml-org open-source community; Georgi Gerganov team joined Hugging Face in 2026 while projects remain open-source and community-governed
people:
  - "community/ggml-org/llama.cpp/Georgi Gerganov"
last_verified: "2026-09"
---
# ggml

## 项目定位

ggml 是 ggml-org 的轻量级 C/C++ tensor library，目标是以极少依赖在 commodity hardware 上提供可移植、高效的机器学习执行基础。它是 [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] 的底层核心之一，也是 GGUF / 低比特量化 / 多硬件本地推理生态的重要基础层。

官方 README 当前强调：
- plain C/C++、无第三方依赖；
- x86 / ARM / RISC-V / LoongArch / PowerPC / s390x / WebAssembly 等跨平台；
- CPU / GPU / NPU / browser backend；
- 2–8 bit integer quantization，以及 MXFP4 / NVFP4；
- runtime 零内存分配设计。

## 与 llama.cpp 的关系

llama.cpp 官方 README 明确写明项目 **built on top of ggml**。反过来，ggml README 当前也要求 core ggml library 的改动优先向 llama.cpp 提 PR，以获得更充分的 review 与测试。

因此在图谱中将两者建成紧密技术链：

`ggml tensor runtime → llama.cpp local inference engine`

而不是两个互不相干的开源仓库。

## Hugging Face 关系

2026-02-20 Hugging Face 官方宣布 GGML / llama.cpp 团队加入 Hugging Face。公告同时说明开源项目保持原有社区治理与技术自主，因此这里使用 `joined-hugging-face-maintainer-team` 描述强组织关系，而不是写成“HF 创建了 ggml”。

## 关键人物

- [[community/ggml-org/llama.cpp/Georgi Gerganov|Georgi Gerganov]]：ggml 创始人、llama.cpp maintainer；2026 年随团队加入 Hugging Face。

## Sources
- https://github.com/ggml-org/ggml
- https://github.com/ggml-org/ggml/blob/master/README.md
- https://ggml.ai/
- https://huggingface.co/blog/ggml-joins-hf
