# Typed Relation Coverage

由 `scripts/audit-typed-relations.py` 自动生成。`typed_person_link_coverage` 只表示人物页中已解析的人物 wikilink 有多少被结构化关系覆盖，不代表事实完整度。

- Typed relation edges: 358
- Person nodes with typed relations: 110 / 261
- Hard errors: 0
- Warnings: 4

## Relation types

- `coworker`: 148
- `paper-coauthor`: 139
- `research-collaboration`: 73
- `open-source-collaboration`: 71
- `mentor-network`: 53
- `technical-collaboration`: 50
- `cofounder`: 38
- `advisor`: 15
- `same-lab`: 10
- `community-maintainer`: 10
- `student`: 9
- `career-connection`: 5

## Next migration candidates

优先展示 bridge score 高、已有 person-to-person wikilink、但尚未建立 typed relations 的人物。

| Rank | Person | Bridge | Degree | Person links | Typed relations |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]] | 10.059 | 10 | 4 | 0 |
| 2 | [[community/hpcaitech/Colossal-AI/Hongxin Liu|Hongxin Liu]] | 9.770 | 8 | 4 | 0 |
| 3 | [[community/deepseek-ai/DeepSeek-Infra/Jiashi Li|Jiashi Li]] | 9.009 | 10 | 3 | 0 |
| 4 | [[company/趋境科技/卢佳豪 Jiahao Lu|卢佳豪]] | 8.707 | 6 | 2 | 0 |
| 5 | [[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]] | 8.685 | 11 | 6 | 0 |
| 6 | [[company/OpenAI/Luke Metz|Luke Metz]] | 8.522 | 9 | 4 | 0 |
| 7 | [[community/ModelTC/LightLLM/Junyi Chen|Junyi Chen]] | 8.485 | 5 | 2 | 0 |
| 8 | [[community/llm-d/llm-d/Clayton Coleman|Clayton Coleman]] | 8.370 | 8 | 3 | 0 |
| 9 | [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢]] | 8.370 | 8 | 3 | 0 |
| 10 | [[university/北京大学/吴童 Tong Wu|Tong Wu]] | 8.357 | 6 | 1 | 0 |
| 11 | [[university/北京大学/Yining Shi|Yining Shi]] | 8.200 | 7 | 4 | 0 |
| 12 | [[university/启元实验室/王豪杰 Haojie Wang|王豪杰]] | 8.200 | 7 | 1 | 0 |
| 13 | [[community/vllm-project/vLLM/Matthew Bonanni|Matthew Bonanni]] | 8.007 | 6 | 2 | 0 |
| 14 | [[community/ai-dynamo/NIXL/Mikhail Brinskiy|Mikhail Brinskiy]] | 7.785 | 5 | 1 | 0 |
| 15 | [[community/openEuler/openYuanRong/梁义 Yi Liang|梁义]] | 7.522 | 4 | 1 | 0 |
| 16 | [[company/深度求索/郭达雅 Daya Guo|郭达雅]] | 7.159 | 10 | 4 | 0 |
| 17 | [[university/北京大学/程羽 Yu Cheng|Yu Cheng]] | 6.870 | 8 | 4 | 0 |
| 18 | [[community/flashinfer-ai/FlashInfer/陈天奇 Tianqi Chen|陈天奇]] | 6.700 | 7 | 1 | 0 |
| 19 | [[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]] | 6.520 | 8 | 3 | 0 |
| 20 | [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航]] | 6.507 | 6 | 1 | 0 |
| 21 | [[university/UC Berkeley/Xiangxi Mo|Xiangxi Mo]] | 6.372 | 4 | 1 | 0 |
| 22 | [[university/北京大学/Lei Wang|Lei Wang]] | 6.350 | 7 | 3 | 0 |
| 23 | [[community/flashinfer-ai/FlashInfer/aleozlx|Alex Yang]] | 6.157 | 6 | 4 | 0 |
| 24 | [[community/llm-d/llm-d/Ashok Chandrasekar|Ashok Chandrasekar]] | 6.157 | 6 | 3 | 0 |
| 25 | [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]] | 6.157 | 6 | 4 | 0 |
| 26 | [[community/llm-d/llm-d/Vita Bortnikov|Vita Bortnikov]] | 6.157 | 6 | 4 | 0 |
| 27 | [[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行]] | 6.157 | 6 | 3 | 0 |
| 28 | [[university/上海交通大学/Fan Wu|Fan Wu]] | 6.022 | 4 | 1 | 0 |
| 29 | [[university/启元实验室/李映辉 Yinghui Li|李映辉]] | 5.935 | 5 | 4 | 0 |
| 30 | [[university/启元实验室/潘泽众 Zezhong Pan|潘泽众]] | 5.935 | 5 | 4 | 0 |
| 31 | [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成]] | 5.935 | 5 | 4 | 0 |
| 32 | [[community/Ascend/ops-transformer/Konstantin Berestizshevsky|Konstantin Berestizshevsky]] | 5.672 | 4 | 1 | 0 |
| 33 | [[community/ai-dynamo/Dynamo/Matej Kosec|Matej Kosec]] | 5.672 | 4 | 2 | 0 |
| 34 | [[community/llm-d/llm-d/张家驹 Jiaju Zhang|张家驹]] | 5.672 | 4 | 1 | 0 |
| 35 | [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远]] | 5.672 | 4 | 2 | 0 |
| 36 | [[university/上海交通大学/Shengzhong Liu|Shengzhong Liu]] | 5.350 | 3 | 2 | 0 |
| 37 | [[community/Ascend/ops-transformer/wangchao661|wangchao661]] | 5.350 | 3 | 1 | 0 |
| 38 | [[community/openEuler/openYuanRong/罗站城 Zhancheng Luo|罗站城]] | 5.350 | 3 | 1 | 0 |
| 39 | [[company/阿里巴巴/林俊旸 Junyang Lin|林俊旸]] | 4.822 | 9 | 5 | 0 |
| 40 | [[company/阿里巴巴/惠彬原 Binyuan Hui|惠彬原]] | 4.670 | 8 | 4 | 0 |

## Structured bridge nodes

| Person | Bridge | Person links | Typed | Coverage |
| --- | ---: | ---: | ---: | ---: |
| [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超]] | 14.855 | 16 | 16 | 100.0% |
| [[community/vllm-project/vLLM/李卓翰 Zhuohan Li|李卓翰]] | 14.274 | 4 | 4 | 100.0% |
| [[company/趋境科技/武永卫 Yongwei Wu|武永卫]] | 14.274 | 5 | 3 | 60.0% |
| [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰]] | 12.672 | 8 | 6 | 75.0% |
| [[company/Inferact/Ion Stoica|Ion Stoica]] | 12.598 | 8 | 8 | 100.0% |
| [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]] | 12.520 | 8 | 7 | 87.5% |
| [[community/vllm-project/vLLM/乔一凡 Yifan Qiao|乔一凡]] | 12.520 | 8 | 8 | 100.0% |
| [[company/Inferact/Woosuk Kwon|Woosuk Kwon]] | 12.437 | 6 | 6 | 100.0% |
| [[company/RadixArk/盛颖 Ying Sheng|盛颖]] | 12.170 | 7 | 7 | 100.0% |
| [[university/清华大学/Mingxing Zhang|章明星]] | 12.087 | 4 | 3 | 75.0% |
| [[company/清程极智/翟季冬 Jidong Zhai|翟季冬]] | 11.692 | 11 | 10 | 90.9% |
| [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]] | 11.535 | 12 | 11 | 91.7% |
| [[community/vllm-project/vLLM/Simon Mo|Simon Mo]] | 11.387 | 7 | 7 | 100.0% |
| [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]] | 11.350 | 7 | 7 | 100.0% |
| [[company/OpenAI/柳晓萱 Xiaoxuan Liu|柳晓萱]] | 11.300 | 7 | 4 | 57.1% |
| [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民]] | 11.207 | 5 | 5 | 100.0% |
| [[community/vllm-project/vLLM/Robert Shaw|Robert Shaw]] | 10.922 | 6 | 5 | 83.3% |
| [[community/vllm-project/vLLM/Michael Goin|Michael Goin]] | 10.507 | 5 | 4 | 80.0% |
| [[company/TensorMesh/程翊华 Yihua Cheng|程翊华]] | 10.409 | 4 | 2 | 50.0% |
| [[community/sgl-project/SGLang/谢志强 Zhiqiang Xie|谢志强]] | 10.409 | 3 | 3 | 100.0% |
| [[company/清程极智/郑纬民 Weimin Zheng|郑纬民]] | 10.300 | 4 | 2 | 50.0% |
| [[company/字节跳动/方佳瑞 Jiarui Fang|方佳瑞]] | 10.185 | 4 | 3 | 75.0% |
| [[company/OpenAI/翁家翌 Jiayi Weng|翁家翌]] | 10.057 | 5 | 3 | 60.0% |
| [[community/vllm-project/vLLM/Nick Hill|Nick Hill]] | 9.922 | 5 | 3 | 60.0% |
| [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]] | 9.770 | 2 | 2 | 100.0% |
| [[community/vllm-project/vLLM/Yongye Zhu|Yongye Zhu]] | 9.709 | 4 | 2 | 50.0% |
| [[community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie|谢威宇]] | 9.600 | 3 | 3 | 100.0% |
| [[university/清华大学/Ruoyu Qin|秦若愚]] | 9.572 | 3 | 3 | 100.0% |
| [[company/RadixArk/Qiaolin Yu|Qiaolin Yu]] | 9.485 | 4 | 4 | 100.0% |
| [[company/RadixArk/朱邦华 Banghua Zhu|朱邦华]] | 9.485 | 5 | 5 | 100.0% |
