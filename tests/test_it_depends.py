"""Decision contract and isolated packaging; not recommendation-quality evaluation."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/it-depends"
spec = importlib.util.spec_from_file_location(
    "it_depends_reference_tools", ROOT / "scripts/reference_tools.py"
)
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class ItDependsStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        cls.template = (SOURCE / "references/decision-record.md").read_text(
            encoding="utf-8")

    def assert_contract(self, document, phrases):
        # Presence checks expose missing instructions, not agent compliance.
        normalized = " ".join(document.split())
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, normalized)

    def test_metadata_activation_and_exclusions(self):
        self.assertTrue(self.entry.startswith(
            "---\nname: it-depends\ndescription: |\n"))
        self.assert_contract(self.entry.split("---", 2)[1], (
            "Use when:", "intended behavior is sufficiently understood",
            "approach remains undecided", "multiple meaningful technical approaches",
            "architectural or implementation-strategy tradeoffs",
            "consequential technology, integration, or design choice",
            "Do not use when:", "what to build is still unclear",
            "approach is already settled", "trivial conventional task",
            "whether an idea should exist",
            "execution/code changes are requested without an unresolved approach decision",
        ))
        self.assertIn("Lens: Which approach, given the constraints?", self.entry)
        self.assertIn("Do not require a Decision Record for routine development", self.entry)

    def test_template_fields(self):
        self.assertEqual(re.findall(r"^## (.+)$", self.template, re.MULTILINE), [
            "Decision question and context",
            "Requirements, constraints, and assumptions",
            "Alternatives and tradeoffs",
            "Chosen or provisionally preferred approach",
            "Rejected alternatives and reasons",
            "Reversibility and revisit conditions",
            "Evidence and verification limitations",
            "Open questions and next evidence",
            "Boundaries and handoff",
        ])
        self.assert_contract(self.template, (
            "original request", "non-goals", "operational constraints",
            "retain upstream AC-n", "Supporting evidence and limits",
            "Dependent option or conclusion", "not execution authorization",
            "short fields are sufficient",
        ))

    def test_genuine_comparison_and_project_fit(self):
        self.assert_contract(self.entry, (
            "Compare at least two genuine alternatives before recommending a choice",
            "plausibly address the actual objective under known constraints",
            "do not manufacture weak or straw-man options",
            "Use consistent criteria across options",
            "what it does better", "why its disadvantages outweigh those benefits here",
            "existing conventions, operational constraints",
            "cost of introducing dependencies or abstractions",
            "sophistication is not evidence of superiority",
            "arbitrary numerical scores", "invented benchmarks",
            "unsupported performance claims",
        ))
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "at least two genuine alternatives", "`one-way`",
                "undo is impractical", "assumption", "reverse the choice",
                "unresolved", "cheapest useful investigation",
            ))
        self.assert_contract(self.entry, (
            "If multiple alternatives cannot be meaningfully assessed",
            "do not fabricate alternatives or force a recommendation",
            "keep the assessment provisional",
        ))

    def test_evidence_and_upstream_reverification(self):
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "Upstream:", "Re-derived:", "load-bearing", "actual",
                "`inferred`", "`assumed`", "`unknown`",
                "unverified premise", "insufficient evidence with no value offered",
                "Shared-origin artifacts count as one source",
            ))
        self.assert_contract(self.entry, (
            "Independently re-derive", "freshness", "original request",
            "ownership, boundary, consumer, and rollback claims",
            "Name failed or unavailable re-derivations",
            "names the inherited claim", "attribute user reports",
            "surface every assumption relied on in open questions",
            "Do not invent reads, tests, measurements, or successful outcomes",
        ))

    def test_standalone_fallbacks_and_boundaries(self):
        self.assert_contract(self.entry, (
            "Without Requirements, derive only minimal supported criteria",
            "Without a Codebase Map, inspect only task-relevant code",
            "Without repository access", "do not invent inspection",
            "No sibling skill or shared reference is required",
            "relative to this installed skill directory",
            "If unreadable, disclose the missing template",
            "do not borrow sibling files", "Missing siblings",
            "do not automatically activate a pipeline",
            "Do not classify the nine Interface Check surfaces",
            "No additional decision-specific hard gate",
            "human-authority gates have no escape",
            "Comprehensive behavioral evaluation remains deferred",
        ))
        for skill, artifact in (
            ("define-done", "Requirements"),
            ("think-before-you-commit", "Implementation Plan"),
            ("devils-advocate", "Challenge Report"),
            ("you-are-here", "Codebase Map"),
            ("previously-on", "Handoff Document"),
            ("read-the-contract", "Contract Review"),
        ):
            self.assertIn(skill, self.entry)
            self.assert_contract(self.entry, (artifact,))

    def test_isolated_codex_claude_links_and_bytes(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {
            Path("SKILL.md"), Path("references/decision-record.md")
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
                    self.assertIn(installed.resolve() / "references/decision-record.md", links)
        self.assertEqual(snapshot(SOURCE), original)

    def test_sync_preserves_bytes_and_rejects_unneeded_shared_references(self):
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
