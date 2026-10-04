#!/usr/bin/env python3
"""Regression tests for graph parsing, schema enforcement, references and explorer exports."""
import importlib.util
import json
import pathlib
import subprocess
import tempfile
import unittest
from graph_common import read_frontmatter, split_frontmatter, field_values

SCRIPTS = pathlib.Path(__file__).resolve().parent


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), SCRIPTS / (name + '.py'))
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


GRAPH = module('audit-graph')
TYPED = module('audit-typed-relations')
SCHEMA = module('audit-node-schema')
SIDECARS = module('generate-node-schemas')


class GraphQualityTests(unittest.TestCase):
    def test_block_lists_survive_all_consumers(self):
        text = '---\nname: Example\nhardware:\n  - ascend\naliases:\n  - CP\n---\n# Body\n'
        expected = {'name': 'Example', 'hardware': ['ascend'], 'aliases': ['CP']}
        self.assertEqual(GRAPH.parse_frontmatter(text)[0], expected)
        self.assertEqual(TYPED.parse_frontmatter(text), expected)
        self.assertEqual(SIDECARS.normalize_frontmatter({'type': 'project'}, text)[1]['hardware'], ['ascend'])

    def test_quoted_commas_and_escapes_are_not_delimiters(self):
        text = '---\naliases: ["MADSys Lab, Tsinghua University", "a\\\"b"]\n---\n'
        self.assertEqual(read_frontmatter(text)['aliases'], ['MADSys Lab, Tsinghua University', 'a"b'])
        self.assertEqual(field_values(text.splitlines()[1:-1], 'aliases'), ['MADSys Lab, Tsinghua University', 'a"b'])

    def test_native_relation_and_dates(self):
        text = '---\nlast_verified: 2026-10-04\nrelations:\n  - target: B\n    type: [advisor]\n    confidence: high\n---\n'
        parsed = read_frontmatter(text)
        self.assertEqual(parsed['last_verified'], '2026-10-04')
        self.assertEqual(parsed['relations'][0]['type'], ['advisor'])

    def test_crlf_and_body_preservation(self):
        self.assertEqual(split_frontmatter('---\r\nname: CP\r\n---\r\nbody\r\n'), ({'name': 'CP'}, 'body\r\n'))

    def test_invalid_yaml_is_not_silently_accepted(self):
        for text in ['---\nname: a\nname: b\n---\n', '---\nname: a', '---\n- a\n---\n']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                read_frontmatter(text)

    def test_schema_enforces_layer_lifecycle_and_list_types(self):
        schema = {'required': ['type', 'name'], 'fields': {'layer': {'enum': ['kernel']}, 'status': {'enum': ['active', 'unknown']}, 'hardware': {'type': 'array[string]'}}}
        errors = SCHEMA.validate({'type': 'project', 'name': 'A', 'layer': 'gpu-kernels', 'status': 'research', 'hardware': 'ascend'}, schema)
        self.assertEqual(len(errors), 3)
        self.assertFalse(SCHEMA.validate({'type': 'project', 'name': 'A', 'layer': 'kernel', 'status': 'unknown', 'hardware': ['ascend']}, schema))

    def test_coverage_counts_intersection_and_separates_extra_relations(self):
        self.assertEqual(TYPED.person_link_coverage({'A'}, {'A', 'B'}), (1, 1, 1.0))
        self.assertEqual(TYPED.person_link_coverage({'A', 'C'}, {'A', 'B'}), (1, 1, 0.5))
        self.assertEqual(TYPED.person_link_coverage(set(), {'B'}), (0, 1, 0.0))

    def test_name_with_slash_resolves_to_canonical_file(self):
        record = {'path': 'concept/Direct Storage IO.md', 'id': 'concept/Direct Storage IO', 'rel_no_ext': 'concept/Direct Storage IO'}
        source = {'rel_no_ext': 'concept/NVMe SSD'}
        self.assertEqual(GRAPH.resolve('Direct Storage I/O', source, {}, {'direct storage i/o': [record]})[0], record)

    def test_wikilink_normalizer_accepts_unnamed_index(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            (root / 'index.md').write_text('# Index\n[[CP]]\n')
            (root / 'CP.md').write_text('---\nname: Context Parallelism\naliases: [CP]\n---\n')
            result = subprocess.run(['node', str(SCRIPTS / 'normalize-wikilinks.mjs'), str(root)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_scoped_integrations_provenance_and_explorer_roundtrip(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            def write(path, text):
                destination = root / path
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(text)
            write('company/GPUStack/GPUStack.md', '---\ntype: company\nname: GPUStack\n---\n')
            write('community/GPUStack/GPUStack.md', '---\ntype: project\nname: GPUStack\n---\n')
            write('community/Runner/Runner.md', '---\ntype: project\nname: Runner\nintegrations:\n  - GPUStack\nlast_verified: 2026-10\n---\n## Sources\n- https://example.org/official\n')
            write('community/A/A.md', '---\ntype: person\nname: A\nrelations:\n  - target: community/B/B\n    type: [advisor]\n    confidence: high\n    start: "2020"\n    evidence: ["https://example.org/advisor"]\n---\n')
            write('community/B/B.md', '---\ntype: person\nname: B\n---\n')
            write('concept/CP.md', '---\ntype: concept\nname: Context Parallelism\naliases: [CP]\nprojects:\n  - Runner\n---\n## Sources\n- https://example.org/cp\n')
            for script in ['audit-graph', 'audit-typed-relations']:
                subprocess.run(['python3', str(SCRIPTS / (script + '.py')), '--root', str(root)], check=True, capture_output=True)
            typed = json.loads((root / 'generated/typed-edges.json').read_text())
            integration = next(edge for edge in typed if 'project-integration' in edge['relation_types'])
            self.assertEqual(integration['target'], 'community/GPUStack/GPUStack')
            self.assertEqual(integration['confidence'], 'medium')
            self.assertEqual(integration['provenance']['source_urls'], ['https://example.org/official'])
            self.assertEqual(integration['provenance']['field'], 'integrations')
            self.assertTrue(integration['provenance']['line'])
            output = root / 'explorer'
            subprocess.run(['python3', str(SCRIPTS / 'build-graph-explorer.py'), '--generated', str(root / 'generated'), '--output', str(output)], check=True, capture_output=True)
            data = json.loads((output / 'data.json').read_text())
            assertion = next(a for edge in data['edges'] for a in edge['assertions'] if 'advisor' in a['relation_types'])
            self.assertEqual(assertion['source'], 'community/A/A')
            self.assertEqual(assertion['target'], 'community/B/B')
            self.assertEqual(assertion['start'], '2020')
            self.assertEqual(assertion['evidence'], ['https://example.org/advisor'])
            html = (output / 'index.html').read_text()
            self.assertIn('marker-end', html)
            self.assertIn('edgeDetails', html)
            self.assertIn('pathMode', html)
            self.assertEqual(next(n for n in data['nodes'] if n['type'] == 'concept')['aliases'], ['CP'])


if __name__ == '__main__':
    unittest.main()
