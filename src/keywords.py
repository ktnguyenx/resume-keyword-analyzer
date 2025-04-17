from collections import Counter

SKILL_VOCAB = {
    "python", "java", "javascript", "typescript", "c", "c++", "sql",
    "html", "css", "react", "node", "git", "github", "pandas",
    "numpy", "scikit-learn", "machine", "learning", "nlp", "data",
    "analysis", "analytics", "excel", "aws", "linux", "docker",
    "flask", "django", "api", "apis", "testing", "communication",
    "leadership", "teamwork", "problem-solving", "debugging"
}


def extract_keywords(tokens: list[str], top_n: int = 25) -> set[str]:
    counts = Counter(tokens)
    frequent_words = {word for word, _ in counts.most_common(top_n)}
    skill_words = {word for word in tokens if word in SKILL_VOCAB}
    return frequent_words.union(skill_words)


def extract_keyword_counts(tokens: list[str]) -> dict[str, int]:
    counts = Counter(tokens)
    return dict(counts)
