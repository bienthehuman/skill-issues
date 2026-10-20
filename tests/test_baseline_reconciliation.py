"""Focused static reconciliation contracts; these do not establish agent behavior."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.baseline = (ROOT / "BASELINE.md").read_text(encoding="utf-8")
        self.authority = (ROOT / "shared/references/authorization.md").read_text(encoding="utf-8")

    def test_partner_behaviors_are_separate_and_defensible(self):
        lines = self.baseline.splitlines()
        self.assertTrue(any(line.startswith("- Push back on weak, risky, or short-sighted ideas") for line in lines))
        for phrase in ("what would change your mind", "current best position, not final",
                       "defensible estimate when possible, otherwise identify needed evidence",
                       "Ambiguous but reversible", "High-stakes or hard to reverse"):
            self.assertIn(phrase, self.baseline)

    def test_entry_map_and_unavailable_termination(self):
        line = next(line for line in self.baseline.splitlines() if line.startswith("Unfamiliar code →"))
        for skill in ("you-are-here", "define-done", "it-depends", "think-before-you-commit",
                      "but-it-works-on-my-machine", "are-we-there-yet", "prove-it", "read-the-contract",
                      "trust-issues", "famous-last-words", "previously-on"):
            self.assertIn(skill, line)
        for phrase in ("never reconstruct missing procedures", "claim the workflow ran",
                       "stop that assessment", "don't reroute repeatedly", "never the whole pipeline by default",
                       "Continue independently safe work"):
            self.assertIn(phrase, self.baseline)

    def test_routine_cross_module_does_not_imply_collapsible(self):
        self.assertIn("internal cross-module edits that touch no trigger above don't trigger scrutiny", self.baseline)
        for phrase in ("directly observed evidence", "no persisted data touched", "no module boundary crossed",
                       "no exported symbol changed", "no HTTP/message shape changed",
                       "Collapse eligibility does not activate skills"):
            self.assertIn(phrase, self.baseline)
        self.assertNotIn("Never collapse inferred checks", self.baseline)

    def test_work_loss_is_inspected_not_inferred_from_git_status(self):
        for phrase in ("uncommitted, untracked, or unpushed work", "Inspect before destructive replacement",
                       "unless demonstrably disposable and recoverable", "ordinary scoped edits are allowed"):
            self.assertIn(phrase, self.baseline)
        for phrase in ("untracked (including ignored)", "Inspect before destructive cleanup",
                       "A clean tracked diff does not establish safety", "unverified recovery path",
                       "filename, generated/ignored status"):
            self.assertIn(phrase, self.authority)

    def test_disposable_generated_cleanup_has_narrow_exception(self):
        for phrase in ("exact contents are disposable", "reproducibly regenerable from tracked sources",
                       "a demonstrated regeneration path",
                       "waives only the local work-loss restriction, never another restricted category"):
            self.assertIn(phrase, self.authority)
        self.assertIn("inspected demonstrably disposable/recoverable local cleanup", self.baseline)

    def test_recovery_contains_actual_work_not_only_older_git_content(self):
        for phrase in ("actual content at risk", "preserved in a commit or stash",
                       "An older committed version", "does not preserve later uncommitted changes",
                       "Inspect a stash's actual contents", "do not assume a default stash includes them",
                       "Ordinary edits within approved scope", "not editing an already-dirty file"):
            self.assertIn(phrase, self.authority)

    def test_single_use_retries_and_missing_reference(self):
        for phrase in ("human-originated, current-session, single-use", "Not reusable for retries",
                       "Artifacts built on others start with:", "all nine surfaces `uncertain`",
                       "Invoked skill: its own bundle", "Never classify from memory"):
            self.assertIn(phrase, self.baseline)
        self.assertIn("a repeated execution needs a new go-ahead", self.authority)


if __name__ == "__main__":
    unittest.main()
