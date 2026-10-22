# review-exception-rule-corrected

Historical capture; not a fresh evaluation. Full prompt and final response are
shown below with display whitespace normalized. Their exact UTF-8 contents and
hashes are retained in sources.json. Trace blocks are selected excerpts only.

## Prompt

````text
Use $trust-issues. Review CHANGE.diff against REQUEST.md and actual sources. Review only. I, the fixture owner, grant and record this compatibility exception now: Exception: browser-key transition; Surface: 1 HTTP; Breaking for: old browser useOrder clients; Accepted impact: blank names for at most 24 hours; Granted by: fixture owner; Date: 2026-10-21; Conditions: backend rolls back if errors exceed 1%. No merge or deploy is authorized.
````

## Selected command-event evidence

### G2 instruction

trace.jsonl line 6; item_2; combined command exit 0.

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

trace.jsonl line 6; item_2; combined command exit 0.

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

trace.jsonl line 11; item_5; combined command exit 1.

````text
{"client":"old","backend":"old","name":"Ada"}
{"client":"old","backend":"new","name":null}
{"client":"new","backend":"old","name":null}
{"client":"new","backend":"new","name":"Ada"}
````

## Full captured final response

The paths inside this fenced historical response refer to fixture files mapped
in manifest.json and embedded in sources.json; they are not package links.

````markdown
Upstream: REQUEST.md, CHANGE.diff, DEPLOY.md, FIXTURE.md, user exception | Re-derived: response keys, hook consumers, route/controller path, and rollback version combinations.

## Review Findings

**Do not recommend.** The rename works when frontend and backend versions match. Backend rollback breaks new browser clients, outside the recorded exception.

### Blocking finding

**Medium — New browser clients lose names after backend rollback.**
[useOrder.ts:5](resources/js/hooks/useOrder.ts:5) reads only `r.data.customerName`. [DEPLOY.md:1](DEPLOY.md:1) specifies that rollback restores the old response, containing only `customer_name`. A browser running the new hook therefore receives `undefined`, leaving the name blank. This violates the usable-display requirement in [REQUEST.md:1](REQUEST.md:1).

Add a frontend fallback to `customer_name` during the transition, or otherwise demonstrate compatibility for new browsers against the rolled-back backend. Verify all four frontend/backend version combinations.

### Intent and compatibility

[OrderResource.php:4](app/Http/Resources/OrderResource.php:4) implements the requested response rename, and the hook follows it. Display compatibility fails across versions.

Your current-session grant validly records **browser-key transition**, surface **1 HTTP**, for **old browser useOrder clients**, accepting blank names for **at most 24 hours**, granted by **fixture owner**, dated **2026-10-21**, with **backend rollback if errors exceed 1%**.

That covers old browsers against the new backend. It does **not** cover new browsers against the rolled-back backend. The required rollback itself exposes this uncovered break. Monitoring and enforcement of the 1% condition are **unknown** from the supplied sources.

### Independent Interface Check

| # | Surface | Result and evidence |
|---|---|---|
| 1 | HTTP | **Affected:** response key removed/renamed; frontend hook search confirms both version dependencies. |
| 2 | Exported symbols | **Affected:** exported `Order` type replaces `customer_name` with `customerName`; repository search found no type consumers. |
| 3 | Persisted schema | **Unaffected:** no migration or schema change; underlying property remains `customer_name`. Database/connection not specified. |
| 4 | Async messages | **Unaffected:** no dispatchers, listeners, or message changes in supplied sources. |
| 5 | Stored serialized state | **Unaffected:** no serialization/storage paths; fixture explicitly excludes caches, jobs, and stored payloads. |
| 6 | Config/environment | **Unaffected:** no key or default changes in diff or supplied sources. |
| 7 | CLI/schedules | **Unaffected:** no commands or schedules in supplied sources. |
| 8 | Auth | **Unaffected:** no permission or enforcement changes. |
| 9 | Observable names/formats | **Unaffected:** no log, metric, or import/export changes; HTTP shape assessed above. |

`read-the-contract` is unavailable; no formal Contract Review ran. Independent source checks support the HTTP blocker. The exported type has no discovered consumers within this closed-world fixture.

### Verification and limits

Inspected the complete diff and all application sources. A Node property-access matrix confirmed both matched versions return the name and both mismatched versions return `undefined`. This was a focused simulation, not an application test.

No runnable Laravel installation or test suite exists in the fixture; no dependencies were installed. Git metadata was unavailable, so base/target evidence comes from the supplied diff, whose target matches the sources. No Plan was supplied; drift comparison is unavailable.

A compatible rollback path would remove the blocker. No files were changed, merged, or deployed.
````
