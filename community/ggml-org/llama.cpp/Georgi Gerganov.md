---
type: person
name: Georgi Gerganov
aliases: ["Georgi Gerganov", "ggerganov"]
current_affiliations: ["Hugging Face"]
communities: [llama.cpp, ggml]
roles: [llama.cpp Maintainer, ggml Founder, Hugging Face Team]
linked_companies:
  - "company/Hugging Face/Hugging Face"
areas: [local-inference, edge-inference, tensor-runtime, quantization, gguf, cpu-gpu-hybrid, c-cpp, multi-backend]
confidence: verified
last_verified: "2026-09"
projects:
  - "llama.cpp"
---
# Georgi Gerganov

Georgi Gerganov 是 [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] / [[community/ggml-org/ggml/ggml|ggml]] 生态的核心人物，也是本图谱连接 **Local AI / edge inference** 与主流 AI Infra 的关键节点。

## llama.cpp / ggml

- llama.cpp 官方 README 当前维护的 `maintainer PRs` 查询明确包含 `ggerganov`，因此这里把其角色记录为 llama.cpp Maintainer，而不是仅凭历史提交数量推断治理身份。
- ggml 官方站点说明 ggml.ai 于 2023 年由 Georgi Gerganov 创立，用于支持 ggml 的开发。
- llama.cpp 官方 README 明确说明项目构建在 ggml tensor library 之上。

## Hugging Face

2026-02-20，Hugging Face 官方宣布 **GGML and llama.cpp join Hugging Face**。公告明确说明 Georgi Gerganov 和团队加入 Hugging Face，同时 Georgi 与团队继续全职维护 llama.cpp，并对技术方向与社区保持自主领导。

因此这里将 `current_affiliations: ["Hugging Face"]` 作为当前公开组织关系；这条边来自组织级官方公告，不是通过个人邮箱或单个 commit 推断。

## 技术位置

Georgi / ggml / llama.cpp 生态长期聚焦：
- C/C++ 本地推理 runtime；
- GGUF 与低比特量化；
- CPU / GPU 混合执行；
- Apple Metal、CUDA、HIP、Vulkan、SYCL、CANN、OpenVINO 等多硬件 backend；
- consumer hardware / edge devices 上的大模型推理。

这条路线与数据中心 serving engine 的 vLLM / SGLang，以及 edge-native MoE runtime [[community/FlashML-org/FreeToken/FreeToken|FreeToken]] 形成互补的 inference systems 分支。

## 邮箱规则

公开 Git commit / AUTHORS 中可见个人 Gmail `ggerganov@gmail.com`，但按照仓库现有邮箱机制，个人 Gmail 不写入 canonical `public_email`，只保留为来源证据。

## Sources
- https://github.com/ggml-org/llama.cpp
- https://github.com/ggml-org/llama.cpp/blob/master/README.md
- https://github.com/ggml-org/llama.cpp/blob/master/AUTHORS
- https://github.com/ggml-org/ggml
- https://ggml.ai/
- https://huggingface.co/blog/ggml-joins-hf
- https://huggingface.co/ggerganov

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/Hugging Face/Hugging Face|Hugging Face]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
