# 05 · Tasks ("good first issues")

Small tasks for [Exercise 8](04-exercises.md#exercise-8--fix-a-real-bug-or-add-a-function).
**One task = one branch = one pull request.** Each task has an issue on GitHub.
Comment *"I'll take this"* first, so two people don't do the same one.

🟢 easy · 🟡 a little harder

You don't have to write tests, but if you want to, look at the files in `tests/`
and copy their style.

---

### T1 🟢 Fix the lap time formatting bug

`python3 -m ecotrack data/sample_laps.csv` prints `Best lap: 4:2.71`. It should be
`4:02.71`. The comment in `format_lap_time` in `ecotrack/laps.py` shows the
correct output.

*Hint:* in Python, `f"{x:05.2f}"` pads a number with zeros to 5 characters.

### T2 🟢 Add a `slowest_lap` function

Add `slowest_lap(lap_times)` to `ecotrack/laps.py`. It works like `best_lap`
but returns the **largest** time.

### T3 🟢 Show the number of laps

Make the program print an extra first line: `Laps:         8`.
The file to change is `ecotrack/cli.py`. *Hint:* `len(lap_times)`.

### T4 🟡 Show the slowest lap

Print `Slowest lap:  4:11.84` in the summary. This needs **T2** to be merged first.
When it is, update your branch to get it, with `git pull upstream main` or,
even better, `git fetch upstream && git rebase upstream/main`.
(Waiting for someone else's work is normal in a team!)

### T5 🟢 Don't crash on zero energy

`efficiency_km_per_kwh(10, 0)` in `ecotrack/telemetry.py` crashes with a
confusing `ZeroDivisionError`. Make it raise
`ValueError("energy_kwh must be positive")` instead, like `average_speed_kmh` does.

### T6 🟢 Add a speed conversion helper

Add `kmh_to_ms(speed_kmh)` to `ecotrack/telemetry.py`. It converts km/h to m/s
(divide by 3.6).

### T7 🟢 Add a `median_lap` function

Add `median_lap(lap_times)` to `ecotrack/laps.py`. *Hint:* the `statistics`
module has a `median` function.

### T8 🟢 Ignore log files

`python3 -m ecotrack data/sample_laps.csv > run.log` creates a file that shows up
in `git status`. Add the right pattern to the project's `.gitignore`
(see [the .gitignore guide](gitignore-guide.md)). Check it with `git check-ignore -v run.log`.

### T9 🟢 Improve the docs

Found something confusing in these guides? Fix it! Typos, clearer wording, or a
missing step for your OS. Documentation PRs are real contributions.

---

**Finished a task?** Pick another one on a **new branch**, or review someone else's PR. 👀
