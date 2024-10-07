from pathlib import Path
import re


# Regular expression to match markdown links that start with http and may or may not have a {...} block
markdown_link_pattern = re.compile(r'(\[([^\]]+)\]\((http[^\)]+)\))(\{[^}]*\})?')

def append_target_blank_to_links(file_path):
    # Read the content of the file
    content = file_path.read_text(encoding='utf-8')

    # Function to modify the markdown link and add target="_blank"
    def add_target_blank(match):
        link = match.group(1)  # Full markdown link [text](url)
        url = match.group(3)  # Extracted URL from the link
        existing_attrs = match.group(4)  # Existing {...} attributes block

        # Skip the modification if the link contains "img.shields.io" (indicating a badge)
        if 'img.shields.io' in url or url.endswith('.png') or url.endswith('.svg'):
            return match.group(0)  # Return the original match without modification

        # If there's already a {...} block, append target="_blank" if not present
        if existing_attrs:
            if 'target="_blank"' not in existing_attrs:
                # Add target="_blank" within the existing {...} block
                updated_attrs = existing_attrs.rstrip(' }') + ' target="_blank" }'
                return link + updated_attrs
            else:
                return link + existing_attrs
        else:
            # If no {...} block exists, add one with target="_blank"
            return link + '{: target="_blank"}'

    # Apply the function to all matches found in the file content
    updated_content = markdown_link_pattern.sub(add_target_blank, content)
    
    # Write back the updated content if changes were made
    if updated_content != content:
        file_path.write_text(updated_content, encoding='utf-8')
        print(f'Updated links in {file_path}')
    else:
        print(f'No changes needed in {file_path}')

def link_check():
    directory = Path.cwd()
    for file_path in directory.glob('**/*.md'):
        print(file_path)
        if file_path in ["README.md"]:
            continue
        append_target_blank_to_links(file_path)

if __name__ == "__main__":
    link_check()