# Milestone 1 results — 2026-10-20

## Native Windows follow-up (historical summary)

The locally retained report `evals/windows-20261020/REPORT.md`, dated 2026-10-20,
reports **9/9 corrected-fixture Codex reference-loading checks passed** under
SPEC 11.0. The original B1 control introduced a public constructor dependency,
legitimately affecting surface 2; a corrected fixture and fresh rerun replaced it
in the valid matrix. The original attempt remains retained, not reclassified.

This is a tracked summary of that historical report, not a new evaluation or a
portable transcript archive. The detailed report, configuration records and raw
captures are retained only locally in ignored `evals/windows-20261020/` and are
unavailable in a fresh checkout. Global AGENTS instructions remained visible;
complete instruction isolation was not achieved. Claude Code was deferred and
not executed; cross-agent validation and the full Milestone 1 criteria remain unmet.

The remaining sections preserve the original WSL attempt and its limitations;
their blocked results are not results from the later native Windows matrix.

## Automated checks

Passed: all 15 foundation tests and 2 new structural tests on WSL Python 3.12.3.
Reference synchronization generated two bundles; check-references passed for one
skill with zero drift. Foundation tests verify canonical SPEC hash, baseline,
synchronization refusal/idempotence, installation preservation and isolated paths.
New tests cover standalone packaging for both agents/all cases, deliberate missing
reference isolation, fresh-destination refusal, local reference links, and eleven
artifact fields. These do not prove behavioral quality or generated-plan conformance.

## Behavioral matrix

| Agent | A1 | A2 | A3 | B1 | B2 | B3 | C1 | C2 | C3 |
|---|---|---|---|---|---|---|---|---|---|
| Codex | blocked (attempted) | blocked | blocked | blocked | blocked | blocked | blocked | blocked | blocked |
| Claude Code | blocked | blocked | blocked | blocked | blocked | blocked | blocked | blocked | blocked |

Only Codex A1 was attempted. The other 17 sessions were **not executed**, with
blocked status reflecting unavailable prerequisites, not behavioral outcomes.
No behavioral run passed; no successful behavior has been simulated.

Codex CLI: 0.163.0-alpha.10.2 on Windows. Neither CLI was found inside WSL;
Claude Code was not found on Windows PATH. Windows Codex can launch from the
WSL UNC fixture, but its read-only execution policy rejected both PowerShell file
reads and a bash pwd attempt. Session exited 0 after producing a partial plan;
exit 0 is not a pass. Other cases were not repeated against the same execution
blocker. Global instruction/skill isolation also remains unverified; ignoring
user config alone does not establish a clean inventory.

## Attempted Codex A1

Disposable project: `/tmp/skill-issues-m1-codex-A1` in Ubuntu WSL, accessed as
`//wsl.localhost/Ubuntu/tmp/skill-issues-m1-codex-A1` from Windows. One skill plus
Codex baseline was installed; generated manifest retained under `evals/traces/`.
Prompt: “Use $think-before-you-commit. The approach is settled: rename the
OrderResource response field customer_name to customerName and update its React
consumer in the same change. Inspect this fixture and produce the Implementation
Plan only. Do not implement it.”

Command flags: `codex exec --ignore-user-config --ignore-rules --ephemeral
--skip-git-repo-check --sandbox read-only --json -C <fixture> <prompt>`.
No model override. New session ID: `01a157df-996a-7f70-ac5f-7d81a50fd5c8`.
An initial launcher attempt used a malformed UNC path and failed before a session
started; corrected once. No reminder/correction prompts were sent to the agent.

| Criterion | Outcome | Observed evidence |
|---|---|---|
| Requested activation | passed | item_0 says it will use think-before-you-commit |
| Interface reference actually read | blocked | read command rejected by policy |
| Read before classification | blocked | no successful read; fallback only |
| Expected A classification | blocked | all nine uncertain instead of an inspected A finding |
| Frontend evidence | blocked | no source inspection possible |
| Required handoff | observed, partial | final names scoped read-the-contract reviews for unresolved surfaces |
| Additional prompting | passed | zero extra prompts within session |
| Missing-reference fallback | observed under access failure | final lists 1–9 uncertain without recreating names; not a Case C pass |
| Authorization reference access | blocked | same read command rejected; baseline fallback disclosed |
| Plan only | observed | final reports no edits/tests; no successful mutation commands in available trace |

Full streamed output was returned through the parent tool responses rather than
redirected to a repository file. `traces/codex-A1-excerpts.txt` retains selected
exact excerpts, not a complete transcript. This audit limitation is another reason
not to claim a pass. Reproduce using the documented redirected command to retain
full JSONL/stderr. The disposable fixture still exists; canonical references were
never removed. Case C structural fixture copies were temporary and cleaned up;
no behavioral C installation requires restoration.

## Completion and limitations

Implemented only think-before-you-commit. No specification changes, sibling
placeholders, commits, global installs, or restricted operations. The negative
control uses an explicit boundary-crossing service delegation to satisfy the
stakes trigger while keeping HTTP unchanged; it must use the full scan.

Human intervention: WSL filesystem/command escalation was required by the parent
sandbox; no in-session behavioral reminders. A corrected launcher path was needed.
The skill-creator quick validator passed ("Skill is valid!"). Final git diff --check passed.

Remaining: an environment with working read tools and verified isolated agent
inventories, Claude Code availability, all 18 fresh behavioral runs with full
traces, and manual criterion-by-criterion review. Implicit routing and broader
Wave 1 authority/cost evaluations are not executed here.

**Milestone 1 exit criteria are not met.**
