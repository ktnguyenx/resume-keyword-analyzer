TECHNICAL_KEYWORDS = {
    "python", "java", "javascript", "typescript", "sql", "html", "css",
    "react", "node", "git", "github", "pandas", "numpy", "scikit-learn",
    "nlp", "api", "apis", "docker", "linux", "aws", "flask", "django",
    "testing", "debugging", "excel", "analytics"
}

SOFT_KEYWORDS = {
    "communication", "leadership", "teamwork", "collaboration",
    "problem-solving", "problem", "solving"
}

HIGH_VALUE_PHRASES = {
    "machine learning",
    "natural language processing",
    "data analysis",
    "data science",
    "software engineering",
    "web development",
    "version control",
    "project management",
    "unit testing",
    "data visualization",
}


def get_keyword_weight(keyword: str, frequency: int = 1) -> float:
    if keyword in TECHNICAL_KEYWORDS:
        base = 3.0
    elif keyword in SOFT_KEYWORDS:
        base = 1.5
    else:
        base = 2.0

    return base + 0.25 * max(frequency - 1, 0)


def get_phrase_weight(phrase: str, frequency: int = 1) -> float:
    if phrase in HIGH_VALUE_PHRASES:
        base = 4.0
    else:
        base = 2.5

    return base + 0.4 * max(frequency - 1, 0)
