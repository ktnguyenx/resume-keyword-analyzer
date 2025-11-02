from collections import Counter

STANDALONE_SKILL_VOCAB = {
    "python",
    "java",
    "javascript",
    "typescript",
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
    "testing",
    "communication",
    "leadership",
    "teamwork",
    "debugging",
    "automation",
    "streamlit",
    "spacy",
}


def extract_keywords(tokens: list[str], top_n: int = 30) -> set[str]:
    counts = Counter(tokens)

    return {
        token
        for token, _ in counts.most_common(top_n)
        if token in STANDALONE_SKILL_VOCAB
    }
