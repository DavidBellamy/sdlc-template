# C4 Level 2: Containers

The keystone map: zoom in one level to the major runtime/deliverable pieces and
how they talk. "Container" here means a separately deployable or runnable unit
(a service, a CLI, a database, a CI pipeline), not specifically a Docker
container.

The diagram describes *this template* as an example.

```mermaid
flowchart TD
    dev[Developer]
    subgraph repo[sdlc-template repository]
        pkg[src/sdlc_template<br/>example Python package]
        tests[tests<br/>pytest suite]
        ci[CI pipeline<br/>ruff + ty + pytest umbrella]
        img[Docker image<br/>built on PR, not pushed]
        site[MkDocs site<br/>published to Pages]
    end

    dev -->|writes| pkg
    dev -->|writes| tests
    pkg --> ci
    tests --> ci
    pkg --> img
    repo -->|push to main| site
    ci -->|gates| dev
```

## What belongs here

- Each major container, its responsibility, and its key technology.
- The data/control flow between containers.
- The contracts at the seams (link to [interfaces](interfaces.md)).

## What does not belong here

- The internals of any one container (that is [Level 3](components.md), written
  lazily).
- Class-level detail (Level 4, never hand-maintained).
