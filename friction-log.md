# Friction log

Source: SPEC Appendix B. One line per entry:

`date | type | skill | prompt | what happened | proposed change`

Types: `misfire` (unnecessary activation), `miss` (missing activation), `heavy` (excess ceremony), `wrong` (incorrect output), `inherited` (propagated upstream error), `opaque` (reasoning not followable).

Every baseline or skill change must be traceable to an entry. Milestone 1 has one blocked behavioral attempt; see evals/results.md.

Initial baseline provenance (2026-10-20): Milestone 0 extracted SPEC section 4 verbatim, with no rule changes. This bootstrap record is not an observed routing miss and must not enter evaluation metrics. Record subsequent behavioral changes using the format above.

Milestone 1 bootstrap provenance (2026-10-20): initial skill/template derived from SPEC 3.5, 3.6, 8 and 9.1; no behavioral tuning claimed. This bootstrap record is not an observed routing result.

2026-10-20 | opaque | think-before-you-commit | Milestone 1 Case A1 | Codex read commands rejected by execution policy; returned a disclosed partial plan with nine uncertain surfaces; no inspection evidence available | Repair evaluation environment and retain full redirected traces before judging skill behavior; do not weaken loading gates
2026-10-20 | opaque | think-before-you-commit | Milestone 1 matrix | Claude Code absent on Windows and both agent CLIs absent inside WSL; remaining sessions not executed | Provide isolated agent runtimes with working read tools; keep matrix blocked
