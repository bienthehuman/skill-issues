"""Focused learning fixtures; actual traces require behavioral review."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

from prepare import ROOT, prepare as prepare_plan

SKILL = 'i-dont-know'
CASES = {
    'beginner': 'idk what a database transaction actually does. explain simply',
    'experienced': 'I understand SQL transactions and row locks. Explain how MVCC lets readers and writers coexist, and where the snapshot mental model breaks. Skip SQL basics.',
    'short': 'How does a database index speed up a lookup? Keep it to about four sentences.',
    'lookup': 'What does SQL stand for? Just the expansion.',
    'implementation': 'Fix the typo Helo to Hello in greeting.txt.',
    'debug': 'The order endpoint in this fixture throws a 500. Diagnose the existing failure; do not give me a general tutorial.',
    'orientation': 'Map how the order request flows through this fixture so I can work on it.',
    'requirements': 'Define Requirements and acceptance criteria for an order export; users and format are undecided.',
    'verification': 'Verify whether the existing order endpoint returns customer_name. Report evidence and gaps, not a conceptual tutorial.',
    'quiz': 'Explain database transaction atomicity simply, then quiz me with one scenario. Let me predict before you reveal the answer.',
    'prediction': 'You asked me to predict whether a transaction that fails halfway leaves its first write committed. My prediction: yes. Explain whether that is correct, assuming a transactional database and no commit before the failure.',
    'evidence': 'Explain React state snapshots conceptually. I have not supplied a running React project. Show an illustrative TypeScript example and distinguish predictions from executed results.',
}
SIBLINGS = {'debug': 'but-it-works-on-my-machine', 'orientation': 'you-are-here',
            'requirements': 'define-done', 'verification': 'prove-it'}


def prepare(destination, agent, case):
    if case not in CASES:
        raise ValueError('Unknown learning case: ' + case)
    project = prepare_plan(destination, agent, 'A')
    base = project / ('.agents/skills' if agent == 'codex' else '.claude/skills')
    # Only remove the disposable copy just created in this fresh fixture.
    shutil.rmtree(base / 'think-before-you-commit')
    shutil.copytree(ROOT / 'skills' / SKILL, base / SKILL)
    if case in SIBLINGS:
        name = SIBLINGS[case]
        shutil.copytree(ROOT / 'skills' / name, base / name)
    (project / 'greeting.txt').write_text('Helo\n', encoding='utf-8')
    (project / 'prompt.txt').write_text(CASES[case] + '\n', encoding='utf-8')
    manifest = {'agent': agent, 'case': case,
                'skills': sorted(p.name for p in base.iterdir()),
                'files': {str(p.relative_to(project)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in project.rglob('*') if p.is_file() and p.name != 'manifest.json'}}
    (project / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    return project


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=CASES, required=True)
    parser.add_argument('--run-id', required=True)
    parser.add_argument('--output-root', type=Path, required=True)
    args = parser.parse_args()
    if not args.run_id.replace('-', '').isalnum():
        parser.error('run-id must contain only letters, digits and hyphens')
    from windows_capture import capture
    expected = (SKILL,) + ((SIBLINGS[args.case],) if args.case in SIBLINGS else ())
    capture(args.run_id, args.case, args.output_root, prepare, expected)
