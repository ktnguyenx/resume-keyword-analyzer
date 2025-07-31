SECTION_HEADERS = {
    "skills": "skills",
    "technical skills": "skills",
    "experience": "experience",
    "work experience": "experience",
    "projects": "projects",
    "education": "education",
}


def split_into_sections(text: str) -> dict[str, str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    sections = {}
    current_section = "general"
    buffer = []

    for line in lines:
        normalized = line.lower().rstrip(":")
        if normalized in SECTION_HEADERS:
            if buffer:
                sections[current_section] = "\n".join(buffer).strip()
                buffer = []
            current_section = SECTION_HEADERS[normalized]
        else:
            buffer.append(line)

    if buffer:
        sections[current_section] = "\n".join(buffer).strip()

    return sections
