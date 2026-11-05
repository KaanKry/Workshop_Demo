# .gitignore guide: don't push the wrong files

Your editor, operating system, Python and ROS all create files you **never**
want in a shared repository. If you commit them, you get:

- 🔐 **leaked secrets**: an API key or Wi-Fi password in `.env` stays in the git history *forever*
- 🐘 **huge repos**: a committed `.venv/` (50 MB) or a rosbag (2 GB) slows every clone, for everyone
- 💥 **pointless conflicts**: your `.vscode/settings.json` fights with your teammate's
- 🗑️ **noise in PRs**: `__pycache__/`, `.DS_Store` and `build/` hide the real changes

`.gitignore` tells git: *"pretend these files don't exist"*.

---

## 1 · What should never be committed

| Category | Examples | Why |
|----------|----------|-----|
| **Secrets** | `.env`, `*.pem`, `id_ed25519`, `credentials.json`, `secrets.yaml` | Anyone who can read the repo (or ever could) can use them |
| **Virtual environments** | `.venv/`, `venv/`, `env/`, `.conda/` | Huge, machine-specific, and can be rebuilt with `pip install` |
| **Generated / compiled files** | `__pycache__/`, `*.pyc`, `*.egg-info/`, `build/`, `dist/`, `*.o`, `*.so` | Rebuilt automatically from the source |
| **Tool caches** | `.pytest_cache/`, `.ruff_cache/`, `.mypy_cache/`, `.coverage` | Local only |
| **Editor / IDE settings** | `.vscode/`, `.idea/`, `*.swp`, `*~` | Personal preferences, different on every machine |
| **OS junk** | `.DS_Store` (macOS), `Thumbs.db`, `desktop.ini` (Windows) | Created by your file browser |
| **Big data & logs** | `*.bag`, `*.db3`, `*.mcap`, `*.log`, `*.csv` dumps, videos | Too big for git. Share them on the team drive instead |
| **ROS 2 workspace output** | `build/`, `install/`, `log/` | Produced by `colcon build` |

> 💡 Rule of thumb: **if a file can be regenerated, or if it's personal, or if
> it's secret, it doesn't belong in git.**

---

## 2 · How `.gitignore` patterns work

`.gitignore` is a plain text file at the root of the repo, with one pattern per line.
Have a look at this repo's [`.gitignore`](../.gitignore).

| Pattern | Ignores |
|---------|---------|
| `# text` | nothing: it's a comment |
| `.env` | any file or folder called `.env`, in any folder |
| `*.log` | every file ending in `.log` |
| `build/` | every **folder** called `build` (the trailing `/` means "folders only") |
| `/build/` | only the `build` folder at the **root** of the repo (the leading `/` anchors it) |
| `docs/*.pdf` | PDFs directly inside `docs/` |
| `**/temp` | `temp` at any depth (`a/temp`, `a/b/temp`, ...) |
| `!keep.log` | **un**-ignore: `keep.log` is tracked even though `*.log` is ignored |

⚠️ Two gotchas:

- **`.gitignore` only affects files that are *not yet tracked*.** If you already
  committed a file, adding it to `.gitignore` does nothing. See [section 5](#5--oops-i-already-committed-it).
- **You can't un-ignore a file inside an ignored folder.** `build/` + `!build/keep.txt`
  doesn't work. Use `build/*` + `!build/keep.txt` instead.

---

## 3 · Two kinds of ignore files: project vs. personal

| | **Project** `.gitignore` | **Global** (personal) ignore file |
|---|---|---|
| Where | in the repo, committed | in your home folder, never committed |
| Shared with the team? | ✅ yes | ❌ no, it applies only on your computer, in **every** repo |
| Put here | things **the project** produces: `.venv/`, `__pycache__/`, `build/`, `.env` | things **you** produce: your editor's files, your OS's files |

Why the split? The project shouldn't need to know that *you* use VS Code on a Mac
while your teammate uses PyCharm on Windows. A global ignore file protects you in
**every** repository, including ones whose `.gitignore` forgot about `.DS_Store`.

(This workshop repo lists editor and OS files in its `.gitignore` too, as a safety net for beginners.)

### Set up your global ignore file (do it once, takes 2 minutes)

Git automatically reads `~/.config/git/ignore`. Create it:

```bash
mkdir -p ~/.config/git
touch ~/.config/git/ignore
```

Open it in your editor (for example `code ~/.config/git/ignore`), paste the blocks
for **your** OS and editors from [section 4](#4--editor-and-os-cheat-sheet), and save.

✅ **Check** in a throw-away repo (the workshop repo already ignores `.DS_Store`
itself, so it wouldn't prove anything):

```bash
mkdir ~/ignore-test && cd ~/ignore-test
git init
touch .DS_Store
git status            # .DS_Store should NOT appear as untracked
git check-ignore -v .DS_Store
cd .. && rm -rf ~/ignore-test
```

```
/Users/you/.config/git/ignore:2:.DS_Store	.DS_Store
```

The output tells you **which file and which line** ignored it.

---

## 4 · Editor and OS cheat sheet

Copy the blocks you need into your global ignore file.

### VS Code (and Cursor, VSCodium)

```gitignore
# VS Code
.vscode/*
!.vscode/extensions.json
*.code-workspace
.history/
```

> **Should `.vscode/` be committed?** Mostly **no**: `settings.json` holds personal
> things like font size, theme and local paths. The exception is
> `.vscode/extensions.json`, which only *recommends* extensions (for example Python and Ruff)
> to teammates, so it's fine to share. That's why it's un-ignored above.
> Some teams also share `.vscode/launch.json` for debug configs. Agree on it
> as a team, and never put machine-specific paths in it.

**VS Code habit:** in the **Source Control** panel (Ctrl/Cmd+Shift+G), read the
list of changed files **before** clicking ✓ Commit. If you see `.venv`,
`__pycache__` or `.env` there, **stop** and fix `.gitignore` first. Avoid
"Stage All Changes" until you've read the list.

### JetBrains (PyCharm, CLion, IntelliJ)

```gitignore
# JetBrains
.idea/
*.iml
```

### Vim / Neovim

```gitignore
# Vim
*.swp
*.swo
*~
Session.vim
```

### Emacs

```gitignore
# Emacs
*~
\#*\#
.\#*
```

### Sublime Text

```gitignore
# Sublime Text
*.sublime-workspace
```

### Jupyter notebooks

```gitignore
# Jupyter
.ipynb_checkpoints/
```

### macOS

```gitignore
# macOS
.DS_Store
.AppleDouble
._*
```

### Windows

```gitignore
# Windows
Thumbs.db
desktop.ini
$RECYCLE.BIN/
```

### Linux

```gitignore
# Linux
*~
.directory
.Trash-*
```

### For project `.gitignore` files: Python and ROS 2

These belong in the **repo's** `.gitignore`, not your global one:

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
.pytest_cache/
.ruff_cache/
.mypy_cache/

# Secrets
.env
.env.*
!.env.example

# ROS 2 / colcon workspace
build/
install/
log/

# Recorded data: share on the team drive, not git
*.bag
*.db3
*.mcap
```

> 💡 Don't write these from scratch. GitHub keeps ready-made templates for almost
> every language and tool at <https://github.com/github/gitignore> (`Python.gitignore`,
> `Global/VisualStudioCode.gitignore`, `Global/macOS.gitignore`, ...). When you
> create a new repo on GitHub, the **"Add .gitignore"** dropdown uses these.

> 🔑 **The `.env.example` trick:** commit a `.env.example` with the variable
> *names* and fake values (`API_KEY=changeme`). Teammates copy it to `.env` and
> fill in the real values, and the real `.env` stays ignored.

---

## 5 · Oops, I already committed it

### A file that shouldn't be tracked (not secret)

Example: you committed `.vscode/settings.json` or `__pycache__/`.

```bash
# 1. Add the pattern to .gitignore
echo "__pycache__/" >> .gitignore

# 2. Stop tracking the file but KEEP it on your disk
git rm -r --cached __pycache__/

# 3. Commit both changes (on a branch, then PR as usual)
git add .gitignore
git commit -m "Stop tracking __pycache__"
```

`--cached` is the important part. Without it, git also deletes the file from your disk.

### A secret (password, token, key) 🚨

1. **Rotate the secret immediately**: revoke the key or token and create a new one,
   or change the password. Assume the old one is compromised **the moment it
   was pushed**. Deleting it in a new commit doesn't help, because it's still in the history.
2. Tell the team lead.
3. Remove the file from tracking as above and add it to `.gitignore`.
4. Optionally clean the history (with `git filter-repo`). Ask a mentor, because
   it rewrites history for everyone.

Step 1 is the one that actually protects you.

---

## 6 · Useful commands

| Command | What it does |
|---------|--------------|
| `git status` | Shows untracked files. Read it before every commit! |
| `git status --ignored` | Also lists the files that are being ignored |
| `git check-ignore -v <file>` | Explains **why** a file is ignored (which file, which line) |
| `git ls-files` | Lists everything git is tracking. Look for things that shouldn't be there |
| `git rm --cached <file>` | Stop tracking a file, keep it on disk |
| `git add -p` | Stage changes piece by piece, so you see exactly what goes in |

---

## 🧪 Mini exercise (5 min)

In your clone of the workshop repo:

```bash
# Create some files that should NEVER be committed
echo "API_KEY=super-secret" > .env
mkdir -p .vscode && echo '{"editor.fontSize": 18}' > .vscode/settings.json
touch notes.swp
python3 -m ecotrack data/sample_laps.csv > run.log

git status
```

1. Which of these files does `git status` show? Which are hidden?
2. For each hidden one, run `git check-ignore -v <file>` to see which rule hides it.
3. `run.log` is probably **not** ignored. Add the right pattern to your
   **global** or the **project** ignore file. Which one is correct, and why?
   *(Answer: logs are produced by the project, so they go in the project `.gitignore`.
   That would make a nice small PR!)*
4. Clean up: `rm -rf .env .vscode notes.swp run.log`

✅ **Checkpoint:** `git status` says *"nothing to commit, working tree clean"*
and you can explain the difference between the project and the global ignore file.
