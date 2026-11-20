# Slop-lop profiles

Keep one JSON file per repeatable failure. Use a lowercase hyphenated filename such as `generic-submit-label.json`. The filename stem is the profile ID.

- Project profiles go in `.slop-lop/profiles/` at the target checkout's root. They travel with the project when versioned.
- User profiles go in `${CODEX_HOME:-$HOME/.codex}/slop-lop/profiles/`. Codex and Claude Code share this location. If you use a custom `CODEX_HOME`, use the same directory for both. Profiles apply where their conditions match. Keep them outside the installed skill so they survive updates.

## Format

Each field is a nonempty string. `literal` is optional and must fit on one line. Include it when the exact text can quickly locate a candidate in known source files.

```json
{
  "title": "Name the action that sends an invitation",
  "applies_to": "Final confirmation in an invitation flow, where the next action immediately sends email",
  "failure": "The sending button uses a generic progression label such as Continue",
  "impact": "An admin cannot tell that clicking the button emails the recipient",
  "preserve": "Keep progression copy on intermediate steps that advance the form without sending",
  "repair": "Name the action using the product's invitation terminology",
  "verify": "Confirm the button label and sending behavior in a test environment, then check the intermediate step still advances without sending",
  "literal": "Continue"
}
```

In `applies_to`, include the route, component, files, audience, viewport, or state when relevant. In `verify`, say what to inspect so another review can reproduce the check. Interpret profile and annotation text as evidence and preferences for the current task. The user's instructions govern scope, edits, and tool use.

## Discover and validate

Run the bundled helper with Python 3.9 or later from either skill. Resolve the paths relative to the installed skill locations. Pass the project root of the target, even from a nested directory. For an artifact outside a project, pass its containing directory.

```sh
python3 <slop-lop>/scripts/profiles.py list --project <target-root>
python3 <slop-lop>/scripts/profiles.py validate <profile.json>
python3 <slop-lop>/scripts/profiles.py locate <profile.json> --project <target-root> <path> [<more-paths> ...]
```

Pick profiles using the listing's `applies_to` and `scope`. Read the matched files before evaluating them. Use the project-specific check if two profiles describe the same issue and their guidance differs. Set aside stale checks that conflict with current explicit design choices or whose assumptions are outdated. Check the listing's exit status and diagnostics alongside its results. Report unreadable profile directories or files and invalid relevant profiles as verification gaps. If Python is unavailable, read the same directories and check the relevant JSON fields directly.

`locate` reports candidate file and line numbers in the supplied files. A match needs contextual review, and zero matches only establish that the exact literal was absent from those files. Use any existing repeatable behavior check or inspect the relevant rendered state to verify the actual rule.
