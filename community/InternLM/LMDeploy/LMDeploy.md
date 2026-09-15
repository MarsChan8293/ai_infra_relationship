---
type: project
name: LMDeploy
linked_people: []
layer: inference-engine
open_source: true
repository: https://github.com/InternLM/lmdeploy
areas: [llm-inference, model-serving, quantization, cuda-kernels, kv-cache, tensor-parallelism, multimodal-inference, heterogeneous-deployment]
governance: InternLM open-source ecosystem / Shanghai AI Laboratory
people:
  - "university/上海人工智能实验室/Li Zhang"
  - "university/上海人工智能实验室/Han Lv"
  - "university/上海人工智能实验室/Qian Yao"
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

## 当前核心人物桥
- [[university/上海人工智能实验室/Li Zhang|Li Zhang / lzhangzz]]：TurboMind mixed-precision CUDA/GEMM、低比特 kernel、AWQ backend 与 Linear API。PR #4943 在 2026-09 继续扩展 SM90 U4/MXFP4/NVFP4/E4M3/FP8 mixed GEMM。
- [[university/上海人工智能实验室/Han Lv|Han Lv / lvhan028]]：serving/API/runtime 高频贡献者。PR #4841 为 OpenAI-compatible Chat Completions 增加 server-side multi-choice fan-out，并完整处理 streaming、session cleanup 与 usage accounting。
- [[university/上海人工智能实验室/Qian Yao|Qian Yao / grimoire]]：PyTorch/Triton/CUDA kernel 高频贡献者。PR #4861 为 paged attention 与 DeepSeek-V4 prefill 引入 CUDA PDL；commit email `yaoqian@pjlab.org.cn` 与 TurboMind 论文作者身份直接对应。

三人都在 2026 年修订版 TurboMind 系统论文中以 Shanghai AI Laboratory affiliation 出现，因此这批关系由“论文 affiliation + GitHub identity + 直接工程 PR”三层证据支撑，而不是 contributor 排名推断。

## 与上海 AI 实验室的关系
[[上海人工智能实验室]] 官方开源页面直接列出 LMDeploy，并将其描述为涵盖大模型轻量化、推理部署和服务的解决方案。实验室 2026 年“大模型推理部署方向”招聘岗位也明确要求参与 LMDeploy 项目研发和推理优化，因此这里建立机构 → 项目的直接强关系，而不是仅依据个人贡献反推机构关系。

## 生态关系
LMDeploy 官方仓库明确致谢 vLLM、FasterTransformer、DeepSpeed-MII 等项目。致谢或兼容关系本身不升级为组织级合作边；后续 BFS 应优先从 TurboMind 论文作者、长期 maintainer 和核心 review/commit 网络建立人物关系。

## Sources
- https://github.com/InternLM/lmdeploy
- https://github.com/InternLM/lmdeploy/pull/4943
- https://github.com/InternLM/lmdeploy/pull/4841
- https://github.com/InternLM/lmdeploy/pull/4861
- https://www.shlab.org.cn/open
- https://www.shlab.org.cn/intern-ai
- https://www.shlab.org.cn/joinus/detail/7630830897067673919?mode=campus
- https://arxiv.org/html/2508.15601v2
