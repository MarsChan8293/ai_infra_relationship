---
type: person
name: Canlin Guo
aliases: ["gcanlin", "@gcanlin"]
communities: ["vLLM-Omni", "vLLM-Ascend"]
projects: ["vLLM-Omni"]
areas: [ascend, npu, hardware-backend, multimodal-serving, tts, diffusion]
roles: [vLLM-Omni Active Committer, NPU Integration Owner]
confidence: verified
last_verified: "2026-09"
---
# Canlin Guo

## vLLM-Omni 角色
vLLM-Omni 官方 governance 将 Canlin Guo（`@gcanlin`）列为 Active Committer，职责明确为 **Hardware plugin, NPU integration, and TTS Model Support**。CODEOWNERS 同时把 model executor、plugins、platforms、attention 与 profiler 等硬件相关路径分配给他。

## Ascend / NPU 主线
- 2026 Q1 / Q2 NPU roadmap 的主要推动者，公开路线明确写出 vLLM-Omni NPU 支持依赖 [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]，并把 [[MindIE-SD]] 作为 Ascend-optimized diffusion operator library 接入 FlashAttentionBackend / CustomOp 路径。
- vLLM-Ascend 官方 contributors 列表也记录了 `@gcanlin` 的贡献，因此这里写为社区贡献关联，不把其升级为 vLLM-Ascend maintainer。

## 人物定位
这是 vLLM-Omni 中非常典型的 **硬件桥节点**：从 omni / diffusion serving 往下连接 Ascend NPU、vLLM-Ascend、MindIE-SD 与 hardware plugin abstraction。

## Sources
- https://github.com/vllm-project/vllm-omni/blob/main/docs/community/governance.md
- https://github.com/vllm-project/vllm-omni/blob/main/.github/CODEOWNERS
- https://github.com/vllm-project/vllm-omni/issues/886
- https://github.com/vllm-project/vllm-omni/issues/2223
- https://github.com/vllm-project/vllm-ascend/blob/main/docs/source/community/contributors.md
- https://github.com/gcanlin
