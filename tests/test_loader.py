from pathlib import Path

from src.loader import load_text


def test_load_text_from_txt(tmp_path: Path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello world", encoding="utf-8")

    assert load_text(str(file_path)) == "hello world"
