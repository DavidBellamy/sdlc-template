# sdlc-template

A process-first **template repository** for new software projects. The code is
deliberately trivial; the value is the software development lifecycle (SDLC)
scaffolding around it: planning, design, decision records, interface contracts,
quality gates, and CI/CD, all version-controlled and reviewable.

Click **Use this template** on GitHub to start a new project with all of this in
place from the first commit.

## What this gives you

| Concern | Where it lives | Why there |
| --- | --- | --- |
| The process itself | [`docs/process/lifecycle.md`](docs/process/lifecycle.md) | The full SDLC, from stakeholders to launch |
| Goals / non-goals per milestone | [`plans/goals.md`](plans/goals.md) | Working PM doc, scoped to a release |
| Ownership (R/A) | [`.github/CODEOWNERS`](.github/CODEOWNERS) | Machine-enforced; gates review |
| Ownership (C/I) | [`plans/raci.md`](plans/raci.md) | The parts CODEOWNERS cannot express |
| Architecture (C4 L1-L3) | [`docs/architecture/`](docs/architecture/) | Human-authored, published via MkDocs |
| Decisions | [`docs/adr/`](docs/adr/) | Immutable, terse, one per decision |
| Proposals (RFCs) | GitHub Issues (`design_doc` form) | Mutable, threaded, permanent on GitHub |
| Machine-checkable interfaces | [`schema/`](schema/), `src/**` type sigs | Build inputs, co-located with code |
| Prose interface contracts | [`docs/architecture/interfaces.md`](docs/architecture/interfaces.md) | For CLI/shell/env contracts with no machine format |
| Code standards | [`pyproject.toml`](pyproject.toml), [`.pre-commit-config.yaml`](.pre-commit-config.yaml) | Executable and enforced, not prose |
| Timeline | GitHub Milestones (+ [`ROADMAP.md`](ROADMAP.md)) | Living, not a static chart |

## Toolchain

Python with [Astral](https://astral.sh/) tooling: [`uv`](https://docs.astral.sh/uv/)
(envs and locking), [`ruff`](https://docs.astral.sh/ruff/) (lint and format),
[`ty`](https://github.com/astral-sh/ty) (type checking). Tests with `pytest`.
Docs with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Quick start

```bash
# After clicking "Use this template" and cloning your new repo:
./scripts/dev/setup.sh   # creates the venv, installs hooks, runs the gate once
```

The same gate runs in CI on every pull request (see
[`.github/workflows/ci.yml`](.github/workflows/ci.yml)).

## How the pieces connect

The artifacts are not independent; they form one traceability chain so that
"everything is written down" also means "everything is linked":

```
ROADMAP version
  -> GitHub Milestone (description = definition of done)
    -> Issue (feature_request / design_doc, with acceptance-criteria checkboxes)
      -> Pull Request (Closes #N, re-checks the same criteria, justifies deferrals)
        -> squash commit carrying (#N)
          -> CHANGELOG.md entry
          -> ADR (if an architectural decision was made)
```

See [`docs/process/lifecycle.md`](docs/process/lifecycle.md) for the full process
and [`CONTRIBUTING.md`](CONTRIBUTING.md) for day-to-day conventions.

## License

Apache-2.0. See [`LICENSE`](LICENSE).
