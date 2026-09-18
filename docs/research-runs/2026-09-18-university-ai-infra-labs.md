# 2026-09-18 University AI Infra Labs Add

## Goal

把上一轮筛出的高价值高校 AI Infra 实验室 / 研究组加入图谱，聚焦 inference optimization、serving、compiler/runtime、KV cache、quantization 与 distributed ML systems，而不是扩展成泛 AI 实验室目录。

## Added canonical nodes

- `university/University of Washington/SAMPL`
- `university/Stanford University/MAST Lab`
- `university/UC San Diego/UC San Diego`
- `university/UC San Diego/Hao AI Lab`
- `university/Carnegie Mellon University/Catalyst Group`
- `university/复旦大学/徐跃东课题组`

## Enriched existing nodes

- `university/University of Washington/SyFI Lab`
- `university/Massachusetts Institute of Technology/HAN Lab`
- `university/上海交通大学/IPADS`
- University of Washington / Stanford / Carnegie Mellon / 复旦 school pages were updated with canonical lab links.

## High-value graph bridges

- **SAMPL ↔ FlashInfer / TVM lineage** through Zihao Ye, Ruihang Lai, Tianqi Chen and Lianmin Zheng.
- **SAMPL ↔ CMU Catalyst** is explicitly described by the SAMPL official site as part of its collaboration network.
- **MAST ↔ SGLang** through Zhiqiang Xie and Contextra's SGLang-based implementation.
- **Hao AI Lab ↔ vLLM / DistServe / Lookahead Decoding / FastChat** from Hao Zhang's current official project history.
- **Catalyst ↔ FlashInfer/compiler ecosystem** through Tianqi Chen, Ruihang Lai and Zihao Ye.
- **IPADS ↔ PowerInfer / KunServe / BlitzScale / KV cache systems**.
- **徐跃东课题组 ↔ LLM training/inference systems** from the official Fudan faculty page.

## Naming / evidence boundaries

- CMU is represented by the official **Catalyst Group**, not an invented umbrella label such as “CMU ML Systems Network”.
- The Fudan node is deliberately named **徐跃东课题组**. “Yuedong Xu Group” is only an alias for graph search; the official page uses the generic term 课题组 and does not establish a formal English lab brand.
- Same university, shared publication venue, downstream integration, or project compatibility does not imply direct collaboration, advisor relation, employment, or shared governance.
- Existing generated schema / reverse-link artifacts were not edited manually; repository automation should regenerate them from Markdown.

## Follow-up EXPAND candidates

1. SyFI: Baris Kasikci, Stephanie Wang, Arvind Krishnamurthy; NanoFlow, M*, VibeServe, VoxServe.
2. SAMPL: Luis Ceze; Punica, Atom, Fiddler, SparseTIR.
3. HAN Lab: Song Han, Jiaming Tang, Junxian Guo; QServe, LServe, AWQ, StreamingLLM.
4. MAST: Christos Kozyrakis; Contextra, RaidServe.
5. Hao AI Lab: Hao Zhang; Dynasor, DeepConf and the DistServe author network.
6. Catalyst: Zhihao Jia, Rashmi Vinayak; FlexFlow Serve, Helix, XGrammar, Mirage Persistent Kernel.
7. 徐跃东课题组: students and concrete LLM training/inference systems with public code or systems-paper evidence.

## Primary sources checked

- https://syfi.cs.washington.edu/
- https://sampl.cs.washington.edu/
- https://hanlab.mit.edu/
- https://mast.stanford.edu/
- https://cseweb.ucsd.edu/~haozhang/
- https://ipads.sjtu.edu.cn/
- https://catalyst.cs.cmu.edu/
- https://ai3.fudan.edu.cn/info/1088/2024.htm
