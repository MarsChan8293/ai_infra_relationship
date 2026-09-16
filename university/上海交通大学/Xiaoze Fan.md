---
type: person
name: Xiaoze Fan
aliases: ["Xiaoze Fan", "范晓泽", "JasonFan", "jason-fxz"]
current_affiliations: ["上海交通大学","UC Berkeley Sky Computing Lab"]
schools:
  - "UC Berkeley"
  - "上海交通大学"
communities: [FreeToken, SGLang]
roles: [Undergraduate Researcher, Visiting Student Researcher, FreeToken Co-first Author, mini-SGLang Developer]
public_email: jasonfxz@sjtu.edu.cn
areas: [llm-serving, moe-inference, edge-inference, scheduling, radix-cache, chunked-prefill, overlap-scheduling, gpu-systems]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"university/UC Berkeley/Shuo Yang","type":["mentor-network","paper-coauthor","research-collaboration"],"project":"FreeToken","start":"2026","confidence":"high","evidence":["https://jasonfxz.top/","https://arxiv.org/abs/2608.16157"]}'
  - '{"target":"company/Inferact/Ion Stoica","type":["mentor-network","research-collaboration","paper-coauthor"],"project":"FreeToken","start":"2026","confidence":"high","evidence":["https://jasonfxz.top/","https://arxiv.org/abs/2608.16157"]}'
---
# Xiaoze Fan（范晓泽）

上海交通大学致远学院 ACM Honors Class 计算机本科生；2026 年起在 UC Berkeley Sky Computing Lab 担任 Visiting Student Researcher。个人主页明确写明由 [[company/Inferact/Ion Stoica|Ion Stoica]] supervised、由 [[university/UC Berkeley/Shuo Yang|Shuo Yang]] mentored。

## FreeToken

[[community/FlashML-org/FreeToken/FreeToken|FreeToken]] 论文共同一作，是该项目连接 Berkeley Sky、上海交通大学与 SGLang 生态的重要人物节点。

FreeToken 关注消费级硬件上的大 MoE inference：CPU–GPU 自适应执行、expert residency/cache、host-memory streaming、KV/state reuse 和显存动态分配。Xiaoze Fan 的公开研究兴趣本身就是 ML systems / efficient LLM systems，因此项目方向与其此前工作具有连续性。

## mini-SGLang / SGLang 桥

Xiaoze Fan 的个人主页和 GitHub 均将 **mini-SGLang** 列为本人主要项目。mini-SGLang 当前位于 `sgl-project/mini-sglang`，是一个紧凑但高性能的 SGLang 实现，包含：
- Radix Cache；
- Chunked Prefill；
- Overlap Scheduling；
- Tensor Parallelism；
- FlashAttention / FlashInfer kernels。

FreeToken 官方 README 又明确说明项目 **deeply inspired by mini-SGLang**，因此存在一条直接且高价值的技术传播链：

`SGLang → mini-SGLang → Xiaoze Fan → FreeToken`

这里记录的是项目与代码设计传承，不把所有 SGLang maintainer 自动写成 Xiaoze Fan 的直接人际关系。

## SGLang 直接贡献

个人 CV 记录其参与 PD-Multiplexing，并将相关实现 upstream 到 SGLang 社区。因此 `communities: [SGLang]` 有直接工程贡献依据，不只是因为 mini-SGLang 名称相近。

## 教育 / 研究网络

- 上海交通大学：ACM Honors Class，本科计算机；
- UC Berkeley Sky Computing Lab：2026 Visiting Student Researcher；
- Ion Stoica：访问研究 supervisor；
- Shuo Yang：mentor；同时为 FreeToken 共同一作。

## 公开职业邮箱

`jasonfxz@sjtu.edu.cn`，来自个人主页 / CV 与 FreeToken Git commit trailer，属于学校职业/学术邮箱，可作为 canonical public_email。

## 学校关联
- [[university/UC Berkeley/UC Berkeley|UC Berkeley]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。
- [[university/上海交通大学/上海交通大学|上海交通大学]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://jasonfxz.top/
- https://jasonfxz.top/assets/pdf/CV.pdf
- https://github.com/jason-fxz
- https://github.com/sgl-project/mini-sglang
- https://github.com/FlashML-org/FreeToken
- https://arxiv.org/abs/2608.16157
- https://github.com/FlashML-org/FreeToken/commit/9d32fa8642ac2f8ba3500089fbca72ea267a12c7
