from src.fuzzy_match import find_fuzzy_matches


def test_find_fuzzy_matches_returns_close_matches():
    resume_concepts = {"data analysis", "python", "version control"}
    job_concepts = {"data analytic", "python"}

    matches = find_fuzzy_matches(resume_concepts, job_concepts, threshold=80)

    assert any(item["job_concept"] == "data analytic" for item in matches)
