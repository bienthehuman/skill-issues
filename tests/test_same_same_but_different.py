"""Refactor instructions and standalone packaging; not behavioral evaluation."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/same-same-but-different"
spec = importlib.util.spec_from_file_location(
    "refactor_reference_tools", ROOT / "scripts/reference_tools.py")
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class SameSameButDifferentStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        cls.template = (SOURCE / "references/refactor-plan.md").read_text(
            encoding="utf-8")

    def assert_contract(self, document, phrases):
        # Presence checks detect omissions, not compliance or reasoning quality.
        normalized = " ".join(document.split())
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, normalized)

    def test_metadata_activation_and_exclusions(self):
        self.assertTrue(self.entry.startswith(
            "---\nname: same-same-but-different\ndescription: |\n"))
        self.assert_contract(self.entry.split("---", 2)[1], (
            "Use when:", "behavior-preserving refactor", "internal restructure",
            "code reorganization", "externally observable behavior",
            "verification of behavioral invariants", "Do not use when:",
            "functionality intentionally changes", "bug fix", "trivial rename",
            "mechanical edit already has adequate guarantees",
            "ordinary implementation", "contract redesign or migration",
            "Do not turn every cleanup into a formal refactoring workflow",
        ))
        self.assertIn("Lens: Change structure, not behavior.", self.entry)

    def test_template_required_fields(self):
        self.assertEqual(re.findall(r"^## (.+)$", self.template, re.MULTILINE), [
            "Objective and scope", "Inputs and current behavior",
            "Preservation invariants and contracts",
            "Behavior evidence and G1 readiness",
            "Known defects intentionally preserved",
            "Ordered reversible steps and individual verification",
            "Reversibility and rollback considerations", "Stop conditions",
            "Interface Check", "Risks, uncertainties and open questions",
            "Relevant downstream handoffs and bounded conclusion",
        ])
        self.assert_contract(self.entry, (
            "Read `references/refactor-plan.md`",
            "relative to this installed skill directory", "If unreadable",
            "partial plan retaining the required fields", "do not borrow sibling files",
        ))
        self.assert_contract(self.template, (
            "Target code, intended structural improvement", "Path / invariant",
            "Consequence of unnoticed change", "Sufficient / insufficient and rationale",
            "Gap and required verification", "Step / prerequisite",
            "Verification and unchanged expected outcome", "Reversal / rollback limits",
            "failed, blocked and unrun checks", "commands, revision, environment",
        ))

    def test_g1_per_path_sufficiency_and_compiler_limits(self):
        self.assert_contract(self.entry, (
            "Establish G1 before refactoring code edits",
            "For every affected behavioral path", "preservation invariant",
            "consequence of an unnoticed change", "sufficient or insufficient assessment",
            "test inputs, setup, and assertions", "would they detect the behavior breaking?",
            '"the tests pass" is not a sufficiency statement',
            "named existing tests exercising the path", "snapshots/golden outputs",
            "characterization tests", "other specifically identified reliable verification",
            "rename-only or move-only changes", "only for behavior they actually protect",
            "runtime behavior, serialization, reflective lookup, or external consumers",
            "Do not require new tests when equivalent reliable evidence already suffices",
            "G1 blocks refactoring code edits if any touched path lacks evidence",
            "targeted characterization or alternative verification",
            "Proposed or merely written tests are not executed/passed evidence",
            "do not average away an unprotected path",
        ))
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "Existing tests alone do not", "G1", "every touched path",
                "runtime behavior, serialization", "external consumers",
            ))

    def test_known_defects_steps_and_stop_conditions(self):
        self.assert_contract(self.entry, (
            "Do not assume current behavior is correct",
            "known defects intentionally preserved", "not desired functionality",
            "Separate bug fixes and functional improvements",
            "small, ordered steps", "prerequisites", "practical reversal",
            "Each step ends in a verifiable, working state",
            "Prefer independently verifiable changes over large rewrites",
            "If a refactoring step requires changing a test's expected behavior",
            "stop and identify the behavior change separately",
            "Test relocation, import updates, or structural reorganization",
            "preserve the same assertions and expected outcomes",
            "Do not rewrite failing tests or weaken assertions",
            "failed verification", "newly unprotected paths",
            "Reassess G1 if the actual scope expands",
        ))
        self.assert_contract(self.template, (
            "Known bug -> path/invariant -> evidence",
            "behavior intentionally unchanged", "separate follow-up",
            "stop and separate the behavior change",
            "do not rewrite failures or weaken assertions",
            "`one-way`", "undo is impractical",
        ))

    def test_interface_read_before_classification_and_failure_fallback(self):
        self.assert_contract(self.entry, (
            "Before performing an Interface Check, read `references/interface-check.md`",
            "relative to this installed skill directory, in this run",
            "Do not classify interface surfaces until the reference has been loaded",
            "do not reconstruct the checklist from memory",
            "canonical nine-surface plan-time scan", "evidence for every",
            "Expand only affected and uncertain entries",
            "frontend consumer search rule unless API types are generated",
            "database/connection naming", "stored-state investigation",
            "Collapse only when directly observed evidence establishes all four",
            "conditions in the reference", "an inferred check cannot collapse",
            "mark all nine surfaces `uncertain`", "reference was not loaded",
            "assessment as incomplete", "restoration/read of this bundle or human direction",
            "Do not borrow a sibling's reference", "fabricate classifications",
            "Split any proposed interface contract change out of the refactor",
            "scoped read-the-contract handoff", "known consumers/search limits",
            "A handoff is not a completed Contract Review",
        ))
        # The directive must precede the instruction to apply the scan.
        self.assertLess(self.entry.index("Before performing an Interface Check"),
                        self.entry.index("Apply its canonical nine-surface"))
        self.assert_contract(self.template, (
            "read this installed bundle's interface-check.md",
            "all four canonical conditions", "never inferred",
            "all nine surfaces `uncertain`", "assessment is incomplete",
        ))
        canonical = (ROOT / "shared/references/interface-check.md").read_bytes()
        self.assertEqual((SOURCE / "references/interface-check.md").read_bytes(),
                         canonical)

    def test_evidence_envelope_standalone_and_boundaries(self):
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "Upstream:", "Re-derived:", "first line", "load-bearing",
                "actual source checks", "Shared-origin artifacts count as one source",
                "`inferred`", "`assumed`", "`unknown`", "unverified premise",
                "insufficient evidence with no value offered",
                "open questions", "one-way",
            ))
            for skill in ("prove-it", "think-before-you-commit", "read-the-contract",
                          "trust-issues", "what-could-possibly-go-wrong"):
                self.assertIn(skill, document)
        self.assert_contract(self.entry, (
            "Without behavior evidence", "each evidence gap",
            "With insufficient existing tests", "exactly which behavior lacks protection",
            "Without repository access, work only with supplied code/evidence",
            "Do not claim repository searches or test execution occurred",
            "No sibling skill is required", "not required to be installed",
            "does not automatically execute it or the downstream pipeline",
            "without reconstructing their procedures or claiming the skill ran",
            "G6/G7 human-authority gates have no escape",
            "ordinary approved reversible work is allowed",
            "Do not add a refactor-specific authorization mechanism",
            "Comprehensive behavioral evaluation remains deferred",
            "Structural validation does not establish behavior-preservation reasoning",
        ))

    def test_isolated_codex_claude_links_and_bytes(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {
            Path("SKILL.md"), Path("references/refactor-plan.md"),
            Path("references/interface-check.md")})
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
                    for name in ("refactor-plan.md", "interface-check.md"):
                        self.assertIn(installed.resolve() / "references" / name, links)
                    # Backtick read directives resolve from the installed skill,
                    # independently of the project's working directory.
                    entry = (installed / "SKILL.md").read_text(encoding="utf-8")
                    for target in re.findall(r"`(references/[^`]+\.md)`", entry):
                        self.assertTrue((installed / target).is_file(), target)
        self.assertEqual(snapshot(SOURCE), original)

    def test_sync_missing_bundle_drift_and_private_template_preservation(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / "shared", root / "shared")
            installed = root / "skills" / SOURCE.name
            shutil.copytree(SOURCE, installed)
            before = snapshot(root)
            bundle = installed / "references/interface-check.md"
            canonical = (root / "shared/references/interface-check.md").read_bytes()
            for options in ({}, {"check": True}, {"update": True}):
                self.assertEqual(references.reference_plan(root, **options), ([], 1))
                self.assertEqual(snapshot(root), before)
            bundle.unlink()
            missing = snapshot(root)
            with self.assertRaisesRegex(ValueError, "Missing bundled reference"):
                references.reference_plan(root, check=True)
            changes, count = references.reference_plan(root)
            self.assertEqual((changes, count), ([(bundle, canonical)], 1))
            self.assertEqual(snapshot(root), missing)  # preflight does not write
            for path, data in changes:
                references.atomic_write(path, data)
            self.assertEqual(snapshot(root), before)
            bundle.write_bytes(b"deliberate fixture drift\n")
            drifted = snapshot(root)
            for options in ({}, {"check": True}):
                with self.assertRaisesRegex(ValueError, "Divergent bundled reference"):
                    references.reference_plan(root, **options)
                self.assertEqual(snapshot(root), drifted)
            changes, count = references.reference_plan(root, update=True)
            self.assertEqual((changes, count), ([(bundle, canonical)], 1))
            for path, data in changes:
                references.atomic_write(path, data)
            self.assertEqual(snapshot(root), before)
            # Only Interface Check is needed: authorization remains baseline-owned.
            unexpected = installed / "references/authorization.md"
            unexpected.write_bytes((root / "shared/references/authorization.md").read_bytes())
            for options in ({}, {"check": True}, {"update": True}):
                with self.assertRaisesRegex(ValueError, "Unexpected shared reference"):
                    references.reference_plan(root, **options)
            unexpected.unlink()
            self.assertEqual(snapshot(root), before)


if __name__ == "__main__":
    unittest.main()
