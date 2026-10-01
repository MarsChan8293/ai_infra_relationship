---
type: project
name: clangd-ascend
parent: DeepSeek-Infra
status: active
repository: https://github.com/deepseek-ai/clangd-ascend
docs: https://github.com/deepseek-ai/clangd-ascend
last_verified: "2026-10"
companies: ["深度求索"]
layer: compiler
areas:
  - "developer-tooling"
  - "language-server"
  - "ascendc"
  - "code-completion"
  - "diagnostics"
  - "navigation"
hardware:
  - "ascend"
integrations:
  - "CANN"
---
# clangd-ascend

## 项目简介
clangd-ascend 是 DeepSeek 针对 AscendC 定制的 clangd，为 `.asc` kernel 源文件提供代码补全、诊断、跳转和导航能力，补齐 Ascend kernel 开发工具链中的 IDE / language-server 层。

## 核心能力
- 支持主要 AscendC builtin types、address spaces 与 kernel launch 语法。
- 通过 `include/cce_stubs/` 为 AscendC builtin function 提供声明。
- 基于 LLVM / clangd patch 构建，运行时读取本地 CANN headers。
- [[DeepEP-Ascend]] 仓库将它作为开发/调试子模块；它负责开发期代码智能，和 [[DeepJIT]] 的运行时编译职责不同。

## 生态关系
[[DeepEP-Ascend]] · [[DeepJIT]] · [[community/Ascend/Ascend/Ascend|Ascend]] · [[community/Ascend/CANN/CANN|CANN]] · LLVM/clangd

## Sources
- https://github.com/deepseek-ai/clangd-ascend
- https://github.com/deepseek-ai/DeepEP-Ascend
