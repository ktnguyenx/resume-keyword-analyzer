from src.section_weights import get_section_weight


def find_concept_locations(
    matched_concepts: set[str],
    resume_section_concepts: dict[str, set[str]],
) -> dict[str, list[str]]:
    concept_locations = {}

    for concept in matched_concepts:
        locations = [
            section_name
            for section_name, concepts in resume_section_concepts.items()
            if concept in concepts
        ]
        concept_locations[concept] = sorted(locations)

    return concept_locations


def compute_weighted_match_score(
    job_concepts: set[str],
    concept_locations: dict[str, list[str]],
) -> float:
    if not job_concepts:
        return 0.0

    total_possible = len(job_concepts)
    score_sum = 0.0

    for concept in job_concepts:
        locations = concept_locations.get(concept, [])
        if locations:
            best_weight = max(get_section_weight(location) for location in locations)
            score_sum += best_weight

    return round((score_sum / total_possible) * 100, 2)


def analyze_match(
    resume_raw_terms: set[str],
    job_raw_terms: set[str],
    resume_term_map: dict[str, str],
    job_term_map: dict[str, str],
    resume_section_concepts: dict[str, set[str]],
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

    concept_locations = find_concept_locations(
        matched_concepts,
        resume_section_concepts,
    )

    match_score = compute_weighted_match_score(job_concepts, concept_locations)

    return {
        "exact_matches": exact_matches,
        "alias_inferred_matches": alias_inferred_matches,
        "matched_concepts": sorted(matched_concepts),
        "missing_concepts": sorted(missing_concepts),
        "extra_concepts": sorted(extra_concepts),
        "concept_locations": concept_locations,
        "match_score": match_score,
    }
