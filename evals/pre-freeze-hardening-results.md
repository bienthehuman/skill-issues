# Pre-freeze hardening corrections — 2026-10-22

Base revision: `cdc14433dd4536bb301b24076134ec864e636cba` on `master`.
Initial tracked/untracked status was clean; ignored local work was present.
No commit, tag, push, baseline/specification edit or dependency installation.

## Documentation discrepancy

The earlier reconciliation was real: `22674ab43fb8524573fa4e52554d244f587d3917`
(`revise documents and run readiness checks`) exists on local and remote
`feat/readiness-check`. It updates PROJECT_STATE.md, README.md and
docs/development.md to 17 skills. The reflog records that commit followed by a
checkout from `feat/readiness-check` back to `master` at `cdc1443`. The current
branch does not contain the reconciliation. This explains the apparent
contradiction; the audit inspected the actual older documentation on master.

The three documentation corrections were reapplied selectively from that commit,
with current-task provenance/transient-state updates. Its SPEC additions were not
imported. The earlier structural-readiness decision was checked in the completed
Codex chat `Assess integration readiness`, ID
`01a16261-13f2-7a70-83f4-e6447c5cdaeb`: it reports structural readiness at `cdc1443`
and 107 passing tests, while retaining behavioral gaps. Earlier documentation
maintenance results remain explicitly historical, not new test results.

## Portable G2 evidence

[The six-file package](traces/g2-rollback/README.md) contains:

- `original.md`: full prompt/final and selected read evidence from
  `review-exception-first`, which recommends despite the uncovered reverse break.
- `corrected.md`: equivalent material from `review-exception-rule-corrected`,
  which blocks the same break; also includes the four-combination simulation.
- `covered.md`: the broader human-exception control and its simulation.
- `sources.json`: 22 deduplicated exact UTF-8 contents, covering all 16
  manifest-listed fixture files per run and exact captured prompts/finals.
- `manifest.json`: fixture mappings, source/payload SHA-256 hashes, selected
  trace lines/event identifiers and output offsets/hashes; whitelisted provenance.
- `README.md`: interpretation, verification, sanitization and confounders.

The case views normalize display whitespace and fence historical links; they are
not full transcripts. Raw run/config/inventory logs and host paths are omitted.
Exact source bytes remain available in the deduplicated JSON contents. The existing
review report links the package. Original ignored captures were not overwritten.

All source metadata/trace/prompt/final hashes were compared with the retained
captures, all 48 fixture-file mappings matched their archived bytes, and each
selected excerpt matched its recorded successful read or simulation output.
An allowlisted-content review and scan found no host/profile paths or tested
credential patterns; the fixtures and Ada simulation input are synthetic.

Hash checks establish consistency, not authenticity signatures. CLI defaults do
not establish the resolved model/reasoning settings; global instructions remained
visible. The broader control changes both exception scope and deployment notes.
The corrected simulation has a combined-command exit 1 from a following no-match
search, despite emitting all four simulation results. No application integration
or operational enforcement was demonstrated. These limitations are in the package.

## Planning presentation and observed comparison

Only the presentation paragraph and private template changed. The entry metadata,
activation, workflow, authority and gates are byte-identical to HEAD. A combined
ordered table is preferred when suitable: step/prerequisite, files/reason, AC-n,
check/expected result and reversal/limits. The affected-files, verification and
reversibility fields can reference those rows instead of repeating them.
All eleven information fields remain, including Interface Check evidence and the
dedicated Restricted steps field. No baseline or compatibility rule changed.

The existing harness compared retained
`.local/refinement-runs/refinement-planning-20261022-2/` with fresh
`.local/hardening-runs/hardening-planning-20261022-2/`.
The original prompt, application files, baseline and fixture notes match. Manifest
differences are the two planning files plus the refinement skill's two files,
which received historical corrections after the retained run. Neither trace
loads that refinement skill; its different advertised presence is still a
comparison limitation. Both runs used CLI `0.163.0-alpha.10.2`, null requested
model/reasoning overrides, expected inventories, read-only fixtures and visible
global instructions. Resolved settings and complete isolation remain unknown.

Fresh trace line 6 successfully returns the new planning instructions and required
references, before inspection/search output at line 8 and the final plan. Run exit
is 0; fixture and canonical hashes remained unchanged. The result has one combined
table in section 4 and references it from sections 5 and 6. It retains criteria,
nine evidenced surfaces, contract handoffs, rollback limits and Restricted steps.
It remains a plan and does not claim execution or compatibility approval.

The fresh response is **1,081 whitespace-delimited words versus 979** previously.
This demonstrates less duplication in those tables, not a shorter total response
or a measured token saving. It also places the upstream envelope below the title,
contrary to the existing first-line rule. That format miss remains disclosed;
no unrelated behavior correction was added. One nondeterministic static-fixture
comparison does not establish broader improvement or reliability.

## Verification commands and results

Python below means the bundled executable
`C:/Users/ASUS/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`,
with `PYTHONDONTWRITEBYTECODE=1` and `-B`.

| Command/check | Actual outcome |
|---|---|
| `python -B -m unittest discover -s tests -q` | Initial sandbox attempt: 107 tests, 111 temporary-access setup/cleanup errors. Approved outside-sandbox rerun: **107 passed in 28.801s** before the two package tests were added. Final approved full-suite run: **109 passed in 31.431s**. |
| `python -B -m unittest discover -s tests -p test_g2_evidence.py -v` | Initial check caught nested code fences truncating an excerpt view. Switched outer fences to four backticks; final **2 passed** with complete prompt/final/excerpt comparisons. |
| `python -B -m unittest discover -s tests -p test_milestone1.py -v` | Information-contract check passed in sandbox; packaging case hit temporary-access errors. Approved outside-sandbox rerun: **2 passed in 0.785s**. All eleven fields and standalone packaging preserved. |
| `python -B scripts/check-references` | **17 skills, zero changes/drift**. |
| `python -B <system skill-creator>/scripts/quick_validate.py skills/think-before-you-commit` | **Blocked** before validation: missing `yaml`. No dependency installed. |
| `python -B evals/prompt_refinement.py --case planning --run-id hardening-planning-20261022-1 --output-root .local/hardening-runs` | Sandbox preparation failed during baseline installation; no behavioral result. Partial new fixture/output retained. |
| Same capture command with fresh ID `hardening-planning-20261022-2`, approved outside sandbox | **Captured, exit 0**; manually inspected as described above. Evaluated agent remained read-only, approval never. |
| Direct provenance/hash/redaction assertions | Source hashes, archived mappings, excerpt offsets and unchanged planning authority/gates passed. |
| Local documentation links and scope assertions | **25 active local links/anchors passed**; tracked changes remain within scope; SPEC.md and BASELINE.md are byte-identical to HEAD. |
| `git diff --check` and new-file whitespace assertions | Passed. The new package/tests/report are untracked, so their whitespace was checked directly as well. |

The six-file portable package is **99,713 bytes**. A scoped `git add` attempt
could not create `.git/index.lock` in the sandbox; the required outside-sandbox
Git-index approval was declined. No staging retry was made. The six package files,
integrity test and this report remain **untracked**, pending inclusion in version
control by the user. Nothing was committed or pushed, and existing staging was
unchanged. The portable-evidence finding is therefore prepared but not fully
closed: a fresh checkout will not receive these files until they enter a commit.

The initial 2,059-file preservation inventory was written to per-command sandbox
temporary storage, which was unavailable to later commands, including an approved
outside-sandbox lookup. Therefore no exhaustive initial/final ignored-file hash
comparison is claimed. Git scope checks and direct G2 archive/source comparisons
provide narrower preservation evidence. Edits target only the files listed below;
new capture IDs avoid replacing existing evidence. No deletion or cleanup ran.

## Changed files and remaining limits

- `PROJECT_STATE.md`, `README.md`, `docs/development.md`.
- `skills/think-before-you-commit/SKILL.md` and its
  `references/implementation-plan.md`.
- `evals/reviews-results.md`, `friction-log.md`, this report.
- `evals/traces/g2-rollback/{README.md,original.md,corrected.md,covered.md,manifest.json,sources.json}`.
- `tests/test_g2_evidence.py`.

No demonstrated safety, authorization or structural blocker remains among these
hardening findings. Evidence inclusion in version control remains a pre-freeze
follow-up because Git-index approval was declined. The fresh envelope-format miss
is non-blocking and behavioral
reliability remains unestablished; full SPEC 11.7, Claude behavior, repetitions,
controls, complete isolation and live-system evidence remain outstanding. The
optional authoring validator and baseline tokenizer gaps remain unchanged.
No freeze/tag is performed or authorized by this report.
