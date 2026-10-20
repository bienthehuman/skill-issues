"""Prepare one isolated integration run; never modify global agent configuration."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = "think-before-you-commit"


def prepare(destination, agent, case):
    destination = Path(destination).resolve()
    if destination.exists():
        raise ValueError("Destination must not exist; use a fresh directory for every run")
    destination.mkdir(parents=True)
    files = {
        "routes/api.php": "<?php\nRoute::get('/orders/{order}', [OrderController::class, 'show']);\n",
        "app/Http/Controllers/OrderController.php": "<?php\nclass OrderController {\n public function show(Order $order) {\n  $resource = new OrderResource($order);\n  return $resource->response()->setStatusCode(200);\n }\n}\n",
        "app/Http/Resources/OrderResource.php": "<?php\nclass OrderResource {\n public function toArray($request) {\n  return ['id' => $this->id, 'customer_name' => $this->customer_name];\n }\n}\n",
        "app/Http/Requests/ShowOrderRequest.php": "<?php\nclass ShowOrderRequest { public function rules() { return ['id' => 'integer|min:1']; } }\n",
        "resources/js/hooks/useOrder.ts": "import { useEffect, useState } from 'react';\nexport type Order = { id: number; customer_name: string };\nexport function useOrder(id: number) {\n const [name, setName] = useState('');\n useEffect(() => { fetch(`/api/orders/${id}`).then(r => r.json()).then(r => setName(r.data.customer_name)); }, [id]);\n return name;\n}\n",
        "FIXTURE.md": "Closed-world static inspection fixture, not a runnable Laravel installation. All application sources are included. No generated API types, external consumers, database writes, jobs, caches, settings, CLI, auth, log/metric consumers or import/export formats exist in this fixture. Do not install dependencies.\n",
    }
    if case == "B":
        files["app/Http/Controllers/OrderController.php"] = "<?php\nclass OrderController {\n public function __construct(private OrderPresentationService $presenter) {}\n public function show(Order $order) {\n  $resource = new OrderResource($order);\n  return $resource->response()->setStatusCode(200);\n }\n}\n"
        files["app/Services/OrderPresentationService.php"] = "<?php\nclass OrderPresentationService {\n public function present(Order $order): OrderResource {\n  return new OrderResource($order);\n }\n}\n"
    for name, content in files.items():
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    base = ".agents/skills" if agent == "codex" else ".claude/skills"
    installed = destination / base / SKILL
    shutil.copytree(ROOT / "skills" / SKILL, installed)
    subprocess.run([sys.executable, str(ROOT / "scripts/install-baseline"), "--agent", agent,
                    "--project", str(destination), "--apply"], check=True, capture_output=True)
    if case == "C":
        (installed / "references/interface-check.md").unlink()
    approach = ("Rename the OrderResource response field customer_name to customerName and update its React consumer in the same change."
                if case in ("A", "C") else
                "Delegate OrderResource construction from OrderController::show to the existing injected OrderPresentationService::present method across the controller/service boundary. Keep all existing public signatures and injection wiring, the API resource, validation rules, response shape, error format and status code unchanged.")
    prompt = ("Use $think-before-you-commit. The approach is settled: " + approach +
              " Inspect this fixture and produce the Implementation Plan only. Do not implement it.")
    (destination / "prompt.txt").write_text(prompt + "\n", encoding="utf-8")
    manifest = {"agent": agent, "case": case, "skill_path": str(installed),
                "fixture_sha256": {name: hashlib.sha256((destination / name).read_bytes()).hexdigest() for name in files},
                "skill_sha256": {str(p.relative_to(installed)): hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in installed.rglob("*") if p.is_file()},
                "missing_reference": case == "C"}
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--agent", choices=("codex", "claude"), required=True)
    parser.add_argument("--case", choices=("A", "B", "C"), required=True)
    args = parser.parse_args()
    try:
        print(prepare(args.destination, args.agent, args.case))
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + "\n")
