from src.preprocess import get_doc

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
    "computer science",
    "application programming interface",
    "object oriented programming",
    "continuous integration",
}


def normalize_phrase(text: str) -> str:
    doc = get_doc(text)
    parts = []

    for token in doc:
        if token.is_space or token.is_punct or token.is_stop:
            continue
        lemma = token.lemma_.lower().strip()
        if lemma and lemma != "-pron-":
            parts.append(lemma)

    return " ".join(parts)


def extract_phrases(text: str) -> set[str]:
    doc = get_doc(text)
    found = set()

    for chunk in doc.noun_chunks:
        normalized = normalize_phrase(chunk.text)
        if normalized in COMMON_SKILL_PHRASES:
            found.add(normalized)

    text_normalized = normalize_phrase(text)
    for phrase in COMMON_SKILL_PHRASES:
        if phrase in text_normalized:
            found.add(phrase)

    return found
