# G2 reverse-rollback regression evidence

These are historical Codex captures from 2026-10-21, preserved from the ignored
`evals/review-runs/` directory on 2026-10-22 at repository HEAD `cdc1443`.
Original captures remain unchanged. This package contains full prompts and final
responses, selected command-event excerpts, and hash-verified fixture contents.
**It does not contain full transcripts.**

| Case | Capture | Observed decision |
|---|---|---|
| [Original](original.md) | `review-exception-first` | Recommends with an old-browser exception despite recognizing an uncovered new-browser/old-backend rollback break. |
| [Corrected](corrected.md) | `review-exception-rule-corrected` | Blocks the same uncovered break after the instruction correction. |
| [Broader exception control](covered.md) | `review-exception-covered-first` | Recommends with a human exception explicitly covering both mismatched version combinations. |

The original and corrected prompts and application fixtures are identical. The
correction explicitly requires matching every material break, including reverse
rollback combinations, to the human exception's named consumers and conditions.
The corrected and broader-control installed `trust-issues/SKILL.md` files match
the repository version at `cdc1443`. The correction also changes first-line
artifact-envelope wording; it is not a single-clause isolated experiment.

## Contents and verification

- [manifest.json](manifest.json) identifies each run, whitelisted capture metadata,
  source SHA-256 hashes, fixture path-to-hash mappings, selected trace line/event
  identifiers and excerpt offsets within captured command output.
- [sources.json](sources.json) stores exact UTF-8 file contents keyed by SHA-256,
  deduplicated across cases. It includes all 16 manifest-listed fixture files per
  run (application code, request, diff, deployment notes, installed instructions,
  references and baseline), plus the exact captured prompts and final responses.
  Decode each blob as UTF-8 bytes without newline conversion to verify its hash.
- The three case documents present prompts/finals and excerpts with display
  whitespace normalized. Fenced historical links refer to fixture paths in the
  manifest. They are not links to files in this package.

Package payload hashes exclude manifest.json itself. Hashes detect accidental
alteration and connect exported contents to retained local sources; they are not
an authenticity signature or independent proof that the capture system was honest.
Run `python -B -m unittest discover -s tests -p test_g2_evidence.py -v` from the
repository root to check the portable package without ignored captures.

## Provenance, sanitization and limitations

Captures used Codex CLI `0.163.0-alpha.10.2`, fresh ephemeral sessions, a read-only
evaluated sandbox, approval `never`, and zero follow-up human prompts. Each reports
the expected installed skill inventory and unchanged fixture/canonical bytes.
The Windows backend label `elevated` names the sandbox implementation, not
unrestricted execution. Model/reasoning overrides were null; resolved model and
reasoning settings are unknown. Global instructions remained visible. No Claude
behavior, repeated-trial reliability or complete instruction isolation is shown.

Successful command output contains the installed G2 rule and human-exception
reference before the final verdicts. The corrected simulation emits all four
client/backend results even though its combined command exits 1 after a following
search finds no test files. This is simulation evidence, not an application test
or a claim that the whole command passed. The broader control's simulation command
exits 0. Fixtures are static, closed-world Laravel/React inspection scaffolds.

The broader control changes both the human exception and DEPLOY.md: it adds
operator-owned display monitoring and restoration of matching assets. It is not
a pure one-variable control. Operational enforcement was not executed. The narrow
correction does not establish general stateful rollback safety, historical-grant
validation, exception-condition enforcement or resistance to actual restricted
execution requests.

Sanitization uses an allowlist: fixture text, prompts, finals, relevant excerpt
text, hashes and capture facts only. Raw runtime logs, inventory/config dumps,
absolute host paths, user/profile details and invocation arguments are omitted.
No redaction was necessary inside the exported synthetic fixture/prompt/final
contents; original bytes are retained in sources.json. Export review found no
credentials or real customer data. The name Ada is synthetic simulation input.
