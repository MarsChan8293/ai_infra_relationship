---
type: project
name: "SparkInfer"
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/gittensor-ai-lab/sparkinfer
areas:
  - rtx-pro-6000
  - blackwell-sm120
  - native-cuda
  - moe-inference
  - automated-optimization
  - kernel-benchmark
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# SparkInfer

## 项目简介
SparkInfer 采用 C++/CUDA 构建模型专用 Blackwell 运行时，关注 MoE Kernel、较小原生 Runtime、推测解码及自动优化/性能门禁。

## 硬件兼容性与证据层级
- **RTX 5090 / RTX PRO 6000（SM120）**：README 与 runtime 文档明确列为支持设备，主要可重复性能工作更集中于 RTX 5090。
- **DGX Spark（GB10 / SM121）**：项目文档称为研究目标，但截至 2026-10 的根目录 `CMakeLists.txt` 因 CUDA 12.8 工具链限制明确排除 `sm_121`；**不能列作主构建直接可用或已通过端到端验证**。若后续切换 CUDA Toolkit、构建脚本需再验证。
- **RTX PRO 5000（SM120）**：GPU 架构匹配不等于已验证具体 SKU。

## 核心技术与部署意义
- 原生 Blackwell CUDA Kernel，针对特定模型、权重和量化配置进行 Benchmark Gate。
- 仓库 README、runtime 文档与根构建系统对 SM121 的状态存在差异，应优先以可实际编译/运行的版本确认支持。

## 关系与对比
[[community/NVIDIA/Flare/Flare|Flare]]、[[community/gpillon/Ignis/Ignis|Ignis]] 与 [[community/tpurtell/DS41RT/DS41RT|DS41RT]] 是架构对照。

## 来源
- https://github.com/gittensor-ai-lab/sparkinfer
- https://github.com/gittensor-ai-lab/sparkinfer/blob/HEAD/README.md
