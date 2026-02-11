import yaml


def load_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def render_header(data):
    p = data.get('personalInfo', {})

    md = f"---\ntitle: {p.get('fullName', 'Resume')}\n---\n"

    links = []

    if 'github' in p:
        username = p['github'].get('username')
        links.append(f"[ [Github](https://www.github.com/{username}) ]")

    if 'linkedin' in p:
        url = p['linkedin'].get('url')
        links.append(f"[ [LinkedIn]({url}) ]")

    if 'email' in p:
        email = p.get('email')
        links.append(f"[ [{email}](mailto:{email}) ]")

    if 'phone' in p:
        phone = p.get('phone')
        links.append(f"[ [{phone}](tel:{phone}) ]")

    if 'location' in p:
        location = p.get('location')
        links.append(f"[ {location} ]")

    if links:
        md += f"###### {' - '.join(links)}\n\n"

    if 'summary' in p:
        md += f"{p['summary']}\n\n"

    return md


def render_experience_item(item):
    md = f"### {item.get('company', '')}\n"

    details = [item.get('position'), item.get('years'), item.get('location')]
    details = [d for d in details if d]  # Filter empty
    md += f"##### {', '.join(details)}\n"

    if 'position_summary' in item:
        md += f"{item['position_summary']}\n\n"

    if 'key_acomplishments' in item:
        for acc in item['key_acomplishments']:
            md += f"- {acc}\n"

    md += "\n"
    return md


def render_education_item(item):
    md = f"### {item.get('college', '')}\n"

    parts = []
    if 'title' in item:
        parts.append(f"**Degree:** {item['title']}")
    if 'dates' in item:
        parts.append(f"**Years Attended:** {item['dates']}")
    if 'location' in item:
        parts.append(f"**State, Country:** {item['location']}")

    md += " | ".join(parts) + "\n\n"
    return md


def render_project_item(item):
    title = item.get('title', 'Project')
    url = item.get('url', '')

    if url:
        md = f"### [{title}]({url})\n"
    else:
        md = f"### {title}\n"

    if 'project_summary' in item:
        md += f"{item['project_summary']}\n\n"
    elif 'description' in item:
        md += f"{item['description']}\n\n"

    return md


def render_certification_item(item):
    name = item.get('name', '')
    issuer = item.get('issuer', '')
    year = item.get('year', '')

    line = f"- {name}"
    if issuer:
        line += f" — {issuer}"
    if year:
        line += f" ({year})"
    return line + "\n"


def render_article_item(item):
    title = item.get('title', '')
    url = item.get('url', '#')
    date = item.get('date', '')

    return f"- [{title}]({url}) ({date})\n"


def render_sections(data):
    md = ""
    sections = data.get('sections', [])

    for section in sections:
        title = section.get('title', 'Section')
        s_type = section.get('type', 'text')
        items = section.get('items', [])

        md += f"## {title}\n"

        if s_type == 'work':
            for item in items:
                md += render_experience_item(item)
        elif s_type == 'education':
            for item in items:
                md += render_education_item(item)
        elif s_type == 'projects':
            for item in items:
                md += render_project_item(item)
        elif s_type == 'certification':
            for item in items:
                md += render_certification_item(item)
            md += "\n"
        elif s_type == 'articles':
            for item in items:
                md += render_article_item(item)
            md += "\n"
        else:
            for item in items:
                if isinstance(item, str):
                    md += f"- {item}\n"
            md += "\n"

    return md


def render_skills(data):
    md = "## Skills\n"
    skills = data.get('sidebarSkills', [])

    for group in skills:
        md += f"### {group.get('subheader', '')}\n"
        items = group.get('items', [])

        is_key_value = any(':' in str(i) for i in items)

        if is_key_value:
            for item in items:
                if ':' in item:
                    key, val = item.split(':', 1)
                    md += f"**{key}**:{val}\n"
                else:
                    md += f"{item}\n"
        else:
            for item in items:
                md += f"```{item}```\n"

        md += "\n"
    return md


def render_sidebar_sections(data):
    md = ""
    sidebar_sections = data.get('sidebarSections', [])

    for section in sidebar_sections:
        if section.get('type') == 'languages':
            items = section.get('items', [])
            md += f"**{section.get('title')}**: {', '.join(items)}\n\n"
        else:
            md += f"### {section.get('title')}\n"
            for item in section.get('items', []):
                md += f"- {item}\n"
            md += "\n"

    return md


def main():
    input_file = 'resume.yaml'
    output_file = 'resume.md'

    try:
        data = load_yaml(input_file)

        markdown_content = ""
        markdown_content += render_header(data)
        markdown_content += render_sections(data)
        markdown_content += render_skills(data)
        markdown_content += render_sidebar_sections(data)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

    except FileNotFoundError:
        print(f"Error: Could not find {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
