import re

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "have", "in", "is", "it", "of", "on", "or", "that", "the",
    "to", "was", "were", "will", "with", "using", "use", "used",
    "your", "our", "their", "this", "these", "those", "we",
    "you", "they", "i", "he", "she", "them", "his", "her",
    "candidate", "candidates", "seeking", "seek", "looking",
    "familiarity", "familiar", "plus", "experience", "experienced"
}


def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s+#/.-]", " ", text)
    text = re.sub(r"[./-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = text.split()
    return [token for token in tokens if token not in STOPWORDS and len(token) > 1]
