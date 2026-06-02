# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[semantic versioning](https://semver.org/).

For small projects this file plus the commit and PR history is a sufficient,
lightweight decision record; adopt the formal `docs/adr/` log for the decisions
whose rationale would otherwise be lost.

> Pre-1.0: minor versions may include breaking changes.

## [Unreleased]

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
