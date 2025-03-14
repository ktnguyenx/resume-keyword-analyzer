from collections import Counter


def extract_keywords(tokens: list[str], top_n: int = 20) -> set[str]:
    counts = Counter(tokens)
    most_common = counts.most_common(top_n)
    return {word for word, _ in most_common}
