# Milestone 1 integration evaluation

Structural tests and behavioral evaluations are separate. See `results.md` for
actual outcomes. Do not infer a behavioral pass from the test suite.

## Fixtures and isolation

`prepare.py` creates a fresh static Laravel/React inspection fixture, installs only
think-before-you-commit at `.agents/skills/` (Codex) or `.claude/skills/` (Claude),
and invokes the existing baseline installer for the selected agent. No framework
installation or external dependencies are needed. The fixture is closed-world and
not a runnable Laravel app; this limits the evaluation to planning and inspection.
The manifest records hashes of fixture and installed skill files.

A: rename customer_name in OrderResource to customerName and update the React hook.
B: delegate resource construction to a service, preserving HTTP semantics. This
crosses a module boundary, so planning has a legitimate stakes trigger while
surface 1 stays unaffected. Collapse is prohibited by that boundary crossing.
C: A with the disposable bundled Interface Check removed. The canonical source
and repository bundle remain intact. For a post-evaluation restoration, copy the
repository bundle back to the exact installed path in manifest.json, after retaining
its missing-reference trace; never run C again in that restored directory.

Create one NEW destination for each agent/case/repetition (18 destinations):

```sh
python evals/prepare.py --destination /tmp/m1-codex-A1 --agent codex --case A
```

Repeat cases A/B/C, repetitions 1/2/3, agents codex/claude. Keep fixture directories
outside actual development projects. Run each session from its fixture directory,
not from the skill directory. Read `prompt.txt` verbatim, without adding expected
classifications or reminders. The original prompt explicitly invokes the skill;
these cases test requested activation, not implicit routing accuracy. E1 routing
and trivial-task suites are outside Milestone 1's 18-run matrix.

## CLI commands

Check the installed CLI help first. Use a fresh session, never resume. On the
observed Windows Codex 0.163.0-alpha.10.2 CLI:

```powershell
Set-Location <fixture>
Get-Content -Raw prompt.txt | codex exec --ignore-user-config --ignore-rules --ephemeral --skip-git-repo-check --sandbox read-only --json - > <outside-fixture-trace.jsonl> 2> <outside-fixture-stderr.txt>
```

`--ignore-user-config` does not prove other global instructions or skills are absent.
Inspect the session's discovered skill/instruction inventory and record contamination.
Use a clean disposable OS account/profile if global skills cannot be excluded;
do not modify the developer's global configuration. Inspect actual command events
and successful read outputs, not merely the agent's claim that it read a reference.
Preserve the full event stream and final plan; record version, paths, manifest,
command and exit code. If policy prevents tools from running, record blocked and
do not bypass it. Do not place credentials in traces.

For Claude Code, once available, inspect `claude --help`, use a fresh print-mode
session with stream-json and verbose tool traces (typically
`claude -p --output-format stream-json --verbose` with prompt on stdin), retaining
stderr separately. Verify version-specific flags, skill discovery, loaded baseline
and all global/project instructions before assigning a pass. Never use a permission
bypass to make an evaluation pass.

## Trace review (per run)

Record passed/failed/blocked/not executed for each criterion, with event IDs or
line numbers: activation; successful reference access; access before first
classification; classification; evidence; handoff; extra prompts; missing-reference
fallback. Also audit authorization reference access before restricted-step
identification, template fields, plan-only behavior, and fixture mutations.

A: surface 1 affected, actual frontend consumer search, explicit scoped
read-the-contract handoff. No sibling skill needs to exist.
B: surface 1 unaffected, checks naming route/resource/validation/status/error
behavior and frontend consumer. No unnecessary contract handoff. Full scan because
the planned service extraction crosses a module boundary.
C: all nine uncertain, explicit failed reference access before fallback, no
reconstructed checklist or confident compatibility conclusions. Required
investigation/handoff stays explicit.

No reminder prompts are allowed for a pass. Log reminders as miss and wrong
classifications as wrong in friction-log.md. Re-run fresh after a documented
repair, retaining original failures. A CLI/process failure is blocked, not an
agent-behavior failure. Missing-reference behavior is not passed until observed.
