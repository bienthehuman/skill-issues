"""Static instruction regressions, not agent behavioral validation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BaselineReliabilityTests(unittest.TestCase):
    def test_scenario_instructions(self):
        baseline = (ROOT / "BASELINE.md").read_text(encoding="utf-8")
        scenarios = {
            "unavailable skill": ("If a routed skill is unavailable, name it and the limitation",
                                  "never reconstruct missing procedures", "claim the workflow ran",
                                  "stop that assessment", "request the dependency or human direction",
                                  "don't reroute repeatedly", "Continue independently safe work"),
            "missing reference": ("all nine surfaces `uncertain`", "assessment incomplete",
                                  "Never classify from memory"),
            "reference provider": ("Baseline-only: any installed canonical provider", "name provider/path",
                                   "Invoked skill: its own bundle"),
            "contract routing": ("Affected/uncertain interface surface or contract concern → read-the-contract",),
            "routine cross-module and database work": (
                "Routine reads, ordinary application writes, and internal cross-module edits that touch no trigger above don't trigger scrutiny",),
            "consequential persistence": ("schema or serialized formats", "stored-state interpretation/invariants",
                                         "migrations or transformations", "existing-data compatibility"),
            "independent security": ("Security: authentication, authorization, credentials, sensitive data, untrusted input",),
            "real external effects": ("public publishing", "real credential rotation, revocation, or exposure",
                                      "real messages", "external mutations with real credentials",
                                      "consequential paid APIs", "human-originated",
                                      "current-session, single-use", "action, target, and environment",
                                      "Not reusable for retries", "agent recommendations cannot authorize"),
            "local and mocked work": ("Preparing code, ordinary local work, mocks",
                                      "authorized low-risk read-only requests", "aren't restricted by themselves"),
            "pure chat": ("Support findings; attribute user reports",
                          "Never invent reads, inspections, execution, tests, or results"),
            "wrong upstream handoff": ("Independently re-derive load-bearing upstream",
                                       "requirements, code, and data before plan conformance",
                                       "Shared-origin artifacts count as one source"),
            "project instructions": ("host instruction hierarchy", "compatible project conventions",
                                     "disclose unresolved consequential conflicts", "Instructions do not enforce permissions"),
        }
        for scenario, phrases in scenarios.items():
            with self.subTest(scenario=scenario):
                for phrase in phrases:
                    self.assertIn(phrase, baseline)

    def test_preserved_boundaries_and_authority(self):
        source = (ROOT / "SPEC.md").read_text(encoding="utf-8")
        authorization = (ROOT / "shared/references/authorization.md").read_text(encoding="utf-8")
        interface = (ROOT / "shared/references/interface-check.md").read_text(encoding="utf-8")
        for phrase in ("## Practices are tools", "## Scope and completion", "`reconstructed`", "`one-way`"):
            self.assertIn(phrase, source)
        for phrase in ("**Human-originated.**", "**Current.**", "**Single-use.**",
                       "after any change in the plan", "Teams may extend this list. They may not shorten it.",
                       "Ordinary local implementation, mocked/local API tests", "A dry run that sends messages"):
            self.assertIn(phrase, authorization)
        self.assertEqual(sum(line.startswith("| " + str(i) + " |") for line in interface.splitlines()
                             for i in range(1, 10)), 9)
        self.assertIn("no persisted data touched, no module boundary crossed", interface)
        for skill in ("think-before-you-commit", "read-the-contract"):
            entry = (ROOT / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("relative to this installed skill directory", entry)
            self.assertIn("Do not reconstruct the checklist", entry)
        planning = (ROOT / "skills/think-before-you-commit/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("security-sensitive changes", planning)
        self.assertNotIn("a change touches persisted data", planning)


if __name__ == "__main__":
    unittest.main()
