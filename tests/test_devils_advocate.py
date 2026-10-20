"""Challenge contract and isolated packaging; not verdict-quality evaluation."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/devils-advocate"
spec = importlib.util.spec_from_file_location(
    "devils_advocate_reference_tools", ROOT / "scripts/reference_tools.py"
)
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class DevilsAdvocateStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        cls.template = (SOURCE / "references/challenge-report.md").read_text(
            encoding="utf-8")

    def assert_contract(self, document, phrases):
        # Presence checks reveal missing instructions, not agent compliance.
        normalized = " ".join(document.split())
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, normalized)

    def test_metadata_activation_and_exclusions(self):
        self.assertTrue(self.entry.startswith(
            "---\nname: devils-advocate\ndescription: |\n"))
        self.assert_contract(self.entry.split("---", 2)[1], (
            "Use when:", "direction-level decision", "significant effort",
            "time, complexity, or resources", "explicitly requests a critical challenge",
            "value, adoption, feasibility, or consequence assumptions",
            "Do not use when:", "minor implementation detail",
            "technical implementations of an established goal", "routine coding",
            "debugging", "ordinary code review", "no significant direction-level",
            "Risks or tradeoffs alone do not activate",
        ))
        self.assertIn("Lens: Should this exist, and what would change our mind?", self.entry)

    def test_report_fields(self):
        self.assertEqual(re.findall(r"^## (.+)$", self.template, re.MULTILINE), [
            "Idea or decision being challenged",
            "Intended goal and success conditions",
            "Context and evidence",
            "Load-bearing assumptions",
            "Strongest counter-case",
            "Incentives and adoption friction",
            "Meaningful alternatives or status quo",
            "Verdict, rationale, and uncertainty",
            "Evidence that would overturn the verdict",
            "Recommended next action or investigation",
            "Open questions and limitations",
        ])
        self.assert_contract(self.template, (
            "short fields suffice", "Dependent conclusion", "Evidence basis",
            "failed check/re-derivation", "No forced option count",
        ))

    def test_goal_before_verdict_and_missing_inputs(self):
        self.assert_contract(self.entry, (
            "Establish the goal before judging", "beneficiaries and affected people",
            "what successful adoption or implementation would accomplish",
            "ask what success looks like before issuing a substantive verdict",
            "do not invent a goal", "user demand, business value",
            "Without upstream artifacts", "Without repository access",
            "do not imply code, architecture, or operational details were inspected",
            "Missing evidence remains visible",
        ))
        self.assert_contract(self.template, (
            "ask what success looks like before giving a verdict",
            "Missing evidence is not proof for or against the proposal",
        ))

    def test_substantive_balanced_countercase_and_adoption(self):
        self.assert_contract(self.entry, (
            "hidden, load-bearing assumptions", "materially alter the recommendation",
            "investigative lenses, not a mandatory checklist",
            "Do not manufacture objections", "strongest credible counter-case",
            "opportunity cost", "maintenance costs", "organizational capacity",
            "A theoretically possible failure is not necessarily likely",
            "low-consequence uncertainty alone does not justify rejection",
            "what it establishes, what it does not",
            "Do not invent user behavior or stakeholder preferences",
            "decisive adoption assumptions are unverified",
            "technical feasibility alone does not establish adoption",
        ))
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "Weigh evidence supporting the proposal as seriously as evidence against it",
                "strongest counterargument is not automatically the winning argument",
                "training/migration costs", "support and maintenance responsibilities",
            ))

    def test_defeasible_recommendations(self):
        for document in (self.entry, self.template):
            for verdict in ("Proceed", "Reshape", "Drop"):
                self.assertRegex(document, rf"\*\*{verdict}:?\*\*")
            self.assert_contract(document, (
                "sufficiently justified under established constraints",
                "material adjustment", "explicitly provisional",
            ))
        self.assert_contract(self.entry, (
            "Every verdict identifies concrete evidence that would overturn it",
            "next justified action or investigation", "do not force certainty",
            "manufacture a reason to drop", "missing goal still requires clarification",
        ))
        self.assert_contract(self.template, (
            "Required for every verdict, including Proceed",
            "why they would change it, and how they could be checked",
        ))

    def test_evidence_and_upstream_reverification(self):
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "Upstream:", "Re-derived:", "actual source checks",
                "Independently re-derive load-bearing", "`inferred`", "`assumed`",
                "`unknown`", "unverified premise",
                "insufficient evidence with no value offered",
                "Shared-origin artifacts count as one source",
                "rationale is not independent evidence",
                "attribute user reports", "every assumption relied on in open questions",
            ))
        self.assert_contract(self.entry, (
            "relevance, freshness", "names the inherited claim",
            "Name failed or unavailable re-derivations",
            "Re-check every load-bearing inferred/assumed claim",
        ))

    def test_standalone_template_and_neighboring_boundaries(self):
        self.assert_contract(self.entry, (
            "No sibling skill or shared reference is required",
            "Read `references/challenge-report.md`",
            "relative to this installed skill directory",
            "If unreadable, disclose the missing template",
            "Do not borrow sibling files", "do not automatically activate a pipeline",
            "independently check whether those assumptions still hold",
            "human-authority gates have no escape", "not human approvals",
            "grant no implementation, restricted execution, or compatibility exception authority",
            "behavioral evaluation remains deferred",
        ))
        for skill, artifact in (
            ("define-done", "Requirements"), ("it-depends", "Decision Record"),
            ("think-before-you-commit", "Implementation Plan"),
            ("what-could-possibly-go-wrong", "Impact Report"),
            ("trust-issues", "Review Findings"),
        ):
            self.assertIn(skill, self.entry)
            self.assertIn(artifact, self.entry)

    def test_isolated_codex_claude_links_and_bytes(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {
            Path("SKILL.md"), Path("references/challenge-report.md")
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
                    self.assertIn(installed.resolve() / "references/challenge-report.md", links)
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
