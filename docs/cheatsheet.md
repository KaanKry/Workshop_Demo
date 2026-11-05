# Git cheatsheet

## Setup (once per computer)

```bash
git config --global user.name "Name Surname"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
ssh-keygen -t ed25519 -C "you@example.com"     # then add ~/.ssh/id_ed25519.pub to GitHub
ssh -T git@github.com                          # test: "Hi username!"
```

## Setup (once per fork)

```bash
git clone git@github.com:YOU/REPO.git
cd REPO
git remote add upstream git@github.com:OWNER/REPO.git
```

## The everyday loop 🔁 (one branch per feature)

```bash
git switch main
git pull upstream main                     # 1. get the latest main
git switch -c yourname/short-desc          # 2. new branch for ONE feature
# ...edit...
git status                                 # 3. what changed?
git diff
git add <file>                             # 4. stage
git commit -m "Add something"              # 5. commit
git push -u origin yourname/short-desc     # 6. push to your fork
# 7. open a PR on GitHub → review → merge
git switch main                            # 8. clean up when merged
git pull upstream main
git branch -D yourname/short-desc
```

## Branches

| Command | What it does |
|---------|--------------|
| `git branch` | list your branches (`*` = current) |
| `git switch -c <name>` | create a new branch and move onto it |
| `git switch <name>` | move to an existing branch |
| `git log --oneline --graph --all` | draw all branches |
| `git branch -D <name>` | delete a branch |

## Update my branch with the latest `main`

```bash
git pull upstream main
git push
```

## Conflicts

```bash
git status                     # which files conflict
# open the file, keep what you want, delete the <<<<<<< ======= >>>>>>> lines
git add <file>
git commit -m "Merge main and fix conflict"
git push
# or give up and go back: git merge --abort
```

## Looking around

| Command | Shows |
|---------|-------|
| `git status` | current branch and changed files. Use it all the time! |
| `git diff` | changes not staged yet |
| `git log --oneline` | history |
| `git show <id>` | one commit in detail |
| `git remote -v` | remotes (`origin`, `upstream`) |

## Undo

| Situation | Command |
|-----------|---------|
| Throw away changes to a file | `git restore <file>` |
| Unstage a file | `git restore --staged <file>` |
| Fix last commit message (not pushed) | `git commit --amend -m "New message"` |
| Committed on `main` by mistake | `git reset --hard origin/main` (⚠️ throws the commit away) |
| Undo a commit that's already on `main` | `git revert <id>` (on a branch, then PR) |
| Park work to switch branches | `git stash` … `git stash pop` |

## Ignoring files ([full guide](gitignore-guide.md))

| Command | Shows / does |
|---------|--------------|
| `git status --ignored` | also list ignored files |
| `git check-ignore -v <file>` | which rule ignores the file |
| `git rm --cached <file>` | stop tracking a file you committed by mistake (keeps it on disk) |
| `~/.config/git/ignore` | your personal ignore file for editor and OS junk |

## Words

| Word | Meaning |
|------|---------|
| **repository** | a project folder tracked by git |
| **commit** | a saved snapshot with a message |
| **branch** | a separate line of work, one per feature |
| **main** | the shared branch that must always work (the "trunk") |
| **remote** | a copy of the repo on GitHub (`origin` = your fork, `upstream` = the team's) |
| **fork** | your own copy of someone's repo on GitHub |
| **clone** | download a repo to your computer |
| **pull request (PR)** | a request to merge your branch, with review and tests |
| **merge conflict** | two people changed the same lines; you decide what to keep |
