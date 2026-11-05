# 04 · Exercises

Do these in order. Each ends with a ✅ **Checkpoint**. Stuck for more than
5 minutes? Raise your hand. That's what the mentors are for.

In the commands, replace `YOU` with your GitHub username and `yourname` with
your first name, for example `giulia`.

| # | Exercise | You learn |
|---|----------|-----------|
| 1 | Fork, clone, connect | fork, clone, remotes |
| 2 | Protect `main` and try to break the rule | branch protection |
| 3 | Don't commit the wrong files | `.gitignore` |
| 4 | Your first pull request | branch → commit → push → PR → review |
| 5 | Fix a merge conflict | conflicts, `git pull upstream main` |
| 6 | Two features, two branches | **one branch per feature**, switching branches |
| 7 | Rebase your branch | `git rebase`, conflicts during a rebase, `--force-with-lease` |
| 8 | Fix a real bug or add a function | the full workflow on real code |

---

## Exercise 1 · Fork, clone, connect

1. Open <https://github.com/H2politO/git-workshop> and click **Fork** → **Create fork**.
2. Clone **your fork** (SSH URL!) and add the team repo as `upstream`:

   ```bash
   cd ~/projects
   git clone git@github.com:YOU/git-workshop.git
   cd git-workshop
   git remote add upstream git@github.com:H2politO/git-workshop.git
   ```

3. Run the program:

   ```bash
   python3 -m ecotrack data/sample_laps.csv
   ```

✅ **Checkpoint:** `git remote -v` shows `origin` (your fork) **and** `upstream`
(H2politO), and the program prints a lap summary.

---

## Exercise 2 · Protect `main` and try to break the rule

1. On **your fork** on GitHub: **Settings → Rules → Rulesets → New branch ruleset**
   - Name: `protect-main` · Enforcement: **Active**
   - Target branches: **Add target → Include default branch**
   - ☑ Restrict deletions · ☑ Require a pull request before merging · ☑ Block force pushes
   - Click **Create**
2. Now do the **wrong** thing on purpose. Commit straight on `main` and push:

   ```bash
   git switch main
   echo "oops" >> README.md
   git commit -am "Commit on main by mistake"
   git push origin main
   ```

   You get `push declined due to repository rule violations`. 🎉 The protection works!

3. Undo your mistake. Put your `main` back exactly as it is on GitHub:

   ```bash
   git reset --hard origin/main
   ```

   > ⚠️ `reset --hard` throws away commits and changes. That's what we want here,
   > but use it carefully.

✅ **Checkpoint:** `git status` says *"nothing to commit, working tree clean"*,
and you can explain in one sentence why the push was refused.

---

## Exercise 3 · Don't commit the wrong files

Do the **[mini exercise in the .gitignore guide](gitignore-guide.md#-mini-exercise-5-min)** (5 min).

✅ **Checkpoint:** you can explain what `.gitignore` is for, and your global ignore
file is set up.

---

## Exercise 4 · Your first pull request

Add your name to [`CONTRIBUTORS.md`](../CONTRIBUTORS.md).

1. Update `main` and create a branch:

   ```bash
   git switch main
   git pull upstream main
   git switch -c yourname/add-contributor
   ```

2. Open `CONTRIBUTORS.md` in your editor and add **one line at the end** of the list:

   ```markdown
   - Name Surname (@your-github-username) — Your division
   ```

3. Commit and push:

   ```bash
   git status
   git diff
   git add CONTRIBUTORS.md
   git commit -m "Add Name Surname to contributors"
   git push -u origin yourname/add-contributor
   ```

4. On GitHub, click **Compare & pull request**. Check that the base is
   **`H2politO/git-workshop` · `main`**, then **Create pull request**.
5. **Review a neighbour:** open someone else's PR → **Files changed** → click the
   `+` next to a line → leave a friendly comment.

✅ **Checkpoint:** your PR is open, the check is green ✅, and you left a comment
on someone else's PR.

---

## Exercise 5 · Fix a merge conflict

Everyone added a line at the **end** of the same file. As soon as the first PRs
are merged, the others show *"This branch has conflicts that must be resolved"*.
**That's on purpose:** everyone gets to fix one.

1. On your branch, pull the latest `main`:

   ```bash
   git switch yourname/add-contributor
   git pull upstream main
   ```

   ```
   CONFLICT (content): Merge conflict in CONTRIBUTORS.md
   Automatic merge failed; fix conflicts and then commit the result.
   ```

2. Open `CONTRIBUTORS.md`. Git has marked the clash:

   ```markdown
   - Can Özaydın (@...) — Autonomous Driving
   <<<<<<< HEAD
   - Marco Bianchi (@marcob) — Autonomous Driving
   =======
   - Giulia Rossi (@giuliar) — Vehicle Dynamics
   >>>>>>> 3f2a1b9...
   ```

   - Between `<<<<<<<` and `=======` is **your** version.
   - Between `=======` and `>>>>>>>` is what's on `main` now.

3. We want **both** names. Delete the three marker lines, keep both names, and save:

   ```markdown
   - Can Özaydın (@...) — Autonomous Driving
   - Giulia Rossi (@giuliar) — Vehicle Dynamics
   - Marco Bianchi (@marcob) — Autonomous Driving
   ```

   > 💡 **VS Code** shows buttons above the conflict. **Accept Both Changes**
   > does exactly this.

4. Finish the merge and update the PR:

   ```bash
   git add CONTRIBUTORS.md
   git commit -m "Merge main and fix conflict"
   git push
   ```

   Panicking? `git merge --abort` puts everything back to how it was before the pull.

**No conflict?** Lucky you, your PR was merged first. Help your neighbour with
theirs, which counts too!

✅ **Checkpoint:** your name is on `main` in `CONTRIBUTORS.md`.

---

## Exercise 6 · Two features, two branches

The most important habit: **every feature gets its own branch**. You'll build two
small, unrelated features at the same time and see that they never mix.

- **Feature A:** your own lap data file, `data/laps_yourname.csv`
- **Feature B:** your team profile, `team/yourname.md`

### Feature A, on its own branch

```bash
git switch main
git pull upstream main
git switch -c yourname/lap-data
```

Copy the sample file and change some of the times (invent them!):

```bash
cp data/sample_laps.csv data/laps_yourname.csv
# edit data/laps_yourname.csv in your editor
python3 -m ecotrack data/laps_yourname.csv     # does it work?
git add data/laps_yourname.csv
git commit -m "Add lap data for yourname"
```

### Feature B, on a different branch

Start from **`main`**, not from feature A:

```bash
git switch main
ls data/                       # 👀 laps_yourname.csv is NOT here. It lives only on yourname/lap-data
git switch -c yourname/profile
cp team/_template.md team/yourname.md
# fill in team/yourname.md
git add team/yourname.md
git commit -m "Add team profile for yourname"
```

### Look at what you built

```bash
git log --oneline --graph --all     # two branches, side by side
git switch yourname/lap-data && ls data/ team/
git switch yourname/profile  && ls data/ team/
```

Each branch only has **its own** feature.

### Two PRs

```bash
git switch yourname/lap-data && git push -u origin yourname/lap-data
git switch yourname/profile  && git push -u origin yourname/profile
```

Open **two separate pull requests** on GitHub. They can be reviewed and merged
independently: if the reviewer asks for changes to your profile, your lap data
can still be merged right away.

**Reviewer asked for a change?** Switch to *that* branch, fix, commit, push:

```bash
git switch yourname/profile
# ...edit...
git commit -am "Fix typo in profile"
git push
```

✅ **Checkpoint:** you have two PRs, each with **one** feature, and you can show
a mentor that switching branches changes which files you see.

---

## Exercise 7 · Rebase your branch

Read the **[rebase guide](rebase-guide.md)** first (10 min). Then practise in
three parts. Everything here stays on your fork, and no PR is needed.

### Part A · Catch up with `main`

Pretend you started a branch a while ago: create it from an **old** point of
`main` (3 commits back), and make one commit.

```bash
git fetch upstream
git switch -c yourname/rebase-practice upstream/main~3
echo "rebase practice" > practice-yourname.txt
git add practice-yourname.txt
git commit -m "Add rebase practice file"
git push -u origin yourname/rebase-practice
```

Look at the picture: your branch goes off to the side, and `main` has moved on.

```bash
git log --oneline --graph yourname/rebase-practice upstream/main
```

Write down the ID of your commit (`git log --oneline -1`), then rebase:

```bash
git rebase upstream/main
git log --oneline --graph yourname/rebase-practice upstream/main
git log --oneline -1
```

Your commit now sits **on top of** `main` in a straight line, and it has a **new ID**.

### Part B · Push a rebased branch

```bash
git push
```

Refused (`non-fast-forward`)! GitHub still has your *old* commit. Replace it:

```bash
git push --force-with-lease
```

### Part C · A conflict during a rebase

Make two branches that change the **same line**:

```bash
git switch -c drill-a upstream/main
# edit the FIRST line of README.md to:  # Drill A
git commit -am "Drill A title"

git switch -c drill-b upstream/main
# edit the FIRST line of README.md to:  # Drill B
git commit -am "Drill B title"

git rebase drill-a        # 💥 CONFLICT in README.md
```

Open `README.md`. Remember: **top = the branch you rebase onto (drill-a)**,
**bottom = your commit (drill-b)**. Keep one title, delete the marker lines, save, then:

```bash
git add README.md
git rebase --continue     # not "git commit"!
git log --oneline -3      # Drill B now sits on top of Drill A
```

(Want to start over? `git rebase --abort`.)

### Clean up

```bash
git switch main
git branch -D yourname/rebase-practice drill-a drill-b
git push origin --delete yourname/rebase-practice
```

**Bonus:** make 3 small commits on a new branch (`Add x`, `fix typo`, `oops`),
then squash them into one with `git rebase -i upstream/main`
(see [section 5 of the guide](rebase-guide.md#5--tidy-up-your-commits-interactive-rebase)).

✅ **Checkpoint:** you can explain what rebase does, why the commit ID changed,
why the push needed `--force-with-lease`, and why you never rebase `main`.

> From now on, you can update any of **your** branches either way:
> `git pull upstream main` (merge) or `git fetch upstream && git rebase upstream/main` (rebase).

---

## Exercise 8 · Fix a real bug or add a function

Pick a task from **[05-tasks.md](05-tasks.md)**. Find its issue on GitHub and comment
*"I'll take this"*. **T1** (the lap time bug) is a great first one.

Same loop as before, now with real code:

```bash
git switch main
git pull upstream main
git switch -c yourname/fix-lap-format
# ...edit the code...
python3 -m ecotrack data/sample_laps.csv     # check that it works
git add ecotrack/laps.py
git commit -m "Fix zero padding in format_lap_time"
git push -u origin yourname/fix-lap-format
```

In the PR description write `Closes #<issue number>`.

Done? Clean up, then pick another task on a **new** branch:

```bash
git switch main
git pull upstream main
git branch -D yourname/fix-lap-format     # delete branches that were merged
```

✅ **Checkpoint:** a PR of yours that changes Python code is merged, and its issue is closed.

---

## Bonus (if you finish early)

- **Explore the history:** `git log --oneline`, `git show <commit-id>`, and
  `git blame ecotrack/laps.py`. Who wrote `format_lap_time`, and in which commit?
- **Undo a merged change safely:** on a new branch, `git revert <commit-id>`, then open a PR.
- **Park unfinished work:** `git stash` saves your changes so you can switch
  branches. `git stash pop` brings them back.
- **Add a test:** most tasks can have a test in `tests/`. Look at the existing
  ones and copy the style.
