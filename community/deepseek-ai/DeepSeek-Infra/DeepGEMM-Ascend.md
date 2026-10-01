---
type: project
name: DeepGEMM-Ascend
parent: DeepSeek-Infra
status: active
linked_people: []
repository: https://github.com/deepseek-ai/DeepGEMM-Ascend
docs: https://github.com/deepseek-ai/DeepGEMM-Ascend
last_verified: "2026-10"
companies: ["深度求索"]
company_relation: company-led
layer: runtime
areas:
  - "gemm"
  - "fp8"
  - "fp4"
  - "moe-kernels"
  - "mqa-logits"
  - "jit"
hardware:
  - "ascend"
integrations:
  - "CANN"
  - "DeepJIT"
  - "TileLang"
linked_companies:
  - "company/深度求索/深度求索"
---
# DeepGEMM-Ascend

## 项目简介
DeepGEMM-Ascend 是 DeepSeek 于 2026-09-30 开源的 [[DeepGEMM]] Huawei Ascend 版本。它与 DeepGEMM API 兼容，支持 BF16、FP8、FP4 GEMM、MQA logits 与 MegaMoE，并针对 Ascend 的 MAD、fractal layout、对齐与地址计算做轻量抽象。

## GitHub
https://github.com/deepseek-ai/DeepGEMM-Ascend

## 关键技术
- 首发面向 Ascend 950 系列，要求 CANN 9.20、Bisheng / ld.lld 与 torch_npu。
- 使用稀疏数据加载、协程流水等 Ascend 特定优化逼近硬件峰值。
- JIT runtime 由 [[DeepJIT]] 提供；mHC kernel 使用 TileLang。
- 与 [[DeepGEMM]] 形成同 API 的 NVIDIA / Ascend 双实现关系，而不是独立 serving engine。

## 生态关系
[[DeepGEMM]] · [[DeepJIT]] · [[FlashMLA]] · [[DeepEP-Ascend]] · [[community/Ascend/Ascend/Ascend|Ascend]] · CANN · TileLang

## 公开贡献者
官方 README 列出的 project leads 为 [[周可行 Kexing Zhou]]、[[Zhean Xu]]、[[赵成钢 Chenggang Zhao]]；贡献覆盖 GEMM、MQA logits、mHC、MegaMoE、SF layout 与基础设施。

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
