# Typed Relation Coverage

由 `scripts/audit-typed-relations.py` 自动生成。`typed_person_link_coverage` 只表示人物页中已解析的人物 wikilink 有多少被结构化关系覆盖，不代表事实完整度。

- Typed relation edges: 401
- Person nodes with typed relations: 126 / 327
- Hard errors: 0
- Warnings: 6

## Relation types

- `paper-coauthor`: 171
- `coworker`: 162
- `research-collaboration`: 92
- `open-source-collaboration`: 75
- `mentor-network`: 58
- `technical-collaboration`: 53
- `cofounder`: 40
- `advisor`: 30
- `same-lab`: 15
- `student`: 14
- `community-maintainer`: 10
- `career-connection`: 8

## Next migration candidates

优先展示 bridge score 高、已有 person-to-person wikilink、但尚未建立 typed relations 的人物。

| Rank | Person | Bridge | Degree | Person links | Typed relations |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]] | 10.059 | 10 | 4 | 0 |
| 2 | [[community/hpcaitech/Colossal-AI/Hongxin Liu|Hongxin Liu]] | 9.770 | 8 | 4 | 0 |
| 3 | [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]] | 9.009 | 10 | 3 | 0 |
| 4 | [[community/vllm-project/vLLM/Lucas Wilkinson|Lucas Wilkinson]] | 8.872 | 9 | 4 | 0 |
| 5 | [[company/趋境科技/卢佳豪 Jiahao Lu|卢佳豪]] | 8.707 | 6 | 2 | 0 |
| 6 | [[company/OpenAI/Luke Metz|Luke Metz]] | 8.522 | 9 | 4 | 0 |
| 7 | [[community/ModelTC/LightLLM/Junyi Chen|Junyi Chen]] | 8.485 | 5 | 2 | 0 |
| 8 | [[company/腾讯/Stary|Stary]] | 8.485 | 5 | 2 | 0 |
| 9 | [[community/llm-d/llm-d/Clayton Coleman|Clayton Coleman]] | 8.370 | 8 | 3 | 0 |
| 10 | [[community/kvcache-ai/Mooncake/Yue Chen|Yue Chen]] | 8.370 | 8 | 4 | 0 |
| 11 | [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢]] | 8.370 | 8 | 3 | 0 |
| 12 | [[university/北京大学/吴童 Tong Wu|Tong Wu]] | 8.357 | 6 | 1 | 0 |
| 13 | [[university/北京大学/Yining Shi|Yining Shi]] | 8.200 | 7 | 4 | 0 |
| 14 | [[university/启元实验室/王豪杰 Haojie Wang|王豪杰]] | 8.200 | 7 | 1 | 0 |
| 15 | [[community/vllm-project/vLLM/Matthew Bonanni|Matthew Bonanni]] | 8.007 | 6 | 3 | 0 |
| 16 | [[community/ai-dynamo/NIXL/Mikhail Brinskiy|Mikhail Brinskiy]] | 7.785 | 5 | 1 | 0 |
| 17 | [[community/openEuler/openYuanRong/梁义 Yi Liang|梁义]] | 7.522 | 4 | 1 | 0 |
| 18 | [[company/深度求索/郭达雅 Daya Guo|郭达雅]] | 7.159 | 10 | 4 | 0 |
| 19 | [[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]] | 7.157 | 13 | 3 | 0 |
| 20 | [[university/北京大学/程羽 Yu Cheng|Yu Cheng]] | 6.870 | 8 | 4 | 0 |
| 21 | [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇]] | 6.700 | 7 | 1 | 0 |
| 22 | [[community/kvcache-ai/Mooncake/Xinpeng Zhao|Xinpeng Zhao]] | 6.672 | 9 | 4 | 0 |
| 23 | [[community/kvcache-ai/Mooncake/Xuchun Shang|Xuchun Shang]] | 6.672 | 9 | 4 | 0 |
| 24 | [[community/Ascend/MemCache/yrewzjsx|yrewzjsx]] | 6.672 | 9 | 5 | 0 |
| 25 | [[community/Ascend/MemCache/Zixi Qu|Zixi Qu]] | 6.520 | 8 | 3 | 0 |
| 26 | [[community/Ascend/MemCache/chenyz6|chenyz6]] | 6.520 | 8 | 5 | 0 |
| 27 | [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航]] | 6.507 | 6 | 1 | 0 |
| 28 | [[university/UC Berkeley/Xiangxi Mo|Xiangxi Mo]] | 6.372 | 4 | 1 | 0 |
| 29 | [[university/北京大学/Lei Wang|Lei Wang]] | 6.350 | 7 | 3 | 0 |
| 30 | [[community/kvcache-ai/Mooncake/Zhanhao Cao|Zhanhao Cao]] | 6.350 | 7 | 4 | 0 |
| 31 | [[community/flashinfer-ai/FlashInfer/aleozlx|Alex Yang]] | 6.157 | 6 | 4 | 0 |
| 32 | [[community/llm-d/llm-d/Ashok Chandrasekar|Ashok Chandrasekar]] | 6.157 | 6 | 3 | 0 |
| 33 | [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]] | 6.157 | 6 | 4 | 0 |
| 34 | [[community/llm-d/llm-d/Vita Bortnikov|Vita Bortnikov]] | 6.157 | 6 | 4 | 0 |
| 35 | [[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行]] | 6.157 | 6 | 3 | 0 |
| 36 | [[community/Ascend/MemCache/彭海清 Haiqing Peng|彭海清]] | 6.157 | 6 | 3 | 0 |
| 37 | [[university/上海交通大学/Fan Wu|Fan Wu]] | 6.022 | 4 | 1 | 0 |
| 38 | [[community/vllm-project/vLLM-Ascend/weijinqian0|Jinqian Wei]] | 5.935 | 5 | 3 | 0 |
| 39 | [[community/Ascend/MemCache/j00808874|j00808874]] | 5.935 | 5 | 2 | 0 |
| 40 | [[university/启元实验室/李映辉 Yinghui Li|李映辉]] | 5.935 | 5 | 4 | 0 |

## Structured bridge nodes

| Person | Bridge | Person links | Typed | Coverage |
| --- | ---: | ---: | ---: | ---: |
| [[company/趋境科技/武永卫 Yongwei Wu|武永卫]] | 16.307 | 12 | 12 | 100.0% |
| [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超]] | 14.855 | 16 | 16 | 100.0% |
| [[community/vllm-project/vLLM/李卓翰 Zhuohan Li|李卓翰]] | 14.274 | 4 | 4 | 100.0% |
| [[company/Inferact/Ion Stoica|Ion Stoica]] | 13.859 | 8 | 8 | 100.0% |
| [[university/清华大学/Mingxing Zhang|章明星]] | 12.948 | 4 | 4 | 100.0% |
| [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰]] | 12.672 | 8 | 6 | 75.0% |
| [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]] | 12.520 | 8 | 7 | 87.5% |
| [[community/vllm-project/vLLM/乔一凡 Yifan Qiao|乔一凡]] | 12.520 | 8 | 8 | 100.0% |
| [[company/Inferact/Woosuk Kwon|Woosuk Kwon]] | 12.437 | 6 | 6 | 100.0% |
| [[company/RadixArk/盛颖 Ying Sheng|盛颖]] | 12.170 | 7 | 7 | 100.0% |
| [[company/清程极智/翟季冬 Jidong Zhai|翟季冬]] | 11.692 | 11 | 10 | 90.9% |
| [[company/清程极智/郑纬民 Weimin Zheng|郑纬民]] | 11.650 | 7 | 6 | 85.7% |
| [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]] | 11.535 | 12 | 11 | 91.7% |
| [[community/vllm-project/vLLM/Simon Mo|Simon Mo]] | 11.387 | 7 | 7 | 100.0% |
| [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]] | 11.350 | 7 | 7 | 100.0% |
| [[company/OpenAI/柳晓萱 Xiaoxuan Liu|柳晓萱]] | 11.300 | 7 | 4 | 57.1% |
| [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民]] | 11.207 | 5 | 5 | 100.0% |
| [[university/清华大学/Ruoyu Qin|秦若愚]] | 11.000 | 4 | 3 | 75.0% |
| [[community/vllm-project/vLLM/Robert Shaw|Robert Shaw]] | 10.922 | 6 | 5 | 83.3% |
| [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰]] | 10.857 | 5 | 2 | 40.0% |
| [[community/vllm-project/vLLM/Michael Goin|Michael Goin]] | 10.507 | 6 | 4 | 66.7% |
| [[company/TensorMesh/程翊华 Yihua Cheng|程翊华]] | 10.409 | 4 | 2 | 50.0% |
| [[community/sgl-project/SGLang/谢志强 Zhiqiang Xie|谢志强]] | 10.409 | 3 | 3 | 100.0% |
| [[company/字节跳动/方佳瑞 Jiarui Fang|方佳瑞]] | 10.185 | 4 | 3 | 75.0% |
| [[company/OpenAI/翁家翌 Jiayi Weng|翁家翌]] | 10.057 | 5 | 3 | 60.0% |
| [[community/vllm-project/vLLM/Nick Hill|Nick Hill]] | 9.922 | 5 | 3 | 60.0% |
| [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]] | 9.770 | 2 | 2 | 100.0% |
| [[community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie|谢威宇]] | 9.600 | 3 | 3 | 100.0% |
| [[community/kvcache-ai/KTransformers/Xianglin Chen|Xianglin Chen]] | 9.572 | 6 | 2 | 33.3% |
| [[company/RadixArk/Qiaolin Yu|Qiaolin Yu]] | 9.485 | 4 | 4 | 100.0% |
