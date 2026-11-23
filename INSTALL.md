# Installing the Zluri design system

The same repository works three ways. Pick one — they do not conflict.

| Way | Who it is for | What to do |
| --- | --- | --- |
| **Skill for CLI agents** (Claude Code, Codex, Gemini CLI, Cursor, Copilot, OpenCode, …) | People who design with a terminal agent | Install once (below), then type **`/zluri-design-system`** (Claude Code) or `$zluri-design-system` / pick it from `/skills` (Codex) — or just ask for anything Zluri-branded. |
| **Open Design** | People using Open Design | Design System → **GitHub import** → paste `https://github.com/sk-zluri/zluri-brand-design` → pick **Zluri**. No install needed. |
| **Repo link only** | Any agent, one-off | Share the link and say "read `AGENTS.md` first". Nothing is installed. |

---

## For AI agents: when a user gives you this repo link

If the user shares `https://github.com/sk-zluri/zluri-brand-design` (or a clone of it) and you are a CLI coding agent:

1. **Check whether it is already installed** as a skill named `zluri-design-system` (look in `~/.agents/skills/`, `~/.claude/skills/`, `~/.codex/skills/`, or your own skills list). If it is, use it and skip to step 4.
2. **Ask the user once, before doing anything else**, with these options:
   > "This is the Zluri design system. Do you want me to install it as a skill so it is available as `/zluri-design-system` in all your AI agents (Claude Code, Codex, Gemini CLI, Cursor…)?
   > 1. **Yes — install globally for all my agents** (recommended)
   > 2. Yes — only for this project
   > 3. No — just use it from the link for this task"
3. Install according to the answer (commands below), then tell the user where it went and how to invoke it. Restart is sometimes needed for the agent to see a new skill — say so.
4. Carry on with the user's actual request using `AGENTS.md`.

Never install without asking. If the user is in Open Design, do not offer a skill install — Open Design imports the repo itself.

---

## Install commands

Requires Node.js 18+ and git.

### All agents at once (recommended) — the `skills` CLI

```bash
# global: every agent on this machine (Claude Code, Codex, Gemini CLI, Cursor, …)
npx -y skills add sk-zluri/zluri-brand-design -g -y

# project only: into the current project's agent folders
npx -y skills add sk-zluri/zluri-brand-design -y
```

The CLI copies the repo to `~/.agents/skills/zluri-design-system/` and links it into each detected agent's skills folder (for example `~/.claude/skills/zluri-design-system`). To target specific agents add `-a claude-code -a codex`. Update later with `npx skills update`; remove with `npx skills remove zluri-design-system -g`.

### Manual (no Node) — git clone

```bash
# Claude Code
git clone --depth 1 https://github.com/sk-zluri/zluri-brand-design ~/.claude/skills/zluri-design-system
# Codex CLI and other agents that read ~/.agents/skills
git clone --depth 1 https://github.com/sk-zluri/zluri-brand-design ~/.agents/skills/zluri-design-system
```

Windows PowerShell: replace `~` with `$HOME`. Update with `git pull` inside the folder.

### Check it worked

- Claude Code: type `/zluri-design-system` — it should autocomplete.
- Codex: run `/skills` and look for `zluri-design-system`.
- Or ask the agent: "Which skills do you have for Zluri?"

## Optional: employee-photo tools

Only needed for people posts with supplied photos (`guidelines/13-employee-photos.md`):

```bash
pip install -r tools/people/requirements.txt     # run inside the installed skill folder
```

The first cut-out downloads the `birefnet-portrait` model (~1 GB) to `~/.u2net` / `~/.rembg`.
