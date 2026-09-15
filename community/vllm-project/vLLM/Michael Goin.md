---
type: person
name: Michael Goin
current_affiliations: ["Red Hat"]
schools: ["University of Tennessee, Knoxville"]
communities: [vLLM]
areas: [quantization, kernels, performance, scheduler, hardware-efficiency]
roles: [Principal Engineer, Core Maintainer]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"community/vllm-project/vLLM/Robert Shaw","type":["coworker","open-source-collaboration","technical-collaboration"],"project":"vLLM","company":"Red Hat","confidence":"high","evidence":["https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1","https://www.redhat.com/en/authors/michael-goin","https://docs.vllm.ai/en/latest/governance/process/"]}'
  - '{"target":"community/vllm-project/vLLM/游凯超 Kaichao You","type":["open-source-collaboration","technical-collaboration"],"project":"vLLM","confidence":"high","evidence":["https://vllm.ai/blog/2025-05-12-hardware-plugin","https://vllm.ai/blog/2025-08-20-torch-compile","https://docs.vllm.ai/en/latest/governance/process/"]}'
---
# Michael Goin

社区：[[vLLM]]
当前：[[Red Hat]] Principal / Senior Principal inference engineering

## 教育经历
- 曾在 [[University of Tennessee, Knoxville]] 从事研究生阶段科研

## 工作经历
- [[Oak Ridge National Laboratory]]：研究 / 实习经历
- [[Neural Magic]]：性能工程与技术领导；负责 inference performance
- [[Red Hat]]：Neural Magic 于 2025 年初并入后继续从事 vLLM 与 AI inference

## 社区贡献
vLLM Lead Maintainer / Project Lead，负责 quantization、Blackwell、FlashInfer、DeepEP / DeepGEMM 与性能优化。

## 人物关系
- [[Tyler Michael Smith]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 性能工程合作者**。至少在 2025-02，两人共同参与 DeepSeek MLA / FP8 vLLM 优化；截至 2026-09 仍在 kernels、MoE、distributed inference 等路径协作。
- [[Robert Shaw]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 共同维护者**。2025-02 两人共同被 Red Hat credit 于 DeepSeek 优化；Robert 偏 engine/disaggregated serving，Michael 偏 quantization/performance。
- [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超（Kaichao You）]]：**vLLM Project Lead + compile / hardware-plugin 跨公司技术协作**。2025 Hardware Plugin 工作中两人与 Simon Mo、Robert Shaw 等共同参与 refactor、deep discussion 与 review；2025-08 又共同署名 vLLM 官方 torch.compile 技术文章。两人分属 Red Hat 与 [[Inferact]]，不标记为同事。
- [[Meta/Richard Zou|Richard Zou]]：**PyTorch compiler ↔ vLLM performance 跨公司技术协作**。两人共同署名 2025-08 vLLM torch.compile 技术文章，该内容来自 Red Hat 主持的 vLLM biweekly office hours；截至 2026-09 Richard 在 [[Meta]]、Michael 在 Red Hat。
- [[Lucas Wilkinson]]：**前 Neural Magic、现 Red Hat 同事 + GPU performance 合作者**。2025-02 共同参与 DeepSeek MLA / FP8 优化；两人在 attention、FlashInfer、quantized GEMM 等性能路径持续交叉。
- [[Wentao Ye]]：**Red Hat 同事 + GPU kernel / DeepSeek inference 优化合作者**。Wentao 2025 年加入 Red Hat 后与 Michael 在 Blackwell、DeepEP、DeepGEMM、quantization 等方向处于同一 vLLM 性能工程网络；截至 2026-09 仍持续协作。
- [[Matthew Bonanni]]：**Red Hat 同事 + vLLM C++/CUDA 性能协作者**。截至 2026-09 两人同属 Red Hat vLLM/inference 工程网络；公开资料未确认首次共事的精确月份。

## Sources
- https://www.redhat.com/en/authors/michael-goin
- https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1
- https://www.redhat.com/en/blog/enhancing-deepseek-models-mla-and-fp8-optimizations-vllm
- https://docs.vllm.ai/en/v0.21.0/governance/process/
- https://docs.vllm.ai/en/latest/governance/process/
- https://vllm.ai/blog/2025-05-12-hardware-plugin
- https://vllm.ai/blog/2025-08-20-torch-compile
- https://www.linkedin.com/in/michael-goin
