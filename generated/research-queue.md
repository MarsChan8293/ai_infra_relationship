# Research Queue

由 `scripts/generate-research-queue.py` 自动生成。它排序的是下一轮研究价值，不是人物重要性。

算法：**Gap-aware Best-First BFS + Selective DFS**。先用局部 BFS 建立邻域，再按桥梁度、关系缺口、推理相关性、证据质量与新颖性重新排序；DFS 采用预算制，只允许最高价值的一小撮桥梁人物继续向深层关系链扩展。

公式：`1.60×bridge + 1.80×gap + 2.00×infra_relevance + 0.80×evidence + 0.90×novelty - 1.20×distance_penalty`。

Selective DFS budget: **12**，本轮实际触发 **12**。

| Rank | Person | Score | Strategy | Bridge | Gap | Infra | Distance | Why / next |
| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | [[company/趋境科技/武永卫 Yongwei Wu|武永卫]] | 35.658 | selective-dfs | 14.274 | 1.300 | 3.450 | - | bridge 14.3; infra: serving/inference, kv-cache, distributed; multi-project 3 → typed person relations, hidden person chain |
| 2 | [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰]] | 33.575 | selective-dfs | 12.672 | 1.300 | 3.550 | - | bridge 12.7; infra: serving/inference, kv-cache, distributed; multi-project 3 → typed person relations, hidden person chain |
| 3 | [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超]] | 33.468 | selective-dfs | 14.855 | 1.300 | 1.750 | - | bridge 14.9; infra: serving/inference, distributed; multi-project 2 → typed person relations, hidden person chain |
| 4 | [[company/RadixArk/盛颖 Ying Sheng|盛颖]] | 32.772 | selective-dfs | 12.170 | 1.300 | 3.550 | - | bridge 12.2; infra: serving/inference, kv-cache, scheduler; multi-project 2 → typed person relations, hidden person chain |
| 5 | [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]] | 32.558 | selective-dfs | 11.474 | 1.300 | 4.000 | - | bridge 11.5; infra: serving/inference, kv-cache, scheduler; multi-project 5 → typed person relations, hidden person chain |
| 6 | [[community/vllm-project/vLLM/李卓翰 Zhuohan Li|李卓翰]] | 32.538 | selective-dfs | 14.274 | 1.300 | 1.750 | - | bridge 14.3; infra: serving/inference, distributed; multi-project 2 → typed person relations, hidden person chain |
| 7 | [[company/清程极智/翟季冬 Jidong Zhai|翟季冬]] | 32.208 | selective-dfs | 11.272 | 1.300 | 4.000 | - | bridge 11.3; infra: serving/inference, kv-cache, kernel; multi-project 3 → typed person relations, hidden person chain |
| 8 | [[university/清华大学/Mingxing Zhang|章明星]] | 32.159 | selective-dfs | 12.087 | 1.300 | 3.450 | - | bridge 12.1; infra: serving/inference, kv-cache, distributed; multi-project 4 → typed person relations, hidden person chain |
| 9 | [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民]] | 32.131 | selective-dfs | 10.757 | 2.200 | 3.550 | - | bridge 10.8; gap 2.2; infra: serving/inference, kv-cache, scheduler; multi-project 4 → current affiliation, typed person relations, hidden person chain |
| 10 | [[community/sgl-project/SGLang/谢志强 Zhiqiang Xie|谢志强]] | 31.865 | selective-dfs | 10.409 | 3.300 | 2.800 | - | bridge 10.4; gap 3.3; infra: serving/inference, kv-cache, scheduler → current affiliation, project/community links, typed person relations |
| 11 | [[community/vllm-project/vLLM/Robert Shaw|Robert Shaw]] | 31.675 | selective-dfs | 10.922 | 1.300 | 4.000 | - | bridge 10.9; infra: serving/inference, kv-cache, kernel; multi-project 2 → typed person relations, hidden person chain |
| 12 | [[community/vllm-project/vLLM/乔一凡 Yifan Qiao|乔一凡]] | 31.524 | selective-dfs | 12.520 | 1.300 | 2.700 | - | bridge 12.5; infra: serving/inference, kv-cache, distributed; multi-project 2 → typed person relations, hidden person chain |
| 13 | [[company/Inferact/Woosuk Kwon|Woosuk Kwon]] | 31.172 | best-first | 12.437 | 1.300 | 2.550 | - | bridge 12.4; infra: kv-cache, scheduler, distributed; multi-project 2 → typed person relations |
| 14 | [[community/vllm-project/vLLM/Michael Goin|Michael Goin]] | 31.011 | best-first | 10.507 | 1.300 | 4.000 | - | bridge 10.5; infra: serving/inference, scheduler, kernel → typed person relations |
| 15 | [[company/深度求索/梁文锋 Liang Wenfeng|梁文锋]] | 31.005 | best-first | 9.485 | 2.400 | 4.000 | - | bridge 9.5; gap 2.4; infra: serving/inference, kernel, distributed → project/community links, typed person relations |
| 16 | [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]] | 30.024 | best-first | 12.520 | 1.300 | 1.950 | - | bridge 12.5; infra: serving/inference, kv-cache; multi-project 2 → typed person relations |
| 17 | [[company/Inferact/Ion Stoica|Ion Stoica]] | 29.857 | best-first | 12.598 | 1.300 | 1.750 | - | bridge 12.6; infra: serving/inference, distributed; multi-project 4 → typed person relations |
| 18 | [[community/vllm-project/vLLM/Simon Mo|Simon Mo]] | 29.349 | best-first | 11.387 | 1.300 | 2.600 | - | bridge 11.4; infra: serving/inference, scheduler, distributed; multi-project 2 → typed person relations |
| 19 | [[company/TensorMesh/程翊华 Yihua Cheng|程翊华]] | 29.080 | best-first | 10.409 | 1.300 | 3.550 | - | bridge 10.4; infra: serving/inference, kv-cache, distributed; multi-project 2 → typed person relations |
| 20 | [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与]] | 28.825 | best-first | 9.359 | 1.300 | 4.000 | - | bridge 9.4; infra: serving/inference, kernel, distributed; multi-project 2 → typed person relations |
| 21 | [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]] | 28.705 | best-first | 9.770 | 1.300 | 3.450 | - | bridge 9.8; infra: serving/inference, kv-cache, distributed; multi-project 3 → typed person relations |
| 22 | [[community/vllm-project/vLLM/Tyler Michael Smith|Tyler Michael Smith]] | 28.693 | best-first | 9.250 | 1.300 | 4.000 | - | bridge 9.2; infra: serving/inference, kernel, distributed; multi-project 2 → typed person relations |
| 23 | [[community/sgl-project/SGLang/尹良升 Liangsheng Yin|尹良升]] | 28.596 | best-first | 8.720 | 3.300 | 2.800 | - | bridge 8.7; gap 3.3; infra: serving/inference, kv-cache, scheduler; multi-project 2 → current affiliation, project/community links, typed person relations |
| 24 | [[community/vllm-project/vLLM/Nick Hill|Nick Hill]] | 28.581 | best-first | 9.922 | 1.300 | 3.550 | - | bridge 9.9; infra: serving/inference, kv-cache, scheduler → typed person relations |
| 25 | [[community/llm-d/llm-d/Maroon Ayoub|Maroon Ayoub]] | 28.551 | best-first | 9.707 | 1.300 | 3.550 | - | bridge 9.7; infra: serving/inference, kv-cache, distributed; multi-project 5 → typed person relations |
| 26 | [[community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie|谢威宇]] | 28.409 | best-first | 9.600 | 1.300 | 3.600 | - | bridge 9.6; infra: serving/inference, kv-cache, kernel → typed person relations |
| 27 | [[university/清华大学/Ruoyu Qin|秦若愚]] | 28.146 | best-first | 9.572 | 1.300 | 3.550 | - | bridge 9.6; infra: serving/inference, kv-cache, scheduler; multi-project 2 → typed person relations |
| 28 | [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]] | 27.934 | best-first | 9.009 | 2.700 | 2.400 | - | bridge 9.0; gap 2.7; infra: kernel, distributed, moe; multi-project 3 → current affiliation, typed person relations, biographical/context depth |
| 29 | [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]] | 27.828 | best-first | 11.350 | 1.300 | 1.950 | - | bridge 11.3; infra: serving/inference, kv-cache; multi-project 3 → typed person relations |
| 30 | [[community/kvcache-ai/KTransformers/Ziwei Yuan|Ziwei Yuan]] | 27.824 | best-first | 7.872 | 3.050 | 3.600 | - | bridge 7.9; gap 3.0; infra: serving/inference, kv-cache, kernel → typed person relations, technical areas, biographical/context depth |
| 31 | [[company/清程极智/郑纬民 Weimin Zheng|郑纬民]] | 27.800 | best-first | 10.300 | 1.300 | 2.700 | - | bridge 10.3; infra: serving/inference, kv-cache, distributed → typed person relations |
| 32 | [[university/北京大学/吴童 Tong Wu|Tong Wu]] | 27.511 | best-first | 8.357 | 1.800 | 3.600 | - | bridge 8.4; infra: serving/inference, kv-cache, kernel; multi-project 2 → typed person relations, biographical/context depth |
| 33 | [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]] | 27.387 | best-first | 10.059 | 2.200 | 1.750 | - | bridge 10.1; gap 2.2; infra: serving/inference, distributed; multi-project 3 → current affiliation, typed person relations |
| 34 | [[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪]] | 26.825 | best-first | 9.135 | 1.300 | 3.400 | - | bridge 9.1; infra: serving/inference, kernel, distributed → typed person relations |
| 35 | [[community/hpcaitech/Colossal-AI/Hongxin Liu|Hongxin Liu]] | 26.801 | best-first | 9.770 | 2.700 | 1.400 | - | bridge 9.8; gap 2.7; infra: distributed, quantization → current affiliation, typed person relations, biographical/context depth |
| 36 | [[community/ai-dynamo/Dynamo/Sungsoo Ha|Sungsoo Ha]] | 26.729 | best-first | 8.135 | 3.050 | 2.600 | - | bridge 8.1; gap 3.0; infra: serving/inference, distributed, disaggregation; multi-project 2 → typed person relations, technical areas, biographical/context depth |
| 37 | [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰]] | 26.555 | best-first | 9.222 | 1.300 | 2.800 | - | bridge 9.2; infra: serving/inference, kv-cache, disaggregation → typed person relations |
| 38 | [[community/llm-d/llm-d/Danny Harnik|Danny Harnik]] | 26.547 | best-first | 8.522 | 1.300 | 3.550 | - | bridge 8.5; infra: serving/inference, kv-cache, distributed; multi-project 5 → typed person relations |
| 39 | [[company/TensorMesh/Junchen Jiang|Junchen Jiang]] | 26.434 | best-first | 8.900 | 2.050 | 2.700 | - | bridge 8.9; gap 2.0; infra: serving/inference, kv-cache, distributed → typed person relations, technical areas |
| 40 | [[community/llm-d/llm-d/Abdullah Gharaibeh|Abdullah Gharaibeh]] | 26.099 | best-first | 8.522 | 1.300 | 3.650 | - | bridge 8.5; infra: serving/inference, kv-cache, scheduler → typed person relations |
| 41 | [[company/OpenAI/柳晓萱 Xiaoxuan Liu|柳晓萱]] | 26.010 | best-first | 11.300 | 1.300 | 1.000 | - | bridge 11.3; infra: serving/inference → typed person relations |
| 42 | [[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾]] | 25.948 | best-first | 8.522 | 1.800 | 2.700 | - | bridge 8.5; infra: serving/inference, kv-cache, distributed; multi-project 3 → typed person relations, biographical/context depth |
| 43 | [[company/字节跳动/方佳瑞 Jiarui Fang|方佳瑞]] | 25.807 | best-first | 10.185 | 1.300 | 1.750 | - | bridge 10.2; infra: serving/inference, distributed → typed person relations |
| 44 | [[community/flashinfer-ai/FlashInfer/Jingfan Sun|Jingfan Sun]] | 25.756 | best-first | 8.720 | 1.300 | 3.400 | - | bridge 8.7; infra: serving/inference, kernel, distributed → typed person relations |
| 45 | [[university/浙江大学/Huan Li|Huan Li]] | 25.430 | best-first | 6.507 | 2.400 | 4.000 | - | bridge 6.5; gap 2.4; infra: serving/inference, kv-cache, scheduler; multi-project 2 → project/community links, typed person relations |
| 46 | [[company/潞晨科技/尤洋 Yang You|尤洋]] | 25.381 | best-first | 9.070 | 2.300 | 1.750 | - | bridge 9.1; gap 2.3; infra: serving/inference, distributed → typed person relations, biographical/context depth |
| 47 | [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫]] | 25.224 | best-first | 8.872 | 2.400 | 1.600 | - | bridge 8.9; gap 2.4; infra: scheduler, distributed → project/community links, typed person relations |
| 48 | [[community/ai-dynamo/Dynamo/Ryan McCormick|Ryan McCormick]] | 25.146 | best-first | 7.522 | 3.050 | 2.600 | - | bridge 7.5; gap 3.0; infra: serving/inference, distributed, disaggregation; multi-project 2 → typed person relations, technical areas, biographical/context depth |
| 49 | [[community/ai-dynamo/NIXL/Adit Ranadive|Adit Ranadive]] | 24.917 | best-first | 8.200 | 3.050 | 1.700 | - | bridge 8.2; gap 3.0; infra: kv-cache, distributed; multi-project 5 → typed person relations, technical areas, biographical/context depth |
| 50 | [[community/ModelTC/LightLLM/Junyi Chen|Junyi Chen]] | 24.880 | best-first | 8.485 | 2.700 | 1.750 | - | bridge 8.5; gap 2.7; infra: serving/inference, distributed → current affiliation, typed person relations, biographical/context depth |
| 51 | [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢]] | 24.816 | best-first | 8.370 | 2.200 | 2.400 | - | bridge 8.4; gap 2.2; infra: kernel, distributed, moe; multi-project 2 → current affiliation, typed person relations |
| 52 | [[university/清华大学/Yingdi Shan|闪英迪]] | 24.749 | best-first | 7.050 | 1.800 | 3.500 | - | bridge 7.0; infra: serving/inference, scheduler, kernel → typed person relations, biographical/context depth |
| 53 | [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]] | 24.707 | best-first | 5.700 | 3.050 | 4.000 | - | bridge 5.7; gap 3.0; infra: serving/inference, kv-cache, scheduler → typed person relations, technical areas, biographical/context depth |
| 54 | [[community/kvcache-ai/KTransformers/Peilin Li|Peilin Li]] | 24.524 | best-first | 7.872 | 3.050 | 1.950 | - | bridge 7.9; gap 3.0; infra: serving/inference, kv-cache → typed person relations, technical areas, biographical/context depth |
| 55 | [[company/趋境科技/卢佳豪 Jiahao Lu|卢佳豪]] | 24.491 | best-first | 8.707 | 1.800 | 1.950 | - | bridge 8.7; infra: serving/inference, kv-cache → typed person relations, biographical/context depth |
| 56 | [[company/RadixArk/Qiaolin Yu|Qiaolin Yu]] | 24.444 | best-first | 9.485 | 1.300 | 1.750 | - | bridge 9.5; infra: serving/inference, distributed; multi-project 2 → typed person relations |
| 57 | [[community/vllm-project/vLLM/Matthew Bonanni|Matthew Bonanni]] | 24.410 | best-first | 8.007 | 2.550 | 1.750 | - | bridge 8.0; gap 2.5; infra: serving/inference, distributed → typed person relations, technical areas, biographical/context depth |
| 58 | [[company/RadixArk/Baizhou Zhang|Baizhou Zhang]] | 24.381 | best-first | 8.522 | 1.300 | 2.650 | - | bridge 8.5; infra: serving/inference, kernel, distributed → typed person relations |
| 59 | [[community/LMCache/LMCache/Samm Shen|Samuel Shen]] | 24.306 | best-first | 9.250 | 1.300 | 1.950 | - | bridge 9.2; infra: serving/inference, kv-cache; multi-project 2 → typed person relations |
| 60 | [[company/趋境科技/Hongbo Kang|Hongbo Kang]] | 24.112 | best-first | 8.550 | 2.900 | 0.950 | - | bridge 8.6; gap 2.9; infra: kv-cache → project/community links, typed person relations, biographical/context depth |

## How to use

- `best-first`: 优先补齐缺失关系维度，不沿单一路径无限向下钻。
- `selective-dfs`: 只对高桥梁度、高推理相关、且仍存在关系缺口的人物做深挖，并受 `--dfs-budget` 全局预算约束。
- 需要从某个人出发时，使用 `--seed <name-or-id>`；距离会进入评分，默认优先保留 2-hop 局部网络。
