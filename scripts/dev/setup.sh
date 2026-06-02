#!/usr/bin/env bash
# Reproducible local dev environment. One command to a working, gated checkout.
# Mirrors the principle in docs/process/lifecycle.md: the verification step
# should be portable, not "works on my machine".
set -euo pipefail

cd "$(dirname "$0")/../.."

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required. Install: https://docs.astral.sh/uv/getting-started/installation/" >&2
  exit 1
fi

echo "==> Creating venv and installing dev dependencies"
uv sync --extra dev

echo "==> Installing pre-commit hooks"
uv run pre-commit install

echo "==> Running the gate once to confirm a green baseline"
uv run ruff format --check .
uv run ruff check .
uv run ty check
uv run pytest

echo "==> Ready. The same checks run in CI (.github/workflows/ci.yml)."
