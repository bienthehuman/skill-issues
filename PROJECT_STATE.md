# Skill Issues — project state

Reviewed 2026-10-22 against `1845d0b` and the working tree. This is a continuity
record, not a specification, changelog, mandatory workflow, or execution grant.
Repository facts below come from inspected files; human decisions are attributed.

## Current position

- Canonical specification: [SPEC.md](SPEC.md) **v0.12**. Architecture: 17 skills
  in three waves plus one always-on [BASELINE.md](BASELINE.md), not counted as a
  skill. The applicable baseline includes the v0.12 continuity amendment.
- **14 implementations present**, evidenced by each named directory's `SKILL.md`
  and private artifact template under `skills/<name>/references/`:
  - Wave 1 (7/7): `you-are-here`, `think-before-you-commit`, `read-the-contract`,
    `trust-issues`, `prove-it`, `but-it-works-on-my-machine`, `previously-on`.
  - Wave 2 (6/6): `define-done`, `it-depends`, `what-could-possibly-go-wrong`,
    `devils-advocate`, `select-your-battles`, `same-same-but-different`.
  - Wave 3 (1/4): `famous-last-words`.
- **Remaining (no implementation directories):** `are-we-there-yet`,
  `garbage-in-garbage-out`, `i-dont-know`. Their specification entries are not
  implementations. The complete-inventory and integration-readiness milestones
  are not yet established.
- Evidence limits: source presence establishes implementation inventory, not
  behavioral reliability or installed availability in any host. Historical
  structural and targeted Codex results are recorded in [friction-log.md](friction-log.md)
  and [evals/](evals/), including preserved failures and corrective runs.
  [Review results](evals/reviews-results.md) substantiate `trust-issues` delivery;
  [rollout results](evals/famous-last-words-results.md) substantiate the latest skill.
  Those reports retain Claude Code, isolation, repetition, and regression gaps;
  SPEC 11.7 behavioral exit criteria remain unmet. Historical runs were not
  reproduced for this record.
- Continuity reconciliation is present in BASELINE and SPEC (commit `1845d0b`).
  Canonical baseline equality was checked during this record's creation. The
  supplied human history reports static checks passing and seven behavioral
  scenarios unrun: **`assumed` as historical execution/count claims**, not
  independently established by that commit or a dedicated validation report.
  SPEC's v0.12 revision explicitly says behavioral scenarios remain unrun.
  Its baseline size is an estimate; token-ceiling compliance remains `unknown`.
- Known stale summaries: README's early milestone/count wording and
  `docs/development.md`'s two-skill inventory do not describe today's inventory.
  No existing repository-wide current-state record was identified; report/template
  files serve narrower purposes.

## Durable decisions

| ID / status | Decision, rationale and provenance | Reversibility / revisit |
|---|---|---|
| D1 / `current` | Keep the 17-skill, three-wave architecture and separate baseline. Repository basis: SPEC 3.1; specialist responsibilities and standalone fallbacks avoid a mandatory pipeline (3.3–3.6). | Revisable through an explicit specification decision supported by evidence of missing responsibilities or collisions. |
| D2 / `current` | Permit provisional implementation while deferring comprehensive practical behavioral evaluation to portfolio development. Human-reported decision corroborated by SPEC 3.2, 11.9–11.10 and friction records. Finish inventory, assess integration readiness separately, then freeze/tag before portfolio use; structural passes do not waive reliability gates. | Reversible priority choice; resume evaluation at those milestones, or earlier for a consequential observed failure. |
| D3 / `current` | Implement `are-we-there-yet` next. Source: the human's request establishing durable state (2026-10-22), explicitly overriding the original build sequence. No newer established human decision was found in inspected repository records. Purpose: add the missing measured-performance responsibility; the earlier conversation's detailed selection rationale is `unknown`. | Reversible order decision; revisit on a newer human priority or a demonstrated dependency/blocker. Requirement changes require explicit reconciliation with SPEC. |
| D4 / `current` | Establish continuity from repository evidence and recent human decisions; treat handoffs as claims and separate durable decisions from transient work. Repository basis: v0.12 baseline, SPEC 3.3 and Appendix A. | Revisit on observed continuity failures or consequential new requirements. No guarantee of automatic retrieval across chats. |

D3 supersedes the original sequence **for the immediate next action only**;
it does not change skill requirements or establish an order for the final two skills.

## Deferred work

- Comprehensive practical evaluation and outstanding Wave 1 criteria: postponed
  to test the complete workflow during portfolio development; resume after the
  complete inventory, SPEC 11.9 readiness assessment and initial freeze/tag.
  Keep seeded comparisons and original failures; natural use alone is insufficient.
- Claude Code execution and complete instruction isolation: historical reports
  cite availability/environment limits. Resume when suitable access and isolation
  exist; current availability is `unknown`. Folder-copy tests are not host behavior.
- Continuity behavioral scenarios: reported seven unrun; count/procedure not
  independently confirmed here. Recover or define the actual cases and capture
  fresh behavior before asserting continuity reliability.

## Next action

**Implement `are-we-there-yet` under SPEC 3.5–3.6, 5, G3, 9.3 and 10.**
Produce a self-contained skill and private Performance Report template. It accepts
subjective slowness, establishes a baseline before diagnosis, records workload,
data size/environment/cache conditions and bottleneck evidence, and compares one
change at a time with variance and production differences disclosed.

Relevant existing recipients are `select-your-battles` for schema/index design,
`but-it-works-on-my-machine` for incorrect behavior, and `read-the-contract` for
response/pagination changes. They are optional handoffs, not installation
dependencies; SPEC's loading map assigns this skill no shared references.

Completion is observable when the entrypoint and private template exist, satisfy
the canonical authoring/Performance Report contract, preserve G3 and standalone
fallbacks, resolve references in isolated Codex/Claude folder copies, and have
recorded passing relevant structural/packaging/reference checks. Record failed,
blocked and unrun checks explicitly; this does not establish performance gains
or behavioral reliability.

On a future implementation request, Codex can inspect, draft local files and run
permitted non-destructive checks within that request. This record does not initiate
implementation. Changed requirements/priorities or compatibility exceptions need
a human decision; restricted actions need fresh applicable human authorization
under host rules and BASELINE Authority. Historical grants never supply permission.

## Transient state

- Initial `git status --porcelain`: empty (clean working tree).
- This task adds only `PROJECT_STATE.md`; no skill implementation is in progress
  in the observed tree. No commits, pushes, baseline/spec edits or evaluation
  result changes are part of this task. Recheck Git state on resume.

## Maintenance

Update after a completed skill implementation, changed priority, or consequential
decision affecting future work; trivial coding tasks need no update. Verify
repository-derived facts against the then-current tree and record the review
date/revision. Preserve relevant decision IDs/rationale and explicit
`superseded by <reference>` links; refresh transient state instead of preserving
stale work-in-progress claims. Link detailed specifications/evaluation reports
rather than copying them. Keep human reports, `inferred`, `assumed`, and `unknown`
claims distinguishable. If this record is unavailable or potentially stale,
disclose consequential uncertainty and inspect available evidence; do not invent
continuity. Nothing recorded here authorizes future execution.
