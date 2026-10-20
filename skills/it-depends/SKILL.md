---
name: it-depends
description: |
  Compare engineering approaches and produce an evidence-based Decision Record.
  Use when: the engineering problem or intended behavior is sufficiently understood but the approach remains undecided; multiple meaningful technical approaches need comparison; the user requests architectural or implementation-strategy tradeoffs; or a consequential technology, integration, or design choice needs justification.
  Do not use when: what to build is still unclear, the approach is already settled and needs implementation planning, a trivial conventional task needs no meaningful comparison, the request challenges whether an idea should exist, or execution/code changes are requested without an unresolved approach decision.
---

# It depends

Lens: Which approach, given the constraints?

Inputs: the engineering decision, relevant constraints and context; Requirements
and a Codebase Map when available. Output: a plain Markdown Decision Record using
[references/decision-record.md](references/decision-record.md).
Apply the engineering baseline when available. No sibling skill or shared
reference is required. Do not require a Decision Record for routine development.

## Workflow

1. Establish the actual decision and intended outcome against the original request.
   Identify relevant acceptance criteria, constraints, non-goals, repository
   conventions, implementation and operational conditions, and material assumptions.
   Without Requirements, derive only minimal supported criteria; mark unverified
   premises `assumed`. Without a Codebase Map, inspect only task-relevant code,
   callers, configuration, and dependencies; do not map the whole repository.
   Without repository access, distinguish supplied context from independently
   observed facts, name unavailable evidence, and do not invent inspection,
   project constraints, operational requirements, or stakeholder preferences.
2. Sanity-check upstream artifacts for relevance, freshness, and fidelity to the
   original request. Independently re-derive load-bearing criteria, constraints,
   ownership, boundary, consumer, and rollback claims from actual primary material
   before relying on them. Shared-origin artifacts count as one source.
   An artifact consuming others opens with
   `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name failed or unavailable re-derivations. A dependent conclusion that cannot
   be re-derived remains `inferred` and names the inherited claim; insufficient
   facts remain `unknown`. Agreement among artifacts does not supply evidence.
3. Compare at least two genuine alternatives before recommending a choice.
   Each must plausibly address the actual objective under known constraints;
   do not manufacture weak or straw-man options to justify a favorite. Explain
   feasibility limits rather than silently treating an infeasible option as viable.
   Use consistent criteria across options, prioritized for this decision, not a
   universal checklist. Relevant factors may include correctness, complexity,
   maintainability, architecture/convention fit, development and operational
   costs, supported performance/scalability implications, security/failure risks,
   dependency/integration costs, and reversibility or migration consequences.
   A technically defensible solution may still be a poor project choice:
   explicitly consider existing conventions, operational constraints, and the
   cost of introducing dependencies or abstractions. Prefer straightforward
   existing solutions unless concrete benefits justify deviation; sophistication
   is not evidence of superiority. Avoid arbitrary numerical scores, invented
   benchmarks, and unsupported performance claims.
4. Explain the preferred approach and why its tradeoffs best fit the established
   criteria and evidence. For each rejected alternative, state what it does
   better and why its disadvantages outweigh those benefits here. Document
   whether the decision is reversible or `one-way` (undo is impractical), why,
   and what evidence, changed assumption, or future condition would reverse the
   choice or require revisiting it. Do not invent a reversibility tier.
   If evidence cannot support a choice, keep the assessment provisional or
   unresolved, identify dependent conclusions and the cheapest useful investigation
   that could distinguish the options. If multiple alternatives cannot be
   meaningfully assessed, explain why and name the missing information; do not
   fabricate alternatives or force a recommendation to fill the record.
5. Read `references/decision-record.md`, relative to this installed skill directory,
   before drafting. If unreadable, disclose the missing template and return only
   a partial record preserving the fields below; do not borrow sibling files or
   claim complete packaging. Include decision/context, requirements/constraints/
   assumptions, genuine alternatives, consistent tradeoffs/evidence, chosen or
   provisionally preferred approach, rejected options/reasons, reversibility,
   revisit conditions, unresolved questions, and sources/verification limitations.
   Keep simple decisions compact; the template is not a lengthy architecture
   document requirement.
6. Use canonical evidence conventions: untagged findings name actual inspected
   support; attribute user reports without implying independent verification.
   `inferred` means concluded from observed facts; `assumed` means an unverified
   premise; `unknown` means insufficient evidence with no value offered.
   Re-check every load-bearing inferred/assumed claim against available sources;
   surface every assumption relied on in open questions, with its dependent
   recommendation and needed evidence. Keep failed checks and unresolved gaps
   visible. Do not invent reads, tests, measurements, or successful outcomes.
7. Return the Decision Record and stop approach selection. Identify chosen and
   rejected approaches, constraints, and reversal conditions for optional consumers,
   who must independently check that constraints still hold. A recommendation is
   neither an irreversible decision nor authorization to execute; distinguish
   a recommendation from an established human decision.

## Boundaries and gates

- define-done establishes intended behavior and acceptance criteria (Requirements).
- think-before-you-commit turns a settled approach into an ordered Implementation
  Plan. Do not turn this record into implementation steps or execute the choice.
- devils-advocate challenges whether a direction should be pursued, including
  hidden assumptions and incentives (Challenge Report); approach comparison does
  not replace that direction-level challenge.
- you-are-here maps repository structure, ownership, and boundaries (Codebase Map).
- previously-on preserves durable decisions and rationale across sessions
  (Handoff Document); a preferred approach is not automatically an accepted decision.
- Potentially affected interfaces may be advisory concerns only. Do not classify
  the nine Interface Check surfaces or claim a formal contract review occurred;
  read-the-contract owns Contract Review, not this Decision Record.

These boundaries do not automatically activate a pipeline. Missing siblings do
not prevent supported comparison; do not reconstruct their unavailable procedures.
No additional decision-specific hard gate is introduced. An unsupported choice
stays unresolved while supported analysis can continue. Baseline G6/G7
human-authority gates have no escape for restricted execution or compatibility
exceptions; a recommendation grants neither. Structural checks establish no
recommendation quality, sound tradeoff analysis, or reliable routing. Comprehensive
behavioral evaluation remains deferred to practical and targeted evaluations.
