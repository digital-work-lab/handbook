import yamale
from pathlib import Path
import sys

VALID = True


def check_collections(files_path, schema_path):
    global VALID
    schema = yamale.make_schema(schema_path)
    course_files = Path(files_path).rglob("*.md")

    for course_file in course_files:
        try:
            # Extract YAML header and validate
            yaml_header = course_file.read_text().split("---")[1]
            data = yamale.make_data(content=yaml_header)
            data[0][0]["filename"] = course_file.name
            yamale.validate(schema, data)
            print(f"{course_file} is valid")
        except Exception as e:
            print(f"{course_file} is invalid")
            print(e)
            VALID = False

    # TODO : validate remaining content in md files


if __name__ == "__main__":
    check_collections("./_courses", "src/yaml_schema_course.yaml")
    # TODO : schema for repos
    check_collections("./_projects", "src/yaml_schema_projects.yaml")

    # TODO : repository names!

    if VALID:
        sys.exit(0)  # Exit with success code
    else:
        sys.exit(1)  # Exit with failure code
