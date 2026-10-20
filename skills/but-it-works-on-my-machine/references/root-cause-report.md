# Root Cause Report

If consuming upstream artifacts, make the first line (before the title):
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`
Name failed or unavailable re-derivations. Without upstream artifacts, omit the
envelope rather than inventing checks.

Keep every field, using short entries or explicit not-applicable reasons.
Combine tables when useful; a simple failure needs no lengthy investigation.

## Symptom and expected behavior

Observed failure, expected behavior and its source, scope, available inputs and
evidence locations. Attribute user reports; distinguish them from independent
observations. Identify load-bearing claims throughout the report.

## Environment and reproduction conditions

Relevant revision, runtime/dependencies, configuration, inputs/state, timing and
environment differences, as established. Missing conditions remain explicit.

## Reproduction attempts and results

| Attempt | Steps/actual command and inputs | Conditions | Expected result | Actual observed result and evidence | Limitation |
|---|---|---|---|---|---|

Separate target-failure reproduction from setup errors and reported observations.
If no reproduction exists, producing one is the task: state missing conditions,
attempts/results, remaining uncertainty, and the next useful diagnostic step.
No reproduction means no confirmed diagnosis or confirmed fix.

## Ranked hypotheses and discriminating tests

| Rank / hypothesis | Supporting evidence | Contradicting evidence or gaps | Cheapest useful discriminating test (proposed) | Outcomes distinguishing plausible causes | Status after actual checks |
|---|---|---|---|---|---|

Rank by evidence and explanatory fit, not familiarity. Use only plausible
hypotheses; no fixed count. Explain ranking changes. A test must distinguish
causes rather than repeat a symptom consistent with all explanations.

## Executed diagnostic checks

| Check / hypothesis | Actual command or method, environment/revision | Executed/passed, executed/failed, blocked, or unrun | Actual result and evidence location | Effect on hypothesis / next requirement |
|---|---|---|---|---|

Distinguish proposed tests from executed checks, and setup failures from target
failures. A never-attempted check has no invented output. Preserve failed and
blocked attempts. Explain unsafe or unavailable checks and their limits.

## Root-cause conclusion and confirming evidence

Cause or unresolved causal question; evidence classification; mechanism linking
the cause to the symptom; supporting and contradicting evidence; bounded scope.
Separate observations from causal conclusions. G4: **confirmed** requires the
confirming test and its actual observed result explaining the reproduced failure.
Name the check, conditions, result, and evidence location here (or reference the
executed-check row). Otherwise retain `inferred`; premises may be `assumed`,
and insufficient evidence is `unknown`. Directly supported claims name material
or checks without a label. These are evidence conventions, not execution statuses.

A successful fix alone does not establish causality. A passing changed-state
test without isolating the cause, stack trace, suspicious code, known pattern,
or upstream assertion cannot substitute for confirming evidence. State what
remains unconfirmed and what evidence could change the conclusion.

## Proposed fix, risks, and assumptions

Smallest remedy supported by the diagnosis, affected area, risks and assumptions.
With missing evidence, mark candidate remedies conditional or state that a fix
cannot yet be supported. Distinguish recommendations from any authorized work
actually performed. Diagnosis does not authorize fix implementation.

## Regression specification and handoff

Original symptom and conditions, expected behavior, relevant broken behavior the
regression must detect, proposed assertion/path, available reproduction and
confirming evidence, and execution gaps. Optional consumer: prove-it; no sibling
installation required. This is a specification, not implemented regression tests
or evidence that the skill ran. Consumers independently check that the confirming
test is real and the regression would detect the original failure.

## Gaps, uncertainty, and next steps

Missing reproduction material, unavailable checks, unresolved hypotheses and
load-bearing upstream claims, failed re-derivations, and next useful diagnostic
step. Re-surface every unresolved `assumed` premise the conclusion depends on;
re-check load-bearing `inferred`/`assumed` claims against available primary
evidence and record limitations. Name any specialized handoff and purpose without
claiming it ran. Keep deferred behavioral evaluations separate from structural
checks; structural passes do not prove diagnostic accuracy or G4 compliance.
