SECTION_HEADERS = {
    "skills": "skills",
    "technical skills": "skills",
    "experience": "experience",
    "work experience": "experience",
    "professional experience": "experience",
    "projects": "projects",
    "project experience": "projects",
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
                existing = sections.get(current_section, "")
                new_text = "\n".join(buffer).strip()
                sections[current_section] = (
                    f"{existing}\n{new_text}".strip() if existing else new_text
                )
                buffer = []
            current_section = SECTION_HEADERS[normalized]
        else:
            buffer.append(line)

    if buffer:
        existing = sections.get(current_section, "")
        new_text = "\n".join(buffer).strip()
        sections[current_section] = (
            f"{existing}\n{new_text}".strip() if existing else new_text
        )

    return sections
