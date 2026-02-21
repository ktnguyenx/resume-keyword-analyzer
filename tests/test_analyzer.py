from pathlib import Path

from src.analyzer import run_analysis


def test_run_analysis_returns_config_values(tmp_path: Path):
    resume = tmp_path / "resume.txt"
    job = tmp_path / "job.txt"

    resume.write_text("Skills:\nPython\nGit\n", encoding="utf-8")
    job.write_text("Looking for Python and version control.", encoding="utf-8")

    results = run_analysis(
        str(resume),
        str(job),
        fuzzy_threshold=80,
        include_fuzzy_in_score=False,
    )

    assert results["fuzzy_threshold"] == 80
    assert results["include_fuzzy_in_score"] is False
