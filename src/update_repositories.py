import os
import requests
from pathlib import Path
from datetime import datetime, timedelta
import yaml

ORG_NAME = "digital-work-lab"
BASE_URL = "https://api.github.com"
workflow_filename = ".github/workflows/labot.yml"

PROJECT_PAGE = """
# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Title               | {{ page.title_long }}
Status              | {{ page.status }}
Improvement         | {{ page.improvement_status }}
Started             | {{ page.started }}
Completed           | {{ page.completed }}

{% if page.resources %}
## Resources

  {% for output in page.resources %}
  - [{{ output.name }}]({{ output.link }}){: target="_blank"}
  {% endfor %}
{% endif %}

{% if page.outputs %}
## Outputs

  {% for output in page.outputs %}
  - [{{ output.type }}]({{ output.link }}){: target="_blank"}
  {% endfor %}
{% endif %}

{% if page.related %}
## Related projects 

- {% for item in page.related %}
  - <a href="{{ item }}">{{ item }}</a>
{% endfor %}
{% endif %}"""

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
archived: {repo_data['archived']}
updated_recently: {repo_data['updated_recently']}
associated_projects: []
labot_workflow_status: {repo_data['labot_workflow_status']}
project_type: {repo_data['project_type']}
---

# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Title               | {{ page.title_long }}
Visibility          | {{ page.visibility }}
Collaborators       | {{ page.collaborators }}
Topics              | {{ page.topics }}
URL                 | [Repository Link]({repo_data['html_url']}){{: target="_blank"}}

[![Request Access](https://img.shields.io/badge/Request-Access-blue?style=for-the-badge)]({repo_data['html_url']}/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository)

"""

    with open(file_path, 'w') as file:
        file.write(yaml_header)

def get_project_type(owner, repo_name):
    """Check the project type."""
    repo_contents_url = f"{BASE_URL}/repos/{owner}/{repo_name}/contents"
    response = requests.get(repo_contents_url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Error fetching repository contents: {response.json()}")
        return []

    contents = response.json()
    print(contents)
    file_names = [content['name'] for content in contents]
    p_types = []
    if 'paper.md' in file_names:
        p_types.append('paper')
    if 'settings.json' in file_names and 'status.yaml' in file_names:
        p_types.append('colrev')
    return p_types

def export_project(repo_data: dict):

    # if repo_data["name"] != "lrdm":
    #     return

    HEADERS = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
    }

    # url = f"{repo_data['html_url']}/refs/heads/main/paper.md"
    url = f"https://raw.githubusercontent.com/{ORG_NAME}/{repo_data['name']}/main/paper.md"
    print(url)
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error fetching paper.md: {response.status_code} - {response.text}")
        return

    try:
        paper_md_content = response.text
        # get the yaml header in the md:
        yaml_header = paper_md_content.split("---")[1]
        # parse dict
        paper_data = yaml.safe_load(yaml_header)

        # write to repo_data["name"].md file
        # select paper_data["project"]
        # write to _projects
        cwd = Path.cwd()
        output_dir = cwd / "_projects"
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        file_name = f"{repo_data['name']}.md"
        file_path = os.path.join(output_dir, file_name)
        title_long = ""
        if paper_data['project']['status'] == "published":
            title_long = paper_data['title']
        yaml_header = f"""---
layout: default
title: {paper_data['project']['abbreviation']}
title_long: "{title_long}"
parent: 25 Projects
grand_parent: Research
started: {paper_data['project']['started']}
area: {paper_data['project']['area']}
resources: {paper_data['project'].get('resources', [])}
status: {paper_data['project']['status']}
improvement_status: {paper_data['project']['improvement_status']}
topics: {repo_data['topics']}
repository_url: {repo_data['html_url']}
archived: {repo_data['archived']}
updated_recently: {repo_data['updated_recently']}
associated_projects: []
labot_workflow_status: {repo_data['labot_workflow_status']}
project_type: {repo_data['project_type']}
---
"""
        # write yaml_header to file
        with open(file_path, 'w') as file:
            file.write(yaml_header)
            file.write(PROJECT_PAGE)

    except ValueError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Response content: {response.text}")
    except KeyError as e:
        print(f"KeyError: {e}")

def main():
    repos = get_org_repositories(ORG_NAME)
    cwd = Path.cwd()
    output_dir = cwd / "_repos"

    lycheeignore_path = cwd / ".lycheeignore"
    six_months_ago = datetime.now() - timedelta(days=180)

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for file in Path(output_dir).glob("*"):
        print(f"Removing {file}")
        file.unlink()

    # print contents of output_dir
    print(f"Contents of {output_dir}:")
    for file in Path(output_dir).glob("*"):
        print(f"  {file}")

    for repo in repos:
        if repo["html_url"] in ["https://github.com/digital-work-lab/digital-work-lab.github.io"]:
            print(f"Skipping {repo['name']}")
            continue
        workflow_id = get_workflow_id_by_filename(ORG_NAME, repo['name'], workflow_filename)
        print(workflow_id)
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
        create_markdown_file(repo_data, output_dir)
        
        if "paper" in repo_data["project_type"]:
            export_project(repo_data)

        # append repo_data["html_url"] to .lycheeignore if it's not already there
        with open(lycheeignore_path, 'r') as file:
            lycheeignore = file.read()
            if repo_data["html_url"] not in lycheeignore:
                with open(lycheeignore_path, 'a') as file:
                    file.write(f"\n{repo_data['html_url']}")

    print(f"Markdown files created in {output_dir}")

    # print contents of output_dir
    print(f"Contents of {output_dir}:")
    for file in Path(output_dir).glob("*"):
        print(f"  {file}")




if __name__ == "__main__":
    main()
