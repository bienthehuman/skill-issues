---
name: but-it-works-on-my-machine
description: |
  Diagnose an existing failure and produce an evidence-backed Root Cause Report.
  Use when: observed behavior contradicts expected behavior; a reproducible defect, unexpected error, or regression needs diagnosis; or the user asks why an existing implementation fails.
  Do not use when: implementing a new feature, resolving missing or undefined requirements, investigating slowness or performance, verifying behavior without an existing failure, or implementing an agreed fix whose root cause is already established. Error handling or debugging-related code in a diff alone is not a trigger.
---

# But it works on my machine

Lens: Explain a failure that already exists.

Inputs: a symptom, expected behavior, logs/stack traces, reproduction instructions,
environment details, or relevant code; a Codebase Map and other artifacts are
optional. Output: a Markdown Root Cause Report using
[references/root-cause-report.md](references/root-cause-report.md).
Apply the engineering baseline when available. No sibling skill or shared
reference bundle is required.

## Investigation

1. Establish the observed symptom, expected behavior and its source, scope, and
   relevant environment/revision. Attribute user-reported observations rather
   than claiming independent verification. Distinguish an existing failure from
   an undefined requirement. Identify reproduction conditions such as inputs,
   configuration, dependency versions, state, timing, and environment differences
   only where relevant; do not demand an exhaustive environment inventory.
2. Sanity-check supplied maps, reports, plans, and Test Sets against primary
   evidence available for this failure. Independently re-derive load-bearing
   claims, including relevant paths, ownership/boundaries, and whether a test
   actually detects the failure. Shared-origin artifacts are one source.
   If consuming artifacts, open the report with
   `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name failed or unavailable re-derivations. An upstream assertion that a cause
   is confirmed does not satisfy G4.
3. Obtain or construct the smallest useful reproduction where feasible. Record
   actual steps/commands, inputs, expected and observed results, and conditions.
   Distinguish the target failure from an unrelated setup error. If reproduction
   is unavailable, producing a reproduction is the task: record observations,
   missing conditions, attempts and results, and the next useful reproduction or
   diagnostic step. No reproduction means no confirmed diagnosis or guessed fix.
   Without repository access, work from supplied evidence and identify specific
   code, logs, inputs, or environment material required; return a partial report.
4. Inspect the minimum relevant code, configuration, logs, and execution paths.
   Form candidate hypotheses supported by evidence. Rank plausible hypotheses
   by supporting/contradicting evidence and ability to explain the symptom,
   not by familiarity or how common a bug seems. Do not impose fixed hypothesis
   counts or manufacture alternatives when one explanation is already established.
5. For each hypothesis, identify the cheapest useful discriminating test and
   the outcomes that would distinguish plausible causes. Repeating the symptom
   is insufficient if every explanation predicts it. Prefer checks that reduce
   uncertainty efficiently; avoid speculative rewrites or changing several
   components at once to see whether the symptom disappears.
6. Execute safe, relevant diagnostic checks where possible. Keep proposed tests
   separate from executed checks. Record actual commands/checks, conditions,
   results and evidence locations; distinguish executed/passed, executed/failed,
   blocked, and unrun checks, including setup failures. Update, reject, or retain
   hypotheses from actual results and explain changes in ranking. If a check is
   unsafe or the environment unavailable, disclose why and keep the cause
   unconfirmed. Stop expanding when evidence explains the scoped failure or
   further progress requires unavailable material; name the next useful step.
7. Apply **G4: confirming test before naming root cause**. Label a cause
   **confirmed** only when the report shows the confirming test and its actual
   observed result explaining the reproduced failure. Otherwise the proposed
   cause stays `inferred`; unverified premises are `assumed`, and insufficient
   evidence is `unknown`. A plausible explanation, stack-trace line, suspicious
   code, known bug pattern, or upstream assurance does not confirm causality.
   A successful fix alone is not sufficient: a passing test after a change that
   did not isolate the cause does not establish it. Successful remediation and
   causal confirmation are separate claims. G4 permits an explicitly unconfirmed
   report; it does not require speculative changes to achieve confirmation.
8. Read `references/root-cause-report.md`, relative to this installed skill,
   before producing the report. If unreadable, disclose the missing template
   and return a partial report retaining the required fields below; do not borrow
   sibling references or claim complete packaging. Include symptom/expectation,
   environment/reproduction conditions, reproduction attempts/results, ranked
   hypotheses/evidence/discriminating tests, diagnostic checks/results, cause and
   evidence classification, confirming test/result if confirmed, proposed fix
   with risks/assumptions, regression specification, and gaps/next steps.
   Keep entries short for straightforward failures; combine tables if useful.

## Evidence and conclusion

Separate diagnostic observations from causal conclusions. Directly supported
claims name actual inspected material or checks without a label; `inferred`
means concluded from observed facts, `assumed` an unverified premise, and
`unknown` insufficient evidence. Re-check every load-bearing inferred or assumed
claim where possible. Re-surface unresolved assumptions in gaps. When an upstream
load-bearing claim cannot be re-derived, mark the dependent conclusion `inferred`
and name that claim; missing facts stay `unknown`. State remaining uncertainty
and evidence that would change the conclusion. Never invent reproduction,
execution, or a confirmed fix.

## Scope and handoffs

Own diagnosis, not fix implementation or regression-test implementation. Propose
the smallest supported fix, its risks and assumptions; when evidence is missing,
make any candidate remedy explicitly conditional rather than guessing a fix.
Do not modify unrelated code or silently expand diagnosis into implementation.
Follow host permissions and available baseline authority rules for diagnostic
checks. G6/G7 human-authority gates have no escape; debugging and a suggested
fix do not authorize restricted execution or compatibility exceptions.

Leave task-relevant orientation to you-are-here, performance analysis to
are-we-there-yet, behavioral verification and regression tests to prove-it,
settled implementation planning to think-before-you-commit, consumer compatibility
to read-the-contract, and implementation review/findings to trust-issues.
Explain a warranted handoff and its purpose without triggering an entire pipeline
or claiming another skill ran. If needed skill instructions are unavailable,
name the limitation without reconstructing their procedures.

Provide a regression specification for optional prove-it consumption: original
symptom, reproduction conditions, expected behavior, relevant broken behavior
the test must detect, and available confirming evidence and gaps. Downstream
consumers independently check that the confirming test is real and tests detect
the original failure. Missing siblings never block supported diagnosis.
