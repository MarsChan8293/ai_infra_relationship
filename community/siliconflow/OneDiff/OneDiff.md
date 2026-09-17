---
type: project
name: OneDiff
organization: siliconflow
companies: ["硅基流动"]
company_relation: company-led
layer: diffusion-inference-compiler
open_source: true
linked_companies:
  - "company/硅基流动/硅基流动"
linked_projects:
  - "community/Oneflow-Inc/OneFlow/OneFlow"
---
# OneDiff

OneDiff 是硅基流动维护的开源 diffusion / multimodal inference acceleration 项目，面向 Diffusers、ComfyUI、Stable Diffusion WebUI 等生态提供编译、GPU kernel 和 serving 优化能力。

## 技术位置
- PyTorch module compilation 与 accelerated graph save/load
- optimized GPU kernels
- dynamic shape 与 graph cache，减少线上 serving 重编译成本
- quantization 与显存优化
- distributed inference 场景中的单卡 compiler acceleration
- Diffusion / DiT / image-video generation inference

## Compiler 路线
OneDiff 公开支持两条 compiler backend：
- [[OneFlow]]：延续硅基流动团队的 OneFlow 系统技术积累。
- Nexfort：面向 PyTorch 2.x / DiT 等 workload 的轻量 compiler backend；OneDiff 文档称部分优化正逐步由 OneFlow backend 迁移到 Nexfort。

这使 OneDiff 成为观察 `OneFlow → compiler/kernel → multimodal inference` 人才迁移的高价值入口。

## 人物探索边界
GitHub release、PR、Wiki 中可见 `strint`、`marigoold`、`clackhan`、Xiaoyu Xu 等高信号贡献者 / 维护活动，但本节点暂不据此自动推断其当前雇主。后续应通过企业邮箱、官方团队页、持续 review ownership 等证据再升级人物节点。

## Sources
- https://github.com/siliconflow/onediff
- https://github.com/siliconflow/onediff/wiki
- https://github.com/siliconflow/onediff/tree/main/src/onediff/infer_compiler/backends/nexfort
