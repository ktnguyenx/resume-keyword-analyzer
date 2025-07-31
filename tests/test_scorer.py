from src.scorer import analyze_match


def test_analyze_match_concept_level():
    resume_terms = {"python", "version control", "data analysis"}
    job_terms = {"python", "version control", "machine learning"}

    results = analyze_match(resume_terms, job_terms)

    assert "python" in results["matched_terms"]
    assert "version control" in results["matched_terms"]
    assert "machine learning" in results["missing_terms"]
