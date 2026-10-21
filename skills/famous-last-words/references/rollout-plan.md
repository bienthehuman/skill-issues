# Rollout Plan

If consuming artifacts, put this envelope on the first line, before the title:
`Upstream: <names> | Re-derived: <claims and actual source checks>`.
Keep all fields, with brief reasons for nonapplicable entries. Shared-origin
artifacts count as one source. This plan is not execution authorization.

## Scope and evidence
<Change/revision, production target/environment, objective, stakes trigger,
exclusions, inspected code/configuration and upstream artifacts with freshness
and access limits. Direct findings name supporting sources; attribute user reports.
Use `inferred` for conclusions from evidence, `assumed` for unverified premises,
and `unknown` for insufficient evidence with no value offered. Name load-bearing
claims independently re-derived and unsupported upstream claims.>

## Deployment sequence and compatibility window
| Order / prerequisite | Component / version / action | Reachable mixed-version state and compatibility evidence | Verification / stop condition |
|---|---|---|---|
| <step> | <target and proposed action> | <old/new frontend, backend, producers/workers, rollback versions> | <observable outcome and pause point> |

<Window duration/basis, consumers, how old versions retire, and evidence required
before removing transitional support. No compatibility guarantee from a shared
commit or missing Contract Review.>

## Migration ordering and dependencies
<Database and connection; schema/data steps relative to application versions;
dependencies, locking/concurrency timing, prerequisites and validation. Distinguish
design evidence from proposed execution. State why inapplicable if no migration.>

## Existing data and serialized state
| State / producer / consumer versions | Existing and in-flight state evidence / limits | Transition handling and order | Completion / rollback compatibility check |
|---|---|---|---|
| <persisted rows, queued jobs, caches, sessions, JSON or other payloads> | <age/volume/format or unknown> | <drain, version payloads, dual-read or justified alternative> | <specific observation> |

## Blast radius and precautions
<Observed affected scope and evidence; explicitly label estimates and their basis.
Without an Impact Report: blast radius `unknown`, with a defensible upper-bound
estimate when possible; otherwise say no supported bound exists. Consequences,
staged exposure/pause points and precautions proportional to uncertainty.>

## Detection and rollback triggers
| Named metric / log event / alert and source | Existing or proposed / evidence | Threshold and observation window | Responsible observer / decision owner / response |
|---|---|---|---|
| <specific signal, not just monitor the logs> | <actual source or instrumentation gap> | <concrete trigger; proposed values assumed until validated> | <who observes when and pauses or initiates recovery> |

## Rollback procedure and recovery limits
<Ordered component/state recovery steps, prerequisites, backup/restore evidence,
compatible versions, verification of recovery and residual effects. Identify when
rollback is unsafe/impossible; describe containment/forward recovery and human
decisions. Code reversal alone does not restore data. Reference step IDs below.>

## One-way steps
<Every `one-way` step, exact point of irreversibility, affected state/consumers,
consequences and recovery prerequisites. State none only with supporting evidence.
Carry all items into any requested handoff.>

## Restricted steps (require go-ahead at execution; plan approval does not cover them)
<Complete this field only after the entrypoint's authorization-reference read
step. Use that policy; do not duplicate it here. Include rollout and recovery.>

| Step / exact action and command | Target / environment | Impact / blast radius | Reversibility / prerequisites | Execution approval needed |
|---|---|---|---|---|
| <action> | <named target> | <scope or unknown and supported estimate> | <rollback or one-way; checks first> | <required human decision, not an invented grant> |

## Verification, readiness and open questions
<Actual checks with commands, revision/environment and results; failed, blocked
and unrun checks. Separate proposed rehearsals, telemetry/threshold validation and
restore tests from completed verification. A proposed procedure is not a validated
one. Missing upstream artifacts and production evidence, relied-on assumptions,
consequential gaps, resolving evidence/owner and effect on readiness. Give a bounded
readiness conclusion without execution permission. Include optional scoped handoffs,
not an automatic pipeline or claims that unavailable skills ran.>
