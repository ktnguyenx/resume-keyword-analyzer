from rapidfuzz import fuzz


def find_fuzzy_matches(
    resume_concepts: set[str],
    job_concepts: set[str],
    threshold: int = 85,
) -> list[dict]:
    matches = []

    exact_overlap = resume_concepts & job_concepts

    for job_concept in job_concepts:
        if job_concept in exact_overlap:
            continue

        best_resume_concept = None
        best_score = 0

        for resume_concept in resume_concepts:
            if resume_concept in exact_overlap:
                continue

            score = fuzz.token_sort_ratio(resume_concept, job_concept)
            if score > best_score:
                best_score = score
                best_resume_concept = resume_concept

        if best_resume_concept and best_score >= threshold:
            matches.append({
                "job_concept": job_concept,
                "resume_concept": best_resume_concept,
                "score": best_score,
            })

    return sorted(matches, key=lambda x: x["score"], reverse=True)
