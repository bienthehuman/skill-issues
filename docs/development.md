# Skill Issues

Reusable engineering skills for AI coding agents. Milestone 0 established packaging and installation tooling. Milestone 1 adds think-before-you-commit; behavioral validation remains pending.

## Sources and layout

`SPEC.md` is the canonical v0.3 specification, originally renamed byte-for-byte from `skill-issues-spec.md` at v0.2 and subsequently amended through its revision history. It takes precedence over derived instructions. `BASELINE.md` is its section 4 instruction block, extracted verbatim (37 lines; maximum 40). The references in `shared/references/` are the canonical packaging sources derived from sections 6 and 7, with the applicable loading fallback and materially-risky definition. Edit shared references here, never in bundles.

Skills live at `skills/<name>/SKILL.md`, with bundled references and their own artifact templates in `references/`. The loading map in `scripts/reference_tools.py` implements SPEC section 3.6 and is tested against that table. It includes later-wave names only as packaging metadata; no later-wave implementation is supplied. Other skills receive no shared references.

`tests/` validates tooling. `evals/` is reserved for behavioral evaluation. `friction-log.md` follows Appendix B. No dependency manager or build framework is needed.

## Setup and checks

Use Python 3.9 or newer and Git. Commands below use `python`; use `python3` where appropriate. From this repository:

```sh
python scripts/sync-references
python scripts/check-references
python -m unittest discover -s tests -v
```

Scripts locate their repository from their own file location, so absolute script paths work from another working directory. The reference scripts also accept `--root <repository>` for isolated fixtures. Invoke extensionless scripts through Python on Windows and Unix; executable permission is not required.

The repository contains `think-before-you-commit` and `read-the-contract`. Reference checks validate their bundled copies. The automated tests create temporary skill fixtures to exercise actual copying, drift, and failure cases. Fixtures are not implemented skills.

## Editing and synchronization

1. Change requirements explicitly in `SPEC.md` before changing their meaning elsewhere. The specification hash in the foundation test is a provenance guard; update it deliberately if the specification is amended.
2. Keep `BASELINE.md` consistent with section 4, within 40 lines, and free of file paths. Log baseline or skill changes using Appendix B's format.
3. Edit canonical references in `shared/references/`, preserving the specification's requirements. If section 6 or 7 changes, update its derived reference too; the source-section tests detect omission or alteration of those sections.
4. Run `sync-references`. It creates missing required bundles but refuses divergent or unexpected shared references. It validates all copies before writing any; a validation conflict leaves every bundle unchanged.
5. After reviewing a canonical change, use `python scripts/sync-references --update` to replace divergent bundles explicitly. This still refuses unexpected shared references; review and remove those manually. Private templates are never synchronized or deleted.
6. Run `check-references` and the test suite, then inspect the Git diff. Checks compare exact bytes. `.gitattributes` keeps derived files at LF; `SPEC.md` is exempt from conversion to preserve original bytes.

Unchanged files are not rewritten. Writes use atomic replacement per file and preserve existing file permissions. Preflight prevents partial changes from validation conflicts; it is not a filesystem transaction across all files. I/O failures or concurrent edits can still interrupt a multi-file update. Do not edit bundles concurrently with synchronization. Symbolic links in managed reference paths or the target instruction path are refused.

This tooling detects reference-copy drift, not behavioral plan-versus-diff drift or artifact correctness. No automatic artifact validator is introduced.

## Install the baseline per agent

Choose one agent and an existing project root explicitly. Preview first:

```sh
python /path/to/skill-issues/scripts/install-baseline --agent codex --project /path/to/project
python /path/to/skill-issues/scripts/install-baseline --agent claude --project /path/to/project
```

Review the diff, then repeat the chosen command with `--apply`. Codex writes only `<project>/AGENTS.md`; Claude Code writes only `<project>/CLAUDE.md`. Installing one does not configure the other. No global instruction files are modified.

Existing UTF-8 content (including a BOM and CRLF outside the block) is preserved byte-for-byte, with a separating newline added when needed. A delimited block includes a SHA-256 checksum of the installed baseline, allowing an intact older baseline to be updated. Repeated installation is a no-op. Malformed, duplicate, or checksum-conflicting blocks fail without writing. There is no force/repair option: review user-owned conflicts manually. A checksum detects accidental edits; it is not an authenticity signature.

The installer refuses a root `AGENTS.override.md` for Codex or an alternate `.claude/CLAUDE.md` for Claude Code. Existing instructions can still contradict the baseline semantically; the installer preserves them and cannot resolve that conflict for you. It does not infer authorization from their contents. Plan approval permits scoped reversible work; restricted execution and compatibility exceptions still require the human authority specified in SPEC section 7.

### Verify actual loading separately

The selected directory must be the project root from which you launch a **new** session. For Codex, use the Git root when there is a repository; without a detected root it checks the current directory. Root `AGENTS.md` lies on the discovery path when launching there. Nested overrides and the instruction byte budget can change the effective instructions. Claude Code supports root `CLAUDE.md`; launch there and inspect `/memory` for the loaded file. Check any local, imported, or organization guidance too.

Official documentation checked on 2026-10-20: [Codex instruction discovery](https://developers.openai.com/codex/guides/agents-md) and [Claude Code memory](https://code.claude.com/docs/en/memory). These establish supported locations, not proof of loading in a particular session.

In a disposable project, install for each agent independently. Start the agent there, inspect its instruction-source display/logs (`/memory` in Claude Code), and ask it to summarize the baseline's authority rules. Retain the transcript and loaded path. For Codex, the official guide also describes session/TUI logs for auditing loaded sources. Do not claim activation merely because the file exists or the agent can read it on request. These live checks are separate from the installer tests and have not been executed in Milestone 0.

## Milestone 1

`think-before-you-commit` is implemented with its own artifact template and bundled references. SPEC section 11.0 remains required for Wave 1 behavioral validation, not for permission to implement further skills: run it with that skill installed alone, from the project directory, with three cases, three runs each on Codex and Claude Code (18 runs). Record reference reads before classification, outcomes, and every intervention. See `evals/README.md`.

SPEC section 3.2 now permits provisional implementation across Waves 1–3 with structural and packaging checks, preserving actual dependencies, handoff contracts and standalone fallbacks. After all 17 skills are implemented, assess integration readiness separately (11.9), then freeze and tag the initial complete implementation before portfolio development (11.10). Record versioned observations in the established friction-log conventions, preserve original failures, and require comparable regression evidence before claiming improvement. Implementation complete, integration ready and behaviorally validated are distinct statuses; none is granted by this roadmap amendment.

The earlier Codex-only development allowance is superseded by that implementation sequencing. Claude Code and complete instruction isolation
remain outstanding; provisional implementation does not establish full cross-agent compatibility or
amend the baseline. For the standalone-before-integration contract evaluation,
see `evals/contracts-results.md` and `evals/contracts.py`.
