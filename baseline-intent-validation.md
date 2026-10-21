# Baseline conversational intent revision — SPEC 0.11

Date: 2026-10-21.

The user reported conversational repetition and unnecessary ceremony. Added the
requested rule verbatim immediately after Answer first in Partner contract and in
SPEC's canonical baseline. No existing baseline instruction was removed or rewritten.
SPEC clarifies that contextual yes does not waive restricted authorization and that
required reasoning/pushback remain substantive. No skill was changed or begun.

## Files

- BASELINE.md: one new Partner contract instruction.
- SPEC.md: matching canonical instruction, v0.11 revision and measured budget exception.
- friction-log.md: user-reported friction and change provenance, not invented trace evidence.
- tests/test_baseline_intent.py: two static placement/content and safeguard regressions.
- evals/baseline-intent-cases.md: four conversation cases with expected outcomes and
  failure criteria: settled decision, venting, yes to implementation, detailed scrutiny.
  Includes controls for new risk evidence and insufficient restricted authorization.
- baseline-intent-validation.md: this report.

## Validation

- Approved outside-sandbox `python -m unittest discover -s tests -q`: **96 passed**.
  Includes canonical byte equality, non-empty-line cap, baseline structural/reliability/
  reconciliation/size tests, new intent tests, installers and skill packaging tests.
- Initial sandbox run: 96 tests attempted, 75 error records, including subtests and
  cleanup; Windows WinError 5 temporary-fixture access denials. The approved rerun
  resolved the environment failure. This was not observed agent misbehavior.
- `python scripts/check-references`: checked 13 skills, zero changes/drift.
- `python scripts/sync-references`: 13 skills, zero changes.
- `git diff --check`: passed; Git emitted a friction-log CRLF-to-LF normalization
  warning, consistent with repository LF attributes.
- `python scripts/check-baseline`: **exit 1, token ceiling exceeded**, not a pass.
  Complete UTF-8 baseline including Markdown and final newline: **1,223 tokens**,
  **38 non-empty lines**, **45 physical lines**, measured with **tiktoken 0.14.0 /
  o200k_base** using the previously retained isolated tokenizer and cache. Exact
  agent tokenization may differ. Previous baseline: 1,146 tokens / 37 non-empty
  lines. Increase: 77 tokens / one line. The 40-line cap passes; provisional
  900-token ceiling exceeded by 323; 600–700 target also exceeded.

SPEC section 4 continues the documented exception: retain existing safeguards,
routing, uncertainty, reasoning, evidence and authority, and the new explicit
required-risk/gap/check-results carve-out. Compressing these to offset the new
rule risks weakening guarantees. No threshold was relaxed or checker bypassed.

## Evidence limits

Static preservation and canonical consistency checks passed. The instruction
explicitly retains necessary risks, gaps and check results; existing uncertainty,
verification and justified-pushback instructions remain intact. These facts establish
written consistency, not reliable conversational intent recognition.

The four new behavioral cases are **specified, not executed**. No new agent behavior
was observed, so no new behavioral failure or pass is claimed. The friction source
is the user's report; historical behavioral failures and reports remain unchanged.
Fresh multi-turn captures with model/settings/inventory and tool evidence are still
needed to assess actual behavior, including pending-offer context and authority
controls. No installed baseline was refreshed, and no cross-agent reliability or
improvement over the prior baseline is established.
