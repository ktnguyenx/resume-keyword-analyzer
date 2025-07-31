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
        f"Matched Concepts ({len(results['matched_terms'])}):",
        ", ".join(results["matched_terms"]) or "None",
        "",
        f"Missing Concepts ({len(results['missing_terms'])}):",
        ", ".join(results["missing_terms"]) or "None",
        "",
        "Explanations:",
    ]

    if results.get("explanations"):
        for explanation in results["explanations"]:
            lines.append(f"- {explanation}")
    else:
        lines.append("- No explanations available.")

    return "\n".join(lines)
