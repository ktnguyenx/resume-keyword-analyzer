SECTION_WEIGHTS = {
    "experience": 1.0,
    "projects": 0.9,
    "skills": 0.7,
    "education": 0.4,
    "general": 0.6,
}


def get_section_weight(section_name: str) -> float:
    return SECTION_WEIGHTS.get(section_name, 0.6)
