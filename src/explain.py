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
            "Some matches were inferred through alias normalization rather than exact wording."
        )

    if results.get("missing_concepts"):
        explanations.append(
            f"Highest-priority missing concept: {results['missing_concepts'][0]}"
        )

    return explanations
