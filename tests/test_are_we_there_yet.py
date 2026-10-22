"""Performance contract and isolated packaging, not behavioral compliance tests."""
import importlib.util
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'skills/are-we-there-yet'
spec = importlib.util.spec_from_file_location('performance_refs', ROOT / 'scripts/reference_tools.py')
refs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refs)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}


class PerformanceStructure(unittest.TestCase):
    def test_focused_fixtures_install_only_performance_skill(self):
        sys.path.insert(0, str(ROOT / 'evals'))
        try:
            import performance
            with tempfile.TemporaryDirectory() as folder:
                for agent in ('codex', 'claude'):
                    for case in performance.CASES:
                        project = performance.prepare(Path(folder) / (agent + '-' + case), agent, case)
                        base = project / ('.agents/skills' if agent == 'codex' else '.claude/skills')
                        self.assertEqual([p.name for p in base.iterdir()], [SOURCE.name])
                        self.assertEqual(snapshot(base / SOURCE.name), snapshot(SOURCE))
                        self.assertEqual((project / 'prompt.txt').read_text(encoding='utf-8').strip(), performance.CASES[case])
        finally:
            sys.path.pop(0)

    def test_contract_and_g3_guardrails_present(self):
        entry = (SOURCE / 'SKILL.md').read_text(encoding='utf-8')
        template = (SOURCE / 'references/performance-report.md').read_text(encoding='utf-8')
        self.assertTrue(entry.startswith('---\nname: are-we-there-yet\ndescription: |\n'))
        description = entry.split('---', 2)[1]
        for phrase in ('Use when:', 'this feels slow', 'Do not use when:',
                       'incorrect behavior without a performance symptom'):
            self.assertIn(phrase, description)
        # Omission checks only: these do not establish routing or gate behavior.
        text = ' '.join(entry.split())
        for phrase in ('G3: baseline before diagnosis', 'only escape condition',
                       'establishing one is the immediate task', 'partial report',
                       'one performance intervention at a time', 'non-comparable',
                       'remains unverified', 'G6/G7', 'no escape',
                       'Read `references/performance-report.md`',
                       'No sibling skill or shared reference bundle is required'):
            self.assertIn(phrase, text)
        for field in ('Objective and symptom', 'Workload and reproduction',
                      'Baseline conditions, method and results',
                      'Bottleneck evidence and ranked hypotheses',
                      'Interventions and status', 'Before/after comparison and variance',
                      'Differences from production', 'Verification, uncertainty and gaps',
                      'Relevant handoffs and next measurement'):
            self.assertIn('## ' + field, template)
        for document in (entry, template):
            for phrase in ('`inferred`', '`assumed`', '`unknown`', 'Upstream:',
                           'Re-derived:', 'select-your-battles',
                           'but-it-works-on-my-machine', 'read-the-contract'):
                self.assertIn(phrase, document)

    def test_isolated_installation_paths_and_reference_policy(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {Path('SKILL.md'), Path('references/performance-report.md')})
        with tempfile.TemporaryDirectory() as folder:
            for host in ('.agents', '.claude'):
                root = Path(folder) / host
                installed = root / 'skills' / SOURCE.name
                shutil.copytree(SOURCE, installed)
                self.assertEqual(snapshot(installed), original)
                self.assertEqual(list((root / 'skills').iterdir()), [installed])
                links = []
                for document in installed.rglob('*.md'):
                    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', document.read_text(encoding='utf-8')):
                        resolved = (document.parent / target).resolve()
                        self.assertTrue(resolved.is_relative_to(installed.resolve()))
                        self.assertTrue(resolved.is_file())
                        links.append(resolved)
                self.assertIn((installed / 'references/performance-report.md').resolve(), links)
                shutil.copytree(ROOT / 'shared', root / 'shared')
                before = snapshot(root)
                for options in ({}, {'check': True}, {'update': True}):
                    self.assertEqual(refs.reference_plan(root, **options), ([], 1))
                    self.assertEqual(snapshot(root), before)
                for name in refs.SHARED:
                    unexpected = installed / 'references' / name
                    unexpected.write_bytes((root / 'shared/references' / name).read_bytes())
                    with self.assertRaisesRegex(ValueError, 'Unexpected shared reference'):
                        refs.reference_plan(root, check=True)
                    unexpected.unlink()
        self.assertEqual(snapshot(SOURCE), original)


if __name__ == '__main__':
    unittest.main()
