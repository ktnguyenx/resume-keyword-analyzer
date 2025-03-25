def analyze_match(resume_keywords: set[str], job_keywords: set[str]) -> dict:
    matched = resume_keywords & job_keywords
    missing = job_keywords - resume_keywords
    extra = resume_keywords - job_keywords

    if not job_keywords:
        score = 0.0
    else:
        score = (len(matched) / len(job_keywords)) * 100

    return {
        "resume_keywords": sorted(resume_keywords),
        "job_keywords": sorted(job_keywords),
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
        "extra_keywords": sorted(extra),
        "match_score": round(score, 2),
    }
