"""Portable evidence integrity; these checks do not evaluate agent behavior."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import unittest


PACKAGE = Path(__file__).resolve().parents[1] / "evals/traces/g2-rollback"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def display(text):
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


class PortableG2Evidence(unittest.TestCase):
    def test_payload_and_fixture_hashes_resolve_without_local_captures(self):
        manifest = json.loads((PACKAGE / "manifest.json").read_text(encoding="utf-8"))
        sources = json.loads((PACKAGE / "sources.json").read_text(encoding="utf-8"))
        blobs = sources["blobs_by_sha256"]
        expected = set(manifest["payload_sha256"]) | {"manifest.json"}
        self.assertEqual({p.name for p in PACKAGE.iterdir()}, expected)
        for name, checksum in manifest["payload_sha256"].items():
            self.assertEqual(PurePosixPath(name).name, name)
            self.assertEqual(digest((PACKAGE / name).read_bytes()), checksum, name)
        for checksum, text in blobs.items():
            self.assertEqual(digest(text.encode("utf-8")), checksum)
        self.assertEqual({r["label"] for r in manifest["runs"]},
                         {"original", "corrected", "covered"})
        for run in manifest["runs"]:
            for path, checksum in run["fixture_and_capture_files"].items():
                self.assertFalse(PurePosixPath(path).is_absolute())
                self.assertNotIn("..", PurePosixPath(path).parts)
                self.assertIn(checksum, blobs, (run["id"], path))
            for name in ("prompt.txt", "final.md"):
                self.assertEqual(run["source_sha256"][name],
                                 run["fixture_and_capture_files"]["capture/" + name])

    def test_views_preserve_full_prompt_final_and_identified_excerpts(self):
        manifest = json.loads((PACKAGE / "manifest.json").read_text(encoding="utf-8"))
        blobs = json.loads((PACKAGE / "sources.json").read_text(
            encoding="utf-8"))["blobs_by_sha256"]
        for run in manifest["runs"]:
            document = (PACKAGE / (run["label"] + ".md")).read_text(encoding="utf-8")
            blocks = re.findall(r"^````(?:text|markdown)\n(.*?)\n````$",
                                document, re.S | re.M)
            paths = run["fixture_and_capture_files"]
            self.assertEqual(blocks[0], display(blobs[paths["capture/prompt.txt"]]))
            self.assertEqual(blocks[-1], display(blobs[paths["capture/final.md"]]))
            self.assertEqual(len(blocks) - 2, len(run["selected_events"]))
            for event, block in zip(run["selected_events"], blocks[1:-1]):
                self.assertEqual(digest(block.encode()), event["display_sha256"])
                self.assertGreater(event["end_character"], event["start_character"])
                self.assertIn(f'trace.jsonl line {event["trace_line"]}', document)
                if event["kind"] != "Property-access simulation output":
                    self.assertEqual(event["event_exit_code"], 0)
        runs = {r["label"]: r["fixture_and_capture_files"] for r in manifest["runs"]}
        self.assertEqual(runs["original"]["capture/prompt.txt"],
                         runs["corrected"]["capture/prompt.txt"])
        for path, checksum in runs["original"].items():
            if not path.startswith((".agents/", "capture/")):
                self.assertEqual(checksum, runs["corrected"][path], path)


if __name__ == "__main__":
    unittest.main()
