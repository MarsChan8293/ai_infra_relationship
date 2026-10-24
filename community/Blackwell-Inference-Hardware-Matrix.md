# Blackwell 本地与异构推理：DGX Spark（SM121）/ RTX PRO 6000（SM120）

**核验时间：2026-10-24**。本页维护按真实硬件支持证据区分的项目清单，不以“都属于 Blackwell”替代兼容测试。

## 证据口径
- **实测 / 有部署配置**：上游在指定硬件上提供明确的测试数据、运行或部署方法；不代表由本仓库独立复测。
- **目标 / 构建适配**：上游宣称支持、已有相关编译目标，但未找到该具体 GPU SKU 完整质量与性能回归。
- **需移植 / 暂不支持**：主分支构建配置或运行环境与目标架构不匹配。
- GB10 属 **SM121 + ARM64（aarch64）统一内存**；RTX PRO 6000 Blackwell 96GB 属 **SM120 + x86-64 常见主机 + 离散 GDDR7**。须同时检查计算能力、Kernel、Host CPU/OS、显存/统一内存预算和驱动/CUDA。

## 已新增的 canonical 项目（13）

| 项目 | 上游 GitHub | GB10 / SM121 | RTX PRO 6000 / SM120 | 主线价值 |
| --- | --- | --- | --- | --- |
| [[community/JustVugg/Colibri/Colibri|Colibri]] | https://github.com/JustVugg/colibri | GB10 适配代码、统一内存修复 | 通用 CUDA；具体 SKU 未实测 | CPU / RAM / SSD Expert Streaming |
| [[community/antirez/ds4/ds4|ds4]] | https://github.com/antirez/ds4 | **官方编译目标及实测** | 有 SM120a 编译目标；SKU 未实测 | 精简 C/CUDA Runtime、SSD Streaming |
| [[community/Avarok-Cybersecurity/Atlas/Atlas|Atlas]] | https://github.com/Avarok-Cybersecurity/atlas | **官方镜像与实测** | 需新增 SM120 Kernel target | Rust 原生 Runtime、按模型/硬件定制 |
| [[community/HawkBearPig/DGPP/DGPP|DGPP]] | https://github.com/HawkBearPig/dgpp | **1/2/4 Spark 目标与实测** | 暂无支持证据 | RDMA / RoCE TP、Prefix Cache |
| [[community/sf-stav/veloGB10/veloGB10|veloGB10]] | https://github.com/sf-stav/veloGB10 | **1/2/4 GB10 官方目标及实测** | 不面向通用 GPU 移植 | GB10 专用 NVFP4 / EXL3 / TP |
| [[community/kindlingai/gr8/gr8|gr8]] | https://github.com/kindlingai/gr8 | **3/4/6 Spark Beta 配置及实测** | 不在部署矩阵 | GLM 5.3 原生 CUDA / RoCE |
| [[community/rdaum/Eider/Eider|Eider]] | https://github.com/rdaum/eider | **原生 GB10 目标及实测** | 暂无支持证据 | Rust CUDA/cuBLASLt |
| [[community/Metrale/Metrale-Engine/Metrale-Engine|Metrale Engine]] | https://github.com/Metrale/metrale-inference | **GB10 模型/并发 Benchmark** | 未发现本 SKU 验证 | (hardware, model, quant) 专用编译 |
| [[community/spark-arena/SparkRun/SparkRun|SparkRun]] | https://github.com/spark-arena/sparkrun | **单/多 Spark 部署管理** | 未确认；不是计算引擎 | Recipe、SSH Mesh、容器、集群管理 |
| [[community/tpurtell/DS41RT/DS41RT|DS41RT]] | https://github.com/tpurtell/ds41rt | **4 Spark Expert Worker 实测** | **1/2×6000 Coordinator 实测** | Attention–FFN 异构分离 |
| [[community/gpillon/Ignis/Ignis|Ignis]] | https://github.com/gpillon/ignis | 不属于目标硬件 | **RTX PRO 6000 Profile 实测** | Agent 专用 Rust/CUDA 单卡运行时 |
| [[community/gittensor-ai-lab/SparkInfer/SparkInfer|SparkInfer]] | https://github.com/gittensor-ai-lab/sparkinfer | **文档目标但根 CMake 暂排除 SM121** | **明确目标，主要实测 RTX 5090** | Model-Specific Kernel / Benchmark Gate |
| [[community/jesdga95/Basalt/Basalt|Basalt]] | https://github.com/jesdga95/basalt | 不支持：x86-64 + SM120 为当前平台 | **SM120 架构兼容，6000 SKU 待实测** | Expert 主存/显存分层卸载 |

## 原仓库已存在、无需重复收录
- [[community/NVIDIA/Flare/Flare|Flare]]：NVIDIA SM120/SM121 本地 Agent 推理研究原型。必须以具体模型/量化/TP Recipe 的官方验证为准。
- [[community/NVIDIA/TensorRT-Edge-LLM/TensorRT-Edge-LLM|TensorRT Edge-LLM]]：NVIDIA 边缘 C++ / TensorRT Engine Builder 路线，官方文档包含 DGX Spark 支持矩阵、实验性双机 TP2；不推导 RTX PRO 6000 完整支持。
- [[vLLM]]、[[SGLang]]、[[llama.cpp]]：通用 Serving/本地推理基线；可在合适 CUDA+ARM64 环境部署，但仍需具体模型、算子与上下文组合验证。

## 重点工程评估
1. **同模型并发基线**：TTFT、TPOT、端到端输出吞吐、Prefill、上下文长度、MTP 接受率和正确性；避免对比不同量化或不同 Checkpoint。
2. **GB10 多机**：TP/EP/AFD 拓扑、RoCE 带宽和时延、内存共享与 Expert/KV 容量预算。
3. **PRO 6000 PCIe**：单卡 NVFP4/EXL3、跨 GPU PCIe P2P、Expert Offload 的 RAM/SSD 开销。
4. **跨两种芯片的 AFD**：优先以 DS41RT 的有记录拓扑为参考，不把 PD Disaggregation 与 Attention–FFN Disaggregation 混为一谈。
5. **部署级别**：区分官方支持、在某硬件可编译、官方实测、第三方实测、尚待移植。

## 来源
上述逐项上游链接及节点中的 README/硬件说明；其中 SparkInfer 主线 `CMakeLists.txt` 当前的 SM121 排除记录需在后续升级时重新核验：https://github.com/gittensor-ai-lab/sparkinfer/blob/main/CMakeLists.txt
