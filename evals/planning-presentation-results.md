# Planning envelope correction — 2026-10-22

Scope: the planning skill, its private template and this evaluation record only.
Base HEAD remains `cdc1443`; pre-existing tracked, untracked and ignored work is
preserved, including the G2 package. No staging, commit, push or tag.

## Observed failure and correction

SPEC 5.3 requires an artifact consuming upstreams to open with its
`Upstream: ... | Re-derived: ...` envelope. Both retained planning outputs put
`# Implementation Plan` first: the original separate-table case
`refinement-planning-20261022-2` and combined-table case
`hardening-planning-20261022-2`. The placement failure is therefore not shown to
have been introduced by the combined-table optimization.

The template itself placed the title before its envelope guidance. Move that
existing guidance above the title and make placement explicit; the skill's output
step refers to the template without duplicating the envelope format. No new
table, activation rule, authority behavior or compatibility gate was added.

Exact diff against the files at this task's start (the earlier combined-table
changes were already present and are preserved):

```diff
--- before/skills/think-before-you-commit/SKILL.md
+++ after/skills/think-before-you-commit/SKILL.md
@@ -62,9 +62,10 @@
    restricted-action rules as the minimum protection. If the baseline is also
    unavailable, mark authority classification incomplete and defer potentially
    restricted execution pending the rules and human authorization.
-6. Return the plan and stop. Do not implement, execute restricted actions, create
-   a commit, or grant a compatibility exception. Handoffs are requirements,
-   not completed work.
+6. When consuming upstream artifacts, put the template's envelope on the first
+   line, before the title. Return the plan and stop. Do not implement, execute
+   restricted actions, create a commit, or grant a compatibility exception.
+   Handoffs are requirements, not completed work.

 ## Gates

--- before/skills/think-before-you-commit/references/implementation-plan.md
+++ after/skills/think-before-you-commit/references/implementation-plan.md
@@ -1,7 +1,7 @@
+If upstream artifacts were consumed, make this the first line, before the title:
+`Upstream: <names> | Re-derived: <claims and actual source checks>`
+
 # Implementation Plan
-
-If upstream artifacts were consumed, open with:
-`Upstream: <names> | Re-derived: <claims and actual source checks>`

 ## 1. Objective and intended behavior
 <Task, settled approach, AC-n criteria; missing criteria tagged assumed.>
```

## Focused comparison

Used the existing `evals/prompt_refinement.py --case planning` fixture/capture
harness without changing its prompt or adding rubric reminders.

| Capture | Envelope before title | Tables in sections 4–6 | Whole response words | Sections 4–6 words |
|---|---|---|---|---|
| Original `refinement-planning-20261022-2` | Fail | 3 | 979 | 233 |
| Prior `hardening-planning-20261022-2` | Fail | 1 | 1,081 | 273 |
| Fresh `planning-envelope-20261022-2` | Pass | 1 | 1,003 | 269 |

Counts use whitespace-delimited words, not a tokenizer. The fresh response is
shorter than the previous combined-table sample but longer than the original;
even the combined sections contain more words than the original sections.
No general length/token reduction or causal improvement in total length is claimed.

The observable benefit is organization: one step row now holds its files, criteria,
check, expected outcome and rollback limits together; sections 5 and 6 reference
the row instead of repeating separate file/check tables. This reduces repeated
tabular listings and makes per-step obligations easier to follow. Some summary
repetition remains between the steps, scope, risks and rollback sections; those
sections serve distinct purposes. No additional compression was attempted.

Fresh output inspection found all eleven required information fields:

1. Objective and AC-1–3, with the scope assumption identified.
2. Relevant existing implementation and inspected consumers.
3. Assumptions, missing runtime evidence and outstanding contract review.
4. Ordered steps with prerequisites and criteria.
5. Affected files via step references.
6. Per-step checks/expected outcomes and unrun runtime checks.
7. Nine-surface Interface Check with evidence and scoped contract handoffs.
8. Concrete mixed-version risk and a conditional alias alternative.
9. Coordinated reversal, mismatch risk and absence of a planned one-way operation.
10. Dedicated Restricted steps field; no restricted execution planned or authorized.
11. Explicit exclusions.

The response does not claim implementation, test execution, completed Contract
Review or compatibility approval. It acknowledges both old-consumer/new-response
and new-consumer/old-response mismatch. Runtime and operational rollback limits
remain visible. This is inspection of the result, not proof that safeguards will
hold on other tasks.

## Capture provenance and limits

Raw captures remain in ignored local directories:

- `.local/refinement-runs/refinement-planning-20261022-2/`.
- `.local/hardening-runs/hardening-planning-20261022-2/`.
- `.local/planning-envelope-validation/planning-envelope-20261022-2/`.

The fresh directory retains prompt, manifest, inventory, run metadata, full JSONL,
stderr and final response. Fresh trace line 6 successfully returns the corrected
skill/template and both required references; source inspection/search output
follows at line 8, before the final artifact. Final response begins with the
upstream envelope. Run exit 0, expected skill inventory, fixture unchanged and
canonical unchanged were recorded and inspected.

Latest-to-fresh manifests differ only in the two planning files. Prompt, baseline,
application code, notes, exclusions and advertised sibling files match. The older
original capture also predates two refinement-skill corrections, as already
documented by the hardening report; neither trace loads that sibling.

All three runs use Codex CLI `0.163.0-alpha.10.2`, null requested model/reasoning
overrides, read-only evaluated fixtures, approval never and visible global
instructions. Resolved model/settings and complete isolation remain unknown.
These are single samples on a static Laravel/React scaffold, not a runnable app,
repeated reliability trials, an independent holdout or a multi-agent evaluation.

## Commands, validation and preservation

Commands ran from the repository root using bundled Python
`C:/Users/ASUS/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`,
`-B`, and `PYTHONDONTWRITEBYTECODE=1`.

- `python -B evals/prompt_refinement.py --case planning --run-id planning-envelope-20261022-1 --output-root .local/planning-envelope-validation`:
  sandbox fixture preparation failed in the baseline-install subprocess (exit 1),
  before agent execution. The failed run ID was not reused; partial output was
  left in place. This is not a behavioral failure or a pass.
- The same command with fresh ID `planning-envelope-20261022-2`, approved outside
  the parent sandbox: captured with exit 0. The evaluated session stayed read-only.
- `python -B -m unittest discover -s tests -p test_milestone1.py -v`, approved
  temporary-fixture access: **2 passed in 0.915s**. These check all eleven template
  fields and standalone packaging, not agent behavior.
- `python -B scripts/check-references`: **17 skills; zero changes/drift**.
- `python -B <system skill-creator>/scripts/quick_validate.py skills/think-before-you-commit`:
  blocked before validation by missing `yaml`; no dependency installed.
- `git diff --check` and direct whitespace inspection of this new report: passed.

A persistent initial SHA-256 inventory covers **2,075 pre-existing files** outside
`.git`. Final comparison found no missing file and only the two authorized
planning files changed. All other initial contents, including G2 evidence and
retained captures, match. The Git index hash is unchanged. The inventory,
task-relative exact diff and numeric comparison remain under ignored
`.local/planning-envelope-validation/`; no pre-existing capture was overwritten.

## Recommendation

**Retain the combined-table presentation**, for the observed reduction from three
separate step/file/check tables to one table with explicit cross-references and
co-located verification/rollback obligations. Retain the narrow envelope fix.
Do not describe either as proven output-length optimization or broad behavioral
reliability. No further optimization or instruction expansion is justified here.
