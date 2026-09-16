---
type: person
name: Lucas Wilkinson
current_affiliations: ["Red Hat"]
public_email: lwilkins@redhat.com
communities: [vLLM]
roles: [Project Lead, Core Maintainer, Engineer]
areas: [gpu-kernels, attention, flashinfer, marlin, machete, performance]
confidence: high
last_verified: "2026-09"
---
# Lucas Wilkinson

社区：[[vLLM]]
当前：[[Red Hat]] vLLM Project Lead / Engineer

公开职业邮箱：`lwilkins@redhat.com`。2026-09 的 vLLM 公共提交 trailer 直接使用该地址；它用于组织关联证据，不单独推断职级。

## 教育经历
- 有 [[University of Toronto]] 相关研究经历，方向涉及稀疏矩阵乘与高性能计算

## 工作经历
- [[Neural Magic]]：GPU inference performance
- [[Red Hat]]：Neural Magic 于 2025 年初并入后继续从事 vLLM GPU / kernel performance

## 社区贡献
- [[vLLM]] 当前 governance 将 Lucas 列为 Project Lead / Core Maintainer。
- 负责 attention、FlashAttention、FlashInfer、Marlin、Machete、DeepEP / GPU 性能等路径。

## 人物关系
- [[Tyler Michael Smith]]：**前 Neural Magic、现 Red Hat 同事 + GPU kernel 协作者**。2025-02 两人共同被 Red Hat credit 于 DeepSeek MLA / FP8 vLLM 优化；截至 2026-09 仍在 attention、kernels、distributed performance 上有交叉。
- [[Michael Goin]]：**前 Neural Magic、现 Red Hat 同事 + vLLM performance 合作者**。2025-02 共同参与 DeepSeek 优化；Michael 更偏 quantization / overall performance，Lucas 更偏 attention / GEMM kernel 路径。
- [[Robert Shaw]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 共同维护者**。2025-02 同属 DeepSeek MLA / FP8 优化团队；Robert 负责 engine/distributed，Lucas 负责 GPU 性能，属于上下层协作。
- [[Matthew Bonanni]]：**Red Hat 同事 + CUDA/C++ 性能协作者**。截至 2026-09 两人同属 Red Hat 的 vLLM engineering 网络；公开资料未给出首次共事月份。
- [[Wentao Ye]]：**Red Hat 同事 + GPU performance 协作者**。Wentao 2025 年加入 Red Hat 后，两人在 Blackwell、DeepEP / DeepGEMM、kernel performance 等方向处于同一工程网络；截至 2026-09 持续共事。

## Sources
- https://www.redhat.com/en/blog/enhancing-deepseek-models-mla-and-fp8-optimizations-vllm
- https://github.com/vllm-project/vllm/blob/main/docs/governance/process.md
- https://github.com/vllm-project/vllm/commit/79e205e8cdf7864b8b9f2d23c908b887f2f5badb
