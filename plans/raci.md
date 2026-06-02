# RACI

Ownership has two homes. The **Responsible/Accountable** part is machine-enforced
in [`.github/CODEOWNERS`](../.github/CODEOWNERS) (GitHub requires an owner's
review). This file holds only the **Consulted/Informed** columns, which
CODEOWNERS cannot express, plus cross-team stakeholders.

## Doctrine

- Exactly one **A** (Accountable) per area. The A is the single neck to ring.
- The A is **not** also an **R** for that area.
- At least one **R** (Responsible, the doer) per area.

## Matrix

| Area / decision | A (accountable) | R (responsible) | C (consulted) | I (informed) |
| --- | --- | --- | --- | --- |
| Architecture | @DavidBellamy | @DavidBellamy-or-delegate | <reviewers> | <team> |
| Release / versioning | @DavidBellamy | <doer> | <users> | <team> |
| <component> | <A> | <R> | <C> | <I> |

> Note: in the example matrix the same handle appears as A and R because this is
> a solo template. On a real team, split them per the doctrine above.
