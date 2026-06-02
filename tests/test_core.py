"""Tests for sdlc_template.core.

Demonstrates the test-proportional-to-blast-radius idea from the process doc:
the parser is a small, well-specified contract, so it gets exhaustive
happy-path and error-path coverage.
"""

import pytest

from sdlc_template.core import SemanticVersion, parse_semver


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("1.4.2", SemanticVersion(1, 4, 2)),
        ("v1.4.2", SemanticVersion(1, 4, 2)),
        ("0.0.0", SemanticVersion(0, 0, 0)),
        ("10.20.30", SemanticVersion(10, 20, 30)),
    ],
)
def test_parse_semver_valid(text: str, expected: SemanticVersion) -> None:
    assert parse_semver(text) == expected


@pytest.mark.parametrize(
    "text",
    ["1.2", "1.2.3.4", "1.2.x", "", "a.b.c", "-1.0.0", "1..2"],
)
def test_parse_semver_invalid(text: str) -> None:
    with pytest.raises(ValueError, match=r"version|expected"):
        parse_semver(text)


def test_semantic_version_str_roundtrip() -> None:
    assert str(parse_semver("3.7.11")) == "3.7.11"
