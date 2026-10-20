"""Review fixture integrity and isolation; not behavioral assertions."""
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
import reviews


class ReviewFixtures(unittest.TestCase):
    def test_fresh_self_contained_fixtures(self):
        original = {p: p.read_bytes() for p in (ROOT / 'skills').rglob('*') if p.is_file()}
        with tempfile.TemporaryDirectory() as folder:
            for case in reviews.CASES:
                project = reviews.prepare(Path(folder) / case, 'codex', case)
                base = project / '.agents/skills'
                expected = {'trust-issues', 'read-the-contract'} if case == 'contract-available' else {'trust-issues'}
                self.assertEqual({p.name for p in base.iterdir()}, expected)
                for name in ('interface-check', 'authorization'):
                    ref = base / 'trust-issues/references' / (name + '.md')
                    missing = case == ('missing-interface' if name == 'interface-check' else 'missing-authority')
                    self.assertEqual(ref.exists(), not missing)
                    if not missing:
                        self.assertEqual(ref.read_bytes(), (ROOT / 'shared/references' / ref.name).read_bytes())
                with self.assertRaises(ValueError):
                    reviews.prepare(project, 'codex', case)
            wrong = Path(folder) / 'wrong-intent'
            self.assertIn('1.10', (wrong / 'CHANGE.diff').read_text())
            self.assertIn('discount', (wrong / 'REQUEST.md').read_text())
            drift = Path(folder) / 'http-drift'
            self.assertIn('customer_name.toUpperCase', (drift / 'resources/js/Receipt.tsx').read_text())
            self.assertNotIn(reviews.CASES['http-drift'], (drift / 'prompt.txt').read_text())
        self.assertEqual(original, {p: p.read_bytes() for p in original})
