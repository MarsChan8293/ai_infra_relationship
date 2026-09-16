---
type: project
name: ascend-kernel
companies: ["清程极智"]
company_relation: company-led
layer: kernel
open_source: true
repository: https://github.com/QingCheng-AI/ascend-kernel
areas: [ascend, kernels, llm-inference, heterogeneous-compute]
hardware: [Ascend]
last_verified: "2026-09"
---
# ascend-kernel

## 项目简介
`ascend-kernel` 是清程极智 GitHub 组织公开的 Ascend C kernel 项目，官方 README 明确说明这些算子用于 [[community/thu-pacman/Chitu/Chitu|Chitu（赤兔）]] 推理引擎。

它在图谱中的价值不是独立的通用算子库，而是提供一条很清晰的 `清程极智 → Chitu → Ascend kernel` 技术链，可继续向具体算子优化贡献者扩展。

## 生态关系
- [[company/清程极智/清程极智|清程极智]]：官方 GitHub 组织 `QingCheng-AI` 下项目。
- [[community/thu-pacman/Chitu/Chitu|Chitu]]：README 明确写明“用于 chitu 推理引擎的 Ascend C kernel”。

## Sources
- https://github.com/QingCheng-AI/ascend-kernel
- https://github.com/QingCheng-AI
