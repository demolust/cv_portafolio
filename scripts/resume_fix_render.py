import re


def process_resume(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    skill_buffer = []

    in_skills = False
    in_exp = False

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')
        stripped_line = line.strip()

        if line.startswith("## Skills"):
            in_skills = True
            in_exp = False
        elif line.startswith("## Experience"):
            in_exp = True
            in_skills = False

        if in_skills and re.match(r'^```.+```$', stripped_line):
            skill_buffer.append(stripped_line)
            i += 1
            continue

        if skill_buffer:
            output_lines.append(" ".join(skill_buffer))
            skill_buffer = []

        if in_exp and line.startswith("### ") and not line.startswith("### <span"):
            company = line[4:]

            if i + 1 < len(lines):
                next_line = lines[i + 1].rstrip('\n')

                if next_line.startswith("##### "):
                    raw_data = next_line[6:]

                    parts = raw_data.split(", ")

                    if len(parts) >= 2:
                        title = parts[0]
                        date_str = parts[1]

                        location = ", ".join(parts[2:]) if len(parts) > 2 else ""

                        formatted_company = f'### <span class="left">{company}</span> <span class="right">{location}</span>'
                        formatted_role = f'##### <span class="left">{title}</span> <span class="right">{date_str}</span>'

                        output_lines.append(formatted_company)
                        output_lines.append(formatted_role)

                        i += 2
                        continue

        output_lines.append(line)
        i += 1

    if skill_buffer:
        output_lines.append(" ".join(skill_buffer))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines) + '\n')


if __name__ == "__main__":
    process_resume("resume.md", "resume_fixed.md")
