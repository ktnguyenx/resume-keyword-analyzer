def compute_keyword_overlap(resume_keywords: set[str], jd_keywords: set[str]) -> dict:
    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords.difference(resume_keywords)

    overlap_score = 0.0
    if jd_keywords:
        overlap_score = len(matched) / len(jd_keywords)

    return {
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
        "resume_keywords": sorted(resume_keywords),
        "job_keywords": sorted(jd_keywords),
        "overlap_score": round(overlap_score * 100, 2),
    }
