# School Link Coverage

由 `scripts/audit-school-links.py` 自动生成。`schools:` 只表示可核验的教育、任职或访问研究关联，不自动推断导师、同学或同门关系。

- Person nodes: 204
- People with ≥1 school: 102
- People without known school: 102
- Coverage: 50.0%
- Person-school associations: 138
- School nodes: 46
- Audit errors: 0

## Top schools by linked people

| School | People |
| --- | ---: |
| 清华大学 | 38 |
| UC Berkeley | 16 |
| 北京大学 | 16 |
| 上海交通大学 | 14 |
| Carnegie Mellon University | 7 |
| 浙江大学 | 6 |
| Stanford University | 3 |
| University of Chicago | 3 |
| 厦门大学 | 2 |
| 四川大学 | 2 |
| Georgia Institute of Technology | 2 |
| University of Washington | 2 |
| UCLA | 2 |
| Seoul National University | 1 |
| Harvard University | 1 |
| Franklin W. Olin College of Engineering | 1 |
| Columbia University | 1 |
| 南京大学 | 1 |
| UC Davis | 1 |
| 北京邮电大学 | 1 |
| 复旦大学 | 1 |
| 北京航空航天大学 | 1 |
| 中山大学 | 1 |
| Massachusetts Institute of Technology | 1 |
| Binghamton University | 1 |
| Stony Brook University | 1 |
| Lobachevsky State University of Nizhny Novgorod | 1 |
| 华中科技大学 | 1 |
| 西北工业大学 | 1 |
| 电子科技大学 | 1 |

## High-value people still missing a verified school association

| Rank | Person | Bridge score | Degree |
| ---: | --- | ---: | ---: |
| 1 | [[community/flashinfer-ai/FlashInfer/Yang Xu|Yang Xu]] | 6.52 | 8 |
| 2 | [[community/llm-d/llm-d/Carlos Costa|Carlos Costa]] | 6.35 | 7 |
| 3 | [[company/基流科技/Yanmin Jia|Yanmin Jia]] | 6.35 | 7 |
| 4 | [[community/llm-d/llm-d/Ashok Chandrasekar|Ashok Chandrasekar]] | 6.157 | 6 |
| 5 | [[company/基流科技/He Liu|He Liu]] | 6.157 | 6 |
| 6 | [[community/llm-d/llm-d/Nili Guy|Nili Guy]] | 6.157 | 6 |
| 7 | [[community/llm-d/llm-d/Vita Bortnikov|Vita Bortnikov]] | 6.157 | 6 |
| 8 | [[community/flagos-ai/FlagOS/敖玉龙 Yulong Ao|敖玉龙]] | 6.157 | 6 |
| 9 | [[community/NVIDIA/TensorRT-LLM/Yi Zhang|Yi Zhang]] | 5.935 | 5 |
| 10 | [[company/硅基流动/柳俊丞 Juncheng Liu|柳俊丞]] | 5.935 | 5 |
| 11 | [[company/硅基流动/赵震 Zhao Zhen|赵震]] | 5.935 | 5 |
| 12 | [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]] | 5.7 | 3 |
| 13 | [[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]] | 5.7 | 3 |
| 14 | [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]] | 5.7 | 3 |
| 15 | [[community/kvcache-ai/KTransformers/Qingliang Ou|Qingliang Ou]] | 5.7 | 3 |
| 16 | [[community/ai-dynamo/Dynamo/Stefan Schimanski|Stefan Schimanski]] | 5.7 | 3 |
| 17 | [[community/ai-dynamo/Dynamo/Alec Flowers|Alec Flowers]] | 5.672 | 4 |
| 18 | [[community/ai-dynamo/Dynamo/Ishan Dhanani|Ishan Dhanani]] | 5.672 | 4 |
| 19 | [[community/ai-dynamo/Dynamo/Matej Kosec|Matej Kosec]] | 5.672 | 4 |
| 20 | [[community/ModelTC/LightLLM/Niu Shengxiao|Niu Shengxiao]] | 5.672 | 4 |
| 21 | [[community/NVIDIA/TensorRT-LLM/Xin He|Xin He]] | 5.672 | 4 |
| 22 | [[community/ModelTC/LightLLM/Zaijun Wang|Zaijun Wang]] | 5.672 | 4 |
| 23 | [[community/llm-d/llm-d/张家驹 Jiaju Zhang|张家驹]] | 5.672 | 4 |
| 24 | [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远]] | 5.672 | 4 |
| 25 | [[community/NVIDIA/TensorRT-LLM/Brian Nguyen|Brian Nguyen]] | 5.35 | 3 |
| 26 | [[community/vllm-project/vLLM/Patrick von Platen|Patrick von Platen]] | 5.35 | 3 |
| 27 | [[community/NVIDIA/TensorRT-LLM/Xiao Wang|Xiao Wang]] | 5.35 | 3 |
| 28 | [[community/triton-inference-server/Triton-Inference-Server/Yingge He|Yingge He]] | 5.35 | 3 |
| 29 | [[community/triton-inference-server/Triton-Inference-Server/Akhil Saraswathi|Akhil Saraswathi]] | 4.935 | 2 |
| 30 | [[community/NVIDIA/TensorRT-LLM/Anurag Mukkara|Anurag Mukkara]] | 4.935 | 2 |
| 31 | [[community/NVIDIA/TensorRT-LLM/Chang Liu|Chang Liu]] | 4.935 | 2 |
| 32 | [[community/vllm-project/AIBrix/Chenyu Jiang|Chenyu Jiang]] | 4.935 | 2 |
| 33 | [[community/llm-d/llm-d/David Simmons|David Simmons]] | 4.935 | 2 |
| 34 | [[community/ai-dynamo/NIXL/Efraim Eygin|Efraim Eygin]] | 4.935 | 2 |
| 35 | [[community/NVIDIA/TensorRT-LLM/Faraz Khoubsirat|Faraz Khoubsirat]] | 4.935 | 2 |
| 36 | [[community/ai-dynamo/NIXL/Ilia Yastrebov|Ilia Yastrebov]] | 4.935 | 2 |
| 37 | [[community/llm-d/llm-d/JJ Asghar|JJ Asghar]] | 4.935 | 2 |
| 38 | [[community/ai-dynamo/NIXL/James Thomas|James Thomas]] | 4.935 | 2 |
| 39 | [[community/kvcache-ai/KTransformers/Jiahao Wang|Jiahao Wang]] | 4.935 | 2 |
| 40 | [[community/kvcache-ai/KTransformers/Jiaqi Liao|Jiaqi Liao]] | 4.935 | 2 |
| 41 | [[community/vllm-project/AIBrix/Jingyuan Zhang|Jingyuan Zhang]] | 4.935 | 2 |
| 42 | [[community/ai-dynamo/Dynamo/Julien Mancuso|Julien Mancuso]] | 4.935 | 2 |
| 43 | [[community/ai-dynamo/NIXL/Matvei Pashkovskii|Matvei Pashkovskii]] | 4.935 | 2 |
| 44 | [[community/llm-d/llm-d/Pete Cheslock|Pete Cheslock]] | 4.935 | 2 |
| 45 | [[community/ai-dynamo/NIXL/Rongbing Zhou|Rongbing Zhou]] | 4.935 | 2 |
| 46 | [[community/ai-dynamo/NIXL/Ryan Hankins|Ryan Hankins]] | 4.935 | 2 |
| 47 | [[community/triton-inference-server/Triton-Inference-Server/Sai Kiran Polisetty|Sai Kiran Polisetty]] | 4.935 | 2 |
| 48 | [[community/ModelTC/LightLLM/Sang Chengmeng|Sang Chengmeng]] | 4.935 | 2 |
| 49 | [[community/ModelTC/LightLLM/Su Fubao|Su Fubao]] | 4.935 | 2 |
| 50 | [[community/ai-dynamo/NIXL/Tomer Davidor|Tomer Davidor]] | 4.935 | 2 |
