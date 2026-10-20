# Contract Review

If consuming artifacts, open with:
`Upstream: <names> | Re-derived: <load-bearing claims and actual source checks>`

## Scope and evidence basis

Request; planned change or real diff (identify revision/files); scoped surfaces
and evidenced statuses; inspection limits. Plan-time predictions are weaker than
implemented behavior. Record failed reference access explicitly.

## Consumers and guarantees

| Surface / producer | Consumer | How found / search scope | Before → after guarantee | Breaking / non-breaking / unresolved per consumer | Evidence / reason |
|---|---|---|---|---|---|

Unknown consumers stay `unknown`. Include frontend evidence for HTTP, generated
type provenance if applicable, and database/connection for schema changes.
Distinguish affected contracts from code merely touched.

## Compatibility window (required)

Old clients, old stored payloads, and in-flight jobs that must remain supported;
duration and evidence or exit condition for each. Include mixed deploy versions
and rollback. Explicitly justify any category that does not apply. Missing live
state or timing remains `unknown` with the investigation needed to resolve it.

## Migration path

Ordered consumer/producer changes; dual-read/versioning/drain or other mitigation
where needed; verification of old/new combinations; removal condition; rollback
procedure and limits, including `one-way` steps. This is proposed work, not execution.

## Error semantics

Before/after validation, status codes, error shape, failure/retry behavior as
relevant; consumer impact and evidence. Name uninspected behavior explicitly.

## Risk and unresolved questions

Material-risk assessment and rationale, including possible impact of uncertainty.
List load-bearing `inferred`, `assumed`, and `unknown` claims, the investigation
needed, and evidence that would change the conclusion. Re-surface every assumption
the conclusion depends on. No blanket compatibility claim from a same-repo update.

## Exception proposal

If a break is intended, propose its name, surfaces, named consumers, impact and
duration, mitigation/rollout conditions, and alternatives. Label **proposed, not
granted**. Otherwise state why no proposal is needed. Existing human records are
evidence to inspect for scope, not authority to invent or extend a grant.

## Next work

Scoped inputs/findings for planning, verification, review, and rollout where
relevant. Distinguish completed investigation from required work. No merge verdict
or restricted execution is authorized by this artifact.
