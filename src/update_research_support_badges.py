#!/usr/bin/env python3
import subprocess
import json
import base64
import yaml
from pathlib import Path
import os
import textwrap


def gh_json(args):
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"gh command failed: {' '.join(args)}\n{result.stderr}"
        )
    return json.loads(result.stdout)


def main():
    org = os.environ["ORG_NAME"]
    docs_file = Path(os.environ["DOCS_FILE"])

    # list non-archived repos
    repos_data = gh_json([
        "repo", "list", org,
        "--limit", "200",
        "--json", "name,isArchived"
    ])

    repo_names = [
        r["name"] for r in repos_data
        if not r.get("isArchived")
    ]

    entries = []

    for name in sorted(repo_names):
        # Try to get status.yaml from default branch
        # If missing (404), skip
        proc = subprocess.run(
            [
                "gh", "api",
                f"repos/{org}/{name}/contents/status.yaml"
            ],
            capture_output=True,
            text=True,
        )

        if proc.returncode != 0:
            # no status.yaml in this repo
            continue

        try:
            info = json.loads(proc.stdout)
            content_b64 = info["content"]
            yaml_bytes = base64.b64decode(content_b64)
            status_data = yaml.safe_load(yaml_bytes) or {}
        except Exception as e:
            print(f"Skipping {name}: failed to parse status.yaml ({e})")
            continue

        try:
            value = int(
                status_data["currently"]["md_needs_manual_preparation"]
            )
        except Exception as e:
            print(
                f"Skipping {name}: md_needs_manual_preparation "
                f"missing or invalid ({e})"
            )
            continue

        if value == 0:
            color = "brightgreen"
            message = "ok"
        else:
            color = "orange"
            message = f"{value}_pending"

        # Shields static badge, message must be URL-safe-ish
        # Example: https://img.shields.io/badge/manual_prep-ok-brightgreen
        badge_url = (
            f"https://img.shields.io/badge/manual_prep-{message}-{color}"
        )

        line = (
            f"- [`{name}`](https://github.com/{org}/{name}) "
            f"![Manual prep status]({badge_url})"
        )
        entries.append(line)

    if entries:
        body = "\n".join(entries)
    else:
        body = "_No repositories with `status.yaml` found in the organization._"

    section = textwrap.dedent(f"""\
    <!-- AUTO-GENERATED: research-support-badges START -->
    ### Research support status (auto-generated)

    This section is updated by a GitHub Actions workflow. Do not edit manually.

    {body}

    <!-- AUTO-GENERATED: research-support-badges END -->
    """)

    if not docs_file.exists():
        raise SystemExit(f"{docs_file} does not exist")

    original = docs_file.read_text()

    start_marker = "<!-- AUTO-GENERATED: research-support-badges START -->"
    end_marker = "<!-- AUTO-GENERATED: research-support-badges END -->"

    if start_marker in original and end_marker in original:
        # Replace existing section
        before, rest = original.split(start_marker, 1)
        _, after = rest.split(end_marker, 1)
        new_content = before.rstrip() + "\n\n" + section + "\n" + after.lstrip()
    else:
        # Append section at the end
        if not original.endswith("\n"):
            original += "\n"
        new_content = original + "\n" + section + "\n"

    docs_file.write_text(new_content)
    print(f"Updated {docs_file}")


if __name__ == "__main__":
    main()
