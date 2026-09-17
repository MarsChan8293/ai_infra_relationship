---
type: project
name: OneDiff
organization: siliconflow
linked_people:
  - "community/siliconflow/OneDiff/strint"
  - "community/siliconflow/OneDiff/marigoold"
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
- [[community/Oneflow-Inc/OneFlow/OneFlow|OneFlow]]：延续硅基流动团队的 OneFlow 系统技术积累。
- Nexfort：面向 PyTorch 2.x / DiT 等 workload 的轻量 compiler backend；OneDiff 文档称部分优化正逐步由 OneFlow backend 迁移到 Nexfort。

这使 OneDiff 成为观察 `OneFlow → compiler/kernel → multimodal inference` 人才迁移的高价值入口。

## 维护者 / Collaborator
- [[community/siliconflow/OneDiff/strint|strint]]：GitHub Pull Requests 页面将其标记为 **Collaborator**；release notes 中持续出现 compiler、CI、项目维护相关改动。
- [[community/siliconflow/OneDiff/marigoold|marigoold]]：GitHub Pull Requests 页面将其标记为 **Collaborator**；长期参与 Diffusers / ComfyUI / SD3 等集成与维护。

这里的 `Collaborator` 是 GitHub 项目级权限/身份信号，只用于确认 OneDiff 的维护关系，不自动推断真实姓名、当前雇主或公司职位。`clackhan`、Xiaoyu Xu 等仍保留为贡献线索，待更稳定的 governance / review ownership 证据后再升级人物边。

## Sources
- https://github.com/siliconflow/onediff
- https://github.com/siliconflow/onediff/pulls
- https://github.com/siliconflow/onediff/releases
- https://github.com/siliconflow/onediff/wiki
- https://github.com/siliconflow/onediff/tree/main/src/onediff/infer_compiler/backends/nexfort

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/硅基流动/硅基流动|硅基流动]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
