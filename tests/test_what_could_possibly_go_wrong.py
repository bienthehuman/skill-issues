"""Impact contract and isolated packaging; not blast-radius behavioral evaluation."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/what-could-possibly-go-wrong"
spec = importlib.util.spec_from_file_location(
    "impact_reference_tools", ROOT / "scripts/reference_tools.py"
)
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class WhatCouldPossiblyGoWrongStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        cls.template = (SOURCE / "references/impact-report.md").read_text(
            encoding="utf-8")

    def assert_contract(self, document, phrases):
        # Presence checks detect missing instructions, not agent compliance.
        normalized = " ".join(document.split())
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, normalized)

    def test_metadata_activation_and_exclusions(self):
        self.assertTrue(self.entry.startswith(
            "---\nname: what-could-possibly-go-wrong\ndescription: |\n"))
        self.assert_contract(self.entry.split("---", 2)[1], (
            "Use when:", "consequential dependency or regression-risk question",
            "scrutiny trigger fires on a plan or diff",
            "user requests change-impact or blast-radius analysis",
            "components, state owners, or integration boundaries",
            "Do not use when:", "no meaningful scrutiny trigger",
            "trivial and localized", "live deployment or operational rollback",
            "primary need is contract compatibility", "general repository orientation",
            "Multiple modified files alone do not trigger this skill",
        ))
        self.assertIn("Lens: What in the code and dependencies does this change touch?",
                      self.entry)

    def test_template_fields_and_verification(self):
        self.assertEqual(re.findall(r"^## (.+)$", self.template, re.MULTILINE), [
            "Change objective and investigation scope", "Inputs and provenance",
            "Observed change boundary", "Affected components and dependency paths",
            "Ranked regression risks", "Supporting evidence and uncertainty",
            "Recommended verification and actual execution",
            "Blast-radius coverage and limitations",
            "Open questions and unresolved dependencies",
            "Bounded conclusion and handoff considerations",
        ])
        self.assert_contract(self.entry, (
            "Read `references/impact-report.md`",
            "relative to this installed skill directory", "If unreadable",
            "partial report retaining the fields", "do not borrow sibling files",
        ))
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "verification recommended from verification actually performed",
                "suggested test has not passed",
            ))
        self.assert_contract(self.template, (
            "Link every material risk", "failed, blocked and unrun checks",
            "Actual command/result/evidence", "stopping reason",
        ))

    def test_plan_diff_and_upstream_evidence(self):
        self.assert_contract(self.entry, (
            "A Plan describes intended changes", "a diff evidences actual modifications",
            "Neither proves runtime behavior or complete consumer coverage",
            "use the diff for actual modifications",
            "material discrepancies from planned scope",
            "Do not describe a planned modification as already made",
            "freshness and relevance", "original request",
        ))
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "Upstream:", "Re-derived:", "actual source checks",
                "Shared-origin artifacts count as one source",
                "ownership, boundary", "consumer claims",
                "`inferred`", "`assumed`", "`unknown`",
                "unverified premise", "insufficient evidence with no value offered",
                "dependent conclusion `inferred`", "missing facts",
            ))
        self.assert_contract(self.entry, (
            "observed affected components", "`inferred` potential effects",
            "`assumed` dependencies", "`unknown` consumers or behavior",
            "surface every assumption relied on in open questions",
        ))

    def test_tracing_ranking_and_coverage_severity(self):
        self.assert_contract(self.entry, (
            "concrete dependencies or potential consequences justify it",
            "callers/callees", "persistence and state ownership",
            "events/queues/jobs", "configuration/feature flags",
            "frontend/backend", "not a mandatory checklist",
            "blocked or disproportionate", "Do not map the entire repository",
            "trace supported direct callers only", "**lower bound**",
            "No additional discovered consumers is not proof that none exist",
            "failure trigger and scenario", "consequence/severity",
            "Rank by relevance, evidence, and potential consequences",
            "likelihood or confidence only when defensible",
            "Do not invent probabilities", "arbitrary numerical scores",
            "production traffic, data volumes, or infrastructure",
        ))
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "coverage", "severity", "high-consequence uncertainty",
                "even when no affected consumer was found",
                "scoped", "check", "lower-bound",
            ))

    def test_standalone_and_cross_skill_boundaries(self):
        self.assert_contract(self.entry, (
            "No sibling skill or shared reference is required",
            "Without repository access", "supplied Plan, diff, or other primary material",
            "do not invent inspection or consumers", "Without a Plan or diff",
            "user's description", "clearly limited preliminary assessment",
            "request its objective", "rather than implying safety",
            "Do not perform the canonical Interface Check",
            "reproduce or reclassify all nine surfaces",
            "or claim a Contract Review completed",
            "neither interface-check.md nor authorization.md",
            "known consumers/search limits and open questions",
            "Missing sibling instructions", "never reconstructing their procedures",
            "Do not automatically run the complete pipeline",
            "No impact-specific hard gate", "G6/G7 human-authority gates have no escape",
            "Comprehensive behavioral evaluation remains deferred",
            "routing quality and blast-radius completeness remain unproven",
        ))
        for name in ("you-are-here", "think-before-you-commit", "read-the-contract",
                     "prove-it", "trust-issues", "famous-last-words"):
            self.assertIn(name, self.entry)
            self.assertIn(name, self.template)

    def test_isolated_codex_claude_links_and_bytes(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {
            Path("SKILL.md"), Path("references/impact-report.md")
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
                    self.assertIn(installed.resolve() / "references/impact-report.md", links)
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
