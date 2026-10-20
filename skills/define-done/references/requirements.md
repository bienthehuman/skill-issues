# Requirements

If consuming upstream artifacts, place this before the title:
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`
Name failed/unavailable re-derivations and limits; omit if none were consumed.
Keep fields concise, with explicit none or unknown where appropriate. This is
plain Markdown, not a structured YAML artifact or automatic validator input.

## Objective and scope

Original request, intended outcome, available context, and feature boundary.
State what is established and what remains partial.

## Established requirements

User-attributed or directly supported requirements and source references.
Keep inferred requirements and provisional premises distinguishable from
established intent. Separate optional improvements from requirements.

## Acceptance criteria

| ID | Conditions/inputs and observable expected behavior | Source or explicit assumption | Evidence classification | Verification basis | Dependent open question |
|---|---|---|---|---|---|
| AC-1 | Independently verifiable outcome supported by the request | Request passage, primary source, or named premise | Attributed/direct, `inferred`, or `assumed` | Check that could distinguish success from failure; not an executed result | Question reference or none |

Use stable `AC-n` identifiers within this artifact and retain them during revisions;
do not renumber or reuse an ID for different behavior. Every criterion needs
traceability to intent: testability alone is insufficient. Mark provisional
criteria `assumed`; identify consequential unresolved dependencies explicitly.
Do not invent an outcome for an `unknown`; document the gap below. Criteria
describe behavior, not implementation tasks. Their existence does not prove
they are satisfied.

## Constraints

Established limits and their sources; label inferred or assumed constraints.
Do not introduce architectural or business rules without support.

## Non-goals

Explicit exclusions and source, with proposed exclusions labeled as assumptions.

## Assumptions and evidence

| Load-bearing claim or premise | Source/provenance and actual checks | Classification and limits | Affected AC-n or field |
|---|---|---|---|

Untagged findings require directly inspected support; attribute user reports
without implying independent verification. `inferred` means concluded from
observed facts; `assumed` means an unverified premise; `unknown` means insufficient
evidence with no value offered. Re-check load-bearing inferred/assumed claims
where possible. Shared-origin reports are one source. Identify claims downstream
consumers must independently re-derive, including failed upstream re-derivations.

## Open questions

| Question | Competing interpretations and implications | Consequence and affected AC-n/fields | Working assumption, if defensible | Human clarification or primary evidence needed |
|---|---|---|---|---|

Include every assumption relied on and consequential unresolved decision.
Security, compatibility, data integrity, user obligations, and significant
behavior remain visibly unresolved where unsupported. Provisional `assumed`
criteria do not settle these decisions. Continue supported criteria independently;
do not block the entire artifact or silently choose an interpretation.

## Boundaries, limitations, and handoff

State supported coverage, missing context, contradictory intent, unestablished
criteria, and what would resolve them. Preserve AC-n, constraints, and non-goals
for optional consumers, who independently check testability and fidelity to the
original request. Requirements are usable without downstream skills. They are
not Prompt Refinement, a Decision Record, an Implementation Plan, a Test Set, or
Review Findings. No automatic pipeline, implementation, or verification claim.
