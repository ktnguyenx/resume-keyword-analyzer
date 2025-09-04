from src.scorer import analyze_match


def test_analyze_match_tracks_concept_locations_and_score():
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

    resume_section_concepts = {
        "skills": {"python", "version control"},
        "projects": {"data analysis"},
    }

    results = analyze_match(
        resume_raw_terms,
        job_raw_terms,
        resume_term_map,
        job_term_map,
        resume_section_concepts,
    )

    assert "python" in results["matched_concepts"]
    assert "version control" in results["matched_concepts"]
    assert "machine learning" in results["missing_concepts"]
    assert "skills" in results["concept_locations"]["python"]
    assert results["match_score"] > 0
