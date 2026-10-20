# Impact Report

If consuming upstream artifacts, place this before the title:
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`.
Name failed/unavailable re-derivations and dependent limits; omit the envelope
when no artifacts were consumed. Keep plain Markdown and every field, with short
entries for small changes. The report is an assessment, not execution authority.

## Change objective and investigation scope

Original request, intended outcome, scrutiny reason, investigated components and
exclusions. Identify preliminary scope if no Plan or diff exists; derive only
what the description supports. Do not invent affected code paths.

## Inputs and provenance

Plan/diff/Codebase Map identifiers, revision or base/target when available, direct
inspection and other supplied primary material, freshness and access limits.
A Plan predicts intended changes; a diff evidences actual modifications. Neither
establishes runtime behavior or complete consumer coverage. With both, use the
diff to establish actual modifications. Attribute supplied reports.

## Observed change boundary

Actual modifications supported by the diff, or proposed modifications explicitly
identified as planned. Relevant code/state/contracts, entry points, execution
paths, constraints and assumptions. Record material discrepancies from planned
scope without issuing a plan-conformity or merge verdict.

## Affected components and dependency paths

| Component or behavior | Relationship/path to change and relevant callers/consumers | Supporting source or actual check | Observed, inferred, assumed, or unknown; limits |
|---|---|---|---|

Include state ownership/persistence, asynchronous or integration paths only when
relevant and supported. Distinguish observed affected components from `inferred`
potential effects, `assumed` dependencies and `unknown` consumers or behavior.
Do not treat missing search matches as proof of no consumers.

## Ranked regression risks

| Priority and rationale | Component/behavior and specific failure trigger/scenario | Supporting evidence and assumptions | Consequence/severity | Likelihood/confidence only if defensible | Recommended verification | Remaining uncertainty |
|---|---|---|---|---|---|---|

Rank by relevance, evidence and potential consequences without arbitrary numerical
scores or invented probabilities. Keep investigation coverage separate from impact
severity: retain high-consequence uncertainty even when no affected consumer was
found. Name missing evidence and a scoped resolving check. Speculation is not an
established defect; no invented production traffic, volumes or infrastructure.

## Supporting evidence and uncertainty

| Load-bearing claim | Inspected material or actual source checks | Evidence classification and limits | Dependent conclusion and re-check needed |
|---|---|---|---|

Untagged findings need directly inspected support; `inferred` means concluded
from observed facts; `assumed` means an unverified premise; `unknown` means
insufficient evidence with no value offered. Shared-origin artifacts count as
one source. Independently re-derive ownership, boundary and consumer claims;
re-check load-bearing inferred/assumed claims. If an inherited claim cannot be
re-derived, mark the dependent conclusion `inferred` and name the inherited claim;
missing facts stay `unknown`. Inspection does not establish runtime execution.

## Recommended verification and actual execution

| Material risk | Check, relevant input/path, and regression it should detect | Recommended or actually performed | Actual command/result/evidence if performed; otherwise unrun or blocked |
|---|---|---|---|

Link every material risk to discriminating verification. Distinguish verification
recommended from verification actually performed; a suggested test has not passed.
Record failed, blocked and unrun checks separately from observed passes. Proposed
checks are inputs for behavioral verification, not a completed Test Set.

## Blast-radius coverage and limitations

Name searched paths/sources, available Map coverage, excluded/unavailable areas,
and stopping reason: adequate task-relevant evidence, blocked or disproportionate
further investigation. With a Map, expand only for concrete dependencies or
potential consequences. Without a Codebase Map, trace supported direct callers
only; the discovered blast radius is a **lower bound**, not complete coverage.
Partial searches and unavailable repository access never prove all consumers
were found. State supplied-material limits and missing code/dependency evidence.

## Open questions and unresolved dependencies

Every assumption relied on, unknown consumer/behavior, unresolved relationship,
failed upstream re-derivation and consequential gap. Link each to the affected
conclusion, needed source or resolving check, and any human clarification needed.
Limited evidence does not reduce a potentially severe consequence to low risk.

## Bounded conclusion and handoff considerations

Supported affected components and highest-priority risks with coverage limits.
For a material contract concern, identify the boundary/surface, change, evidence,
known consumers/search limits and open questions for scoped read-the-contract
investigation. This is neither an Interface Check nor a completed Contract Review;
do not reproduce or reclassify all nine surfaces.

Optional handoffs preserve ownership: you-are-here maps structure;
think-before-you-commit plans implementation; prove-it establishes behavioral
verification evidence; trust-issues reviews correctness, plan drift and merge
readiness; famous-last-words handles deployment, operational detection and rollback.
No sibling installation or automatic pipeline is required. Downstream consumers
independently re-derive blast-radius claims, especially lower-bound ones. State
what new evidence could change the assessment; no behavioral reliability claim.
