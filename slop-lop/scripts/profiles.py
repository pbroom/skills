#!/usr/bin/env python3
"""Find and validate saved Slop Lop checks and locate exact text in source files."""

import argparse
import json
import os
import re
import sys
from pathlib import Path


PROFILE_FIELDS = ("title", "applies_to", "failure", "impact", "preserve", "repair", "verify")


def read_profile(path):
    if path.suffix != ".json" or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", path.stem):
        raise ValueError("expected a lowercase, hyphenated ID with a .json extension")
    if not path.is_file():
        raise ValueError("expected a regular file")

    profile = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(profile, dict):
        raise ValueError("expected a JSON object")
    unknown = profile.keys() - {*PROFILE_FIELDS, "literal"}
    if unknown:
        raise ValueError(f"unknown fields: {', '.join(sorted(unknown))}")
    for field in PROFILE_FIELDS:
        value = profile.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"'{field}' must be a nonempty string")
    if "literal" in profile:
        value = profile["literal"]
        if not isinstance(value, str) or not value.strip() or value.splitlines() != [value]:
            raise ValueError("'literal' must be a nonempty single line")
    return profile


def list_profiles(project):
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").expanduser()
    roots = (
        ("project", project, ".slop-lop"),
        ("user", codex_home.resolve(), "slop-lop"),
    )
    summaries = []
    failed = False
    for scope, root, subdir in roots:
        directory = root / subdir / "profiles"
        try:
            if not directory.resolve().is_relative_to(root):
                raise ValueError("profile directory points outside its root")
            paths = sorted(path for path in directory.iterdir() if path.suffix == ".json")
        except FileNotFoundError:
            continue
        except (OSError, RuntimeError, ValueError) as error:
            print(f"{directory}: {error}", file=sys.stderr)
            failed = True
            continue

        for path in paths:
            try:
                if not path.resolve().is_relative_to(directory.resolve()):
                    raise ValueError("profile points outside its directory")
                profile = read_profile(path)
            except (OSError, RuntimeError, ValueError) as error:
                print(f"{path}: {error}", file=sys.stderr)
                failed = True
                continue
            summaries.append({
                "id": path.stem,
                "title": profile["title"],
                "applies_to": profile["applies_to"],
                "scope": scope,
                "path": str(path),
            })
    return summaries, int(failed)


def locate(project, files, literal):
    matches = {}
    for file in files:
        path = (project / file).resolve()
        if not path.is_relative_to(project) or not path.is_file():
            raise ValueError(f"{file}: expected a regular file inside {project}")
        with path.open(encoding="utf-8") as source:
            lines = [number for number, line in enumerate(source, 1) if literal in line]
        if lines:
            matches[path.relative_to(project).as_posix()] = lines
    return [{"path": path, "lines": lines} for path, lines in matches.items()]


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Exit status: 0 success, 1 invalid or unreadable input, 2 invalid command syntax.",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser(
        "list",
        help="List project and user profiles",
        description=("Print a JSON array with id, title, applies_to, scope and absolute path. "
                     "Warn on stderr and return 1 if any profiles could not be read."),
    )
    listing.add_argument("--project", type=Path, default=Path.cwd(), help="Project root (default: cwd)")
    validate = commands.add_parser(
        "validate", help="Validate a profile", description="Print the validated profile ID as JSON."
    )
    validate.add_argument("profile", type=Path)
    locator = commands.add_parser(
        "locate",
        help="Find a profile's literal in named files",
        description=("Print a JSON array of project-relative paths and 1-based matching lines. "
                     "An empty array means there were no exact matches."),
    )
    locator.add_argument("profile", type=Path)
    locator.add_argument("--project", type=Path, required=True, help="Project root")
    locator.add_argument("files", type=Path, nargs="+", metavar="FILE", help="UTF-8 source files")
    args = parser.parse_args()

    try:
        if args.command in ("list", "locate"):
            project = args.project.resolve()
            if not project.is_dir():
                raise ValueError("expected a project directory")
        if args.command == "list":
            result, status = list_profiles(project)
            print(json.dumps(result, indent=2))
            return status
        profile = read_profile(args.profile)
        if args.command == "validate":
            result = {"id": args.profile.stem}
        else:
            if "literal" not in profile:
                raise ValueError("profile has no 'literal' to locate")
            result = locate(project, args.files, profile["literal"])
    except (OSError, RuntimeError, ValueError) as error:
        subject = args.project if args.command == "list" else args.profile
        print(f"{subject}: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
