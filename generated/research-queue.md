# Research Operator Queue

由 `scripts/plan-research-v3.py` 自动生成。仓库只保留三个一级研究方法：`EXPAND`、`DISCOVER`、`VERIFY`。Operator 解释为什么查；relation 解释查什么；strategy 解释去哪查。

- Operators: VERIFY
- Seed: none (global mode)
- Candidate actions: 297
- Selected actions: 177
- History records: 36

## Selected portfolio

| Rank | Operator | Trigger | Source | Type | Relation | Target | Bucket | Priority | History | Why |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | VERIFY | weak_evidence | [[company/xAI/xAI|xAI]] | company | projects | project, community, team | verification | 7.482 | new | coverage 0/3；source type Company；infra: serving/inference, kernel；opens underrepresented target types |
| 2 | VERIFY | weak_evidence | [[university/清华大学/Weimin Zheng|Weimin Zheng]] | person | project_contribution | project, community | verification | 6.711 | new | coverage 1/3；source type Person；infra: serving/inference, kv-cache, distributed；bridge 9.2 |
| 3 | VERIFY | history_followup | [[community/vllm-project/vLLM-Ascend/weijinqian0|Jinqian Wei]] | person | affiliation | company, school, research, team | exploitation | 6.546 | partial | coverage 1/2；source type Person；infra: serving/inference, kv-cache, kernel；opens underrepresented target types |
| 4 | VERIFY | weak_evidence | [[company/Fireworks AI/Fireworks AI|Fireworks AI]] | company | key_people | person | verification | 6.509 | new | coverage 0/4；source type Company；infra: serving/inference, kernel；opens underrepresented target types |
| 5 | VERIFY | weak_evidence | [[university/北京邮电大学/北京邮电大学|北京邮电大学]] | school | labs_or_groups | research, team | verification | 6.157 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |
| 6 | VERIFY | weak_evidence | [[company/道客/道客|道客]] | company | projects | project, community, team | verification | 6.119 | new | coverage 1/3；source type Company；infra: serving/inference, scheduler；opens underrepresented target types |
| 7 | VERIFY | history_followup | [[university/上海交通大学/上海交通大学|上海交通大学]] | school | labs_or_groups | research, team | bridge | 6.099 | partial | coverage 1/2；source type School；infra: serving/inference, kv-cache, distributed；bridge 12.5 |
| 8 | VERIFY | weak_evidence | [[university/电子科技大学/电子科技大学|电子科技大学]] | school | labs_or_groups | research, team | verification | 6.035 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |
| 9 | VERIFY | weak_evidence | [[university/西北工业大学/西北工业大学|西北工业大学]] | school | labs_or_groups | research, team | verification | 6.035 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |
| 10 | VERIFY | weak_evidence | [[company/商汤科技/商汤科技|商汤科技]] | company | projects | project, community, team | verification | 5.660 | new | coverage 1/3；source type Company；infra: serving/inference；opens underrepresented target types |
| 11 | VERIFY | weak_evidence | [[company/字节跳动/字节跳动|字节跳动]] | company | verify_evidence | evidence | verification | 5.622 | new | source coverage 0/2；evidence quality below target |
| 12 | VERIFY | weak_evidence | [[university/南京大学/南京大学|南京大学]] | school | labs_or_groups | research, team | verification | 5.574 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 13 | VERIFY | weak_evidence | [[university/Stony Brook University/Stony Brook University|Stony Brook University]] | school | labs_or_groups | research, team | verification | 5.538 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 14 | VERIFY | weak_evidence | [[company/NVIDIA/NVIDIA|NVIDIA]] | company | verify_evidence | evidence | verification | 5.471 | new | source coverage 0/2；evidence quality below target |
| 15 | VERIFY | weak_evidence | [[university/Binghamton University/Binghamton University|Binghamton University]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 16 | VERIFY | weak_evidence | [[university/Case Western Reserve University/Case Western Reserve University|Case Western Reserve University]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 17 | VERIFY | weak_evidence | [[university/Franklin W. Olin College of Engineering/Franklin W. Olin College of Engineering|Franklin W. Olin College of Engineering]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 18 | VERIFY | weak_evidence | [[university/Lobachevsky State University of Nizhny Novgorod/Lobachevsky State University of Nizhny Novgorod|Lobachevsky State University of Nizhny Novgorod]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 19 | VERIFY | weak_evidence | [[university/Massachusetts Institute of Technology/Massachusetts Institute of Technology|Massachusetts Institute of Technology]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 20 | VERIFY | weak_evidence | [[university/Nanyang Technological University/Nanyang Technological University|Nanyang Technological University]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 21 | VERIFY | weak_evidence | [[university/Seoul National University/Seoul National University|Seoul National University]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 22 | VERIFY | weak_evidence | [[university/Technion - Israel Institute of Technology/Technion - Israel Institute of Technology|Technion - Israel Institute of Technology]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 23 | VERIFY | weak_evidence | [[university/UC Davis/UC Davis|UC Davis]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 24 | VERIFY | weak_evidence | [[university/University of British Columbia/University of British Columbia|University of British Columbia]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 25 | VERIFY | weak_evidence | [[university/华中科技大学/华中科技大学|华中科技大学]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 26 | VERIFY | weak_evidence | [[university/江南大学/江南大学|江南大学]] | school | labs_or_groups | research, team | verification | 5.452 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 27 | VERIFY | weak_evidence | [[university/Georgia Institute of Technology/Georgia Institute of Technology|Georgia Institute of Technology]] | school | labs_or_groups | research, team | verification | 5.421 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 28 | VERIFY | weak_evidence | [[university/University of Washington/University of Washington|University of Washington]] | school | labs_or_groups | research, team | verification | 5.421 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 29 | VERIFY | weak_evidence | [[university/厦门大学/厦门大学|厦门大学]] | school | labs_or_groups | research, team | verification | 5.421 | new | coverage 0/2；source type School；opens underrepresented target types；missing source URLs |
| 30 | VERIFY | weak_evidence | [[company/RadixArk/RadixArk|RadixArk]] | company | projects | project, community, team | verification | 5.410 | new | coverage 2/3；source type Company；infra: serving/inference, kernel；opens underrepresented target types |
| 31 | VERIFY | weak_evidence | [[company/AMD/AMD|AMD]] | company | verify_evidence | evidence | verification | 5.391 | new | source coverage 0/2；evidence quality below target |
| 32 | VERIFY | weak_evidence | [[company/趋境科技/Weiyu Xie|Weiyu Xie]] | person | project_contribution | project, community | verification | 5.247 | new | coverage 1/3；source type Person；infra: kv-cache；bridge 6.5 |
| 33 | VERIFY | weak_evidence | [[company/阿里巴巴/阿里巴巴|阿里巴巴]] | company | verify_evidence | evidence | verification | 5.174 | new | source coverage 0/2；evidence quality below target |
| 34 | VERIFY | weak_evidence | [[university/清华大学/Yongwei Wu|Yongwei Wu]] | person | project_contribution | project, community | verification | 5.068 | new | coverage 2/3；source type Person；infra: serving/inference, moe；bridge 8.7 |
| 35 | VERIFY | weak_evidence | [[company/Meta/Meta|Meta]] | company | projects | project, community, team | verification | 4.930 | new | coverage 2/3；source type Company；infra: serving/inference；opens underrepresented target types |
| 36 | VERIFY | weak_evidence | [[company/HPE/HPE|HPE]] | company | projects | project, community, team | verification | 4.855 | new | coverage 1/3；source type Company；opens underrepresented target types；missing source URLs |
| 37 | VERIFY | weak_evidence | [[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] | project | verify_evidence | evidence | verification | 4.514 | new | source coverage 1/2；evidence quality below target |
| 38 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/NIXL|NIXL]] | project | verify_evidence | evidence | verification | 4.510 | new | source coverage 1/2；evidence quality below target |
| 39 | VERIFY | weak_evidence | [[company/Hugging Face/Hugging Face|Hugging Face]] | company | verify_evidence | evidence | verification | 4.391 | new | source coverage 0/2；evidence quality below target |
| 40 | VERIFY | weak_evidence | [[community/Project-HAMi/HAMi/HAMi|HAMi]] | project | verify_evidence | evidence | verification | 4.379 | new | source coverage 1/2；evidence quality below target |
| 41 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/LightLLM|LightLLM]] | project | verify_evidence | evidence | verification | 4.352 | new | source coverage 1/2；evidence quality below target |
| 42 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] | project | verify_evidence | evidence | verification | 4.343 | new | source coverage 1/2；evidence quality below target |
| 43 | VERIFY | weak_evidence | [[company/Amazon/Amazon|Amazon / AWS]] | company | verify_evidence | evidence | verification | 4.245 | new | source coverage 0/2；evidence quality below target |
| 44 | VERIFY | weak_evidence | [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | project | verify_evidence | evidence | verification | 4.219 | new | source coverage 1/2；evidence quality below target |
| 45 | VERIFY | weak_evidence | [[community/Ascend/ops-transformer/ops-transformer|ops-transformer]] | project | verify_evidence | evidence | verification | 4.219 | new | source coverage 1/2；evidence quality below target |
| 46 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] | project | verify_evidence | evidence | verification | 4.143 | new | source coverage 1/2；evidence quality below target |
| 47 | VERIFY | weak_evidence | [[company/月之暗面/Kimi-K3|Kimi-K3]] | project | verify_evidence | evidence | verification | 4.128 | new | source coverage 1/2；evidence quality below target |
| 48 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]] | project | verify_evidence | evidence | verification | 4.076 | new | source coverage 1/2；evidence quality below target |
| 49 | VERIFY | weak_evidence | [[community/vllm-project/AIBrix/AIBrix|AIBrix]] | project | verify_evidence | evidence | verification | 4.052 | new | source coverage 1/2；evidence quality below target |
| 50 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/DeepJIT|DeepJIT]] | project | verify_evidence | evidence | verification | 4.007 | new | source coverage 1/2；evidence quality below target |
| 51 | VERIFY | weak_evidence | [[community/triton-inference-server/Triton-Inference-Server/Triton-Inference-Server|Triton Inference Server]] | project | verify_evidence | evidence | verification | 3.896 | new | source coverage 1/2；evidence quality below target |
| 52 | VERIFY | weak_evidence | [[company/月之暗面/Kimi-K2|Kimi-K2]] | project | verify_evidence | evidence | verification | 3.842 | new | source coverage 1/2；evidence quality below target |
| 53 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] | project | verify_evidence | evidence | verification | 3.814 | new | source coverage 1/2；evidence quality below target |
| 54 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行]] | person | verify_evidence | evidence | verification | 3.747 | new | source coverage 1/2；evidence quality below target |
| 55 | VERIFY | weak_evidence | [[company/月之暗面/MoonEP|MoonEP]] | project | verify_evidence | evidence | verification | 3.732 | new | source coverage 1/2；evidence quality below target |
| 56 | VERIFY | weak_evidence | [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]] | person | verify_evidence | evidence | verification | 3.728 | new | source coverage 1/2；evidence quality below target |
| 57 | VERIFY | weak_evidence | [[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]] | person | verify_evidence | evidence | verification | 3.728 | new | source coverage 1/2；evidence quality below target |
| 58 | VERIFY | weak_evidence | [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]] | person | verify_evidence | evidence | verification | 3.728 | new | source coverage 1/2；evidence quality below target |
| 59 | VERIFY | weak_evidence | [[community/ai-dynamo/Dynamo/Ryan McCormick|Ryan McCormick]] | person | verify_evidence | evidence | verification | 3.702 | new | source coverage 1/2；evidence quality below target |
| 60 | VERIFY | weak_evidence | [[community/kvcache-ai/KTransformers/Jiahao Wang|Jiahao Wang]] | person | verify_evidence | evidence | verification | 3.693 | new | source coverage 1/2；evidence quality below target |
| 61 | VERIFY | weak_evidence | [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]] | project | verify_evidence | evidence | verification | 3.665 | new | source coverage 1/2；evidence quality below target |
| 62 | VERIFY | weak_evidence | [[company/清程极智/吉青|吉青]] | person | verify_evidence | evidence | verification | 3.665 | new | source coverage 1/2；evidence quality below target |
| 63 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢]] | person | verify_evidence | evidence | verification | 3.659 | new | source coverage 1/2；evidence quality below target |
| 64 | VERIFY | weak_evidence | [[community/kvcache-ai/KTransformers/Hongtao Chen|Hongtao Chen]] | person | verify_evidence | evidence | verification | 3.578 | new | source coverage 1/2；evidence quality below target |
| 65 | VERIFY | weak_evidence | [[community/kvcache-ai/KTransformers/Qingliang Ou|Qingliang Ou]] | person | verify_evidence | evidence | verification | 3.578 | new | source coverage 1/2；evidence quality below target |
| 66 | VERIFY | weak_evidence | [[community/ai-dynamo/Dynamo/Ishan Dhanani|Ishan Dhanani]] | person | verify_evidence | evidence | verification | 3.564 | new | source coverage 1/2；evidence quality below target |
| 67 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/Niu Shengxiao|Niu Shengxiao]] | person | verify_evidence | evidence | verification | 3.564 | new | source coverage 1/2；evidence quality below target |
| 68 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/Zaijun Wang|Zaijun Wang]] | person | verify_evidence | evidence | verification | 3.564 | new | source coverage 1/2；evidence quality below target |
| 69 | VERIFY | weak_evidence | [[community/kvcache-ai/KTransformers/Jiaqi Liao|Jiaqi Liao]] | person | verify_evidence | evidence | verification | 3.543 | new | source coverage 1/2；evidence quality below target |
| 70 | VERIFY | weak_evidence | [[community/triton-inference-server/Triton-Inference-Server/Sai Kiran Polisetty|Sai Kiran Polisetty]] | person | verify_evidence | evidence | verification | 3.540 | new | source coverage 1/2；evidence quality below target |
| 71 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Xin He|Xin He]] | person | verify_evidence | evidence | verification | 3.514 | new | source coverage 1/2；evidence quality below target |
| 72 | VERIFY | weak_evidence | [[university/上海交通大学/Xingda Wei|Xingda Wei]] | person | verify_evidence | evidence | verification | 3.484 | new | source coverage 1/2；evidence quality below target |
| 73 | VERIFY | weak_evidence | [[company/阿里巴巴/Qwen3|Qwen3]] | project | verify_evidence | evidence | verification | 3.474 | new | source coverage 1/2；evidence quality below target |
| 74 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/DeepEP|DeepEP]] | project | verify_evidence | evidence | verification | 3.459 | new | source coverage 1/2；evidence quality below target |
| 75 | VERIFY | weak_evidence | [[community/Ascend/ops-transformer/tangkaidi|tangkaidi]] | person | verify_evidence | evidence | verification | 3.455 | new | source coverage 1/2；evidence quality below target |
| 76 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/Su Fubao|Su Fubao]] | person | verify_evidence | evidence | verification | 3.440 | new | source coverage 1/2；evidence quality below target |
| 77 | VERIFY | weak_evidence | [[community/Deep-Spark/lmcache-iluvatar/lmcache-iluvatar|lmcache-iluvatar]] | project | verify_evidence | evidence | verification | 3.439 | new | source coverage 1/2；evidence quality below target |
| 78 | VERIFY | weak_evidence | [[company/Baseten/Baseten|Baseten]] | company | verify_evidence | evidence | verification | 3.409 | new | source coverage 1/2；evidence quality below target |
| 79 | VERIFY | weak_evidence | [[community/MetaX-MACA/mcoplib/mcoplib|mcoplib]] | project | verify_evidence | evidence | verification | 3.393 | new | source coverage 1/2；evidence quality below target |
| 80 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/Adit Ranadive|Adit Ranadive]] | person | verify_evidence | evidence | verification | 3.298 | new | source coverage 1/2；evidence quality below target |
| 81 | VERIFY | weak_evidence | [[company/智谱/GLM-4.5|GLM-4.5]] | project | verify_evidence | evidence | verification | 3.245 | new | source coverage 1/2；evidence quality below target |
| 82 | VERIFY | weak_evidence | [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航]] | person | verify_evidence | evidence | verification | 3.232 | new | source coverage 1/2；evidence quality below target |
| 83 | VERIFY | weak_evidence | [[community/MetaX-MACA/MXDeepEP/MXDeepEP|MXDeepEP]] | project | verify_evidence | evidence | verification | 3.214 | new | source coverage 1/2；evidence quality below target |
| 84 | VERIFY | weak_evidence | [[university/Stanford University/Stanford University|Stanford University]] | school | verify_evidence | evidence | verification | 3.210 | new | source coverage 1/2；evidence quality below target |
| 85 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Yi Zhang|Yi Zhang]] | person | verify_evidence | evidence | verification | 3.207 | new | source coverage 1/2；evidence quality below target |
| 86 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]] | person | verify_evidence | evidence | verification | 3.205 | new | source coverage 1/2；evidence quality below target |
| 87 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Liang Zhao|Liang Zhao]] | person | verify_evidence | evidence | verification | 3.205 | new | source coverage 1/2；evidence quality below target |
| 88 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Zhean Xu|Zhean Xu]] | person | verify_evidence | evidence | verification | 3.205 | new | source coverage 1/2；evidence quality below target |
| 89 | VERIFY | weak_evidence | [[company/摩尔线程/Xiaodong Ye|Xiaodong Ye]] | person | verify_evidence | evidence | verification | 3.178 | new | source coverage 1/2；evidence quality below target |
| 90 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/Mikhail Brinskiy|Mikhail Brinskiy]] | person | verify_evidence | evidence | verification | 3.170 | new | source coverage 1/2；evidence quality below target |
| 91 | VERIFY | weak_evidence | [[community/triton-inference-server/Triton-Inference-Server/Yingge He|Yingge He]] | person | verify_evidence | evidence | verification | 3.143 | new | source coverage 1/2；evidence quality below target |
| 92 | VERIFY | weak_evidence | [[community/LMCache/LMCache/Hunter Zhang|Hunter Zhang]] | person | verify_evidence | evidence | verification | 3.140 | new | source coverage 1/2；evidence quality below target |
| 93 | VERIFY | weak_evidence | [[community/kvcache-ai/KTransformers/Xingxing Hao|Xingxing Hao]] | person | verify_evidence | evidence | verification | 3.140 | new | source coverage 1/2；evidence quality below target |
| 94 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Xiao Wang|Xiao Wang]] | person | verify_evidence | evidence | verification | 3.118 | new | source coverage 1/2；evidence quality below target |
| 95 | VERIFY | weak_evidence | [[community/triton-inference-server/Triton-Inference-Server/Akhil Saraswathi|Akhil Saraswathi]] | person | verify_evidence | evidence | verification | 3.115 | new | source coverage 1/2；evidence quality below target |
| 96 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Faraz Khoubsirat|Faraz Khoubsirat]] | person | verify_evidence | evidence | verification | 3.115 | new | source coverage 1/2；evidence quality below target |
| 97 | VERIFY | weak_evidence | [[community/sgl-project/SGLang/张晓雨|张晓雨]] | person | verify_evidence | evidence | verification | 3.115 | new | source coverage 1/2；evidence quality below target |
| 98 | VERIFY | weak_evidence | [[university/上海交通大学/Shengzhong Liu|Shengzhong Liu]] | person | verify_evidence | evidence | verification | 3.068 | new | source coverage 1/2；evidence quality below target |
| 99 | VERIFY | weak_evidence | [[company/阿里巴巴/Qwen-Coder|Qwen-Coder]] | project | verify_evidence | evidence | verification | 3.057 | new | source coverage 1/2；evidence quality below target |
| 100 | VERIFY | weak_evidence | [[community/llm-d/llm-d/JJ Asghar|JJ Asghar]] | person | verify_evidence | evidence | verification | 3.040 | new | source coverage 1/2；evidence quality below target |
| 101 | VERIFY | weak_evidence | [[community/ai-dynamo/Dynamo/Julien Mancuso|Julien Mancuso]] | person | verify_evidence | evidence | verification | 3.040 | new | source coverage 1/2；evidence quality below target |
| 102 | VERIFY | weak_evidence | [[university/University of Texas at Austin/University of Texas at Austin|University of Texas at Austin]] | school | verify_evidence | evidence | verification | 3.029 | new | source coverage 1/2；evidence quality below target |
| 103 | VERIFY | weak_evidence | [[community/flashinfer-ai/FlashInfer/陈乐群 Lequn Chen|陈乐群]] | person | verify_evidence | evidence | verification | 2.955 | new | source coverage 1/2；evidence quality below target |
| 104 | VERIFY | weak_evidence | [[university/上海交通大学/Haibo Chen|Haibo Chen]] | person | verify_evidence | evidence | verification | 2.934 | new | source coverage 1/2；evidence quality below target |
| 105 | VERIFY | weak_evidence | [[community/vllm-project/AIBrix/Jianliang Qi|Jianliang Qi]] | person | verify_evidence | evidence | verification | 2.926 | new | source coverage 1/2；evidence quality below target |
| 106 | VERIFY | weak_evidence | [[community/kvcache-ai/Mooncake/Xinran Xu|Xinran Xu]] | person | verify_evidence | evidence | verification | 2.913 | new | source coverage 1/2；evidence quality below target |
| 107 | VERIFY | weak_evidence | [[community/llm-d/llm-d/Marcio A L Silva|Marcio A L Silva]] | person | verify_evidence | evidence | verification | 2.901 | new | source coverage 1/2；evidence quality below target |
| 108 | VERIFY | weak_evidence | [[community/triton-inference-server/Triton-Inference-Server/Faradawn Yang|Faradawn Yang]] | person | verify_evidence | evidence | verification | 2.888 | new | source coverage 1/2；evidence quality below target |
| 109 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/Hailong Yang|Hailong Yang]] | person | verify_evidence | evidence | verification | 2.863 | new | source coverage 1/2；evidence quality below target |
| 110 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/Ruihao Gong|Ruihao Gong]] | person | verify_evidence | evidence | verification | 2.863 | new | source coverage 1/2；evidence quality below target |
| 111 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/Siyu Wu|Siyu Wu]] | person | verify_evidence | evidence | verification | 2.863 | new | source coverage 1/2；evidence quality below target |
| 112 | VERIFY | weak_evidence | [[community/tile-ai/TileScale/TileScale|TileScale]] | project | verify_evidence | evidence | verification | 2.853 | new | source coverage 1/2；evidence quality below target |
| 113 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/Shihao Bai|Shihao Bai]] | person | verify_evidence | evidence | verification | 2.851 | new | source coverage 1/2；evidence quality below target |
| 114 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/LyricZhao|LyricZhao]] | person | verify_evidence | evidence | verification | 2.830 | new | source coverage 1/2；evidence quality below target |
| 115 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Chenhao Xu|Chenhao Xu]] | person | verify_evidence | evidence | verification | 2.802 | new | source coverage 1/2；evidence quality below target |
| 116 | VERIFY | weak_evidence | [[company/OpenAI/GPT-4o|GPT-4o]] | project | verify_evidence | evidence | verification | 2.794 | new | source coverage 1/2；evidence quality below target |
| 117 | VERIFY | weak_evidence | [[company/智谱/GLM-4-Voice|GLM-4-Voice]] | project | verify_evidence | evidence | verification | 2.776 | new | source coverage 1/2；evidence quality below target |
| 118 | VERIFY | weak_evidence | [[community/ai-dynamo/Dynamo/Stefan Schimanski|Stefan Schimanski]] | person | verify_evidence | evidence | verification | 2.728 | new | source coverage 1/2；evidence quality below target |
| 119 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Chengqi Deng|Chengqi Deng]] | person | verify_evidence | evidence | verification | 2.727 | new | source coverage 1/2；evidence quality below target |
| 120 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Liyue Zhang|Liyue Zhang]] | person | verify_evidence | evidence | verification | 2.727 | new | source coverage 1/2；evidence quality below target |
| 121 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou|Shangyan Zhou]] | person | verify_evidence | evidence | verification | 2.727 | new | source coverage 1/2；evidence quality below target |
| 122 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Yuxuan Liu|Yuxuan Liu]] | person | verify_evidence | evidence | verification | 2.727 | new | source coverage 1/2；evidence quality below target |
| 123 | VERIFY | weak_evidence | [[community/ai-dynamo/Dynamo/Alec Flowers|Alec Flowers]] | person | verify_evidence | evidence | verification | 2.714 | new | source coverage 1/2；evidence quality below target |
| 124 | VERIFY | weak_evidence | [[community/ai-dynamo/Dynamo/Matej Kosec|Matej Kosec]] | person | verify_evidence | evidence | verification | 2.714 | new | source coverage 1/2；evidence quality below target |
| 125 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Chang Liu|Chang Liu]] | person | verify_evidence | evidence | verification | 2.665 | new | source coverage 1/2；evidence quality below target |
| 126 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/Matvei Pashkovskii|Matvei Pashkovskii]] | person | verify_evidence | evidence | verification | 2.665 | new | source coverage 1/2；evidence quality below target |
| 127 | VERIFY | weak_evidence | [[community/ModelTC/LightLLM/Sang Chengmeng|Sang Chengmeng]] | person | verify_evidence | evidence | verification | 2.665 | new | source coverage 1/2；evidence quality below target |
| 128 | VERIFY | weak_evidence | [[community/vllm-project/AIBrix/Xin Li|Xin Li]] | person | verify_evidence | evidence | verification | 2.665 | new | source coverage 1/2；evidence quality below target |
| 129 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Yibin Li|Yibin Li]] | person | verify_evidence | evidence | verification | 2.665 | new | source coverage 1/2；evidence quality below target |
| 130 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Zhaoyang Wang|Zhaoyang Wang]] | person | verify_evidence | evidence | verification | 2.665 | new | source coverage 1/2；evidence quality below target |
| 131 | VERIFY | weak_evidence | [[community/sgl-project/SGLang/张亦弛|张亦弛]] | person | verify_evidence | evidence | verification | 2.665 | new | source coverage 1/2；evidence quality below target |
| 132 | VERIFY | weak_evidence | [[university/Oak Ridge National Laboratory/Oak Ridge National Laboratory|Oak Ridge National Laboratory]] | research | verify_evidence | evidence | verification | 2.661 | new | source coverage 1/2；evidence quality below target |
| 133 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Brian Nguyen|Brian Nguyen]] | person | verify_evidence | evidence | verification | 2.643 | new | source coverage 1/2；evidence quality below target |
| 134 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Yao Yao|Yao Yao]] | person | verify_evidence | evidence | verification | 2.640 | new | source coverage 1/2；evidence quality below target |
| 135 | VERIFY | weak_evidence | [[company/OpenAI/GPT-4|GPT-4]] | project | verify_evidence | evidence | verification | 2.630 | new | source coverage 1/2；evidence quality below target |
| 136 | VERIFY | weak_evidence | [[community/sail-sg/EnvPool/EnvPool|EnvPool]] | project | verify_evidence | evidence | verification | 2.599 | new | source coverage 1/2；evidence quality below target |
| 137 | VERIFY | weak_evidence | [[community/vllm-project/AIBrix/Chenyu Jiang|Chenyu Jiang]] | person | verify_evidence | evidence | verification | 2.590 | new | source coverage 1/2；evidence quality below target |
| 138 | VERIFY | weak_evidence | [[university/上海交通大学/Rongxin Cheng|Rongxin Cheng]] | person | verify_evidence | evidence | verification | 2.559 | new | source coverage 1/2；evidence quality below target |
| 139 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/Rongbing Zhou|Rongbing Zhou]] | person | verify_evidence | evidence | verification | 2.540 | new | source coverage 1/2；evidence quality below target |
| 140 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/Tomer Davidor|Tomer Davidor]] | person | verify_evidence | evidence | verification | 2.540 | new | source coverage 1/2；evidence quality below target |
| 141 | VERIFY | weak_evidence | [[community/flashinfer-ai/FlashInfer/Wuwei Lin|Wuwei Lin]] | person | verify_evidence | evidence | verification | 2.505 | new | source coverage 1/2；evidence quality below target |
| 142 | VERIFY | weak_evidence | [[company/OpenAI/o1|o1]] | project | verify_evidence | evidence | verification | 2.482 | new | source coverage 1/2；evidence quality below target |
| 143 | VERIFY | weak_evidence | [[community/vllm-project/AIBrix/CYJiang|CYJiang]] | person | verify_evidence | evidence | verification | 2.469 | new | source coverage 1/2；evidence quality below target |
| 144 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/Anyi Xu|Anyi Xu]] | person | verify_evidence | evidence | verification | 2.427 | new | source coverage 1/2；evidence quality below target |
| 145 | VERIFY | weak_evidence | [[university/Harvard University/Harvard University|Harvard University]] | school | verify_evidence | evidence | verification | 2.357 | new | source coverage 1/2；evidence quality below target |
| 146 | VERIFY | weak_evidence | [[university/Princeton University/Princeton University|Princeton University]] | school | verify_evidence | evidence | verification | 2.357 | new | source coverage 1/2；evidence quality below target |
| 147 | VERIFY | weak_evidence | [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇]] | person | verify_evidence | evidence | verification | 2.295 | new | source coverage 1/2；evidence quality below target |
| 148 | VERIFY | weak_evidence | [[university/UCLA/UCLA|UCLA]] | school | verify_evidence | evidence | verification | 2.268 | new | source coverage 1/2；evidence quality below target |
| 149 | VERIFY | weak_evidence | [[company/OpenAI/GPT-4.5|GPT-4.5]] | project | verify_evidence | evidence | verification | 2.227 | new | source coverage 1/2；evidence quality below target |
| 150 | VERIFY | weak_evidence | [[university/四川大学/四川大学|四川大学]] | school | verify_evidence | evidence | verification | 2.204 | new | source coverage 1/2；evidence quality below target |
| 151 | VERIFY | weak_evidence | [[community/NVIDIA/TensorRT-LLM/Anurag Mukkara|Anurag Mukkara]] | person | verify_evidence | evidence | verification | 2.165 | new | source coverage 1/2；evidence quality below target |
| 152 | VERIFY | weak_evidence | [[community/llm-d/llm-d/David Simmons|David Simmons]] | person | verify_evidence | evidence | verification | 2.165 | new | source coverage 1/2；evidence quality below target |
| 153 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/Efraim Eygin|Efraim Eygin]] | person | verify_evidence | evidence | verification | 2.165 | new | source coverage 1/2；evidence quality below target |
| 154 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/Ilia Yastrebov|Ilia Yastrebov]] | person | verify_evidence | evidence | verification | 2.165 | new | source coverage 1/2；evidence quality below target |
| 155 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/James Thomas|James Thomas]] | person | verify_evidence | evidence | verification | 2.165 | new | source coverage 1/2；evidence quality below target |
| 156 | VERIFY | weak_evidence | [[community/vllm-project/AIBrix/Jingyuan Zhang|Jingyuan Zhang]] | person | verify_evidence | evidence | verification | 2.165 | new | source coverage 1/2；evidence quality below target |
| 157 | VERIFY | weak_evidence | [[community/llm-d/llm-d/Pete Cheslock|Pete Cheslock]] | person | verify_evidence | evidence | verification | 2.165 | new | source coverage 1/2；evidence quality below target |
| 158 | VERIFY | weak_evidence | [[community/ai-dynamo/NIXL/Ryan Hankins|Ryan Hankins]] | person | verify_evidence | evidence | verification | 2.165 | new | source coverage 1/2；evidence quality below target |
| 159 | VERIFY | weak_evidence | [[university/Columbia University/Columbia University|Columbia University]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 160 | VERIFY | weak_evidence | [[university/Cornell Tech/Cornell Tech|Cornell Tech]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 161 | VERIFY | weak_evidence | [[university/Cornell University/Cornell University|Cornell University]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 162 | VERIFY | weak_evidence | [[university/University of Tennessee, Knoxville/University of Tennessee, Knoxville|University of Tennessee, Knoxville]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 163 | VERIFY | weak_evidence | [[university/University of Toronto/University of Toronto|University of Toronto]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 164 | VERIFY | weak_evidence | [[university/University of Warwick/University of Warwick|University of Warwick]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 165 | VERIFY | weak_evidence | [[university/上海科技大学/上海科技大学|上海科技大学]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 166 | VERIFY | weak_evidence | [[university/中山大学/中山大学|中山大学]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 167 | VERIFY | weak_evidence | [[university/北京航空航天大学/北京航空航天大学|北京航空航天大学]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 168 | VERIFY | weak_evidence | [[university/复旦大学/复旦大学|复旦大学]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 169 | VERIFY | weak_evidence | [[university/武汉大学/武汉大学|武汉大学]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 170 | VERIFY | weak_evidence | [[university/西交利物浦大学/西交利物浦大学|西交利物浦大学]] | school | verify_evidence | evidence | verification | 2.130 | new | source coverage 1/2；evidence quality below target |
| 171 | VERIFY | weak_evidence | [[company/阿里巴巴/林俊旸 Junyang Lin|林俊旸]] | person | verify_evidence | evidence | verification | 2.093 | new | source coverage 1/2；evidence quality below target |
| 172 | VERIFY | weak_evidence | [[company/阿里巴巴/惠彬原 Binyuan Hui|惠彬原]] | person | verify_evidence | evidence | verification | 2.083 | new | source coverage 1/2；evidence quality below target |
| 173 | VERIFY | weak_evidence | [[company/阿里巴巴/郁博文 Bowen Yu|郁博文]] | person | verify_evidence | evidence | verification | 2.083 | new | source coverage 1/2；evidence quality below target |
| 174 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/guyan364|guyan364]] | person | verify_evidence | evidence | verification | 2.005 | new | source coverage 1/2；evidence quality below target |
| 175 | VERIFY | weak_evidence | [[community/deepseek-ai/DeepSeek-Infra/kurisu6912|kurisu6912]] | person | verify_evidence | evidence | verification | 1.977 | new | source coverage 1/2；evidence quality below target |
| 176 | VERIFY | weak_evidence | [[community/vllm-project/AIBrix/Guangjian|Guangjian]] | person | verify_evidence | evidence | verification | 1.938 | new | source coverage 1/2；evidence quality below target |
| 177 | VERIFY | weak_evidence | [[community/vllm-project/AIBrix/Jiang Xiaobin|Jiang Xiaobin]] | person | verify_evidence | evidence | verification | 1.938 | new | source coverage 1/2；evidence quality below target |

## VERIFY

Evidence strengthening, contradiction checking and durable-history follow-up.

## Agent execution contract

1. 优先官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文与机构一手资料。
2. Operator 只授权调查，不授权无证据创建节点或边。
3. contributor 不自动等于 maintainer；同校不自动等于同学；兼容不自动等于人物直接合作。
4. 新发现但超出当前 action 的线索留给下一轮 planner，不无限递归。
5. 执行后用 `scripts/record-research-action.py` 记录 success / partial / unresolved / rejected。
6. `action_id` / `action_key` 永远不包含 operator，同一 objective 跨 operator 共享 cooldown/history。

完整说明：`docs/research-action-planner.md`；快速使用：`docs/research-operators.md`。
