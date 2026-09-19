---
type: project
name: TensorRT-LLM
status: active
linked_people:
  - "community/NVIDIA/TensorRT-LLM/Anurag Mukkara"
  - "community/NVIDIA/TensorRT-LLM/Brian Nguyen"
  - "community/NVIDIA/TensorRT-LLM/Chang Liu"
  - "community/NVIDIA/TensorRT-LLM/Faraz Khoubsirat"
  - "community/NVIDIA/TensorRT-LLM/Xiao Wang"
  - "community/NVIDIA/TensorRT-LLM/Xin He"
  - "community/NVIDIA/TensorRT-LLM/Yao Yao"
  - "community/NVIDIA/TensorRT-LLM/Yi Zhang"
  - "community/NVIDIA/TensorRT-LLM/Yibin Li"
  - "community/NVIDIA/TensorRT-LLM/Zhaoyang Wang"
repository: https://github.com/NVIDIA/TensorRT-LLM
docs: https://docs.nvidia.com/tensorrt-llm/
last_verified: "2026-09"
governance: company-led
companies: ["NVIDIA"]
company_relation: company-led
layer: inference-engine
areas:
  - "tensorrt-engine"
  - "quantization"
  - "speculative-decoding"
  - "tensor-parallel"
  - "expert-parallel"
  - "disaggregated-serving"
hardware:
  - "nvidia"
integrations:
  - "NVIDIA Dynamo"
linked_companies:
  - "company/NVIDIA/NVIDIA"
---
# TensorRT-LLM

## 项目简介
TensorRT-LLM 是 NVIDIA 面向 LLM inference 的 runtime、kernel 与模型执行栈，深度结合 CUDA/TensorRT，对 NVIDIA GPU 上的 attention、GEMM、MoE、量化、speculative decoding、KV cache 与多 GPU 执行做系统级优化。

## GitHub
https://github.com/NVIDIA/TensorRT-LLM

## 主要贡献公司
- [[company/NVIDIA/NVIDIA|NVIDIA]]：项目主导维护公司。

## 主要维护者 / 组织
由 [[NVIDIA]] 主导维护。仓库人物页按公开长期贡献/维护证据建模，不把所有 NVIDIA 员工自动纳入核心项目组。

## 生态关系
[[Dynamo]] · [[FlashInfer]] · [[NIXL]] · [[vLLM]] · [[SGLang]] · [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]]。TensorRT-LLM 是 NVIDIA-specialized engine/runtime，而 Dynamo 更偏跨 engine 的集群级 serving 编排。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/NVIDIA/TensorRT-LLM/Anurag Mukkara|Anurag Mukkara]]：[[TensorRT-LLM]]：speculative decoding 方向活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Brian Nguyen|Brian Nguyen]]：[[TensorRT-LLM]]：FlashInfer decode / CUDA Graph 集成活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Chang Liu|Chang Liu]]：[[TensorRT-LLM]]：低精度模型与性能回归方向活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Faraz Khoubsirat|Faraz Khoubsirat]]：[[TensorRT-LLM]]：FMHA/kernel 方向活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Xiao Wang|Xiao Wang]]：[[TensorRT-LLM]]：disaggregated serving 方向活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Xin He|Xin He]]：[[TensorRT-LLM]]：disaggregated serving 方向活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Yao Yao|Yao Yao]]：[[TensorRT-LLM]]：KV cache manager 方向活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Yi Zhang|Yi Zhang]]：[[TensorRT-LLM]]：KV cache management 方向活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Yibin Li|Yibin Li]]：[[TensorRT-LLM]]：model integration 活跃贡献者
- [[community/NVIDIA/TensorRT-LLM/Zhaoyang Wang|Zhaoyang Wang]]：[[TensorRT-LLM]]：近期活跃核心贡献者

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
