from src.preprocess import preprocess_text


def test_preprocess_text_lemmatizes_and_filters():
    text = "Developed APIs and used testing tools for projects."
    tokens = preprocess_text(text)

    assert "develop" in tokens
    assert "api" in tokens
    assert "test" in tokens or "testing" in tokens
