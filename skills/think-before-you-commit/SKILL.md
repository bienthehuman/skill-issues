---
name: think-before-you-commit
description: |
  Turn a settled approach into an evidence-based Implementation Plan.
  Use when: the approach is settled and a change touches persisted data, changes an interface, is hard to roll back, or crosses a module boundary.
  Do not use when: no stakes trigger fires, the change is trivial, the approach is disputed, or the task is diagnosis or completed-code review.
---

# Think before you commit

Lens: Turn a settled approach into ordered, verifiable steps.

Inputs: task and settled approach; optional requirements/criteria, Decision Record,
and Codebase Map. Output: a concise Markdown Implementation Plan using
[references/implementation-plan.md](references/implementation-plan.md).
Apply the engineering baseline's evidence and authority rules.

## Workflow

1. Check routing. If the approach is disputed, identify the unresolved decision
   (it-depends if available) and stop planning that approach. If no stakes trigger
   fires, skip this artifact and return to the ordinary task workflow.
2. Check inputs against the request and current code. Upstream artifacts are
   claims: re-derive load-bearing ownership, boundary, consumer, and rollback
   claims through inspection, naming files and searches. Without a Map, inspect
   touched areas and relevant callers only. Without criteria, write minimal inline
   `assumed` AC-n criteria and surface them as open questions. Without repository
   access, name needed files and mark the plan partial; do not invent evidence.
3. Read `references/implementation-plan.md`. Inspect relevant code before drafting
   ordered steps. Link each step to files/components, criteria, and meaningful
   verification. Distinguish evidence from `inferred`, `assumed`, and `unknown`
   claims; re-check load-bearing inferred/assumed claims where possible and keep
   unresolved assumptions visible. Include risks, alternatives/tradeoffs,
   reversibility (`one-way` when undo is impractical), and out of scope.
4. Before performing the Interface Check, read `references/interface-check.md`,
   relative to this installed skill directory, in this run. Do not classify any
   interface surface until the reference has been loaded; do not work from memory.
   Then perform its nine-surface plan-time scan, naming evidence for every status.
   For HTTP include a frontend consumer search unless types are generated.
   Without consumer searches the check is `inferred`; use `uncertain` instead if
   the missing search could plausibly find a consumer. Expand affected/uncertain
   entries only; name the investigation needed for each uncertainty. Collapse
   only under all four conditions in the reference, never for an inferred check.
   Every affected/uncertain surface needs an explicit scoped read-the-contract
   handoff. If unavailable, identify the required review and inputs without
   inventing a placeholder skill or claiming the review happened.
   If the reference cannot be read, state it could not be loaded, list surfaces
   1 through 9 as `uncertain` with failed access as evidence and restoring/reading
   the bundle as the next investigation. Do not reconstruct the checklist,
   collapse, or issue confident compatibility conclusions.
5. Before identifying restricted operations or writing Restricted steps, read
   `references/authorization.md`, relative to this installed skill directory.
   Then list restricted steps separately from ordinary implementation: exact
   action/command, target/environment, impact, prerequisites, and reversibility.
   If unavailable, disclose the missing reference and use the baseline's
   restricted-action rules as the minimum protection. If the baseline is also
   unavailable, mark authority classification incomplete and defer potentially
   restricted execution pending the rules and human authorization.
6. Return the plan and stop. Do not implement, execute restricted actions, create
   a commit, or grant a compatibility exception. Handoffs are requirements,
   not completed work.

## Gates

- G5: every status needs evidence; bare "none" is invalid. Escape: the loaded
  reference's evidenced collapsed form, only when all four conditions hold.
- G10: read the bundled reference before classifying. The only fallback is all
  nine uncertain with the loading failure disclosed.
- G6/G7: restricted execution and compatibility exceptions need human authority;
  no escape. Plan approval never covers restricted execution.

Keep every required field, but use short fields and compact tables for small
changes rather than eleven essays.
