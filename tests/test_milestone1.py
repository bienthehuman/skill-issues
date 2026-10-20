"""Structural packaging checks only; no behavioral pass claims."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("prepare", ROOT / "evals/prepare.py")
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)


class Milestone1Tests(unittest.TestCase):
    def test_independent_install_and_missing_reference_isolation(self):
        original = (ROOT / "skills" / fixture.SKILL / "references/interface-check.md").read_bytes()
        with tempfile.TemporaryDirectory() as directory:
            for agent in ("codex", "claude"):
                for case in "ABC":
                    project = fixture.prepare(Path(directory) / (agent + case), agent, case)
                    base = ".agents/skills" if agent == "codex" else ".claude/skills"
                    skills = project / base
                    self.assertEqual([p.name for p in skills.iterdir()], [fixture.SKILL])
                    bundle = skills / fixture.SKILL / "references"
                    self.assertTrue((bundle / "authorization.md").is_file())
                    self.assertTrue((bundle / "implementation-plan.md").is_file())
                    self.assertEqual((bundle / "interface-check.md").exists(), case != "C")
                    if case != "C":
                        self.assertEqual((bundle / "interface-check.md").read_bytes(), original)
                    self.assertTrue((project / ("AGENTS.md" if agent == "codex" else "CLAUDE.md")).is_file())
                    with self.assertRaises(ValueError):
                        fixture.prepare(project, agent, case)
        self.assertEqual((ROOT / "skills" / fixture.SKILL / "references/interface-check.md").read_bytes(), original)

    def test_artifact_contract_and_self_contained_links(self):
        skill = ROOT / "skills" / fixture.SKILL
        template = (skill / "references/implementation-plan.md").read_text()
        headings = [line for line in template.splitlines() if line.startswith("## ")]
        self.assertEqual(len(headings), 11)
        for number, heading in enumerate(headings, 1):
            self.assertTrue(heading.startswith(f"## {number}. "))
        for field in ("AC-n", "Re-derived:", "one-way", "go-ahead at execution", "Verification for each step", "Out of scope"):
            self.assertIn(field, template)
        entry = (skill / "SKILL.md").read_text()
        self.assertIn("Use when:", entry)
        self.assertIn("Do not use when:", entry)
        for name in ("interface-check", "authorization", "implementation-plan"):
            self.assertIn(f"references/{name}.md", entry)
            self.assertTrue((skill / f"references/{name}.md").is_file())


if __name__ == "__main__":
    unittest.main()
