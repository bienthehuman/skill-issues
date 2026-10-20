---
name: read-the-contract
description: |
  Evaluate what consumers can rely on and what a change breaks for them.
  Use when: an Interface Check flags an affected or uncertain surface in a planned change or real diff, or a scoped contract investigation is requested.
  Do not use when: the Interface Check legitimately collapsed, no contract concern exists, or the task is general code review or implementation planning.
---

# Read the contract

Lens: What consumers can rely on, and what this breaks for them.

Inputs: an affected or uncertain surface and a planned change or real diff;
optional Implementation Plan, Codebase Map, Impact Report, and existing contract
documentation. Output: a Markdown Contract Review using
[references/contract-review.md](references/contract-review.md).
Apply the engineering baseline's evidence and authority rules.

## Workflow

1. Establish scope and whether this is a plan-time prediction or a review of a
   real diff. A plan review is weaker evidence; do not present proposed behavior
   as implemented. Without a supplied check, investigate the named concern inline.
   Without a change description or repository access, name the missing inputs
   and return a partial review rather than inventing consumers or behavior.
   Re-derive upstream boundary, ownership, consumer, and reversibility claims
   against the request and actual sources before relying on them. A claimed
   legitimate collapse needs evidence; do not inherit it unquestioningly.
2. Before classifying any surface, read `references/interface-check.md`, relative
   to this installed skill directory, in this run. Do not classify from memory.
   Investigate the scoped surfaces and any connected surfaces discovered; this
   is not an automatic repetition of the entire planning scan. Give each status
   evidence and each uncertainty a resolving investigation. If the reference
   cannot be read, disclose the failed access, list surfaces 1 through 9 as
   `uncertain`, and make restoring/reading the bundle the next investigation.
   Do not reconstruct the checklist or issue confident compatibility conclusions.
3. Read `references/contract-review.md`. Discover producers and consumers through
   source and usage searches, naming how each was found and the limits of the
   search. For HTTP search frontend clients, hooks, and types unless API types
   are generated; inspect the generation path when relying on it. Without that
   search the check is `inferred`; use `uncertain` if it could reveal a consumer.
   If the frontend is unavailable, explicitly label HTTP consumer coverage
   `inferred` or `uncertain` even when the producer change itself is directly
   evidenced as affected; a backend-only search cannot establish consumer coverage.
   Consumers not found remain `unknown`, never "none" or automatically "public".
   Scale investigation to consequence: obvious searches for low consequence;
   wider repos, mobile/partner clients, and actual caller evidence for high
   consequence when accessible. If inaccessible, state what remains unknown and
   plan conservative precautions without calling uncertainty a confirmed change.
4. Compare before/after guarantees for each consumer separately: breaking,
   non-breaking, or unresolved with evidence. Include validation, status codes,
   errors, and failure behavior, not just field shapes. Name database/connection
   for schema work. Check old serialized payloads separately from new producers:
   queues, caches, sessions, and JSON data may outlive the changed code.
5. Always state the compatibility window: which old clients, stored payloads,
   and in-flight jobs must work, for how long, and what evidence establishes the
   end of support. Include old frontend/new backend and rollback combinations.
   Unknown duration stays unknown with an investigation or safe exit condition.
   Propose a migration path, ordering, mitigation, verification, and rollback
   limits (`one-way` where appropriate); do not execute it. Assess material risk
   using the loaded reference, including possible impact of unresolved surfaces.
   Supply findings to downstream review; do not issue a merge verdict on its behalf.
6. Before drafting any exception proposal, read `references/authorization.md`
   relative to this installed skill directory. Do not work from memory. State
   the named break, surfaces, consumers, accepted impact/duration, conditions,
   and alternatives as a proposal only. Never fill a human grant into a proposal.
   If the reference is unavailable, disclose it and use baseline Authority rules
   as the floor. If those too are unavailable, mark authority review incomplete
   and defer exception handling and potentially restricted execution.
7. Return the Contract Review with evidence, assumptions/open questions, and
   scoped next work for planning, verification, review, or rollout as relevant.
   Sibling skills need not be installed; describe required work and inputs without
   claiming a handoff completed. Do not implement or execute restricted actions.

## Gates

- G10: load the bundled Interface Check before classification; only escape is
  the disclosed all-nine-uncertain loading-failure fallback.
- G6/G7: restricted execution and compatibility exceptions need human authority;
  no escape. An exception proposal is never a grant.
- Compatibility findings preserve G2's downstream rule: unresolved material risk
  prevents a positive merge recommendation unless a recorded human exception
  covers it. Non-material findings require evidence for all conditions in the
  reference; uncertainty is assessed against its possible impact.

Keep the review proportional: short fields and a per-consumer table, expanding
only consequential findings. Preserve uncertainty and explain what evidence
would change the conclusion.
