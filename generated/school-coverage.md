# School Link Coverage

由 `scripts/audit-school-links.py` 自动生成。`schools:` 只表示可核验的教育、任职或访问研究关联，不自动推断导师、同学或同门关系。

- Person nodes: 261
- People with ≥1 school: 123
- People without known school: 138
- Coverage: 47.1%
- Person-school associations: 161
- School nodes: 46
- Audit errors: 0

## Top schools by linked people

| School | People |
| --- | ---: |
| 清华大学 | 45 |
| UC Berkeley | 20 |
| 北京大学 | 17 |
| 上海交通大学 | 14 |
| Carnegie Mellon University | 7 |
| 浙江大学 | 7 |
| University of Chicago | 6 |
| Stanford University | 3 |
| UCLA | 3 |
| Harvard University | 2 |
| 厦门大学 | 2 |
| 四川大学 | 2 |
| Georgia Institute of Technology | 2 |
| University of Washington | 2 |
| University of Texas at Austin | 2 |
| Seoul National University | 1 |
| Franklin W. Olin College of Engineering | 1 |
| Cornell Tech | 1 |
| 西交利物浦大学 | 1 |
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

## High-value people still missing a verified school association

| Rank | Person | Bridge score | Degree |
| ---: | --- | ---: | ---: |
| 1 | [[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]] | 8.685 | 11 |
| 2 | [[community/vllm-project/vLLM/Roger Wang|Roger Wang]] | 7.372 | 9 |
| 3 | [[company/腾讯/Baolong Mao|Baolong Mao]] | 6.635 | 5 |
| 4 | [[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]] | 6.52 | 8 |
| 5 | [[community/flashinfer-ai/FlashInfer/Yang Xu|Yang Xu]] | 6.52 | 8 |
| 6 | [[community/llm-d/llm-d/Carlos Costa|Carlos Costa]] | 6.35 | 7 |
| 7 | [[company/RadixArk/Cheng Wan|Cheng Wan]] | 6.35 | 7 |
| 8 | [[company/RadixArk/Xiaoyu Zhang|Xiaoyu Zhang]] | 6.35 | 7 |
| 9 | [[company/基流科技/Yanmin Jia|Yanmin Jia]] | 6.35 | 7 |
| 10 | [[community/flashinfer-ai/FlashInfer/aleozlx|Alex Yang]] | 6.157 | 6 |
| 11 | [[community/llm-d/llm-d/Ashok Chandrasekar|Ashok Chandrasekar]] | 6.157 | 6 |
| 12 | [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]] | 6.157 | 6 |
| 13 | [[company/基流科技/He Liu|He Liu]] | 6.157 | 6 |
| 14 | [[community/llm-d/llm-d/Nili Guy|Nili Guy]] | 6.157 | 6 |
| 15 | [[community/llm-d/llm-d/Vita Bortnikov|Vita Bortnikov]] | 6.157 | 6 |
| 16 | [[community/flagos-ai/FlagOS/敖玉龙 Yulong Ao|敖玉龙]] | 6.157 | 6 |
| 17 | [[community/Project-HAMi/HAMi/archlitchi|Mengxuan Li]] | 5.935 | 5 |
| 18 | [[community/NVIDIA/TensorRT-LLM/Yi Zhang|Yi Zhang]] | 5.935 | 5 |
| 19 | [[university/启元实验室/李映辉 Yinghui Li|李映辉]] | 5.935 | 5 |
| 20 | [[company/硅基流动/柳俊丞 Juncheng Liu|柳俊丞]] | 5.935 | 5 |
| 21 | [[university/启元实验室/潘泽众 Zezhong Pan|潘泽众]] | 5.935 | 5 |
| 22 | [[company/硅基流动/赵震 Zhao Zhen|赵震]] | 5.935 | 5 |
| 23 | [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成]] | 5.935 | 5 |
| 24 | [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]] | 5.7 | 3 |
| 25 | [[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]] | 5.7 | 3 |
| 26 | [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]] | 5.7 | 3 |
| 27 | [[company/IBM/Martin Hickey|Martin Hickey]] | 5.7 | 3 |
| 28 | [[community/kvcache-ai/KTransformers/Qingliang Ou|Qingliang Ou]] | 5.7 | 3 |
| 29 | [[community/ai-dynamo/Dynamo/Stefan Schimanski|Stefan Schimanski]] | 5.7 | 3 |
| 30 | [[community/ai-dynamo/Dynamo/Alec Flowers|Alec Flowers]] | 5.672 | 4 |
| 31 | [[community/ai-dynamo/Dynamo/Ishan Dhanani|Ishan Dhanani]] | 5.672 | 4 |
| 32 | [[community/Ascend/ops-transformer/Konstantin Berestizshevsky|Konstantin Berestizshevsky]] | 5.672 | 4 |
| 33 | [[community/ai-dynamo/Dynamo/Matej Kosec|Matej Kosec]] | 5.672 | 4 |
| 34 | [[community/ModelTC/LightLLM/Niu Shengxiao|Niu Shengxiao]] | 5.672 | 4 |
| 35 | [[community/NVIDIA/TensorRT-LLM/Xin He|Xin He]] | 5.672 | 4 |
| 36 | [[community/ModelTC/LightLLM/Zaijun Wang|Zaijun Wang]] | 5.672 | 4 |
| 37 | [[community/llm-d/llm-d/张家驹 Jiaju Zhang|张家驹]] | 5.672 | 4 |
| 38 | [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远]] | 5.672 | 4 |
| 39 | [[community/NVIDIA/TensorRT-LLM/Brian Nguyen|Brian Nguyen]] | 5.35 | 3 |
| 40 | [[company/腾讯/Chunxiao Zheng|Chunxiao Zheng]] | 5.35 | 3 |
| 41 | [[community/vllm-project/vLLM/Patrick von Platen|Patrick von Platen]] | 5.35 | 3 |
| 42 | [[community/NVIDIA/TensorRT-LLM/Xiao Wang|Xiao Wang]] | 5.35 | 3 |
| 43 | [[community/Project-HAMi/HAMi/wawa0210|Xiao Zhang]] | 5.35 | 3 |
| 44 | [[community/triton-inference-server/Triton-Inference-Server/Yingge He|Yingge He]] | 5.35 | 3 |
| 45 | [[community/Ascend/ops-transformer/wangchao661|wangchao661]] | 5.35 | 3 |
| 46 | [[community/openEuler/openYuanRong/罗站城 Zhancheng Luo|罗站城]] | 5.35 | 3 |
| 47 | [[community/triton-inference-server/Triton-Inference-Server/Akhil Saraswathi|Akhil Saraswathi]] | 4.935 | 2 |
| 48 | [[community/NVIDIA/TensorRT-LLM/Anurag Mukkara|Anurag Mukkara]] | 4.935 | 2 |
| 49 | [[community/NVIDIA/TensorRT-LLM/Chang Liu|Chang Liu]] | 4.935 | 2 |
| 50 | [[community/vllm-project/AIBrix/Chenyu Jiang|Chenyu Jiang]] | 4.935 | 2 |
