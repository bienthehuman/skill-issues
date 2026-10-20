---
name: you-are-here
description: |
  Establish task-relevant codebase orientation in a Codebase Map.
  Use when: an engineering task requires understanding unfamiliar code; module ownership, entry points, state ownership, or data flow are unclear; or planning/debugging depends on repository relationships not yet established.
  Do not use when: the relevant code and relationships are already understood, the change is trivial and localized, only a specific known file needs inspection, or a repository-wide inventory would add no value to the current task. A repository's existence alone is not a trigger.
---

# You are here

Lens: Where things live and how data flows, scoped to the task.

Inputs: the engineering question driving orientation and repository access;
supplied trees, key files, and upstream artifacts may supplement or replace
access. Output: a Markdown Codebase Map using
[references/codebase-map.md](references/codebase-map.md).
Apply the engineering baseline when available. This bundle requires no sibling
skills or shared references.

## Workflow

1. State the current engineering question and the smallest useful investigation
   boundary. If the question is missing, request it rather than inventorying the
   repository. Use targeted searches and selective reads, especially in large
   repositories; neither repository size nor a fixed file count determines scope.
2. Sanity-check supplied maps, plans, trees, and reports against the current
   question, revision, and accessible code. Treat shared-origin artifacts as one
   source. Independently re-derive load-bearing upstream ownership, entry-point,
   boundary, and data-flow claims before relying on them. An artifact consuming
   others opens with
   `Upstream: <names> | Re-derived: <claims and actual source checks>`.
   Name failed or unavailable re-derivations and their limits.
3. Locate relevant execution entry points: routes, handlers, components,
   commands, jobs, or scheduled paths as applicable. Trace meaningful calls and
   data transformations through relevant modules, including conditions that
   select the path. Follow concrete references outward only when they resolve
   a relationship needed for this question. Do not enumerate unrelated packages,
   directories, modules, or architectural layers for completeness.
4. Establish where relevant state is created, read, modified, and persisted;
   inspect dependencies and module/integration boundaries only as needed.
   Distinguish execution sites and state writers from ownership. A call site,
   import, or write does not automatically prove exclusive module responsibility
   or state ownership. Support responsibilities with inspected declarations,
   callers, wiring, lifecycle rules, or other relevant evidence; label conclusions
   about ownership `inferred` unless directly established by the cited material.
   Name database/connection and persistence locations when established; otherwise
   leave them `unknown`. Static code inspection shows a defined path, not proof
   that it runs in a deployed environment.
5. Record evidence and unresolved relationships as investigation proceeds. Stop
   expanding when sufficient task-relevant evidence establishes the entry points,
   meaningful execution/data paths, state interactions, and boundaries necessary
   to answer the question. Irrelevant fields need only a short not-applicable
   reason. If necessary evidence is unavailable, stop the unsupported branch,
   name the exact source/check needed, and return supported partial orientation.
   Do not broaden the search to create an appearance of completeness.
6. Read `references/codebase-map.md`, relative to this installed skill directory,
   before writing the map. If unreadable, disclose the missing template and
   return a partial map retaining the fields below; do not borrow sibling files
   or claim complete packaging. Include question/scope, entry points, modules
   and responsibilities, execution/data flow, state ownership/persistence,
   boundaries, supporting evidence, load-bearing claims, and unknowns/limitations.
   Keep every field but scale its detail to the question. Include concrete paths,
   symbols, or other navigable references established by inspection.
7. Separate observations from conclusions using the canonical evidence
   conventions: directly supported findings name actual inspected material or
   checks without a label; `inferred` means concluded from observed facts;
   `assumed` means an unverified premise; `unknown` means insufficient evidence.
   Attribute user reports. An inspected file proves its contents, not runtime
   behavior or exclusive ownership. Re-check every load-bearing `inferred` or
   `assumed` claim against available sources; unresolved premises and failed
   re-derivations remain visible in Unknowns with dependent conclusions bounded.
   Do not invent relationships or replace missing facts with plausible structure.

## Standalone fallback

Without repository access, request the relevant directory tree and key files
for the engineering question, including callers, wiring, or state definitions
needed to establish specific missing relationships. If supplied material supports
useful orientation, produce only a partial Codebase Map and identify its source
and limits. If it does not, state what is required before mapping; do not invent
entry points, responsibilities, ownership, or execution paths. Missing sibling
skills never prevent supported orientation.

## Boundaries and handoff

Own orientation only. Implementation Plans belong to think-before-you-commit,
failure diagnosis to but-it-works-on-my-machine, contract compatibility and
consumer analysis to read-the-contract, implementation findings to trust-issues,
and behavioral verification evidence to prove-it. Identifying a boundary does
not require an Interface Check. Suspicious code is not a confirmed root cause.
Do not recommend architectural changes unless the orientation question explicitly
asks to identify architectural concerns; then distinguish observations from
recommendations. Optional handoffs do not execute downstream work or create a
mandatory pipeline. Name unavailable instructions if a requested assessment
needs them; do not reconstruct their procedures.

Explicitly identify load-bearing entry-point, module/service ownership, state
ownership, boundary, and significant data-flow claims. The map is an upstream
artifact, not proof: downstream consumers must independently re-derive ownership
and boundary claims their conclusions depend on from actual code, and check other
load-bearing relationships. State the task-scoped coverage and stopping reason;
never present the map as exhaustive repository documentation.

No orientation-specific hard gate is added. G6/G7 human-authority gates retain
no escape for restricted execution or compatibility exceptions. Follow host
permissions and available baseline authority rules; orientation does not grant
authority to perform restricted actions.
