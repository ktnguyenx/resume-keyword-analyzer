from src.fuzzy_match import find_fuzzy_matches
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
    fuzzy_matches: list[dict],
    include_fuzzy_in_score: bool = True,
) -> float:
    if not job_concepts:
        return 0.0

    total_possible = len(job_concepts)
    score_sum = 0.0

    fuzzy_job_concepts = {item["job_concept"] for item in fuzzy_matches}

    for concept in job_concepts:
        locations = concept_locations.get(concept, [])
        if locations:
            best_weight = max(get_section_weight(location) for location in locations)
            score_sum += best_weight
        elif include_fuzzy_in_score and concept in fuzzy_job_concepts:
            score_sum += 0.5

    return round((score_sum / total_possible) * 100, 2)


def analyze_match(
    resume_raw_terms: set[str],
    job_raw_terms: set[str],
    resume_term_map: dict[str, str],
    job_term_map: dict[str, str],
    resume_section_concepts: dict[str, set[str]],
    fuzzy_threshold: int = 85,
    include_fuzzy_in_score: bool = True,
) -> dict:
    resume_concepts = set(resume_term_map.values())
    job_concepts = set(job_term_map.values())

    exact_matches = sorted(resume_raw_terms & job_raw_terms)

    matched_concepts = resume_concepts & job_concepts
    fuzzy_matches = find_fuzzy_matches(
        resume_concepts,
        job_concepts,
        threshold=fuzzy_threshold,
    )

    fuzzy_job_concepts = {item["job_concept"] for item in fuzzy_matches}
    all_matched_job_concepts = matched_concepts | fuzzy_job_concepts

    missing_concepts = job_concepts - all_matched_job_concepts
    extra_concepts = resume_concepts - matched_concepts

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

    match_score = compute_weighted_match_score(
        job_concepts,
        concept_locations,
        fuzzy_matches,
        include_fuzzy_in_score=include_fuzzy_in_score,
    )

    return {
        "exact_matches": exact_matches,
        "alias_inferred_matches": alias_inferred_matches,
        "fuzzy_matches": fuzzy_matches,
        "matched_concepts": sorted(all_matched_job_concepts),
        "missing_concepts": sorted(missing_concepts),
        "extra_concepts": sorted(extra_concepts),
        "ranked_missing_concepts": sorted(missing_concepts),
        "concept_locations": concept_locations,
        "match_score": match_score,
        "fuzzy_threshold": fuzzy_threshold,
        "include_fuzzy_in_score": include_fuzzy_in_score,
    }
