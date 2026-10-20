# Review Findings / Security Findings

If consuming artifacts, open with:
`Upstream: <names> | Re-derived: <load-bearing claims and actual checks>`

## Scope and intent

Mode; request; diff base/target and inspected files, or security area and selected
trust boundaries. Established intent and source/AC trace, or one-line `inferred`
intent with confirmation request. Inspection limits and exclusions.

## Intent against implementation

Expected → actual behavior, supporting code/tests, unmet criteria. For standalone
security without a diff state why intent comparison is not applicable.

## Independent Interface Check

Evidence per surface from the diff; expand affected/uncertain surfaces with
consumers, search limits, required investigations, and scoped contract handoffs.
Use collapsed form only when justified. No diff: not applicable unless a scoped
classification is needed. Missing required reference: all nine uncertain and
assessment incomplete. Distinguish completed Contract Reviews from dependencies.

## Plan drift

Planned → actual effects and evidence, including unpredicted surfaces. No Plan:
comparison unavailable. Agreement alone is not independent evidence.

## Findings

For each: severity, file/line or other primary evidence, concrete trigger/path,
expected vs actual result, impact, suggested repair, verification, and blocking
status/reason. Severity: critical (broad compromise or catastrophic loss), high
(significant exploit or core behavior failure), medium (bounded consequential
failure), low (minor defect). Calibrate to demonstrated impact; severity and
compatibility blocking are separate decisions. Say when no findings are supported.

Security findings additionally name attacker capability, trust boundary, existing
defenses and why they fail. Include: **This assessment reviews selected code paths
and trust boundaries; it is not a comprehensive security audit.**

## Compatibility and exceptions

Per affected/uncertain surface: resolved/unresolved, plausible impact, material-risk
conditions with evidence, compatibility window including old data/mixed versions
and rollback, and blocking conclusion. Human exception record/source, named break,
surfaces, consumers, impact, grantor/date and conditions if relevant. Proposals
are never grants. No exception needed: state why.

## Verification and open questions

Checks actually executed with outcomes and evidence; inspected-only, failed,
blocked, and unrun checks separately. Use `inferred`, `assumed`, `unknown` where
needed; re-surface every load-bearing assumption and unsupported upstream claim.
Name evidence or investigations that could change the conclusion.

## Recommendation

One of the four verdicts from SKILL.md; explain blockers or exception scope.
Preliminary intent confirmation stays explicit. Standalone security verdict is
limited to inspected paths. Recommendation is not authorization to merge/deploy.
