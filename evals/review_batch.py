"""Capture remaining first runs without replacing any existing evidence."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import subprocess
import sys

from reviews import CASES, ROOT


def run(case):
    run_id = 'review-' + case + '-first'
    output = ROOT / 'evals/review-runs' / run_id
    if output.exists():
        return case, 'preserved existing run'
    result = subprocess.run([sys.executable, str(ROOT / 'evals/reviews.py'),
                             '--case', case, '--run-id', run_id], capture_output=True)
    # Preserve launcher failures too, independently of agent trace availability.
    output.mkdir(parents=True, exist_ok=True)
    (output / 'launcher.stdout.txt').write_bytes(result.stdout)
    (output / 'launcher.stderr.txt').write_bytes(result.stderr)
    return case, result.returncode


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executor:
        for future in as_completed([executor.submit(run, case) for case in CASES]):
            print(future.result(), flush=True)
