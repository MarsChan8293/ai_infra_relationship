---
type: project
name: veloGB10
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/sf-stav/veloGB10
areas:
  - dgx-spark
  - rust-runtime
  - tensor-parallel
  - roce
  - nvfp4
  - exl3
  - low-latency
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# veloGB10

## 项目简介
专为 GB10 编写的 Rust + CUDA 推理引擎，针对少量选定模型实现原生 Kernel、量化加载、调度以及单机/多节点 Tensor Parallel。

## 硬件兼容性与证据层级
- **DGX Spark 与 GB10 OEM / SM121：官方明确支持**，提供单机、双机 TP2 和四机 TP4 配置及测量记录。
- **RTX PRO 6000 / SM120：官方明确不以通用 GPU 可移植性为目标**，不列为支持。

## 核心技术与部署意义
- NVFP4/FP8、EXL3 量化与 GB10 专用执行路径。
- 对 200GbE 多机部署重点比较通信成本、Prefill/Decode、MTP 接受率和内存带宽。

## 关系与对比
[[community/HawkBearPig/DGPP/DGPP|DGPP]]、[[community/kindlingai/gr8/gr8|gr8]]、[[community/antirez/ds4/ds4|ds4]]。

## 来源
- https://github.com/sf-stav/veloGB10
- https://github.com/sf-stav/veloGB10/blob/HEAD/README.md
