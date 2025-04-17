def build_report(results: dict) -> str:
    score = results["match_score"]

    if score >= 80:
        verdict = "Strong match"
    elif score >= 55:
        verdict = "Moderate match"
    else:
        verdict = "Weak match"

    top_missing_keywords = results["ranked_missing_keywords"][:5]
    top_missing_phrases = results["ranked_missing_phrases"][:5]

    lines = [
        "=" * 60,
        "RESUME ANALYZER REPORT",
        "=" * 60,
        f"Overall Match Score: {score}%",
        f"Keyword Score: {results['keyword_score']}%",
        f"Phrase Score: {results['phrase_score']}%",
        f"Verdict: {verdict}",
        "",
        f"Matched Keywords ({len(results['matched_keywords'])}):",
        ", ".join(results["matched_keywords"]) or "None",
        "",
        f"Matched Phrases ({len(results['matched_phrases'])}):",
        ", ".join(results["matched_phrases"]) or "None",
        "",
        "Top Missing Keywords:",
        ", ".join(top_missing_keywords) or "None",
        "",
        "Top Missing Phrases:",
        ", ".join(top_missing_phrases) or "None",
        "",
        "Suggestions:",
    ]

    if top_missing_phrases:
        lines.append("- Strengthen resume bullets around the highest-value missing phrases where accurate.")
    if top_missing_keywords:
        lines.append("- Add or clarify the most important missing technical terms if you genuinely have that experience.")
    if not top_missing_keywords and not top_missing_phrases:
        lines.append("- Your resume appears strongly aligned with the analyzed job description.")

    lines.append("- Emphasize tools, methods, and technologies in accomplishment-based bullet points.")
    lines.append("- Repeated job-description terms are weighted more heavily in this version.")

    return "\n".join(lines)
