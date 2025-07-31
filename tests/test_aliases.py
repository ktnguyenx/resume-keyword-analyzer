from src.aliases import normalize_terms


def test_normalize_terms_maps_git_to_version_control():
    terms = {"git", "python", "machine learning"}
    normalized = normalize_terms(terms)

    assert "version control" in normalized
    assert "git" not in normalized
    assert "python" in normalized
    assert "machine learning" in normalized
