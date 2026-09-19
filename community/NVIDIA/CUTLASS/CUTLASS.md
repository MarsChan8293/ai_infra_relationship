---
type: project
name: CUTLASS
linked_people: []
layer: runtime
status: active
repository: https://github.com/NVIDIA/cutlass
docs: https://docs.nvidia.com/cutlass/latest/
areas:
  - "gemm"
  - "cute"
  - "cuda-templates"
  - "python-dsl"
hardware:
  - "nvidia"
integrations:
  - "DeepGEMM"
companies: ["NVIDIA"]
last_verified: "2026-09"
linked_companies:
  - "company/NVIDIA/NVIDIA"
---
# CUTLASS

> NVIDIA CUDA 高性能线性代数 kernel 的模板、CuTe 抽象与 Python DSL 工具库。

## 核心能力

| 能力 | 说明 |
|---|---|
| GEMM | 提供高性能矩阵乘 kernel 构建模块 |
| CuTe | 用可组合布局和张量抽象描述数据移动与计算 |
| 低精度类型 | 覆盖 FP8、FP4 等现代 Tensor Core 路径 |
| Kernel Building Blocks | 为自定义 kernel 和上层库提供积木 |

## 边界

CUTLASS 聚焦 NVIDIA CUDA kernel 构建，不负责模型图执行、Serving API 或跨节点调度。

## 集成与后端

- DeepGEMM：kernel 基础设施关系。

## 关联项目

- 推理 runtime：TensorRT-LLM。
- Kernel / DSL 生态：FlashInfer、Triton、TileLang。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前 CUTLASS 官方资料为快照。

## 直接来源

- https://docs.nvidia.com/cutlass/latest/
- https://github.com/NVIDIA/cutlass

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
