from src.preprocess import preprocess_text


def test_preprocess_text():
    text = "Python and SQL are used in Data Analysis."
    tokens = preprocess_text(text)

    assert "python" in tokens
    assert "sql" in tokens
    assert "and" not in tokens
    assert "are" not in tokens
