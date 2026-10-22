---
name: i-dont-know
description: |
  Build understanding of an unfamiliar concept, mechanism, technology, or engineering principle.
  Use when: the user wants to learn, asks "explain", "why", or "how does X work", or requests a check of their conceptual understanding.
  Do not use when: the request is a simple factual lookup, implementation, debugging an existing failure, code review, task-scoped repository orientation, requirements definition, or verification of actual software behavior.
---

# I don't know

Lens: Building understanding, not producing a deliverable.

Inputs: a topic or central question; knowledge level inferred from phrasing and
available context. Output: plain Markdown Learning Notes using
[references/learning-notes.md](references/learning-notes.md). Apply the engineering
baseline when available. No sibling skill or shared reference is required.

## Workflow

1. Check intent rather than matching question words alone: "why is this endpoint
   failing?" requests diagnosis, whereas "why do transactions need isolation?"
   requests understanding. A code example can teach without becoming an
   implementation task. If the topic is missing, ask for it; if only level is
   unknown, infer a reasonable starting level and proceed without a questionnaire.
2. Sanity-check supplied explanations, notes and code against the question and
   available primary material. Re-derive load-bearing claims before relying on
   them; agreement among shared-origin artifacts is one source. When consuming
   artifacts, precede the notes with `Upstream: <names> | Re-derived: <claims and
   actual checks>`, naming unavailable checks and limits. Do not imply repository
   access from conversational context alone.
3. Read `references/learning-notes.md`, relative to this installed skill directory,
   before drafting. If unreadable, disclose the missing template and give a
   supported partial explanation retaining the fields below; do not borrow a
   sibling template or claim the installation is complete.
4. Answer the central question first, before introductory material or a level
   statement (apart from the required upstream envelope when applicable). When
   level is unknown, state the inferred starting level in one brief line after
   the answer. When context already demonstrates expertise, adapt silently or
   state the inference only if useful; do not reteach familiar foundations.
5. Build the explanation from the smallest relevant first principles. Introduce
   technical vocabulary progressively, defining each necessary new term at first
   use. Use a concrete example or analogy when it clarifies the mechanism, and
   connect it back to the actual concept. Prefer examples consistent with the
   user's Laravel, Django, .NET, React/TypeScript or supported database context
   when supplied; do not invent a project stack or version.
6. Distinguish established technical facts, simplified teaching models, knowledge
   assumptions, context-dependent behavior and unknown/unverified claims. Name
   relevant version, configuration or isolation-level dependencies rather than
   generalizing them. Use `inferred`, `assumed` and `unknown` per the evidence
   conventions for evidential claims, not every teaching sentence. Re-check
   load-bearing inferences/assumptions where possible; resurface relied-on
   assumptions in brief open questions or limits when unresolved. Illustrative
   code and predicted outputs are not executed examples. Never claim code
   inspection, execution or runtime verification without actual supporting evidence.
7. Explain where the simplified mental model stops being accurate and what that
   limitation changes in practice. Recommend the single most useful next concept
   and why it follows. Identify which claims would need independent checking
   before using these notes for an engineering decision; notes are not evidence
   of a particular application's behavior.
8. Keep the notes proportional: a simple question may need only a few connected
   sentences covering the answer, mechanism, necessary terms, model limit and
   next concept. Combine template fields; omit irrelevant examples. Greater
   depth is appropriate for a difficult topic or demonstrated expertise, not
   merely because this skill activated. Do not force a long document or quiz.
   A length limit compresses the fields rather than dropping the next concept
   or unknown-level statement: fold these into existing sentences when needed.

## Optional comprehension checks

Only check comprehension when the user opts in, for example "quiz me" or "let me
predict". Ordinary explanations end without an automatic quiz or recurring quiz
offer. For opt-in practice, explain the central concept first unless the user
explicitly requests a prediction before teaching. Present one question/scenario
and wait for the user's prediction before revealing its answer, expected output
or reasoning. Do not hide the reveal later in the same message. On the next turn,
explain the result and reasoning, address any misconception directly, and avoid
unnecessary praise or condescension. If the user already supplied a prediction,
evaluate it and explain; do not make them predict again. Respect requests to stop
practice or receive the answer directly.

## Boundaries and gates

Conceptual discussion can mention diagnosis, orientation, requirements and tests
without invoking their workflows. Existing-failure diagnosis belongs to
but-it-works-on-my-machine; task-scoped codebase orientation to you-are-here;
requirements to define-done; behavior verification to prove-it. These are optional
handoffs, never installation dependencies. previously-on may later record learning;
do not automatically create a handoff or start a delivery pipeline.

No learning-specific hard gate is introduced. Unknown level does not block
teaching. Baseline G6/G7 human-authority gates have no escape; learning notes and
illustrative examples grant no execution authority or compatibility exception.
