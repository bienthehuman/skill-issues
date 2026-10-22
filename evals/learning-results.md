# i-dont-know implementation and focused validation

Date: 2026-10-22. Scope: learning entrypoint, private Learning Notes template,
focused fixtures/rubric and packaging tests. No comprehensive integration restart,
commit, push, sibling contract change or canonical specification/baseline edit.

## Files and behavior

- `skills/i-dont-know/SKILL.md`: activates for conceptual learning and conceptual
  comprehension checks; excludes factual lookups, implementation, existing-failure
  debugging, review, task-scoped orientation, requirements and behavior verification.
- `skills/i-dont-know/references/learning-notes.md`: private content guide covering
  direct answer, first principles, progressive terminology, useful example, model
  limits and next topic. Fields combine into prose for simple questions.
- `evals/learning.py`: 12 focused prompts and fresh fixture preparation, reusing
  existing baseline installation, manifests and Windows capture infrastructure.
- `evals/learning-cases.md`: trace-review criteria, including multi-turn limits.
- `tests/test_i_dont_know.py`: standalone copies, links, reference policy and
  manifest integrity for both host layouts and every fixture.
- This report records results and retained gaps.

The workflow answers first, infers level from context, proceeds without a level
questionnaire, explains relevant first principles, introduces terms as needed,
uses examples proportionally, states model limits and recommends one next concept.
Evidence conventions and upstream sanity checks distinguish teaching models from
inspected or executed system behavior. No sibling or shared bundle is required.
Comprehension checks are opt-in: ask a scenario, wait for a prediction, reveal
reasoning afterward. Already supplied predictions are evaluated directly.

## Initial state and preservation

Initial `git status --short --untracked-files=all` and `git status --porcelain=v1`
were empty. Ignored prior work existed (including `.local`, prior captures and
Python caches). A pre-edit SHA-256 inventory of 2,026 existing files outside
`.git` is retained at `.local/learning-initial.json`; no existing file was replaced
to implement this skill. Preserve that ignored inventory and the captures below.
Final comparison is recorded below; PROJECT_STATE.md is deliberately untouched.

Final SHA-256 comparison: **zero pre-existing files changed or removed**, including
tracked, untracked and ignored files covered by the initial inventory. Final
`git diff --check` exited 0; explicit trailing-whitespace inspection of all six
new files found none. Final status lists only the six intended new files.

## Commands and observed results

PowerShell executable binding for the exact commands below:

```powershell
$learningPython = 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $learningPython -m unittest discover -s tests -p test_i_dont_know.py -v
& $learningPython scripts/check-references
& $learningPython scripts/check-baseline
& $learningPython C:\Users\ASUS\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills/i-dont-know
& $learningPython evals/learning.py --case short --run-id learning-short-20261022-1 --output-root .local/learning-runs
& $learningPython evals/learning.py --case quiz --run-id learning-quiz-20261022-1 --output-root .local/learning-runs
& $learningPython evals/learning.py --case short --run-id learning-short-20261022-2 --output-root .local/learning-runs
git diff --check
git status --short
```

- First unittest attempt in the sandbox: **errors=2**, WinError 5 creating/cleaning
  temporary fixtures. Retained as an environment failure, not behavioral failure.
  Authorized execution outside the sandbox passed **2 tests in 4.321s**. Final
  rerun after the wording correction passed **2 tests in 3.875s**.
- Both tests verify standalone `.agents/skills/i-dont-know` and
  `.claude/skills/i-dont-know` copies, private links contained within the bundle,
  byte equality and reference synchronization/check/update as no-ops. All 12
  fixtures were prepared for each host, with expected sibling inventory only
  for routing controls, prompt fidelity, SHA-256 manifests and refusal to reuse
  destinations. These are packaging results, not Claude execution results.
- `scripts/check-references`: **exit 0**, 17 skills, zero changed files.
- `scripts/check-baseline`: **exit 0**, estimated 1,879 tokens against a 900-token
  ceiling; checker explicitly reports ceiling status **unknown**. This is not
  demonstrated baseline token compliance; unchanged pre-existing limitation.
- Authoring validator: **exit 1**, `ModuleNotFoundError: No module named 'yaml'`.
  No dependencies installed to work around it. Frontmatter and content were
  inspected manually; this does not substitute for a validator pass.
- Bare `python` initially resolved to an inaccessible WindowsApps alias. The
  bundled executable above ran successfully. A trace-summary helper also failed
  once on Windows cp1252 decoding; rerunning with explicit UTF-8 succeeded.
- `git diff --check`: exit 0 before report creation; final repeat below. New
  files are untracked, so this command alone does not inspect their whitespace.

## Behavioral observations and retained failure

Captures are ignored local evidence at `.local/learning-runs/<run-id>/`:
`run.json`, `inventory.json`, `manifest.json`, `prompt.txt`, `trace.jsonl`,
`stderr.txt`, `final.md`. Do not overwrite them with corrective runs.

All three used Codex CLI **0.163.0-alpha.10.2**, fresh ephemeral sessions,
read-only fixtures and the existing runner's default model/settings (recorded in
traces, not pinned by this task). Intended skill inventory was established;
global AGENTS instructions remained present. Under-development feature warnings
were emitted. These are not fully instruction-isolated comparisons.

For each trace, line 6 records successful entrypoint reading, line 8 successful
private-template reading, and line 9 the final response. Line 4 announces skill
use before the answer: answer-first is observed in the final explanation, not
literally across all commentary/tool activity.

| Run | Observed result |
|---|---|
| learning-short-20261022-1 | **Partial/failure retained.** Implicit activation, four sentences, direct answer, B-tree definition, useful analogy, index costs/selectivity limits, no quiz. Omitted both inferred-level statement and next learning topic. Fixture and canonical hashes unchanged; exit 0. |
| learning-quiz-20261022-1 | Earlier bundle explained atomicity first, stated beginner level, defined commit/rollback, used transfer example, limited atomicity to database effects, named isolation next, then posed one stock-count scenario without revealing its answer. Fixture unchanged; exit 0. **Canonical hash audit false:** author added the short-response clarification while this run was still finalizing. Manifest/fixture retain the original bundle. Treat as limited evidence for that bundle, not a clean final-version pass. No user-prediction follow-up was executed. |
| learning-short-20261022-2 | After a narrow instruction to compress rather than omit required fields: four sentences, direct answer, beginner-level assumption, book-index analogy, B-tree defined, large-result-set scan limitation, index selectivity defined as next topic with rationale. No quiz. Both fixture and canonical hashes unchanged; exit 0. Focused final-version short-case pass only. |

The short-case correction does not establish improvement across other cases.
Learning quality and technical completeness still require broader evidence.
In particular, the brief index explanation is a simplified common-index model,
not a claim about every index implementation or a particular query plan.

## Unrun work, discrepancies and next action

Unrun: remaining ten behavioral cases (beginner, experienced, lookup,
implementation, debug, orientation, requirements, verification, prediction and
evidence); live two-turn quiz continuation; final-version quiz rerun; Claude
behavior; repetitions, skill-free comparisons and comprehensive integration.
Static tests exercise fixture preparation, not those prompts' routing/teaching.
No comprehensive test suite was restarted. Static passes do not establish full
behavioral reliability, integration readiness or authorization to freeze/tag.

No requirement change to SPEC 9.3 was needed. PROJECT_STATE.md's inventory is
stale: it lists garbage-in-garbage-out as absent although its entrypoint/template
were present on inspection. With this addition the reference checker sees 17
skills, but SPEC 11.9 requires a separate readiness assessment; inventory alone
does not satisfy it. SPEC 3.3's routing table does not list the learning entry,
while 9.3 defines it; this skill follows 9.3 without editing canonical files.

Recommended next action: perform the separate SPEC 11.9 focused structural
integration-readiness assessment, retaining these behavioral gaps explicitly.
That is a recommendation, not work performed or a freeze/tag grant.
