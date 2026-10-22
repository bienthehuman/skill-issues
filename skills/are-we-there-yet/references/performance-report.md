# Performance Report

If consuming artifacts, precede the title with
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`.
Name failed/unavailable re-derivations and inherited claims. Shared-origin artifacts
count as one source. Keep every field, combining sections for small problems;
mark irrelevant fields not applicable with a reason and unavailable facts `unknown`.
Use a partial report when measurement or the template is unavailable.

## Objective and symptom

Original request, affected operation, scope, metric/target and its source.
Attribute user complaints; a subjective symptom activates investigation, not a
diagnosis. State G3 status: measurable baseline present or missing. If missing,
establishing it is the immediate task; no bottleneck diagnosis or improvement claim.

## Workload and reproduction

Exact steps/commands, input source, data size/distribution, revision, concurrency
and load. Reproduction outcome and evidence location; missing inputs/access.
Separate reproducible observations from assumed production workloads.

## Baseline conditions, method and results

Environment/hardware/resource limits; relevant runtime/database/connection and
versions; cache state, warm-up, metric/units, measurement boundary/tool, repetitions,
raw results/evidence locations and summary with variance/spread. Attribute supplied
captures and identify independently reproduced checks. A single sample leaves
variance unknown. Record blocked or failed measurement attempts without substituting
guessed numbers. Unknown consequential conditions limit baseline adequacy.

## Bottleneck evidence and ranked hypotheses

| Observation and source (profiler, trace, query log, EXPLAIN, resource capture) | Cost/path explained | Confirmed bottleneck or ranked `inferred` hypothesis | Supporting/contradicting evidence and cheapest discriminating check |
|---|---|---|---|

Before G3 is satisfied, only undiagnosed tentative measurement leads may be listed;
do not select a remedy from them. Plan estimates are not actual execution timings.
Rank only supported candidates; no invented profiler results or query plans.

## Interventions and status

| One intervention | Proposed or implemented; exact revision/configuration | Evidence/rationale, expected metric, tradeoffs and correctness risks | Actual execution or required next check/handoff |
|---|---|---|---|

Keep proposed, implemented and verified statuses distinct. No automatic schema
change, migration or deployment. A proposal is not a measured improvement.

## Before/after comparison and variance

| Intervention and metric/units | Before results, repetitions, variance and source | After results, repetitions, variance and source | Comparable conditions or explicit differences | Measured improvement, regression, inconclusive or unverified; evidence and limits |
|---|---|---|---|---|

Compare workload/data, environment, load/concurrency, cache/warm-up and method.
Mark materially different conditions non-comparable; controlled reruns are needed
before attributing a gain. Implemented but unmeasured changes remain unverified.
State relevant correctness/resource checks and their actual results.

## Differences from production

Measured versus production workload/data, environment/resources, cache state,
concurrency and dependencies; known differences and unknowns, and their impact
on conclusions. Do not generalize a local improvement into verified production gains.

## Verification, uncertainty and gaps

Actual commands/checks, evidence locations and passed/failed/blocked/unrun status;
recommended checks separately. `inferred` = conclusion from evidence; `assumed` =
unverified premise; `unknown` = insufficient evidence. Untagged observations name
direct support; attribute user reports. Re-check load-bearing claims and list every
relied-on unresolved assumption with dependent conclusions and resolving evidence.
Failed upstream re-derivation leaves dependent conclusions `inferred`, naming the
inherited claim. Never invent timings, row counts or production workloads.

## Relevant handoffs and next measurement

Only warranted handoffs: select-your-battles for schema/index/query/migration
design, but-it-works-on-my-machine for incorrect behavior, read-the-contract for
response-shape/pagination/interface concerns. Return design interventions here
for comparable remeasurement. Disclose missing siblings without claiming their
workflows ran; continue independently supported work only. Name one concrete
next measurement or resolving action, its purpose and needed access.
