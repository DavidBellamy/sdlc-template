# RFCs and decision records

How proposals and decisions are captured, and why they are two different
artifacts rather than one.

## RFC and ADR are different jobs

- An **RFC (Request for Comments)** is a *proposal*: the full problem, the
  design, the alternatives, the tradeoffs. It is forward-looking and mutable
  while under discussion. It is the *deliberation*.
- An **ADR (Architecture Decision Record)** is a *decision*: terse, structured
  as Context / Decision / Consequences. It is backward-looking and immutable
  from birth. It is the *outcome*.

One does not become the other. A single RFC usually produces **several** ADRs
(one architecture proposal yields decisions about storage, deployment, and
APIs). The ADR is a distilled decision that points back to the RFC, not the RFC
renamed.

## Why there is no `rfc/` directory

Because the RFC already has a permanent, versioned, commentable home: the
**`design_doc` GitHub issue**. GitHub keeps closed issues and their entire
discussion thread forever. Copying the proposal into an `rfc/` file as well would
store the same knowledge twice, which violates DRY. So:

> The `design_doc` issue **is** the RFC. When it is accepted, write an ADR under
> `docs/adr/` that records each decision and links back to the issue (`See #42`).

(If you ever need the long-form rationale to be self-contained inside the repo,
independent of GitHub, then either keep an `rfc/` directory or write fatter ADRs.
The default here is to trust issues as durable storage.)

## Lifecycle

```text
Open a design_doc issue   ->  discuss, revise (the RFC, mutable)
        |
     accepted
        |
        v
Write ADR(s) under docs/adr/   ->  immutable; each links back to the issue
        |
Implement   ->  PR references the issue (Closes #N) and the ADR
```

## Writing an ADR

Copy [`docs/adr/0000-template.md`](../adr/0000-template.md) to the next number, fill it
in, and open a PR. Keep it short: the point is a fast lookup of *what was decided
and why*, not a re-run of the whole debate (that is what the linked issue is
for). Never edit an accepted ADR to reverse it; write a new ADR that supersedes
it and mark the old one superseded.

See [the ADR log](../adr/index.md).
