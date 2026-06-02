# Architecture decision records

An append-only log of the load-bearing decisions and why they were made. The
living docs answer "how does the system work now"; this log answers "why did it
become this way", which is the question that is irrecoverable once the people who
decided move on.

## Rules

- One decision per record. Numbered sequentially.
- Immutable once accepted. To reverse a decision, write a new ADR that supersedes
  the old one and mark the old one `Superseded by ADR-NNNN`.
- Keep it terse: Context, Decision, Consequences. Link the `design_doc` issue for
  the full rationale.

## How to add one

Copy [`0000-template.md`](0000-template.md) to the next number and open a PR. See
[the decision-records process](../process/decision-records.md).

## Log

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
