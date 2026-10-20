# Prove-it implementation validation

Date: 2026-10-21. Scope: provisional standalone skill packaging and structural
validation. No agent-behavior evaluation was executed. Comprehensive behavioral
evaluations are deferred by the author until real portfolio development.

## Implementation

- `skills/prove-it/SKILL.md`: activation/exclusion, three modes, input sanity
  checks, standalone fallbacks, evidence rules, boundaries, and handoffs.
- `skills/prove-it/references/test-set.md`: private Markdown artifact template.
- `tests/test_prove_it.py`: isolated copying into Codex/Claude skill locations,
  local-link resolution, byte preservation, and synchronization isolation.
- `friction-log.md`: bootstrap provenance and documentation maintenance follow-up.
- This report records validation and limitations; it is not behavioral evidence.

No shared reference, sibling skill, installer change, runtime dependency, or
automatic artifact validator was added. SPEC.md, BASELINE.md, existing skills,
README.md, and docs/development.md were left unchanged.

## Contract inspection

Inspected the new entrypoint and template against SPEC sections 3.5–3.6, 5, 8,
9.1, and 10 and the supplied implementation request. This is author inspection,
not evidence that an agent follows these instructions.

Verification maps tests to AC-n and reports satisfied/failed/unverified criteria.
Without criteria, the fallback is characterization rather than invented intent.
Regression accepts minimal failure evidence without a Root Cause Report and
asks for original-failure reproduction and fail-without/pass-with comparison
where feasible; unsafe or unavailable comparisons remain gaps. Characterization
records captured current behavior and intentionally preserved known bugs, without
equating passing tests with correctness against unstated requirements.

The template includes mode/scope, inputs/evidence, tests/expectations,
traceability/outcomes, execution evidence, gaps, intentionally captured bugs,
and bounded conclusions/handoffs. Proposed/written/executed tests are distinct;
execution distinguishes passed, failed, blocked, and unrun, including assertion
versus setup failures. It uses the canonical upstream envelope and evidence
labels. The skill itself contains the evidence definitions so its standalone
operation does not depend on another installed skill's references.

No consequential specification conflict was identified. G1 is described as a
downstream refactor gate; no extra gate requiring new tests was invented.
G6/G7 retain human authority. No Interface Check or shared authorization bundle
is required by the section 3.6 loading map for this skill.

## Actual commands and outcomes

Commands ran from `C:\dev\projects\skill-issues`. Python below means:
`C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.

| Check | Observed result |
|---|---|
| `python -m unittest discover -s tests -v` (initial sandbox attempt) | Failed: 34 tests attempted, 39 error records, including setup/cleanup PermissionError (WinError 5) in sandbox temporary directories. This was an environment failure, not a behavioral evaluation. |
| Same command, approved outside-sandbox rerun | Passed: 34 tests in 13.375s, OK. Includes both new packaging tests and existing foundation/contract/review fixture checks. |
| `python scripts/check-references` | Exit 0: Checked 4 skill(s); 0 file(s) changed. |
| `python scripts/sync-references` | Exit 0: Synchronized 4 skill(s); 0 file(s) changed. |
| `python C:\Users\ASUS\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills/prove-it` | Blocked at import: ModuleNotFoundError: No module named 'yaml'. Validator did not run; no dependencies were installed. |
| `git diff --check` | Exit 0; no whitespace errors. |
| `git diff -- SPEC.md BASELINE.md skills/think-before-you-commit skills/trust-issues skills/read-the-contract` | No output: protected tracked files unchanged. |

The isolated packaging test copies only prove-it into each host's conventional
skill directory, compares all bytes, and resolves every Markdown link within that
copy. It checks the frontmatter name and activation/exclusion presence without a
YAML parser. The synchronization test separately supplies canonical references
to the existing packaging tool, verifies it requests no shared copies for
prove-it, preserves the private template, and rejects accidental shared bundles.
That tool fixture is not a dependency of the installed skill.

## Unexecuted checks and reliability limits

- Skill-creator metadata validation remains blocked by unavailable PyYAML; the
  basic frontmatter assertions and direct inspection are narrower checks.
- No live host loading/discovery, implicit routing, mode execution, inherited
  error probes, assertion-quality probes, or cross-agent behavioral evaluations
  were run. No representative behavioral fixtures were added in this phase.
- Structural tests cannot establish adherence, correct test selection, honest
  evidence reporting, reproduction quality, or downstream detection of broken
  behavior. Those remain to be evaluated during portfolio use.
- Existing historical evaluation evidence/failures remain untouched. These
  packaging results do not clear outstanding Wave 1 exit criteria.
- README.md and docs/development.md have stale implementation counts and
  milestone/version wording; follow-up maintenance only, deliberately unedited.

The bundle is structurally ready for provisional use, with behavioral reliability
unproven and the optional general skill validator blocked as recorded above.
