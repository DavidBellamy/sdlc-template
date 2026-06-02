# Contributing

The day-to-day conventions. The full process is in
[`docs/process/lifecycle.md`](docs/process/lifecycle.md).

## Quick start

```bash
./scripts/dev/setup.sh
```

Creates the venv, installs pre-commit hooks, and runs the gate once.

## Code standards

The standards are **executable config**, not prose. This document does not
restate the rules; it points at them so there is one source of truth:

- Lint and format: [`ruff`](https://docs.astral.sh/ruff/), configured in
  [`pyproject.toml`](pyproject.toml).
- Type checking: [`ty`](https://github.com/astral-sh/ty), configured in
  `pyproject.toml`.
- Tests: `pytest`, configured in `pyproject.toml`.

They run at three mirrored layers: pre-commit (local),
[`ci.yml`](.github/workflows/ci.yml) (required), and branch protection.

## Issues

Every issue enters through a Form (feature, bug, or design_doc); freeform issues
are disabled. Give features concrete **acceptance criteria** as checkboxes. A
design proposal is a `design_doc` issue and is the RFC; see
[decision records](docs/process/decision-records.md).

## Branches and commits

- Branch from `main`: `feature/<name>`, `fix/<name>`, or `pr/<name>`.
- Commit messages: imperative mood, subject under 72 characters, the *why* in the
  body. Architecture and rationale belong in the body or an ADR, not the subject.
- Do not add `Co-Authored-By` lines unless there was real pairing.

## Pull requests

- One logical change per PR. If the description needs "and", consider splitting.
- Use the PR template: say `Closes #N`, restate the issue's acceptance criteria
  as checkboxes, and tick what this PR satisfies (justify any deferral).
- Include verification evidence (the gate passing locally).
- If the PR makes an architectural decision, add an ADR under `docs/adr/`.
- Merges are squash, history stays linear, branches auto-delete.
- Reviews are welcome; whether they are *required* is set by branch protection
  per the team's size (see the lifecycle doc on governance weight).

## Communication and cadence

> Fill in for your team. Single repo: keep it here. Multi-repo team: keep it in
> the team knowledge base and link it here, so the standup time is not copied
> into ten repos.

- Chat channel: <link>
- Standup: <sync if small and co-located, else async-written; cadence>
