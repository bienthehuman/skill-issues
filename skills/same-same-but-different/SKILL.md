---
name: same-same-but-different
description: |
  Produce an evidence-based Refactor Plan that changes structure while preserving behavior.
  Use when: the user requests a behavior-preserving refactor, an internal restructure or code reorganization must preserve externally observable behavior, or meaningful refactoring requires verification of behavioral invariants.
  Do not use when: functionality intentionally changes, the primary objective is a bug fix, a trivial rename or mechanical edit already has adequate guarantees, the task is ordinary implementation, or the primary work is contract redesign or migration. Do not turn every cleanup into a formal refactoring workflow.
---

# Same same but different

Lens: Change structure, not behavior.

Inputs: target code, evidence of current behavior, and relevant requirements and
constraints where available. Output: a Markdown Refactor Plan using
[references/refactor-plan.md](references/refactor-plan.md).
Apply the engineering baseline's evidence and authority rules when available.
No sibling skill is required; the Interface Check reference is bundled here.

## Workflow

1. Establish the structural objective, scope, and exclusions. Inspect target code,
   affected behavioral paths, entry points, callers/consumers, state interactions,
   and boundaries. Identify current outputs, errors, side effects, and other
   observable guarantees relevant to these paths. Do not assume current behavior
   is correct. List known defects intentionally preserved, with evidence; they
   are not desired functionality. Separate bug fixes and functional improvements,
   even useful side benefits, from this refactor.
2. Sanity-check supplied requirements, plans, and Test Sets against the original
   request, current code, tests, and available data. Check freshness and scope;
   independently re-derive load-bearing ownership, boundary, consumer, rollback,
   and coverage claims before relying on them. Shared-origin artifacts count as
   one source. An artifact consuming others opens on its first line with
   `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   If re-derivation fails, mark the dependent conclusion `inferred` and name the
   unsupported claim; missing facts remain `unknown`.
3. Establish G1 before refactoring code edits. For every affected behavioral path,
   identify its preservation invariant, named evidence, verification method,
   limits, consequence of an unnoticed change, and an explicit sufficient or
   insufficient assessment with rationale. Inspect relevant test inputs, setup,
   and assertions: would they detect the behavior breaking? Existing tests alone
   do not guarantee coverage; "the tests pass" is not a sufficiency statement.
   Accept named existing tests exercising the path, snapshots/golden outputs,
   characterization tests, or other specifically identified reliable verification.
   Compiler/type guarantees may suffice for purely mechanical rename-only or
   move-only changes, but only for behavior they actually protect. Type checking
   a renamed method does not establish unchanged runtime behavior, serialization,
   reflective lookup, or external consumers; investigate these where relevant.
   Do not require new tests when equivalent reliable evidence already suffices.
   G1 blocks refactoring code edits if any touched path lacks evidence sufficient
   for its consequences. Identify the precise gap and targeted characterization
   or alternative verification needed; establish it before edits. A prove-it
   handoff may help but is not required to be installed. Proposed or merely
   written tests are not executed/passed evidence. State overall G1 readiness
   from the per-path assessments; do not average away an unprotected path.
4. Before performing an Interface Check, read `references/interface-check.md`
   ([bundled reference](references/interface-check.md)), relative to this installed
   skill directory, in this run. Do not classify interface surfaces until the
   reference has been loaded; do not reconstruct the checklist from memory.
   Apply its canonical nine-surface plan-time scan to contracts that must remain
   unchanged, with evidence for every affected/unaffected/uncertain status.
   Expand only affected and uncertain entries. Follow its frontend consumer
   search rule unless API types are generated, database/connection naming, and
   stored-state investigation. Missing searches cannot establish absence of
   consumers: use `uncertain` if they could plausibly find one, otherwise label
   the limited conclusion `inferred`. Uncertainty is not a confirmed change.
   Collapse only when directly observed evidence establishes all four canonical
   conditions in the reference; an inferred check cannot collapse.
   If the bundled reference cannot be read, mark all nine surfaces `uncertain`,
   state that the reference was not loaded, report the assessment as incomplete,
   and request restoration/read of this bundle or human direction. Do not borrow
   a sibling's reference, fabricate classifications, or claim preservation is
   established. Supported evidence gathering and partial planning may continue.
   Split any proposed interface contract change out of the refactor and identify
   a scoped read-the-contract handoff with surface/status, change, evidence,
   known consumers/search limits, and open questions. Investigate uncertain
   surfaces through that handoff where available without claiming they changed.
   A handoff is not a completed Contract Review.
5. Read `references/refactor-plan.md`, relative to this installed skill directory,
   before writing the plan. If unreadable, disclose it and return a partial plan
   retaining the required fields below; do not borrow sibling files or claim
   complete packaging. Define small, ordered steps, each tied to target files,
   behavioral paths/invariants, prerequisites, relevant verification and expected
   unchanged outcomes, and practical reversal. Each step ends in a verifiable,
   working state. Prefer independently verifiable changes over large rewrites;
   explain the structural benefit and alternatives/tradeoffs. Identify rollback
   limits and `one-way` work where undo is impractical; do not assume a Git revert
   restores state or authorizes discarding other work. This skill produces a plan;
   it does not automatically execute it or the downstream pipeline.
6. State explicit stop conditions for subsequent implementation. If a refactoring
   step requires changing a test's expected behavior, the step has stopped being
   a refactor: stop and identify the behavior change separately. Test relocation,
   import updates, or structural reorganization may preserve the same assertions
   and expected outcomes; justify that distinction rather than treating every
   test-file edit as a behavior change. Do not rewrite failing tests or weaken
   assertions to accommodate the refactor. Stop on unexpected behavior, failed
   verification, newly unprotected paths, or consequential boundary uncertainty;
   investigate before continuing. Reassess G1 if the actual scope expands. Apply
   baseline drift rules: return unexpected consequential behavior changes,
   unplanned affected surfaces, uncertainty not cheaply resolvable, or restricted
   actions to the human. Approval of a refactor does not authorize these changes.
7. Return a proportional plan containing objective/scope, target code and paths,
   preservation invariants/contracts, evidence and per-path sufficiency, known
   bugs intentionally preserved, ordered steps with individual verification,
   reversibility/rollback, stop conditions, Interface Check, risks/uncertainties,
   open questions, and warranted downstream handoffs. Distinguish verification
   proposed from actually performed, with commands/results and failed, blocked,
   and unrun checks. Direct findings name inspected material or actual results;
   `inferred` means concluded from observed facts, `assumed` an unverified premise,
   and `unknown` insufficient evidence with no value offered. Attribute user
   reports. Re-check load-bearing inferred/assumed claims; surface every relied-on
   assumption in open questions and state what evidence would change the plan.

## Standalone fallbacks and boundaries

Without behavior evidence, identify affected paths, record each evidence gap,
recommend how to establish adequate coverage, and leave G1 unsatisfied until it
exists. With insufficient existing tests, name exactly which behavior lacks
protection and the targeted characterization or reliable alternative needed.
Without repository access, work only with supplied code/evidence; keep unsupported
preservation claims uncertain and the plan partial. Do not claim repository
searches or test execution occurred. Missing requirements do not establish that
current behavior is correct; plan only supported preservation invariants.

Own behavior-preserving refactor planning and evidence sufficiency. prove-it owns
behavioral verification/regression/characterization evidence; think-before-you-commit
owns general implementation planning for a settled approach; read-the-contract
investigates consumers and compatibility; trust-issues reviews actual requirements,
risks, and the resulting diff, independently checking evidence against paths
actually touched; what-could-possibly-go-wrong analyzes broader impact/regression
risks. These are optional, justified handoffs, never a mandatory pipeline. When
needed sibling instructions are unavailable, name the limitation and required
inputs without reconstructing their procedures or claiming the skill ran.

G1 permits edits only after sufficient evidence exists for every touched path;
compiler-protected mechanical changes use their stated, bounded evidence rather
than automatically requiring new tests. G5/G10 require the loaded reference's
evidence and collapse rules, with only the disclosed all-nine-uncertain fallback
when loading fails. G6/G7 human-authority gates have no escape: follow host
permissions and baseline authority rules; ordinary approved reversible work is
allowed, while consequential/restricted actions return to the human. Do not add
a refactor-specific authorization mechanism or treat a plan as an execution grant.

Comprehensive behavioral evaluation remains deferred. Structural validation does
not establish behavior-preservation reasoning, actual G1 compliance, Interface
Check accuracy, or safe refactoring.
