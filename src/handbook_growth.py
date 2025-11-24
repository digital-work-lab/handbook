#!/usr/bin/env python3
import subprocess
import datetime as dt
from collections import defaultdict
from pathlib import PurePosixPath
import calendar

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# --- helpers -----------------------------------------------------


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
        "--pretty=format:%H%x09%ad%x09%ae",  # hash, date, author email
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


# --- main logic --------------------------------------------------


def sample_commits(commits, step="month"):
    """Down-sample commits to one per month (or per week) for content snapshots."""
    by_key = {}
    for c in commits:
        hsh = c["hash"]
        date = c["date"]
        if step == "month":
            key = (date.year, date.month)
        elif step == "week":
            key = (date.isocalendar().year, date.isocalendar().week)
        else:
            key = date  # no sampling
        # keep the *last* commit in that period
        by_key[key] = c
    # sort by actual date
    return sorted(by_key.values(), key=lambda x: x["date"])


def collect_stats(branch="main"):
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

            # crude "section" detection from filename like docs/10.10-handbook.md
            if path.startswith("docs/"):
                # take leading number before first dot, e.g., 10, 20, 30, ...
                name = PurePosixPath(path).name
                prefix = name.split(".")[0]
                try:
                    section_number = int(prefix)
                    top_level_section = (section_number // 10) * 10  # 10,20,30,40,50
                except ValueError:
                    top_level_section = 0  # other
                section_counts[top_level_section] += 1
            else:
                section_counts[0] += 1  # index.md etc.

        # monthly activity for this snapshot's month
        activity = monthly_activity.get((year, month), {"commits": 0, "authors": set()})
        commits_in_month = activity["commits"]

        # average weekly commits in this month
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


def main():
    df = collect_stats("main")
    df.to_csv("assets/reports/handbook_growth.csv", index=False)
    print("Wrote handbook_growth.csv")

    # ensure datetime64 for date column
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

    # ----- custom date ticks: YYYY-01-01 and YYYY-06-01 -----
    start_year = int(df["date"].dt.year.min())
    end_year = int(df["date"].dt.year.max())

    ticks = []
    for year in range(start_year, end_year + 1):
        for month in (1, 6):
            ticks.append(dt.datetime(year, month, 1))

    ax.set_xticks(ticks)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    # ----- force the plot to start at 2023-05 -----
    xmin = dt.datetime(2023, 5, 1)
    xmax = ticks[-1]
    ax.set_xlim(xmin, xmax)

    ax.legend(loc="upper left")

    fig.tight_layout()
    plt.savefig("assets/reports/handbook_activity_over_time.png", dpi=150)
    print("Saved handbook_activity_over_time.png")



if __name__ == "__main__":
    main()
