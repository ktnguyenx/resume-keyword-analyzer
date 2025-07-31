def analyze_match(resume_terms: set[str], job_terms: set[str]) -> dict:
    matched_terms = resume_terms & job_terms
    missing_terms = job_terms - resume_terms
    extra_terms = resume_terms - job_terms

    match_score = (len(matched_terms) / len(job_terms) * 100) if job_terms else 0.0

    ranked_missing_terms = sorted(missing_terms)
    ranked_matched_terms = sorted(matched_terms)

    return {
        "matched_terms": sorted(matched_terms),
        "missing_terms": sorted(missing_terms),
        "extra_terms": sorted(extra_terms),
        "ranked_missing_terms": ranked_missing_terms,
        "ranked_matched_terms": ranked_matched_terms,
        "match_score": round(match_score, 2),
    }
