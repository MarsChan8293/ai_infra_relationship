# community

AI 推理引擎、训练系统、GPU/NPU kernel、AI compiler、量化、KV Cache、数据传输、集合通信、分布式 serving 与异构计算等开源社区与技术项目的一级分类入口。

## 目录组织规则
`community/` 按 canonical upstream namespace / 治理组织分层，而不是把每个项目直接平铺在一级目录。结构统一为：

`community/<organization>/<project>/...`

`organization` 优先采用项目实际使用的上游 GitHub / GitCode namespace 或明确治理组织，而不是按技术类别或主要贡献公司机械归类。例如 NVIDIA 发起的 Dynamo / NIXL 位于 `ai-dynamo`，而不是因公司关系统一塞进 `NVIDIA`。短双链继续使用项目 basename，目录迁移不改变 canonical 项目名。

### 组织 → 项目
- `vllm-project`：[[AIBrix]] · [[vLLM]] · [[vLLM-Ascend]]
- `ai-dynamo`：[[Dynamo]] · [[NIXL]]
- `kvcache-ai`：[[KTransformers]] · [[Mooncake]]
- `Ascend`：[[MindIE-LLM]] · [[MindIE-Motor]] · [[MindIE-SD]] · [[msModelSlim]] · [[ops-transformer]]
- `deepseek-ai`：[[DeepSeek-Infra]] / 3FS / DeepEP / DeepGEMM / DeepJIT / FlashMLA
- `hpcaitech`：[[Colossal-AI]]
- `flashinfer-ai`：[[FlashInfer]]
- `Project-HAMi`：[[HAMi]]
- `LMCache`：[[LMCache]]
- `ModelTC`：[[LightLLM]]
- `Oneflow-Inc`：[[OneFlow]]
- `ray-project`：[[Ray-Serve]]
- `sgl-project`：[[SGLang]]
- `NVIDIA`：[[TensorRT-LLM]]
- `tile-ai`：[[TileLang]]
- `lightseekorg`：[[TokenSpeed]]
- `triton-inference-server`：[[Triton-Inference-Server]]
- `sii-research`：[[VCCL]]
- `llm-d`：[[llm-d]]

## 公司关系字段
所有项目主节点统一使用 `companies` 表示**主要公司贡献/维护关系**，并用 `company_relation` 描述关系性质。`companies` 不是赞助商、用户或兼容厂商列表；只有原始发起、founding contributor、core maintainer network、长期工程贡献等强证据才进入。学术/社区主导且没有明确主要公司的项目使用 `companies: []`。`companies` 使用公司 canonical 实体名；中国公司统一使用中文 canonical 名称。

常见关系：`company-originated` · `company-led` · `founding-contributors` · `cross-company-core-contributors` · `core-maintainer-network` · `industry-academia-co-development` · `community-led`。

## 项目 → 主要贡献公司
| 项目 | 主要公司 | 关系 |
| --- | --- | --- |
| [[AIBrix]] | [[company/字节跳动/字节跳动|字节跳动]] | 原始开发 / 发起 |
| [[Colossal-AI]] | [[company/潞晨科技/潞晨科技|潞晨科技]] | 发起 / 主导 |
| [[DeepSeek-Infra]] / 3FS / DeepEP / DeepGEMM / DeepJIT / FlashMLA | [[company/深度求索/深度求索|深度求索]] | 发起 / 主导 |
| [[Dynamo]] / [[NIXL]] / [[TensorRT-LLM]] / [[Triton-Inference-Server]] | [[company/NVIDIA/NVIDIA|NVIDIA]] | 发起 / 主导 |
| [[vLLM]] | [[company/Inferact/Inferact|Inferact]] · [[company/Red Hat/Red Hat|Red Hat]] · [[company/Meta/Meta|Meta]] · [[company/Hugging Face/Hugging Face|Hugging Face]] · [[company/TensorMesh/TensorMesh|TensorMesh]] | 跨公司 core contributor 网络 |
| [[SGLang]] | [[company/RadixArk/RadixArk|RadixArk]] | core maintainer / 产业化网络 |
| [[LMCache]] | [[company/TensorMesh/TensorMesh|TensorMesh]] | research → startup core network |
| [[Mooncake]] | [[company/月之暗面/月之暗面|月之暗面]] | 产学共研 / production workload |
| [[Ray-Serve]] | [[company/Anyscale/Anyscale|Anyscale]] | core commercial / maintainer ecosystem |
| [[TokenSpeed]] | [[company/NVIDIA/NVIDIA|NVIDIA]] · [[company/AMD/AMD|AMD]] · [[company/Together AI/Together AI|Together AI]] · [[company/阿里巴巴/阿里巴巴|阿里巴巴]] | 跨公司共同创建/协作 |
| [[HAMi]] | [[company/第四范式/第四范式|第四范式]] · [[company/密瓜智能/密瓜智能|密瓜智能]] · [[company/道客/道客|道客]] · [[company/NVIDIA/NVIDIA|NVIDIA]] · [[company/华为/华为|华为]] | originator + 跨公司 maintainer/contributor |
| [[KTransformers]] | [[company/趋境科技/趋境科技|趋境科技]] | 产业/学术核心网络 |
| [[VCCL]] | [[company/基流科技/基流科技|基流科技]] | 产业/研究共建 |
| [[OneFlow]] | [[company/一流科技/一流科技|一流科技]] | 原始开发 / 主导 |
| [[vLLM-Ascend]] / [[MindIE-LLM]] / [[MindIE-Motor]] / [[MindIE-SD]] / [[msModelSlim]] / [[ops-transformer]] | [[company/华为/华为|华为]] | Ascend/CANN/MindIE 核心贡献 |
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

旧 `Communities/` 重复索引已移除；项目实体仍以项目同名文件作为 canonical 节点，但物理目录统一归入上游 organization / namespace。
