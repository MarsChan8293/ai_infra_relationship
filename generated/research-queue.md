# Research Queue

由 `scripts/generate-research-queue.py` 自动生成。它排序的是下一轮研究价值，不是人物重要性。

算法：**Gap-aware Best-First BFS + Selective DFS**。先用局部 BFS 建立邻域，再按桥梁度、关系缺口、推理相关性、证据质量与新颖性重新排序；只有高价值桥梁人物才触发 DFS 深挖。

公式：`1.60×bridge + 1.80×gap + 2.00×infra_relevance + 0.80×evidence + 0.90×novelty - 1.20×distance_penalty`。

| Rank | Person | Score | Strategy | Bridge | Gap | Infra | Distance | Why / next |
| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超]] | 33.468 | selective-dfs | 14.855 | 1.300 | 1.750 | - | bridge 14.9; infra: serving/inference, distributed; multi-project 2 → typed person relations, hidden person chain |
| 2 | [[company/趋境科技/武永卫 Yongwei Wu|武永卫]] | 32.977 | selective-dfs | 12.598 | 1.300 | 3.450 | - | bridge 12.6; infra: serving/inference, kv-cache, distributed; multi-project 3 → typed person relations, hidden person chain |
| 3 | [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰]] | 32.654 | selective-dfs | 13.159 | 1.300 | 2.700 | - | bridge 13.2; infra: serving/inference, kv-cache, distributed; multi-project 3 → typed person relations, hidden person chain |
| 4 | [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]] | 32.558 | selective-dfs | 11.474 | 1.300 | 4.000 | - | bridge 11.5; infra: serving/inference, kv-cache, scheduler; multi-project 5 → typed person relations, hidden person chain |
| 5 | [[community/vllm-project/vLLM/李卓翰 Zhuohan Li|李卓翰]] | 32.538 | selective-dfs | 14.274 | 1.300 | 1.750 | - | bridge 14.3; infra: serving/inference, distributed; multi-project 2 → typed person relations, hidden person chain |
| 6 | [[university/清华大学/Mingxing Zhang|章明星]] | 32.159 | selective-dfs | 12.087 | 1.300 | 3.450 | - | bridge 12.1; infra: serving/inference, kv-cache, distributed; multi-project 4 → typed person relations, hidden person chain |
| 7 | [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民]] | 32.131 | selective-dfs | 10.757 | 2.200 | 3.550 | - | bridge 10.8; gap 2.2; infra: serving/inference, kv-cache, scheduler; multi-project 4 → current affiliation, typed person relations, hidden person chain |
| 8 | [[community/sgl-project/SGLang/谢志强 Zhiqiang Xie|谢志强]] | 31.865 | selective-dfs | 10.409 | 3.300 | 2.800 | - | bridge 10.4; gap 3.3; infra: serving/inference, kv-cache, scheduler → current affiliation, project/community links, typed person relations |
| 9 | [[community/vllm-project/vLLM/乔一凡 Yifan Qiao|乔一凡]] | 31.632 | selective-dfs | 12.520 | 1.300 | 2.700 | - | bridge 12.5; infra: serving/inference, kv-cache, distributed; multi-project 2 → typed person relations, hidden person chain |
| 10 | [[company/清程极智/翟季冬 Jidong Zhai|翟季冬]] | 31.530 | selective-dfs | 10.848 | 1.300 | 4.000 | - | bridge 10.8; infra: serving/inference, kv-cache, kernel; multi-project 3 → typed person relations, hidden person chain |
| 11 | [[company/深度求索/梁文锋 Liang Wenfeng|梁文锋]] | 31.005 | selective-dfs | 9.485 | 2.400 | 4.000 | - | bridge 9.5; gap 2.4; infra: serving/inference, kernel, distributed → project/community links, typed person relations, hidden person chain |
| 12 | [[company/Inferact/Woosuk Kwon|Woosuk Kwon]] | 30.892 | selective-dfs | 12.437 | 1.300 | 2.550 | - | bridge 12.4; infra: kv-cache, scheduler, distributed; multi-project 2 → typed person relations, hidden person chain |
| 13 | [[company/RadixArk/盛颖 Ying Sheng|盛颖]] | 30.872 | selective-dfs | 12.170 | 1.300 | 2.600 | - | bridge 12.2; infra: serving/inference, scheduler, distributed; multi-project 2 → typed person relations, hidden person chain |
| 14 | [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]] | 30.024 | selective-dfs | 12.520 | 1.300 | 1.950 | - | bridge 12.5; infra: serving/inference, kv-cache; multi-project 2 → typed person relations, hidden person chain |
| 15 | [[company/Inferact/Ion Stoica|Ion Stoica]] | 29.577 | selective-dfs | 12.598 | 1.300 | 1.750 | - | bridge 12.6; infra: serving/inference, distributed; multi-project 4 → typed person relations, hidden person chain |
| 16 | [[community/sgl-project/SGLang/尹良升 Liangsheng Yin|尹良升]] | 29.496 | selective-dfs | 8.720 | 3.800 | 2.800 | - | bridge 8.7; gap 3.8; infra: serving/inference, kv-cache, scheduler; multi-project 2 → current affiliation, project/community links, typed person relations |
| 17 | [[company/TensorMesh/程翊华 Yihua Cheng|程翊华]] | 29.091 | selective-dfs | 11.107 | 1.300 | 2.700 | - | bridge 11.1; infra: serving/inference, kv-cache, distributed; multi-project 2 → typed person relations, hidden person chain |
| 18 | [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与]] | 28.825 | selective-dfs | 9.359 | 1.300 | 4.000 | - | bridge 9.4; infra: serving/inference, kernel, distributed; multi-project 2 → typed person relations, hidden person chain |
| 19 | [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]] | 28.705 | selective-dfs | 9.770 | 1.300 | 3.450 | - | bridge 9.8; infra: serving/inference, kv-cache, distributed; multi-project 3 → typed person relations, hidden person chain |
| 20 | [[community/llm-d/llm-d/Maroon Ayoub|Maroon Ayoub]] | 28.551 | selective-dfs | 9.707 | 1.300 | 3.550 | - | bridge 9.7; infra: serving/inference, kv-cache, distributed; multi-project 5 → typed person relations, hidden person chain |
| 21 | [[community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie|谢威宇]] | 28.409 | selective-dfs | 9.600 | 1.300 | 3.600 | - | bridge 9.6; infra: serving/inference, kv-cache, kernel → typed person relations, hidden person chain |
| 22 | [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]] | 28.233 | selective-dfs | 11.350 | 1.300 | 1.950 | - | bridge 11.3; infra: serving/inference, kv-cache; multi-project 3 → typed person relations, hidden person chain |
| 23 | [[university/北京大学/吴童 Tong Wu|Tong Wu]] | 28.225 | selective-dfs | 7.785 | 2.900 | 3.600 | - | bridge 7.8; gap 2.9; infra: serving/inference, kv-cache, kernel → project/community links, typed person relations, biographical/context depth |
| 24 | [[university/清华大学/Ruoyu Qin|秦若愚]] | 28.146 | selective-dfs | 9.572 | 1.300 | 3.550 | - | bridge 9.6; infra: serving/inference, kv-cache, scheduler; multi-project 2 → typed person relations, hidden person chain |
| 25 | [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]] | 27.934 | selective-dfs | 9.009 | 2.700 | 2.400 | - | bridge 9.0; gap 2.7; infra: kernel, distributed, moe; multi-project 3 → current affiliation, typed person relations, biographical/context depth |
| 26 | [[community/kvcache-ai/KTransformers/Ziwei Yuan|Ziwei Yuan]] | 27.824 | selective-dfs | 7.872 | 3.050 | 3.600 | - | bridge 7.9; gap 3.0; infra: serving/inference, kv-cache, kernel → typed person relations, technical areas, biographical/context depth |
| 27 | [[company/清程极智/郑纬民 Weimin Zheng|郑纬民]] | 27.800 | selective-dfs | 10.300 | 1.300 | 2.700 | - | bridge 10.3; infra: serving/inference, kv-cache, distributed → typed person relations, hidden person chain |
| 28 | [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]] | 27.387 | selective-dfs | 10.059 | 2.200 | 1.750 | - | bridge 10.1; gap 2.2; infra: serving/inference, distributed; multi-project 3 → current affiliation, typed person relations, hidden person chain |
| 29 | [[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪]] | 26.825 | selective-dfs | 9.135 | 1.300 | 3.400 | - | bridge 9.1; infra: serving/inference, kernel, distributed → typed person relations, hidden person chain |
| 30 | [[community/hpcaitech/Colossal-AI/Hongxin Liu|Hongxin Liu]] | 26.801 | selective-dfs | 9.770 | 2.700 | 1.400 | - | bridge 9.8; gap 2.7; infra: distributed, quantization → current affiliation, typed person relations, biographical/context depth |
| 31 | [[community/ai-dynamo/Dynamo/Sungsoo Ha|Sungsoo Ha]] | 26.729 | selective-dfs | 8.135 | 3.050 | 2.600 | - | bridge 8.1; gap 3.0; infra: serving/inference, distributed, disaggregation; multi-project 2 → typed person relations, technical areas, biographical/context depth |
| 32 | [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰]] | 26.555 | selective-dfs | 9.222 | 1.300 | 2.800 | - | bridge 9.2; infra: serving/inference, kv-cache, disaggregation → typed person relations, hidden person chain |
| 33 | [[community/llm-d/llm-d/Danny Harnik|Danny Harnik]] | 26.547 | selective-dfs | 8.522 | 1.300 | 3.550 | - | bridge 8.5; infra: serving/inference, kv-cache, distributed; multi-project 5 → typed person relations, hidden person chain |
| 34 | [[community/llm-d/llm-d/Abdullah Gharaibeh|Abdullah Gharaibeh]] | 26.504 | selective-dfs | 8.522 | 1.300 | 3.650 | - | bridge 8.5; infra: serving/inference, kv-cache, scheduler → typed person relations, hidden person chain |
| 35 | [[company/OpenAI/柳晓萱 Xiaoxuan Liu|柳晓萱]] | 26.010 | selective-dfs | 11.300 | 1.300 | 1.000 | - | bridge 11.3; infra: serving/inference → typed person relations, hidden person chain |
| 36 | [[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾]] | 25.948 | selective-dfs | 8.522 | 1.800 | 2.700 | - | bridge 8.5; infra: serving/inference, kv-cache, distributed; multi-project 3 → typed person relations, biographical/context depth, hidden person chain |
| 37 | [[company/TensorMesh/Junchen Jiang|Junchen Jiang]] | 25.834 | selective-dfs | 8.900 | 2.550 | 1.950 | - | bridge 8.9; gap 2.5; infra: serving/inference, kv-cache → typed person relations, technical areas, biographical/context depth |
| 38 | [[company/字节跳动/方佳瑞 Jiarui Fang|方佳瑞]] | 25.807 | selective-dfs | 10.185 | 1.300 | 1.750 | - | bridge 10.2; infra: serving/inference, distributed → typed person relations, hidden person chain |
| 39 | [[community/flashinfer-ai/FlashInfer/Jingfan Sun|Jingfan Sun]] | 25.756 | selective-dfs | 8.720 | 1.300 | 3.400 | - | bridge 8.7; infra: serving/inference, kernel, distributed → typed person relations, hidden person chain |
| 40 | [[company/硅基流动/袁进辉 Jinhui Yuan|袁进辉]] | 25.632 | selective-dfs | 8.720 | 2.400 | 1.750 | - | bridge 8.7; gap 2.4; infra: serving/inference, distributed → project/community links, typed person relations, hidden person chain |
| 41 | [[university/浙江大学/Huan Li|Huan Li]] | 25.430 | selective-dfs | 6.507 | 2.400 | 4.000 | - | bridge 6.5; gap 2.4; infra: serving/inference, kv-cache, scheduler; multi-project 2 → project/community links, typed person relations, hidden person chain |
| 42 | [[company/潞晨科技/尤洋 Yang You|尤洋]] | 25.381 | selective-dfs | 9.070 | 2.300 | 1.750 | - | bridge 9.1; gap 2.3; infra: serving/inference, distributed → typed person relations, biographical/context depth, hidden person chain |
| 43 | [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫]] | 25.224 | selective-dfs | 8.872 | 2.400 | 1.600 | - | bridge 8.9; gap 2.4; infra: scheduler, distributed → project/community links, typed person relations, hidden person chain |
| 44 | [[community/ai-dynamo/Dynamo/Ryan McCormick|Ryan McCormick]] | 25.146 | selective-dfs | 7.522 | 3.050 | 2.600 | - | bridge 7.5; gap 3.0; infra: serving/inference, distributed, disaggregation; multi-project 2 → typed person relations, technical areas, biographical/context depth |
| 45 | [[community/ai-dynamo/NIXL/Adit Ranadive|Adit Ranadive]] | 24.917 | selective-dfs | 8.200 | 3.050 | 1.700 | - | bridge 8.2; gap 3.0; infra: kv-cache, distributed; multi-project 5 → typed person relations, technical areas, biographical/context depth |
| 46 | [[community/ModelTC/LightLLM/Junyi Chen|Junyi Chen]] | 24.880 | selective-dfs | 8.485 | 2.700 | 1.750 | - | bridge 8.5; gap 2.7; infra: serving/inference, distributed → current affiliation, typed person relations, biographical/context depth |
| 47 | [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢]] | 24.816 | selective-dfs | 8.370 | 2.200 | 2.400 | - | bridge 8.4; gap 2.2; infra: kernel, distributed, moe; multi-project 2 → current affiliation, typed person relations, hidden person chain |
| 48 | [[university/清华大学/Yingdi Shan|闪英迪]] | 24.749 | selective-dfs | 7.050 | 1.800 | 3.500 | - | bridge 7.0; infra: serving/inference, scheduler, kernel → typed person relations, biographical/context depth, hidden person chain |
| 49 | [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]] | 24.707 | selective-dfs | 5.700 | 3.050 | 4.000 | - | bridge 5.7; gap 3.0; infra: serving/inference, kv-cache, scheduler → typed person relations, technical areas, biographical/context depth |
| 50 | [[community/kvcache-ai/KTransformers/Peilin Li|Peilin Li]] | 24.524 | selective-dfs | 7.872 | 3.050 | 1.950 | - | bridge 7.9; gap 3.0; infra: serving/inference, kv-cache → typed person relations, technical areas, biographical/context depth |
| 51 | [[company/趋境科技/卢佳豪 Jiahao Lu|卢佳豪]] | 24.491 | selective-dfs | 8.707 | 1.800 | 1.950 | - | bridge 8.7; infra: serving/inference, kv-cache → typed person relations, biographical/context depth, hidden person chain |
| 52 | [[company/RadixArk/Qiaolin Yu|Qiaolin Yu]] | 24.444 | selective-dfs | 9.485 | 1.300 | 1.750 | - | bridge 9.5; infra: serving/inference, distributed; multi-project 2 → typed person relations, hidden person chain |
| 53 | [[company/RadixArk/Baizhou Zhang|Baizhou Zhang]] | 24.381 | selective-dfs | 8.522 | 1.300 | 2.650 | - | bridge 8.5; infra: serving/inference, kernel, distributed → typed person relations, hidden person chain |
| 54 | [[company/趋境科技/Hongbo Kang|Hongbo Kang]] | 24.112 | best-first | 8.550 | 2.900 | 0.950 | - | bridge 8.6; gap 2.9; infra: kv-cache → project/community links, typed person relations, biographical/context depth |
| 55 | [[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行]] | 24.013 | selective-dfs | 6.157 | 2.700 | 3.400 | - | bridge 6.2; gap 2.7; infra: serving/inference, kernel, distributed → current affiliation, typed person relations, biographical/context depth |
| 56 | [[community/vllm-project/vLLM/Matthew Bonanni|Matthew Bonanni]] | 24.005 | selective-dfs | 8.007 | 2.550 | 1.750 | - | bridge 8.0; gap 2.5; infra: serving/inference, distributed → typed person relations, technical areas, biographical/context depth |
| 57 | [[company/深度求索/陈德里 Deli Chen|陈德里]] | 23.954 | selective-dfs | 8.370 | 2.400 | 1.650 | - | bridge 8.4; gap 2.4; infra: kernel, moe → project/community links, typed person relations, hidden person chain |
| 58 | [[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]] | 23.907 | selective-dfs | 5.700 | 3.050 | 3.600 | - | bridge 5.7; gap 3.0; infra: serving/inference, kv-cache, kernel → typed person relations, technical areas, biographical/context depth |
| 59 | [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]] | 23.907 | selective-dfs | 5.700 | 3.050 | 3.600 | - | bridge 5.7; gap 3.0; infra: serving/inference, kv-cache, kernel → typed person relations, technical areas, biographical/context depth |
| 60 | [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航]] | 23.823 | selective-dfs | 6.507 | 3.950 | 1.900 | - | bridge 6.5; gap 4.0; infra: serving/inference, kernel → current affiliation, typed person relations, technical areas |

## How to use

- `best-first`: 优先补齐缺失关系维度，不沿单一路径无限向下钻。
- `selective-dfs`: 只对高桥梁度、高推理相关、且仍存在关系缺口的人物做深挖。
- 需要从某个人出发时，使用 `--seed <name-or-id>`；距离会进入评分，默认优先保留 2-hop 局部网络。
