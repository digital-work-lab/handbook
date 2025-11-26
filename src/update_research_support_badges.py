#!/usr/bin/env python3
from github import Github
from pathlib import Path
import os
import base64
import yaml
import textwrap


def main():
    token = os.environ["GITHUB_TOKEN"]
    org_name = "digital-work-lab"
    docs_file = Path("docs/20-research/20_processes/20.23.research-support.md")

    g = Github(token)
    org = g.get_organization(org_name)

    entries = []

    for repo in org.get_repos():
        if repo.archived:
            continue
        print(repo)
        # Try to read status.yaml from the repo
        try:
            file = repo.get_contents("status.yaml")
        except Exception:
            continue  # skip repos without status.yaml

        try:
            yaml_bytes = base64.b64decode(file.content)
            status_data = yaml.safe_load(yaml_bytes) or {}
            value = int(status_data["currently"]["md_needs_manual_preparation"])
        except Exception as e:
            print(
                f"Skipping {repo.name}: could not parse "
                f"md_needs_manual_preparation ({e})"
            )
            continue

        if value == 0:
            message = "ok"
            color = "brightgreen"
        else:
            message = f"{value}_pending"
            color = "orange"

        badge_url = (
            f"https://img.shields.io/badge/manual_prep-{message}-{color}"
            .replace(" ", "_")
        )

        # Table row (Markdown)
        row = (
            f"| [{repo.name}](https://github.com/{org_name}/{repo.name}/blob/main/data/records.bib)"
            '{{: target="_blank"}} '
            f"| ![Manual prep status]({badge_url})"
            '{{: target="_blank"}} |'
        )
        entries.append(row)

    if entries:
        # Markdown table header + rows
        body = "\n".join([
            "| Repository | Manual prep status |",
            "|------------|---------------------|",
            *entries,
        ])
    else:
        body = "_No repositories with `status.yaml` found in the organization._"

    section = textwrap.dedent(f"""\
<!-- AUTO-GENERATED: research-support-badges START -->
## Preparation of reference metadata

This section is updated by a [GitHub Actions workflow](https://github.com/digital-work-lab/handbook/actions/workflows/update-research-support-badges.yml){{: target="_blank"}}. Do not edit manually.

{body}

<!-- AUTO-GENERATED: research-support-badges END -->
    """)

    if not docs_file.exists():
        raise SystemExit(f"{docs_file} does not exist")

    original = docs_file.read_text()

    start_marker = "<!-- AUTO-GENERATED: research-support-badges START -->"
    end_marker = "<!-- AUTO-GENERATED: research-support-badges END -->"

    # Replace or append
    if start_marker in original and end_marker in original:
        before, rest = original.split(start_marker, 1)
        _, after = rest.split(end_marker, 1)
        new_content = before.rstrip() + "\n\n" + section + "\n" + after.lstrip()
    else:
        if not original.endswith("\n"):
            original += "\n"
        new_content = original + "\n" + section + "\n"

    docs_file.write_text(new_content)
    print(f"Updated {docs_file}")


if __name__ == "__main__":
    main()
