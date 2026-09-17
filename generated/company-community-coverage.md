# Company ↔ Community / Project Coverage

由 `scripts/audit-company-community-links.py` 自动生成。人工事实来自公司 `projects:` / `communities:` 与社区/项目 `companies:` / `company:`；派生镜像分别写入 `linked_projects:` 与 `linked_companies:`。员工个人参与不会自动升级为公司级关系。模型团队/模型项目会被识别为合法的公司项目值，但不进入本社区关系层。

- Company nodes: 50
- Companies with ≥1 linked project/community: 38
- Project/community nodes: 111
- Project/community nodes with ≥1 linked company: 67
- Bidirectional association pairs: 86
- Explicitly asserted on both sides: 86
- Company-side only explicit assertions: 0
- Entity-side only explicit assertions: 0
- Recognized non-community project targets: 4
- Unresolved explicit source values: 0
- Audit errors: 0

| Company | Community / project | Type | Relation | Explicit source |
| --- | --- | --- | --- | --- |
| [[company/AMD/AMD|AMD]] | [[community/lightseekorg/TokenSpeed/TokenSpeed|TokenSpeed]] | project | cross-company-co-creation | both |
| [[company/Anyscale/Anyscale|Anyscale]] | [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]] | project | core-commercial-ecosystem | both |
| [[company/CoreWeave/CoreWeave|CoreWeave]] | [[community/llm-d/llm-d/llm-d|llm-d]] | project | founding-contributors | both |
| [[company/Google/Google|Google]] | [[community/llm-d/llm-d/llm-d|llm-d]] | project | founding-contributors | both |
| [[company/GPUStack/GPUStack|GPUStack]] | [[community/gpustack/GPUStack/GPUStack|GPUStack]] | project |  | both |
| [[company/HPE/HPE|HPE]] | [[community/ai-dynamo/NIXL/NIXL|NIXL]] | project | company-led | both |
| [[company/Hugging Face/Hugging Face|Hugging Face]] | [[community/ggml-org/ggml/ggml|ggml]] | project | joined-hugging-face-maintainer-team | both |
| [[company/Hugging Face/Hugging Face|Hugging Face]] | [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] | project | joined-hugging-face-maintainer-team | both |
| [[company/Hugging Face/Hugging Face|Hugging Face]] | [[community/vllm-project/vLLM/vLLM|vLLM]] | project | cross-company-core-contributors | both |
| [[company/IBM/IBM|IBM]] | [[community/llm-d/llm-d/llm-d|llm-d]] | project | founding-contributors | both |
| [[company/Inferact/Inferact|Inferact]] | [[community/vllm-project/vLLM/vLLM|vLLM]] | project | cross-company-core-contributors | both |
| [[company/Intel/Intel|Intel]] | [[company/Intel/OpenVINO|OpenVINO]] | project | company-led | both |
| [[company/Intel/Intel|Intel]] | [[company/Intel/OpenVINO GenAI|OpenVINO GenAI]] | project | company-led | both |
| [[company/Intel/Intel|Intel]] | [[company/Intel/xFasterTransformer|xFasterTransformer]] | project | company-led | both |
| [[company/Meta/Meta|Meta]] | [[community/vllm-project/vLLM/vLLM|vLLM]] | project | cross-company-core-contributors | both |
| [[company/Neural Magic/Neural Magic|Neural Magic]] | [[community/vllm-project/vLLM/vLLM|vLLM]] | project | cross-company-core-contributors | both |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | [[community/Project-HAMi/HAMi/HAMi|HAMi]] | project | cross-company-maintainer-network | both |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | [[community/llm-d/llm-d/llm-d|llm-d]] | project | founding-contributors | both |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | [[community/ai-dynamo/NIXL/NIXL|NIXL]] | project | company-led | both |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] | project | company-led | both |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | [[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] | project | company-led | both |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | [[community/lightseekorg/TokenSpeed/TokenSpeed|TokenSpeed]] | project | cross-company-co-creation | both |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]] | project | company-led | both |
| [[company/Ollama/Ollama|Ollama]] | [[community/ollama/Ollama/Ollama|Ollama]] | project | company-originated | both |
| [[company/RadixArk/RadixArk|RadixArk]] | [[community/radixark/Miles/Miles|Miles]] | project | company-led | both |
| [[company/RadixArk/RadixArk|RadixArk]] | [[community/sgl-project/SGLang/SGLang|SGLang]] | project | core-maintainer-network | both |
| [[company/Red Hat/Red Hat|Red Hat]] | [[community/llm-d/llm-d/llm-d|llm-d]] | project | founding-contributors | both |
| [[company/Red Hat/Red Hat|Red Hat]] | [[community/vllm-project/vLLM/vLLM|vLLM]] | project | cross-company-core-contributors | both |
| [[company/TensorMesh/TensorMesh|TensorMesh]] | [[community/LMCache/LMCache/LMCache|LMCache]] | project | research-to-startup-core-network | both |
| [[company/TensorMesh/TensorMesh|TensorMesh]] | [[community/vllm-project/vLLM/vLLM|vLLM]] | project | cross-company-core-contributors | both |
| [[company/Together AI/Together AI|Together AI]] | [[company/Together AI/Ladder Residual|Ladder Residual]] | project | research-collaboration | both |
| [[company/Together AI/Together AI|Together AI]] | [[community/lightseekorg/TokenSpeed/TokenSpeed|TokenSpeed]] | project | cross-company-co-creation | both |
| [[company/一流科技/一流科技|一流科技]] | [[community/Oneflow-Inc/OneFlow/OneFlow|OneFlow]] | project | company-originated | both |
| [[company/华为/华为|华为]] | [[community/Ascend/CANN/CANN|CANN]] | project | company-led | both |
| [[company/华为/华为|华为]] | [[community/Project-HAMi/HAMi/HAMi|HAMi]] | project | cross-company-maintainer-network | both |
| [[company/华为/华为|华为]] | [[community/Ascend/MemCache/MemCache|MemCache]] | project | company-led | both |
| [[company/华为/华为|华为]] | [[community/Ascend/MemFabric/MemFabric|MemFabric]] | project | company-led | both |
| [[company/华为/华为|华为]] | [[community/Ascend/MindIE-LLM/MindIE-LLM|MindIE-LLM]] | project | company-led | both |
| [[company/华为/华为|华为]] | [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | project | company-led | both |
| [[company/华为/华为|华为]] | [[community/Ascend/MindIE-SD/MindIE-SD|MindIE-SD]] | project | company-led | both |
| [[company/华为/华为|华为]] | [[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] | project | company-led | both |
| [[company/华为/华为|华为]] | [[community/openEuler/openYuanRong/openYuanRong|openYuanRong]] | project | company-originated-open-source | both |
| [[company/华为/华为|华为]] | [[community/Ascend/ops-transformer/ops-transformer|ops-transformer]] | project | company-led | both |
| [[company/华为/华为|华为]] | [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]] | project | hardware-ecosystem-core-contributor | both |
| [[company/商汤科技/商汤科技|商汤科技]] | [[community/ModelTC/LightLLM/LightLLM|LightLLM]] | project | community-led | both |
| [[company/基流科技/基流科技|基流科技（InfraWaves）]] | [[community/sii-research/VCCL/VCCL|VCCL]] | project | industry-research-co-development | both |
| [[company/天数智芯/天数智芯|天数智芯]] | [[community/Deep-Spark/DeepSparkInference/DeepSparkInference|DeepSparkInference]] | project | company-originated | both |
| [[company/天数智芯/天数智芯|天数智芯]] | [[community/Deep-Spark/iluvatar-corex-ixrt/iluvatar-corex-ixrt|iluvatar-corex-ixrt]] | project | company-led | both |
| [[company/天数智芯/天数智芯|天数智芯]] | [[community/Deep-Spark/lmcache-iluvatar/lmcache-iluvatar|lmcache-iluvatar]] | project | company-originated | both |
| [[company/字节跳动/字节跳动|字节跳动]] | [[community/vllm-project/AIBrix/AIBrix|AIBrix]] | project | company-originated | both |
| [[company/密瓜智能/密瓜智能|密瓜智能]] | [[community/Project-HAMi/HAMi/HAMi|HAMi]] | project | cross-company-maintainer-network | both |
| [[company/摩尔线程/摩尔线程|摩尔线程]] | [[community/MooreThreads/MATE/MATE|MATE]] | project | company-led | both |
| [[company/摩尔线程/摩尔线程|摩尔线程]] | [[community/MooreThreads/torch_musa/torch_musa|torch_musa]] | project | company-led | both |
| [[company/摩尔线程/摩尔线程|摩尔线程]] | [[community/MooreThreads/vllm-musa/vllm-musa|vllm-musa]] | project | company-led | both |
| [[company/月之暗面/月之暗面|月之暗面]] | [[company/月之暗面/checkpoint-engine|Checkpoint Engine]] | infra-project |  | both |
| [[company/月之暗面/月之暗面|月之暗面]] | [[community/kvcache-ai/KVCache.AI/KVCache.AI|KVCache.AI]] | community | industry-academia-co-development | both |
| [[company/月之暗面/月之暗面|月之暗面]] | [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] | project | industry-academia-co-development | both |
| [[company/月之暗面/月之暗面|月之暗面]] | [[company/月之暗面/MoonEP|MoonEP]] | infra-project |  | both |
| [[company/月之暗面/月之暗面|月之暗面]] | [[company/月之暗面/Seer|Seer]] | project | industry-academia-research-collaboration | both |
| [[company/沐曦/沐曦|沐曦]] | [[community/MetaX-MACA/mcoplib/mcoplib|mcoplib]] | project | company-led | both |
| [[company/沐曦/沐曦|沐曦]] | [[community/MetaX-MACA/MXDeepEP/MXDeepEP|MXDeepEP]] | project | company-led | both |
| [[company/沐曦/沐曦|沐曦]] | [[community/MetaX-MACA/vLLM-metax/vLLM-metax|vLLM-metax]] | project | company-led | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] | project | company-led | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] | project | company-led | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] | project | company-led | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DeepSeek-Infra/DeepJIT|DeepJIT]] | project | company-led | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DeepSeek-Infra/DeepSeek-Infra|DeepSeek Infra]] | project-collection | company-led | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DeepSeek-Infra/DeepSelect|DeepSelect]] | project | company-led | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DeepSpec/DeepSpec|DeepSpec]] | project | company-led | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DualPath/DualPath|DualPath]] | project | industry-academia-research-collaboration | both |
| [[company/深度求索/深度求索|深度求索]] | [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]] | project | company-led | both |
| [[company/清程极智/清程极智|清程极智]] | [[community/QingCheng-AI/ascend-kernel/ascend-kernel|ascend-kernel]] | project | company-led | both |
| [[company/清程极智/清程极智|清程极智]] | [[community/thu-pacman/BaGuaLu/BaGuaLu|BaGuaLu]] | project | company-led | both |
| [[company/清程极智/清程极智|清程极智]] | [[community/thu-pacman/Chitu/Chitu|Chitu]] | project | company-originated-and-jointly-open-sourced-with-tsinghua | both |
| [[company/潞晨科技/潞晨科技|潞晨科技]] | [[community/hpcaitech/Colossal-AI/Colossal-AI|Colossal-AI]] | project | company-originated | both |
| [[company/硅基流动/硅基流动|硅基流动]] | [[community/siliconflow/OneDiff/OneDiff|OneDiff]] | project | company-led | both |
| [[company/硅基流动/硅基流动|硅基流动]] | [[community/siliconflow/SiliconLLM/SiliconLLM|SiliconLLM]] | project | company-led | both |
| [[company/第四范式/第四范式|第四范式]] | [[community/Project-HAMi/HAMi/HAMi|HAMi]] | project | cross-company-maintainer-network | both |
| [[company/腾讯/腾讯|腾讯]] | [[community/taco-project/FlexKV/FlexKV|FlexKV]] | project | company-led | both |
| [[company/腾讯/腾讯|腾讯]] | [[community/Tencent/HPC-Ops/HPC-Ops|HPC-Ops]] | project | company-led | both |
| [[company/趋境科技/趋境科技|趋境科技]] | [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]] | project | industry-academia-core-network | both |
| [[company/趋境科技/趋境科技|趋境科技]] | [[community/kvcache-ai/KVCache.AI/KVCache.AI|KVCache.AI]] | community | industry-academia-co-development | both |
| [[company/趋境科技/趋境科技|趋境科技]] | [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] | project | industry-academia-co-development | both |
| [[company/道客/道客|道客]] | [[community/Project-HAMi/HAMi/HAMi|HAMi]] | project | cross-company-maintainer-network | both |
| [[company/阿里巴巴/阿里巴巴|阿里巴巴]] | [[community/lightseekorg/TokenSpeed/TokenSpeed|TokenSpeed]] | project | cross-company-co-creation | both |
| [[company/面壁智能/面壁智能|面壁智能]] | [[company/面壁智能/ForgeTrain|ForgeTrain]] | infra-project |  | both |

## Recognized non-community project targets

- company/阿里巴巴/阿里巴巴.md → `Qwen`
- company/阿里巴巴/阿里巴巴.md → `Qwen3`
- company/阿里巴巴/阿里巴巴.md → `Qwen-Coder`
- company/面壁智能/面壁智能.md → `MiniCPM`
