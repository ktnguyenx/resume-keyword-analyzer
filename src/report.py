def build_report(results: dict) -> str:
    score = results["match_score"]

    if score >= 80:
        verdict = "Strong match"
    elif score >= 55:
        verdict = "Moderate match"
    else:
        verdict = "Weak match"

    lines = [
        "=" * 60,
        "RESUME ANALYZER REPORT",
        "=" * 60,
        f"Overall Match Score: {score}%",
        f"Verdict: {verdict}",
        "",
        f"Matched Concepts ({len(results['matched_concepts'])}):",
    ]

    if results["matched_concepts"]:
        for concept in results["matched_concepts"]:
            locations = results["concept_locations"].get(concept, [])
            location_text = ", ".join(locations) if locations else "unknown location"
            lines.append(f"- {concept} (found in: {location_text})")
    else:
        lines.append("None")

    lines.extend([
        "",
        f"Missing Concepts ({len(results['missing_concepts'])}):",
        ", ".join(results["missing_concepts"]) or "None",
        "",
        "Alias-Inferred Matches:",
    ])

    if results["alias_inferred_matches"]:
        for item in results["alias_inferred_matches"]:
            lines.append(
                f"- {item['job_term']} matched concept '{item['concept']}' via {', '.join(item['matched_by'])}"
            )
    else:
        lines.append("- None")

    lines.append("")
    lines.append("Explanations:")

    if results.get("explanations"):
        for explanation in results["explanations"]:
            lines.append(f"- {explanation}")
    else:
        lines.append("- No explanations available.")

    return "\n".join(lines)
