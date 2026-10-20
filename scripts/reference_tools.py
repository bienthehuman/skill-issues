"""Reference packaging policy from SPEC section 3.6; no third-party dependencies."""

import argparse
import os
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
SHARED = ("interface-check.md", "authorization.md")
LOADING_MAP = {
    "think-before-you-commit": SHARED,
    "trust-issues": SHARED,
    "read-the-contract": SHARED,
    "same-same-but-different": (SHARED[0],),
    "famous-last-words": (SHARED[1],),
    "previously-on": (SHARED[1],),
}


def local_path(path, root):
    """Do not follow links outside the selected tree, including dangling links."""
    for item in (path, *path.parents):
        if item == root:
            break
        if item.is_symlink():
            raise ValueError(f"Refusing symbolic link: {item}")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes selected tree: {path}")


def atomic_write(path, data):
    """Replace one file atomically; unchanged files are never rewritten."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=".skill-issues-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
        if path.exists():
            os.chmod(name, path.stat().st_mode)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def reference_plan(root, check=False, update=False):
    canonical = {}
    for name in SHARED:
        path = root / "shared" / "references" / name
        local_path(path, root)
        canonical[name] = path.read_bytes()
    changes, errors = [], []
    skills = root / "skills"
    local_path(skills, root)
    count = 0
    for skill in sorted(skills.iterdir()) if skills.exists() else []:
        local_path(skill, root)
        if not skill.is_dir():
            continue
        active = (skill / "SKILL.md").is_file()
        count += int(active)
        expected = LOADING_MAP.get(skill.name, ()) if active else ()
        for name in SHARED:
            path = skill / "references" / name
            local_path(path, root)
            if name not in expected:
                if path.exists():
                    errors.append(f"Unexpected shared reference: {path}")
                continue
            if not path.exists():
                if check:
                    errors.append(f"Missing bundled reference: {path}")
                else:
                    changes.append((path, canonical[name]))
            elif path.read_bytes() != canonical[name]:
                if check or not update:
                    errors.append(f"Divergent bundled reference: {path}")
                else:
                    changes.append((path, canonical[name]))
    if errors:
        raise ValueError("\n".join(errors))
    return changes, count


def main(check=False):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Validate bundled references." if check
                                     else "Bundle canonical references; refuse divergence by default.")
    parser.add_argument("--root", type=Path, default=ROOT,
                        help="repository root (default: script's repository)")
    if not check:
        parser.add_argument("--update", action="store_true",
                            help="explicitly replace divergent copies with reviewed canonical bytes")
    args = parser.parse_args()
    try:
        changes, count = reference_plan(args.root.resolve(), check, getattr(args, "update", False))
        # Complete validation precedes every write. This is not a multi-file filesystem transaction.
        for path, data in changes:
            atomic_write(path, data)
            print(f"Wrote {path}")
        print(f"{'Checked' if check else 'Synchronized'} {count} skill(s); {len(changes)} file(s) changed.")
        if count == 0:
            print("No skills present; bundle validation is vacuous. Use the fixture tests.")
        return 0
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
