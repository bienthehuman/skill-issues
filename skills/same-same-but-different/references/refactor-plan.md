# Refactor Plan

If upstream artifacts were consumed, open on the first line, before the title:
`Upstream: <names> | Re-derived: <claims and actual source checks>`.
Shared-origin artifacts count as one source. Re-derive load-bearing claims;
unsupported dependent conclusions remain `inferred`, naming the missing check.
Keep the plan proportional to scope and consequences; retain every field, using
brief entries where sufficient. This is planning, not automatic execution.

## Objective and scope
<Target code, intended structural improvement, original request/constraints,
exclusions, alternatives and why this structure helps. Separate functional work.>

## Inputs and current behavior
<Inspected code/revision, entry points, callers/consumers, state interactions,
boundaries, requirements and upstream artifacts; freshness and access limits.
Distinguish observed behavior from inspection-based assumptions and user reports.
Direct findings name supporting material/checks; `inferred` = conclusion from
observed facts; `assumed` = unverified premise; `unknown` = insufficient evidence
with no value offered. Re-check load-bearing inferred/assumed claims.>

## Preservation invariants and contracts
<Identify each affected behavioral path, target files, current outputs/errors,
side effects and contracts that must remain unchanged, including every Interface
Check surface. Give path/invariant identifiers for traceability, not new evidence
labels. Current behavior is not automatically desired or correct behavior.>

## Behavior evidence and G1 readiness
| Path / invariant | Named evidence and actual source checks | Protected behavior / limits | Consequence of unnoticed change | Sufficient / insufficient and rationale | Gap and required verification |
|---|---|---|---|---|---|
| <path> | <test IDs/assertions, snapshot, compiler guarantee, characterization, other reliable evidence> | <what detects a break; what remains unprotected> | <consequence> | <explicit per-path judgment> | <targeted evidence needed> |

<Overall G1: satisfied only if evidence is sufficient for every touched path;
otherwise refactoring code edits blocked. Existing tests alone do not establish
coverage. Compiler/type guarantees protect only demonstrated mechanical behavior,
not automatically runtime behavior, serialization or external consumers. No new
tests required if equivalent reliable evidence suffices. Distinguish suggested,
written and executed checks; do not claim proposed verification passed.>

## Known defects intentionally preserved
<Known bug -> path/invariant -> evidence -> behavior intentionally unchanged ->
separate follow-up, if warranted. Not desired functionality. State none identified
with inspection limits rather than claiming no defects exist.>

## Ordered reversible steps and individual verification
| Step / prerequisite | Target files and structural change | Paths / invariants preserved | Verification and unchanged expected outcome | Reversal / rollback limits |
|---|---|---|---|---|
| <small ordered step> | <change> | <IDs> | <named relevant check after this step> | <practical undo> |

<Each step ends in a verifiable, working state; prefer independently verifiable
changes. State baseline verification actually performed with commands, revision,
environment, results and evidence; report failed, blocked and unrun checks
separately from future checks. No assertion weakening or functional side benefits.>

## Reversibility and rollback considerations
<How to reverse steps without losing unrelated work; recovery prerequisites and
limits, especially state. Mark `one-way` if undo is impractical. Plan approval does
not authorize destructive Git operations, shared/production migrations, live
infrastructure changes or other restricted actions; return these to the human.>

## Stop conditions
<If a refactoring step requires changing a test's expected behavior, it has stopped
being a refactor: stop and separate the behavior change. Structural test edits
must retain assertions and outcomes; do not rewrite failures or weaken assertions.
Stop for unexpected behavior, failed verification, missing evidence/newly touched
paths (reassess G1), consequential uncertainty, unplanned affected surfaces, or
restricted actions. State resolving evidence and decisions needed to continue.>

## Interface Check
<Before classification read this installed bundle's interface-check.md in this
run, never from memory. Use its canonical nine-surface scan with evidence for
every status; expand affected/uncertain surfaces only. Collapse only with directly
observed evidence satisfying all four canonical conditions; never inferred.
Follow frontend search/generated-type, database/connection and stored-state rules.
If the bundled reference is unavailable, mark all nine surfaces `uncertain`,
state it was not loaded and assessment is incomplete; do not substitute sibling
references or fabricate classifications. Split proposed contract changes from
the refactor and identify scoped read-the-contract handoffs. A handoff is not a
completed Contract Review; uncertainty is not a confirmed change.>

## Risks, uncertainties and open questions
<Missing inputs, assumptions relied on, unresolved coverage/consumer questions,
tradeoffs and blocking status; name next investigation, load-bearing claims and
evidence that would change the plan. Unsupported preservation remains uncertain.>

## Relevant downstream handoffs and bounded conclusion
<G1 readiness and remaining limitations. Optional prove-it evidence work,
read-the-contract compatibility investigation, trust-issues review of the actual
diff and paths, what-could-possibly-go-wrong broader impact, or
think-before-you-commit general planning when warranted. Provide scope, evidence,
gaps and needed inputs. Missing siblings do not prevent supported partial work;
do not reconstruct procedures or claim handoffs ran. No automatic full pipeline.
Structural validation does not prove safe refactoring or behavioral reliability.>
