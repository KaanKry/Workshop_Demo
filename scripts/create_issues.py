"""Create one GitHub issue per task in docs/05-tasks.md.

Facilitator only. Requires the GitHub CLI (`gh`), logged in with `gh auth login`.

    python scripts/create_issues.py --repo H2politO/git-workshop --dry-run
    python scripts/create_issues.py --repo H2politO/git-workshop
"""

import argparse
import re
import subprocess
from pathlib import Path

TASKS_FILE = Path(__file__).resolve().parent.parent / "docs" / "05-tasks.md"
HEADING = re.compile(r"^### (T\d+) \S+ (.+)$")
RELATIVE_LINK = re.compile(r"\]\((?!https?:)([^)]+)\)")


def parse_tasks(text: str) -> list[tuple[str, str]]:
    """Return (title, body) pairs, one per `### Tn ...` heading."""
    tasks: list[tuple[str, list[str]]] = []
    for line in text.splitlines():
        match = HEADING.match(line)
        if match:
            tasks.append((f"{match.group(1)}: {match.group(2)}", []))
        elif line.startswith("---") and tasks:
            tasks.append(("", []))  # a horizontal rule ends the last task
        elif tasks and tasks[-1][0]:
            tasks[-1][1].append(line)
    return [(title, "\n".join(body).strip()) for title, body in tasks if title]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", required=True, help="OWNER/REPO, e.g. H2politO/git-workshop")
    parser.add_argument("--dry-run", action="store_true", help="print, don't create")
    args = parser.parse_args()

    docs_url = f"https://github.com/{args.repo}/blob/main/docs"
    for title, body in parse_tasks(TASKS_FILE.read_text(encoding="utf-8")):
        # Relative links like (04-exercises.md#...) don't work inside issues.
        body = RELATIVE_LINK.sub(lambda m: f"]({docs_url}/{m.group(1)})", body)
        body += f"\n\n_From [docs/05-tasks.md]({docs_url}/05-tasks.md)._"
        print(f"→ {title}")
        if args.dry_run:
            continue
        subprocess.run(
            ["gh", "issue", "create", "--repo", args.repo, "--title", title,
             "--body", body, "--label", "good first issue"],
            check=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
