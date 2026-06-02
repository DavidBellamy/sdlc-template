# Interface contracts

An interface spec is the *contract* at a seam between two components. It is the
part that must be agreed before two people build across the seam in parallel, so
it is shared-owned: changing it requires both sides to agree.

## Specify in a machine-checkable format when one exists

A diagram (mermaid sequence or class) can *illustrate* an interface, but it
cannot *be* the contract, because nothing enforces that the diagram matches
reality. The contract itself goes in the format a machine can check, and that
format lives **next to the code**, not in `docs/`, so PR review sees the contract
and its implementation together and CI can enforce it.

| Interface type | Format | Lives in |
| --- | --- | --- |
| HTTP API | OpenAPI (YAML) | next to the service |
| RPC | Protobuf `.proto` | `proto/` |
| Data / config | JSON Schema | [`schema/`](https://github.com/davidbellamy/sdlc-template/blob/main/schema/config.schema.json) |
| Library API | type signatures + docstrings | `src/**` |

The example in this repo is [`schema/config.schema.json`](https://github.com/davidbellamy/sdlc-template/blob/main/schema/config.schema.json):
a machine-checkable config contract co-located with the code, not buried in docs.

## Use a prose table only when no machine format exists

CLI flags, shell-function outputs, and environment-variable contracts have no
standard machine format. For those, write a disciplined markdown table. The
columns that make it a real contract (not just a description) are **type**,
**allowed values**, **when it is set**, and the **error/precondition behavior**.
The last one is the half people forget and the half that causes integration bugs.

### Example: a shell-function output contract

`resolve_config()` sets these globals in the caller's shell on success (exit 0):

| Name | Type | Meaning | Set when |
| --- | --- | --- | --- |
| `CONFIG_PATH` | abs path | resolved config file, symlinks resolved | always on success |
| `CONFIG_SOURCE` | enum: `flag` \| `env` \| `default` | which resolution branch won | always on success |
| `CONFIG_DIGEST` | `sha256:...` or `""` | content hash; empty if unknown | always; may be empty |

Preconditions: caller passes `--config-dir`. Error contract: non-zero exit,
globals unset, diagnostic on stderr.
