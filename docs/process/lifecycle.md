# The software development lifecycle

This is the process the template encodes. The guiding principle, the steps, and
the reasoning behind each choice.

## Principle

**All key information is written and version-controlled, and changes to it go
through review.** That includes the stakeholder list, goals and non-goals,
design docs, decision records, ownership, and the timeline. If a decision only
exists in someone's head or a chat message, it does not exist.

Two corollaries shape everything below:

1. **Match the medium to the change-speed.** Things that change at
   architecture-speed (designs, decisions, contracts) are hand-authored markdown
   gated by review. Things that change at code-speed (API reference, class
   diagrams) are generated from code, never hand-maintained.
2. **Every rule must map to an enforcement mechanism.** A rule with no detector
   and no recovery action is a wish. Branch protection is the gate, CI is the
   detector, revert is the recovery. Do not write down a rule you cannot enforce.

## Governance weight scales with team size and blast radius

Before the steps: this process is a dial, not a fixed weight. A solo, greenfield
spike needs almost none of it; a multi-developer service that others depend on
needs all of it. Turn the dial up as the team grows and as breakage gets more
expensive. Step 0 is the first click of that dial.

## 0. Bootstrap (brownfield on-ramp)

Before any feature work on an existing repo, make the invariant measurable:

- Turn on branch protection, required review, and CI on `main`.
- Define what "`main` works" means: green CI, a passing smoke test, and
  deployable. Without a definition, the invariant is unenforceable.

The initial scaffold is pushed to `main` directly (you cannot gate on a branch
that does not exist yet); protection turns on immediately after, and from then
on `main` is only ever updated through reviewed, CI-passing PRs.

## 1. Stakeholders and decision authority

Name the core devs, leadership, and target users. Then assign **decision
authority**:

- **Ownership (Responsible / Accountable)** is expressed in
  [`.github/CODEOWNERS`](https://github.com/davidbellamy/sdlc-template/blob/main/.github/CODEOWNERS),
  which GitHub enforces by requiring an owner's review. This is the executable
  form; a markdown table would rot.
- **Consulted / Informed** cannot be expressed in CODEOWNERS, so the C and I of
  RACI live in [`plans/raci.md`](https://github.com/davidbellamy/sdlc-template/blob/main/plans/raci.md).
- RACI doctrine: there is exactly one **A** per area, the A is not also an **R**,
  and there is at least one **R** per A. R is the doer; A is the single neck to
  ring.
- For one-off decisions (as opposed to ongoing ownership), do not use RACI; the
  ADR's "who decided" line is the right record.

## 2. Goals, non-goals, and definition of done

Write the milestone's goals in [`plans/goals.md`](https://github.com/davidbellamy/sdlc-template/blob/main/plans/goals.md),
split into:

- **Invariants**: must hold, non-negotiable. Frozen in writing.
- **Hypotheses**: believed but being tested. Dated and explicitly provisional.
- **Non-goals**: what you are deliberately not doing, with the reason. Non-goals
  prevent scope creep and settle arguments cheaply.

The **definition of done** is the milestone's measurable exit criterion. In this
template, the GitHub Milestone description doubles as the definition of done, so
the plan and the tracker cannot drift apart.

## 3. Design: de-risk, then draw

1. **Spike the riskiest unknowns first.** A spike is a time-boxed, throwaway
   experiment that answers one question ("can enroot import this image on the
   target FS?"). Its job is to convert an unknown into a known fact before the
   design commits to it. Spikes are exempt from TDD; you delete them.
2. **Write the design** as C4 levels 1 and 2 (see [the architecture docs](../architecture/context.md)).
   While in flight, a design is an RFC living as a `design_doc` issue: mutable
   and commentable. Once accepted, it is committed and each decision is recorded
   as an ADR.
3. **Define the interfaces** in a machine-checkable format where one exists
   (type signatures, JSON Schema, OpenAPI, protobuf) co-located with the code;
   use a prose markdown table only for contracts with no machine format
   (CLI/shell/env-var). See [interfaces](../architecture/interfaces.md). Do this
   lazily: only freeze a contract before two people build across it in parallel.
4. **C4 level 3 (components)** is written lazily, only when level 2's one
   paragraph about a component stops being enough. **Level 4 (code) is never
   hand-maintained** because it changes at code-speed; generate it if ever needed.

## 4. Set up for execution

- **Ownership**: primary plus backup per component (CODEOWNERS + raci.md).
  Interfaces are shared-owned: changing a contract needs both sides to agree.
- **Communication**: agree the channels and the issue/PR conventions
  (see [CONTRIBUTING](https://github.com/davidbellamy/sdlc-template/blob/main/CONTRIBUTING.md)).
- **Cadence**: short status standups, synchronous if the team is small and
  co-located, async-written otherwise (which also satisfies the
  everything-in-writing principle).
- **Timeline**: GitHub Milestones (scope/version-driven), not a static Gantt.
  Milestones are connected to the work, so they cannot silently lie the way a
  hand-maintained chart does. See [`ROADMAP.md`](https://github.com/davidbellamy/sdlc-template/blob/main/ROADMAP.md).
- **Code standards**: defined as executable config
  ([`pyproject.toml`](https://github.com/davidbellamy/sdlc-template/blob/main/pyproject.toml),
  [`.pre-commit-config.yaml`](https://github.com/davidbellamy/sdlc-template/blob/main/.pre-commit-config.yaml)),
  enforced at three mirrored layers: pre-commit (local), CI, branch protection.

## 5. Implement

- **Tests proportional to blast radius.** Well-specified contracts and
  invariants get tests; throwaway spikes do not. A test that does not gate the
  merge is documentation, not a guarantee, so the test job is wired into branch
  protection via the umbrella check.
- **The invariant "`main` works" holds from the first commit**, enforced by CI
  plus one-command revert, not by hoping nobody breaks it.
- **CI vs CD: the merge is the boundary.** Everything that can be checked before
  merge without needing production is a pre-merge gate (build, lint, types,
  tests, hermetic smoke). Everything that needs the deployed reality runs
  post-merge and is protected by a canary plus rollback, because you cannot
  deploy `main` before `main` exists. See
  [`build-image.yml`](https://github.com/davidbellamy/sdlc-template/blob/main/.github/workflows/build-image.yml)
  for the shift-left build gate.

## 6. Launch, gather feedback, and loop

Define **kill/pivot criteria before** launch. Release the milestone, gather
feedback, and route it back to step 2 (goals) or step 3 (design). The process is
a control loop, not a pipeline: every step has an exit criterion and a path
backward. After launch, the invariant's blast radius grows (real users now
depend on `main`); its existence does not change.

## The traceability chain

The artifacts are not independent. They link into one chain so that "written
down" also means "connected":

```text
ROADMAP version
  -> Milestone (description = definition of done)
    -> Issue (feature_request / design_doc, acceptance-criteria checkboxes)
      -> Pull Request (Closes #N, re-checks the same criteria, justifies deferrals)
        -> squash commit carrying (#N)
          -> CHANGELOG.md entry
          -> ADR (if an architectural decision was made)
```

## Anti-patterns this process guards against

- **Documented process ahead of provisioned state**: referencing labels,
  milestones, or settings that were never created. Every rule here maps to a real
  file or a real GitHub setting.
- **The unenforceable invariant**: "`main` always works" with no smoke test and
  no rollback.
- **Big design up front**: writing all of C4 and every component doc before any
  code. De-risk with spikes, write L1/L2, defer L3, never hand-write L4.
- **Tests that do not gate**: a green local test suite that CI does not require.
