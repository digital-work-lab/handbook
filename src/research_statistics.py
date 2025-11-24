#!/usr/bin/env python3
import os
import datetime as dt

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from github import Github, GithubException


ORG_NAME = "digital-work-lab"

RESEARCH_CSV = "assets/reports/research_repos_activity_per_month.csv"
TEACH_CSV = "assets/reports/teaching_repos_activity_per_month.csv"
LAB_CSV = "assets/reports/lab_management_repos_activity_per_month.csv"

COMBINED_PLOT = "assets/reports/teaching_research_lab_handbook_commits_per_month.png"


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------


def iter_topic_repos(org, topic, exclude_names=None):
    """Yield repos in the org whose GitHub 'topics' include the given topic."""
    exclude_names = set(exclude_names or [])

    for repo in org.get_repos():
        if repo.archived:
            continue

        # skip explicitly excluded repos
        if repo.name in exclude_names:
            continue

        try:
            topics = repo.get_topics()  # GitHub repository topics
        except GithubException as e:
            print(f"Could not get topics for {repo.full_name}: {e}")
            continue

        if topic in topics:
            print(f"Using repo (topic '{topic}'): {repo.full_name}")
            yield repo


def collect_lines_added_for_repo(repo, path_suffix="paper.md"):
    """
    For a given repo, return list of dicts:
    {
        'repo': repo_name,
        'date': date (datetime.date),
        'lines_added': additions_to *path_suffix* in commit
    }

    Matches any file whose name ends with path_suffix (e.g., 'paper.md').
    Each row = one commit that changed that file with > 0 added lines.
    """
    rows = []

    try:
        commits = repo.get_commits(path=path_suffix)
    except GithubException as e:
        print(f"Could not get commits for {repo.full_name}: {e}")
        return rows

    for c in commits:
        full_commit = repo.get_commit(c.sha)
        commit_date = full_commit.commit.author.date.date()

        lines_added = 0
        for f in full_commit.files:
            if f.filename.endswith(path_suffix):
                lines_added += f.additions

        if lines_added > 0:
            rows.append(
                {
                    "repo": repo.name,
                    "date": commit_date,
                    "lines_added": lines_added,
                }
            )

    return rows


def collect_md_lines_added_for_repo(repo):
    """
    For a given repo, count additions in ALL markdown files (*.md, *.markdown) per commit.

    Returns list of dicts:
    {
        'repo': repo_name,
        'date': date (datetime.date),
        'lines_added': additions_to_all_md_files_in_commit
    }

    Each row = one commit that changed at least one markdown file with > 0 added lines.
    """
    rows = []

    try:
        commits = repo.get_commits()  # all commits; we'll filter by files
    except GithubException as e:
        print(f"Could not get commits for {repo.full_name}: {e}")
        return rows

    for c in commits:
        full_commit = repo.get_commit(c.sha)
        commit_date = full_commit.commit.author.date.date()

        lines_added = 0
        for f in full_commit.files:
            if f.filename.endswith(".md") or f.filename.endswith(".markdown"):
                lines_added += f.additions

        if lines_added > 0:
            rows.append(
                {
                    "repo": repo.name,
                    "date": commit_date,
                    "lines_added": lines_added,
                }
            )

    return rows


def make_jan_jun_ticks(dates):
    """Return list of YYYY-01-01 and YYYY-06-01 ticks over the span of `dates`."""
    dates = pd.to_datetime(dates)
    start_year = int(dates.min().year)
    end_year = int(dates.max().year)

    ticks = []
    for year in range(start_year, end_year + 1):
        for month in (1, 6):
            ticks.append(dt.datetime(year, month, 1))
    return ticks


def aggregate_activity(rows, csv_path, group_label):
    """
    Turn a list of per-commit rows into:
    - a per-repo-per-month CSV (lines_added, commits)
    - an aggregated per-month DataFrame with columns ['date', 'commits'].
    """
    if not rows:
        print(f"No data collected for {group_label}.")
        return pd.DataFrame(columns=["date", "commits"])

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df["year_month"] = df["date"].dt.to_period("M").dt.to_timestamp()

    per_repo_month = (
        df
        .groupby(["repo", "year_month"], as_index=False)
        .agg(
            lines_added=("lines_added", "sum"),
            commits=("lines_added", "size"),
        )
    )

    per_repo_month.to_csv(csv_path, index=False)
    print(f"Wrote {group_label} per-project activity to {csv_path}")

    agg = (
        per_repo_month
        .groupby("year_month", as_index=False)["commits"]
        .sum()
    )
    agg.rename(columns={"year_month": "date"}, inplace=True)
    return agg


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------


def main():
    token = os.environ["GITHUB_TOKEN"]
    g = Github(token)
    org = g.get_organization(ORG_NAME)

    # -------------------- RESEARCH REPOS (topic: research) --------------------
    all_rows_research = []
    for repo in iter_topic_repos(org, "research"):
        # For research repos: focus on paper.md
        repo_rows = collect_lines_added_for_repo(repo, path_suffix="paper.md")
        all_rows_research.extend(repo_rows)

    agg_research = aggregate_activity(
        all_rows_research,
        RESEARCH_CSV,
        group_label="research (topic 'research')",
    )

    # -------------------- TEACHING REPOS (topic: teaching) --------------------
    all_rows_teaching = []

    teaching_excludes = {
        "test-quartz",
        "thesis-test",
        "theses-confidential",
        "teaching_hub",
        "practice-git",
        "digital-work-lecture-exam",
    }

    for repo in iter_topic_repos(org, "teaching", exclude_names=teaching_excludes):
        # For teaching repos: count all markdown activity
        repo_rows = collect_md_lines_added_for_repo(repo)
        all_rows_teaching.extend(repo_rows)

    agg_teaching = aggregate_activity(
        all_rows_teaching,
        TEACH_CSV,
        group_label="teaching (topic 'teaching')",
    )

    # -------------------- LAB-MANAGEMENT REPOS (topic: lab-management) --------------------
    all_rows_lab = []
    for repo in iter_topic_repos(org, "lab-management"):
        # For lab-management repos: count all markdown activity
        repo_rows = collect_md_lines_added_for_repo(repo)
        all_rows_lab.extend(repo_rows)

    agg_lab = aggregate_activity(
        all_rows_lab,
        LAB_CSV,
        group_label="lab-management (topic 'lab-management')",
    )


    # -------------------- COMBINED PLOT: commits/month --------------------
    if (
        agg_research.empty
        and agg_teaching.empty
        and agg_lab.empty
    ):
        print("No data to plot.")
        return

    # collect all dates to set the overall axis range and ticks
    date_series_list = []
    if not agg_research.empty:
        date_series_list.append(agg_research["date"])
    if not agg_teaching.empty:
        date_series_list.append(agg_teaching["date"])
    if not agg_lab.empty:
        date_series_list.append(agg_lab["date"])

    dates_for_ticks = pd.concat(date_series_list, ignore_index=True)

    fig, ax = plt.subplots(figsize=(12, 4.5))

    if not agg_research.empty:
        ax.plot(
            agg_research["date"],
            agg_research["commits"],
            marker="o",
            label="Commits / month (research-tagged repos)",
        )

    if not agg_teaching.empty:
        ax.plot(
            agg_teaching["date"],
            agg_teaching["commits"],
            marker="s",
            label="Commits / month (teaching-tagged repos)",
        )

    if not agg_lab.empty:
        ax.plot(
            agg_lab["date"],
            agg_lab["commits"],
            marker="D",
            label="Commits / month (lab-management-tagged repos)",
        )

    ax.set_xlabel("Date")
    ax.set_ylabel("Commits per month")
    ax.set_title(
        "Digital-Work Lab – Commits per month\n"
        "(research, teaching, lab-management, handbook)"
    )

    ticks = make_jan_jun_ticks(dates_for_ticks)
    if ticks:
        ax.set_xticks(ticks)
        ax.set_xlim(ticks[0], ticks[-1])
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    ax.legend(loc="upper left")
    fig.tight_layout()
    plt.savefig(COMBINED_PLOT, dpi=150)
    print(f"Saved combined commits plot to {COMBINED_PLOT}")


if __name__ == "__main__":
    main()
