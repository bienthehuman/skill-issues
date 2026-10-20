---
name: what-could-possibly-go-wrong
description: |
  Analyze change impact in an inspectable Impact Report.
  Use when: a proposed or implemented change raises a consequential dependency or regression-risk question; a scrutiny trigger fires on a plan or diff; the user requests change-impact or blast-radius analysis; or multiple relevant components, state owners, or integration boundaries may be affected.
  Do not use when: no meaningful scrutiny trigger or impact-analysis need exists; a change is trivial and localized without consequential dependencies; the question is live deployment or operational rollback; the primary need is contract compatibility; or general repository orientation is requested without a proposed change. Multiple modified files alone do not trigger this skill.
---

# What could possibly go wrong

Lens: What in the code and dependencies does this change touch?

Inputs: an Implementation Plan or actual diff; a Codebase Map when available;
relevant repository code and dependencies. Output: a Markdown Impact Report using
[references/impact-report.md](references/impact-report.md).
Apply the engineering baseline when available. No sibling skill or shared
reference is required.

## Workflow

1. Establish the change objective, original request, available inputs and revision,
   scrutiny reason, and smallest useful investigation scope. Sanity-check upstream
   freshness and relevance. A Plan describes intended changes and possible
   impact; a diff evidences actual modifications. Neither proves runtime behavior
   or complete consumer coverage. When both exist, use the diff for actual
   modifications and note material discrepancies from planned scope. Do not
   describe a planned modification as already made. Leave plan conformity and
   merge recommendations to trust-issues.
2. Independently re-derive load-bearing upstream ownership, boundary, and consumer
   claims from actual code and dependency evidence before relying on them.
   Shared-origin artifacts count as one source. An artifact consuming others
   opens with `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name failed or unavailable re-derivations and dependent limits. If an inherited
   claim cannot be re-derived, mark the dependent conclusion `inferred` and name
   that claim; missing facts remain `unknown`.
3. Identify the intended change and observed boundary: relevant code, state,
   contracts, entry points, execution paths, callers/consumers, dependencies,
   integration points, constraints and assumptions. With a Codebase Map, use
   primary evidence to trace relevant dependency paths, expanding only when
   concrete dependencies or potential consequences justify it. As relevant,
   inspect callers/callees, services/modules, persistence and state ownership,
   events/queues/jobs and asynchronous consumers, API/shared-interface consumers,
   configuration/feature flags, frontend/backend interactions, and separately
   maintained or deployed integration points. This is an investigation guide,
   not a mandatory checklist. Stop when task-relevant risks can be meaningfully
   assessed, or further investigation is blocked or disproportionate; record why.
   Do not map the entire repository by default.
   Without a Codebase Map, trace supported direct callers only and explicitly
   report the discovered blast radius as a **lower bound**. Do not expand this
   fallback into an implicit repository map or imply all consumers were found.
   No additional discovered consumers is not proof that none exist. Partial
   searches and unavailable sources never establish complete impact coverage.
4. Identify specific, credible regression scenarios grounded in the change and
   observed dependencies. For each material risk name affected behavior/component,
   failure trigger and scenario, evidence and assumptions, consequence/severity,
   recommended verification that would detect it, and remaining uncertainty.
   Rank by relevance, evidence, and potential consequences, explaining the order;
   use likelihood or confidence only when defensible. Do not invent probabilities,
   arbitrary numerical scores, production traffic, data volumes, or infrastructure.
   Separate investigation coverage from impact severity: a potentially severe
   regression with limited evidence remains a high-consequence uncertainty,
   even when no affected consumer was found. Identify the missing evidence and
   a scoped check to resolve it, without presenting speculation as a defect.
5. Read `references/impact-report.md`, relative to this installed skill directory,
   before writing the report. If unreadable, disclose the missing template and
   return a partial report retaining the fields below; do not borrow sibling
   files or claim complete packaging. Include objective/scope, input provenance,
   observed change boundary, affected components/dependency paths, ranked risks,
   evidence/uncertainty, verification per material risk, coverage/limitations,
   open questions/unresolved dependencies, and handoff considerations. Retain
   every field, using short entries for small changes.
6. Separate observed affected components from `inferred` potential effects,
   `assumed` dependencies, and `unknown` consumers or behavior. Untagged findings
   need directly inspected supporting material or actual checks; attribute user
   reports. `inferred` means concluded from observed facts; `assumed` means an
   unverified premise; `unknown` means insufficient evidence with no value offered.
   Re-check load-bearing inferred/assumed claims where possible, and surface every
   assumption relied on in open questions. Distinguish verification recommended
   from verification actually performed, naming actual commands/results only.
   A suggested test has not passed; inspection alone does not prove runtime
   behavior. Return a bounded assessment with stopping reason and the evidence
   that could change its conclusions.

## Standalone fallbacks

Without repository access, work only from supplied Plan, diff, or other primary
material. Name missing code/dependency evidence and unsupported conclusions;
do not invent inspection or consumers. Without a Plan or diff, identify the
proposed change from the user's description if possible and produce only a
clearly limited preliminary assessment. If the change cannot be established,
request its objective and relevant material rather than inventing code paths.
The no-Map direct-callers-only, lower-bound fallback still applies. Consequential
uncertainty remains explicit and limits conclusions rather than implying safety.

## Boundaries and handoff

Own affected components and regression risks. you-are-here owns Codebase Map
orientation/ownership mapping; think-before-you-commit owns ordered Implementation
Plan steps; prove-it owns Test Set behavioral verification evidence; trust-issues
owns correctness review, plan drift assessment and merge recommendations;
famous-last-words owns Rollout Plan deployment sequencing, operational detection,
rollback and production-specific risks.

Identify a material contract concern by its specific boundary/surface, change,
supporting evidence, known consumers/search limits and open questions; recommend
scoped read-the-contract investigation when warranted. That skill owns Contract
Review compatibility and migration implications. Do not perform the canonical
Interface Check, reproduce or reclassify all nine surfaces, or claim a Contract
Review completed. This bundle needs neither interface-check.md nor authorization.md.

Handoffs are optional work recommendations, not completed assessments. Missing
sibling instructions require naming the limitation and needed inputs, never
reconstructing their procedures. Do not automatically run the complete pipeline.
Downstream consumers must independently re-derive blast-radius claims, especially
lower-bound ones. No impact-specific hard gate is added. G6/G7 human-authority
gates have no escape; follow host permissions and available baseline authority
rules. Analysis grants no restricted execution or compatibility exception.

Structural validation supports provisional standalone use only. Comprehensive
behavioral evaluation remains deferred to complete-workflow portfolio development;
regression-risk detection, routing quality and blast-radius completeness remain
unproven.
