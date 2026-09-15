# Company / Project → Person Reverse Coverage

由 `scripts/audit-entity-reverse-links.py` 自动生成。公司反向边来自人物 `current_affiliations:`；项目/社区反向边来自人物 `projects:` / `communities:`。

- Company nodes: 40
- Companies with ≥1 linked person: 30
- Company-person associations: 132
- Project/community nodes: 46
- Project/community nodes with ≥1 linked person: 28
- Project/community-person associations: 190
- Unresolved source values (backlog, non-fatal): 41
- Audit errors: 0

## Companies

| Company | Linked people |
| --- | ---: |
| [[company/NVIDIA/NVIDIA|NVIDIA]] | 30 |
| [[company/趋境科技/趋境科技|趋境科技]] | 12 |
| [[company/清程极智/清程极智|清程极智]] | 7 |
| [[company/Inferact/Inferact|Inferact]] | 6 |
| [[company/IBM/IBM|IBM]] | 5 |
| [[company/Red Hat/Red Hat|Red Hat]] | 5 |
| [[company/基流科技/基流科技|基流科技（InfraWaves）]] | 5 |
| [[company/智谱/智谱|智谱]] | 5 |
| [[company/OpenAI/OpenAI|OpenAI]] | 4 |
| [[company/商汤科技/商汤科技|商汤科技]] | 4 |
| [[company/无问芯穹/无问芯穹|无问芯穹]] | 4 |
| [[company/月之暗面/月之暗面|月之暗面]] | 4 |
| [[company/深度求索/深度求索|深度求索]] | 4 |
| [[company/硅基流动/硅基流动|硅基流动]] | 4 |
| [[company/阿里巴巴/阿里巴巴|阿里巴巴]] | 4 |
| [[company/Google/Google|Google]] | 3 |
| [[company/Meta/Meta|Meta]] | 3 |
| [[company/TensorMesh/TensorMesh|TensorMesh]] | 3 |
| [[company/字节跳动/字节跳动|字节跳动]] | 3 |
| [[company/清昴智能/清昴智能|清昴智能]] | 3 |
| [[company/RadixArk/RadixArk|RadixArk]] | 2 |
| [[company/Together AI/Together AI|Together AI]] | 2 |
| [[company/派欧云/派欧云|派欧云]] | 2 |
| [[company/潞晨科技/潞晨科技|潞晨科技]] | 2 |
| [[company/AMD/AMD|AMD]] | 1 |
| [[company/Amazon/Amazon|Amazon / AWS]] | 1 |
| [[company/Databricks/Databricks|Databricks]] | 1 |
| [[company/HPE/HPE|HPE]] | 1 |
| [[company/Hugging Face/Hugging Face|Hugging Face]] | 1 |
| [[company/道客/道客|道客]] | 1 |

## Projects / communities

| Entity | Linked people |
| --- | ---: |
| [[community/deepseek-ai/DeepSeek-Infra/DeepSeek-Infra|DeepSeek Infra]] | 16 |
| [[community/vllm-project/vLLM/vLLM|vLLM]] | 15 |
| [[community/llm-d/llm-d/llm-d|llm-d]] | 13 |
| [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]] | 12 |
| [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] | 11 |
| [[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] | 11 |
| [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] | 11 |
| [[community/sgl-project/SGLang/SGLang|SGLang]] | 10 |
| [[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] | 10 |
| [[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] | 9 |
| [[community/ModelTC/LightLLM/LightLLM|LightLLM]] | 9 |
| [[community/ai-dynamo/NIXL/NIXL|NIXL]] | 9 |
| [[community/vllm-project/AIBrix/AIBrix|AIBrix]] | 7 |
| [[community/flagos-ai/FlagOS/FlagOS|FlagOS]] | 6 |
| [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] | 6 |
| [[community/hpcaitech/Colossal-AI/Colossal-AI|Colossal-AI]] | 5 |
| [[community/flagos-ai/FlagScale/FlagScale|FlagScale]] | 4 |
| [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]] | 4 |
| [[community/sii-research/VCCL/VCCL|VCCL]] | 4 |
| [[community/deepseek-ai/DeepSeek-Infra/DeepJIT|DeepJIT]] | 3 |
| [[community/LMCache/LMCache/LMCache|LMCache]] | 3 |
| [[community/Ascend/ops-transformer/ops-transformer|ops-transformer]] | 3 |
| [[community/flagos-ai/FlagCX/FlagCX|FlagCX]] | 2 |
| [[community/flagos-ai/FlagGems/FlagGems|FlagGems]] | 2 |
| [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]] | 2 |
| [[community/flagos-ai/FlagAttention/FlagAttention|FlagAttention]] | 1 |
| [[community/ray-project/Ray/Ray|Ray]] | 1 |
| [[community/lightseekorg/TokenSpeed/TokenSpeed|TokenSpeed]] | 1 |

## Unresolved source values

这些值尚未安全解析到 canonical company/project/community 节点，不自动造边。

- `company/Inferact/Ion Stoica.md` · `affiliation` → `UC Berkeley`
- `company/Inferact/Joseph Gonzalez.md` · `affiliation` → `UC Berkeley`
- `company/RadixArk/盛颖 Ying Sheng.md` · `communities` → `LMSYS`
- `company/无问芯穹/汪玉 Yu Wang.md` · `affiliation` → `Tsinghua University`
- `company/智谱/唐杰 Jie Tang.md` · `affiliation` → `Tsinghua University`
- `company/清昴智能/朱文武 Wenwu Zhu.md` · `affiliation` → `Tsinghua University`
- `company/清程极智/翟季冬 Jidong Zhai.md` · `affiliation` → `Tsinghua University`
- `company/清程极智/郑纬民 Weimin Zheng.md` · `affiliation` → `Tsinghua University`
- `company/趋境科技/Hongbo Kang.md` · `affiliation` → `Tsinghua University`
- `company/趋境科技/武永卫 Yongwei Wu.md` · `affiliation` → `Tsinghua University`
- `company/阿里巴巴/唐天一 Tianyi Tang.md` · `affiliation` → `Qwen`
- `community/flagos-ai/FlagOS/敖玉龙 Yulong Ao.md` · `affiliation` → `北京智源人工智能研究院`
- `community/kvcache-ai/KTransformers/Boxin Zhang.md` · `affiliation` → `MADSys Lab, Tsinghua University`
- `community/kvcache-ai/KTransformers/Hongtao Chen.md` · `affiliation` → `MADSys Lab, Tsinghua University`
- `community/kvcache-ai/KTransformers/Jianwei Dong.md` · `affiliation` → `MADSys Lab, Tsinghua University`
- `community/kvcache-ai/KTransformers/Jingqi Tang.md` · `affiliation` → `MADSys Lab, Tsinghua University`
- `community/kvcache-ai/KTransformers/Qingliang Ou.md` · `affiliation` → `MADSys Lab, Tsinghua University`
- `community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie.md` · `affiliation` → `Tsinghua University`
- `community/llm-d/llm-d/Ashok Chandrasekar.md` · `communities` → `Kubernetes`
- `community/llm-d/llm-d/Maroon Ayoub.md` · `affiliation` → `IBM Research`
- `community/sgl-project/SGLang/Shenggui Li.md` · `communities` → `SpecForge`
- `community/sgl-project/SGLang/Yineng Zhang.md` · `affiliation` → `LightSeek Foundation`
- `community/sgl-project/SGLang/郑连民 Lianmin Zheng.md` · `communities` → `LMSYS`
- `community/vllm-project/vLLM/Patrick von Platen.md` · `communities` → `Hugging Face`
- `university/上海交通大学/Fan Wu.md` · `affiliation` → `Shanghai Jiao Tong University`
- `university/上海交通大学/Haibo Chen.md` · `affiliation` → `Shanghai Jiao Tong University`
- `university/上海交通大学/Rong Chen.md` · `affiliation` → `Shanghai Jiao Tong University`
- `university/上海交通大学/Rongxin Cheng.md` · `affiliation` → `Shanghai Jiao Tong University`
- `university/上海交通大学/Shengzhong Liu.md` · `affiliation` → `Shanghai Jiao Tong University`
- `university/上海交通大学/Xingda Wei.md` · `affiliation` → `Shanghai Jiao Tong University`
- `university/北京大学/Lei Wang.md` · `affiliation` → `Peking University / Tile-AI`
- `university/北京大学/吴童 Tong Wu.md` · `affiliation` → `Peking University / Tile-AI`
- `university/北京大学/杨智 Zhi Yang.md` · `affiliation` → `Peking University`
- `university/北京大学/程羽 Yu Cheng.md` · `affiliation` → `Peking University`
- `university/北京大学/马凌霄 Lingxiao Ma.md` · `affiliation` → `Microsoft Research Asia`
- `university/浙江大学/Huan Li.md` · `affiliation` → `浙江大学`
- `university/浙江大学/Jue Wang.md` · `affiliation` → `浙江大学`
- `university/浙江大学/Lidan Shou.md` · `affiliation` → `浙江大学`
- `university/浙江大学/Zheng Li.md` · `affiliation` → `浙江大学`
- `university/清华大学/Mingxing Zhang.md` · `affiliation` → `Tsinghua University`
- `university/清华大学/Ruoyu Qin.md` · `affiliation` → `Tsinghua University`
