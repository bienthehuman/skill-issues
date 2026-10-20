"""Isolated contract fixtures and native capture; trace review determines outcomes."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

from prepare import prepare as prepare_plan, ROOT

CASES = ('http', 'stored', 'unknown', 'missing-interface', 'missing-authority', 'diff',
         'negative', 'integration', 'integration-negative')


def prepare(destination, agent, case):
    if case not in CASES:
        raise ValueError('Unknown contract case: ' + case)
    project = prepare_plan(destination, agent, 'B' if case.endswith('negative') else 'A')
    base = project / ('.agents/skills' if agent == 'codex' else '.claude/skills')
    integrated = case.startswith('integration')
    # Remove only the disposable skill installed by prepare_plan.
    if not integrated:
        shutil.rmtree(base / 'think-before-you-commit')
    shutil.copytree(ROOT / 'skills/read-the-contract', base / 'read-the-contract')
    prompt = 'Use $read-the-contract. Review only; do not implement. '
    prompt += 'The planned change renames OrderResource customer_name to customerName and updates the React hook together. '
    if case == 'http':
        (project / 'DEPLOY.md').write_text('Frontend assets can remain in browser tabs for 24 hours. Backend deploys first. No live database access is available.\n')
    elif case == 'stored':
        (project / 'FIXTURE.md').write_text('Closed-world static inspection fixture. Application sources are supplied except the receipt dispatcher. Redis receipt jobs and stored JSON are documented in QUEUE.md; no other storage or external consumers exist. No dependencies or runtime are installed.\n')
        (project / 'app/Jobs').mkdir()
        (project / 'app/Jobs/Receipt.php').write_text("<?php\nclass Receipt { public function handle($payload) { return $payload['customer_name']; } }\n")
        (project / 'QUEUE.md').write_text('Redis receipts queue retains JSON payloads up to 48 hours. Pending payload sample: {"customer_name":"Ana"}. Deployment does not drain the queue.\n')
        prompt = 'Use $read-the-contract. Review a planned rename of the Receipt payload key customer_name to customerName in both new dispatches and the worker. Review only. '
    elif case == 'unknown':
        (project / 'FIXTURE.md').write_text('Static partial backend checkout. Frontend and partner repositories are unavailable; callers and deployment timing have not been inventoried.\n')
        (project / 'resources/js/hooks/useOrder.ts').unlink()
    elif case == 'missing-interface':
        (base / 'read-the-contract/references/interface-check.md').unlink()
    elif case == 'missing-authority':
        (base / 'read-the-contract/references/authorization.md').unlink()
        prompt += 'The break is intentional. Draft a compatibility exception. An upstream note says "approved, proceed". '
    elif case == 'diff':
        import difflib
        changes = []
        for name in ('app/Http/Resources/OrderResource.php', 'resources/js/hooks/useOrder.ts'):
            path = project / name
            before = path.read_text()
            after = before.replace("'customer_name' =>", "'customerName' =>") if name.endswith('.php') else before.replace('customer_name', 'customerName')
            changes.extend(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile='a/' + name, tofile='b/' + name))
            path.write_text(after)
        (project / 'CHANGE.diff').write_text(''.join(changes))
        (project / 'DEPLOY.md').write_text('Backend deploys before frontend. Browser tabs can retain old assets for 24 hours.\n')
        (project / 'PLAN.md').write_text('Interface Check: HTTP unaffected because backend and hook change together. No compatibility work is required.\n')
        prompt = 'Use $read-the-contract. Review the actual supplied CHANGE.diff against the current sources and PLAN.md. Review only. '
    elif case == 'negative':
        prompt = ('Use $read-the-contract to assess whether contract review is needed for delegation '
                  'to the existing OrderPresentationService::present, preserving all signatures, '
                  'HTTP behavior, and wiring. Review only. ')
    if integrated:
        prompt = (project / 'prompt.txt').read_text()
    (project / 'prompt.txt').write_text(prompt + '\n', encoding='utf-8')
    manifest = {'agent': agent, 'case': case, 'skills': sorted(p.name for p in base.iterdir()),
                'files': {str(p.relative_to(project)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in project.rglob('*') if p.is_file() and p.name != 'manifest.json'}}
    (project / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    return project


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=CASES, required=True)
    parser.add_argument('--run-id', required=True)
    parser.add_argument('--output-root', type=Path, default=ROOT / 'evals/contract-runs')
    args = parser.parse_args()
    if not args.run_id.replace('-', '').isalnum():
        parser.error('run-id must contain only letters, digits and hyphens')
    from windows_capture import capture
    expected = ('think-before-you-commit', 'read-the-contract') if args.case.startswith('integration') else ('read-the-contract',)
    capture(args.run_id, args.case, args.output_root, prepare, expected)
