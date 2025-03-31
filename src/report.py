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
        f"Overall Match Score: {score}%",
        f"Keyword Score: {results['keyword_score']}%",
        f"Phrase Score: {results['phrase_score']}%",
        f"Verdict: {verdict}",
        "",
        f"Matched Keywords ({len(results['matched_keywords'])}):",
        ", ".join(results["matched_keywords"]) or "None",
        "",
        f"Missing Keywords ({len(results['missing_keywords'])}):",
        ", ".join(results["missing_keywords"]) or "None",
        "",
        f"Matched Phrases ({len(results['matched_phrases'])}):",
        ", ".join(results["matched_phrases"]) or "None",
        "",
        f"Missing Phrases ({len(results['missing_phrases'])}):",
        ", ".join(results["missing_phrases"]) or "None",
        "",
        "Suggestions:",
    ]

    if results["missing_phrases"]:
        lines.append("- Add experience bullets that reflect the missing high-value phrases where truthful.")
    if results["missing_keywords"]:
        lines.append("- Strengthen the resume around the most relevant missing technical terms.")
    if not results["missing_keywords"] and not results["missing_phrases"]:
        lines.append("- Your resume appears well aligned with the detected requirements.")

    lines.append("- Keep matching skills inside accomplishment-focused bullet points.")
    return "\n".join(lines)
