# Graph quality and relationship exports

Install Python dependencies with `python3 -m pip install -r scripts/requirements.txt`.
All graph/typed-relation/schema/index exports and entity field readers use
`scripts/graph_common.py`. Quoted commas, block lists, native YAML relationship
objects, JSON-string relationship items and string dates are supported. Duplicate
YAML keys, malformed frontmatter and unterminated frontmatter fail visibly.

`scripts/audit-node-schema.py` enforces registered types, required fields, known
field types, date formats and Project enum values in both CI workflows. Primary
`layer` values come from `schema/project.yaml`; fine detail belongs in `areas`.
`status` describes lifecycle; `maturity` describes research/production readiness;
`code_availability` distinguishes public, closed and unconfirmed source. A public
repository does not by itself prove a production-ready system or an open-source
license. Historical layer detail is preserved in `areas`, with a migration log in
`research/project-schema-normalization.json`.

Project integrations resolve only to Project nodes. Canonical paths disambiguate
same-name entities. Missing integration targets and missing Markdown links fail
the audits, rather than silently omitting the declared relation.

Typed edges preserve their authored source, target, time, confidence and direct
evidence. Derived Project integration and Project–Concept support assertions carry
`provenance.source_path`, `field`, source line, page-level source URLs and the
page's verification date. Page references are explicitly marked as not individually
verified evidence; derived assertions default to medium confidence. The absence
of an assertion-specific source must not be disguised by copying unrelated page
URLs into its direct `evidence` array.

The explorer groups edges visually by unordered pair, but retains every original
assertion and its direction. `advisor` means the **target is the source's advisor**;
`student` means the **target is the source's student**. Project–Concept arrows point
from implementation/consumer to concept. Symmetric collaborations remain visually
undirected. Clicking or keyboard-activating an edge reveals original assertions,
time, confidence, verification date and evidence/provenance. Path Finder defaults
to association paths, with a directed mode that respects directional assertions.

Person-link coverage is the intersection of outgoing person wikilink targets and
typed person relation targets, divided by the outgoing person link count. Extra
typed targets are reported separately. An empty denominator reports zero coverage;
it must not produce artificial 100% coverage or percentages above 100%.

Run `python3 scripts/test-graph-quality.py` for parser, schema, reference,
provenance, direction and coverage regressions. Existing research planner tests
remain separate. Schema validity and link resolution do not prove factual accuracy:
current affiliations require current evidence, and contributor/maintainer/employment
roles remain distinct.
