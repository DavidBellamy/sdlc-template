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

- Branch from `main` using:

  ```text
  <type>/<issue-number>-<short-kebab-description>
  ```

  Examples:

  ```text
  feature/12-add-project-bootstrap-command
  fix/18-handle-missing-roadmap-version
  design/21-record-release-gate-decision
  docs/34-clarify-lifecycle-step-zero
  ```

- Issue-required branch types:

  | Type | Use for |
  | --- | --- |
  | `feature` | New user-facing or project-facing capability |
  | `fix` | Bug fix or incorrect behavior |
  | `design` | Architecture, ADR, lifecycle, or process design work |
  | `refactor` | Internal restructuring without behavior change |
  | `perf` | Performance improvement |
  | `spike` | Time-boxed investigation or prototype |

- Issue-or-`no-issue` branch types:

  | Type | Use for |
  | --- | --- |
  | `docs` | Documentation-only changes |
  | `test` | Test-only changes |
  | `ci` | GitHub Actions, checks, workflows, automation |
  | `build` | Build system, packaging, Docker, toolchain |
  | `deps` | Dependency updates |
  | `chore` | Low-risk maintenance that does not fit another type |

- Special branch types:

  | Type | Use for |
  | --- | --- |
  | `release` | Release preparation branch, e.g. `release/0.2.0` |
  | `hotfix` | Urgent patch branch, e.g. `hotfix/0.2.1-fix-docs-publish` |

- For trivial maintenance changes that do not need an issue, use `no-issue`:

  ```text
  docs/no-issue-fix-typo
  ci/no-issue-pin-action-version
  deps/no-issue-bump-ruff
  chore/no-issue-update-codeowners-comment
  ```

- `no-issue` is only allowed for `docs`, `test`, `ci`, `build`, `deps`, and
  `chore`. Features, bugs, design changes, refactors, performance work, and
  spikes should have an issue.
- Branch names are enforced in CI. Use lowercase kebab-case; do not use spaces,
  underscores, personal names, or vague names such as `pr/foo`.
- Commit messages: imperative mood, subject under 72 characters, the *why* in the
  body. Architecture and rationale belong in the body or an ADR, not the subject.
- Do not add `Co-Authored-By` lines unless there was real pairing.

## Pull requests

- One logical change per PR. If the description needs "and", consider splitting.
- Use the PR template: say `Closes #N` for issue-linked work, or explain why the
  PR is allowed to use `no-issue`; restate the issue's acceptance criteria as
  checkboxes when there is a linked issue.
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
