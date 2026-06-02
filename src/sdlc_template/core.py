"""Example domain logic: parsing semantic version strings.

Chosen because milestones in this template are named by semantic version (see
ROADMAP.md), so the example ties back to the process the template teaches.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SemanticVersion:
    """An immutable major.minor.patch version.

    Attributes:
        major: Backwards-incompatible API version.
        minor: Backwards-compatible feature version.
        patch: Backwards-compatible bug-fix version.
    """

    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        """Render as the canonical ``major.minor.patch`` string."""
        return f"{self.major}.{self.minor}.{self.patch}"


def parse_semver(version: str) -> SemanticVersion:
    """Parse a ``major.minor.patch`` string into a SemanticVersion.

    Args:
        version: A version string such as ``"1.4.2"``. A leading ``v`` is
            accepted and stripped (``"v1.4.2"``).

    Returns:
        The parsed SemanticVersion.

    Raises:
        ValueError: If the string is not three dot-separated non-negative
            integers.
    """
    cleaned = version.removeprefix("v")
    parts = cleaned.split(".")
    if len(parts) != 3:
        raise ValueError(f"expected major.minor.patch, got {version!r}")
    try:
        major, minor, patch = (int(p) for p in parts)
    except ValueError as exc:
        raise ValueError(f"version components must be integers: {version!r}") from exc
    if major < 0 or minor < 0 or patch < 0:
        raise ValueError(f"version components must be non-negative: {version!r}")
    return SemanticVersion(major, minor, patch)
