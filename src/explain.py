def build_explanations(results: dict) -> list[str]:
    explanations = []

    score = results["match_score"]

    if score >= 75:
        explanations.append(
            "The resume aligns well with the job description across most major concepts."
        )
    elif score >= 50:
        explanations.append(
            "The resume shows moderate alignment, but several relevant concepts are still missing."
        )
    else:
        explanations.append(
            "The resume is missing several important concepts from the job description."
        )

    if results.get("alias_inferred_matches"):
        explanations.append(
            "Some matches were identified through alias normalization."
        )

    if results.get("fuzzy_matches"):
        explanations.append(
            "Some concept matches were identified through fuzzy similarity rather than exact wording."
        )

    if results.get("ranked_missing_concepts"):
        explanations.append(
            f"Top missing concept: {results['ranked_missing_concepts'][0]}"
        )

    return explanations
