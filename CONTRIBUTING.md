# Contributing

The rules are the same ones we use for the real car software.

1. **`main` must always work.** Nobody pushes to it directly, because it is
   protected on GitHub.
2. **One branch per feature or fix.** Two different things go on two different
   branches and become two pull requests.
3. **Small and short-lived.** A branch should be merged within a day or two,
   then deleted.
4. **Every change goes through a pull request (PR).** Another person reviews
   it, and the automatic tests must be green ✅.
5. **Stay up to date.** Before starting a branch, update `main`. If `main`
   changes while you work, bring it into your branch, either with
   `git pull upstream main` or by rebasing
   (`git fetch upstream && git rebase upstream/main && git push --force-with-lease`).
   Only ever rebase **your own** branches, never `main`.

## Branch names

```
yourname/short-description
```

Examples: `giulia/fix-lap-format`, `marco/add-slowest-lap`

## Commit messages

Start with a verb ("Add", "Fix", "Update"), keep it short, and say what changed:

- ✅ `Fix zero padding in format_lap_time`
- ✅ `Add slowest_lap function`
- ❌ `fix`, `changes`, `asdfgh`, `final version 2 REAL`

## The everyday loop

```bash
git switch main
git pull upstream main                    # 1. get the latest main
git switch -c yourname/short-description  # 2. new branch for ONE thing
# ...edit, then:
git add <files>
git commit -m "Add something"             # 3. commit
git push -u origin yourname/short-description   # 4. push, then open a PR on GitHub
```

PRs are merged with **"Squash and merge"**, so each PR becomes one tidy commit on `main`.
