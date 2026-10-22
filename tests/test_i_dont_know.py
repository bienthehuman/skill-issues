"""Focused packaging and fixture integrity checks, not behavioral assertions."""
import importlib.util
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'skills/i-dont-know'
spec = importlib.util.spec_from_file_location('refinement_refs', ROOT / 'scripts/reference_tools.py')
refs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refs)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}


class LearningPackaging(unittest.TestCase):
    def test_standalone_bundle_and_links(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {Path('SKILL.md'), Path('references/learning-notes.md')})
        with tempfile.TemporaryDirectory() as folder:
            for host in ('.agents', '.claude'):
                root = Path(folder) / host
                installed = root / 'skills' / SOURCE.name
                shutil.copytree(SOURCE, installed)
                self.assertEqual(snapshot(installed), original)
                for document in installed.rglob('*.md'):
                    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', document.read_text(encoding='utf-8')):
                        resolved = (document.parent / target).resolve()
                        self.assertTrue(resolved.is_relative_to(installed.resolve()))
                        self.assertTrue(resolved.is_file())
                shutil.copytree(ROOT / 'shared', root / 'shared')
                before = snapshot(root)
                for options in ({}, {'check': True}, {'update': True}):
                    self.assertEqual(refs.reference_plan(root, **options), ([], 1))
                    self.assertEqual(snapshot(root), before)
        self.assertEqual(snapshot(SOURCE), original)

    def test_fixtures_and_manifest(self):
        sys.path.insert(0, str(ROOT / 'evals'))
        try:
            import learning as fixtures
            with tempfile.TemporaryDirectory() as folder:
                for agent in ('codex', 'claude'):
                    for case, prompt in fixtures.CASES.items():
                        project = fixtures.prepare(Path(folder) / (agent + '-' + case), agent, case)
                        base = project / ('.agents/skills' if agent == 'codex' else '.claude/skills')
                        expected = {SOURCE.name}
                        sibling = fixtures.SIBLINGS.get(case)
                        if sibling:
                            expected.add(sibling)
                        self.assertEqual({p.name for p in base.iterdir()}, expected)
                        self.assertEqual(snapshot(base / SOURCE.name), snapshot(SOURCE))
                        self.assertEqual((project / 'prompt.txt').read_text(encoding='utf-8').strip(), prompt)
                        import hashlib
                        import json
                        manifest = json.loads((project / 'manifest.json').read_text(encoding='utf-8'))
                        self.assertEqual(manifest['skills'], sorted(expected))
                        for name, digest in manifest['files'].items():
                            self.assertEqual(hashlib.sha256((project / name).read_bytes()).hexdigest(), digest)
                        with self.assertRaisesRegex(ValueError, 'must not exist'):
                            fixtures.prepare(project, agent, case)
        finally:
            sys.path.pop(0)


if __name__ == '__main__':
    unittest.main()
