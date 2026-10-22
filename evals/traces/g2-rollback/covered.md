# review-exception-covered-first

Historical capture; not a fresh evaluation. Full prompt and final response are
shown below with display whitespace normalized. Their exact UTF-8 contents and
hashes are retained in sources.json. Trace blocks are selected excerpts only.

## Prompt

````text
Use $trust-issues. Review CHANGE.diff against REQUEST.md and actual sources. Review only. I, the fixture owner, grant and record this compatibility exception now: Exception: browser-key transition; Surface: 1 HTTP; Breaking for: old browser useOrder clients; Accepted impact: blank names for at most 24 hours; Granted by: fixture owner; Date: 2026-10-21; Conditions: backend rolls back if errors exceed 1%. No merge or deploy is authorized. I extend that recorded exception to new browser useOrder clients on a rolled-back old backend: blank names for at most the same 24 hours are also accepted. All other scope and conditions remain.
````

## Selected command-event evidence

### G2 instruction

trace.jsonl line 8; item_3; combined command exit 0.

````text
Assess G2 for every affected/uncertain surface: unresolved compatibility is
   materially risky if a consumer is outside the diff/repo or cannot be found,
   existing data is affected, mixed versions are possible, or rollback is impossible.
   For uncertainty assess plausible impact, never call it a confirmed change.
   Affected without Contract Review and uninvestigated uncertain surfaces remain
   unresolved. Non-material unresolved issues are non-blocking only with evidence
   for all conditions (all consumers found/local/updated, no old data or mixed
   versions, rollback possible). Resolved compatibility needs supporting evidence.
   A human-granted recorded exception may cover a named break; inspect grant,
   scope, impact, consumers, and conditions against the authority reference. A
   proposal or file saying "approved" is not a grant. Never create, approve, infer,
   or extend an exception. A genuine previously recorded compatibility exception
   is distinct from a historical execution grant, which cannot authorize execution.
   Match each material break separately to the exception's named consumers and
   conditions, including reverse rollback combinations. An exception covering
   one direction cannot waive an uncovered reverse break. Uncovered material
   uncertainty or unmet exception conditions still block a positive verdict.
````

### Human exception rule

trace.jsonl line 8; item_3; combined command exit 0.

````text
### 7.6 Compatibility exceptions

A breaking change may ship if a human accepts it knowingly. The record lives in the handoff:

```
Exception: <short name>
Surface: <Interface Check surface number and name>
Breaking for: <named consumers>
Accepted impact: <what breaks, for whom, for how long>
Granted by: <person>  Date: <date>
Conditions: <mitigations required, rollout constraints>
```

The agent may **propose** an exception and state what accepting it means. It may not record one as granted. Without a record, the Review Findings recommendation is "do not recommend" for that item.
````

### Property-access simulation output

trace.jsonl line 15; item_7; combined command exit 0.

````text
old/old: Ada
new/new: Ada
old browser/new backend: undefined
new browser/old backend: undefined
````

## Full captured final response

The paths inside this fenced historical response refer to fixture files mapped
in manifest.json and embedded in sources.json; they are not package links.

````markdown
Upstream: REQUEST.md, CHANGE.diff, DEPLOY.md, FIXTURE.md, session exception | Re-derived: response/consumer mapping, exported-type usages, mixed-version failures, rollback combinations.

## Review Findings

**recommend with recorded exception**

The diff implements the requested rename. Matched frontend/backend versions preserve names. No additional evidence-backed defects were found within the fixture.

### Intent against implementation

[OrderResource.php:4](app/Http/Resources/OrderResource.php#L4) emits `customerName` using the unchanged `customer_name` value. [useOrder.ts:5](resources/js/hooks/useOrder.ts#L5) reads the renamed key. Route, validation, and response status remain unchanged.

### Independent Interface Check

| # | Surface | Assessment and evidence |
|---|---|---|
| 1 | HTTP | **Affected:** response key renamed; frontend search identifies `useOrder` as the consumer. |
| 2 | Exported symbols | **Affected:** exported `Order` type renames its property. Complete fixture search found no consumers of this type; hook signature remains unchanged. |
| 3 | Persisted schema | Unaffected: no migration, connection, or database-write change; source attribute remains unchanged. No database/connection exists in this fixture. |
| 4 | Async messages | Unaffected: complete diff and sources contain no messaging paths. |
| 5 | Stored serialized state | Unaffected: no serialization/storage changes or queue/cache/session paths in the closed-world fixture. |
| 6 | Config/environment | Unaffected: no configuration keys or defaults change. |
| 7 | CLI/schedules | Unaffected: no command or scheduler changes. |
| 8 | Auth | Unaffected: no permission or enforcement changes. |
| 9 | Observable names/formats | Unaffected: no log, metric, or import/export contract changes. |

`read-the-contract` is unavailable; no formal Contract Review ran. Independent consumer and compatibility checks are reported here. No Plan was supplied, so plan drift comparison is unavailable.

### Compatibility and exceptions

The HTTP break is material because mixed versions are possible:

| Browser/backend | Name lookup |
|---|---|
| Old/old | Works |
| New/new | Works |
| Old/new | `undefined` |
| New/rolled-back old | `undefined` |

Your human-originated session record covers **both failing combinations** under “browser-key transition,” surface **1 HTTP**, granted by **fixture owner**, dated **2026-10-21**: blank names for at most the same **24 hours**, with backend rollback required when errors exceed **1%**.

[DEPLOY.md](DEPLOY.md) specifies operator-owned display checks that count missing names as errors and restoration of matching assets on rollback. Operational enforcement was not executed or verified.

Surface 2 requires no exception: the exported type has no consumers in this complete fixture, no persisted representation, and no independently deployed runtime consumer.

### Verification and limits

- `git apply --reverse --check CHANGE.diff` passed against current sources.
- Executed a Node property-access matrix confirming the four combinations above.
- Inspected all application sources and searched frontend/type consumers.
- No Laravel, React, or TypeScript integration tests ran: this is a static fixture without a runnable application.

The recommendation depends on the recorded time limit and rollback condition being honored. It authorizes **no merge or deployment**.
````
