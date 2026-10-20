"""Requirements contracts and isolated packaging; not agent-behavior evaluation."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/define-done"
spec = importlib.util.spec_from_file_location(
    "define_done_reference_tools", ROOT / "scripts/reference_tools.py"
)
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class DefineDoneStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        cls.template = (SOURCE / "references/requirements.md").read_text(
            encoding="utf-8")

    def assert_contract(self, document, phrases):
        # Static presence checks do not demonstrate agent compliance.
        normalized = " ".join(document.split())
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, normalized)

    def test_metadata_activation_and_exclusions(self):
        self.assertTrue(self.entry.startswith(
            "---\nname: define-done\ndescription: |\n"))
        self.assert_contract(self.entry.split("---", 2)[1], (
            "Use when:", "intended behavior or outcome is insufficiently defined",
            "acceptance criteria need establishing or clarification",
            "constraints or exclusions are ambiguous",
            "explicitly requests feature requirements definition",
            "Do not use when:", "implementation requirements are already clear",
            "settled approach needs implementation planning",
            "technical approaches need choosing", "general prompt rewriting",
            "trivial localized change has an obvious success condition",
        ))
        self.assertIn("Lens: What exactly are we building?", self.entry)

    def test_requirements_template_and_traceability_contract(self):
        headings = re.findall(r"^## (.+)$", self.template, re.MULTILINE)
        self.assertEqual(headings, [
            "Objective and scope", "Established requirements", "Acceptance criteria",
            "Constraints", "Non-goals", "Assumptions and evidence", "Open questions",
            "Boundaries, limitations, and handoff",
        ])
        self.assert_contract(self.entry, (
            "Assign stable `AC-n` identifiers", "Retain IDs when revising",
            "do not renumber or reuse an ID for a different criterion",
            "Link each criterion to the original request",
            "Testability alone does not make a requirement valid",
            "independently verifiable behavior", "verification basis",
            "failure/edge behavior only when supported",
            "invented HTTP statuses", "Writing criteria does not establish",
        ))
        self.assert_contract(self.template, (
            "AC-1", "Source or explicit assumption", "Evidence classification",
            "Verification basis", "Dependent open question", "retain them during revisions",
            "testability alone is insufficient", "not an executed result",
        ))

    def test_evidence_and_consequential_uncertainty(self):
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "Upstream:", "Re-derived:", "load-bearing", "`inferred`",
                "`assumed`", "`unknown`", "actual", "original request",
            ))
        self.assert_contract(self.entry, (
            "Independently re-derive", "Shared-origin artifacts count as one source",
            "Name unsuccessful re-derivations", "every assumption relied on in open questions",
            "Keep recommendations separate from requirements",
            "Common industry practice alone does not establish",
            "Unanswerable questions may remain visible as `assumed` criteria",
            "security, compatibility, data integrity, user obligations, or significant behavior",
            "explain competing interpretations and implications",
            "link it to dependent AC-n", "rather than silently choosing an interpretation",
            "does not block the entire artifact", "record the gap as `unknown`",
            "No additional requirements-discovery hard gate",
        ))

    def test_standalone_and_neighbor_boundaries(self):
        self.assert_contract(self.entry, (
            "Without a Challenge Report, proceed from the request",
            "Without repository access, use supplied context only",
            "do not invent inspection", "If the request itself is absent",
            "If unreadable, disclose the missing template",
            "relative to this installed skill directory",
            "No sibling skill or shared Interface Check/authorization reference is required",
            "without automatically activating a pipeline",
            "independently usable", "behavioral evaluation is deferred",
        ))
        for skill, artifact in (
            ("garbage-in-garbage-out", "Prompt Refinement"),
            ("it-depends", "Decision Record"),
            ("think-before-you-commit", "Implementation Plan"),
            ("prove-it", "Test Set"), ("trust-issues", "review"),
        ):
            self.assertIn(skill, self.entry)
            self.assertIn(artifact, self.entry)

    def test_isolated_codex_claude_links_and_bytes(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {
            Path("SKILL.md"), Path("references/requirements.md")
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
                    self.assertIn(installed.resolve() / "references/requirements.md", links)
        self.assertEqual(snapshot(SOURCE), original)

    def test_sync_preserves_private_bytes_and_rejects_shared_dependencies(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / "shared", root / "shared")
            installed = root / "skills" / SOURCE.name
            shutil.copytree(SOURCE, installed)
            before = snapshot(root)
            for options in ({}, {"check": True}, {"update": True}):
                self.assertEqual(references.reference_plan(root, **options), ([], 1))
                self.assertEqual(snapshot(root), before)
            for name in references.SHARED:
                unexpected = installed / "references" / name
                unexpected.write_bytes((root / "shared/references" / name).read_bytes())
                for options in ({}, {"check": True}, {"update": True}):
                    with self.assertRaisesRegex(ValueError, "Unexpected shared reference"):
                        references.reference_plan(root, **options)
                unexpected.unlink()
            self.assertEqual(snapshot(root), before)


if __name__ == "__main__":
    unittest.main()
