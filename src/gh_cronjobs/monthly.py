#! /usr/bin/env python
import datetime
from pathlib import Path

import git


def update_git_diff_in_readme():
    repo = git.Repo()
    latest = ""
    first_in_month = ""
    first_date_in_month = ""
    current_month = 0
    for commit in repo.iter_commits(rev="main"):
        date = datetime.datetime.fromtimestamp(commit.committed_date)
        if latest == "":
            latest = commit
            current_month = date.month
        if date.month < current_month - 1:
            break
        first_in_month = commit
        first_date_in_month = date

    index_content = Path("index.md").read_text(encoding="utf-8")

    before_diff = index_content[: index_content.find("## Recent changes")]

    after_diff = index_content[index_content.find("## Contributors") :]
    selected_month = first_date_in_month.strftime("%B")

    updated_content = (
        before_diff
        + "## Recent changes\n\n"
        + f"- [Handbook changes in {selected_month}](https://github.com/digital-work-lab/handbook/compare/{first_in_month}...{latest})\n\n"
        + after_diff
    )

    with open("index.md", "w", encoding="utf-8") as file:
        file.write(updated_content)

    repo.index.add(["index.md"])
    repo.index.commit(f"Update changes for {selected_month}")


if __name__ == "__main__":
    update_git_diff_in_readme()
