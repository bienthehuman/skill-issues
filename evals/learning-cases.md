# Focused learning trace rubric

Run fresh fixtures via `learning.py`, retaining inventory, prompt, manifest,
trace, stderr and final answer. Review routing before teaching quality. Fixtures
are static inspection material, not a runnable framework. Packaging tests do not
execute these prompts or establish behavioral passes.

| Case | Expected routing and observable behavior |
|---|---|
| beginner | Learning activates implicitly; answers what a transaction does first, then briefly states an inferred level; explains from foundations, defines atomicity at first use, uses a helpful example and states transactional-storage limits; names one next concept. No quiz. |
| experienced | Learning activates; explains MVCC without SQL basics, defines unfamiliar vocabulary progressively, distinguishes snapshot model from isolation-level/engine behavior and covers a concrete model limit. No questionnaire or quiz. |
| short | Learning activates; roughly four sentences, answer first, useful mechanism, term explained as needed, model limitation (for example selectivity/write costs), one next concept; no forced document headings or quiz. |
| lookup | Learning does not activate or emit Learning Notes; returns the expansion only. |
| implementation | Learning does not activate; ordinary typo edit, no learning artifact. The default read-only capture cannot establish the edit itself; assess routing separately from sandbox blockage. |
| debug | Routes diagnosis rather than learning; no unsupported confirmed cause from static code or fabricated runtime. |
| orientation | Routes task-scoped repository orientation rather than general learning. |
| requirements | Routes requirements definition rather than learning. |
| verification | Routes evidence gathering rather than teaching; static inspection does not prove deployed runtime. |
| quiz | Explains first, asks one prediction scenario, then stops; no answer/reasoning for that scenario in the same response. Continue manually in the same session with a prediction, retaining both turns; only then should it reveal reasoning without condescension. |
| prediction | Evaluates the already supplied prediction directly, explains rollback under the stated assumptions, and does not demand another prediction or claim this fixture was executed. This standalone case does not establish multi-turn waiting. |
| evidence | Labels TypeScript and predicted results as illustrative, distinguishes facts/model/context and does not invent code inspection or execution. |

At least three positive and three negative prompts are provided per SPEC 11.2.
Record actual successful entrypoint/template reads, answer order, level matching,
vocabulary timing, model limits, length, optional-check behavior and evidence
claims with trace line numbers. Record failures and fresh corrective reruns
separately. Do not pass on prose keyword matches. The quiz follow-up must be
observed across turns to establish predict-then-reveal; a lone final response
cannot prove waiting or correction behavior. Claude folder copies are packaging
evidence only. Comprehensive integration, comparisons and repeated runs remain
outside this focused implementation task.
