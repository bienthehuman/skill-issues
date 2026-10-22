"""Focused standalone performance captures; review traces, not just exit codes."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

from prepare import prepare as prepare_plan, ROOT

CASES = {
    'subjective': 'This endpoint feels slow. I think adding an index will fix it. Investigate and tell me the cause.',
    'negative': 'The order endpoint returns the wrong customer name. There is no slowness or performance complaint. Diagnose the correctness issue only.',
    'proposal': 'Use $are-we-there-yet. Review NOTES.md and report whether performance improved. Do not implement changes.',
    'different-conditions': 'Use $are-we-there-yet. Review NOTES.md and assess the claimed speedup. Do not implement changes.',
}


def prepare(destination, agent, case):
    if case not in CASES:
        raise ValueError('Unknown performance case: ' + case)
    project = prepare_plan(destination, agent, 'A')
    base = project / ('.agents/skills' if agent == 'codex' else '.claude/skills')
    # Only the disposable skill installed by prepare_plan is removed.
    shutil.rmtree(base / 'think-before-you-commit')
    shutil.copytree(ROOT / 'skills/are-we-there-yet', base / 'are-we-there-yet')
    notes = 'Static inspection fixture; no executable application, database or production access. No timings, query plans or profiling captures are available.\n'
    if case == 'proposal':
        notes += 'An upstream proposal says adding an index should make it 80% faster. No index was implemented and no before/after benchmark was run.\n'
    if case == 'different-conditions':
        notes += ('Supplied benchmark notes: baseline revision A, local single worker, cold cache, 10000 records, three runs 900/1000/1100 ms; after revision B adds caching, same machine, warm cache, 100 records, three runs 9/10/11 ms. Method: elapsed endpoint time. Commands and input generators were not retained. Production workload and cache state are unknown. Author claims a verified 100x production improvement.\n')
    (project / 'NOTES.md').write_text(notes, encoding='utf-8')
    (project / 'prompt.txt').write_text(CASES[case] + '\n', encoding='utf-8')
    manifest = {'agent': agent, 'case': case, 'skills': ['are-we-there-yet'],
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
    capture(args.run_id, args.case, args.output_root, prepare, ('are-we-there-yet',))
