from pathlib import Path

from pypdf import PdfReader
from docx import Document


def load_text(filepath: str) -> str:
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    suffix = path.suffix.lower()

    if suffix == ".txt":
        return _load_txt(path)
    if suffix == ".pdf":
        return _load_pdf(path)
    if suffix == ".docx":
        return _load_docx(path)

    raise ValueError(
        f"Unsupported file type: {suffix}. Supported types are .txt, .pdf, .docx"
    )


def _load_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    text_parts = []

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text_parts.append(extracted)

    return "\n".join(text_parts)


def _load_docx(path: Path) -> str:
    document = Document(str(path))
    return "\n".join(paragraph.text for paragraph in document.paragraphs)
