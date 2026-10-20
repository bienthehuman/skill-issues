"""Standalone packaging checks; these do not evaluate agent behavior."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "prove-it"
spec = importlib.util.spec_from_file_location(
    "prove_it_reference_tools", ROOT / "scripts" / "reference_tools.py"
)
references = importlib.util.module_from_spec(spec)
spec.loader.exec_module(references)


class ProveItPackaging(unittest.TestCase):
    def test_install_alone_and_resolve_all_markdown_links(self):
        original = {p.relative_to(SOURCE): p.read_bytes()
                    for p in SOURCE.rglob("*") if p.is_file()}
        with tempfile.TemporaryDirectory() as folder:
            for host in (".agents", ".claude"):
                skills = Path(folder) / host / "skills"
                installed = skills / "prove-it"
                shutil.copytree(SOURCE, installed)
                self.assertEqual([p.name for p in skills.iterdir()], ["prove-it"])
                self.assertEqual(
                    {p.relative_to(installed): p.read_bytes()
                     for p in installed.rglob("*") if p.is_file()}, original
                )
                entry = (installed / "SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(entry.startswith("---\nname: prove-it\ndescription: |\n"))
                self.assertIn("Use when:", entry.split("---", 2)[1])
                self.assertIn("Do not use when:", entry.split("---", 2)[1])
                links = []
                for document in installed.rglob("*.md"):
                    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)",
                                             document.read_text(encoding="utf-8")):
                        resolved = (document.parent / target).resolve()
                        self.assertTrue(resolved.is_relative_to(installed.resolve()))
                        self.assertTrue(resolved.is_file(), target)
                        links.append(resolved)
                self.assertIn(installed.resolve() / "references/test-set.md", links)
        self.assertEqual(original, {p.relative_to(SOURCE): p.read_bytes()
                                   for p in SOURCE.rglob("*") if p.is_file()})

    def test_sync_leaves_private_template_untouched_without_shared_dependencies(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / "shared", root / "shared")
            installed = root / "skills/prove-it"
            shutil.copytree(SOURCE, installed)
            before = {p.relative_to(root): p.read_bytes()
                      for p in root.rglob("*") if p.is_file()}
            self.assertEqual(references.reference_plan(root), ([], 1))
            self.assertEqual(references.reference_plan(root, check=True), ([], 1))
            self.assertEqual(before, {p.relative_to(root): p.read_bytes()
                                      for p in root.rglob("*") if p.is_file()})
            # Detect accidental future addition of either shared dependency.
            for name in references.SHARED:
                unexpected = installed / "references" / name
                unexpected.write_bytes((root / "shared/references" / name).read_bytes())
                with self.assertRaisesRegex(ValueError, "Unexpected shared reference"):
                    references.reference_plan(root, check=True)
                unexpected.unlink()


if __name__ == "__main__":
    unittest.main()
