---
type: project
name: LMDeploy
linked_people: []
layer: inference-engine
open_source: true
repository: https://github.com/InternLM/lmdeploy
areas: [llm-inference, model-serving, quantization, cuda-kernels, kv-cache, tensor-parallelism, multimodal-inference, heterogeneous-deployment]
governance: InternLM open-source ecosystem / Shanghai AI Laboratory
last_verified: "2026-09"
linked_companies: []
---
# LMDeploy

LMDeploy 是面向大语言模型与多模态模型的压缩、部署和 serving 工具链。官方仓库将其定位为 LLM compression / deployment / serving toolkit，核心推理引擎包括 TurboMind。

## 核心技术
- persistent / continuous batching
- blocked KV cache
- dynamic split & fuse
- tensor parallelism
- 高性能 CUDA kernels
- weight-only、KV 等量化路径
- 多机、多卡模型服务与多模型部署

## 与上海 AI 实验室的关系
[[上海人工智能实验室]] 官方开源页面直接列出 LMDeploy，并将其描述为涵盖大模型轻量化、推理部署和服务的解决方案。实验室 2026 年“大模型推理部署方向”招聘岗位也明确要求参与 LMDeploy 项目研发和推理优化，因此这里建立机构 → 项目的直接强关系，而不是仅依据个人贡献反推机构关系。

## 生态关系
LMDeploy 官方仓库明确致谢 vLLM、FasterTransformer、DeepSpeed-MII 等项目。致谢或兼容关系本身不升级为组织级合作边；后续 BFS 应优先从 TurboMind 论文作者、长期 maintainer 和核心 review/commit 网络建立人物关系。

## Sources
- https://github.com/InternLM/lmdeploy
- https://www.shlab.org.cn/open
- https://www.shlab.org.cn/intern-ai
- https://www.shlab.org.cn/joinus/detail/7630830897067673919?mode=campus
- https://arxiv.org/abs/2508.15601
