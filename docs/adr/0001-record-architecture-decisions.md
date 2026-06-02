# ADR-0001: Record architecture decisions

- **Status**: Accepted
- **Date**: 2026-06-02
- **Deciders**: @DavidBellamy
- **RFC**: n/a (bootstrap decision)

## Context

Decisions made during a project's life are easy to lose. The code shows *what*
the system does now, but not *why* it became that way. On a team with churn
(interns, part-timers, contractors), the rationale leaves with the people, and
the next person re-litigates settled questions or is afraid to touch anything.

## Decision

We will keep an append-only log of architecture decision records under
`docs/adr/`. Each record is terse (Context / Decision / Consequences), immutable
once accepted, and links back to the `design_doc` issue (the RFC) for the full
rationale. Reversing a decision means writing a new, superseding ADR.

## Consequences

- The "why" survives independent of who is on the team. This is the
  highest-return artifact on a team with turnover.
- A small, ongoing tax: every load-bearing decision costs one short markdown file
  and a PR.
- The ADR log and the `design_doc` issues divide cleanly: issues hold the
  long-form, mutable deliberation; ADRs hold the terse, immutable outcome. No
  separate `rfc/` directory is needed.
