"""Structural packaging and fixture checks, not behavioral safety assertions."""
import importlib.util
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
import rollouts

spec = importlib.util.spec_from_file_location('rollout_references', ROOT / 'scripts/reference_tools.py')
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)
SOURCE = ROOT / 'skills/famous-last-words'


class RolloutStructure(unittest.TestCase):
    def test_standalone_links_and_bundle(self):
        for host in ('.agents', '.claude'):
            with tempfile.TemporaryDirectory() as folder:
                installed = Path(folder) / host / 'skills/famous-last-words'
                shutil.copytree(SOURCE, installed)
                self.assertEqual({str(p.relative_to(installed)).replace('\\', '/')
                                  for p in installed.rglob('*') if p.is_file()},
                                 {'SKILL.md', 'references/authorization.md', 'references/rollout-plan.md'})
                self.assertEqual((installed / 'references/authorization.md').read_bytes(),
                                 (ROOT / 'shared/references/authorization.md').read_bytes())
                for document in installed.rglob('*.md'):
                    for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)', document.read_text(encoding='utf-8')):
                        target = (document.parent / link).resolve()
                        self.assertTrue(target.is_relative_to(installed.resolve()))
                        self.assertTrue(target.is_file())

    def test_sync_drift_missing_and_private_template(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / 'shared', root / 'shared')
            installed = root / 'skills/famous-last-words'
            shutil.copytree(SOURCE, installed)
            template = (installed / 'references/rollout-plan.md').read_bytes()
            self.assertEqual(references.reference_plan(root, check=True), ([], 1))
            bundle = installed / 'references/authorization.md'
            bundle.unlink()
            with self.assertRaisesRegex(ValueError, 'Missing bundled reference'):
                references.reference_plan(root, check=True)
            changes, count = references.reference_plan(root)
            self.assertEqual(count, 1)
            for path, data in changes:
                references.atomic_write(path, data)
            bundle.write_text('fixture drift', encoding='utf-8')
            for options in ({}, {'check': True}):
                with self.assertRaisesRegex(ValueError, 'Divergent bundled reference'):
                    references.reference_plan(root, **options)
            self.assertEqual((installed / 'references/rollout-plan.md').read_bytes(), template)

    def test_required_structure_and_authority_read_order(self):
        entry = (SOURCE / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(entry.startswith('---\nname: famous-last-words\ndescription: |\n'))
        for phrase in ('Use when:', 'Do not use when:', 'Lens:', 'Upstream:', 'Re-derived:',
                       'G6', 'G7', 'no escape', 'previous-session', 'single-use',
                       'Without an Impact Report', 'upper-bound estimate'):
            self.assertIn(phrase, entry)
        self.assertLess(entry.index('Before identifying or evaluating Restricted steps, read'),
                        entry.index('Now list Restricted steps'))
        template = (SOURCE / 'references/rollout-plan.md').read_text(encoding='utf-8')
        self.assertEqual(len(re.findall(r'^## ', template, re.M)), 10)
        for field in ('Deployment sequence and compatibility window', 'Migration ordering',
                      'Existing data and serialized state', 'Blast radius', 'Detection and rollback triggers',
                      'Rollback procedure', 'One-way steps', 'Restricted steps', 'Verification, readiness'):
            self.assertIn('## ' + field, template)

    def test_all_fixtures_and_neighbor_inventory(self):
        for agent in ('codex', 'claude'):
            for case in rollouts.CASES:
                with self.subTest(agent=agent, case=case), tempfile.TemporaryDirectory() as folder:
                    project = rollouts.prepare(Path(folder) / 'new', agent, case)
                    host = '.agents' if agent == 'codex' else '.claude'
                    self.assertEqual({p.name for p in (project / host / 'skills').iterdir()},
                                     {'famous-last-words', *rollouts.NEIGHBORS})
                    reference = project / host / 'skills/famous-last-words/references/authorization.md'
                    self.assertEqual(reference.exists(), case != 'missing-authority')
                    self.assertNotIn(rollouts.CASES[case][1], (project / 'prompt.txt').read_text())
                    if case == 'migration':
                        self.assertIn('No API or queue payload key changes',
                                      (project / 'PLAN.md').read_text())
                        self.assertIn('amount_minor', (project / 'migration.sql').read_text())
                    if case == 'queued':
                        self.assertIn('only the receipt payload key',
                                      (project / 'PLAN.md').read_text())
                    with self.assertRaises(FileExistsError):
                        rollouts.prepare(project, agent, case)


if __name__ == '__main__':
    unittest.main()
