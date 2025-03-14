import re

STOPWORDS = {
    "the", "and", "or", "a", "an", "to", "of", "in", "on", "for", "with",
    "is", "are", "as", "by", "at", "from", "that", "this", "be", "will"
}


def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = text.split()
    return [token for token in tokens if token not in STOPWORDS]
