# Facilitator guide

How to set up and run the workshop. Participants don't need this page.

## 1 · Create the upstream repository (a few days before)

1. In the **H2politO** GitHub organization, create an **empty, public** repo
   called `git-workshop` (no README, no license, no .gitignore).
   - It needs to be public: on GitHub **Free** organizations, branch protection
     is only enforced on public repos.
2. If the org or repo name is **not** `H2politO/git-workshop`, replace it everywhere:

   ```bash
   # macOS (BSD sed). On Linux, drop the '' after -i
   grep -rl "H2politO/git-workshop" . --exclude-dir=.git | xargs sed -i '' 's#H2politO/git-workshop#ORG/REPO#g'
   ```

3. Put your GitHub handle in `CONTRIBUTORS.md` (replace `@CHANGE-ME`).
4. Push:

   ```bash
   git remote add origin git@github.com:H2politO/git-workshop.git
   git push -u origin main
   ```

5. Open the **Actions** tab and wait for the first **CI** run to go green. It
   must have run once before you can select the `test` check in step 2.3.

## 2 · Configure the repository

### 2.1 Settings → General → Pull Requests

- ☐ Allow merge commits
- ☑ **Allow squash merging** (default message: *Pull request title*)
- ☐ Allow rebase merging
- ☑ Always suggest updating pull request branches
- ☑ **Automatically delete head branches**

### 2.2 Collaborators / teams

**Approvals only count from people with *write* access.** Give mentors (the
experienced members) **Write** access via **Settings → Collaborators and teams**.
Participants don't need any access, because they work from forks.

### 2.3 Settings → Rules → Rulesets → New branch ruleset

| Setting | Value |
|---------|-------|
| Name | `protect-main` |
| Enforcement | Active |
| Bypass list | empty (or org admins only, for emergencies) |
| Target | Include default branch |
| ☑ Restrict deletions | |
| ☑ Require linear history | works because PRs are squash-merged |
| ☑ Require a pull request before merging | 1 approval |
| ☑ Require status checks to pass | add **`test`** (GitHub Actions) |
| ☐ Require branches to be up to date | leave **off**: with 20 people merging, everyone would have to update after every merge |
| ☑ Block force pushes | |

### 2.4 Settings → Actions → General

Under **"Approval for running fork pull request workflows from contributors"**,
GitHub may hold CI on PRs from first-time contributors until someone with write access
clicks **Approve and run** on the PR. Choose the least strict option and expect to
approve runs for brand-new accounts by hand during Exercise 4.

### 2.5 Issues

Create one issue per task in `docs/05-tasks.md`:

```bash
gh auth login
python3 scripts/create_issues.py --repo H2politO/git-workshop --dry-run
python3 scripts/create_issues.py --repo H2politO/git-workshop
```

## 3 · Before the day

- Send participants **[00-prerequisites.md](00-prerequisites.md)** at least 3 days before.
- Ask people to come 15 min early if `ssh -T git@github.com` doesn't work yet.
- Plan for **1 mentor per ~5 participants**.
- Check the room's Wi-Fi: if port 22 is blocked, everyone needs the
  `ssh.github.com:443` config from the prerequisites.

## 4 · Running it

| Block | Notes |
|-------|-------|
| Setup check | Everyone runs `ssh -T git@github.com` and the program. Mentors fix stragglers |
| Git basics | Live-demo the playground from 01 on the projector. Run `git status` after **every** command. Spend most of the time on the **two branches** demo |
| .gitignore | Show `git status` with a `.env` and `.vscode/` in the folder, then with the ignore file |
| Trunk-based | Tell the "merge hell" story. Keep it short |
| GitHub workflow | Live: fork → clone → `remote add upstream` → branch → push → open a PR |
| Ex. 1–3 | Common problems: HTTPS clone, PR opened against the fork instead of upstream |
| Ex. 4–5 | **Merge CONTRIBUTORS PRs in waves** (merge 3, pause, merge 3…), so most people hit a real conflict in Ex. 5 |
| Ex. 6 | Check that the two PRs are **separate** and each contains one file. A PR with both files means the second branch was created from the first instead of from `main`. Good teaching moment |
| Rebase talk | Draw the before/after picture on the whiteboard. Hammer two points: commit IDs change, and **never rebase `main`**. Live-demo a rebase conflict and point out that top/bottom are flipped compared with a merge |
| Ex. 7 | Needs `upstream/main~3` to exist, which is guaranteed by the repo's own history. Common problems: typing `git commit` instead of `git rebase --continue`, `--force` instead of `--force-with-lease`, landing in vim during `rebase -i` |
| Ex. 8 | Mentors review. Push back (kindly) on PRs that do two things: "split it into two branches" |
| Wrap-up | Show `git log --oneline` on upstream: a clean history built by the whole room |

## 5 · Common problems

| Symptom | Fix |
|---------|-----|
| `Permission denied (publickey)` | Key not on GitHub or not loaded: `ssh-add ~/.ssh/id_ed25519`, recheck Settings → SSH keys |
| `Connection timed out` on port 22 | Use `ssh.github.com` port 443 (see prerequisites) |
| Asked for username/password on push | Cloned with HTTPS → `git remote set-url origin git@github.com:YOU/git-workshop.git` |
| `remote: Permission to H2politO/... denied` | Pushing to `upstream`. Push to `origin` (their fork) |
| `fatal: Need to specify how to reconcile divergent branches` | Missing config: `git config --global pull.rebase false` |
| PR contains commits/files from another feature | Branch was created from another branch. Recreate it from `main` and copy the file over |
| PR targets their own fork | Change the base repository to `H2politO/git-workshop` |
| CI never starts on the PR | First-time contributor: click **Approve and run** |
| `git switch` refuses: "changes would be overwritten" | Uncommitted work: commit it (or `git stash`) first |
| `git branch -d` says "not fully merged" | Expected after a squash merge: use `-D` |
| Push rejected `non-fast-forward` after a rebase | Expected: `git push --force-with-lease` |
| "You are currently rebasing" and they're lost | `git status` explains where they are; `git rebase --abort` resets to safety |
| A rebase went wrong after it finished | `git reset --hard ORIG_HEAD`, or find the old commit with `git reflog` |
| Stuck in vim | `Esc` `:wq` `Enter`, then set `core.editor` |
| `python3: command not found` (Windows) | Use `python` instead |

## 6 · After the workshop

- Leave the repo up as onboarding material for new members.
- Before the first push, tag the starting point so you can reuse it next year:
  `git tag workshop-start && git push --tags`.
