---
type: project
name: CUTLASS
linked_people:
  - "community/NVIDIA/CUTLASS/Aniket Shivam"
  - "community/NVIDIA/CUTLASS/Brandon Sun"
  - "community/NVIDIA/CUTLASS/dePaul Miller"
  - "community/NVIDIA/CUTLASS/IonThruster"
  - "community/NVIDIA/CUTLASS/Jack Kosaian"
  - "community/NVIDIA/CUTLASS/Junkai Wu"
  - "community/NVIDIA/CUTLASS/Yujia Zhai"
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

## 维护与团队联系

2026-08-10，原 CUTLASS admin hwu36 公开宣布不再全职维护，并明确要求后续需要 CUTLASS team attention 时联系以下 7 个账号。本页把这组“团队联系/维护线索”编码进图谱，但不把该 handoff 自动等同于一份正式 MAINTAINERS roster。

- [[community/NVIDIA/CUTLASS/Junkai Wu|Junkai Wu (@Junkai-Wu)]]：handoff 联系人；2026-08 之后持续发布 CUTLASS release discussion，GitHub PR 也出现 Collaborator 信号。
- [[community/NVIDIA/CUTLASS/IonThruster|@IonThruster]]：handoff 联系人。
- [[community/NVIDIA/CUTLASS/Aniket Shivam|Aniket Shivam (@ANIKET-SHIVAM)]]：handoff 联系人；官方 CONTRIBUTORS 列为 CUTLASS C++ developer。
- [[community/NVIDIA/CUTLASS/Jack Kosaian|Jack Kosaian (@jackkosaian)]]：handoff 联系人；官方 CONTRIBUTORS 列为 CUTLASS C++ developer。
- [[community/NVIDIA/CUTLASS/dePaul Miller|dePaul Miller (@depaulmillz)]]：handoff 联系人；官方 CONTRIBUTORS 列为 CUTLASS C++ developer。
- [[community/NVIDIA/CUTLASS/Yujia Zhai|Yujia Zhai (@yzhaiustc)]]：handoff 联系人；官方 CONTRIBUTORS 列为 CUTLASS C++ developer。
- [[community/NVIDIA/CUTLASS/Brandon Sun|Brandon Sun (@brandon-yujie-sun)]]：handoff 联系人；官方 CONTRIBUTORS 列为 CUTLASS DSL developer。

治理边界：当前仓库未发现 CODEOWNERS / MAINTAINERS 文件，因此除具备额外 release / Collaborator 信号的账号外，不把上述联系人统一升级为“formal maintainer”。

## 直接来源

- https://docs.nvidia.com/cutlass/latest/
- https://github.com/NVIDIA/cutlass

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/NVIDIA/CUTLASS/Aniket Shivam|Aniket Shivam]]：[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：handoff 联系人；当前证据不足以单独标为 formal maintainer。
- [[community/NVIDIA/CUTLASS/Brandon Sun|Brandon Sun]]：[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：handoff 联系人；当前证据不足以单独标为 formal maintainer。
- [[community/NVIDIA/CUTLASS/dePaul Miller|dePaul Miller]]：[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：handoff 联系人；当前证据不足以单独标为 formal maintainer。
- [[community/NVIDIA/CUTLASS/IonThruster|IonThruster]]：[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：handoff 联系人；当前证据不足以单独标为 formal maintainer。
- [[community/NVIDIA/CUTLASS/Jack Kosaian|Jack Kosaian]]：[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：handoff 联系人；当前证据不足以单独标为 formal maintainer。
- [[community/NVIDIA/CUTLASS/Junkai Wu|Junkai Wu]]：[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：handoff 联系人，并有持续 release / Collaborator 信号。
- [[community/NVIDIA/CUTLASS/Yujia Zhai|Yujia Zhai]]：[[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]]：handoff 联系人；当前证据不足以单独标为 formal maintainer。

<!-- END AUTO PROJECT PEOPLE -->
