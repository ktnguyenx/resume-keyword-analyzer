import re

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "in", "is", "it", "of", "on", "or", "that", "the", "to",
    "was", "were", "will", "with", "using", "use", "used"
}


def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s+#./-]", " ", text)
    tokens = text.split()
    return [token for token in tokens if token not in STOPWORDS and len(token) > 1]
