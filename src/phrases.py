COMMON_SKILL_PHRASES = {
    "machine learning",
    "data analysis",
    "data science",
    "natural language processing",
    "project management",
    "version control",
    "software engineering",
    "web development",
    "problem solving",
    "team collaboration",
    "unit testing",
    "data visualization",
    "object oriented",
    "computer science",
}


def extract_phrases(tokens: list[str], max_n: int = 3) -> set[str]:
    found = set()

    for n in range(2, max_n + 1):
        for i in range(len(tokens) - n + 1):
            phrase = " ".join(tokens[i:i + n])
            if phrase in COMMON_SKILL_PHRASES:
                found.add(phrase)

    return found
