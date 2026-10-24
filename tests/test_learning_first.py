"""Static preservation and fixture/capture checks, not agent-behavior results."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
import learning_first as fixtures
import windows_capture as runner


class LearningFirstFixtures(unittest.TestCase):
    def test_existing_baseline_bytes_preserved_outside_approved_amendment(self):
        current = (ROOT / 'BASELINE.md').read_bytes()
        lines = current.splitlines(keepends=True)
        invitation = [line for line in lines if line.startswith(b'- Learning first:')]
        self.assertEqual(len(invitation), 1)
        restored = b''.join(line for line in lines if line not in invitation).replace(
            b'- Answer first, except for the bounded learning-first invitation below.',
            b'- Answer first.', 1)
        # Canonical v0.12 baseline digest: all pre-existing rules remain byte-identical.
        self.assertEqual(hashlib.sha256(restored).hexdigest(),
                         '14a5ea3932440e8a3f0f8686d105f66b4b44e1b91a222387c078cec8234e4739')

    def test_all_cases_both_hosts_manifest_and_delayed_observation(self):
        self.assertEqual(len(fixtures.CASES), 18)
        self.assertEqual({int(key.split('-')[0]) for key in fixtures.CASES}, set(range(1, 19)))
        with tempfile.TemporaryDirectory() as folder:
            for agent in ('codex', 'claude'):
                for case, (prompt, followups) in fixtures.CASES.items():
                    with self.subTest(agent=agent, case=case):
                        project = fixtures.prepare(Path(folder) / (agent + '-' + case), agent, case)
                        manifest = json.loads((project / 'manifest.json').read_text(encoding='utf-8'))
                        self.assertEqual((project / 'prompt.txt').read_text(encoding='utf-8').strip(), prompt)
                        self.assertFalse((project / 'followups.json').exists(), 'Do not leak future user reasoning')
                        for name, digest in manifest['files'].items():
                            self.assertEqual(hashlib.sha256((project / name).read_bytes()).hexdigest(), digest)
                        base = project / ('.agents/skills' if agent == 'codex' else '.claude/skills')
                        actual = {p.name for p in base.iterdir()} if base.exists() else set()
                        self.assertEqual(actual, set(fixtures.SKILLS.get(case, ())))
                        for skill in actual:
                            for source in (ROOT / 'skills' / skill).rglob('*'):
                                if source.is_file():
                                    self.assertEqual((base / skill / source.relative_to(ROOT / 'skills' / skill)).read_bytes(), source.read_bytes())
                        self.assertFalse((project / 'observation.json').exists())
                        if case == '08-contradiction':
                            original = (project / 'HANDOFF.md').read_bytes()
                            fixtures.before_followup(project, case, 0)
                            self.assertEqual((project / 'HANDOFF.md').read_bytes(), original)
                            self.assertEqual(json.loads((project / 'observation.json').read_text())['p95_ms'], 420)
                            with self.assertRaises(ValueError):
                                fixtures.before_followup(project, case, 0)
                        with self.assertRaisesRegex(ValueError, 'must not exist'):
                            fixtures.prepare(project, agent, case)

    def test_canonical_optional_block_matches_private_template(self):
        spec = (ROOT / 'SPEC.md').read_text(encoding='utf-8')
        template = (ROOT / 'skills/previously-on/references/handoff-document.md').read_text(encoding='utf-8')
        block = 'Optional prediction/outcome notes' + template.split('Optional prediction/outcome notes', 1)[1].split('\n## Recorded exceptions', 1)[0]
        self.assertIn(block, spec.split('## Appendix A:', 1)[1])
        rubric = (ROOT / 'evals/learning-first-cases.md').read_text(encoding='utf-8')
        table = rubric[rubric.index('| Case |'):rubric.index('\n\nCase 2/')]
        self.assertIn(table, spec.split('### 11.11 ', 1)[1])

    def test_capture_continues_exact_session_without_ephemeral_and_retains_turns(self):
        # Exercise real orchestration with fake CLI responses; this is not a live run.
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ('skills', 'shared'):
                (root / name).mkdir()
            for name in ('SPEC.md', 'BASELINE.md'):
                (root / name).write_text('fixture\n', encoding='utf-8')
            commands = []

            def run(command, **kwargs):
                commands.append(command)
                if 'debug' in command:
                    kwargs['stdout'].write(b'[]')
                else:
                    kwargs['stdout'].write(b'{"type":"thread.started","thread_id":"fixture-session"}\n')
                    Path(command[command.index('-o') + 1]).write_text('fixture answer', encoding='utf-8')
                return subprocess.CompletedProcess(command, 0)

            with patch.object(runner, 'ROOT', root), patch.object(runner, 'CODEX', 'fixture-codex'), \
                 patch.object(runner.subprocess, 'run', side_effect=run), \
                 patch.object(runner.subprocess, 'check_output', return_value='fixture-version'), \
                 patch.object(runner.tempfile, 'gettempdir', return_value=str(root)):
                # Runner owns its fresh conventional fixture path.
                def prepare_at(destination, agent, case):
                    destination.mkdir(parents=True)
                    (destination / 'prompt.txt').write_text('initial', encoding='utf-8')
                    (destination / 'manifest.json').write_text('{}', encoding='utf-8')
                    return destination
                runner.capture('fresh', 'test', root / 'out', prepare_at, (), followups=('skip',))
            self.assertNotIn('--ephemeral', commands[1])
            self.assertEqual(commands[2][commands[2].index('exec') + 1], 'resume')
            self.assertEqual(commands[2][-2:], ['fixture-session', '-'])
            metadata = json.loads((root / 'out/fresh/run.json').read_text(encoding='utf-8'))
            self.assertEqual([turn['prompt'] for turn in metadata['turns']], ['initial', 'skip'])
            self.assertTrue(metadata['fixture_unchanged'])
            self.assertTrue(metadata['canonical_unchanged'])


if __name__ == '__main__':
    unittest.main()
