"""Structural/standalone packaging checks, not agent-behavior evaluations."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "you-are-here"
spec = importlib.util.spec_from_file_location(
    "you_are_here_reference_tools", ROOT / "scripts" / "reference_tools.py"
)
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


def snapshot(root):
    return {p.relative_to(root): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class YouAreHerePackaging(unittest.TestCase):
    def test_install_alone_and_resolve_all_markdown_links(self):
        original = snapshot(SOURCE)
        self.assertEqual(set(original), {
            Path("SKILL.md"), Path("references/codebase-map.md")
        })
        with tempfile.TemporaryDirectory() as folder:
            for host in (".agents", ".claude"):
                with self.subTest(host=host):
                    skills = Path(folder) / host / "skills"
                    installed = skills / "you-are-here"
                    shutil.copytree(SOURCE, installed)
                    self.assertEqual([p.name for p in skills.iterdir()], ["you-are-here"])
                    self.assertEqual(snapshot(installed), original)
                    links = []
                    for document in installed.rglob("*.md"):
                        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)",
                                                 document.read_text(encoding="utf-8")):
                            resolved = (document.parent / target).resolve()
                            self.assertTrue(resolved.is_relative_to(installed.resolve()))
                            self.assertTrue(resolved.is_file(), target)
                            links.append(resolved)
                    self.assertIn(installed.resolve() / "references/codebase-map.md", links)
        self.assertEqual(snapshot(SOURCE), original)

    def test_metadata_and_required_artifact_fields(self):
        entry = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(entry.startswith("---\nname: you-are-here\ndescription: |\n"))
        description = entry.split("---", 2)[1]
        for field in ("Use when:", "Do not use when:"):
            self.assertIn(field, description)
        template = (SOURCE / "references/codebase-map.md").read_text(encoding="utf-8")
        headings = set(re.findall(r"^## (.+)$", template, re.MULTILINE))
        self.assertTrue({
            "Engineering question and scope", "Entry points",
            "Modules and responsibilities", "Execution and data flow",
            "State ownership and persistence", "Module and integration boundaries",
            "Evidence and load-bearing claims",
            "Unknowns, limitations, and follow-up questions",
            "Bounded conclusion and handoff",
        }.issubset(headings))
        for document in (entry, template):
            for label in ("`inferred`", "`assumed`", "`unknown`"):
                self.assertIn(label, document)
            self.assertIn("Upstream:", document)
            self.assertIn("Re-derived:", document)

    def test_sync_preserves_private_template_without_shared_dependencies(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / "shared", root / "shared")
            installed = root / "skills/you-are-here"
            shutil.copytree(SOURCE, installed)
            before = snapshot(root)
            self.assertEqual(references.reference_plan(root), ([], 1))
            self.assertEqual(references.reference_plan(root, check=True), ([], 1))
            self.assertEqual(snapshot(root), before)
            for name in references.SHARED:
                unexpected = installed / "references" / name
                unexpected.write_bytes((root / "shared/references" / name).read_bytes())
                with self.assertRaisesRegex(ValueError, "Unexpected shared reference"):
                    references.reference_plan(root, check=True)
                unexpected.unlink()


if __name__ == "__main__":
    unittest.main()
