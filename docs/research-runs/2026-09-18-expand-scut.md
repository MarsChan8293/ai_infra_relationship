# 2026-09-18 EXPAND 华南理工大学

## Operator

- operator: `EXPAND`
- seed: `华南理工大学`
- objective: 从学校节点向 AI Infra 实验室、核心人物、系统项目与产业桥梁扩一层，优先推理优化、算力调度、GPU/NPU、国产加速器和边缘部署。

## Added canonical nodes

- `university/华南理工大学/华南理工大学`
- `university/华南理工大学/先进计算体系结构团队`
- `university/华南理工大学/林伟伟 Weiwei Lin`
- `university/华南理工大学/王新华 Xinhua Wang`
- `university/华南理工大学/Kairos`
- `university/华南理工大学/国产可信算力产业应用创新实验室`
- `university/华南理工大学/许言午 Yanwu Xu`
- `company/广电五舟/广电五舟`

## High-value graph bridges

### ACAT → heterogeneous AI scheduling

ACAT 官方资料把 CPU/GPU/NPU 异构算力管理、深度学习负载调度、GPU 共享和面向 AI 大模型的算力优化列为当前研究方向；其研究资源明确包含 LLM inference scheduling。

### ACAT → Ascend

林伟伟团队公开介绍中记录了针对华为国产昇腾 AI 集群的任务调度与 NPU 碎片卡整理技术方案，并获华为火花奖。这是一条强技术合作线索，但不推断为华为雇佣或开源维护关系。

### 王新华 → Kairos / LLM scheduling

王新华官方学生页记录 GPU/NPU cluster scheduling、GPU sharing 与 Kairos；其公开 GitHub bio 直接写明大模型推理调度。

### SCUT → 广电五舟 → domestic AI compute

2026 年华南理工与广电五舟共建“国产可信算力产业应用创新实验室”，官方方向包含国产算力适配、云端训练、边缘推理、终端部署和国产芯片智算一体机。

### 广电五舟 → Ascend ecosystem

广电五舟公开披露与华为昇腾、沐曦、百度昆仑芯、阿里平头哥等国产芯片生态合作。当前没有证据把某一种芯片直接归因到 SCUT 联合实验室项目，因此保留为公司级生态关系。

## Intentionally not expanded

- SCUT-DLVCLab / TongGu：属于模型与视觉/NLP研究，当前与 inference infrastructure 的直接证据不足。
- SoulChat / 广东省数字孪生人重点实验室：偏领域模型与应用，本轮不作为 AI Infra 主干。
- 刘国志等 ACAT 大模型微调/安全研究者：有价值，但当前主要是 resource-efficient fine-tuning / safety alignment，不优先于推理调度。
- Concord / CoMi：王新华官方页标记为 Under Review，本轮不创建独立 canonical 项目，待论文状态稳定后 VERIFY。

## Follow-up

1. VERIFY ACAT 与华为昇腾合作的公开技术细节，寻找可公开的 scheduler / patent / paper / project 名称。
2. EXPAND 王新华，继续追踪 Concord、CoMi 及 LLM inference scheduling 是否已有公开论文或代码。
3. EXPAND 广电五舟，梳理其昇腾、沐曦、昆仑芯与平头哥的具体产品适配关系。
4. VERIFY 华南理工 × 广电五舟联合实验室具体一体机的 accelerator / runtime 软件栈，避免把公司级 Ascend 生态关系错误下沉到项目级。
5. DISCOVER SCUT 其他真正做 compiler / runtime / serving / heterogeneous compute 的团队，再决定是否扩第二层。

## Primary sources

- https://github.com/ACAT-SCUT/.github/blob/main/profile/README.md
- https://github.com/ACAT-SCUT/.github/blob/main/profile/research-resources/scheduling.md
- https://github.com/ACAT-SCUT/.github/blob/main/profile/students/wangxinhua.md
- https://github.com/henls
- https://news.scut.edu.cn/2026/0514/c41a59894/page.htm
- https://kjj.gz.gov.cn/xwlb/yw/content/post_10763798.html
- https://www.wuzhoucloud.com/
- https://static.cninfo.com.cn/finalpage/2026-08-06/1225461142.PDF
