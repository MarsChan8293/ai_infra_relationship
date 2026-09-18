# School Link Coverage

由 `scripts/audit-school-links.py` 自动生成。`schools:` 只表示可核验的教育、任职或访问研究关联，不自动推断导师、同学或同门关系。

- Person nodes: 375
- People with ≥1 school: 156
- People without known school: 219
- Coverage: 41.6%
- Person-school associations: 204
- School nodes: 47
- Audit errors: 0

## Top schools by linked people

| School | People |
| --- | ---: |
| 清华大学 | 61 |
| UC Berkeley | 28 |
| 北京大学 | 21 |
| 上海交通大学 | 19 |
| Carnegie Mellon University | 7 |
| 浙江大学 | 7 |
| University of Chicago | 6 |
| Stanford University | 4 |
| 厦门大学 | 4 |
| UCLA | 3 |
| Harvard University | 2 |
| 北京邮电大学 | 2 |
| 四川大学 | 2 |
| Stony Brook University | 2 |
| Georgia Institute of Technology | 2 |
| University of Washington | 2 |
| University of Texas at Austin | 2 |
| 香港科技大学 | 2 |
| 香港中文大学 | 2 |
| Seoul National University | 1 |
| Franklin W. Olin College of Engineering | 1 |
| Cornell Tech | 1 |
| 西交利物浦大学 | 1 |
| Columbia University | 1 |
| 南京大学 | 1 |
| UC Davis | 1 |
| 复旦大学 | 1 |
| 北京航空航天大学 | 1 |
| 中山大学 | 1 |
| Massachusetts Institute of Technology | 1 |

## High-value people still missing a verified school association

| Rank | Person | Bridge score | Degree |
| ---: | --- | ---: | ---: |
| 1 | [[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]] | 11.198 | 18 |
| 2 | [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成]] | 10.535 | 11 |
| 3 | [[university/启元实验室/潘泽众 Zezhong Pan|潘泽众]] | 8.55 | 7 |
| 4 | [[company/腾讯/Stary|Stary]] | 8.485 | 5 |
| 5 | [[company/腾讯/Baolong Mao|Baolong Mao]] | 7.75 | 7 |
| 6 | [[community/vllm-project/vLLM/Roger Wang|Roger Wang]] | 7.372 | 9 |
| 7 | [[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]] | 7.157 | 13 |
| 8 | [[company/RadixArk/Xiaoyu Zhang|Xiaoyu Zhang]] | 6.87 | 8 |
| 9 | [[company/杭州先进编译科技有限公司/李嘉楠|李嘉楠]] | 6.7 | 7 |
| 10 | [[community/kvcache-ai/Mooncake/Xinpeng Zhao|Xinpeng Zhao]] | 6.672 | 9 |
| 11 | [[community/kvcache-ai/Mooncake/Xuchun Shang|Xuchun Shang]] | 6.672 | 9 |
| 12 | [[community/Ascend/MemCache/yrewzjsx|yrewzjsx]] | 6.672 | 9 |
| 13 | [[community/flashinfer-ai/FlashInfer/Yang Xu|Yang Xu]] | 6.52 | 8 |
| 14 | [[community/Ascend/MemCache/Zixi Qu|Zixi Qu]] | 6.52 | 8 |
| 15 | [[community/Ascend/MemCache/chenyz6|chenyz6]] | 6.52 | 8 |
| 16 | [[company/硅基流动/柳俊丞 Juncheng Liu|柳俊丞]] | 6.507 | 6 |
| 17 | [[company/杭州先进编译科技有限公司/柴赟达|柴赟达]] | 6.507 | 6 |
| 18 | [[community/llm-d/llm-d/Carlos Costa|Carlos Costa]] | 6.35 | 7 |
| 19 | [[company/RadixArk/Cheng Wan|Cheng Wan]] | 6.35 | 7 |
| 20 | [[company/基流科技/Yanmin Jia|Yanmin Jia]] | 6.35 | 7 |
| 21 | [[community/kvcache-ai/Mooncake/Zhanhao Cao|Zhanhao Cao]] | 6.35 | 7 |
| 22 | [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远]] | 6.285 | 5 |
| 23 | [[community/flashinfer-ai/FlashInfer/aleozlx|Alex Yang]] | 6.157 | 6 |
| 24 | [[community/llm-d/llm-d/Ashok Chandrasekar|Ashok Chandrasekar]] | 6.157 | 6 |
| 25 | [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]] | 6.157 | 6 |
| 26 | [[company/基流科技/He Liu|He Liu]] | 6.157 | 6 |
| 27 | [[community/llm-d/llm-d/Nili Guy|Nili Guy]] | 6.157 | 6 |
| 28 | [[community/llm-d/llm-d/Vita Bortnikov|Vita Bortnikov]] | 6.157 | 6 |
| 29 | [[community/Ascend/MemCache/彭海清 Haiqing Peng|彭海清]] | 6.157 | 6 |
| 30 | [[community/flagos-ai/FlagOS/敖玉龙 Yulong Ao|敖玉龙]] | 6.157 | 6 |
| 31 | [[company/腾讯/Chunxiao Zheng|Chunxiao Zheng]] | 6.022 | 4 |
| 32 | [[community/deepseek-ai/DeepSeek-Infra/Huanqi Cao|Huanqi Cao]] | 5.935 | 5 |
| 33 | [[community/vllm-project/vLLM-Ascend/weijinqian0|Jinqian Wei]] | 5.935 | 5 |
| 34 | [[community/Project-HAMi/HAMi/archlitchi|Mengxuan Li]] | 5.935 | 5 |
| 35 | [[community/NVIDIA/TensorRT-LLM/Yi Zhang|Yi Zhang]] | 5.935 | 5 |
| 36 | [[community/Ascend/MemCache/j00808874|j00808874]] | 5.935 | 5 |
| 37 | [[university/启元实验室/李映辉 Yinghui Li|李映辉]] | 5.935 | 5 |
| 38 | [[company/硅基流动/赵震 Zhao Zhen|赵震]] | 5.935 | 5 |
| 39 | [[community/kvcache-ai/KTransformers/Boxin Zhang|Boxin Zhang]] | 5.7 | 3 |
| 40 | [[community/kvcache-ai/KTransformers/Jianwei Dong|Jianwei Dong]] | 5.7 | 3 |
| 41 | [[community/kvcache-ai/KTransformers/Jingqi Tang|Jingqi Tang]] | 5.7 | 3 |
| 42 | [[company/IBM/Martin Hickey|Martin Hickey]] | 5.7 | 3 |
| 43 | [[community/kvcache-ai/KTransformers/Qingliang Ou|Qingliang Ou]] | 5.7 | 3 |
| 44 | [[community/ai-dynamo/Dynamo/Stefan Schimanski|Stefan Schimanski]] | 5.7 | 3 |
| 45 | [[community/LMCache/LMCache/Tony Lin|Tony Lin]] | 5.7 | 3 |
| 46 | [[company/摩尔线程/Xiaodong Ye|Xiaodong Ye]] | 5.7 | 3 |
| 47 | [[company/沐曦/Xin Li|Xin Li]] | 5.7 | 3 |
| 48 | [[company/天数智芯/honglyua|honglyua]] | 5.7 | 3 |
| 49 | [[company/天数智芯/shengyan.zhao|shengyan.zhao]] | 5.7 | 3 |
| 50 | [[company/RadixArk/童心源 Xinyuan Tong|童心源]] | 5.7 | 3 |
