# skills

Agent skills for [Claude Code](https://claude.com/claude-code) and [Codex](https://developers.openai.com/codex/skills).

| Skill | What it does |
|---|---|
| [orchestration-mode](orchestration-mode/SKILL.md) | Hands implementation work to background subagents so the main session stays free for discussion and new requests. It turns on only when you ask for orchestration, coordinator or dispatcher mode. |
| [resolve-issues](resolve-issues/SKILL.md) | Works through a repository's open GitHub issues and PR feedback, including inline review threads, PR and issue comments, and reviews that aren't stale. It ranks the work, then checks and resolves each item in turn. |
| [slop-lop](slop-lop/SKILL.md) | Finds and fixes generic copy, design choices that get in the way, and unnecessary code. Keeps familiar patterns that serve the task. |
| [target-lock](target-lock/SKILL.md) | Turns a screenshot or annotation into a reusable slop-lop check and replays it against the example. |

## Install

Clone the repo and link the skills you want into your personal skills folder:

```bash
git clone https://github.com/pbroom/skills.git ~/pbroom-skills
```

```bash
ln -s ~/pbroom-skills/orchestration-mode ~/pbroom-skills/resolve-issues ~/.claude/skills/
```

To use a skill in a single project, copy its folder into that project's `.claude/skills/` instead.

## Teach slop-lop a check

Install `slop-lop` and `target-lock` together in your Codex skills directory.

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s ~/pbroom-skills/slop-lop ~/pbroom-skills/target-lock "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Attach a screenshot, add a browser comment, or paste an example. In Codex, say `$target-lock Save this as a check for this project.` Include what bothered you and where it happened if the example leaves either unclear. Use `$slop-lop` on later reviews to replay matching [saved checks](slop-lop/references/profiles.md).

## License

[MIT](LICENSE)
