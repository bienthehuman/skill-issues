---
name: define-done
description: |
  Turn an unclear feature request into testable Requirements.
  Use when: intended behavior or outcome is insufficiently defined, acceptance criteria need establishing or clarification, important constraints or exclusions are ambiguous, or the user explicitly requests feature requirements definition.
  Do not use when: implementation requirements are already clear, a settled approach needs implementation planning, technical approaches need choosing, general prompt rewriting is requested, or a trivial localized change has an obvious success condition.
---

# Define done

Lens: What exactly are we building?

Inputs: original feature request or desired behavior, available user constraints
and relevant context; optional Challenge Report. Output: a Markdown Requirements
artifact using [references/requirements.md](references/requirements.md).
Apply the engineering baseline when available. No sibling skill or shared
Interface Check/authorization reference is required.

## Workflow

1. Check what is unclear. Do not turn routine implementation into a mandatory
   requirements workshop. Start from the original request and authoritative
   project material actually available. Without a Challenge Report, proceed
   from the request. Without repository access, use supplied context only and
   name needed primary material; do not invent inspection. If the request itself
   is absent, ask for the desired outcome and return only supported partial work.
2. Sanity-check upstream artifacts against the original request and available
   primary material. Independently re-derive load-bearing claims, including
   Challenge Report assumptions, boundaries, ownership, consumers, and compatibility
   claims when relied on. Shared-origin artifacts count as one source.
   Open an artifact consuming others with
   `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name unsuccessful re-derivations and the conclusions they limit; do not borrow
   confidence from agreement or imply unavailable checks occurred.
3. Identify intended outcome, observable behavior, explicit requirements,
   constraints, non-goals, missing information, and assumptions. Attribute
   user-established requirements; untagged findings need direct supporting
   inspected material. Use `inferred` for conclusions from observed facts,
   `assumed` for unverified premises, and `unknown` when evidence is insufficient
   and no value can be offered. Re-check load-bearing inferred/assumed claims
   where possible; surface every assumption relied on in open questions.
   Keep recommendations separate from requirements. Common industry practice
   alone does not establish a feature, architecture constraint, or business rule.
4. Read `references/requirements.md`, relative to this installed skill directory,
   before drafting. If unreadable, disclose the missing template and produce a
   partial artifact retaining objective, established requirements, AC-n,
   constraints, non-goals, assumptions/evidence, open questions, and limitations;
   do not borrow sibling references or claim complete packaging.
   Assign stable `AC-n` identifiers. Retain IDs when revising an artifact; do not
   renumber or reuse an ID for a different criterion. Link each criterion to the
   original request, available source evidence, or an explicit assumption.
   Testability alone does not make a requirement valid. Describe independently
   verifiable behavior: relevant conditions/inputs, observable expected outcome,
   and verification basis. Include failure/edge behavior only when supported.
   Avoid implementation-task checklists and invented HTTP statuses, error formats,
   permission rules, timing thresholds, or UI behavior. Verification basis names
   how a criterion could be checked; it is not a claim that a test ran.
5. Handle uncertainty proportionally. For reversible low-risk ambiguity, state
   the working assumption and continue with useful provisional `assumed` criteria.
   Unanswerable questions may remain visible as `assumed` criteria; this fallback
   does not supply missing facts. For consequential ambiguity affecting security,
   compatibility, data integrity, user obligations, or significant behavior,
   explain competing interpretations and implications, identify the human
   clarification needed, and link it to dependent AC-n. Leave those conclusions
   provisional rather than silently choosing an interpretation. If no defensible
   provisional outcome exists, record the gap as `unknown` instead of guessing.
   An unresolved consequential question does not block the entire artifact:
   provide supported criteria and identify which depend on the decision. Do not
   claim completeness or finalize dependent requirements as established. Avoid
   a mandatory discovery checklist or requiring every minor answer.
6. Return bounded Requirements. Identify load-bearing criteria, constraints,
   exclusions, and assumptions for downstream independent checking. Preserve
   unsupported or contradictory intent as visible gaps. Writing criteria does
   not establish that they are satisfied. Stop after requirements definition;
   mention optional follow-up only where warranted, without automatically
   activating a pipeline or implementing the feature.

## Boundaries and gates

- garbage-in-garbage-out improves an instruction and produces Prompt Refinement;
  refinement is not confirmed Requirements.
- it-depends evaluates technical alternatives against requirements and produces
  a Decision Record; this skill does not select an implementation approach.
- think-before-you-commit turns a settled approach into an Implementation Plan;
  this skill does not prescribe implementation steps.
- prove-it produces a Test Set with behavioral verification evidence against
  AC-n; this skill defines completion, not evidence of satisfied criteria.
- trust-issues reviews implementation behavior and risks against established
  intent; Requirements are not a review verdict.

Requirements remain independently usable when these skills are unavailable.
Consumers must independently check criterion testability and fidelity to the
original request. Missing siblings do not prevent requirements definition.
No additional requirements-discovery hard gate is introduced. Baseline G6/G7
human-authority rules have no escape; Requirements grant no execution authority
or compatibility exception. Structural checks do not establish requirement quality,
routing accuracy, or reliable uncertainty handling; behavioral evaluation is deferred.
