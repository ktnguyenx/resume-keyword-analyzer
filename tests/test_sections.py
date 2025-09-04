from src.sections import split_into_sections


def test_split_into_sections_recognizes_common_headers():
    text = """
    Skills:
    Python, Git

    Experience:
    Built data tools

    Projects:
    Resume analyzer app
    """

    sections = split_into_sections(text)

    assert "skills" in sections
    assert "experience" in sections
    assert "projects" in sections
