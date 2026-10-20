---
name: select-your-battles
description: |
  Review database design against application access patterns in a Schema Review.
  Use when: designing or changing schemas; evaluating indexes, constraints, relationships, data structures, queries, or migration designs; investigating schema-level query-performance concerns; or receiving a relevant are-we-there-yet handoff. Route by database topic, whether entered through design or performance investigation.
  Do not use when: ordinary application debugging has no database-design concern; the primary issue is uninvestigated ORM-level N+1 behavior; the need is performance measurement or bottleneck identification; the task is production migration execution or deployment sequencing; or a trivial application change affects no database structure, access pattern, or concurrency behavior.
---

# Select your battles

Lens: Is the data shape right for how it is accessed?

Inputs: existing schema or proposed schema change, relevant access patterns,
available query/workload/database evidence, and an optional Implementation Plan.
Output: a plain Markdown Schema Review using
[references/schema-review.md](references/schema-review.md).
Apply the engineering baseline when available. No sibling skill or shared
reference bundle is required.

## Workflow

1. Establish the original objective and smallest useful scope. Sanity-check
   upstream relevance, freshness, and proposed versus existing state. Independently
   re-derive load-bearing ownership, boundary, consumer, schema, workload, and
   rollback claims against available code, SQL, configuration, and data before
   relying on them. Shared-origin artifacts count as one source. If consuming
   artifacts, open with `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name failed or unavailable re-derivations; a dependent conclusion that cannot
   be re-derived remains `inferred` and names its inherited claim. Missing facts
   remain `unknown`; upstream agreement does not establish them.
2. Identify the database engine, named database and connection, relevant schema
   objects, and version when supported behavior depends on it. The canonical
   stack uses MySQL, MariaDB, or PostgreSQL: one engine per codebase, potentially
   multiple databases or connections. Do not infer MySQL from Laravel or assume
   a connection from framework conventions. Inspect actual configuration/schema
   evidence without exposing credentials. Identify query shapes, predicates,
   workload, read/write characteristics, existing indexes and constraints, and
   relevant transaction behavior. Distinguish observed requirements from inferred
   access patterns and assumed workloads. Unknown engine, connection, version,
   or workload limits the conclusions; disclose it and avoid unsupported
   engine-specific conclusions. Use the actual engine's supported behavior,
   not generic allegedly portable SQL advice.
3. Pair each meaningful schema decision with the application behavior or access
   pattern it serves. Review relationships, primary/foreign keys, uniqueness,
   check constraints, nullability, defaults, types/representation, and integrity
   invariants where relevant. Consider existing-data compatibility and read/write
   costs. A structural integrity finding may stand without workload evidence;
   query and index suitability cannot be established without access patterns.
   Prefer the simplest maintainable, operationally feasible structure satisfying
   demonstrated requirements; theoretical scalability alone earns no complexity.
4. Every proposed index must serve a named query or access pattern; flag an index
   without one. Inspect predicates, joins, ordering/grouping, existing indexes,
   available selectivity evidence, composite column ordering, engine-specific
   behavior, and write amplification/maintenance cost. Do not blanket-index every
   foreign key or mentioned column. Use available actual query plans or
   representative measurements; without adequate evidence, mark the recommendation
   provisional and name the measurement needed. A plausible optimizer choice
   is not an observed improvement.
5. Performance claims need EXPLAIN or equivalent query-plan output, actual row
   counts, representative measurements, observed query behavior, or relevant
   database statistics sufficient for the particular claim. Without EXPLAIN,
   counts, or representative measurements, performance improvements remain
   unverified; do not promote structural plausibility into measured benefit.
   Unsupported benefit premises are `assumed`, deductions from observed facts
   are `inferred`, and insufficient evidence with no value offered is `unknown`.
   Do not invent query plans, cardinalities, timings, throughput, selectivity,
   lock durations, or improvements. Even a plan or row count does not establish
   an improvement: comparable before/after measurements must establish that
   outcome. are-we-there-yet owns baseline measurement, bottleneck identification,
   and remeasurement; specify needed evidence without claiming that workflow ran.
6. Where relevant, examine atomic operations, constraints, concurrent writes,
   race conditions, isolation assumptions, lock scope/contention, deadlocks,
   retry/idempotency requirements, and consistency across connections. Ground
   findings in actual engine and application behavior. Separate observed problems
   from hypothetical risks; name scenarios, consequences, supporting evidence,
   and the inspection or concurrency test needed for unresolved behavior. Weigh
   throughput, contention, and operational costs before stronger isolation or
   additional locks; do not prescribe them reflexively.
7. Review migration design: intended transformation, existing-data compatibility,
   backfill requirements, null/default transitions, introducing constraints,
   preserving data, compatibility with existing application versions, and locking
   implications. Identify reversible decisions and `one-way` operations (cannot
   be undone or undo is impractical), including potential permanent information
   loss. A framework down() method does not establish reversibility: recreating
   a dropped column does not restore its data. Separate design from production
   execution order, deployment timing, lock timing, rollback triggers/procedures,
   and operational monitoring, which belong to famous-last-words.
8. Read `references/schema-review.md`, relative to this installed skill directory,
   before drafting. If unreadable, disclose the missing template and return only
   a partial review preserving the fields below; do not borrow sibling files or
   claim complete packaging. Include objective/scope, engine/database/connection,
   schema/evidence inputs, access patterns/queries, paired schema decisions,
   justified indexes, constraints/invariants, transactions, concurrency/locking,
   migration compatibility/reversibility, performance evidence/limits,
   recommendations/tradeoffs, open questions, and relevant downstream handoffs.
   Keep every field compact; use not applicable with a reason where appropriate.
   A small index review must not become a complete architecture assessment.
9. Untagged findings name directly inspected support; attribute user reports
   without implying verification. Re-check load-bearing `inferred` and `assumed`
   claims against available sources; surface every relied-on assumption in open
   questions with dependent recommendations and resolving evidence. Keep failed,
   blocked, and unrun checks visible, separate from recommended verification.
   Return the review and stop; do not implement recommendations or run migrations.

## Standalone fallbacks

Without access patterns, request relevant workload/query information, review
supported structural properties only, and explicitly leave query/index suitability
unresolved. Missing workload evidence limits conclusions, not all useful analysis.
Without repository or database access, use supplied SQL, migrations, models,
query definitions, or other evidence; name unavailable sources and mark the
assessment limited. Do not invent schema or database state. Without performance
evidence, offer qualified design recommendations and required measurements only.
Without an Implementation Plan, review the supplied schema/change directly.
Missing siblings do not block supported analysis; name unavailable workflows and
their needed inputs without reconstructing procedures or claiming completed work.

## Boundaries and gates

- select-your-battles owns schema, index, query-design, transaction, and
  migration-design decisions through the Schema Review.
- are-we-there-yet owns Performance Report measurement and bottleneck diagnosis;
  uninvestigated ORM-level N+1 goes there first. Return design findings for
  comparable remeasurement before calling performance improved.
- think-before-you-commit owns the Implementation Plan, not this review.
- read-the-contract owns Contract Review consumer compatibility, interface
  changes, and compatibility windows. Flag relevant concerns with evidence and
  known consumers/unknowns; do not perform or claim its formal Interface Check.
- what-could-possibly-go-wrong owns Impact Report code/dependency impact analysis.
- famous-last-words owns Rollout Plan production sequencing, migration execution
  planning, rollback and operational detection. Supply migration design and
  every `one-way` item; do not turn this review into a rollout procedure.
- it-depends owns Decision Record broader approach selection beyond database design.

Handoffs are optional recommendations, not a mandatory pipeline or completed
assessments. Consumers independently re-derive decisions, migration design and
performance claims, especially those lacking EXPLAIN or counts. No additional
design-specific hard gate is introduced. G6/G7 human-authority gates have no
escape: respect host permissions and baseline authority rules. A Schema Review
is not authorization to run a migration, perform restricted operations, or grant
compatibility exceptions; restricted execution needs the baseline/specification
section 7 human authorization. No interface-check.md or authorization.md bundle
is needed under section 3.6.

Structural validation supports provisional standalone use only. Comprehensive
behavioral evaluation remains deferred; database advice, optimizer reasoning,
concurrency analysis, routing reliability, and performance benefits remain unproven.
