If upstream artifacts were consumed, make this the first line, before the title:
`Upstream: <names> | Re-derived: <claims and actual source checks>`

# Implementation Plan

## 1. Objective and intended behavior
<Task, settled approach, AC-n criteria; missing criteria tagged assumed.>

## 2. Relevant existing implementation
<Inspected paths, behavior, callers and boundaries; name checks.>

## 3. Assumptions and unresolved questions
<inferred/assumed/unknown claims, missing inputs and how to resolve them.>

## 4. Ordered implementation steps
<Prefer one ordered table combining the fields below when appropriate; otherwise
use separate fields. Record each item once and reference its step ID elsewhere.>

| Step / prerequisite | Files/components and reason | AC-n | Check/test and expected observable result | Reversal / rollback details and limits |
|---|---|---|---|---|

## 5. Affected files and components
<Reference step-table rows when files/components and reasons are already recorded;
list only additional affected components here.>

## 6. Verification for each step
<Reference the per-step checks and expected results in the combined table when
used; record coverage gaps and unrun checks here without repeating those rows.>

## 7. Interface Check
<Read interface-check.md immediately before classifying. Use its nine-surface scan with status and evidence. Expand affected/uncertain surfaces and name scoped read-the-contract handoffs. Collapse only under all four conditions, never inferred. If unavailable: surfaces 1-9 uncertain; disclose failure; do not reconstruct the checklist or claim compatibility.>

## 8. Risks and tradeoffs
<Risks, alternatives considered and evidence that would change the plan.>

## 9. Reversibility and one-way steps
<Reference per-step rollback details when recorded above; retain recovery
prerequisites and cross-step rollback limits here. Mark impractical or irreversible
undo one-way.>

## 10. Restricted steps (require go-ahead at execution; plan approval does not cover them)
<Read authorization.md before identifying operations. Separate restricted actions from ordinary work: action/command, target/environment, impact, prerequisites, reversibility. State absence if none planned. Disclose missing reference and baseline fallback.>

## 11. Out of scope
<Explicit exclusions. Stop after the plan.>
