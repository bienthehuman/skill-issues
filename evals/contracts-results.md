# Contract Review evaluation — 2026-10-20

Implemented `read-the-contract` from SPEC 3.5–3.6, 6–8, 9.1/9.1.1 and the
artifact exchange contract. Both shared references are bundled byte-for-byte
through existing synchronization. SPEC, BASELINE, and shared references remain
unchanged. The author explicitly permitted Wave 1 development following successful
Codex-only validation; this is not full cross-agent validation.

## Method and evidence

Fresh native Codex sessions, static Laravel/React fixtures, read-only sandbox,
approval `never`, no reminder prompts. Standalone cases installed only
read-the-contract. Only after standalone review and the fresh unknown-consumer
repair passed was the planning handoff updated and two-skill integration started.
No evaluator was given expected classifications or author conclusions. The diff
case deliberately supplied a false upstream plan as test input.

The existing Windows capture runner now accepts a fixture preparer and expected
skill inventory, preserving its original defaults. Each inventory matched its
expected installed skills. Global AGENTS.md instructions remain present: these
are independent sessions, not complete instruction isolation. Claude Code was
not evaluated. Static fixtures establish inspection behavior, not live Laravel,
Redis, deployment, or browser behavior.

Full JSONL, final artifacts, inventories, manifests, commands, CLI version,
stderr, and before/after hashes remain locally in `contract-runs/<run-id>/`.
This generated capture directory is ignored, matching the existing Windows
capture policy. The portable reviewed evidence is in `contract-evidence/`.
Event IDs below refer to completed command events in each run's trace; inspect
actual output, not exit code alone (combined PowerShell reads can exit 0 after
one missing-file error). Classification follows the reads in all listed runs.

## Targeted results

| Run | Outcome | Observed evidence |
|---|---|---|
| contract-http-1 | Pass | Interface/template read item_2; inventory/source/frontend searches item_3–4. Identifies old tabs/new backend and reverse rollback break; 24-hour window anchored to last old-asset delivery; staged migration and error semantics. |
| contract-stored-3 | Pass | Interface/template item_2; source/queue/frontend searches item_3. Surfaces 4/5 affected, existing JSON/new worker and new JSON/old worker distinguished; 48-hour window after final old dispatch plus retry/replay investigation. |
| contract-unknown-2 | Pass after repair | Interface/template item_2; partial-source searches item_3. Explicit uncertain HTTP consumer coverage, conditional per-consumer claims, unknown support duration, broader investigations; no invented consumers. Missing Git metadata is disclosed. |
| contract-missing-interface-1 | Pass | item_2 output contains failed bundle access; item_3 confirms missing file; sources item_4. All nine uncertain, disclosed partial review, restoration required; no checklist reconstructed. Preliminary source comparisons remain conditional. |
| contract-missing-authority-1 | Pass | item_2 output includes successful Interface Check and failed authorization access; sources/searches item_3. Baseline fallback disclosed, upstream approval rejected as authority, exception proposed with impact/duration/conditions/alternatives and no grant. |
| contract-negative-1 | Pass | Interface/template item_2; sources/frontend item_3. All unaffected with evidence; no collapse across module boundary, no migration/exception, eventual diff check required. |
| contract-diff-2 | Pass | Interface/template item_2; sources/diff/frontend searches item_3–4. Re-derives affected HTTP and exported-type contracts, explicitly rejects false upstream plan, distinguishes old/new consumers and rollback, requires a bounded migration. |
| contract-integration-1 | Pass | Planning template, Interface Check and authorization item_2; actual sources/frontend searches item_3. Affected HTTP/exported type; scoped pending handoffs with evidence/consumers/questions and required Contract Review fields. No completed-review claim or implementation. |
| contract-integration-negative-1 | Pass | Planning/reference reads item_2; sources/frontend item_3. Full nine-surface unaffected scan, no contract handoff, no collapse or implementation. |

All completed fixtures remained unchanged; inventory checks passed and zero
extra human prompts were sent inside evaluated sessions. These are targeted
observations, not nondeterminism guarantees or completion of the full E1/E2/E3/E5
corpus. Implicit routing is not established by explicitly invoked standalone
cases. Integration tests establish the plan handoff contract; they do not pretend
the planner ran the downstream review.

## Repairs and retained limitations

- `contract-stored-1` exposed contradictory inherited fixture prose claiming no
  jobs existed. The agent correctly challenged it. Corrected the fixture and
  retained the original run; it is not the clean stored-state acceptance run.
- `contract-unknown-1` kept consumers unknown but omitted an explicit evidence
  label on HTTP consumer coverage. Logged as `wrong`, clarified that producer
  evidence cannot establish consumer coverage, and reran fresh as unknown-2.
- `contract-diff-1` and `contract-stored-2` overlapped that author edit and report
  `canonical_unchanged=false`; their installed fixtures stayed unchanged. Retained
  as historical behavior evidence, excluded from clean integrity acceptance;
  reran against stable canonical skills as diff-2 and stored-3.
- Main suite: 18 tests pass, including both agents' packaging, deliberate missing
  bundles, standalone/two-skill inventory, fresh destination refusal, preservation,
  canonical provenance, and drift checks. These are structural results.
- Reference check: two skills, zero drift. Optional skill-creator quick validator
  could not start because bundled Python lacks PyYAML; no dependency was added.
- Initial sandboxed test invocation failed on temporary-directory permissions;
  the approved rerun passed. No evaluation sandbox or authority gate was weakened.

Claude Code evaluation and complete instruction isolation remain outstanding and
must be completed before claiming full cross-agent compatibility. Full Wave 1
release criteria remain open.
