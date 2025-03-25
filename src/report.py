def build_report(results: dict) -> str:
    score = results["match_score"]

    if score >= 75:
        verdict = "Strong match"
    elif score >= 50:
        verdict = "Moderate match"
    else:
        verdict = "Weak match"

    lines = [
        "=" * 50,
        "RESUME ANALYZER REPORT",
        "=" * 50,
        f"Match Score: {score}%",
        f"Verdict: {verdict}",
        "",
        f"Matched Keywords ({len(results['matched_keywords'])}):",
        ", ".join(results["matched_keywords"]) or "None",
        "",
        f"Missing Keywords ({len(results['missing_keywords'])}):",
        ", ".join(results["missing_keywords"]) or "None",
        "",
        f"Extra Resume Keywords ({len(results['extra_keywords'])}):",
        ", ".join(results["extra_keywords"]) or "None",
        "",
        "Suggestions:",
    ]

    if results["missing_keywords"]:
        lines.append(
            "- Consider adding the most relevant missing skills if you genuinely have them."
        )
    else:
        lines.append("- Your resume already covers the main detected keywords.")

    lines.append("- Tailor bullet points so matching skills appear in context, not as keyword stuffing.")
    lines.append("- Prioritize technical skills and tools that appear repeatedly in the job description.")

    return "\n".join(lines)
