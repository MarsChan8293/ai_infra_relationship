---
type: person
name: Michael Goin
current_affiliations: ["Red Hat"]
schools:
  - "University of Tennessee, Knoxville"
communities: [vLLM]
linked_companies:
  - "company/Red Hat/Red Hat"
areas: [quantization, kernels, performance, scheduler, hardware-efficiency]
roles: [Principal Engineer, Core Maintainer]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"community/vllm-project/vLLM/Robert Shaw","type":["coworker","open-source-collaboration","technical-collaboration"],"project":"vLLM","company":"Red Hat","confidence":"high","evidence":["https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1","https://www.redhat.com/en/authors/michael-goin","https://docs.vllm.ai/en/latest/governance/process/"]}'
  - '{"target":"community/vllm-project/vLLM/游凯超 Kaichao You","type":["open-source-collaboration","technical-collaboration"],"project":"vLLM","confidence":"high","evidence":["https://vllm.ai/blog/2025-05-12-hardware-plugin","https://vllm.ai/blog/2025-08-20-torch-compile","https://docs.vllm.ai/en/latest/governance/process/"]}'
  - '{"target":"company/Meta/Richard Zou","type":["technical-collaboration"],"project":"vLLM","confidence":"high","evidence":["https://vllm.ai/blog/2025-08-20-torch-compile"]}'
  - '{"target":"community/vllm-project/vLLM/Tyler Michael Smith","type":["coworker","open-source-collaboration","technical-collaboration"],"project":"vLLM","company":"Red Hat","start":"2025","confidence":"high","evidence":["https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1","https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community"]}'
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
- [[Tyler Michael Smith]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 性能工程合作者**。2024 FP8 支持和 2025 DeepSeek-R1 优化均有 Red Hat / Neural Magic 官方共同署名，关系不是仅凭同公司推断；2025–至今继续处于 vLLM kernels、MoE、distributed inference 工程网络。
- [[Robert Shaw]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 共同维护者**。2025-02 两人共同被 Red Hat credit 于 DeepSeek 优化；Robert 偏 engine/disaggregated serving，Michael 偏 quantization/performance。
- [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超（Kaichao You）]]：**vLLM Project Lead + compile / hardware-plugin 跨公司技术协作**。2025 Hardware Plugin 工作中两人与 Simon Mo、Robert Shaw 等共同参与 refactor、deep discussion 与 review；2025-08 又共同署名 vLLM 官方 torch.compile 技术文章。两人分属 Red Hat 与 [[Inferact]]，不标记为同事。
- [[Meta/Richard Zou|Richard Zou]]：**PyTorch compiler ↔ vLLM performance 跨公司技术协作**。两人共同署名 2025-08 vLLM 官方 torch.compile 技术文章；这是工程技术文章而非学术论文，因此仅记录 technical-collaboration，不记录 paper-coauthor。
- [[Lucas Wilkinson]]：**前 Neural Magic、现 Red Hat 同事 + GPU performance 合作者**。2025-02 共同参与 DeepSeek MLA / FP8 优化；两人在 attention、FlashInfer、quantized GEMM 等性能路径持续交叉。
- [[Wentao Ye]]：**Red Hat 同事 + GPU kernel / DeepSeek inference 优化合作者**。Wentao 2025 年加入 Red Hat 后与 Michael 在 Blackwell、DeepEP、DeepGEMM、quantization 等方向处于同一 vLLM 性能工程网络；截至 2026-09 仍持续协作。
- [[Matthew Bonanni]]：**候选 Red Hat / vLLM 关系，暂缓结构化**。两人同属 Red Hat 的 vLLM / inference engineering 网络，但当前公开资料不足以证明可单独归因的直接协作，不能仅凭同公司建立强边。

## Sources
- https://www.redhat.com/en/authors/michael-goin
- https://developers.redhat.com/articles/2025/03/19/how-we-optimized-vllm-deepseek-r1
- https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community
- https://www.redhat.com/en/blog/enhancing-deepseek-models-mla-and-fp8-optimizations-vllm
- https://docs.vllm.ai/en/v0.21.0/governance/process/
- https://docs.vllm.ai/en/latest/governance/process/
- https://vllm.ai/blog/2025-05-12-hardware-plugin
- https://vllm.ai/blog/2025-08-20-torch-compile
- https://www.linkedin.com/in/michael-goin

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/Red Hat/Red Hat|Red Hat]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
