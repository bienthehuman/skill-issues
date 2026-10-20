# Test Set

If consuming upstream artifacts, make the first line (before the title):
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`
Name failed or unavailable re-derivations explicitly. No upstream artifacts:
omit the envelope rather than inventing checks.

Keep every field, using short entries or explicit not-applicable reasons where
appropriate. Expand only material uncertainty; tables may be combined.

## Mode and scope

Verification / regression / characterization; behavioral question, target
revision/environment, paths and limits. Separate modes if more than one applies.
Characterization captures what code does, not what it should do.

## Inputs and evidence

Original request, AC-n criteria, Root Cause Report/failure evidence, current code,
existing tests, and optional artifacts actually available, with locations.
Identify missing inputs and standalone fallback used. Name load-bearing claims,
their independent checks, and unresolved upstream claims. Attribute reported
results; do not present them as observed execution.

## Tests and expectations

| Test ID and location | Inputs/setup and path exercised | Expected behavior or captured characterization | Assertion and relevant broken behavior it detects | Proposed / written / executed |
|---|---|---|---|---|

For characterization, distinguish observations from inferred expectations.
For regression, include the original symptom, reproduction conditions, and
expected/actual result; a cause remains unsupported until independently shown.

## Traceability and outcomes

| AC-n / root cause or original failure / characterization behavior ID | Source and behavioral statement | Test IDs | Outcome and supporting evidence | Limits |
|---|---|---|---|---|

Verification: each criterion is satisfied, failed, or unverified; partial coverage
is unverified. State any mismatch with the request. Regression: separately state
original-failure reproduction and fixed-state evidence. Characterization: state
only behavior actually captured, separating intended behavior when known.
Identifiers and execution statuses are not new evidence labels.

## Execution evidence

| Check/test IDs | Actual command, working directory, revision/environment | Executed/passed, executed/failed, blocked, or unrun | Actual result and output/evidence location | Limitation or next requirement |
|---|---|---|---|---|

Record commands only as actually run; mark suggested commands as proposed/unrun.
Differentiate assertion failures from setup/runner errors. A blocked attempt
records its actual error; a never-attempted check has no invented output.
Regression comparisons name both revisions/conditions, whether the same test ran,
the original failure without the fix, and the result with it. If comparison was
not feasible or safe, say why and what remains unverified. Coverage measurements
appear only with an actual measurement and its scope.

## Gaps and uncertainties

Missing paths, assertions, requirements, data, environment, execution, or
reproduction; unresolved upstream claims; load-bearing assumptions and how to
resolve them. Use `inferred`, `assumed`, and `unknown` as defined in SKILL.md;
directly supported claims still name their material/checks. Re-surface every
unresolved assumption the conclusion depends on. Include evidence that would
change the conclusion and next checks. Unrun behavioral evaluations stay unrun.

## Known bugs intentionally captured

Characterization bug, source evidence, test IDs, and why retained. If none are
identified in the inspected scope, state that bounded observation; it does not
mean the code is bug-free. Other modes may mark this field not applicable.

## Conclusion and handoff

Bounded behavioral conclusion with its load-bearing evidence and limitations.
No build, compilation, plan conformance, reported pass, or characterization pass
alone proves intended correctness. Name captured paths for refactor consumers.
Downstream consumers independently check that tests detect relevant broken
behavior. Identify needed diagnosis, planning, contract analysis, or review
without claiming it completed or requiring sibling installation.
