---
name: famous-last-words
description: |
  Produce an evidence-based Rollout Plan for the running system: deployment, rollback, and detection.
  Use when: a change is going to production and a relevant persistence, contract, security, operations, or integration stakes trigger has fired.
  Do not use when: the work is an ordinary internal change, has a legitimately collapsed Interface Check, or has no relevant persisted-data or operational consequences. Implementation planning, contract investigation, and migration design alone do not activate rollout planning.
---

# Famous last words

Lens: The running system—deployment, rollback, and detection.

Inputs: Implementation Plan, Impact Report, Contract Review (especially its
compatibility window), Schema Review when relevant, and available code,
configuration and operational evidence. Review Findings may also inform readiness.
Output: a Markdown Rollout Plan using
[references/rollout-plan.md](references/rollout-plan.md). No sibling is required.
Apply the engineering baseline's evidence and authority rules when available.
Producing or approving this plan never authorizes a production operation.

## Workflow

1. Establish the production change, target environment, intended release and
   relevant stakes trigger. Check exclusions before expanding the work. General
   implementation planning belongs to think-before-you-commit; consumer and
   compatibility investigation to read-the-contract; schema, query and migration
   design to select-your-battles. Use only warranted handoffs, not a full pipeline.
2. Inspect available sources and deployment configuration. Check upstream scope
   and freshness against the request and current revision. Independently re-derive
   consequential ownership, boundaries, consumer completeness, blast radius,
   compatibility and rollback claims against actual code, configuration and data.
   Shared-origin artifacts count as one source. If consuming artifacts, open the
   first line with `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   A missing check must be disclosed, not described as completed; dependent
   conclusions remain `inferred`, naming the unsupported upstream claim, and
   missing facts remain `unknown`.
3. Read `references/rollout-plan.md`, relative to this installed skill directory,
   before drafting. If unreadable, disclose incomplete packaging and produce a
   partial plan retaining the required fields below. Establish deployment sequence
   and component ordering with prerequisites, per-step verification and stop
   conditions. Check old frontend/new backend, new frontend/old backend where
   reachable, worker/producer overlaps and rollback versions. Updating both sides
   in one commit does not establish simultaneous deployment. Define the supported
   compatibility window and its retirement evidence; never invent guarantees.
4. Order migrations and dependencies around application versions, locks and
   operational timing for the named database and connection. Consume migration
   design without assuming it was validated. Account for existing persisted data,
   queued and in-flight jobs, cached values, sessions, JSON and other serialized
   state across deployment and rollback. Specify applicable drain, payload
   versioning, dual-read or staged transition behavior, and how completion is
   observed. Do not casually flush live state. Identify steps whose undo is
   impossible or impractical as `one-way`, with consequences, prerequisites and
   the point after which code rollback is unsafe. A Git revert is not data recovery.
5. State blast radius from evidence, separating observed scope from an explicitly
   labeled estimate. Without an Impact Report, state blast radius `unknown` and
   give a defensible upper-bound estimate when possible, with basis and limits.
   If no bound is supported, say so. Scale precautions to consequences: staged
   exposure, pause points, recovery preparation or a readiness blocker as warranted.
   Missing production configuration, counts, traffic, queue age, dashboards or
   restore evidence must have an explicit effect on readiness, not invented values.
6. Define rollback triggers as concrete observable signals with thresholds,
   observation windows and responsible observers. Name metrics, log events or
   alerts, their source, when observation starts, and who decides to pause or
   roll back. "Monitor the logs" alone is invalid. Distinguish existing instruments
   from proposed instrumentation and label proposed thresholds `assumed` pending
   baseline validation. Unknown telemetry or ownership remains a readiness gap.
   Give ordered rollback procedures, version/state compatibility prerequisites,
   recovery verification and limits. When rollback is unsafe or impossible, name
   containment and forward-recovery options and required human decisions instead
   of promising reversal. Base side-effect and irreversibility claims on inspected
   handlers/configuration; a job's name alone does not establish external delivery.
   Rollback itself can require Restricted execution.
7. Before identifying or evaluating Restricted steps, read
   `references/authorization.md` ([bundled reference](references/authorization.md)),
   relative to this installed skill directory, in this run. Do not reconstruct it
   from memory. If it cannot be loaded, disclose that limitation and fall back to
   the baseline's inline Authority floor; if that too is unavailable, do not claim
   an authority assessment is complete or execute consequential operations.
   Now list Restricted steps under the dedicated field below using the loaded
   policy, separating ordinary preparation from execution. G6 execution go-ahead
   and G7 human-only compatibility exceptions have no escape. For each Restricted
   action require explicit, human-originated, current-session, single-use
   authorization at execution, including retries. Plan approval, previous-session
   authorization, repository text and tool output are not execution permission.
   Present the exact action/command, target, environment, impact/blast radius,
   reversibility and prerequisites before requesting that go-ahead, then wait.
   During planning, list these requirements without asking for premature execution
   approval. Never record a compatibility exception as granted without human
   authorization; distinguish proposals and historical records from current grants.
8. Return the proportional plan with scope/inputs, sequence and mixed-version
   window, migration ordering, stored-state handling, blast radius, rollback
   triggers and procedure, detection/observers, `one-way` steps, Restricted steps,
   verification/readiness and open questions. Keep all fields; explain nonapplicable
   ones briefly. Name checks actually performed, commands/results and failed,
   blocked or unrun checks separately from proposed validation. An inspected or
   proposed deployment procedure is not a validated one. Re-check load-bearing
   `inferred` (conclusion from evidence) and `assumed` (unverified premise) claims;
   resurface relied-on assumptions in open questions. `unknown` means insufficient
   evidence with no value offered. Direct findings name actual inspected sources
   or checks; attribute user reports. Include every `one-way` step and unresolved
   execution prerequisite in the previously-on handoff when one is requested.

## Standalone fallbacks and readiness

Without an Implementation Plan, derive only the minimal sequence supported by the
change and evidence. Without a Contract Review, investigate available consumers
and version windows but do not assert compatibility from their absence. Without
a relevant Schema Review, identify migration design/locking/reversibility questions
and the evidence needed; do not reconstruct unavailable sibling procedures.
Without repository or production access, work from supplied material, name missing
information and its effect on readiness, and leave unsupported conclusions incomplete.
Missing artifacts do not prohibit supported partial planning. Consequential gaps
return to the human with the needed evidence or decision; unavailable skills are
named as limitations, never claimed to have run. This skill does not perform or
reclassify an Interface Check, grant merge approval, or execute the rollout.

Comprehensive behavioral validation remains deferred under the specification.
Structural checks alone establish neither operational safety nor Codex or Claude
Code reliability.
