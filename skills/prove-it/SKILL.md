---
name: prove-it
description: |
  Establish inspectable evidence of software behavior in a Test Set.
  Use when: verifying behavior against acceptance criteria, including after implementation; establishing regression evidence after a fix; or capturing current behavior before refactoring.
  Do not use when: routine implementation merely involves an ordinary test command, the task is implementation planning, root-cause diagnosis, compatibility analysis, or a merge review without a behavioral verification task.
---

# Prove it

Lens: Evidence that behavior is correct.

Inputs: acceptance criteria identified by `AC-n` (verification), a Root Cause
Report or minimal failure evidence (regression), or current code
(characterization). The original request, implementation diff, existing tests,
Plan, and Contract Review are optional supporting inputs. Output: a Markdown
Test Set using [references/test-set.md](references/test-set.md).
Apply the engineering baseline when available. This bundle needs no sibling
skill or shared Interface Check/authorization reference.

## Workflow

1. Establish the behavioral question, scope, available sources, and mode. An
   ordinary test run alone does not warrant this skill or a full Test Set.
   Without criteria, use characterization rather than inventing intended
   behavior. A supplied failure with an expected/actual result can support
   regression without a Root Cause Report; name the missing report and do not
   invent a cause. If neither code nor execution is available, return a partial
   Test Set from supplied evidence, with needed sources and checks explicit.
2. Sanity-check inputs against the actual request, code, tests, and available
   data before plan conformance. Independently re-derive load-bearing upstream
   claims, including criteria fidelity, the reality of a confirming test,
   ownership/boundaries, and consumer completeness when relied on. Shared-origin
   reports are one source. A report saying a test passed is attributed evidence,
   not an independently observed run or confirmed root cause.
   Open an artifact consuming others with
   `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name unsuccessful re-derivations and their limits rather than filling this
   line with generic claims of verification.
3. Read `references/test-set.md`, relative to this installed skill directory,
   before producing the artifact. If unreadable, disclose the missing template
   and return a partial assessment preserving the fields listed below; do not
   borrow a sibling's references or claim complete packaging.
   Select checks whose assertions distinguish the target behavior from plausible
   broken behavior. Inspect setup, inputs, assertions, and relevant paths;
   a green test with a weak or unrelated assertion is insufficient. Prefer
   existing test conventions and focused checks over a new test framework.
4. Apply the relevant mode:
   - **Verification:** derive tests from each `AC-n`, independently checking
     criteria against the original request when available. Retain supplied IDs;
     expose omitted, contradictory, or untestable criteria as gaps. Map tests to
     criteria and report each as satisfied, failed, or unverified with actual
     evidence. Partial coverage leaves the criterion unverified. If the request
     is unavailable, disclose that criteria fidelity has not been established.
   - **Regression:** inspect the original symptom, repro conditions, expected
     result, and any confirming test. Establish that the test detects the
     original failure where feasible. Prefer a disposable, isolated comparison
     that runs the same test without the fix (original failure) and with it
     (pass), recording revisions, conditions, and results. An unrelated setup
     error is not reproduction. Never undo user work to manufacture a red run.
     If reproduction is unsafe, inaccessible, or impractical, explain why,
     record supported evidence and the missing comparison, and limit the
     regression conclusion. A passing fixed-state test alone does not confirm
     the original cause or demonstrate that it would have caught the failure.
   - **Characterization:** inspect current code and exercise relevant inputs
     and paths, recording exactly which behavior the tests capture. Assign
     local behavior identifiers for traceability; these are identifiers, not
     evidence labels. Separate observed execution from expectations inferred
     through inspection. List known bugs deliberately captured, with test IDs
     and evidence; do not silently fix them. Passing characterization establishes
     only captured current behavior, never correctness against unstated intent.
5. Write or propose scoped tests and execute supported checks where available.
   Record actual commands, environment/revision, test selection, results, and
   supporting output or durable evidence locations. Distinguish proposed tests,
   written tests, and executed tests. Separate executed/passed, executed/failed,
   blocked, and unrun checks; distinguish assertion failures from runner/setup
   failures. For blocked checks state the blocker and next requirement. Missing
   execution does not prevent a supported partial Test Set, but prevents claims
   that those checks passed. Do not invent commands, results, coverage, or
   observed failures. Builds, compilation, plan agreement, upstream assurances,
   and characterization passes alone do not establish intended correctness.
6. Return a proportional Test Set with all required fields: mode/scope, inputs
   and evidence, tests and expectations, traceability, execution evidence,
   gaps/uncertainties, intentionally captured known bugs, and bounded conclusion.
   State the load-bearing claims and what evidence could change the conclusion.
   Directly supported claims name inspected material or actual results;
   `inferred` means a conclusion from observed facts, `assumed` an unverified
   premise, and `unknown` insufficient evidence. Re-check load-bearing inferred
   or assumed claims where possible; unresolved assumptions reappear in Gaps.
   If an upstream load-bearing claim cannot be re-derived, mark the dependent
   conclusion `inferred` and name the claim; missing facts stay `unknown`.

## Boundaries and gates

Own behavioral verification evidence. Leave implementation planning to
think-before-you-commit, root-cause diagnosis to but-it-works-on-my-machine,
consumer-contract analysis to read-the-contract, and findings/merge recommendations
to trust-issues. These are optional handoffs, never installation dependencies.
When needed instructions are unavailable, name the limitation without inventing
their procedures or claiming those assessments ran. Continue supported checks.

For a refactor handoff, name the paths captured and gaps. G1 belongs to the
refactor workflow: sufficient current-behavior evidence is needed for every path
touched; named existing tests, compiler/type guarantees for purely mechanical
renames/moves, snapshots, characterization tests, or other stated reliable
verification may supply it. Do not impose new tests when sufficient evidence
already exists, or claim this Test Set covers unexamined paths.

G6/G7: restricted execution and compatibility exceptions require human authority,
with no escape. Follow actual host permissions and available baseline authority
rules. A request to verify does not authorize destructive rollback, production
operations, or external effects; keep checks local/isolated where possible and
defer restricted execution pending the required human authorization.

Downstream consumers receive traceability, evidence, and Gaps. They must
independently establish that the tests would fail for relevant broken behavior;
this artifact's confidence does not replace that check. No merge verdict is issued.
