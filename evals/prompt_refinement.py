"""Focused Prompt Refinement fixtures; trace review determines behavioral results."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

from prepare import prepare as prepare_plan, ROOT

SKILL = 'garbage-in-garbage-out'
CASES = {
    'clear': 'Refine this prompt: "Translate Hello into Spanish. Return only the translation."',
    'low-risk': 'make this prompt better: "Write a short friendly reminder to my book club to bring their books. Use our usual language."',
    'consequential': 'Strengthen this prompt: "Clean up duplicate customer records in our shared database." Keep it limited to duplicates; do not add unrelated maintenance.',
    'code': 'Deepen this prompt using the available fixture: "Rename customer_name to customerName in the order response and its React consumer. Preserve status codes, validation and error semantics. No dependencies, schema changes or other features."',
    'research': 'Make this research prompt more rigorous: "Using the original study supplied in NOTES.md, assess whether the evidence supports the claimed improvement. Do not generalize beyond the measured population or invent missing measurements."',
    'trivial': 'fix the typo Helo to Hello in greeting.txt',
    'requirements': 'help me define what an order export must do and write Requirements with acceptance criteria. The format and users are undecided.',
    'planning': 'Use $think-before-you-commit. The approach is settled: rename customer_name to customerName in the order API and update its React consumer. Produce an Implementation Plan only.',
    'discussion': 'Why can duplicate records make analysis misleading? Explain briefly.',
}


def prepare(destination, agent, case):
    if case not in CASES:
        raise ValueError('Unknown refinement case: ' + case)
    project = prepare_plan(destination, agent, 'A')
    base = project / ('.agents/skills' if agent == 'codex' else '.claude/skills')
    # Remove only the disposable copy created by prepare_plan in this fresh fixture.
    shutil.rmtree(base / 'think-before-you-commit')
    shutil.copytree(ROOT / 'skills' / SKILL, base / SKILL)
    # Routing controls include the actual alternative so absence cannot mask routing.
    sibling = {'requirements': 'define-done', 'planning': 'think-before-you-commit'}.get(case)
    if sibling:
        shutil.copytree(ROOT / 'skills' / sibling, base / sibling)
    (project / 'greeting.txt').write_text('Helo\n', encoding='utf-8')
    notes = 'No additional task context is supplied. This fixture has no database or executable application.\n'
    if case == 'research':
        notes = ('Original study and raw measurements were not supplied. An author summary claims a 40% improvement in 12 volunteers; allocation, outcomes, controls and uncertainty were not reported. This is a summary, not the original study.\n')
    (project / 'NOTES.md').write_text(notes, encoding='utf-8')
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
    expected = (SKILL,)
    sibling = {'requirements': 'define-done', 'planning': 'think-before-you-commit'}.get(args.case)
    if sibling:
        expected += (sibling,)
    capture(args.run_id, args.case, args.output_root, prepare, expected)
