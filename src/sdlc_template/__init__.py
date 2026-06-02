"""sdlc_template: a trivial example package.

The point of this package is not the code, it is to make the CI gate (ruff,
ty, pytest) real and green so the template demonstrates a working pipeline.
Replace this module with your own when you use the template.
"""

from sdlc_template.core import SemanticVersion, parse_semver

__all__ = ["SemanticVersion", "parse_semver"]
