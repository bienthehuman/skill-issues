# Schema Review

If consuming artifacts, place this before the title:
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`.
Name failed/unavailable re-derivations and dependent limits; omit the envelope
when no artifacts were consumed. Use plain Markdown, retain every field, and
keep small reviews compact. Mark irrelevant fields not applicable with a reason.
This review is not migration execution authorization.

## Objective and scope

Original request, intended outcome, reviewed schema/change, exclusions and
investigation limits. Distinguish proposed changes from existing behavior.

## Database context and input evidence

Engine; version when behavior depends on it; named database and connection;
relevant schema objects; SQL, migrations, models, queries, configuration and
upstream artifacts actually available/inspected. Do not assume MySQL from Laravel.
Disclose unknown identity/version and avoid unsupported engine-specific advice.
Name unavailable repository/database access and supplied-material limits.

## Access patterns and queries

| Named query/access pattern | Application requirement, predicates, joins, ordering/grouping | Read/write characteristics and workload evidence | Observed, inferred, assumed, or unknown; source and limits |
|---|---|---|---|

Separate established requirements from inferred patterns and assumed workloads.
Without access patterns, request queries/workload, review supported structural
integrity properties only, and leave query/index suitability unresolved.

## Schema decisions and supported behavior

| Schema decision | Named access pattern or integrity requirement served | Existing/proposed structure and evidence | Simpler alternatives, tradeoffs, and unresolved suitability |
|---|---|---|---|

Relevant relationships, keys, nullability/defaults, types/representation and
existing-data compatibility. Justify complexity by demonstrated requirements.

## Index recommendations and justification

| Proposed index or change | Named query/access pattern served | Predicates/joins/order/grouping and composite column ordering | Existing indexes and engine-specific behavior | Selectivity/plan/measurement evidence and limits | Write amplification/maintenance cost and alternatives |
|---|---|---|---|---|---|

Flag indexes without a named query/access pattern. No blanket foreign-key indexing.
Missing evidence makes recommendations provisional; name the needed measurement.

## Constraints and integrity invariants

Primary/foreign keys, uniqueness, checks, nullability/default guarantees, relevant
invariants, enforcement evidence, and compatibility with existing data. Structural
integrity findings can remain useful despite missing workload evidence.

## Transaction boundaries

Atomic operations, participating database/connection, isolation assumptions,
constraint responsibilities, retries/idempotency, and cross-connection consistency.
Name evidence and unresolved behavior; do not assume cross-connection atomicity.

## Concurrency and locking risks

| Operation/scenario | Observed problem or hypothetical risk; evidence | Race, lock scope/contention, deadlock, or consistency consequence | Design recommendation and throughput/operational tradeoff | Needed inspection or concurrency test |
|---|---|---|---|---|

Ground behavior in the actual engine; do not invent lock durations or prescribe
stronger isolation/locks without considering costs.

## Migration design and existing-data compatibility

Intended transformation, backfill, null/default transitions, introducing
constraints, data preservation, existing application-version compatibility and
locking implications. Keep production execution order/timing, rollback triggers
and procedures, and monitoring with famous-last-words.

## Reversibility and one-way items

| Decision/operation | Reversible or `one-way` (cannot be undone or undo is impractical) | Data lost or preserved; actual recovery basis and limits | Downstream handoff |
|---|---|---|---|

List every `one-way` item or explicitly state none with supporting rationale.
A down() method is not proof: recreating a dropped column cannot restore lost data.

## Performance evidence and limitations

| Load-bearing claim | Actual EXPLAIN/plan, row counts, measurements, observations or statistics | Evidence classification and limits | Comparable measurement needed; recommended versus actually performed |
|---|---|---|---|

Untagged findings name directly inspected support; attribute user reports.
`inferred` means concluded from observed facts; `assumed` means an unverified
premise; `unknown` means insufficient evidence with no value offered.
Shared-origin artifacts count as one source. Independently re-derive load-bearing
claims against actual code/schema/data. Failed re-derivations leave dependent
conclusions `inferred`, naming the inherited claim; missing facts stay `unknown`.
Re-check load-bearing inferred/assumed claims; never invent plans, cardinalities,
timings, throughput, selectivity or improvements. Without EXPLAIN, counts or
representative measurements, improvements remain unverified. Optimizer plausibility
is not observed benefit; only comparable before/after measurements establish
improvement. are-we-there-yet owns measurement. Record failed, blocked and unrun
checks separately from actual passes.

## Recommendations and tradeoffs

Supported or provisional design recommendations, rationale, simpler alternatives,
read/write and operational costs, load-bearing claims, evidence limits, and what
new evidence would change the conclusion. No unsupported performance guarantees.

## Open questions and unknowns

Every relied-on assumption, unknown engine/connection/version/workload, failed
upstream re-derivation, dependent recommendation and required source/check.
Missing evidence limits conclusions without suppressing supported findings.

## Relevant downstream handoffs

Only warranted work and inputs: think-before-you-commit for Implementation Plan;
are-we-there-yet for Performance Report and comparable remeasurement;
read-the-contract for Contract Review compatibility/consumer windows;
what-could-possibly-go-wrong for Impact Report dependencies;
famous-last-words for Rollout Plan execution sequencing, rollback/detection,
migration design and every `one-way` item; it-depends for broader Decision Record
approach choices. Identify unavailable siblings without reconstructing procedures.
Consumers independently check design, reversibility and unsupported performance
claims. No automatic pipeline, restricted execution, or behavioral reliability claim.
