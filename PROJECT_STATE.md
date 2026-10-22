# Skill Issues — project state

Reviewed 2026-10-22 against `cdc1443` and the documentation working tree.
This is a continuity record, not a specification or execution grant.

## Current position

- Canonical specification: [SPEC.md](SPEC.md) **v0.12**; separate always-on
  [BASELINE.md](BASELINE.md), including the continuity amendment.
- **All 17 canonical skills implemented**, each with its private template:
  - Wave 1 (7/7): `you-are-here`, `think-before-you-commit`, `read-the-contract`,
    `trust-issues`, `prove-it`, `but-it-works-on-my-machine`, `previously-on`.
  - Wave 2 (6/6): `define-done`, `it-depends`, `what-could-possibly-go-wrong`,
    `devils-advocate`, `select-your-battles`, `same-same-but-different`.
  - Wave 3 (4/4): `famous-last-words`, `are-we-there-yet`,
    `garbage-in-garbage-out`, `i-dont-know`.
- **Implementation phase complete; structural integration readiness established
  at revision `cdc1443`.** The separate read-only SPEC 11.9 assessment on
  2026-10-22 (Codex chat “Assess integration readiness”, ID
  `01a16261-13f2-7a70-83f4-e6447c5cdaeb`) found no consequential structural blocker.
  It reported **107 passing repository tests** on the approved rerun after
  sandbox temporary-directory denials; reference checks covered 17 skills with
  zero drift, nine shared bundles matched canonical bytes, 21 private Markdown
  links resolved, standalone Codex/Claude layouts passed, and baseline extraction
  matched SPEC byte-for-byte. These are prior assessment results, separate from
  the maintenance checks below. This record makes the decision available in the
  repository; the detailed assessment was returned in chat, not a tracked report.
- **Structural readiness is not behavioral reliability.** SPEC 11.7 remains
  unmet. Source presence and folder-copy tests do not establish installed host
  availability, activation, reasoning quality, or authorization compliance.
- Next phase: controlled portfolio-project use under SPEC 11.10, after freezing
  and tagging the reviewed initial implementation. No freeze/tag is established
  by this record or performed by this documentation task.

## Evidence and outstanding limitations

Historical reports retain original failures and corrective runs; none were rerun
as behavioral evaluations during this maintenance task:

- [Initial results](evals/results.md) retain the blocked first attempt;
  [Windows report](evals/windows-20261020/REPORT.md) reports the corrected Codex
  9/9 reference-loading matrix and preserves the confounded original control.
  [Contract results](evals/contracts-results.md) record focused repaired passes.
- [Review results](evals/reviews-results.md) retain rollback-exception and artifact
  envelope failures with partial corrective coverage. [Rollout results](evals/famous-last-words-results.md)
  retain unsupported irreversibility reasoning and fixture confounds; successful
  live recovery is unproven.
- [Verification results](evals/prove-it-results.md) establish packaging, not live
  mode execution. [Performance results](evals/performance-results.md) report four
  focused cases, but no runnable baseline/intervention measurement path, live
  profiling or executed intervention. Its historical 102-test result is unchanged.
- [Refinement results](evals/prompt-refinement-results.md) preserve G8 regressions;
  final corrections cover selected cases only. Missing-input/unreadable-template
  fallbacks, full SPEC 11.8 comparisons and downstream integration remain unrun.
- [Learning results](evals/learning-results.md) retain omitted fields and a
  confounded quiz capture; the corrected short case is a focused pass only.
  Ten remaining cases, final-version quiz rerun and two-turn continuation remain
  unrun, as do repetitions and skill-free comparisons.
- Claude behavioral validation, complete instruction isolation, broad repeated
  trials and skill-free controls, full E1–E5 coverage, ten trivial tasks, real-project
  evidence and comprehensive integration remain outstanding. Earlier specialist
  structural checks in [friction-log.md](friction-log.md) do not establish live
  orientation, debugging, requirements, design, impact, challenge, schema or
  refactoring reliability. Controlled natural use does not replace seeded criteria.
- Continuity scenarios and baseline conversational regression cases remain unrun.
  The earlier human-reported seven continuity cases are an **assumed historical
  count**, not an independently recovered procedure. SPEC v0.12 records them as
  unrun; no cross-chat retrieval guarantee is established.
- Optional authoring validation was blocked by missing PyYAML (`yaml`); manual
  metadata inspection is narrower evidence, not a validator pass. No dependencies
  were added. Historical environment failures remain recorded in their reports.
- Baseline: 39 non-empty lines meet the 40-line cap. The v0.12 **1,879-token
  character estimate** is not a tokenizer measurement; ceiling compliance is
  **unknown**. Historical measured overages and the safeguard-preserving exception
  in SPEC 4 remain in force; do not treat checker exit 0 as token compliance.

## Durable decisions

| ID / status | Decision, rationale and provenance | Reversibility / revisit |
|---|---|---|
| D1 / `current` | Keep the 17-skill, three-wave architecture and separate baseline. Repository basis: SPEC 3.1; specialist responsibilities and standalone fallbacks avoid a mandatory pipeline (3.3–3.6). | Revisable through an explicit specification decision supported by evidence of missing responsibilities or collisions. |
| D2 / `current` | Permit provisional implementation while deferring comprehensive practical behavioral evaluation to portfolio development. Human-reported decision corroborated by SPEC 3.2, 11.9–11.10 and friction records. Finish inventory, assess integration readiness separately, then freeze/tag before portfolio use; structural passes do not waive reliability gates. | Reversible priority choice; resume evaluation at those milestones, or earlier for a consequential observed failure. |
| D3 / `fulfilled` | Implement `are-we-there-yet` next. Source: the human's request establishing durable state (2026-10-22), explicitly overriding the original build sequence. Purpose: add the missing measured-performance responsibility; the earlier conversation's detailed selection rationale is `unknown`. Files now exist; see Current position and the performance validation report. | The immediate priority is fulfilled, not superseded by a new human ordering decision. It establishes no order for the final two skills. Requirement changes require explicit reconciliation with SPEC. |
| D4 / `current` | Establish continuity from repository evidence and recent human decisions; treat handoffs as claims and separate durable decisions from transient work. Repository basis: v0.12 baseline, SPEC 3.3 and Appendix A. | Revisit on observed continuity failures or consequential new requirements. No guarantee of automatic retrieval across chats. |

D3 superseded the original sequence **for that immediate action only**;
it did not change skill requirements or establish an order for the final two skills.
Both have since been implemented; this rationale is retained as decision history.

## Next action

Prepare a reviewed freeze/tag of the initial complete implementation, then use it
in one portfolio project under SPEC 11.10. Record the installed inventory,
agent/model/settings and version with observations in the existing friction log;
preserve failed cases for comparable regression checks. This recommendation is
not authorization to commit, tag, push or execute restricted actions.

## Transient state

The working tree was clean at this task's start; the previously recorded untracked
performance implementation is now committed. This task changes documentation only.
Ignored captures and other existing local work are preserved. No skill or baseline
implementation, comprehensive evaluation, dependency, commit or push is part of it.

## Maintenance verification — 2026-10-22

Newly executed with bundled Python 3.12.14 (`-B`):

- `python -B -m unittest discover -s tests -q`: sandbox attempt ran 107 tests
  with 111 temporary-fixture access error records; approved outside-sandbox rerun
  **107 passed in 28.267s**. No assertion or implementation changes were needed.
- `python -B scripts/check-references`: **17 skills, zero changes/drift**.
- Direct assertions: SPEC 3.1, README and directory inventories equal **17**;
  extracted baseline equals `BASELINE.md` byte-for-byte. All **17 local Markdown
  links** in the four changed documents resolve, including explicit anchors.
- `python -B scripts/check-baseline`: exit 0, **39 non-empty lines**, estimated
  **1,879 tokens**, ceiling status **unknown**; no measured token pass claimed.
- `git diff --check`: passed. Only the four intended Markdown files changed;
  skill implementations, baseline, scripts, tests and historical reports unchanged.

No comprehensive or focused behavioral captures, optional PyYAML authoring
validator, external web-link availability checks or tokenizer measurement were
run here. The existing optional-validator blocker remains unresolved.

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
