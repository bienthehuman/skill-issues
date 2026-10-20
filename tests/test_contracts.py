"""Packaging and evaluation isolation, not behavioral validation."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
spec = importlib.util.spec_from_file_location('contracts', ROOT / 'evals/contracts.py')
fixtures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixtures)


class ContractTests(unittest.TestCase):
    def test_isolated_bundles_and_faults(self):
        canonical = {p: p.read_bytes() for p in (ROOT / 'skills').rglob('*') if p.is_file()}
        with tempfile.TemporaryDirectory() as directory:
            for agent in ('codex', 'claude'):
                for case in fixtures.CASES:
                    project = fixtures.prepare(Path(directory) / (agent + case), agent, case)
                    base = project / ('.agents/skills' if agent == 'codex' else '.claude/skills')
                    expected = {'read-the-contract'}
                    if case.startswith('integration'):
                        expected.add('think-before-you-commit')
                    self.assertEqual({p.name for p in base.iterdir()}, expected)
                    refs = base / 'read-the-contract/references'
                    for name in ('interface-check', 'authorization'):
                        path = refs / (name + '.md')
                        missing = case == ('missing-interface' if name == 'interface-check' else 'missing-authority')
                        self.assertEqual(path.exists(), not missing)
                        if not missing:
                            self.assertEqual(path.read_bytes(), (ROOT / 'shared/references' / path.name).read_bytes())
                    self.assertTrue((refs / 'contract-review.md').is_file())
                    with self.assertRaises(ValueError):
                        fixtures.prepare(project, agent, case)
        self.assertEqual(canonical, {p: p.read_bytes() for p in canonical})
