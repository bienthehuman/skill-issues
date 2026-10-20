# Codebase Map

If consuming upstream artifacts, place this before the title:
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`
Name failed/unavailable re-derivations; omit the envelope if none were consumed.
Keep every field, using brief entries or explicit not-applicable reasons. Combine
tables when useful; scale detail to the engineering question.

## Engineering question and scope

Question, available repository/revision or supplied sources, investigated paths,
excluded areas, and limits. State whether orientation is partial, what evidence
was sufficient to stop, or which unavailable evidence prevented completion.
This is task-scoped coverage, not an exhaustive repository inventory.

## Entry points

| Relevant entry point and path/symbol | Trigger and conditions | Supporting evidence and limits |
|---|---|---|

Distinguish declared routes/schedules/wiring from observed execution.

## Modules and responsibilities

| Module and navigable reference | Observed behavior | Responsibility/ownership conclusion and supporting evidence |
|---|---|---|

Execution location alone does not establish ownership or exclusive responsibility.
Label inferred architectural conclusions rather than presenting them as facts.

## Execution and data flow

Trace the meaningful path from entry through relevant modules to outputs or
effects, with paths/symbols, transformations, conditions, and evidence for links.
Distinguish statically defined paths from observed runtime behavior. Mark missing
links explicitly instead of drawing an uninterrupted guessed path.

## State ownership and persistence

| State and location | Observed readers/writers and lifecycle | Ownership claim and evidence | Persistence interaction and database/connection if established |
|---|---|---|---|

A writer is not automatically the owner. Distinguish transient and persisted
state where relevant; unknown ownership or storage stays explicit.

## Module and integration boundaries

| Relevant boundary and endpoints | What crosses it and dependencies | Evidence and limitations |
|---|---|---|

Document relevant relationships; this is not an Interface Check or compatibility
verdict. Distinguish observed wiring from inferred module boundaries.

## Evidence and load-bearing claims

| Claim relied on | Supporting paths/symbols, inspected material, or actual checks | Evidential limits and independent re-check needed |
|---|---|---|

Identify entry points, module/service ownership, state ownership, boundaries, and
significant data-flow relationships on which the answer depends. Use the canonical
conventions: untagged findings require direct supporting material; `inferred`
means a conclusion from observed facts; `assumed` an unverified premise; `unknown`
insufficient evidence. Attribute supplied reports. File inspection establishes
contents, not runtime execution or exclusive ownership. Record actual checks
only; re-check load-bearing inferred/assumed claims where possible.

## Unknowns, limitations, and follow-up questions

Missing evidence, unresolved relationships, unsupported conclusions, failed
upstream re-derivations, and every assumption a conclusion depends on. For each
material gap, name the source or check needed and the conclusion it limits.
Without repository access, identify the requested tree/key files and why needed.

## Bounded conclusion and handoff

Answer the orientation question to the extent supported, with stopping reason
and remaining uncertainty. Downstream consumers must independently re-derive
ownership and boundary claims their conclusions depend on from actual code;
this map is not proof for planning, diagnosis, compatibility, review, or behavioral
verification. Identify optional follow-up work without executing it.
