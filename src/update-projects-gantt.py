import os
import re
from datetime import datetime


def parse_md_file(file_path):
    """Parse metadata from a Markdown file."""
    with open(file_path, "r") as f:
        content = f.read()

    metadata = {}
    topics = re.search(r"topics:\s*(.*)", content)
    if "paper" not in topics.group(1):
        raise ValueError(f"File {file_path} does not contain 'paper' in topics.")
    # Extract relevant fields using regex
    metadata["title"] = re.search(r"title:\s*(.*)", content).group(1)
    metadata["started"] = re.search(r"started:\s*(\d{4}-\d{2}-\d{2})", content).group(1)
    completed_match = re.search(r"completed:\s*(\d{4}-\d{2}-\d{2})", content)
    metadata["completed"] = completed_match.group(1) if completed_match else None
    metadata["area"] = re.search(r"area:\s*(.*)", content).group(1)
    metadata["status"] = re.search(r"status:\s*(.*)", content).group(1)
    slug = os.path.splitext(os.path.basename(file_path))[0]
    metadata["path"] = f"{{{{ site.baseurl }}}}/docs/10-lab/18-resources/{slug}.html"
    return metadata


def generate_mermaid_chart(projects):
    """Generate a Mermaid Gantt chart."""
    chart = """---
displayMode: compact
---
gantt
title Research Portfolio
dateFormat YYYY-MM-DD
axisFormat %Y
"""

    # Group projects by their area
    grouped_projects = {
        "work_practices": [],
        "distributed_organizing": [],
        "knowledge_synthesis": [],
        "others": [],
    }
    for project in projects:
        area = project["area"]
        if area in grouped_projects:
            grouped_projects[area].append(project)
        else:
            grouped_projects["others"].append(project)

    # remove others if empty
    if not grouped_projects["others"]:
        del grouped_projects["others"]

    # Sort projects by the started date within each area
    current_date = datetime.now().strftime("%Y-%m-%d")
    end_note = ""
    for area, items in grouped_projects.items():
        # sort descending
        items.sort(
            key=lambda x: datetime.strptime(x["started"], "%Y-%m-%d"), reverse=True
        )
        chart += f"\n    section {area}\n"
        for project in items:
            completed_date = (
                project["completed"] if project["completed"] else current_date
            )
            bar_type = "a1"
            if project["status"] == "revising":
                bar_type = "crit"
            if project["status"] == "abandoned":
                bar_type = "done"
            if project["status"] == "under-review":
                bar_type = "under_review"

            chart += f"        {project['title']} :{project['title']}, {project['started']}, {completed_date}\n"
            end_note += f'    click {project["title"]} href "{project["path"]}"\n'

    chart += "\n\n" + end_note
    return chart


def main():
    projects_dir = "_repos"
    projects = []

    for filename in os.listdir(projects_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(projects_dir, filename)
            try:
                project_data = parse_md_file(file_path)
                projects.append(project_data)
            except ValueError as ve:
                pass
            except Exception as e:
                # raise e
                print(f"Error processing file {filename}: {e}")

    mermaid_chart = generate_mermaid_chart(projects)

    with open("docs/20-research/25-projects-gantt.md", "w") as f:
        f.write("---\n")
        f.write("layout: default\n")
        f.write("title: Projects portfolio\n")
        f.write("nav_exclude: true\n")
        f.write("---\n\n{: .text-center}\n```mermaid\n")
        f.write(mermaid_chart)
        f.write("```\n")


if __name__ == "__main__":
    main()
