"""Size-check semantics; tokenizer availability must not turn estimates into proof."""
import importlib.machinery
import importlib.util
from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader("baseline_size", str(ROOT / "scripts/check-baseline"))
spec = importlib.util.spec_from_loader(loader.name, loader)
size = importlib.util.module_from_spec(spec)
loader.exec_module(size)


class BaselineSizeTests(TestCase):
    def test_estimate_never_proves_ceiling_compliance(self):
        with patch.dict("sys.modules", {"tiktoken": None}):
            result = size.measure("rule\n\n" * 40)
        self.assertEqual(result["nonempty_lines"], 40)
        self.assertEqual(result["physical_lines"], 80)
        self.assertEqual(result["kind"], "estimate")
        self.assertEqual(result["ceiling_status"], "unknown")

    def test_measurement_reports_real_ceiling_failure(self):
        tokenizer = SimpleNamespace(__version__="test-double",
                                    get_encoding=lambda _: SimpleNamespace(encode=lambda _: range(901)))
        with patch.dict("sys.modules", {"tiktoken": tokenizer}):
            result = size.measure("example")
        self.assertEqual(result["kind"], "measured")
        self.assertEqual(result["tokens"], 901)
        self.assertEqual(result["ceiling_status"], "exceeded")
