# H2politO Git Workshop 🚗💨

Welcome to Team H2politO! This repository is a **practice playground** where
you'll learn:

- the basics of **git**: commits, history, and **branches** (one branch per feature)
- **how we work as a team** (trunk-based development)
- **GitHub**: forking, protecting `main`, and opening **pull requests**

The code is a tiny Python program called `ecotrack` that prints lap statistics
for our Shell Eco-marathon car. It is very simple, and it has a few small bugs
and missing features for you to work on. **You can't break anything here**, so
experiment freely.

> **First time with git?** Perfect, so is almost everyone in the room. Follow the
> guides in order and ask a mentor whenever you get stuck.

---

## 📋 Before the workshop (at home, ~30 min)

Complete **[docs/00-prerequisites.md](docs/00-prerequisites.md)**:

1. Install git and Python
2. Create a GitHub account
3. Configure git, and set up a global ignore file for your editor's junk files
4. Create an **SSH key** and add it to GitHub
5. **Clone** this repository and run the program

Stuck? Come 15 minutes early and we'll fix it together.

## 🗺️ Workshop agenda

| Time   | Topic | Material |
|--------|-------|----------|
| 15 min | Setup check | [00 · Prerequisites](docs/00-prerequisites.md) |
| 25 min | Git basics: commits and branches | [01 · Git basics](docs/01-git-basics.md) |
| 10 min | Not committing the wrong files | [.gitignore guide](docs/gitignore-guide.md) |
| 10 min | How we work: trunk-based development | [02 · Trunk-based development](docs/02-trunk-based-development.md) |
| 20 min | GitHub: forks, protected `main`, pull requests | [03 · GitHub workflow](docs/03-github-workflow.md) |
| 75 min | Hands-on exercises | [04 · Exercises](docs/04-exercises.md) + [05 · Tasks](docs/05-tasks.md) |
| 10 min | Wrap-up and questions | [Cheatsheet](docs/cheatsheet.md) |

Keep the **[cheatsheet](docs/cheatsheet.md)** open in a tab.

## 🐍 The project

```text
.
├── ecotrack/            # the Python program
│   ├── laps.py          #   lap time statistics
│   ├── telemetry.py     #   speed and efficiency helpers
│   └── cli.py           #   what gets printed on screen
├── data/                # lap times (CSV files)
├── team/                # one file per team member (you'll add yours!)
├── tests/               # automatic tests, run by GitHub on every PR
└── docs/                # the workshop guides
```

Run it from this folder:

```bash
python3 -m ecotrack data/sample_laps.csv      # on Windows: python -m ecotrack data/sample_laps.csv
```

Look closely at the output. Something is wrong… 👀 (That's task T1 in
[docs/05-tasks.md](docs/05-tasks.md).)

<details>
<summary>Optional: run the tests yourself</summary>

GitHub runs the tests automatically on every pull request, so you don't have to.
If you're curious:

```bash
python3 -m pip install pytest
python3 -m pytest
```
</details>

## 🤝 Contributing

Read **[CONTRIBUTING.md](CONTRIBUTING.md)**. It's short.

## 🧑‍🏫 Running the workshop?

See **[docs/facilitator-guide.md](docs/facilitator-guide.md)**.
