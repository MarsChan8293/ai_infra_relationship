---
type: person
name: Richard Zou
aliases: [Richard Zou]
company: Meta
communities: [vLLM]
areas: [pytorch-compiler, torch-compile, ai-infrastructure]
---
# Richard Zou

当前：[[Meta]] Senior Staff Software Engineer；长期参与 PyTorch compiler / torch.compile

## AI Infra 工作
- PyTorch compiler / torch.compile：参与 PyTorch 2 compiler 生态与 graph capture / compilation infrastructure
- [[vLLM]]：通过 torch.compile integration 与硬件可移植性工作连接到 vLLM serving stack
- 2026 vLLM Conference：以 PyTorch / Meta 身份分享 PyTorch 对 vLLM 的支持

## 人物关系
- [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超（Kaichao You）]]：**PyTorch compiler ↔ vLLM 技术协作，不是同事**。2025-08 vLLM 官方 torch.compile 技术文章由 Richard、游凯超、Michael Goin 等共同署名，内容来自 Red Hat 主持的 vLLM biweekly office hours；游凯超负责 vLLM compile integration 一侧，Richard 位于 PyTorch / Meta compiler 一侧。截至 2026-09 分属 Meta 与 [[Inferact]]。
- [[community/vllm-project/vLLM/Michael Goin|Michael Goin]]：**PyTorch compiler ↔ vLLM performance 跨公司技术协作**。两人共同署名 2025-08 vLLM torch.compile 技术文章；截至 2026-09 分属 Meta 与 [[Red Hat]]。
- Thomas Parnell：**vLLM 硬件可移植性公开技术协作者**。2026 PyTorch Conference 两人共同分享 hardware-agnostic vLLM model definitions，展示 Intel Gaudi/HPU 与 IBM Spyre 等后端无需 fork 模型定义的路径。

## Sources
- https://vllm.ai/blog/2025-08-20-torch-compile
- https://vllm.ai/events/vllm-conference/2026
- https://pytorch.org/blog/vllm-sessions-at-pytorch-conference-north-america-2026/
