"""Packaging and installer tests, not agent-behavior evaluations."""

import importlib.machinery
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import reference_tools as refs

loader = importlib.machinery.SourceFileLoader("installer", str(ROOT / "scripts/install-baseline"))
spec = importlib.util.spec_from_loader(loader.name, loader)
installer = importlib.util.module_from_spec(spec)
loader.exec_module(installer)


class FoundationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill-issues-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        canonical = self.root / "shared/references"
        canonical.mkdir(parents=True)
        for name in refs.SHARED:
            (canonical / name).write_bytes((ROOT / "shared/references" / name).read_bytes())

    def skill(self, name):
        folder = self.root / "skills" / name
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text("Fixture only; not an implemented skill.\n", encoding="utf-8")
        return folder

    def run_script(self, name, *args):
        # Different working directory proves scripts do not depend on the caller's cwd.
        return subprocess.run([sys.executable, str(ROOT / "scripts" / name), *map(str, args)],
                              cwd=self.root, capture_output=True, text=True, encoding="utf-8")

    def sync(self, *args):
        return self.run_script("sync-references", "--root", self.root, *args)

    def check(self):
        return self.run_script("check-references", "--root", self.root)

    def snapshot(self):
        return {str(p.relative_to(self.root)): (p.read_bytes(), p.stat().st_mtime_ns)
                for p in self.root.rglob("*") if p.is_file()}

    def test_baseline_extracted_within_cap(self):
        raw = (ROOT / "SPEC.md").read_bytes()
        baseline = raw.split(b"## 4. Shared baseline", 1)[1].split(b"```markdown\n", 1)[1].split(b"```", 1)[0]
        self.assertEqual((ROOT / "BASELINE.md").read_bytes(), baseline)
        self.assertLessEqual(len(baseline.splitlines()), 40)

    def test_scope_and_completion_requirements(self):
        baseline = (ROOT / "BASELINE.md").read_text(encoding="utf-8")
        for requirement in (
            "## Scope and completion", "Change only what the task requires",
            "No unrelated cleanup, formatting, or refactoring",
            "only after checking nothing else uses it", "Leave pre-existing issues alone",
            "report consequential correctness, security, or data-loss issues separately",
            "multi-step work or any stakes trigger", "observable success criteria first",
            "pair each step with a verification method", "one-line done-when",
            "does not activate additional skills or change their boundaries",
            "execute relevant checks where possible",
            "Code inspection alone does not establish runtime correctness",
            "Report failed, blocked, and unrun checks",
            "without naming supporting evidence or a check",
            "mark unsupported conclusions `assumed` or `unknown`",
            "Upstream artifacts are claims, not proof",
            "Artifacts with a shared origin count as one source",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, baseline)

    def test_reference_source_sections_preserved(self):
        source = (ROOT / "SPEC.md").read_text(encoding="utf-8")
        for heading, name in (("6. Interface Check", refs.SHARED[0]),
                              ("7. Authority and authorization", refs.SHARED[1])):
            section = source.split("## " + heading + "\n", 1)[1].split("\n---\n", 1)[0].strip()
            self.assertIn(section, (ROOT / "shared/references" / name).read_text(encoding="utf-8"))

    def test_loading_map_matches_spec(self):
        source = (ROOT / "SPEC.md").read_text(encoding="utf-8")
        table = source.split("**Loading map**", 1)[1].split("All other skills", 1)[0]
        expected = {}
        for line in table.splitlines():
            cells = [cell.strip() for cell in line.split("|")]
            if len(cells) == 5 and cells[1] not in ("Skill", "---"):
                expected[cells[1]] = tuple(name.strip() + ".md" for name in cells[2].split(","))
        self.assertEqual(refs.LOADING_MAP, expected)

    def test_sync_selection_and_idempotence(self):
        for name in (*refs.LOADING_MAP, "prove-it"):
            folder = self.skill(name)
            (folder / "references").mkdir()
            (folder / "references/template.md").write_bytes(b"private template\r\n")
        self.assertEqual(self.sync().returncode, 0)
        for folder in (self.root / "skills").iterdir():
            actual = {p.name for p in (folder / "references").iterdir()}
            self.assertEqual(actual, set(refs.LOADING_MAP.get(folder.name, ())) | {"template.md"})
            self.assertEqual((folder / "references/template.md").read_bytes(), b"private template\r\n")
        before = self.snapshot()
        self.assertEqual(self.sync().returncode, 0)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.check().returncode, 0)
        self.assertEqual(self.snapshot(), before)

    def test_drift_fails_without_partial_writes(self):
        folder = self.skill("trust-issues")
        self.assertEqual(self.sync().returncode, 0)
        divergent = folder / "references/authorization.md"
        divergent.write_bytes(b"deliberately modified bundle\n")
        missing = folder / "references/interface-check.md"
        missing.unlink()
        before = self.snapshot()
        for result in (self.check(), self.sync()):
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("Divergent", result.stderr)
            self.assertEqual(self.snapshot(), before)
        self.assertFalse(missing.exists())
        result = self.sync("--update")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.check().returncode, 0)

    def test_reviewed_canonical_update(self):
        self.skill("think-before-you-commit")
        self.assertEqual(self.sync().returncode, 0)
        path = self.root / "shared/references/interface-check.md"
        path.write_bytes(path.read_bytes() + b"\nReviewed canonical update fixture.\n")
        self.assertEqual(self.sync().returncode, 1)
        self.assertEqual(self.sync("--update").returncode, 0)
        self.assertEqual(self.check().returncode, 0)

    def test_missing_and_unexpected_references(self):
        folder = self.skill("prove-it")
        (folder / "references").mkdir()
        unexpected = folder / "references/authorization.md"
        unexpected.write_bytes(b"unexpected")
        self.skill("read-the-contract")
        before = self.snapshot()
        self.assertIn("Missing", self.check().stderr)
        for args in ((), ("--update",)):
            result = self.sync(*args)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Unexpected", result.stderr)
            self.assertEqual(self.snapshot(), before)

    def test_orphan_bundle_rejected(self):
        folder = self.root / "skills/orphan/references"
        folder.mkdir(parents=True)
        (folder / "interface-check.md").write_bytes(b"orphan")
        self.assertEqual(self.check().returncode, 1)

    def test_missing_canonical_prevents_writes(self):
        self.skill("trust-issues")
        (self.root / "shared/references/authorization.md").unlink()
        before = self.snapshot()
        self.assertEqual(self.sync().returncode, 1)
        self.assertEqual(self.snapshot(), before)

    def test_empty_repository_is_explicit(self):
        result = self.check()
        self.assertEqual(result.returncode, 0)
        self.assertIn("vacuous", result.stdout)

    def test_each_agent_installs_independently(self):
        for agent, filename in installer.TARGETS.items():
            with self.subTest(agent=agent):
                project = self.root / agent
                project.mkdir()
                result = self.run_script("install-baseline", "--agent", agent, "--project", project)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertFalse((project / filename).exists())
                result = self.run_script("install-baseline", "--agent", agent, "--project", project, "--apply")
                self.assertEqual(result.returncode, 0, result.stderr)
                path = project / filename
                self.assertIn((ROOT / "BASELINE.md").read_bytes(), path.read_bytes())
                self.assertEqual({p.name for p in project.iterdir()}, {filename})
                before = self.snapshot()
                result = self.run_script("install-baseline", "--agent", agent, "--project", project, "--apply")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(self.snapshot(), before)

    def test_each_agent_preserves_user_content_and_refuses_conflicts(self):
        original = b"\xef\xbb\xbf# Project rules\r\nKeep these bytes, including no final newline."
        suffix = b"\r\n# More user rules\r\n"
        for agent, filename in installer.TARGETS.items():
            with self.subTest(agent=agent):
                project = self.root / agent
                project.mkdir()
                path = project / filename
                path.write_bytes(original)
                args = ("--agent", agent, "--project", project, "--apply")
                self.assertEqual(self.run_script("install-baseline", *args).returncode, 0)
                self.assertTrue(path.read_bytes().startswith(original))
                path.write_bytes(path.read_bytes() + suffix)
                before = path.read_bytes()
                self.assertEqual(self.run_script("install-baseline", *args).returncode, 0)
                self.assertEqual(path.read_bytes(), before)
                path.write_bytes(before.replace(b"## Authority", b"## Edited authority"))
                conflict = path.read_bytes()
                result = self.run_script("install-baseline", *args)
                self.assertEqual(result.returncode, 1)
                self.assertIn("Conflicting managed block", result.stderr)
                self.assertEqual(path.read_bytes(), conflict)

    def test_malformed_markers_refused_for_each_agent(self):
        baseline = (ROOT / "BASELINE.md").read_bytes()
        valid = installer.proposed_content(b"", baseline)
        cases = (installer.PREFIX, valid + valid,
                 valid.replace(b":start", b":begin"),
                 valid.replace(installer.END, b""), valid.replace(b"\n", b"\r\n"),
                 b"text" + valid, installer.END + valid)
        for agent, filename in installer.TARGETS.items():
            project = self.root / agent
            project.mkdir()
            for data in cases:
                with self.subTest(agent=agent, data=data[:60]):
                    path = project / filename
                    path.write_bytes(data)
                    result = self.run_script("install-baseline", "--agent", agent,
                                             "--project", project, "--apply")
                    self.assertEqual(result.returncode, 1)
                    self.assertEqual(path.read_bytes(), data)

    def test_intact_old_baseline_can_update_preserving_surroundings(self):
        old = installer.proposed_content(b"User prefix\r\n", b"Old baseline\n") + b"User suffix"
        new = installer.proposed_content(old, b"New baseline\n")
        self.assertTrue(new.startswith(b"User prefix\r\n"))
        self.assertTrue(new.endswith(b"User suffix"))
        self.assertNotIn(b"Old baseline", new)
        self.assertIn(b"New baseline", new)

    def test_shadowing_instruction_files_refused(self):
        for agent, conflict in (("codex", "AGENTS.override.md"), ("claude", ".claude/CLAUDE.md")):
            project = self.root / agent
            path = project / conflict
            path.parent.mkdir(parents=True)
            path.write_bytes(b"user-owned instructions")
            before = self.snapshot()
            result = self.run_script("install-baseline", "--agent", agent, "--project", project, "--apply")
            self.assertEqual(result.returncode, 1)
            self.assertEqual(self.snapshot(), before)


if __name__ == "__main__":
    unittest.main()
