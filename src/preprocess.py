import spacy

_NLP = None


def get_nlp():
    global _NLP
    if _NLP is None:
        _NLP = spacy.load("en_core_web_sm")
    return _NLP


def preprocess_text(text: str) -> list[str]:
    nlp = get_nlp()
    doc = nlp(text)

    tokens = []
    for token in doc:
        if token.is_space or token.is_punct:
            continue
        if token.is_stop:
            continue
        if not token.text.strip():
            continue

        lemma = token.lemma_.lower().strip()
        if not lemma or len(lemma) <= 1:
            continue
        if lemma in {"-pron-"}:
            continue

        tokens.append(lemma)

    return tokens


def get_doc(text: str):
    nlp = get_nlp()
    return nlp(text)
