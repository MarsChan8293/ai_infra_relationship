---
type: project
name: DeepJIT
parent: DeepSeek-Infra
status: active
repository: https://github.com/deepseek-ai/DeepJIT
last_verified: "2026-09"
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/guyan364"
  - "community/deepseek-ai/DeepSeek-Infra/kurisu6912"
  - "community/deepseek-ai/DeepSeek-Infra/LyricZhao"
companies: ["深度求索"]
company_relation: company-led
layer: compiler
areas:
  - "jit-compilation"
  - "gpu-kernel-generation"
hardware:
  - "gpu"
integrations: []
linked_companies:
  - "company/深度求索/深度求索"
---
# DeepJIT

## 项目简介
DeepJIT 是 DeepSeek 在 2026 年开源的轻量 xPU kernel JIT compilation/runtime library，使用 C++20，目标是为 NVIDIA CUDA GPU 与 Huawei Ascend NPU 等平台提供更统一的 kernel 动态编译与加载能力。

## GitHub
https://github.com/deepseek-ai/DeepJIT

## 主要贡献公司
- [[company/深度求索/深度求索|深度求索]]：发起并通过 deepseek-ai 维护。

## 主要维护者 / 组织
由 [[深度求索]] / deepseek-ai 维护。当前公开主要作者节点包括 [[guyan364]]、[[kurisu6912]]、[[LyricZhao]]。

## 生态关系
[[vLLM-Ascend]] · [[DeepGEMM]] · CUDA · Ascend/CANN。它补的是 kernel toolchain/JIT 层，而不是完整 serving runtime。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/guyan364|guyan364]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/kurisu6912|kurisu6912]]：社区贡献关联；人物页已明确记录该社区。
- [[community/deepseek-ai/DeepSeek-Infra/LyricZhao|LyricZhao]]：社区贡献关联；人物页已明确记录该社区。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
