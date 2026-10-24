"""Native Windows Codex evaluation capture. Human trace review determines pass/fail."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import tomllib

from prepare import prepare

ROOT = Path(__file__).resolve().parents[1]
CODEX = shutil.which('codex')


def hashes(folder):
    return {str(p.relative_to(folder)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts}


def capture(run_id, case, output_root, prepare_run=prepare,
            expected_skills=('think-before-you-commit',), baseline_path=None,
            sandbox='read-only', model=None, reasoning_effort=None,
            evaluation_scope=None, followups=(), before_followup=None):
    baseline_path = Path(baseline_path) if baseline_path is not None else ROOT / 'BASELINE.md'
    output = output_root.resolve() / run_id
    output.mkdir(parents=True, exist_ok=False)
    project = Path(tempfile.gettempdir()) / 'skill-issues-m1-windows-20261020' / run_id
    prepare_run(project, 'codex', case)
    # Suppress project discovery, then inject precisely the canonical baseline.
    # Global AGENTS.md survives this CLI setting; retain this isolation limitation.
    # The fixture still contains its independently installed AGENTS.md for audit.
    instructions = baseline_path.read_text(encoding='utf-8')
    if evaluation_scope is not None:
        instructions += '\n\nEvaluation access boundary (not a baseline rule):\n' + evaluation_scope
    config = ['windows.sandbox="elevated"', 'project_doc_max_bytes=0',
              'developer_instructions=' + json.dumps(instructions),
              'tool_output_token_limit=20000', 'web_search="disabled"']
    if reasoning_effort is not None:
        config.append('model_reasoning_effort=' + json.dumps(reasoning_effort))
    user_config = Path.home() / '.codex/config.toml'
    cfg = tomllib.loads(user_config.read_text(encoding='utf-8')) if user_config.exists() else {}
    for name in cfg.get('mcp_servers', {}):
        config.append('mcp_servers.' + json.dumps(name) + '.enabled=false')
        config.append('mcp_servers.' + json.dumps(name) + '.command=' + json.dumps('cmd.exe'))
    for name in cfg.get('plugins', {}):
        config.append('plugins.' + json.dumps(name) + '.enabled=false')
    disabled = []
    for base in (Path.home() / '.codex/skills', Path.home() / '.agents/skills',
                 Path.home() / '.codex/plugins/cache'):
        if base.exists():
            disabled.extend(sorted({p.as_posix() for p in base.rglob('SKILL.md')}))
    config.append('skills.config=[' + ','.join('{path=' + json.dumps(p) + ',enabled=false}' for p in disabled) + ']')
    common = [CODEX, '--enable', 'skip_host_skill_discovery', '--disable', 'plugins', '-a', 'never', '-s', sandbox, '-C', str(project)]
    if model is not None:
        common.extend(['--model', model])
    for value in config:
        common.extend(['-c', value])
    prompt = (project / 'prompt.txt').read_text(encoding='utf-8')
    before = hashes(project)
    canonical = {name: hashes(ROOT / name) for name in ('skills', 'shared')}
    canonical.update({name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                      for name in ('SPEC.md', 'BASELINE.md')})
    version = subprocess.check_output([CODEX, '--version'], text=True).strip()
    metadata = {'run_id': run_id, 'case': case, 'agent': 'codex', 'version': version,
                'cwd': str(project), 'sandbox': sandbox, 'windows_backend': 'elevated',
                'model_requested': model, 'reasoning_effort_requested': reasoning_effort,
                'evaluation_scope': evaluation_scope,
                'approval': 'never', 'prompt': prompt, 'disabled_skill_paths': disabled,
                'baseline_delivery': 'developer_instructions; project_doc_max_bytes=0',
                'baseline_path': str(baseline_path.resolve()),
                'baseline_sha256': hashlib.sha256(baseline_path.read_bytes()).hexdigest(),
                'fixture_before': before, 'canonical_before': canonical, 'human_prompts': 0,
                'scripted_followups': list(followups)}
    # Debug uses the same overrides, but lacks exec's ignore-user-config switch.
    # Review this inventory before treating it as evidence of an isolated run.
    audit = common + ['debug', 'prompt-input', prompt]
    metadata['inventory_argv'] = audit
    with (output / 'inventory.json').open('wb') as stdout, (output / 'inventory.stderr.txt').open('wb') as stderr:
        metadata['inventory_exit_code'] = subprocess.run(audit, cwd=project, stdout=stdout, stderr=stderr).returncode
    inventory = json.loads((output / 'inventory.json').read_text(encoding='utf-8-sig')) if metadata['inventory_exit_code'] == 0 else []
    texts = [c.get('text', '') for m in inventory for c in m.get('content', [])]
    catalogs = [t.split('### Available skills', 1)[1] for t in texts if '<skills_instructions>' in t and '### Available skills' in t]
    available = [line for catalog in catalogs for line in catalog.splitlines() if line.startswith('- ')]
    metadata['available_skills'] = available
    metadata['expected_skills'] = list(expected_skills)
    metadata['single_skill_inventory'] = (len(available) == len(expected_skills) and
        all(any(line.startswith('- ' + name + ':') for line in available)
            for name in expected_skills))
    metadata['global_instructions_present'] = any(t.startswith('# AGENTS.md instructions') for t in texts)
    if not metadata['single_skill_inventory']:
        metadata['result'] = 'blocked: expected skill inventory not established'
        (output / 'run.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
        raise RuntimeError(metadata['result'])
    (output / 'manifest.json').write_bytes((project / 'manifest.json').read_bytes())
    (output / 'prompt.txt').write_text(prompt, encoding='utf-8')
    command = common + ['exec', '--ignore-user-config'] + ([] if followups else ['--ephemeral']) + ['--skip-git-repo-check',
                        '--json', '-o', str(output / 'final.md'), '-']
    metadata['argv'] = command
    (output / 'run.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    print('RUNNING ' + run_id + ' in ' + str(project), flush=True)
    with (output / 'trace.jsonl').open('wb') as stdout, (output / 'stderr.txt').open('wb') as stderr:
        result = subprocess.run(command, cwd=project, input=prompt.encode('utf-8'), stdout=stdout, stderr=stderr)
    metadata['exit_code'] = result.returncode
    metadata['turns'] = [{'prompt': prompt, 'exit_code': result.returncode,
                          'trace': 'trace.jsonl', 'final': 'final.md'}]
    if followups and result.returncode == 0:
        events = [json.loads(line) for line in (output / 'trace.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
        session_id = next((event.get('thread_id') for event in events if event.get('type') == 'thread.started'), None)
        if not session_id:
            metadata['continuation_blocked'] = 'No thread.started session ID in trace'
        else:
            metadata['session_id'] = session_id
            for index, followup in enumerate(followups):
                if before_followup is not None:
                    before_followup(project, case, index)
                turn = index + 2
                trace_name, final_name = f'trace-turn{turn}.jsonl', f'final-turn{turn}.md'
                (output / f'prompt-turn{turn}.txt').write_text(followup, encoding='utf-8')
                resume = common + ['exec', 'resume', '--ignore-user-config', '--skip-git-repo-check',
                                   '--json', '-o', str(output / final_name), session_id, '-']
                with (output / trace_name).open('wb') as stdout, (output / f'stderr-turn{turn}.txt').open('wb') as stderr:
                    continuation = subprocess.run(resume, cwd=project, input=followup.encode('utf-8'), stdout=stdout, stderr=stderr)
                metadata['turns'].append({'prompt': followup, 'argv': resume,
                    'exit_code': continuation.returncode, 'trace': trace_name, 'final': final_name,
                    'fixture_after': hashes(project)})
                (output / 'run.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
                if continuation.returncode:
                    metadata['continuation_blocked'] = f'Turn {turn} process exit {continuation.returncode}'
                    break
    metadata['fixture_after'] = hashes(project)
    metadata['fixture_unchanged'] = metadata['fixture_after'] == before
    metadata['canonical_after'] = {name: hashes(ROOT / name) for name in ('skills', 'shared')}
    metadata['canonical_after'].update({name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                                      for name in ('SPEC.md', 'BASELINE.md')})
    metadata['canonical_unchanged'] = metadata['canonical_after'] == canonical
    metadata['result'] = 'not reviewed'
    (output / 'run.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    print('CAPTURED ' + run_id + '; exit=' + str(result.returncode) + '; unchanged=' + str(metadata['fixture_unchanged']), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-id', required=True)
    parser.add_argument('--case', choices=('A', 'B', 'C'), required=True)
    parser.add_argument('--output-root', type=Path, default=ROOT / 'evals/windows-20261020')
    args = parser.parse_args()
    if not args.run_id.replace('-', '').isalnum():
        parser.error('run-id must contain only letters, digits and hyphens')
    capture(args.run_id, args.case, args.output_root)
