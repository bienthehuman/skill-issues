---
name: devils-advocate
description: |
  Challenge whether an engineering or product direction deserves pursuit and produce a Challenge Report.
  Use when: a direction-level decision warrants substantive scrutiny before significant effort; substantial time, complexity, or resources are being considered; the user explicitly requests a critical challenge to an idea, proposal, or plan; or important value, adoption, feasibility, or consequence assumptions need examination before commitment.
  Do not use when: only a minor implementation detail is at issue, technical implementations of an established goal need comparison, the task is routine coding, debugging, or ordinary code review, or no significant direction-level decision exists. Risks or tradeoffs alone do not activate this skill.
---

# Devil's advocate

Lens: Should this exist, and what would change our mind?

Inputs: a claim, idea, proposed direction, or plan; available objectives,
constraints, and supporting evidence. Output: a plain Markdown Challenge Report
using [references/challenge-report.md](references/challenge-report.md).
Apply the engineering baseline when available. No sibling skill or shared
reference is required. Ordinary engineering conversations do not require a
challenge session.

## Workflow

1. Establish the goal before judging the idea. Identify the intended outcome,
   problem, beneficiaries and affected people, relevant constraints, current
   alternatives (including the status quo where meaningful), and what successful
   adoption or implementation would accomplish. Use the original request and
   available primary context. If the goal is unstated and cannot be reliably
   established, ask what success looks like before issuing a substantive verdict.
   Return only supported context and questions meanwhile; do not invent a goal,
   stakeholder objectives, user demand, business value, or operational constraints.
   Without upstream artifacts, assess the user-provided idea and context directly.
   Without repository access, name the missing sources and do not imply code,
   architecture, or operational details were inspected.
2. Sanity-check upstream artifacts for relevance, freshness, and fidelity to the
   original request. Independently re-derive load-bearing claims from actual
   primary material, including objectives, constraints, ownership, boundary,
   consumer, and rollback claims when relied on. An artifact consuming others
   opens with `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name failed or unavailable re-derivations and their dependent limitations.
   A dependent conclusion not re-derived remains `inferred` and names the
   inherited claim. Shared-origin artifacts count as one source. The proposing
   agent's rationale is not independent evidence.
3. Identify hidden, load-bearing assumptions whose failure would materially
   alter the recommendation. Useful lenses include problem significance, actual
   user need, whether the solution addresses the cause, feasible adoption,
   implementation and maintenance costs, organizational capacity, incentives,
   and whether a simpler intervention achieves most of the benefit. These are
   investigative lenses, not a mandatory checklist. For each important assumption,
   name its evidence basis, dependent conclusion, and what would establish or
   challenge it. Do not manufacture objections to populate the report.
4. Construct the strongest credible counter-case against pursuing this direction,
   engaging with the actual objective and available evidence. Consider opportunity
   cost, complexity, maintenance, deployment/operations, unintended consequences,
   alternatives, and doing nothing only where relevant. A theoretically possible
   failure is not necessarily likely; low-consequence uncertainty alone does not
   justify rejection. Weigh evidence supporting the proposal as seriously as
   evidence against it. The strongest counterargument is not automatically the
   winning argument: explain what it establishes, what it does not, and why the
   balance of evidence supports the recommendation. Strengthen the decision,
   without performative skepticism or reflexive opposition.
   For consequential product or feature directions, compare supported proposal value
   against worthwhile work displaced by pursuing it, including meaningful costs of
   delaying either the proposal or its alternatives. Do not require formal business
   analysis, numerical ROI, or invented estimates.
5. Examine incentives and adoption friction using actual context: existing user
   workflows, training/migration costs, stakeholder incentives, ownership,
   support and maintenance responsibilities, operational capacity, and extra
   steps may matter. Do not invent user behavior or stakeholder preferences.
   If decisive adoption assumptions are unverified, label them and name the
   evidence needed; technical feasibility alone does not establish adoption.
6. Use canonical evidence labels throughout the assessment. Untagged findings
   name directly inspected supporting material; attribute user reports without
   implying independent verification. `inferred` means concluded from observed
   facts; `assumed` means an unverified premise; `unknown` means insufficient
   evidence with no value offered. Re-check every load-bearing inferred/assumed
   claim against available sources. Surface every assumption relied on in open
   questions, linked to its dependent recommendation and needed evidence. Missing
   evidence remains visible; do not invent inspections, tests, or results.
7. With an established goal, conclude with one canonical recommendation:
   - **Proceed:** sufficiently justified under established constraints.
   - **Reshape:** the underlying goal is worthwhile, but the direction needs
     material adjustment.
   - **Drop:** available evidence does not justify pursuing the proposed form.
   Explain why the verdict follows, the decisive assumptions, supporting evidence,
   and what the opposing case establishes. Every verdict identifies concrete
   evidence that would overturn it and the next justified action or investigation.
   When evidence is insufficient, keep the recommendation explicitly provisional
   and name dependent gaps; do not force certainty or manufacture a reason to drop.
   A missing goal still requires clarification rather than a verdict.
8. Read `references/challenge-report.md`, relative to this installed skill
   directory, before drafting. If unreadable, disclose the missing template and
   return a partial report preserving idea, goal/success conditions, context and
   evidence, assumptions, counter-case, incentives/adoption friction, meaningful
   alternatives, verdict/rationale/uncertainty, overturning evidence, next action,
   open questions, and limitations. Do not borrow sibling files or claim complete
   packaging. Keep the report proportional; short fields suffice for simple ideas.
   Return the Challenge Report and stop the challenge; do not execute the proposal.

## Boundaries and gates

- define-done establishes what to build and acceptance criteria (Requirements).
- it-depends compares technical approaches to an established goal (Decision Record).
- think-before-you-commit plans a settled approach (Implementation Plan).
- what-could-possibly-go-wrong analyzes change impact and regression risks
  (Impact Report).
- trust-issues reviews implementation against intended behavior and safety
  concerns (Review Findings or Security Findings).

A Challenge Report may inform Requirements or a Decision Record. Preserve verdict,
load-bearing assumptions, and overturning evidence for optional consumers, who
independently check whether those assumptions still hold. Neither artifact nor
sibling installation is required; do not automatically activate a pipeline or
reconstruct unavailable skill procedures. This report does not substitute for
technical approach comparison, code review, or a formal Interface Check.
No additional challenge-specific hard gate is introduced beyond establishing the
goal before a verdict. Supported analysis may continue while that goal is missing.
Baseline G6/G7 human-authority gates have no escape: recommendations are not human
approvals and grant no implementation, restricted execution, or compatibility
exception authority. Structural validation does not establish useful criticism,
calibrated verdicts, or reliable activation. Comprehensive behavioral evaluation
remains deferred to practical and targeted evaluations.
