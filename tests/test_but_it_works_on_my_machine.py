"""Structural contracts and isolated packaging, not agent-behavior evaluations."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/but-it-works-on-my-machine"
spec = importlib.util.spec_from_file_location(
    "debugging_reference_tools", ROOT / "scripts/reference_tools.py"
)
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class ButItWorksOnMyMachineStructure(unittest.TestCase):
    def test_metadata_and_routing_boundaries(self):
        entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(entry.startswith(
            "---\nname: but-it-works-on-my-machine\ndescription: |\n"))
        description = entry.split("---", 2)[1]
        for phrase in (
            "Use when:", "observed behavior contradicts expected behavior",
            "unexpected error", "regression needs diagnosis", "Do not use when:",
            "new feature", "missing or undefined requirements", "slowness or performance",
            "without an existing failure", "root cause is already established",
            "code in a diff alone is not a trigger",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, description)
        self.assertIn("Lens: Explain a failure that already exists.", entry)

    def test_report_fields_and_evidence_conventions(self):
        template = (SOURCE / "references/root-cause-report.md").read_text(encoding="utf-8")
        headings = set(re.findall(r"^## (.+)$", template, re.MULTILINE))
        self.assertTrue({
            "Symptom and expected behavior", "Environment and reproduction conditions",
            "Reproduction attempts and results", "Ranked hypotheses and discriminating tests",
            "Executed diagnostic checks", "Root-cause conclusion and confirming evidence",
            "Proposed fix, risks, and assumptions", "Regression specification and handoff",
            "Gaps, uncertainty, and next steps",
        }.issubset(headings))
        entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        for document in (entry, template):
            for phrase in ("Upstream:", "Re-derived:", "`inferred`", "`assumed`",
                           "`unknown`", "load-bearing", "proposed", "actual observed result"):
                with self.subTest(phrase=phrase):
                    self.assertIn(phrase, " ".join(document.split()))

    def test_g4_and_reproduction_safeguards_are_explicit(self):
        # Static instruction checks do not demonstrate agent compliance.
        entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        normalized = " ".join(entry.split())
        for phrase in (
            "G4: confirming test before naming root cause",
            "only when the report shows the confirming test and its actual observed result",
            "No reproduction means no confirmed diagnosis",
            "A successful fix alone is not sufficient",
            "did not isolate the cause does not establish it",
            "not by familiarity or how common a bug seems",
            "outcomes that would distinguish plausible causes",
            "missing conditions, attempts and results",
            "Without repository access", "No sibling skill or shared reference bundle",
            "not fix implementation or regression-test implementation",
            "Read `references/root-cause-report.md`", "If unreadable",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, normalized)

    def test_install_alone_resolve_links_and_preserve_bytes(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {
            Path("SKILL.md"), Path("references/root-cause-report.md")
        })
        with tempfile.TemporaryDirectory() as folder:
            for host in (".agents", ".claude"):
                with self.subTest(host=host):
                    skills = Path(folder) / host / "skills"
                    installed = skills / SOURCE.name
                    shutil.copytree(SOURCE, installed)
                    self.assertEqual([p.name for p in skills.iterdir()], [SOURCE.name])
                    self.assertEqual(snapshot(installed), original)
                    links = []
                    for document in installed.rglob("*.md"):
                        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)",
                                                 document.read_text(encoding="utf-8")):
                            resolved = (document.parent / target).resolve()
                            self.assertTrue(resolved.is_relative_to(installed.resolve()))
                            self.assertTrue(resolved.is_file(), target)
                            links.append(resolved)
                    self.assertIn(installed.resolve() / "references/root-cause-report.md", links)
        self.assertEqual(snapshot(SOURCE), original)

    def test_sync_preserves_private_template_without_shared_dependencies(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / "shared", root / "shared")
            installed = root / "skills" / SOURCE.name
            shutil.copytree(SOURCE, installed)
            before = snapshot(root)
            self.assertEqual(references.reference_plan(root), ([], 1))
            self.assertEqual(references.reference_plan(root, check=True), ([], 1))
            self.assertEqual(snapshot(root), before)
            for name in references.SHARED:
                unexpected = installed / "references" / name
                unexpected.write_bytes((root / "shared/references" / name).read_bytes())
                with self.assertRaisesRegex(ValueError, "Unexpected shared reference"):
                    references.reference_plan(root, check=True)
                unexpected.unlink()


if __name__ == "__main__":
    unittest.main()
