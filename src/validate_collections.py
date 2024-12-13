import yamale
from pathlib import Path
import sys

VALID = True

def check_collections(files_path, schema_path):
    global VALID
    schema = yamale.make_schema(schema_path)
    course_files = Path(files_path).rglob('*.md')
    
    for course_file in course_files:
        try:
            # Extract YAML header and validate
            yaml_header = course_file.read_text().split('---')[1]
            data = yamale.make_data(content=yaml_header)
            data[0][0]["filename"] = course_file.name
            yamale.validate(schema, data)
            print(f'{course_file} is valid')
        except Exception as e:
            print(f'{course_file} is invalid')
            print(e)
            VALID = False
    
    # TODO : validate remaining content in md files

def check_dangling_repos():
    global VALID
    # Check if all repos are mentioned in the course files
    repos = Path('./_repos').rglob('*.md')
    repos = [repo_file.stem for repo_file in repos]

    repo_urls = []
    for repo in repos:
        repo_file = Path(f'./_repos/{repo}.md')
        repo_content = repo_file.read_text()
        # get yaml header, resources and links
        yaml_header = repo_content.split('---')[1]
        data = yamale.make_data(content=yaml_header)
        if data[0][0]["area"] == "research":
            if "paper" in data[0][0]["topics"]:
                repo_urls.append(data[0][0]["html_url"])

    projects = Path('./_projects').rglob('*.md')
    projects = [project_file.stem for project_file in projects]
    
    linked_repos = []
    for project in projects:
        project_file = Path(f'./_projects/{project}.md')
        project_content = project_file.read_text()
        # get yaml header, resources and links
        yaml_header = project_content.split('---')[1]
        data = yamale.make_data(content=yaml_header)
        for resource in data[0][0].get("resources", []):
            if resource["link"].startswith("https://github.com/"):
                linked_repos.append(resource["link"])
    
    dangling_repos = list(set(repo_urls) - set(linked_repos))
    if len(dangling_repos) > 0:
        print("Dangling paper repositories (not linked in projects):")
        for repo in dangling_repos:
            print(repo)
        VALID = False

if __name__ == "__main__":

    check_collections('./_courses', 'src/yaml_schema_course.yaml')
    check_collections('./_projects', 'src/yaml_schema_projects.yaml')

    check_dangling_repos()

    # TODO : repository names!

    if VALID:
        sys.exit(0)  # Exit with success code
    else:
        sys.exit(1)  # Exit with failure code
