---
type: person
name: Jinqian Wei
english_name: Jinqian Wei
aliases: ["weijinqian0", "@weijinqian0", "weijinqian_v1", "@weijinqian_v1"]
public_email: weijinqian@huawei.com
communities: [vLLM-Ascend]
roles: [Committer, RFC Author]
areas: [llm-inference, ascend, attention, operators, graph-execution, moe, kv-cache]
confidence: high
last_verified: "2026-09"
---
# Jinqian Wei（weijinqian0 / weijinqian_v1）

社区：[[vLLM-Ascend]]

## 身份与组织证据
vLLM-Ascend 官方 Contributors 页面将 GitHub ID `@weijinqian0` 对应实名列为 **Jinqian Wei**，并列入 committer 名单，日期为 2025-10。

2026-01 的 operator adaptation framework 提交提供了进一步的 handle 消歧证据：同一提交同时出现 `Signed-off-by: weijinqian_v1 <weijinqian@huawei.com>` 与 `Signed-off-by: weijinqian0 <1184188277@qq.com>`，并由 `weijinqian_v1` 共同署名。结合官方实名映射，可把 `weijinqian0` 与 `weijinqian_v1` 归并为同一开源身份。canonical `public_email` 使用公开职业邮箱 `weijinqian@huawei.com`；QQ 邮箱仅作为历史提交证据，不作为默认联系字段。

这里仍不把企业邮箱单独升级为“当前在职”声明；华为关联由邮箱域名机制生成 `email_affiliations` / `linked_companies`。

## 社区贡献
- 活跃于 Attention backend、Ascend 算子、图执行、Model Runner V2 与模型性能相关工作。
- 参与跨硬件 operator adaptation framework，使不同 Ascend 硬件版本的算子差异可通过中间适配层消化。
- 参与 Model Runner V2 post-update 性能优化与 MLA builder/cache refactor。
- 2026-09 发起 DeepSeek V4.1 on Ascend roadmap RFC，覆盖 MoE quantization、通信与 attention projection 等推理路径；此前也参与 DeepSeek V4 KV Pool known-issue / release integration。

## 人物关系
- [[community/vllm-project/vLLM-Ascend/Wang Xiyuan|Wang Xiyuan]]：社区治理/Attention 工程邻接关系；缺 pair-specific 证据时不自动生成 typed edge。
- [[community/vllm-project/vLLM-Ascend/yiz-liu|yiz-liu]]：release integration / roadmap 邻接关系；不因 feature landing 自动推断直接协作强度。
- [[community/vllm-project/vLLM-Ascend/zzzzwwjj|zzzzwwjj]]：模型/算子实现邻接关系，保留作后续研究。

## Sources
- https://docs.vllm.ai/projects/ascend/en/latest/community/contributors.html
- https://docs.vllm.ai/projects/ascend/zh-cn/main/community/contributors.html
- https://github.com/vllm-project/vllm-ascend/commit/1ccb9acd9ad48e5a857f7f06887ccf66911d0b20
- https://github.com/vllm-project/vllm-ascend/commit/bdd90c0088ab3d477f9d007d22f087165ad9d201
- https://github.com/vllm-project/vllm-ascend/commit/dbe4c338f2fac797bba8d03352f13f4af7da2aa6
- https://github.com/vllm-project/vllm-ascend/issues/16375
- https://github.com/vllm-project/vllm-ascend/issues/15067
