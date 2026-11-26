#!/usr/bin/env python3
"""Validate an Agent Skill package.

Checks that SKILL.md exists, has valid YAML frontmatter with the required
fields, respects size limits, and that all relative markdown links resolve.

Usage:
    python3 scripts/validate_skill.py [path-to-skill-dir]

Exit codes:
    0  valid
    1  validation errors found
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)]+)\)")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_SKILL_BYTES = 20_000
REQUIRED = ("name", "description")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with a YAML frontmatter block (---)")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("frontmatter is not closed with ---")
    raw = text[4:end]
    body = text[end + 4 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def validate(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_file = root / "SKILL.md"

    if not skill_file.is_file():
        return [f"missing {skill_file.relative_to(root)}"], warnings

    text = skill_file.read_text(encoding="utf-8")

    if len(text.encode("utf-8")) > MAX_SKILL_BYTES:
        errors.append(f"SKILL.md exceeds {MAX_SKILL_BYTES} bytes; move detail into references/")

    try:
        meta, body = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)], warnings

    for field in REQUIRED:
        if field not in meta or not meta[field]:
            errors.append(f"frontmatter missing required field: {field}")

    name = meta.get("name", "")
    if name:
        if len(name) > MAX_NAME:
            errors.append(f"name exceeds {MAX_NAME} characters")
        if not NAME_RE.match(name):
            errors.append("name must be lowercase kebab-case (a-z, 0-9, hyphens)")
        if name != root.name:
            warnings.append(
                f"name '{name}' does not match directory '{root.name}' "
                "(rename the install folder to match before installing)"
            )

    description = meta.get("description", "")
    if len(description) > MAX_DESCRIPTION:
        errors.append(f"description exceeds {MAX_DESCRIPTION} characters")

    if not re.search(r"^#\s+\S", body, flags=re.MULTILINE):
        errors.append("SKILL.md body must contain an H1 heading")

    for target in LINK_RE.findall(body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (root / clean).exists():
            errors.append(f"broken relative link: {target}")

    return errors, warnings


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors, warnings = validate(root)
    for warn in warnings:
        print(f"WARN {warn}")
    if errors:
        print(f"FAIL {root}")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"OK {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
