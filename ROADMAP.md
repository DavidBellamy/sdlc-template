# Roadmap

The narrative companion to GitHub Milestones. Milestones are the living tracker
(issues open and close against them); this file is the prose plan and, most
importantly, the **out-of-scope** boundary. Planning depth tapers with horizon:
near versions are detailed, far ones are placeholders.

## Versioning

Milestones are named by semantic version. Each milestone's description is its
**definition of done**, so the plan and the tracker stay in sync.

## v0.1.0 (current): the template itself

- A working, green pipeline: ruff + ty + pytest, gated by branch protection.
- The full process scaffolding: planning, C4 design docs, ADR log, interface
  contract conventions, issue/PR Forms, CI/CD split.
- Definition of done: a new project can click "Use this template" and have all
  of the above from its first commit.

## v0.2.0 (next): make the example real

- Replace the placeholder package with a small but genuine domain example.
- Add a post-merge CD path (registry push + canary + rollback) to demonstrate
  the CI/CD boundary end to end.

## v1.0.0 (later): adoption

- A `scripts/init.sh` that renames the package and resets the example for a fresh
  project.
- A short screencast of the daily loop.

## Out of scope (for now)

- Multiple language ecosystems. This template is Python-first by design; the
  process scaffolding is language-agnostic but the config is not.
- Monorepo layouts. The structure assumes one project per repo.
- Cloud-specific deployment. The CD example stays registry-agnostic.
