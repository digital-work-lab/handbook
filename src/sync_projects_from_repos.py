"""Synchronize research paper project pages from repository metadata.

This script reads repository definitions from the `_repos/` collection and
creates or updates corresponding project pages in `_projects/` for all repos
that are tagged with both ``research`` and ``paper`` (case-insensitive).

Existing project files keep their custom fields and body content. Only the
canonical fields required by the handbook schema are refreshed and a standard
resources table is ensured to exist. Newly created project files receive the
default page body template defined here.
"""
from __future__ import annotations

import datetime as _dt
import io
import re
from pathlib import Path
from typing import Iterable, List, MutableMapping, Sequence

import frontmatter
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

REPO_DIR = Path(__file__).resolve().parent.parent / "_repos"
PROJECT_DIR = Path(__file__).resolve().parent.parent / "_projects"

PAGE_TEMPLATE = """# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Title               | {{ page.title_long }}
Status              | {{ page.status }}
Started             | {{ page.started }}
Completed           | {{ page.completed }}

## Resources
{% if page.resources %}
<table class="resources">
  <thead>
    <tr>
      <th>Name</th>
      <th>Access</th>
      <th>Last updated</th>
      <th>Request</th>
    </tr>
  </thead>
  <tbody>
    {% for res in page.resources %}
    <tr>
      <td>
        {% if res.link %}
          <a href="{{ res.link }}" target="_blank" rel="noopener">
            {{ res.name | default: res.link }}
          </a>
        {% else %}
          {{ res.name | default: "—" }}
        {% endif %}
      </td>
      <td>
        {% if res.access and res.access.size > 0 %}
          {% for u in res.access %}
            {% if forloop.first == false %}, {% endif %}
            <a href="https://github.com/{{ u }}" target="_blank" rel="noopener">@{{ u }}</a>
          {% endfor %}
        {% else %}
          —
        {% endif %}
      </td>
      <td>
        {% if res.last_updated %}
          {{ res.last_updated | date: "%Y-%m-%d" }}
        {% else %}
          —
        {% endif %}
      </td>
      <td>
        {% if res.link and res.link contains "https://github.com" %}
          <a href="https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository"
             target="_blank" rel="noopener">
            <img src="https://img.shields.io/badge/Request-Access-blue" alt="Request Access">
          </a>
        {% else %}
          —
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<p>—</p>
{% endif %}
"""

RESOURCES_BLOCK = """
## Resources
{% if page.resources %}
<table class="resources">
  <thead>
    <tr>
      <th>Name</th>
      <th>Access</th>
      <th>Last updated</th>
      <th>Request</th>
    </tr>
  </thead>
  <tbody>
    {% for res in page.resources %}
    <tr>
      <td>
        {% if res.link %}
          <a href="{{ res.link }}" target="_blank" rel="noopener">
            {{ res.name | default: res.link }}
          </a>
        {% else %}
          {{ res.name | default: "—" }}
        {% endif %}
      </td>
      <td>
        {% if res.access and res.access.size > 0 %}
          {% for u in res.access %}
            {% if forloop.first == false %}, {% endif %}
            <a href="https://github.com/{{ u }}" target="_blank" rel="noopener">@{{ u }}</a>
          {% endfor %}
        {% else %}
          —
        {% endif %}
      </td>
      <td>
        {% if res.last_updated %}
          {{ res.last_updated | date: "%Y-%m-%d" }}
        {% else %}
          —
        {% endif %}
      </td>
      <td>
        {% if res.link and res.link contains "https://github.com" %}
          <a href="https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository"
             target="_blank" rel="noopener">
            <img src="https://img.shields.io/badge/Request-Access-blue" alt="Request Access">
          </a>
        {% else %}
          —
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<p>—</p>
{% endif %}
""".strip()


def slugify(value: str) -> str:
    """Return a kebab-case slug consisting only of lowercase alphanumerics."""
    value = value.lower()
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"[^a-z0-9-]", "", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "project"


def ensure_commented_map(data: MutableMapping | None) -> CommentedMap:
    """Recursively convert a mapping to ``CommentedMap`` for ruamel.yaml."""
    data = data or {}
    if isinstance(data, CommentedMap):
        cm = CommentedMap()
        for key, value in data.items():
            cm[key] = _convert_value(value)
        return cm

    cm = CommentedMap()
    for key, value in data.items():
        cm[key] = _convert_value(value)
    return cm


def _convert_value(value):
    if isinstance(value, MutableMapping):
        return ensure_commented_map(value)
    if isinstance(value, list):
        return [_convert_value(v) for v in value]
    return value


def load_repo_posts() -> Iterable[tuple[Path, frontmatter.Post]]:
    for path in sorted(REPO_DIR.glob("*.md")):
        yield path, frontmatter.load(path)


def repo_matches(metadata: MutableMapping) -> bool:
    tags = metadata.get("topics", []) or []
    print(tags)
    tags_lower = {str(tag).lower() for tag in tags}
    return {"research", "paper"}.issubset(tags_lower)


def derive_status(metadata: MutableMapping) -> str:
    if metadata.get("archived") is True:
        return "archived"
    tags = metadata.get("tags", []) or []
    tags_lower = {str(tag).lower() for tag in tags}
    if {"research", "paper"}.issubset(tags_lower):
        return "under-review"
    return "planned"


def determine_title(metadata: MutableMapping) -> str:
    title = metadata.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    html_url = metadata.get("html_url", "")
    return html_url.rstrip("/").split("/")[-1] if html_url else "project"


def build_resources(metadata: MutableMapping) -> List[CommentedMap]:
    access = metadata.get("collaborators") or []
    if not isinstance(access, Sequence) or isinstance(access, (str, bytes)):
        access = [str(access)] if access else []
    access_list = [str(item) for item in access if str(item).strip()]

    html_url = metadata.get("html_url")
    pushed_at = metadata.get("pushed_at")
    if pushed_at:
        try:
            last_updated = _dt.datetime.fromisoformat(str(pushed_at)).date()
        except ValueError:
            last_updated = _dt.date.today()
    else:
        last_updated = _dt.date.today()

    resource = CommentedMap()
    resource["name"] = "GitHub repository"
    resource["link"] = html_url
    resource["access"] = access_list
    resource["last_updated"] = last_updated.isoformat()
    return [resource]


def merge_metadata(existing: MutableMapping | None, updates: MutableMapping) -> CommentedMap:
    existing_cm = ensure_commented_map(existing)
    updates_cm = ensure_commented_map(updates)

    key_order = [
        "layout",
        "title",
        "title_long",
        "parent",
        "grand_parent",
        "status",
        "associated_projects",
        "resources",
    ]

    merged = CommentedMap()
    for key in key_order:
        if key in updates_cm:
            merged[key] = updates_cm[key]
        elif key in existing_cm:
            merged[key] = existing_cm[key]

    for key, value in existing_cm.items():
        if key not in merged:
            merged[key] = value

    return merged


def ensure_resources_section(body: str) -> str:
    if "## Resources" in body:
        return body
    body = body.rstrip()
    if body:
        body += "\n\n"
    body += RESOURCES_BLOCK
    return body


def write_project_file(path: Path, metadata: CommentedMap, body: str) -> None:
    yaml = YAML()
    yaml.default_flow_style = False
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.preserve_quotes = True

    buffer = io.StringIO()
    yaml.dump(metadata, buffer)
    yaml_content = buffer.getvalue()
    if not yaml_content.endswith("\n"):
        yaml_content += "\n"

    body = body.strip()
    content = f"---\n{yaml_content}---\n\n{body}\n"
    path.write_text(content, encoding="utf-8")


def sync_project(metadata: MutableMapping, repo_path: Path) -> tuple[str, str]:
    title = determine_title(metadata)
    slug = slugify(title)
    project_path = PROJECT_DIR / f"{slug}.md"

    new_metadata = CommentedMap()
    new_metadata["layout"] = "default"
    new_metadata["title"] = title
    new_metadata["title_long"] = ""
    new_metadata["parent"] = "25 Projects"
    new_metadata["grand_parent"] = "Research"
    new_metadata["status"] = derive_status(metadata)
    new_metadata["associated_projects"] = []
    new_metadata["resources"] = build_resources(metadata)

    if project_path.exists():
        existing_post = frontmatter.load(project_path)
        merged_metadata = merge_metadata(existing_post.metadata, new_metadata)
        body_content = existing_post.content or ""
        body_content = ensure_resources_section(body_content)
        action = "updated"
    else:
        merged_metadata = merge_metadata({}, new_metadata)
        body_content = PAGE_TEMPLATE.strip()
        action = "created"

    write_project_file(project_path, merged_metadata, body_content)
    return action, slug


def main() -> None:
    created = []
    updated = []

    for repo_path, post in load_repo_posts():
        metadata = post.metadata or {}
        if not repo_matches(metadata):
            continue

        action, slug = sync_project(metadata, repo_path)
        if action == "created":
            created.append(slug)
        else:
            updated.append(slug)

    summary = []
    if created:
        summary.append(f"created: {', '.join(created)}")
    if updated:
        summary.append(f"updated: {', '.join(updated)}")
    if summary:
        print("Sync complete (" + "; ".join(summary) + ")")
    else:
        print("Sync complete (no matching repositories)")


if __name__ == "__main__":
    main()
