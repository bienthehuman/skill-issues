# Prompt Refinement implementation verification — 2026-10-22

Implemented against SPEC v0.12 sections 3.3–3.6, 5, G8, 9.3, 10, 11.8 and
decision 2. Initial `git status --short --untracked-files=all` was empty at
`a5beb5fb9720b5f05285c87165e4d17db2b340b1`. Ignored `.local/`, historical
evaluation captures, caches and local audit files were present and preserved.
SPEC.md, BASELINE.md, PROJECT_STATE.md and existing skill contracts were not edited.
The state record's historical untracked-performance claim is stale against this
initial Git inspection; it was not treated as authority or rewritten. No commit/push.

## Files and behavior

- `skills/garbage-in-garbage-out/SKILL.md`: explicit refinement intent only;
  ordinary implementation, discussion, requirements, approach selection and settled
  planning excluded. Three integrated stages, proportional four-lens depth, G8,
  source/evidence discipline, complete reusable prompt and strict stop.
- `skills/garbage-in-garbage-out/references/prompt-refinement.md`: private Markdown
  template for understanding, four lens findings, assumptions/open questions and
  complete refined prompt; unresolved consequential drafts remain partial.
- `evals/prompt_refinement.py`: nine focused cases using existing preparation and
  capture infrastructure. Requirements/planning controls install the appropriate
  real sibling; other cases install only refinement. Evaluated prompts contain no
  rubric reminders. Code, research and ordinary discussion are represented.
- `tests/test_garbage_in_garbage_out.py`: standalone bytes/relative links/reference
  policy, fresh-fixture refusal, exact prompt/inventory and manifest integrity.
- This report and the directly relevant friction-log entries record observed
  results and retained failures.

G8 checks available relevant context before questions. Only interpretations that
materially alter approach/risk block dependent finalization. Harmless gaps proceed
with explicit provisional assumptions, while unaffected work continues under a
consequential blocker. Refinement never runs downstream skills or executes the task.
Missing siblings do not block this skill; no shared reference bundle is needed.

## Exact commands and static outcomes

Commands ran in PowerShell from the repository root. Bind the executable as:

```powershell
$py = 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m unittest discover -s tests -p test_garbage_in_garbage_out.py -v
& $py -m unittest discover -s tests -v
& $py scripts/check-references
& $py 'C:\Users\ASUS\.codex\skills\.system\skill-creator\scripts\quick_validate.py' skills/garbage-in-garbage-out
git diff --check
```

- The initial `python --version` and `python -m unittest discover -s tests -p
  test_garbage_in_garbage_out.py -v` could not start the Windows Store alias.
- Bundled-Python focused run: two errors from sandbox temporary-directory access,
  including cleanup `WinError 5`. Approved rerun: **2 tests passed**, 3.382s.
- Full repository regression: **105 tests passed**, 26.323s. This preceded the
  final instruction-only corrections for visible lens findings and context checks.
- Focused rerun after the first corrections: **2 tests passed**, 3.165s.
  Final rerun after the G8/low-risk fixture correction: **2 tests passed**, 3.290s,
  including all nine fixtures for both host layouts (18 preparations).
- Standalone folder copies in `.agents/skills` and `.claude/skills` preserve exactly
  the entrypoint/private template, resolve local links and need no sibling. Sync,
  check and update policy operations leave their private bytes unchanged.
- Final `scripts/check-references`: **16 skills, zero changes**, exit 0.
- `quick_validate.py`: **blocked**, missing `yaml`/PyYAML; no dependency installed.
  Repository packaging checks do not substitute for that validator.
- `git diff --check`: passed. New untracked sources also received direct inspection;
  default Git diff alone does not cover their contents.

## Behavioral commands and capture controls

```powershell
& $py evals/prompt_refinement.py --case clear --run-id refinement-clear-20261022-1 --output-root .local/refinement-runs
$cases = @('clear','low-risk','consequential','code','research','trivial','requirements','planning','discussion')
foreach ($case in $cases) {
 & $py evals/prompt_refinement.py --case $case --run-id "refinement-$case-20261022-2" --output-root .local/refinement-runs
 if ($LASTEXITCODE -ne 0) { break }
}
$cases = @('clear','low-risk','consequential')
foreach ($case in $cases) {
 & $py evals/prompt_refinement.py --case $case --run-id "refinement-$case-20261022-3" --output-root .local/refinement-runs
 if ($LASTEXITCODE -ne 0) { break }
}
$cases = @('consequential','low-risk')
foreach ($case in $cases) {
 & $py evals/prompt_refinement.py --case $case --run-id "refinement-$case-20261022-4" --output-root .local/refinement-runs
 if ($LASTEXITCODE -ne 0) { break }
}
```

The first capture was blocked during sandbox fixture preparation: baseline-install
subprocess exited 1. Its empty output directory and partial temporary fixture were
not deleted; the traceback is retained in the chat. All subsequent captures use
fresh IDs and approved temporary-fixture access, with the evaluated agent still
read-only and approval `never`. No reminders were sent. Original failures remain
under ignored `.local/refinement-runs/`; do not overwrite them.

Codex CLI **0.163.0-alpha.10.2**; requested model/reasoning overrides are null
(CLI defaults, not a claimed pinned model). `run.json` records commands, version,
inventory, settings, hashes and fixture path; JSONL retains tool events, final
responses, stderr and usage. All nine `-2` captures exited 0, established expected
inventory, and reported fixture/canonical bytes unchanged. Exit status alone was
not counted as behavioral success. Successful tool outputs and final artifacts
were inspected. Global instructions remain present; discovery suppression is not
complete instruction isolation. No comprehensive evaluation was reopened.

## Original focused trace review

| Case (`refinement-<case>-20261022-2`) | Observed result | Trace evidence |
|---|---|---|
| clear | Routing, brevity, reusability and stopping pass; **miss**: primary material and independent verification not separately observable in the compressed assessment. | `item_2` entrypoint, `item_3` template; final short prompt, no translation execution. |
| low-risk | Casual explicit request activates; next-meeting assumption visible, no blocking question, original reminder preserved; four lens findings can be mapped to prose but are not labeled. | `item_2` entrypoint, `item_3` template; no reminder written/executed. |
| consequential | Partial draft, merge/delete/flag question and duplicate-only limit preserved; **G8 miss**: no available task-context inspection before asking. | `item_2` entrypoint and `item_3` template only; correct question alone does not pass full G8. |
| code | Four lenses meaningfully reflected in producer/consumer inspection, source-based methods and diff/search verification; complete prompt preserves status/validation/error and dependency/schema/feature exclusions. No execution. | `item_2` entrypoint/listing; `item_3` template, fixture notes, manifest and application source reads. |
| research | Inspects NOTES.md; corrects false primary-study premise, attributes summary, retains population/no-invented-measurement exclusions, proposes source tracing and reproducible calculations without claiming execution. Complete prompt; all four lenses present. | `item_2` entrypoint, `item_3` notes, `item_4` template. |
| trivial | No refinement activation or artifact; inspects typo only. Actual edit blocked by read-only sandbox, so this is a routing pass only. | `item_2` greeting read; no skill/template read. |
| requirements | Uses define-done and produces provisional Requirements, no refinement activation. Quality of that sibling artifact is outside this evaluation. | `item_2` sibling entrypoint; `item_3` sibling template/listing; `item_4` sources. |
| planning | Uses think-before-you-commit and produces Implementation Plan, no refinement activation. Other plan-format issues are outside this task. | `item_2` sibling and its three references; `item_3` source inspection/search. |
| discussion | Brief explanation, no refinement artifact, skill read or tool use. | Final response; no command events. |

After the stable `-2` batch completed, the skill/template were narrowly corrected
to make all four lens findings visible even in concise output and to require actual
accessible task-context inspection before a blocking question. Earlier passing
cases are evidence for the earlier bytes, not reruns against the corrected version.

## Corrective capture review

The three `-3` captures exited 0 with expected inventories and unchanged
fixture/canonical bytes. Each successfully read entrypoint (`item_2`) and template
(`item_3`). Clear now has four concise labeled, task-specific findings and a
complete prompt without executing translation. Low-risk also shows all four
lenses, but chose wording requiring no assumptions; it does not establish the
assumption path on that version. Consequential **failed again**: no task-context
read, no blocking question and an unqualified final prompt deferring clarification
to the executor. This is a retained regression, not a pass.

After all `-3` captures finished, added an explicit instruction not to move the
current G8 decision into the eventual executor's task. The low-risk fixture was
also clarified with "Use our usual language" so an actual harmless unknown must
be handled, rather than treating an optional next-meeting addition as a missing
fact. Original prompts/manifests remain retained. `-4` runs use these final bytes.

Both `-4` runs exited 0 with expected inventory, fixture unchanged and canonical
unchanged. Trace review:

- **Consequential: pass for G8.** `item_2` reads the entrypoint, `item_3` reads
  the template and lists available context, `item_4` successfully reads NOTES.md,
  prompt.txt, FIXTURE.md and AGENTS.md. Final response states the context did not
  resolve merge/delete/flag alternatives, asks the focused question and provides
  unaffected requirements as a clearly partial refinement. Four task-specific
  lens findings are visible; no cleanup or sibling invocation occurred.
- **Low-risk: pass for provisional assumption/proceeding.** `item_2` and `item_3`
  read entrypoint/template. Final response marks usual language unknown, offers
  an optional prior-message example, and explicitly defaults provisionally to
  friendly English when no example is provided. No blocking question or execution.
  Four lens findings and a copyable prompt preserve the reminder's purpose.
  The optional example slot is unnecessary for the fallback path but does not
  require an answer before reuse; no evidence claims that an example was supplied.

Across all **14 completed captures**, inventory and hash audits passed. These
include retained behavioral failures; this count is not a count of passing cases.
No auto-execution or downstream skill read was observed in any positive case.
The three original positive routing cases clear/low-risk/consequential plus code
and research activated; four negative cases excluded refinement. Only the two
ambiguity cases were rerun against the final G8 wording. Clear passed on the prior
revision; negative/code/research routing was not repeated after the narrow fixes.

## Remaining limits and specification discrepancies

No contract discrepancy was identified in source inspection. The original observed
misses above are behavioral failures, not waived requirements. Standalone folder
copies do not establish Claude execution or reliable host discovery. Missing-input
and unreadable-template fallbacks, repeated trials, sibling-free comparison controls,
fully isolated runs, downstream integration and full SPEC 11.8 comparison evaluation
remain unrun. The template cannot guarantee reasoning quality. Raw captures are
local ignored files and will not travel with a checkout; preserve separately if needed.
PROJECT_STATE.md remains unchanged as requested and therefore does not reflect this
new implementation. This is focused provisional evidence, not full behavioral validation.

Recommended next action: implement `i-dont-know` under its canonical standalone
contract, then perform the separately required complete-inventory readiness assessment.
