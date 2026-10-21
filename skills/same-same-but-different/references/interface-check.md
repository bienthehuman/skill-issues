# Interface Check

Source: specification v0.5, sections 6, 3.6, and 9.1.1. Section numbers below refer to the specification. This is the canonical packaging reference.

## Loading requirement (section 3.6)

A skill that needs a shared reference puts a directive immediately before the step that uses it. The directive names the file, says to read it first, and forbids working from memory. Standard form for the Interface Check:

> Before performing an Interface Check, read `references/interface-check.md`.
> Do not classify interface surfaces until the reference has been loaded.
> If it cannot be read, mark every surface `uncertain`, state that the reference was not loaded, and do not classify from memory.

### 6.1 Purpose

The Interface Check establishes whether a **contract** might change. It does not establish whether code associated with a contract was touched. Editing a controller does not necessarily change an API contract, and altering a table does not necessarily affect any consumer. The check asks: could anything that relies on this surface now behave differently?

It is required in **plans** (think-before-you-commit), **reviews** (trust-issues, run against the diff), and **refactor plans** (same-same-but-different). A potential interface contract change (stakes trigger 2) requires checking the relevant contracts; read-the-contract investigates flagged or explicitly scoped concerns, without automatically repeating the full planning scan. Baseline-only reference providers and missing-reference behavior are defined in section 3.6; missing skills use section 3.3's disclosed partial-work fallback. The stricter collapse conditions below do not themselves activate a skill. This section is the source text for `interface-check.md` (section 3.6).

### 6.2 The nine surfaces

| # | Surface | Contract changes when… | Evidence to name |
|---|---|---|---|
| 1 | **HTTP:** routes, request validation, response shape (Laravel API resources, DRF serializers, .NET DTOs), status codes, error format | A field is added, removed, renamed, or retyped; validation tightens or loosens; a status code or error shape changes | Route list diff; resource/serializer diff; **frontend consumer search** (API client, hooks, TS types) unless types are generated |
| 2 | **Exported symbols:** TS exports, component props, shared packages, public methods | A signature, prop, or exported type changes | Usage search across packages; compiler/typecheck result |
| 3 | **Persisted schema:** migrations, columns, indexes, constraints, enums, defaults. **Name the database/connection.** | A column or constraint changes in a way existing rows, queries, or other connections depend on | Migration diff; queries touching the table; other connections referencing it |
| 4 | **Async messages:** events, listeners, queued jobs, Django signals, broadcast payloads | A payload shape, event name, or job class/signature changes | Dispatch and listener search; payload definitions |
| 5 | **Stored serialized state:** payloads already in queues, caches, sessions, JSON columns | New code must read data written by old code, or the reverse | Serialization/format diff; what is currently stored (queue contents, cache keys, session format, JSON column samples) |
| 6 | **Config, env, feature flags:** `.env`, `appsettings`, Django settings, flags | A key is added, renamed, removed, or its default changes | Config diff; where each key is read; deployment config sources |
| 7 | **CLI and scheduled work:** artisan commands, Django management commands, cron/scheduler entries | A command name, arguments, output, or schedule changes | Command signature diff; scheduler/cron definitions; callers |
| 8 | **Auth:** roles, permissions, policies/gates, token scopes | A permission is added, renamed, or changes who can do what | Policy/gate diff; permission seeds; usages |
| 9 | **Observable names and file formats:** log lines, metric names that dashboards or alerts use; import/export formats | A name or format that something external depends on changes | Search of dashboards/alerts if accessible; export/import consumers |

The list is owned by the author and is extended from real incidents (section 12, decision 12). Candidate additions to watch: cache key formats (currently under 5), auth scopes in third-party integrations (currently under 8).

### 6.3 Statuses and evidence

Each surface gets one status:

- `unaffected`: with how it was checked. "None" alone is invalid.
- `affected`: a concrete finding naming what changes.
- `uncertain`: could not be established either way. It is a request for investigation, not a claim that a contract changed, and it is never reported or summarized as `affected`. It states what is unknown and which investigation would resolve it. It triggers a scoped read-the-contract run to resolve it to `affected` or `unaffected`. If it is still unresolved at review, gate G2 applies the materially-risky test (section 9.1.1) to the *possible* impact.

Every `affected` and `uncertain` entry, and every `unaffected` entry, carries an evidence statement per section 5.1. An `unaffected` conclusion that rests on a search that could not be run (no frontend access, no dashboard access) is `inferred`, and an `inferred` check cannot use the collapsed form. If the missing search could plausibly have found a consumer, use `uncertain` instead of `unaffected`.

### 6.4 Cost control: scan, then expand

Nine paragraphs per change is the failure mode. The default is a **lightweight scan**: one line per surface. Only `affected` and `uncertain` surfaces are expanded.

```
Interface Check (scan)
1 HTTP: unaffected, OrderController touched but OrderResource fields, validation, and status codes unchanged (diff of resource + request class)
2 Exported symbols: unaffected, no exported symbol in diff (grep of diff for `export`)
3 Persisted schema [mysql: orders_db]: AFFECTED, adds NOT NULL column `channel` without default → expand below
4 Async messages: unaffected, no events or jobs in diff
5 Stored serialized state: UNCERTAIN, `OrderPlaced` job payload gains a field; queued instances unchecked → expand below
6–9: unaffected, no config, CLI, auth, or log/metric changes in diff (grep)
```

**Collapse rule.** The whole check collapses to one line, with evidence, only if all four hold: no persisted data touched, no module boundary crossed, no exported symbol changed, no HTTP or message shape changed. Example:

> Interface Check: unaffected. Changes are internal to `OrderService`; grep for callers of the modified methods found only the two in this file.

A collapsed check marked `inferred` cannot collapse. Use the scan.

### 6.5 Stack-specific rule: the backend/frontend boundary

Laravel, Django, and .NET talking to React/TypeScript have no compiler across the boundary. Changing a response shape leaves the TypeScript types compiling while the UI fails at runtime. For surface 1, the evidence must include a frontend consumer search unless the types are generated from the API definition. If the frontend is not accessible, the status is `uncertain` or the check is `inferred`.

### 6.6 Surface 5 is about time

Stored serialized state is the one surface a diff review cannot show. Old data meets new code: queued jobs, cached values, sessions, and JSON columns written before the deploy. It always feeds the compatibility window (section 9, read-the-contract) and the Rollout Plan.

### 6.7 Plan-time prediction versus review-time ground truth

The plan-time check is a prediction. It covers what the plan says it will touch. The review-time check is run again against the diff, which is ground truth. A surface that the diff touches and the plan did not predict is a **drift finding**.

## Materially risky (section 9.1.1; gate G2)

A compatibility issue is materially risky if any of these hold: a consumer exists outside this diff or repo or cannot be found; data already in the wild is affected (surface 5, persisted rows); a mixed-version state is possible during rollout; or rollback is not possible. If none hold, it is a non-blocking finding. For an `uncertain` surface, apply the test to the *possible* impact: if the plausible impact would meet any condition, the unresolved uncertainty is blocking until investigated.
