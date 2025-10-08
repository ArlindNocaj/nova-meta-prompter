#!/usr/bin/env python3
"""Bump the patch version in pyproject.toml"""
import re
import sys
from pathlib import Path


def bump_version(version_str: str, part: str = "patch") -> str:
    """Bump semantic version string."""
    major, minor, patch = map(int, version_str.split("."))

    if part == "major":
        return f"{major + 1}.0.0"
    elif part == "minor":
        return f"{major}.{minor + 1}.0"
    else:  # patch
        return f"{major}.{minor}.{patch + 1}"


def main():
    """Bump version in pyproject.toml."""
    part = sys.argv[1] if len(sys.argv) > 1 else "patch"

    if part not in ["major", "minor", "patch"]:
        print(f"Invalid version part: {part}. Use major, minor, or patch.")
        sys.exit(1)

    pyproject_path = Path(__file__).parent / "pyproject.toml"
    content = pyproject_path.read_text()

    # Find current version
    match = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
    if not match:
        print("Could not find version in pyproject.toml")
        sys.exit(1)

    old_version = match.group(1)
    new_version = bump_version(old_version, part)

    # Replace version
    new_content = re.sub(
        r'^version\s*=\s*"[^"]+"',
        f'version = "{new_version}"',
        content,
        count=1,
        flags=re.MULTILINE
    )

    # Update __init__.py as well
    init_path = Path(__file__).parent / "nova_meta_prompter" / "__init__.py"
    init_content = init_path.read_text()
    init_content = re.sub(
        r'^__version__\s*=\s*"[^"]+"',
        f'__version__ = "{new_version}"',
        init_content,
        count=1,
        flags=re.MULTILINE
    )

    # Write files
    pyproject_path.write_text(new_content)
    init_path.write_text(init_content)

    print(f"Bumped version: {old_version} → {new_version}")


if __name__ == "__main__":
    main()
