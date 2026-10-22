# Skill Issues

*For those with skill issues, these might be the skills you need.*

**An opinionated collection of engineering skills for AI coding agents.**

AI can write code. That doesn't always mean it should.

Skill Issues is a collection of reusable skills designed to help AI coding agents approach software engineering more deliberately — understanding problems before solving them, challenging assumptions, investigating failures, evaluating tradeoffs, and verifying their work.

The goal isn't just to make AI better at completing tasks. It's to make AI a better engineering partner while keeping developers informed, capable, and in control.

**A little backstory**

> Built Skill Issues to prevent skill issues. Immediately encountered a skill issue.

Turns out, even the person building the toolkit needs the toolkit.

## Philosophy

Good engineering is more than writing working code.

It's understanding why something needs to exist, knowing what might break when it changes, being able to defend technical decisions, and recognizing when a simpler approach is better.

Skill Issues follows a few principles:

- **Understand before implementing.** Investigate the problem and its context before proposing changes.
- **Evidence over confidence.** Distinguish verified findings from assumptions and unknowns.
- **Challenge assumptions.** Push back on questionable decisions rather than automatically agreeing.
- **Rigor proportional to risk.** Small changes shouldn't require unnecessary process.
- **Preserve understanding.** Use correct technical terminology and explain decisions without overwhelming the reader.
- **Humans remain in control.** Recommendations are not authorization to perform consequential actions.

An AI assistant should help developers become more capable, not more dependent.

## Project Status

**All 17 canonical skills are implemented.** The separate SPEC 11.9 assessment
found revision `cdc1443` structurally ready for controlled portfolio-project use
and reported 107 passing repository tests plus reference/packaging checks.
Structural readiness does not establish behavioral reliability: SPEC 11.7 remains
unmet, Claude behavior and complete instruction isolation remain outstanding,
and baseline token-ceiling compliance is unknown.

See [project state](PROJECT_STATE.md) for the readiness decision, evidence and
remaining limitations. Implementation is complete; freeze/tag the reviewed initial
implementation before controlled portfolio use under SPEC 11.10.

## Implemented Skills

The collection is organized into three implementation waves.

### Wave 1 — Core Engineering Loop

| Skill | Purpose |
|---|---|
| `you-are-here` | Understand unfamiliar codebases and their data flow |
| `think-before-you-commit` | Plan implementation before changing code |
| `read-the-contract` | Evaluate interface contracts and compatibility |
| `trust-issues` | Review correctness, regressions, and security |
| `prove-it` | Establish evidence that behavior is correct |
| `but-it-works-on-my-machine` | Investigate failures and identify root causes |
| `previously-on` | Preserve decisions and context across sessions |

### Wave 2 — Engineering Decisions

| Skill | Purpose |
|---|---|
| `define-done` | Establish clear, testable requirements |
| `it-depends` | Evaluate system design alternatives |
| `what-could-possibly-go-wrong` | Analyze change impact and regression risks |
| `devils-advocate` | Challenge ideas and hidden assumptions |
| `select-your-battles` | Review database design and data access |
| `same-same-but-different` | Refactor while preserving behavior |

### Wave 3 — Operations and Learning

| Skill | Purpose |
|---|---|
| `famous-last-words` | Plan safe rollouts and operational recovery |
| `are-we-there-yet` | Investigate performance using measurements |
| `garbage-in-garbage-out` | Improve task formulation and prompt quality |
| `i-dont-know` | Build understanding of unfamiliar technical topics |

The waves organize implementation dependencies, not relative importance. Later waves may be implemented provisionally before earlier waves pass behavioral validation. Structural checks accompany implementation; integration readiness requires a separate assessment after all 17 skills exist, before the initial freeze and tag for portfolio evaluation. Neither implementation completion nor integration readiness establishes behavioral reliability.

## Getting Started

**Requirements:** Python 3.9+ and Git.

Clone the repository, then run:

```bash
python scripts/sync-references
python scripts/check-references
python -m unittest discover -s tests -v
```

Use `python3` where appropriate.

These commands validate repository structure and packaging. They do not establish behavioral reliability.

### Installing the Baseline

Skill Issues provides an always-on engineering baseline for Codex and Claude Code.

Preview installation into an existing project:

```bash
python scripts/install-baseline \
  --agent codex \
  --project /path/to/project
```

For Claude Code, use `--agent claude`.

Review the preview before repeating the command with `--apply`.

The installer preserves existing instructions outside its managed block and refuses conflicting or malformed installations.

To refresh an existing installation, use the same preview command, review the diff, then rerun with `--apply`. An intact managed block is replaced only after its recorded digest is validated; edited or malformed blocks require manual review. Do not overwrite `AGENTS.md` or `CLAUDE.md` directly. Start a new agent session afterward; installation alone does not prove runtime loading.

The installer targets project instructions only; it does not refresh global instruction files. Skill Issues follows the host's instruction hierarchy and compatible project conventions, without overriding higher-priority instructions or technically enforcing permissions. Refresh installed skills separately from the reviewed `skills/<name>/` folders,
including each complete `references/` directory. Reference synchronization updates
repository bundles, not installed copies. Unavailable skills must be disclosed;
their workflows must not be invented or reported complete.

### Installing skills

Copy each selected skill's whole directory into the target project's
`.agents/skills/<name>/` for Codex or `.claude/skills/<name>/` for Claude Code.
Install all 17 directories for the complete inventory; a single skill can also be
installed standalone. Keep `SKILL.md` and its bundled references together; no
repository-level shared folder is required. Start a new host session and verify
actual discovery/loading separately; folder-copy tests do not prove activation.

Installing the baseline does not install skills. The current specification is
v0.12. Run `python scripts/check-baseline` to report the 40-non-empty-line cap and
token budget: a character estimate cannot prove compliance with the provisional
900-token ceiling. Preserve SPEC 4's safeguard-preserving exception and historical
measurements; see [project state](PROJECT_STATE.md) for current limits.

## How It Works

Skill Issues separates engineering work into focused responsibilities.

Each skill has:

- A defined purpose and activation conditions.
- Required inputs and fallbacks.
- An evidence-driven workflow.
- A structured, inspectable output.
- Clear boundaries and handoff rules.

Skills can exchange artifacts without treating earlier conclusions as unquestionable facts.

The always-on baseline establishes shared principles for communication, verification, and human authority.

## Development

`SPEC.md` is the canonical specification and takes precedence over derived instructions.

Shared references live in `shared/references/`. Required copies are bundled into individual skills during packaging.

To validate references:

```bash
python scripts/check-references
```

To synchronize reviewed changes:

```bash
python scripts/sync-references --update
```

The project distinguishes automated packaging tests from actual agent behavior evaluations. Passing structural tests does not establish that a skill is reliable.

For implementation details, refer to `SPEC.md` and the repository's technical documentation.

## Roadmap

- [x] Milestone 0 — Repository foundation and tooling
- [ ] Milestone 1 — First skill and reference-loading evaluation (outstanding behavioral evidence does not block implementation)
- [ ] Milestone 2 — Interface Check workflow validation
- [x] Milestone 3 — Wave 1 implementation inventory complete; behavioral validation remains pending
- [x] Wave 2 — Engineering decision specialists implemented; behavior pending
- [x] Wave 3 — Operations, performance, refinement and learning implemented; behavior pending
- [x] Complete inventory — Structural and packaging validation recorded for all 17 skills
- [x] Integration readiness — Structural assessment at `cdc1443` (SPEC 11.9); behavior pending
- [ ] Initial complete implementation — Freeze and tag before portfolio development
- [ ] Practical evaluation — Portfolio use, evidence-driven revisions, and comparable regression checks; preserve original failures (SPEC 11.10)
- [ ] Wave 1 behavioral validation — Meet all existing exit criteria (SPEC 11.7)

## A Final Thought

Skill Issues isn't about making AI replace engineering judgment.

It's about making that judgment more deliberate, explainable, and verifiable.

Because sometimes, the problem isn't the code.

**It's the decisions that led to it.**
