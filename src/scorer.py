def analyze_match(
    resume_raw_terms: set[str],
    job_raw_terms: set[str],
    resume_term_map: dict[str, str],
    job_term_map: dict[str, str],
) -> dict:
    resume_concepts = set(resume_term_map.values())
    job_concepts = set(job_term_map.values())

    matched_concepts = resume_concepts & job_concepts
    missing_concepts = job_concepts - resume_concepts
    extra_concepts = resume_concepts - job_concepts

    exact_matches = sorted(resume_raw_terms & job_raw_terms)

    alias_inferred_matches = []
    for job_term, concept in job_term_map.items():
        if concept in matched_concepts and job_term not in resume_raw_terms:
            matching_resume_terms = sorted(
                term for term, mapped in resume_term_map.items()
                if mapped == concept
            )
            if matching_resume_terms:
                alias_inferred_matches.append({
                    "job_term": job_term,
                    "concept": concept,
                    "matched_by": matching_resume_terms,
                })

    alias_inferred_matches = sorted(
        alias_inferred_matches,
        key=lambda item: (item["concept"], item["job_term"])
    )

    match_score = (len(matched_concepts) / len(job_concepts) * 100) if job_concepts else 0.0

    return {
        "exact_matches": exact_matches,
        "alias_inferred_matches": alias_inferred_matches,
        "matched_concepts": sorted(matched_concepts),
        "missing_concepts": sorted(missing_concepts),
        "extra_concepts": sorted(extra_concepts),
        "match_score": round(match_score, 2),
    }
