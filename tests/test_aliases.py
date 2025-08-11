from src.aliases import build_term_to_concept_map


def test_build_term_to_concept_map_maps_git_to_version_control():
    terms = {"git", "python", "machine learning"}
    term_map = build_term_to_concept_map(terms)

    assert term_map["git"] == "version control"
    assert term_map["python"] == "python"
    assert term_map["machine learning"] == "machine learning"
