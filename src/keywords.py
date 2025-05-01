from collections import Counter

STANDALONE_SKILL_VOCAB = {
    "python",
    "java",
    "javascript",
    "typescript",
    "c",
    "c++",
    "sql",
    "html",
    "css",
    "react",
    "node",
    "git",
    "github",
    "pandas",
    "numpy",
    "excel",
    "aws",
    "linux",
    "docker",
    "flask",
    "django",
    "api",
    "apis",
    "testing",
    "communication",
    "leadership",
    "teamwork",
    "debugging",
    "automation",
}

PHRASE_FRAGMENT_WORDS = {
    "data",
    "analysis",
    "machine",
    "learning",
    "natural",
    "language",
    "processing",
    "version",
    "control",
    "project",
    "management",
    "software",
    "engineering",
    "web",
    "development",
    "problem",
    "solving",
    "unit",
    "visualization",
    "science",
    "computer",
}


def extract_keywords(tokens: list[str], top_n: int = 20) -> set[str]:
    counts = Counter(tokens)

    keywords = {
        word
        for word, _ in counts.most_common(top_n)
        if word in STANDALONE_SKILL_VOCAB and word not in PHRASE_FRAGMENT_WORDS
    }

    return keywords


def extract_keyword_counts(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))
