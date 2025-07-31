def build_explanations(results: dict) -> list[str]:
    explanations = []

    if results["match_score"] >= 75:
        explanations.append(
            "The resume aligns well with the job description across major concepts."
        )
    elif results["match_score"] >= 50:
        explanations.append(
            "The resume shows partial alignment, but several relevant concepts are still missing."
        )
    else:
        explanations.append(
            "The resume is missing several important concepts from the job description."
        )

    if results.get("matched_aliases"):
        explanations.append(
            "Some matches were identified through concept normalization rather than exact wording."
        )

    if results.get("ranked_missing_terms"):
        explanations.append(
            f"Top missing concept: {results['ranked_missing_terms'][0]}"
        )

    return explanations
