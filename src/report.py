def build_report(results: dict) -> str:
    lines = [
        "=== Resume Keyword Analyzer Report ===",
        f"Overlap Score: {results['overlap_score']}%",
        "",
        f"Matched Keywords: {', '.join(results['matched_keywords']) or 'None'}",
        f"Missing Keywords: {', '.join(results['missing_keywords']) or 'None'}",
    ]
    return "\n".join(lines)
