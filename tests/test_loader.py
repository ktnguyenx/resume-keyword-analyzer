from pathlib import Path

import pytest

from src.loader import load_text


def test_load_text_from_txt(tmp_path: Path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello world", encoding="utf-8")

    assert load_text(str(file_path)) == "hello world"


def test_load_text_raises_for_missing_file():
    with pytest.raises(FileNotFoundError):
        load_text("does_not_exist.txt")
