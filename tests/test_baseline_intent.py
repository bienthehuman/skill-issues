"""Static intent/safeguard contracts, not observations of agent behavior."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BaselineIntentTests(unittest.TestCase):
    def test_intent_rule_follows_answer_first(self):
        lines = (ROOT / "BASELINE.md").read_text(encoding="utf-8").splitlines()
        index = next(i for i, line in enumerate(lines) if line.startswith("- Answer first."))
        rule = lines[index + 1]
        for phrase in ("Match the intent: action, analysis, discussion, or acknowledgment",
                       "if a question or offer is pending, treat a bare yes as action",
                       "Don’t restate settled decisions", "echo the user’s point as insight",
                       "add something substantive or keep it short",
                       "Skip unsolicited frameworks, recaps, and next steps",
                       "never skip risks, gaps, or check results the work requires"):
            self.assertIn(phrase, rule)
        self.assertEqual(sum("Match the intent:" in line for line in lines), 1)

    def test_brevity_retains_required_scrutiny_and_authority(self):
        baseline = (ROOT / "BASELINE.md").read_text(encoding="utf-8")
        for phrase in ("Show reasoning: tradeoffs, alternatives, what would change your mind",
                       "Push back on weak, risky, or short-sighted ideas",
                       "Uncertain: say so", "otherwise identify needed evidence",
                       "Disclose failed, blocked, and unrun checks",
                       "Never invent reads, inspections, execution, tests, or results",
                       "human-originated, current-session, single-use authorization",
                       "naming action, target, and environment. Not reusable for retries"):
            self.assertIn(phrase, baseline)
        spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
        self.assertIn("it does not supply missing action/target/environment details", spec)


if __name__ == "__main__":
    unittest.main()
