# Company / Project → Person Reverse Coverage

由 `scripts/audit-entity-reverse-links.py` 自动生成。公司人物边来自人物 `current_affiliations:` 与 `email_affiliations:` 的并集；后者由公开职业邮箱域名规则生成，不单独代表当前任职。项目/社区反向边来自人物 `projects:` / `communities:`。

- Company nodes: 50
- Companies with ≥1 linked person: 42
- Company-person associations: 207
- Email-domain-supported associations: 27
- People with generated linked_companies: 206
- Project/community nodes: 106
- Project/community nodes with ≥1 linked person: 76
- Project/community-person associations: 392
- Non-company affiliations recognized and routed elsewhere: 68
- Unresolved source values (backlog, non-fatal): 4
- Audit errors: 0

## Companies

| Company | Linked people |
| --- | ---: |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | 32 |
| [[company/华为/华为|华为]] | 20 |
| [[company/趋境科技/趋境科技|趋境科技]] | 16 |
| [[company/Inferact/Inferact|Inferact]] | 9 |
| [[company/Red Hat/Red Hat|Red Hat]] | 9 |
| [[company/RadixArk/RadixArk|RadixArk]] | 8 |
| [[company/清程极智/清程极智|清程极智]] | 8 |
| [[company/字节跳动/字节跳动|字节跳动]] | 7 |
| [[company/阿里巴巴/阿里巴巴|阿里巴巴]] | 7 |
| [[company/IBM/IBM|IBM]] | 6 |
| [[company/深度求索/深度求索|深度求索]] | 6 |
| [[company/硅基流动/硅基流动|硅基流动]] | 6 |
| [[company/TensorMesh/TensorMesh|TensorMesh]] | 5 |
| [[company/基流科技/基流科技|基流科技（InfraWaves）]] | 5 |
| [[company/智谱/智谱|智谱]] | 5 |
| [[company/月之暗面/月之暗面|月之暗面]] | 5 |
| [[company/OpenAI/OpenAI|OpenAI]] | 4 |
| [[company/商汤科技/商汤科技|商汤科技]] | 4 |
| [[company/无问芯穹/无问芯穹|无问芯穹]] | 4 |
| [[company/Google/Google|Google]] | 3 |
| [[company/Meta/Meta|Meta]] | 3 |
| [[company/派欧云/派欧云|派欧云]] | 3 |
| [[company/清昴智能/清昴智能|清昴智能]] | 3 |
| [[company/腾讯/腾讯|腾讯]] | 3 |
| [[company/AMD/AMD|AMD]] | 2 |
| [[company/Hugging Face/Hugging Face|Hugging Face]] | 2 |
| [[company/Ollama/Ollama|Ollama]] | 2 |
| [[company/Together AI/Together AI|Together AI]] | 2 |
| [[company/天数智芯/天数智芯|天数智芯]] | 2 |
| [[company/密瓜智能/密瓜智能|密瓜智能]] | 2 |
| [[company/沐曦/沐曦|沐曦]] | 2 |
| [[company/潞晨科技/潞晨科技|潞晨科技]] | 2 |
| [[company/Amazon/Amazon|Amazon / AWS]] | 1 |
| [[company/Databricks/Databricks|Databricks]] | 1 |
| [[company/GPUStack/GPUStack|GPUStack]] | 1 |
| [[company/HPE/HPE|HPE]] | 1 |
| [[company/Intel/Intel|Intel]] | 1 |
| [[company/Samsung/Samsung|Samsung]] | 1 |
| [[company/摩尔线程/摩尔线程|摩尔线程]] | 1 |
| [[company/积算科技/积算科技|积算科技]] | 1 |
| [[company/道客/道客|道客]] | 1 |
| [[company/面壁智能/面壁智能|面壁智能]] | 1 |

## Projects / communities

| Entity | Linked people |
| --- | ---: |
| [[community/sgl-project/SGLang/SGLang|SGLang]] | 29 |
| [[community/vllm-project/vLLM/vLLM|vLLM]] | 29 |
| [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] | 21 |
| [[community/LMCache/LMCache/LMCache|LMCache]] | 19 |
| [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]] | 18 |
| [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]] | 17 |
| [[community/deepseek-ai/DeepSeek-Infra/DeepSeek-Infra|DeepSeek Infra]] | 16 |
| [[community/llm-d/llm-d/llm-d|llm-d]] | 15 |
| [[community/Ascend/MemCache/MemCache|MemCache]] | 14 |
| [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] | 11 |
| [[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] | 11 |
| [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] | 11 |
| [[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] | 10 |
| [[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] | 9 |
| [[community/ModelTC/LightLLM/LightLLM|LightLLM]] | 9 |
| [[community/ai-dynamo/NIXL/NIXL|NIXL]] | 9 |
| [[community/vllm-project/AIBrix/AIBrix|AIBrix]] | 7 |
| [[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]] | 7 |
| [[community/flagos-ai/FlagOS/FlagOS|FlagOS]] | 6 |
| [[community/flagos-ai/FlagTree/FlagTree|FlagTree]] | 6 |
| [[community/Ascend/MemFabric/MemFabric|MemFabric]] | 6 |
| [[community/hpcaitech/Colossal-AI/Colossal-AI|Colossal-AI]] | 5 |
| [[community/vllm-project/Jenga/Jenga|Jenga]] | 5 |
| [[community/kvcache-ai/Mooncake/TENT|TENT]] | 5 |
| [[community/flagos-ai/FlagScale/FlagScale|FlagScale]] | 4 |
| [[community/Project-HAMi/HAMi/HAMi|HAMi]] | 4 |
| [[community/tile-ai/TileLang/TileLang|TileLang]] | 4 |
| [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]] | 4 |
| [[community/sii-research/VCCL/VCCL|VCCL]] | 4 |
| [[community/deepseek-ai/DeepSeek-Infra/DeepJIT|DeepJIT]] | 3 |
| [[community/InternLM/LMDeploy/LMDeploy|LMDeploy]] | 3 |
| [[community/radixark/Miles/Miles|Miles]] | 3 |
| [[company/月之暗面/Seer|Seer]] | 3 |
| [[community/Ascend/ops-transformer/ops-transformer|ops-transformer]] | 3 |
| [[community/Deep-Spark/DeepSpark/DeepSpark|DeepSpark]] | 2 |
| [[community/Deep-Spark/DeepSparkInference/DeepSparkInference|DeepSparkInference]] | 2 |
| [[community/deepseek-ai/DualPath/DualPath|DualPath]] | 2 |
| [[university/清华大学/FastDecode|FastDecode]] | 2 |
| [[community/flagos-ai/FlagCX/FlagCX|FlagCX]] | 2 |
| [[community/flagos-ai/FlagGems/FlagGems|FlagGems]] | 2 |
| [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]] | 2 |
| [[university/浙江大学/FloE|FloE]] | 2 |
| [[community/FlashML-org/FreeToken/FreeToken|FreeToken]] | 2 |
| [[community/Project-HAMi/ascend-device-plugin/ascend-device-plugin|HAMi Ascend Device Plugin]] | 2 |
| [[community/InfiniTensor/InfiniTensor|InfiniTensor]] | 2 |
| [[community/lmsys-org/LMSYS/LMSYS|LMSYS]] | 2 |
| [[university/香港中文大学/LiveServe|LiveServe]] | 2 |
| [[community/MetaX-MACA/MetaX-MACA/MetaX-MACA|MetaX-MACA]] | 2 |
| [[university/UC Berkeley/MoE-Lightning|MoE-Lightning]] | 2 |
| [[community/ollama/Ollama/Ollama|Ollama]] | 2 |
| [[community/Oneflow-Inc/OneFlow/OneFlow|OneFlow]] | 2 |
| [[community/ray-project/Ray/Ray|Ray]] | 2 |
| [[community/tile-ai/TileScale/TileScale|TileScale]] | 2 |
| [[community/openEuler/openYuanRong/openYuanRong|openYuanRong]] | 2 |
| [[community/thu-pacman/BaGuaLu/BaGuaLu|BaGuaLu]] | 1 |
| [[community/thu-pacman/Chitu/Chitu|Chitu]] | 1 |
| [[community/deepseek-ai/DeepSpec/DeepSpec|DeepSpec]] | 1 |
| [[community/flagos-ai/FlagAttention/FlagAttention|FlagAttention]] | 1 |
| [[community/taco-project/FlexKV/FlexKV|FlexKV]] | 1 |
| [[community/gpustack/GPUStack/GPUStack|GPUStack]] | 1 |
| [[university/浙江大学/HMI|HMI]] | 1 |
| [[community/cloud-native/Kubernetes/Kubernetes|Kubernetes]] | 1 |
| [[university/上海交通大学/KunServe|KunServe]] | 1 |
| [[company/Together AI/Ladder Residual|Ladder Residual]] | 1 |
| [[community/lightseekorg/LightSeek-Foundation/LightSeek-Foundation|LightSeek Foundation]] | 1 |
| [[community/MooreThreads/MUSA/MUSA|MUSA]] | 1 |
| [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | 1 |
| [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]] | 1 |
| [[community/sgl-project/SpecForge/SpecForge|SpecForge]] | 1 |
| [[community/lightseekorg/TokenSpeed/TokenSpeed|TokenSpeed]] | 1 |
| [[community/Ascend/TransferQueue/TransferQueue|TransferQueue]] | 1 |
| [[community/verl-project/VeRL-Omni/VeRL-Omni|VeRL-Omni]] | 1 |
| [[community/ggml-org/ggml/ggml|ggml]] | 1 |
| [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] | 1 |
| [[community/MetaX-MACA/vLLM-metax/vLLM-metax|vLLM-metax]] | 1 |
| [[community/MooreThreads/vllm-musa/vllm-musa|vllm-musa]] | 1 |

## Unresolved source values

这些值尚未安全解析到 canonical company/project/community 节点，不自动造边。

- `university/UC Berkeley/Shuo Yang.md` · `affiliation` → `Sky Computing Lab`
- `university/UC Berkeley/Shuo Yang.md` · `affiliation` → `LMSYS`
- `university/上海交通大学/Xiaoze Fan.md` · `affiliation` → `UC Berkeley Sky Computing Lab`
- `university/清华大学/Weichao Guo.md` · `affiliation` → `OPPO`
