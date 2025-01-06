import os
import requests
from pathlib import Path
from datetime import datetime, timedelta
import yaml

ORG_NAME = "digital-work-lab"
BASE_URL = "https://api.github.com"
workflow_filename = ".github/workflows/labot.yml"
cwd = Path.cwd()
OUTPUT_DIR = cwd / "_repos"




GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise EnvironmentError("The GITHUB_TOKEN environment variable is not set or empty.")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.mercy-preview+json"
}

def get_workflow_id_by_filename(owner, repo_name, workflow_filename):
    """Gets the workflow ID for a specific workflow file in the repository."""
    url = f"{BASE_URL}/repos/{owner}/{repo_name}/actions/workflows"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Error fetching workflows: {response.json()}")
    
    workflows = response.json().get('workflows', [])
    for workflow in workflows:
        if workflow['path'].lower() == workflow_filename.lower():  # Matching by filename
            return workflow['id']

    return None  # Return None if the workflow is not found

def get_workflow_status(owner, repo_name, workflow_id):
    """Fetches the status of the latest workflow run."""
    if workflow_id is None:
        return "not-found"
    url = f"{BASE_URL}/repos/{owner}/{repo_name}/actions/workflows/{workflow_id}/runs"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Error fetching workflow runs: {response.json()}")
    
    runs = response.json().get('workflow_runs', [])
    if not runs:
        return "No runs found"

    # You can filter the runs to get the latest one
    latest_run = runs[0]  # Most recent run
    status = latest_run['status']  # Can be 'queued', 'in_progress', 'completed'
    conclusion = latest_run.get('conclusion', 'No conclusion')  # 'success', 'failure', 'neutral', etc.
    
    return conclusion

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


def get_project_type(owner, repo_name):
    """Check the project type."""
    repo_contents_url = f"{BASE_URL}/repos/{owner}/{repo_name}/contents"
    response = requests.get(repo_contents_url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Error fetching repository contents: {response.json()}")
        return []

    contents = response.json()
    file_names = [content['name'] for content in contents]
    p_types = []
    if 'paper.md' in file_names:
        p_types.append('paper')
    if 'settings.json' in file_names and 'status.yaml' in file_names:
        p_types.append('colrev')
    return p_types

def generate_default_yaml_header(repo_data):
    """Generates the default YAML header for a repository."""
    return f"""---
layout: default
title: {repo_data['name']}
title_long: "{repo_data['title_long']}"
parent: 25 Projects
grand_parent: Research
visibility: {repo_data['visibility']}
collaborators: {repo_data['collaborators']}
area: {repo_data['area']}
topics: {repo_data['topics']}
html_url: {repo_data['html_url']}
archived: {repo_data['archived']}
updated_recently: {repo_data['updated_recently']}
associated_projects: []
labot_workflow_status: {repo_data['labot_workflow_status']}
project_type: {repo_data['project_type']}"""

def generate_paper_specific_yaml_header(paper_data, repo_data):
    """Generates additional YAML header content for paper-specific projects."""
    return f"""
started: {paper_data['project']['started']}
area: {paper_data['project']['area']}
resources: {paper_data['project'].get('resources', [])}
status: {paper_data['project']['status']}
improvement_status: {paper_data['project']['improvement_status']}
repository_url: {repo_data['html_url']}
---
"""

def generate_markdown_content(yaml_header, markdown_body):
    """Combines YAML header and markdown body to create the complete content."""
    return yaml_header + markdown_body

def create_markdown_file(repo_data, content):
    """Writes the markdown content to a file."""
    file_name = f"{repo_data['name']}.md"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(content)

def fetch_paper_data(repo_data):
    """Fetches paper.md content for a repository."""
    HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    url = f"https://raw.githubusercontent.com/{ORG_NAME}/{repo_data['name']}/main/paper.md"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error fetching paper.md: {response.status_code} - {response.text}")
        return None
    return response.text

def process_repo(repo_data):
    """Processes a repository to create its markdown file."""
    if "paper" in repo_data["project_type"]:
        paper_content = fetch_paper_data(repo_data)
        paper_data = {}
        if paper_content:
            try:
                paper_yaml_header = paper_content.split("---")[1]
                paper_data = yaml.safe_load(paper_yaml_header)
                title_long = paper_data['title'] if paper_data['project']['status'] == "published" else ""
            except Exception as e:
                print(f"Error processing paper.md: {e}")
                title_long = "ERROR"

        else:
            title_long = "ERROR"
    else:
        title_long = repo_data["description"]
    repo_data["title_long"] = title_long

    yaml_header = generate_default_yaml_header(repo_data)

    if "paper" in repo_data["project_type"]:
        try:
            yaml_header += generate_paper_specific_yaml_header(paper_data, repo_data)
        except Exception as e:
            print(f"Error processing paper.md: {e}")

    yaml_header += "\n---\n"

    markdown_body = f"""
# {{{{ page.title }}}}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{{{ page.title }}}}
Title               | {{{{ page.title_long }}}}
Visibility          | {{{{ page.visibility }}}}
Access              | {{{{ page.collaborators topics | join: ", "}}}}
Topics              | {{{{ page.topics | join: ", " }}}}
URL                 | [{repo_data['html_url']}]({repo_data['html_url']}){{: target="_blank"}}

[![Request Access](https://img.shields.io/badge/Request-Access-blue?style=for-the-badge)](https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository)
"""

    content = generate_markdown_content(yaml_header, markdown_body)
    create_markdown_file(repo_data, content)

def main():
    repos = get_org_repositories(ORG_NAME)

    lycheeignore_path = cwd / ".lycheeignore"
    six_months_ago = datetime.now() - timedelta(days=180)

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    for file in Path(OUTPUT_DIR).glob("*"):
        print(f"Removing {file}")
        file.unlink()

    # print contents of OUTPUT_DIR
    print(f"Contents of {OUTPUT_DIR}:")
    for file in Path(OUTPUT_DIR).glob("*"):
        print(f"  {file}")

    for repo in repos:
        if repo["html_url"] in ["https://github.com/digital-work-lab/digital-work-lab.github.io"]:
            print(f"Skipping {repo['name']}")
            continue
        workflow_id = get_workflow_id_by_filename(ORG_NAME, repo['name'], workflow_filename)
        labot_workflow_status = get_workflow_status(ORG_NAME, repo['name'], workflow_id)

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
            "archived": repo["archived"],
            "collaborators": get_repo_collaborators(ORG_NAME, repo["name"]),
            "updated_recently": datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ") > six_months_ago,
            "labot_workflow_status": labot_workflow_status,
            "project_type": get_project_type(ORG_NAME, repo["name"])
        }
        if "paper" in repo_data["topics"] and 'paper' not in repo_data['project_type']:
            repo_data["project_type"].append("paper")
        if not("paper" in repo_data['project_type'] or "teaching-materials" in repo_data['topics']):
            repo_data["labot_workflow_status"] = "not-applicable"

        process_repo(repo_data)

        # append repo_data["html_url"] to .lycheeignore if it's not already there
        with open(lycheeignore_path, 'r') as file:
            lycheeignore = file.read()
            if repo_data["html_url"] not in lycheeignore:
                with open(lycheeignore_path, 'a') as file:
                    file.write(f"\n{repo_data['html_url']}")

    print(f"Markdown files created in {OUTPUT_DIR}")

    # print contents of OUTPUT_DIR
    print(f"Contents of {OUTPUT_DIR}:")
    for file in Path(OUTPUT_DIR).glob("*"):
        print(f"  {file}")




if __name__ == "__main__":
    main()
