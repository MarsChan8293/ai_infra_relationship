# Mooncake Focused HAES Run — 2026-09-16

This is a bounded seed-focused research pass centered on `Mooncake`. It is intentionally isolated from the unfinished global HAES Run 4 branch.

## Search objective

Expand Mooncake along four typed directions:

1. governance / maintainers,
2. person affiliation and identity quality,
3. 2026 inference ↔ training / RL data-plane projects,
4. missing production-side paper authors.

The pass does not recursively chase every integration or every contributor logo.

## Outcomes

| # | Source | Action | Outcome | Graph / evidence delta |
| ---: | --- | --- | --- | --- |
| 1 | Mooncake | maintainers | success | Official `MAINTAINERS.md` confirms four Codeowners: Teng Ma, Shangming Cai, Feng Ren, Ke Yang. Promoted Ke Yang and Shangming Cai from note pages to canonical `person` nodes. |
| 2 | Ke Yang | affiliation | success | Official maintainer record uses `yangke@approaching.ai` and labels him Approaching AI; structured current affiliation to 趋境科技 without inventing title. |
| 3 | Shangming Cai | affiliation | success | Official maintainer record labels him Alibaba Cloud and assigns SGLang Integration responsibility; structured current affiliation to 阿里巴巴. |
| 4 | Mooncake | related project: TENT | success | Added canonical TENT project from the 2026 paper and Mooncake Transfer Engine NEXT roadmap. |
| 5 | Mooncake | related project: Checkpoint Engine | success | Added Moonshot AI Checkpoint Engine; its P2P model-weight update path directly depends on Mooncake Transfer Engine. |
| 6 | Mooncake | related project: Speculators | success | Added vLLM Speculators; multi-node online training uses a Mooncake backend to stream hidden states between inference workers and trainers. |
| 7 | Mooncake | related project: TorchSpec | success | Added TorchSpec; its disaggregated speculative-decoding training streams hidden states through Mooncake Store. |
| 8 | Miles | Mooncake integration | success | Added the 2026-08 Mooncake rollout-data-transfer integration to the existing Miles node. |
| 9 | Mooncake | paper-author gap | success | Added Zheming Li, Weiran He, Jialei Cui, Xinran Xu as project-credit person nodes. Their 2025 Moonshot AI paper affiliations are kept historical and are not promoted to 2026 current employment. |
| 10 | Mooncake | contributor organizations | rejected | `MAINTAINERS.md` shows many contributor logos, but explicitly calls them Contributors and invites logos through PRs. These were not promoted to governance/member-company edges. |

## Graph delta

### New canonical nodes

- `TENT`
- `Checkpoint Engine`
- `Speculators`
- `TorchSpec`
- `Zheming Li`
- `Weiran He`
- `Jialei Cui`
- `Xinran Xu`

### Existing nodes enriched

- `Mooncake`
- `Ke Yang` (note → person)
- `Shangming Cai` (note → person)
- `月之暗面`
- `Miles`
- `LightSeek Foundation`

## Main finding

The strongest new structural result is that Mooncake should no longer be modeled only as a KV-cache serving project. By 2026 its official ecosystem forms a broader data-plane chain:

`KV cache / Store → Transfer Engine → TENT → RL weight & rollout transfer → hidden-state streaming → speculative decoding training`

Concrete paths include:

- `Mooncake → TENT → Checkpoint Engine`
- `Mooncake → Miles`
- `Mooncake → Speculators → vLLM`
- `Mooncake → TorchSpec → LightSeek Foundation / vLLM / SGLang / TensorRT-LLM`

This makes Mooncake a bridge between inference serving and post-training/RL infrastructure rather than merely a remote KV-cache backend.

## Evidence boundaries

- A current Codeowner entry is sufficient for governance role and the organization explicitly named in that entry.
- A 2025 paper affiliation is historical evidence, not automatic 2026 `current_affiliations`.
- Project integration is a project-level edge and does not imply direct person-to-person collaboration.
- Contributor logos are not treated as governance or company ownership.

## Primary sources

- https://github.com/kvcache-ai/Mooncake/blob/main/MAINTAINERS.md
- https://github.com/kvcache-ai/Mooncake
- https://www.usenix.org/conference/fast25/presentation/qin
- https://arxiv.org/abs/2604.00368
- https://github.com/MoonshotAI/checkpoint-engine
- https://github.com/vllm-project/speculators
- https://github.com/lightseekorg/TorchSpec
- https://github.com/radixark/miles
