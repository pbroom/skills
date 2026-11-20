# skills

Agent skills for [Claude Code](https://claude.com/claude-code).

| Skill | What it does |
|---|---|
| [orchestration-mode](orchestration-mode/SKILL.md) | Hands implementation work to background subagents so the main session stays free for discussion and new requests. It turns on only when you ask for orchestration, coordinator or dispatcher mode. |
| [resolve-issues](resolve-issues/SKILL.md) | Works through a repository's open GitHub issues and PR feedback, including inline review threads, PR and issue comments, and reviews that aren't stale. It ranks the work, then checks and resolves each item in turn. |
| [slop-lop](slop-lop/SKILL.md) | Finds and fixes generic copy, design choices that get in the way, and unnecessary code. Keeps familiar patterns that serve the task. |

## Install

Clone the repo and link the skills you want into your personal skills folder:

```bash
git clone https://github.com/pbroom/skills.git ~/pbroom-skills
```

```bash
ln -s ~/pbroom-skills/orchestration-mode ~/pbroom-skills/resolve-issues ~/.claude/skills/
```

To use a skill in a single project, copy its folder into that project's `.claude/skills/` instead.

## License

[MIT](LICENSE)
