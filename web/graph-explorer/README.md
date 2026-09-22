# Graph Explorer 2.0

The explorer is a presentation layer over the repository's existing Markdown graph.

## Data flow

1. `scripts/audit-graph.py` and `scripts/audit-typed-relations.py` produce graph artifacts.
2. `scripts/build-graph-explorer.py` adapts them into `data.json`.
3. Graphology loads the graph in the browser.
4. Louvain derives communities at runtime.
5. ForceAtlas2 lays out the graph and Sigma.js renders it with WebGL.

Galaxy community IDs, layout coordinates, colors and sizes are view state. They are not persisted to Markdown or schema.

## Local development

Generate data first, then place it beside the Vite build during local testing:

```bash
python3 scripts/build-graph-explorer.py --generated generated --output web/graph-explorer/public --base-path /ai_infra_relationship
cd web/graph-explorer
npm install
npm run dev
```

The production GitHub Pages workflow builds the same frontend and copies its output into Quartz's `public/graph-explorer` directory.
