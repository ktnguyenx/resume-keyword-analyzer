def analyze_match(
    resume_keywords: set[str],
    job_keywords: set[str],
    resume_phrases: set[str],
    job_phrases: set[str],
) -> dict:
    matched_keywords = resume_keywords & job_keywords
    missing_keywords = job_keywords - resume_keywords
    extra_keywords = resume_keywords - job_keywords

    matched_phrases = resume_phrases & job_phrases
    missing_phrases = job_phrases - resume_phrases

    keyword_score = (
        len(matched_keywords) / len(job_keywords) * 100 if job_keywords else 0
    )

    phrase_score = (
        len(matched_phrases) / len(job_phrases) * 100 if job_phrases else 0
    )

    total_score = round((0.7 * keyword_score) + (0.3 * phrase_score), 2)

    return {
        "resume_keywords": sorted(resume_keywords),
        "job_keywords": sorted(job_keywords),
        "matched_keywords": sorted(matched_keywords),
        "missing_keywords": sorted(missing_keywords),
        "extra_keywords": sorted(extra_keywords),
        "resume_phrases": sorted(resume_phrases),
        "job_phrases": sorted(job_phrases),
        "matched_phrases": sorted(matched_phrases),
        "missing_phrases": sorted(missing_phrases),
        "keyword_score": round(keyword_score, 2),
        "phrase_score": round(phrase_score, 2),
        "match_score": total_score,
    }
