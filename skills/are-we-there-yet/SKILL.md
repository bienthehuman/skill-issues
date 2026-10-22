---
name: are-we-there-yet
description: |
  Investigate slowness through measurement and produce a Performance Report.
  Use when: execution, requests, queries, or processing are slow or inefficient; performance has degraded; the user says "this feels slow"; or a database-design handoff needs comparable performance remeasurement. Includes uninvestigated ORM-level N+1 symptoms.
  Do not use when: the primary problem is incorrect behavior without a performance symptom; requirements are missing; or the task is only schema, index, query, or migration design without performance measurement. Route ordinary correctness bugs to but-it-works-on-my-machine and database design to select-your-battles.
---

# Are we there yet

Lens: Slowness, measured.

Inputs: objective or subjective symptom, a workload that reproduces it, available
code, measurements and environment evidence; upstream artifacts are optional.
Output: a Markdown Performance Report using
[references/performance-report.md](references/performance-report.md).
Apply the engineering baseline when available. No sibling skill or shared
reference bundle is required.

## Investigation

1. Establish the original objective, affected operation, scope and meaningful
   performance metric or target. Attribute subjective complaints and supplied
   measurements to their sources. Sanity-check upstream relevance, freshness,
   revision and proposed versus implemented state. Independently re-derive
   load-bearing workload, boundary, ownership, consumer and recovery claims
   against available code, configuration, data and actual captures. Shared-origin
   artifacts count as one source. If consuming artifacts, open with
   `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name failed or unavailable checks; dependent conclusions remain `inferred`
   and name inherited claims. Missing facts remain `unknown`.
2. Apply **G3: baseline before diagnosis**. A measurable baseline is required
   before diagnosing a bottleneck or claiming any improvement. Its only escape
   condition is that a measurable baseline exists. "Feels slow" activates this
   skill but does not confirm a cause or bypass G3. Without a baseline,
   establishing one is the immediate task, not choosing an optimization.
   Locate usable existing measurements or construct the smallest reproducible
   workload. Record steps/commands, inputs and data size/distribution, revision,
   environment/runtime/database versions as relevant, resource limits,
   concurrency/load, cache state and warm-up, measurement method and units,
   repetitions and actual results. Unknown conditions limit interpretation;
   a vague timing with no reproducible context is not an adequate baseline.
3. Measure safely where feasible. Choose metrics that capture the complaint
   (for example latency distribution, throughput, CPU, memory or query count).
   Retain raw results or evidence locations; report repeated measurements and
   variance/spread using an appropriate stated summary. A single sample cannot
   establish variance: label that gap and limit the claim. Without executable
   access, use attributable supplied captures and state what was not independently
   reproduced. If meaningful measurement is unavailable, return a partial report
   with missing inputs, blocked/unrun checks and the next baseline measurement;
   do not diagnose a bottleneck or invent a baseline.
4. After G3 is satisfied, gather bottleneck evidence appropriate to the workload:
   profiler samples, traces, query logs, EXPLAIN or equivalent query-plan output,
   resource/queue observations. Connect the measured cost to the affected path.
   Identify the actual database/connection before engine-specific plan reasoning.
   Distinguish estimated plan costs/row counts from actual execution observations;
   EXPLAIN alone does not establish wall-clock improvement. Rank hypotheses by
   supporting and contradicting evidence when the cause is incomplete, with a
   discriminating check for each. Keep candidates `inferred`, not confirmed
   bottlenecks. Before a baseline exists, record only tentative leads for future
   measurement, explicitly undiagnosed; do not use them to select a remedy.
5. Propose the smallest evidence-supported intervention, its tradeoffs, expected
   metric and verification method. Distinguish proposed from implemented changes.
   Implement only within the user's authorized scope; otherwise return the
   proposal. Test one performance intervention at a time, retaining the baseline
   and identifying the exact changed revision/configuration. Do not bundle cache,
   query, schema and response changes into an uninterpretable experiment.
   Route schema/index/query or migration design to select-your-battles; return
   its design findings here for measurement. Route incorrect behavior requiring
   root-cause diagnosis to but-it-works-on-my-machine, and response-shape,
   pagination or other relevant interface changes to read-the-contract.
6. Remeasure each implemented intervention under comparable workload, data,
   environment, concurrency, cache/warm-up and measurement method. Record before
   and after results, repetitions, variance and evidence, including regressions
   or inconclusive results. Explicitly identify changed conditions; if materially
   different, mark the comparison non-comparable and rerun controlled measurements
   before attributing improvement. Preserve correctness and relevant resource/cost
   checks; faster wrong results are not success. A proposed optimization or an
   implemented change without comparable remeasurement remains unverified.
   State measured-condition differences from production and limit extrapolation;
   local gains do not establish production gains.
7. Read `references/performance-report.md`, relative to this installed skill
   directory, before drafting. If unreadable, disclose the missing template and
   return a partial report retaining the required fields below; do not borrow
   sibling files or claim complete packaging. Include objective/symptom, workload
   and reproduction, baseline conditions/method/results, bottleneck evidence,
   ranked hypotheses, interventions and their status, comparable before/after
   results with variance, production differences, verification/gaps and relevant
   handoffs. Keep simple issues compact; combine fields or tables where useful.

## Evidence and boundaries

Direct observations name inspected support; attribute user reports. Use existing
labels: `inferred` for conclusions from evidence, `assumed` for unverified premises,
`unknown` for insufficient evidence. Re-check load-bearing inferred/assumed claims
and surface unresolved assumptions with dependent conclusions and resolving checks.
Do not invent timings, row counts, production workloads, query plans or profiler
results. Separate actual passes, failures, blocked and unrun verification from
recommended checks. No structural check proves behavioral reliability.

Missing siblings are not installation dependencies: disclose the unavailable
workflow and continue only independently supported measurement/reporting. Do not
reconstruct missing procedures or claim another skill ran. Handoffs are optional,
not a mandatory pipeline. Performance analysis does not automatically authorize
schema changes, migrations or production deployment. Follow baseline authority
and host permissions for measurement as well as intervention. G6/G7 human-authority
gates have no escape; a report grants neither restricted execution nor compatibility
exceptions. No shared reference or formal Interface Check is assigned to this skill.
