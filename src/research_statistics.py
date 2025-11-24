#!/usr/bin/env python3
"""
Integrated monthly activity reports for the Digital-Work Lab.

- Org-wide stats (research / teaching / lab-management repos via GitHub API)
- Handbook growth based on local git history
- Plots:
    - teaching_repos_activity_per_month.csv
    - research_repos_activity_per_month.csv
    - lab_management_repos_activity_per_month.csv
    - handbook_growth.csv
    - teaching_research_lab_handbook_commits_per_month.png
    - handbook_activity_over_time.png
"""

import os
import subprocess
import calendar
import datetime as dt
from collections import defaultdict
from pathlib import PurePosixPath

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from github import Github, GithubException


# ----------------------------------------------------------------------
# Shared / config
# ----------------------------------------------------------------------

ORG_NAME = "digital-work-lab"

RESEARCH_CSV = "assets/reports/research_repos_activity_per_month.csv"
TEACH_CSV = "assets/reports/teaching_repos_activity_per_month.csv"
LAB_CSV = "assets/reports/lab_management_repos_activity_per_month.csv"
HANDBOOK_CSV = "assets/reports/handbook_growth.csv"

COMBINED_PLOT = "assets/reports/teaching_research_lab_handbook_commits_per_month.png"
HANDBOOK_PLOT = "assets/reports/handbook_activity_over_time.png"


def make_jan_jun_ticks(dates):
    """Return list of YYYY-01-01 and YYYY-06-01 ticks over the span of `dates`."""
    dates = pd.to_datetime(dates)
    if dates.empty:
        return []

    start_year = int(dates.min().year)
    end_year = int(dates.max().year)

    ticks = []
    for year in range(start_year, end_year + 1):
        for month in (1, 6):
            ticks.append(dt.datetime(year, month, 1))
    return ticks


# ----------------------------------------------------------------------
# Part 1 – Org-wide stats (from research_statistics.py)
# ----------------------------------------------------------------------


def iter_topic_repos(org, topic, exclude_names=None):
    """Yield repos in the org whose GitHub 'topics' include the given topic."""
    exclude_names = set(exclude_names or [])

    for repo in org.get_repos():
        if repo.archived:
            continue

        if repo.name in exclude_names:
            continue

        try:
            topics = repo.get_topics()
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
    For a given repo, count additions in all markdown files (*.md, *.markdown) per commit.

    Returns list of dicts:
    {
        'repo': repo_name,
        'date': date (datetime.date),
        'lines_added': additions_to_all_md_files_in_commit
    }
    """
    rows = []

    try:
        commits = repo.get_commits()
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
        df.groupby(["repo", "year_month"], as_index=False)
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


def collect_org_activity(github_token):
    """Collect activity for research / teaching / lab-management repos."""
    g = Github(github_token)
    org = g.get_organization(ORG_NAME)

    # ----- RESEARCH: topic 'research', focus on paper.md -----
    all_rows_research = []
    for repo in iter_topic_repos(org, "research"):
        repo_rows = collect_lines_added_for_repo(repo, path_suffix="paper.md")
        all_rows_research.extend(repo_rows)

    agg_research = aggregate_activity(
        all_rows_research,
        RESEARCH_CSV,
        group_label="research (topic 'research')",
    )

    # ----- TEACHING: topic 'teaching', all markdown -----
    teaching_excludes = {
        "test-quartz",
        "thesis-test",
        "theses-confidential",
        "teaching_hub",
        "practice-git",
        "digital-work-lecture-exam",
    }

    all_rows_teaching = []
    for repo in iter_topic_repos(org, "teaching", exclude_names=teaching_excludes):
        repo_rows = collect_md_lines_added_for_repo(repo)
        all_rows_teaching.extend(repo_rows)

    agg_teaching = aggregate_activity(
        all_rows_teaching,
        TEACH_CSV,
        group_label="teaching (topic 'teaching')",
    )

    # ----- LAB-MANAGEMENT: topic 'lab-management', all markdown -----
    all_rows_lab = []
    for repo in iter_topic_repos(org, "lab-management"):
        repo_rows = collect_md_lines_added_for_repo(repo)
        all_rows_lab.extend(repo_rows)

    agg_lab = aggregate_activity(
        all_rows_lab,
        LAB_CSV,
        group_label="lab-management (topic 'lab-management')",
    )

    return agg_research, agg_teaching, agg_lab


# ----------------------------------------------------------------------
# Part 2 – Handbook growth (from handbook_growth.py)
# ----------------------------------------------------------------------


def run(cmd):
    result = subprocess.run(
        cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    return result.stdout.strip()


def get_commits(branch="main"):
    """Return list of commit dicts with hash, date, author (oldest -> newest)."""
    log_output = run([
        "git", "log", branch,
        "--reverse",
        "--pretty=format:%H%x09%ad%x09%ae",
        "--date=short",
    ])
    commits = []
    for line in log_output.splitlines():
        commit_hash, date_str, author = line.split("\t")
        date = dt.date.fromisoformat(date_str)
        commits.append({"hash": commit_hash, "date": date, "author": author})
    return commits


def list_markdown_files_at_commit(commit_hash):
    """List markdown files under docs/ plus index.md at the given commit."""
    tree_output = run(["git", "ls-tree", "-r", "--name-only", commit_hash])
    files = []
    for line in tree_output.splitlines():
        p = PurePosixPath(line)
        if (
            (str(p).startswith("docs/") or str(p) == "index.md")
            and p.suffix in {".md", ".markdown"}
        ):
            files.append(str(p))
    return files


def get_file_content_at_commit(commit_hash, path):
    return run(["git", "show", f"{commit_hash}:{path}"])


def sample_commits(commits, step="month"):
    """Down-sample commits to one per month (or per week) for content snapshots."""
    by_key = {}
    for c in commits:
        date = c["date"]
        if step == "month":
            key = (date.year, date.month)
        elif step == "week":
            key = (date.isocalendar().year, date.isocalendar().week)
        else:
            key = date
        by_key[key] = c  # keep the *last* commit in that period
    return sorted(by_key.values(), key=lambda x: x["date"])


def collect_handbook_stats(branch="main"):
    """Return DataFrame of handbook stats (similar to original collect_stats)."""
    commits = get_commits(branch)
    sampled = sample_commits(commits, step="month")

    # Monthly activity: commits per month & contributors per month
    monthly_activity = {}
    for c in commits:
        d = c["date"]
        key = (d.year, d.month)
        entry = monthly_activity.setdefault(
            key, {"commits": 0, "authors": set()}
        )
        entry["commits"] += 1
        entry["authors"].add(c["author"])

    rows = []

    for c in sampled:
        commit_hash = c["hash"]
        date = c["date"]
        year, month = date.year, date.month

        md_files = list_markdown_files_at_commit(commit_hash)

        total_lines = 0
        section_counts = defaultdict(int)

        for path in md_files:
            content = get_file_content_at_commit(commit_hash, path)
            lines = content.splitlines()
            total_lines += len(lines)

            if path.startswith("docs/"):
                name = PurePosixPath(path).name
                prefix = name.split(".")[0]
                try:
                    section_number = int(prefix)
                    top_level_section = (section_number // 10) * 10
                except ValueError:
                    top_level_section = 0
                section_counts[top_level_section] += 1
            else:
                section_counts[0] += 1

        activity = monthly_activity.get((year, month), {"commits": 0, "authors": set()})
        commits_in_month = activity["commits"]

        days_in_month = calendar.monthrange(year, month)[1]
        weeks_in_month = days_in_month / 7.0 if days_in_month else 1.0
        avg_weekly_commits = commits_in_month / weeks_in_month if weeks_in_month else 0.0

        row = {
            "date": date,
            "commit": commit_hash,
            "num_files": len(md_files),
            "total_lines": total_lines,
            "commits_in_month": commits_in_month,
            "contributors_in_month": len(activity["authors"]),
            "avg_weekly_commits_in_month": avg_weekly_commits,
        }
        for sec in sorted(section_counts.keys()):
            row[f"count_section_{sec}"] = section_counts[sec]

        rows.append(row)

    df = pd.DataFrame(rows).sort_values("date")
    return df


def write_and_plot_handbook(df):
    """Write handbook CSV and plot handbook_activity_over_time.png."""
    df.to_csv(HANDBOOK_CSV, index=False)
    print(f"Wrote handbook growth data to {HANDBOOK_CSV}")

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])

    fig, ax = plt.subplots(figsize=(12, 4.5))

    # activity
    ax.plot(
        df["date"],
        df["avg_weekly_commits_in_month"],
        marker="o",
        label="Avg weekly commits in month",
    )
    ax.plot(
        df["date"],
        df["contributors_in_month"],
        marker="s",
        label="Contributors / month",
    )

    # content (scaled)
    ax.plot(
        df["date"],
        df["num_files"] / 10.0,
        marker="^",
        label="Pages / 10 (tens of pages)",
    )
    ax.plot(
        df["date"],
        df["total_lines"] / 1000.0,
        marker="v",
        label="Markdown lines / 1000 (thousands)",
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Activity / scaled content")
    ax.set_title("Digital-Work Lab Handbook – Monthly Activity & Growth")

    # custom date ticks (Jan / Jun)
    ticks = make_jan_jun_ticks(df["date"])
    if ticks:
        ax.set_xticks(ticks)
        ax.set_xlim(ticks[0], ticks[-1])
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    fig.tight_layout()
    plt.savefig(HANDBOOK_PLOT, dpi=150)
    print(f"Saved handbook activity plot to {HANDBOOK_PLOT}")


def aggregate_handbook_monthly(df):
    """
    Turn handbook snapshot df into monthly commit counts for combined plot.

    We have one row per sampled month already; we:
    - normalize its date to first-of-month
    - use commits_in_month as 'commits'
    """
    if df.empty:
        return pd.DataFrame(columns=["date", "commits"])

    tmp = df.copy()
    tmp["date"] = pd.to_datetime(tmp["date"])
    tmp["month"] = tmp["date"].dt.to_period("M").dt.to_timestamp()

    agg = (
        tmp.groupby("month", as_index=False)["commits_in_month"]
        .max()
        .rename(columns={"month": "date", "commits_in_month": "commits"})
    )
    return agg


# ----------------------------------------------------------------------
# Combined plot
# ----------------------------------------------------------------------


def plot_combined(agg_research, agg_teaching, agg_lab, agg_handbook):
    """Plot combined commits per month (research / teaching / lab / handbook)."""
    if (
        agg_research.empty
        and agg_teaching.empty
        and agg_lab.empty
        and agg_handbook.empty
    ):
        print("No data to plot for combined commits.")
        return

    # collect all dates for axis range and tick computation
    date_series_list = []
    if not agg_research.empty:
        date_series_list.append(agg_research["date"])
    if not agg_teaching.empty:
        date_series_list.append(agg_teaching["date"])
    if not agg_lab.empty:
        date_series_list.append(agg_lab["date"])
    if not agg_handbook.empty:
        date_series_list.append(agg_handbook["date"])

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

    if not agg_handbook.empty:
        ax.plot(
            agg_handbook["date"],
            agg_handbook["commits"],
            marker="^",
            label="Commits / month (handbook repo)",
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


# ----------------------------------------------------------------------
# Main entry point
# ----------------------------------------------------------------------


def main():
    token = os.environ["GITHUB_TOKEN"]

    # 1) Org-wide stats (research / teaching / lab-management)
    agg_research, agg_teaching, agg_lab = collect_org_activity(token)

    # 2) Handbook growth (local repo)
    handbook_df = collect_handbook_stats(branch="main")
    write_and_plot_handbook(handbook_df)
    agg_handbook = aggregate_handbook_monthly(handbook_df)

    # 3) Combined commits plot including handbook
    plot_combined(agg_research, agg_teaching, agg_lab, agg_handbook)


if __name__ == "__main__":
    main()
