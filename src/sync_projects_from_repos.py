"""
Synchronize research paper project pages from repository metadata.

This script reads repository definitions from the `_repos/` collection and
creates or updates corresponding project pages in `_projects/` for all repos
that are tagged with both ``research`` and ``paper`` (case-insensitive).

Existing project files keep their custom fields and body content. Only the
canonical fields required by the handbook schema are refreshed and a standard
resources table is ensured to exist. Newly created project files receive the
default page body template defined here.

Duplicate guard:
- A new project file is created only if the repository URL is not already
  referenced in any existing project's `resources[*].link`. If found, creation
  is skipped (but updating an existing page with the same slug proceeds).

Resource merge:
- Existing `resources` are NOT replaced. We merge by URL:
  * If a resource with the same normalized link exists, we update its
    `access` and `last_updated` (preserve `name` and any custom fields).
  * Otherwise, we append the new resource entry.
"""
from __future__ import annotations

import datetime as _dt
import io
import re
from pathlib import Path
from typing import Iterable, List, MutableMapping, Sequence, Dict, Any
from urllib.parse import urlparse

import frontmatter
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

REPO_DIR = Path(__file__).resolve().parent.parent / "_repos"
PROJECT_DIR = Path(__file__).resolve().parent.parent / "_projects"

PAGE_TEMPLATE = """## {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Team                | {{ page.collaborators | join: ", " }}
Status              | {{ page.status }}

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
    value = value.lower()
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"[^a-z0-9-]", "", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "project"


def ensure_commented_map(data: MutableMapping | None) -> CommentedMap:
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


def normalize_repo_url(url: str) -> str:
    """Normalize repo URLs (handles ssh, .git, case, trailing slash)."""
    if not url:
        return ""
    url = url.strip()
    if url.startswith("git@"):
        try:
            host = url.split("@", 1)[1].split(":", 1)[0]
            path = url.split(":", 1)[1]
            path = path.rstrip("/").rstrip(".git")
            return f"https://{host.lower()}/{path}".rstrip("/").lower()
        except Exception:
            return url.lower().rstrip("/")
    parsed = urlparse(url)
    netloc = (parsed.netloc or "").lower()
    path = (parsed.path or "").rstrip("/").rstrip(".git")
    if not netloc and path:
        parts = path.lstrip("/").split("/", 1)
        if parts and parts[0]:
            netloc = parts[0].lower()
            path = "/" + (parts[1] if len(parts) > 1 else "")
    normalized = (
        f"https://{netloc}{path}".rstrip("/").lower()
        if netloc
        else url.lower().rstrip("/")
    )
    return normalized


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
    resource["name"] = "GitHub repository"  # only used when adding a NEW entry
    resource["link"] = html_url
    resource["access"] = access_list
    # store as a real date so YAML emits it without quotes
    resource["last_updated"] = last_updated
    return [resource]


def merge_resources(existing: Any, updates: Any) -> List[CommentedMap]:
    """
    Merge resources by normalized 'link'.
    - Keep all existing entries.
    - If an update matches an existing link, update `access` and `last_updated` only;
      preserve existing `name` and any custom fields.
    - If an update link is new, append it (using the update's whole entry).
    """
    # Normalize structures
    existing_list: List[MutableMapping] = existing if isinstance(existing, list) else []
    updates_list: List[MutableMapping] = updates if isinstance(updates, list) else []

    # Build index for existing by normalized link
    index: Dict[str, MutableMapping] = {}
    for res in existing_list:
        if not isinstance(res, MutableMapping):
            continue
        norm = normalize_repo_url(str(res.get("link", "")))
        if norm:
            index.setdefault(norm, res)

    # Apply updates
    for upd in updates_list:
        if not isinstance(upd, MutableMapping):
            continue
        norm = normalize_repo_url(str(upd.get("link", "")))
        if not norm:
            continue
        if norm in index:
            tgt = index[norm]
            # Update access if provided
            if "access" in upd and isinstance(upd["access"], list):
                tgt["access"] = [str(x) for x in upd["access"]]
            # Update last_updated if provided; accept date or ISO string
            if "last_updated" in upd and upd["last_updated"]:
                lv = upd["last_updated"]
                if isinstance(lv, str):
                    try:
                        lv = _dt.date.fromisoformat(lv)
                    except ValueError:
                        # if parsing fails, keep the original value
                        pass
                tgt["last_updated"] = lv
            # Keep existing name if present; only set if missing
            if not tgt.get("name") and upd.get("name"):
                tgt["name"] = upd["name"]
        else:
            # Append new entry (convert to CommentedMap for consistency)
            cm = CommentedMap()
            for k, v in upd.items():
                cm[k] = v
            existing_list.append(cm)
            index[norm] = cm

    # Ensure each result is CommentedMap
    merged: List[CommentedMap] = []
    for res in existing_list:
        if isinstance(res, CommentedMap):
            merged.append(res)
        elif isinstance(res, MutableMapping):
            cm = CommentedMap()
            for k, v in res.items():
                cm[k] = v
            merged.append(cm)
    return merged


def merge_metadata(
    existing: MutableMapping | None, updates: MutableMapping
) -> CommentedMap:
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
        "resources",  # handled specially below
    ]

    merged = CommentedMap()

    for key in key_order:
        if key == "resources":
            # Merge resources instead of replacing
            merged[key] = merge_resources(existing_cm.get(key), updates_cm.get(key))
            continue
        if key in updates_cm:
            merged[key] = updates_cm[key]
        elif key in existing_cm:
            merged[key] = existing_cm[key]

    # Bring over any remaining existing keys (e.g., collaborators, tags) untouched
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


def index_existing_resource_links() -> Dict[str, Path]:
    """Return a map of normalized resource-link -> project file that references it."""
    index: Dict[str, Path] = {}
    for proj_path in sorted(PROJECT_DIR.glob("*.md")):
        try:
            post = frontmatter.load(proj_path)
        except Exception:
            continue
        resources = post.metadata.get("resources", []) or []
        if not isinstance(resources, list):
            continue
        for res in resources:
            if not isinstance(res, MutableMapping):
                continue
            link = str(res.get("link", "")).strip()
            norm = normalize_repo_url(link)
            if norm:
                index.setdefault(norm, proj_path)
    return index


def sync_project(
    metadata: MutableMapping,
    repo_path: Path,
    existing_links_index: Dict[str, Path],
) -> tuple[str, str]:
    title = determine_title(metadata)
    slug = slugify(title)
    project_path = PROJECT_DIR / f"{slug}.md"

    html_url = str(metadata.get("html_url", "")).strip()
    norm_repo_url = normalize_repo_url(html_url)

    new_metadata = CommentedMap()
    new_metadata["layout"] = "default"
    new_metadata["title"] = title
    new_metadata["title_long"] = ""
    new_metadata["parent"] = "25 Projects"
    new_metadata["grand_parent"] = "Research"
    new_metadata["associated_projects"] = []
    new_metadata["resources"] = build_resources(metadata)

    if project_path.exists():
        existing_post = frontmatter.load(project_path)
        merged_metadata = merge_metadata(existing_post.metadata, new_metadata)
        body_content = existing_post.content or ""
        body_content = ensure_resources_section(body_content)
        action = "updated"
        write_project_file(project_path, merged_metadata, body_content)
        return action, slug

    # No project file yet: only create if URL isn't already referenced elsewhere
    if norm_repo_url and norm_repo_url in existing_links_index:
        return "skipped-duplicate", slug

    new_metadata["status"] = derive_status(metadata)
    merged_metadata = merge_metadata({}, new_metadata)
    body_content = PAGE_TEMPLATE.strip()
    write_project_file(project_path, merged_metadata, body_content)
    return "created", slug


def main() -> None:
    created: List[str] = []
    updated: List[str] = []
    skipped: List[str] = []

    existing_links_index = index_existing_resource_links()

    for repo_path, post in load_repo_posts():
        metadata = post.metadata or {}
        if not repo_matches(metadata):
            continue

        action, slug = sync_project(metadata, repo_path, existing_links_index)
        if action == "created":
            created.append(slug)
            for res in build_resources(metadata):
                norm = normalize_repo_url(str(res.get("link", "")))
                if norm:
                    existing_links_index.setdefault(norm, PROJECT_DIR / f"{slug}.md")
        elif action == "updated":
            updated.append(slug)
        elif action == "skipped-duplicate":
            skipped.append(slug)

    summary = []
    if created:
        summary.append(f"created: {', '.join(created)}")
    if updated:
        summary.append(f"updated: {', '.join(updated)}")
    if skipped:
        summary.append(f"skipped-duplicate: {', '.join(skipped)}")
    if summary:
        print("Sync complete (" + "; ".join(summary) + ")")
    else:
        print("Sync complete (no matching repositories)")


if __name__ == "__main__":
    main()
