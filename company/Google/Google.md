---
type: company
name: Google
---
# Google

## 公司简介
Google 在 AI Infra 中横跨 TPU、JAX/XLA、Kubernetes/GKE、数据中心网络、模型训练和 production serving，同时拥有 Google DeepMind / Gemini 等 foundation-model 体系。它既是硬件/编译/云平台提供者，也是大模型研究组织，因此常同时出现在基础设施和模型图谱两侧。

## 推理优化人才连接
- [[community/llm-d/Clayton Coleman|Clayton Coleman]]：Distinguished Engineer；[[llm-d]] founding / project leadership 网络成员，当前活跃状态按其 leave/inactive 记录处理。
- [[community/llm-d/Abdullah Gharaibeh|Abdullah Gharaibeh]]：Senior Staff Software Engineer；llm-d Router SIG Lead，负责 predicted-latency / token-aware routing、KV-cache affinity 等方向。
- [[community/llm-d/Ashok Chandrasekar|Ashok Chandrasekar]]：llm-d Benchmarking SIG Lead；同时参与 Kubernetes SIG/WG Serving 的 Inference Perf 基准工作。
- [[vLLM/李卓翰 Zhuohan Li|李卓翰（Zhuohan Li）]]：2021–2024 曾在 Google Brain / Google DeepMind 做 Research Intern，之后进入 OpenAI、Meta；这里只记录历史 affiliation。

## 图谱中的连接
- [[llm-d]]：Google 人员覆盖项目 leadership、Router 与 Benchmarking，并与 [[IBM]]、[[Red Hat]] 形成跨公司 Kubernetes-native distributed inference 网络。
- Kubernetes / Inference Gateway / Inference Perf：构成 Google 与开源 serving control plane 的重要技术桥。
- [[vLLM]]、JAX/TPU 等关系需按具体项目/人物证据区分，不能把平台兼容直接写成人物合作。

## Sources
- https://llm-d.ai/community/sigs
- https://llm-d.ai/blog/authors
- https://github.com/kubernetes-sigs/inference-perf
