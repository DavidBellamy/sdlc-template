# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[semantic versioning](https://semver.org/).

For small projects this file plus the commit and PR history is a sufficient,
lightweight decision record; adopt the formal `docs/adr/` log for the decisions
whose rationale would otherwise be lost.

> Pre-1.0: minor versions may include breaking changes.

## [Unreleased]

### Added

- Dependabot now watches the `docker` ecosystem (base images in
  `docker/Dockerfile`) (#3).
- CI requires every pull request to add a `CHANGELOG.md` entry (or carry a
  `skip-changelog` label), gated through the `lint-typecheck-test` umbrella (#15).

### Changed

- Standardized on Python 3.13 across `requires-python`, ruff/ty config,
  `.python-version`, the CI matrix, and the Docker base image; regenerated
  `uv.lock` (#14).

### Fixed

- CI `test` matrix now runs pytest in the correct per-version environment with
  the dev extra (`uv run --extra dev --python <ver> pytest`), fixing a missing
  pytest on the 3.13 leg (#1).
- `docs` workflow step name no longer contains a colon that broke YAML parsing
  and prevented the workflow from loading (#1).

## [0.1.0] - 2026-06-02

### Added

- Initial process-first template scaffold.
- Python skeleton (`src/sdlc_template`) with a green gate: ruff, ty, pytest.
- CI workflows: `ci.yml` (lint/typecheck/test matrix + umbrella check),
  `secrets.yml` (gitleaks), `docs.yml` (MkDocs to Pages), `build-image.yml`
  (shift-left Docker build gate).
- Issue Forms (feature, bug, design_doc) and a PR template.
- Docs site: the SDLC lifecycle, RFC/ADR process, C4 architecture pages, and the
  ADR log.
- Planning docs: `plans/goals.md`, `plans/raci.md`, `ROADMAP.md`.
- `CODEOWNERS`, `dependabot.yml`, `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`.

[Unreleased]: https://github.com/davidbellamy/sdlc-template/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/davidbellamy/sdlc-template/releases/tag/v0.1.0
