---
type: project
name: "Metrale Engine"
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/Metrale/metrale-inference
areas:
  - rust-runtime
  - cuda-kernel
  - dgx-spark
  - dedicated-inference-engine
  - nvfp4
  - speculative-decoding
  - model-hardware-specialization
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# Metrale Engine

## 项目简介
Metrale Engine 是 Rust + CUDA 专用 LLM 运行时，针对 `(hardware, model, quantization)` 生成 Kernel PTX，以单一原生二进制文件提供兼容 OpenAI / Anthropic 的 Serving，不要求在线 Python。

## 硬件兼容性与证据层级
- **DGX Spark（GB10 / SM121）**：README 有本机 Qwen3.8 系列并发梯度和同条件 vLLM 对比，属于实测平台。
- 项目还列出 Hopper、B200/B300、AMD Strix Halo 和 Apple Metal 等研究/实现目标；各模型与精度的覆盖不一致。
- **RTX PRO 6000（SM120）**：未见该 SKU 的官方端到端实测，不应因为都叫 Blackwell 就直接断言支持。

## 核心技术与部署意义
- 按目标模型 × 芯片 × 量化构建 Kernel，适合比较通用抽象层与专用运行时成本。
- 上游性能报告须保留模型、量化、Prefill/Decode 以及每个并发梯度的测试条件。

## 关系与对比
[[community/Avarok-Cybersecurity/Atlas/Atlas|Atlas]]、[[community/NVIDIA/Flare/Flare|Flare]]、[[vLLM]] 属于对照关系而非直接集成。

## 来源
- https://github.com/Metrale/metrale-inference
- https://github.com/Metrale/metrale-inference/blob/HEAD/README.md
