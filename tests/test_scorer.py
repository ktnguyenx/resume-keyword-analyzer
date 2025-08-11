from src.scorer import analyze_match


def test_analyze_match_separates_exact_and_alias_matches():
    resume_raw_terms = {"git", "python", "data analysis"}
    job_raw_terms = {"version control", "python", "machine learning"}

    resume_term_map = {
        "git": "version control",
        "python": "python",
        "data analysis": "data analysis",
    }

    job_term_map = {
        "version control": "version control",
        "python": "python",
        "machine learning": "machine learning",
    }

    results = analyze_match(
        resume_raw_terms,
        job_raw_terms,
        resume_term_map,
        job_term_map,
    )

    assert "python" in results["exact_matches"]
    assert "version control" in results["matched_concepts"]
    assert "machine learning" in results["missing_concepts"]
    assert len(results["alias_inferred_matches"]) >= 1
