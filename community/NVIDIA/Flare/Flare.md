---
type: project
name: Flare
layer: inference-engine
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/NVIDIA/flare-local-inference
docs: https://github.com/NVIDIA/flare-local-inference/tree/main/docs
areas:
  - local-inference
  - agent-serving
  - model-preparation
  - cuda-graph
  - kv-cache
  - prefix-cache
  - tensor-parallel
hardware:
  - nvidia
integrations:
  - FlashInfer
companies:
  - NVIDIA
last_verified: "2026-10"
---

# Flare

## 项目简介

Flare（仓库名 `flare-local-inference`）是 NVIDIA 面向 **SM120/SM121** GPU 的本地大模型推理研究原型，重点针对长上下文、coding agent、重复工具调用与前缀/对话状态复用。它属于推理引擎层，服务范围集中于工作站、DGX Spark 等紧凑系统；项目官方明确指出**并非生产推理引擎 [[vLLM]] 的替代品**。

## 技术架构

- **Ignition（构建期 / Python）**：通过 PyTorch、Transformers 和 [[FlashInfer]]/b12x 准备模型、执行 kernel 调优、编译和 CUDA Graph 捕获，并导出运行包。
- **Helios（在线期 / Rust）**：通过预准备的运行包完成请求调度、缓存与 CUDA Graph 回放；在线服务进程不需要 Python 解释器。
- **状态所有权**：除 KV Cache，还显式维护 recurrent/continuation state、前缀 checkpoint、会话分支和恢复状态；设计中包含分层 prefix-cache offload。
- **容量与拓扑约束**：各模型的 Recipe 和图捕获配置限定可运行组合；tensor-parallel 每个 TP 度数需要独立导出包，不能直接跨 TP 度数复用。

## GitHub / 文档

- 官方源码：https://github.com/NVIDIA/flare-local-inference
- 设计文档：https://github.com/NVIDIA/flare-local-inference/blob/main/docs/core-design.md
- 模型准备：https://github.com/NVIDIA/flare-local-inference/blob/main/docs/model-preparation.md
- 多机方案：https://github.com/NVIDIA/flare-local-inference/blob/main/docs/multi-host.md
- 许可证：Apache-2.0（仓库许可证）。

## 主要维护者 / 组织

- [[company/NVIDIA/NVIDIA|NVIDIA]]：项目发布于 NVIDIA 官方 GitHub 组织，可核验的公司发起/维护关系。
- 具体核心个人贡献者尚未独立核验；不根据组织归属推断个人雇佣、职务或治理权限。

## 生态关系

- **[[FlashInfer]]**：直接软件依赖。Flare 在模型准备阶段使用 FlashInfer/b12x，并锁定相应版本；此项属于可核验的 integration。
- **[[vLLM]]**：架构与定位对照；vLLM 覆盖更广泛的模型、硬件和生产推理场景，Flare 服务范围更窄。**不代表两者直接集成。**
- **[[TensorRT-LLM]]**：同属 NVIDIA GPU 推理引擎生态，但不是 Flare 的同义名或可替换 runtime。
- **[[company/NVIDIA/NVIDIA|NVIDIA]]**：发起/主要维护组织。

## RTX PRO 5000 72GB 适配评估

RTX PRO 5000 Blackwell 属于 SM120 类目标硬件，在架构方向上适合验证 Flare；但不应将 GPU 架构匹配解读为所有官方 Recipe、权重精度和并行规模都已在该 SKU 上验证。

对于 8×72GB、2 组四卡 PCIe Switch 的服务器，建议：
1. 用官方单卡 Recipe 测试导出、启动、正确性、TTFT/TPOT 和显存峰值。
2. 将 TP2/TP4 首选部署在同一 PCIe Switch 下，首先检查 GPU P2P 拓扑。
3. 重点比较长会话、前缀复用、Agent tool-call 场景；使用相同模型、量化和并发参数与 vLLM 对齐基线。
4. 对跨交换机或跨机 RoCE 独立验证通信，不因存在 200GbE 网卡而假定跨机可直接部署。

## 边界与风险

- 官方定位为 **research prototype**；不宜未经长期稳定性验证就替代生产 vLLM。
- 专注 SM120/SM121 和选定模型 Recipe，不提供通用 AMD、Ascend 或其他 NVIDIA 架构的可移植承诺。
- 模型/TP/图捕获容量依赖预准备包；使用前应确认对应 Recipe、显存与 PCIe/P2P 条件。
- 性能优势必须由 RTX PRO 5000 实机同条件 benchmark 证明，不能单凭 Rust 运行时或 CUDA Graph 推断。

## Sources

- https://github.com/NVIDIA/flare-local-inference
- https://github.com/NVIDIA/flare-local-inference/blob/main/README.md
- https://github.com/NVIDIA/flare-local-inference/blob/main/docs/core-design.md
- https://github.com/NVIDIA/flare-local-inference/blob/main/docs/model-preparation.md
