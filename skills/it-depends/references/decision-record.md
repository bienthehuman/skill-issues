# Decision Record

If consuming upstream artifacts, place this before the title:
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`.
Name failed/unavailable re-derivations and dependent limitations. Omit the envelope
when no artifacts were consumed. Keep this plain Markdown and proportional to
the decision; short fields are sufficient for a simple choice.

## Decision question and context

Actual engineering choice, intended outcome, original request, and relevant
implementation/operational context. Distinguish a recommendation from an
established human decision.

## Requirements, constraints, and assumptions

Relevant acceptance criteria (retain upstream AC-n when supplied), non-goals,
project conventions, operational constraints, and their sources. Without
Requirements derive only minimal supported criteria; mark unverified premises
`assumed`. Identify assumptions that could change the choice; do not invent limits.

## Alternatives and tradeoffs

Compare at least two genuine alternatives that plausibly meet the objective under
known constraints. Use consistent decision-relevant criteria and evidence for
each option, including its strengths, disadvantages, and feasibility limits.

| Criterion and why it matters | Option A: viable approach | Option B: viable approach | Supporting evidence and limits |
|---|---|---|---|

Add options only when meaningful. Consider project fit, operational constraints,
and dependency or abstraction costs explicitly. Other factors need attention only
when relevant. No straw-man alternatives, arbitrary scores, invented benchmarks,
or unsupported performance claims. If meaningful comparison is unavailable,
explain the gap rather than inventing options or a choice.

## Chosen or provisionally preferred approach

Preferred option and rationale against the established criteria, with concrete
benefits and accepted costs. State provisional or unresolved where evidence
cannot support a choice, including which conclusions depend on missing facts.
This is a recommendation, not execution authorization.

## Rejected alternatives and reasons

For each meaningful rejected option, explain what it does better, why its costs
outweigh those benefits in this context, and the evidence supporting rejection.
If unresolved, retain candidates without pretending they have been rejected.

## Reversibility and revisit conditions

Reversible or `one-way` (undo is impractical), with reasons and relevant migration
or recovery implications. Name evidence, assumption changes, or future conditions
that would reverse the choice or require reconsideration. Do not prescribe an
implementation sequence or imply rollback has been tested.

## Evidence and verification limitations

| Load-bearing claim | Source/provenance and actual checks | Evidence classification and limits | Dependent option or conclusion |
|---|---|---|---|

Untagged findings require directly inspected support; attribute user reports.
`inferred` means concluded from observed facts; `assumed` means an unverified
premise; `unknown` means insufficient evidence with no value offered. Re-check
load-bearing inferred/assumed claims. Shared-origin artifacts count as one source.
Name failed re-derivations and unavailable repository access or other sources.
Dependent conclusions not independently re-derived remain `inferred` and name
the inherited claim; do not claim verification based on artifact agreement.

## Open questions and next evidence

Every assumption relied on, unresolved question, and consequential evidence gap,
linked to the affected recommendation. Name the cheapest useful investigation
that could distinguish options, its decision-changing result, or needed human
clarification. Preserve uncertainty rather than forcing confidence.

## Boundaries and handoff

Supported scope and remaining limitations. Optional consumers receive chosen and
rejected approaches, constraints, and reversal conditions; they independently
check that constraints still hold. Interface concerns are advisory only, not a
canonical Interface Check or formal Contract Review. No automatic pipeline,
Implementation Plan, execution, or behavioral reliability claim.
