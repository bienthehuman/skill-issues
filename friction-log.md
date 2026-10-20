# Friction log

Source: SPEC Appendix B. One line per entry:

`date | type | skill | prompt | what happened | proposed change`

Types: `misfire` (unnecessary activation), `miss` (missing activation), `heavy` (excess ceremony), `wrong` (incorrect output), `inherited` (propagated upstream error), `opaque` (reasoning not followable).

Every baseline or skill change must be traceable to an entry. No behavioral runs have occurred yet.

Initial baseline provenance (2026-10-20): Milestone 0 extracted SPEC section 4 verbatim, with no rule changes. This bootstrap record is not an observed routing miss and must not enter evaluation metrics. Record subsequent behavioral changes using the format above.
