# community

AI 推理引擎、训练系统、GPU/NPU kernel、AI compiler、量化、KV Cache、数据传输、集合通信、分布式 serving 与异构计算等开源社区与技术项目的一级分类入口。

## 公司关系字段
所有项目主节点统一使用 `companies` 表示**主要公司贡献/维护关系**，并用 `company_relation` 描述关系性质。`companies` 不是赞助商、用户或兼容厂商列表；只有原始发起、founding contributor、core maintainer network、长期工程贡献等强证据才进入。学术/社区主导且没有明确主要公司的项目使用 `companies: []`。

常见关系：`company-originated` · `company-led` · `founding-contributors` · `cross-company-core-contributors` · `core-maintainer-network` · `industry-academia-co-development` · `community-led`。

## 项目 → 主要贡献公司
| 项目 | 主要公司 | 关系 |
| --- | --- | --- |
| [[AIBrix]] | [[company/ByteDance/ByteDance|ByteDance]] | 原始开发 / 发起 |
| [[Colossal-AI]] | [[company/HPC-AI Tech/HPC-AI Tech|HPC-AI Tech]] | 发起 / 主导 |
| [[DeepSeek-Infra]] / 3FS / DeepEP / DeepGEMM / DeepJIT / FlashMLA | [[company/DeepSeek/DeepSeek|DeepSeek]] | 发起 / 主导 |
| [[Dynamo]] / [[NIXL]] / [[TensorRT-LLM]] / [[Triton-Inference-Server]] | [[company/NVIDIA/NVIDIA|NVIDIA]] | 发起 / 主导 |
| [[vLLM]] | [[company/Inferact/Inferact|Inferact]] · [[company/Red Hat/Red Hat|Red Hat]] · [[company/Meta/Meta|Meta]] · [[company/Hugging Face/Hugging Face|Hugging Face]] · [[company/TensorMesh/TensorMesh|TensorMesh]] | 跨公司 core contributor 网络 |
| [[SGLang]] | [[company/RadixArk/RadixArk|RadixArk]] | core maintainer / 产业化网络 |
| [[LMCache]] | [[company/TensorMesh/TensorMesh|TensorMesh]] | research → startup core network |
| [[Mooncake]] | [[company/Moonshot-AI/Moonshot-AI|Moonshot AI]] | 产学共研 / production workload |
| [[Ray-Serve]] | [[company/Anyscale/Anyscale|Anyscale]] | core commercial / maintainer ecosystem |
| [[TokenSpeed]] | [[company/NVIDIA/NVIDIA|NVIDIA]] · [[company/AMD/AMD|AMD]] · [[company/Together AI/Together AI|Together AI]] · [[company/Alibaba Cloud/Alibaba Cloud|Alibaba Cloud]] | 跨公司共同创建/协作 |
| [[HAMi]] | [[company/4Paradigm/4Paradigm|4Paradigm]] · [[company/Dynamia/Dynamia|Dynamia]] · [[company/DaoCloud/DaoCloud|DaoCloud]] · [[company/NVIDIA/NVIDIA|NVIDIA]] · [[company/Huawei/Huawei|Huawei]] | originator + 跨公司 maintainer/contributor |
| [[KTransformers]] | [[company/Approaching.AI/Approaching.AI|Approaching.AI]] | 产业/学术核心网络 |
| [[VCCL]] | [[company/基流科技/基流科技|基流科技]] | 产业/研究共建 |
| [[OneFlow]] | [[company/OneFlow Inc/OneFlow Inc|OneFlow Inc]] | 原始开发 / 主导 |
| [[vLLM-Ascend]] / [[MindIE-LLM]] / [[MindIE-Motor]] / [[MindIE-SD]] / [[msModelSlim]] / [[ops-transformer]] | [[company/Huawei/Huawei|Huawei]] | Ascend/CANN/MindIE 核心贡献 |
| [[llm-d]] | [[company/Red Hat/Red Hat|Red Hat]] · [[company/Google/Google|Google]] · [[company/IBM/IBM|IBM]] · [[company/CoreWeave/CoreWeave|CoreWeave]] · [[company/NVIDIA/NVIDIA|NVIDIA]] | founding contributors |
| [[LightLLM]] | 暂无单一主要公司 | ModelTC 社区主导 |
| [[FlashInfer]] | 暂无单一主要公司 | 学术/开源社区 + 产业贡献 |
| [[TileLang]] | 暂无单一主要公司 | 北大/MSRA 研究起源 |

## Serving Engine
[[vLLM]] · [[SGLang]] · [[TensorRT-LLM]] · [[LightLLM]] · [[Ray-Serve]] · [[TokenSpeed]]

## Distributed Training / Framework
[[OneFlow]] · [[Colossal-AI]]

## Compiler / Kernel DSL
[[TileLang]]

## Kernel / Communication / KV
[[FlashInfer]] · [[VCCL]] · [[DeepSeek-Infra]] · [[LMCache]] · [[Mooncake]] · [[NIXL]]

## Distributed / Cloud Native
[[Dynamo]] · [[llm-d]] · [[AIBrix]] · [[Triton-Inference-Server]]

## Ascend Inference Optimization
[[vLLM-Ascend]] · [[ops-transformer]] · [[MindIE-LLM]] · [[MindIE-Motor]] · [[MindIE-SD]] · [[msModelSlim]]

## Hardware / Heterogeneous
[[HAMi]] · [[KTransformers]]

旧 `Communities/` 重复索引已移除；vLLM、SGLang、OneFlow、Colossal-AI、VCCL、TileLang 等均以各自主目录中的实体同名文件作为 canonical 社区节点。
