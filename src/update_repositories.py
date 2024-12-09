import os
import requests
from pathlib import Path

ORG_NAME = "digital-work-lab"
BASE_URL = "https://api.github.com"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise EnvironmentError("The GITHUB_TOKEN environment variable is not set or empty.")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.mercy-preview+json"
}

def get_org_repositories(org_name):
    url = f"{BASE_URL}/orgs/{org_name}/repos"
    repositories = []
    page = 1

    while True:
        response = requests.get(url, headers=HEADERS, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            raise Exception(f"Error fetching repositories: {response.json()}")
        
        repos = response.json()
        if not repos:
            break

        repositories.extend(repos)
        page += 1

    return repositories

def get_repo_collaborators(owner, repo_name):
    url = f"{BASE_URL}/repos/{owner}/{repo_name}/collaborators"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 403:
        return ["Access Denied: Requires admin rights"]
    elif response.status_code != 200:
        return []

    return [collab['login'] for collab in response.json() if collab['login'] != "geritwagner"]

def create_markdown_file(repo_data, output_dir):
    """Creates a markdown file with YAML front matter."""
    file_name = f"{repo_data['name']}.md"
    file_path = os.path.join(output_dir, file_name)
    yaml_header = f"""---
layout: default
title: {repo_data['name']}
title_long: "{repo_data['description'] or repo_data['name']}"
parent: Projects
grand_parent: Research
visibility: {repo_data['visibility']}
collaborators: {repo_data['collaborators']}
area: {repo_data['area']}
topics: {repo_data['topics']}
html_url: {repo_data['html_url']}
associated_projects: []
---

# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Title               | {{ page.title_long }}
Visibility          | {{ page.visibility }}
Collaborators       | {{ page.collaborators }}
Topics              | {{ page.topics }}
URL                 | [Repository Link]({repo_data['html_url']})

[![Request Access](https://img.shields.io/badge/Request-Access-blue?style=for-the-badge)]({repo_data['html_url']}/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository)

"""

    with open(file_path, 'w') as file:
        file.write(yaml_header)

def main():
    repos = get_org_repositories(ORG_NAME)
    output_dir = "_repos"

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for repo in repos:
        print(f"Processing {repo['name']}...")
        area = "other"
        if "research" in repo["topics"]:
            area = "research"
        elif "teaching" in repo["topics"]:
            area = "teaching"

        repo_data = {
            "name": repo["name"],
            "html_url": repo["html_url"],
            "visibility": "Private" if repo["private"] else "Public",
            "description": repo.get("description", ""),
            "area": area,
            "topics": repo["topics"],
            "created_at": repo["created_at"],
            "collaborators": get_repo_collaborators(ORG_NAME, repo["name"])
        }
        create_markdown_file(repo_data, output_dir)

    print(f"Markdown files created in {output_dir}")

if __name__ == "__main__":
    main()
