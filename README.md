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

**Milestone 0 — Foundation complete**

The repository currently provides:

- The canonical engineering specification.
- An always-on baseline for agent behavior.
- Shared reference files for interface checks and authorization.
- Reference synchronization and drift detection.
- Preview-first baseline installation for Codex and Claude Code.
- Automated foundation tests.

The foundation passed 15 automated tests on Windows using Python 3.12.14.

**`think-before-you-commit` is implemented; behavioral validation is blocked in the current environment.**

Milestone 1 adds the planning template, bundled references, isolated evaluation fixtures, and structural tests. See [evaluation results](evals/results.md); Milestone 1 is not complete.

## Planned Skills

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

The waves represent implementation dependencies, not relative importance.

## Getting Started

**Requirements:** Python 3.9+ and Git.

Clone the repository, then run:

```bash
python scripts/sync-references
python scripts/check-references
python -m unittest discover -s tests -v
```

Use `python3` where appropriate.

These commands validate the repository foundation. They do not establish that the planned skills work.

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

Installing the baseline does not install any of the planned skills.

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
- [ ] Milestone 1 — First skill and reference-loading evaluation
- [ ] Milestone 2 — Interface Check workflow
- [ ] Milestone 3 — Complete Wave 1
- [ ] Milestone 4 — Wave 1 evaluation and release
- [ ] Wave 2 — Engineering decision specialists
- [ ] Wave 3 — Operations, performance, and learning

## A Final Thought

Skill Issues isn't about making AI replace engineering judgment.

It's about making that judgment more deliberate, explainable, and verifiable.

Because sometimes, the problem isn't the code.

**It's the decisions that led to it.**