# Getting started

## Use the template

1. Click **Use this template** on the GitHub repo to create your own project.
2. Clone it and run the bootstrap:

   ```bash
   ./scripts/dev/setup.sh
   ```

   This creates the virtual environment with `uv`, installs the pre-commit
   hooks, and runs the full gate once (`ruff format`, `ruff`, `ty`, `pytest`) so
   you start from a known-green baseline.

## Make it yours

- Replace `src/sdlc_template/` and `tests/` with your own package and tests.
- Update `pyproject.toml` (`name`, `description`, dependencies).
- Edit `plans/goals.md` for your first milestone, and create a matching GitHub
  Milestone whose description is the definition of done.
- Set ownership in `.github/CODEOWNERS`.
- Fill in the C4 [context](architecture/context.md) and
  [containers](architecture/containers.md) for your system.

## Daily loop

Read [the lifecycle](process/lifecycle.md) for the full process. Day to day:

1. Open an issue (feature, bug, or design_doc) with acceptance criteria.
2. Branch, implement with tests, keep the gate green locally.
3. Open a PR that says `Closes #N` and re-checks the issue's acceptance criteria.
4. Merge when CI is green and review is resolved. Squash; history stays linear.
5. Add a `CHANGELOG.md` entry, and an ADR if you made an architectural decision.

See [CONTRIBUTING](https://github.com/davidbellamy/sdlc-template/blob/main/CONTRIBUTING.md)
for the conventions.
