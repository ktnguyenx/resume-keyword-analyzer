from src.phrases import extract_phrases


def test_extract_phrases_finds_known_skill_phrases():
    text = "Worked on machine learning and natural language processing projects."
    phrases = extract_phrases(text)

    assert "machine learning" in phrases
    assert "natural language processing" in phrases
