---
type: person
name: Li Zhang
aliases: [lzhangzz]
current_affiliations: ["上海人工智能实验室"]
projects: [LMDeploy]
areas: [llm-inference, turbomind, cuda-kernels, gemm, mixed-precision, quantization, gpu-kernels]
roles: [LMDeploy Contributor, TurboMind Kernel Contributor]
confidence: verified
last_verified: "2026-09"
---
# Li Zhang

GitHub：`lzhangzz`

## 当前关系
- [[上海人工智能实验室]]：2026 年修订版 TurboMind / LMDeploy 论文明确列出 Li Zhang 的 affiliation 为 Shanghai AI Laboratory。
- [[LMDeploy]]：长期核心代码贡献者之一，重点集中在 TurboMind、CUDA/GEMM、量化与高性能 kernel 路径。

## LMDeploy / TurboMind
- 2026-09 的 LMDeploy PR #4943 由 `lzhangzz` 提交，直接扩展 SM90 混合精度 GEMM，覆盖 U4、MXFP4、NVFP4、E4M3、FP8×MXFP4 等路径，并统一 TurboMind linear execution 与 PyTorch AWQ backend。
- Git commit metadata 将 `lzhangzz` 明确映射为 **Li Zhang**。
- 《LMDeploy Accelerates Mixed-Precision LLM Inference with TurboMind》列 Li Zhang 为共同第一作者，论文系统性描述 TurboMind 的 mixed-precision GEMM、attention 与 KV memory loading pipeline。

## 为什么重要
Li Zhang 是上海 AI Lab → LMDeploy → TurboMind → CUDA/GEMM/低比特推理这一条线最直接的工程桥节点之一，适合作为后续 kernel / quantization BFS seed。

## Sources
- https://arxiv.org/html/2508.15601v2
- https://github.com/lzhangzz
- https://github.com/InternLM/lmdeploy/pull/4943
- https://github.com/InternLM/lmdeploy
