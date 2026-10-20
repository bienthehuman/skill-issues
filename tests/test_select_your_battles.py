"""Schema contract and isolated packaging; not database-advice evaluation."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/select-your-battles"
spec = importlib.util.spec_from_file_location(
    "schema_reference_tools", ROOT / "scripts/reference_tools.py")
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class SelectYourBattlesStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        cls.template = (SOURCE / "references/schema-review.md").read_text(
            encoding="utf-8")

    def assert_contract(self, document, phrases):
        # Presence checks detect omissions, not agent compliance or sound advice.
        normalized = " ".join(document.split())
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, normalized)

    def test_metadata_activation_and_exclusions(self):
        self.assertTrue(self.entry.startswith(
            "---\nname: select-your-battles\ndescription: |\n"))
        self.assert_contract(self.entry.split("---", 2)[1], (
            "Use when:", "schemas", "indexes", "constraints", "queries",
            "migration designs", "are-we-there-yet handoff", "Route by database topic",
            "Do not use when:", "ordinary application debugging",
            "uninvestigated ORM-level N+1", "performance measurement",
            "bottleneck identification", "production migration execution",
            "deployment sequencing", "trivial application change",
        ))
        self.assertIn("Lens: Is the data shape right for how it is accessed?", self.entry)

    def test_template_fields(self):
        self.assertEqual(re.findall(r"^## (.+)$", self.template, re.MULTILINE), [
            "Objective and scope", "Database context and input evidence",
            "Access patterns and queries", "Schema decisions and supported behavior",
            "Index recommendations and justification",
            "Constraints and integrity invariants", "Transaction boundaries",
            "Concurrency and locking risks",
            "Migration design and existing-data compatibility",
            "Reversibility and one-way items", "Performance evidence and limitations",
            "Recommendations and tradeoffs", "Open questions and unknowns",
            "Relevant downstream handoffs",
        ])
        self.assert_contract(self.entry, (
            "Read `references/schema-review.md`", "relative to this installed skill directory",
            "If unreadable", "partial review", "do not borrow sibling files",
            "A small index review must not become a complete architecture assessment",
        ))

    def test_engine_and_access_pattern_discipline(self):
        self.assert_contract(self.entry, (
            "database engine, named database and connection", "version",
            "MySQL, MariaDB, or PostgreSQL", "multiple databases or connections",
            "Do not infer MySQL from Laravel", "actual engine's supported behavior",
            "avoid unsupported engine-specific conclusions",
            "Pair each meaningful schema decision", "application behavior or access pattern",
            "Every proposed index must serve a named query or access pattern",
            "existing indexes", "composite column ordering", "selectivity evidence",
            "write amplification/maintenance cost", "Do not blanket-index",
            "provisional", "name the measurement needed",
        ))

    def test_performance_evidence_and_upstream_envelope(self):
        for document in (self.entry, self.template):
            self.assert_contract(document, (
                "Upstream:", "Re-derived:", "load-bearing", "actual",
                "Shared-origin artifacts count as one source",
                "`inferred`", "`assumed`", "`unknown`", "unverified",
                "EXPLAIN", "row counts", "comparable before/after measurements",
                "improvements remain unverified", "failed", "blocked", "unrun",
            ))
        self.assert_contract(self.entry, (
            "Do not invent query plans, cardinalities, timings, throughput, selectivity, lock durations, or improvements",
            "a dependent conclusion that cannot be re-derived remains `inferred`",
            "Missing facts remain `unknown`", "surface every relied-on assumption",
            "A plausible optimizer choice is not an observed improvement",
        ))

    def test_concurrency_integrity_and_migration_design(self):
        self.assert_contract(self.entry, (
            "atomic operations", "constraints", "concurrent writes", "race conditions",
            "isolation assumptions", "lock scope/contention", "deadlocks",
            "retry/idempotency", "consistency across connections",
            "Separate observed problems from hypothetical risks",
            "throughput, contention, and operational costs",
            "existing-data compatibility", "backfill requirements",
            "null/default transitions", "existing application versions",
            "`one-way`", "undo is impractical", "permanent information loss",
            "down() method does not establish reversibility",
            "recreating a dropped column does not restore its data",
        ))

    def test_standalone_fallbacks_and_boundaries(self):
        self.assert_contract(self.entry, (
            "No sibling skill or shared reference bundle is required",
            "Without access patterns, request relevant workload/query information",
            "review supported structural properties only",
            "query/index suitability unresolved",
            "Missing workload evidence limits conclusions, not all useful analysis",
            "Without repository or database access", "Do not invent schema or database state",
            "Without performance evidence", "Without an Implementation Plan",
            "Missing siblings do not block supported analysis",
            "not a mandatory pipeline", "G6/G7 human-authority gates have no escape",
            "not authorization to run a migration", "section 7 human authorization",
            "Comprehensive behavioral evaluation remains deferred",
        ))
        for skill, artifact in (
            ("are-we-there-yet", "Performance Report"),
            ("think-before-you-commit", "Implementation Plan"),
            ("read-the-contract", "Contract Review"),
            ("what-could-possibly-go-wrong", "Impact Report"),
            ("famous-last-words", "Rollout Plan"),
            ("it-depends", "Decision Record"),
        ):
            self.assertIn(skill, self.entry)
            self.assertIn(artifact, self.entry)

    def test_isolated_codex_claude_links_and_bytes(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {
            Path("SKILL.md"), Path("references/schema-review.md")})
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
                    self.assertIn(installed.resolve() / "references/schema-review.md", links)
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
