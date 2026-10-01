---
type: project
name: clangd-ascend
parent: DeepSeek-Infra
status: active
repository: https://github.com/deepseek-ai/clangd-ascend
docs: https://github.com/deepseek-ai/clangd-ascend
last_verified: "2026-10"
companies: ["深度求索"]
company_relation: company-led
layer: compiler
areas:
  - "developer-tooling"
  - "ascendc"
  - "code-completion"
  - "diagnostics"
hardware:
  - "ascend"
integrations:
  - "LLVM"
  - "clangd"
  - "CANN"
linked_companies:
  - "company/深度求索/深度求索"
---
# clangd-ascend

## 项目简介
clangd-ascend 是 DeepSeek 针对 AscendC 定制的 clangd，为 `.asc` kernel 源文件提供代码补全、诊断、跳转与导航能力，补齐 Ascend kernel 开发工具链中的 IDE / language-server 层。

## GitHub
https://github.com/deepseek-ai/clangd-ascend

## 关键技术
- 支持主要 AscendC builtin types、address spaces 与 kernel launch 语法。
- 通过 `include/cce_stubs/` 为 AscendC builtin function 提供声明。
- 基于 LLVM/clangd patches 构建，运行时读取本地 CANN headers。
- 被 [[DeepEP-Ascend]] 作为开发/调试子模块使用，与 [[DeepJIT]] 的运行时编译职责互补。

## 生态关系
[[DeepEP-Ascend]] · [[DeepJIT]] · [[community/Ascend/Ascend/Ascend|Ascend]] · LLVM/clangd · CANN
