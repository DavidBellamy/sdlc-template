# Minimal image for the example package. Built (not pushed) on every PR by
# .github/workflows/build-image.yml to gate "does the image still build" before
# merge. Uses uv for fast, reproducible installs.
FROM python:3.13-slim

# Copy the uv binary from its official image (no curl|sh needed).
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy only what is needed to resolve and install dependencies first, so this
# layer caches across source-only changes.
COPY pyproject.toml README.md ./
COPY src ./src

# Install into the system environment (no venv layer needed in a container).
RUN uv pip install --system --no-cache .

# Smoke check that the package imports. A real service would set an ENTRYPOINT.
RUN python -c "import sdlc_template; print(sdlc_template.__name__, 'ok')"
