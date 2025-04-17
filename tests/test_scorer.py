from src.scorer import analyze_match


def test_analyze_match_returns_weighted_scores():
    results = analyze_match(
        resume_keywords={"python", "git"},
        job_keywords={"python", "git", "sql"},
        resume_phrases={"data analysis"},
        job_phrases={"data analysis", "machine learning"},
        job_keyword_counts={"python": 2, "git": 1, "sql": 3},
        job_phrase_counts={"data analysis": 1, "machine learning": 2},
    )

    assert "match_score" in results
    assert "ranked_missing_keywords" in results
    assert "ranked_missing_phrases" in results
    assert "sql" in results["missing_keywords"]
    assert "machine learning" in results["missing_phrases"]
