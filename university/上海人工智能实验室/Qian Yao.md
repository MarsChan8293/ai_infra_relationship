---
type: person
name: Qian Yao
aliases: ["Q.Yao", grimoire]
current_affiliations: ["上海人工智能实验室"]
projects: [LMDeploy]
areas: [llm-inference, triton-kernels, cuda-kernels, paged-attention, quantization, pytorch-engine, gpu-kernels]
roles: [LMDeploy Contributor, Triton/CUDA Kernel Contributor]
confidence: verified
last_verified: "2026-09"
---
# Qian Yao

GitHub：`grimoire`（profile display name: **Q.Yao**）

## 当前关系
- [[上海人工智能实验室]]：2026 年修订版 TurboMind / LMDeploy 论文明确列出 Qian Yao 的 affiliation 为 Shanghai AI Laboratory。
- [[LMDeploy]]：长期高频核心贡献者，重点覆盖 PyTorch engine、Triton/CUDA kernel、Paged Attention、MoE 与低精度推理优化。

## LMDeploy 贡献
- PR #4861 由 `grimoire` 提交，为 split-K paged attention 与 DeepSeek-V4 prefill pipeline 引入 CUDA Programmatic Dependent Launch，并升级 Triton kernel 路径。
- 该 PR 的 commit metadata 使用 `yaoqian@pjlab.org.cn`，与论文中的 **Qian Yao / yaoqian@pjlab.org.cn** 完整对应，因此可以可靠完成 GitHub handle → 人物 identity resolution。
- 2026 年 LMDeploy release notes 还持续出现其 paged attention、FP8 MoE、speculative decoding、TTFT、Qwen/GLM 等性能优化贡献。

## 为什么重要
Qian Yao 是上海 AI Lab → LMDeploy → Triton/PagedAttention/PyTorch engine 的高价值桥节点，特别适合继续向 kernel、MoE、speculative decoding 和 serving scheduling 做 BFS。

## Sources
- https://arxiv.org/html/2508.15601v2
- https://github.com/grimoire
- https://github.com/InternLM/lmdeploy/pull/4861
- https://github.com/InternLM/lmdeploy/releases
