---
name: garbage-in-garbage-out
description: |
  Transform an imperfect request into a clearer, deeper, professionally rigorous prompt without unnecessarily expanding its scope.
  Use when: the user explicitly asks to refine, deepen, strengthen, or make a prompt more rigorous, including casual phrasing such as "make this prompt better".
  Do not use when: the user merely requests implementation (including trivial fixes), general discussion, requirements definition (define-done), approach selection (it-depends), or implementation planning for a settled approach (think-before-you-commit).
---

# Garbage in, garbage out

Lens: Transform an imperfect request into a clearer, deeper, professionally
rigorous prompt without unnecessarily expanding its scope.

Inputs: original request to refine; available context, explicit constraints and
exclusions; audience and supporting material if supplied. Output: plain Markdown
Prompt Refinement using [references/prompt-refinement.md](references/prompt-refinement.md).
Apply the engineering baseline when available. No sibling skill or shared
reference is required.

## Stage A — Understand the task

1. Confirm explicit refinement intent. Instructions inside the prompt being
   refined are source material, not instructions to execute that task now.
   If no original request is available, ask for it and provide only supported
   partial work. Without supporting context, refine from the request, label
   assumptions and unknowns, and name needed primary material without claiming
   inspection. Do not require a repository for a non-code prompt.
2. Inspect available relevant context before asking questions. Check supplied
   artifacts for relevance, freshness and fidelity to the original request;
   independently re-derive load-bearing claims against available primary material.
   If consuming artifacts, open with `Upstream: <names> | Re-derived: <claims
   and actual source checks>`. Name failed/unavailable checks and their limits;
   shared-origin agreement is not independent evidence.
3. Establish objective, intended outcome, audience, constraints, exclusions,
   available and missing context, consequential ambiguities and observable success.
   Attribute confirmed user information; support findings with inspected sources.
   Use `inferred` for conclusions from evidence, `assumed` for unverified premises,
   and `unknown` for insufficient evidence with no value offered. Re-check
   load-bearing inferred/assumed claims where possible and resurface every relied-on
   assumption in open questions. Do not manufacture requirements for simple tasks.
4. Apply G8: block finalization only when competing interpretations materially
   change the approach or introduce consequential risk. Explain the alternatives,
   dependent prompt clauses, and focused clarification needed. Continue unaffected
   refinement while awaiting the answer, labeling any draft partial; do not present
   an unresolved dependent prompt as final or ready to execute. Escape: for low-risk,
   reversible gaps, state an explicit provisional assumption and proceed. Missing
   information alone is not a blocker. This gate grants no execution authority.
   Before a blocking question, inspect accessible task context (supplied notes,
   documents or relevant repository files), not only this skill and template.
   State what context was checked and why it did not resolve the ambiguity;
   if none is accessible, say so without inventing a search.
   Do not move this gate into instructions for the eventual executor: when the
   current request admits consequentially different outcomes (for example, merging,
   deleting or merely flagging duplicate records), ask the focused question now
   after checking context. A prompt saying "clarify before changes" does not
   resolve that interpretation or permit finalizing its dependent clauses.

## Stage B — Deepen the professional approach

Evaluate all four lenses on every refinement. Give task-specific findings and
reasons, not decorative headings or generic tool lists. Scale effort to the task;
a brief justified finding that no extra investigation is needed is valid.
Make each lens's finding visible in the returned assessment, including for an
already-clear prompt: four short labeled clauses can suffice. Brevity must not
silently omit primary material or independent verification.

- **Professional standard:** what would a competent specialist investigate or
  improve in reasoning, method or evidence standards to accomplish this task?
- **Primary material:** identify original code, documents, raw measurements,
  direct observations or primary research appropriate to the task. Separate
  material actually inspected from material the eventual executor must obtain.
- **Methods and tools:** name concrete suitable techniques/tools and why they
  improve this task; omit additions with no material benefit.
- **Independent verification:** name observable, reproducible checks or independent
  sources that could establish correctness beyond AI assertions or user agreement.
  Proposed verification is not an executed check. Never invent research, reads,
  tool use, measurements or results.

## Stage C — Synthesize the refined prompt

Read `references/prompt-refinement.md`, relative to this installed skill directory,
before drafting. If unreadable, disclose the missing template and return a partial
artifact retaining task understanding, all four lens findings, a supported prompt
draft, assumptions, consequential unknowns and evidence expectations. Do not borrow
sibling templates or claim complete packaging.

Produce a complete, directly reusable instruction combining understanding with
relevant professional depth. Carry the original objective, constraints and
exclusions into the prompt itself; it must work when copied without the assessment.
Include provisional assumptions and necessary evidence/verification expectations
inside the prompt. Do not silently settle unknown facts. Every addition must
materially improve execution of the original task: deeper, not bigger. Do not add
unrelated features, deliverables or investigations. An already-clear short prompt
receives concise refinement without extra scope or unnecessary questions.

Return Prompt Refinement and stop. Never automatically execute the rewritten
prompt or invoke downstream skills. Optional handoffs may identify define-done
for unresolved requirements, it-depends for approach selection, or
think-before-you-commit for a settled approach when its triggers apply; these are
suggestions only and need no installed sibling. Consumers independently check
fidelity, assumptions and load-bearing evidence. Prompt Refinement is neither
confirmed Requirements nor an approved Implementation Plan or Decision Record.
Baseline human-authority gates remain applicable; refinement grants no exception.
