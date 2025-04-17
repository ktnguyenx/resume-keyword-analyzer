from src.weights import get_keyword_weight, get_phrase_weight


def analyze_match(
    resume_keywords: set[str],
    job_keywords: set[str],
    resume_phrases: set[str],
    job_phrases: set[str],
    job_keyword_counts: dict[str, int],
    job_phrase_counts: dict[str, int],
) -> dict:
    matched_keywords = resume_keywords & job_keywords
    missing_keywords = job_keywords - resume_keywords
    extra_keywords = resume_keywords - job_keywords

    matched_phrases = resume_phrases & job_phrases
    missing_phrases = job_phrases - resume_phrases

    keyword_weights = {
        kw: get_keyword_weight(kw, job_keyword_counts.get(kw, 1))
        for kw in job_keywords
    }

    phrase_weights = {
        ph: get_phrase_weight(ph, job_phrase_counts.get(ph, 1))
        for ph in job_phrases
    }

    total_keyword_weight = sum(keyword_weights.values())
    matched_keyword_weight = sum(keyword_weights[kw] for kw in matched_keywords)

    total_phrase_weight = sum(phrase_weights.values())
    matched_phrase_weight = sum(phrase_weights[ph] for ph in matched_phrases)

    keyword_score = (
        (matched_keyword_weight / total_keyword_weight) * 100
        if total_keyword_weight else 0
    )

    phrase_score = (
        (matched_phrase_weight / total_phrase_weight) * 100
        if total_phrase_weight else 0
    )

    total_score = round((0.65 * keyword_score) + (0.35 * phrase_score), 2)

    ranked_missing_keywords = sorted(
        missing_keywords,
        key=lambda kw: keyword_weights.get(kw, 0),
        reverse=True
    )

    ranked_missing_phrases = sorted(
        missing_phrases,
        key=lambda ph: phrase_weights.get(ph, 0),
        reverse=True
    )

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
        "keyword_weights": keyword_weights,
        "phrase_weights": phrase_weights,
        "ranked_missing_keywords": ranked_missing_keywords,
        "ranked_missing_phrases": ranked_missing_phrases,
    }
