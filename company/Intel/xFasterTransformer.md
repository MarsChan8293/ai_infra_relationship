---
type: project
name: xFasterTransformer
organization: Intel
linked_people: []
companies: ["Intel"]
company_relation: company-led
layer: cpu-llm-inference-runtime
open_source: true
repository: https://github.com/intel/xFasterTransformer
areas: [llm-inference, cpu, xeon, distributed-inference, quantization, vllm]
last_verified: "2026-09"
linked_companies:
  - "company/Intel/Intel"
---
# xFasterTransformer

xFasterTransformer（xFT）是 Intel 组织下的开源 LLM inference runtime，重点利用 Xeon / x86 平台能力，在单 socket、多 socket 和多节点场景提供高性能、可扩展的模型推理。

## AI Infra 位置
- C++ / Python 两层 API，覆盖模型转换、runtime 与 benchmark。
- 支持多 socket / 多节点 distributed inference。
- 支持 BF16、INT8、INT4、NF4 等多种推理数据类型。
- 提供 vLLM fork / `vllm-xft` serving 路径以及 OpenAI-compatible server。
- 2026 年仍有正式 release，支持 Qwen3、DeepSeek-R1 / V3 等模型，属于 Intel 当前仍活跃的 LLM inference 项目，而不是历史兼容层。

## Intel 关系
该仓库直接位于 `intel/xFasterTransformer`，README 使用 Intel Xeon 作为核心优化平台，并公开 `xft.maintainer@intel.com` 维护联系方式，因此可以建立 Intel → xFasterTransformer 的高置信 company-led 项目边。

## Sources
- https://github.com/intel/xFasterTransformer
- https://github.com/intel/xFasterTransformer/releases
