# Friction log

Source: SPEC Appendix B. One line per entry:

`date | type | skill | prompt | what happened | proposed change`

Types: `misfire` (unnecessary activation), `miss` (missing activation), `heavy` (excess ceremony), `wrong` (incorrect output), `inherited` (propagated upstream error), `opaque` (reasoning not followable).

Every baseline or skill change must be traceable to an entry. Milestone 1 has one blocked behavioral attempt; see evals/results.md.

2026-10-20 | opaque | baseline | Add engineering practices to the baseline | Baseline did not require concrete justification when invoking principles or patterns, adding structural costs, or abstracting duplication; specification amendment requested, not an observed evaluation result | Add three always-on practices-as-tools rules in SPEC 0.3 section 4 and BASELINE.md; preserve existing rules and the 40-line cap

Initial baseline provenance (2026-10-20): Milestone 0 extracted SPEC section 4 verbatim, with no rule changes. This bootstrap record is not an observed routing miss and must not enter evaluation metrics. Record subsequent behavioral changes using the format above.

Milestone 1 bootstrap provenance (2026-10-20): initial skill/template derived from SPEC 3.5, 3.6, 8 and 9.1; no behavioral tuning claimed. This bootstrap record is not an observed routing result.

2026-10-20 | opaque | think-before-you-commit | Milestone 1 Case A1 | Codex read commands rejected by execution policy; returned a disclosed partial plan with nine uncertain surfaces; no inspection evidence available | Repair evaluation environment and retain full redirected traces before judging skill behavior; do not weaken loading gates
2026-10-20 | opaque | think-before-you-commit | Milestone 1 matrix | Claude Code absent on Windows and both agent CLIs absent inside WSL; remaining sessions not executed | Provide isolated agent runtimes with working read tools; keep matrix blocked

2026-10-20 | opaque | think-before-you-commit | Windows file smoke | Store python alias is unavailable; bundled Python works; diagnostic provisioning failure is historical and native Get-Content succeeds; .NET ReadAllText is blocked by constrained language mode | Use bundled Python and retain the successful native trace; no sandbox weakening or reinstall
2026-10-20 | opaque | think-before-you-commit | Windows isolation probes | skills.config folder paths did not remove skills; SKILL.md paths plus skip_host_skill_discovery and disabled plugins leave one skill; global AGENTS.md remains visible despite project_doc_max_bytes=0 | Keep per-invocation controls and captured inventories; disclose residual global guidance instead of claiming complete isolation
2026-10-20 | wrong | think-before-you-commit | Windows reference smoke launcher | Disabled MCP table without command failed schema loading before any agent session | Add an inert command to the disabled per-invocation MCP entry; preserve failed startup artifacts
2026-10-20 | wrong | think-before-you-commit | Windows B1 negative control | HTTP unaffected correctly, but new controller constructor dependency changed surface 2 and justified a contract-review handoff, confounding the intended negative control | Seed B with an existing injected presenter and present method; preserve signatures and wiring; rerun fresh without changing expectations or skill instructions
