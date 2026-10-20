"""Archive completed fixtures and index trace evidence; never assign behavioral passes."""
import json
from pathlib import Path
import shutil

from reviews import ROOT


def audit():
    summaries = []
    for output in sorted((ROOT / 'evals/review-runs').iterdir()):
        run = output / 'run.json'
        if not run.exists():
            continue
        metadata = json.loads(run.read_text(encoding='utf-8'))
        if 'exit_code' not in metadata:
            continue
        source = Path(metadata['cwd'])
        archived = output / 'fixture'
        if not archived.exists():
            shutil.copytree(source, archived)
        reads = []
        for number, line in enumerate((output / 'trace.jsonl').read_text(encoding='utf-8').splitlines(), 1):
            event = json.loads(line)
            item = event.get('item', {})
            if item.get('type') == 'command_execution' and event.get('type') == 'item.completed':
                command = item.get('command', '')
                if any(name in command for name in ('interface-check.md', 'authorization.md', 'SKILL.md', 'findings.md')):
                    reads.append({'line': number, 'command': command, 'exit_code': item.get('exit_code'),
                                  'output_present': bool(item.get('aggregated_output'))})
        summary = {key: metadata.get(key) for key in ('run_id', 'case', 'version', 'exit_code',
                    'single_skill_inventory', 'global_instructions_present', 'fixture_unchanged',
                    'canonical_unchanged', 'model_requested', 'reasoning_effort_requested', 'human_prompts')}
        summary['reference_events'] = reads
        summaries.append(summary)
    (ROOT / 'evals/review-runs/evidence-index.json').write_text(json.dumps(summaries, indent=2), encoding='utf-8')
    print(json.dumps([{k: v for k, v in s.items() if k != 'reference_events'} for s in summaries], indent=2))


if __name__ == '__main__':
    audit()
