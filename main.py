from src.loader import load_text
from src.preprocess import preprocess_text
from src.keywords import extract_keywords
from src.phrases import extract_phrases
from src.scorer import analyze_match
from src.report import build_report
import sys


def main():
    if len(sys.argv) == 3:
        resume_path = sys.argv[1]
        job_path = sys.argv[2]
    else:
        resume_path = "sample_data/sample_resume.txt"
        job_path = "sample_data/sample_job_description.txt"

    resume_text = load_text(resume_path)
    job_text = load_text(job_path)

    resume_tokens = preprocess_text(resume_text)
    job_tokens = preprocess_text(job_text)

    resume_keywords = extract_keywords(resume_tokens)
    job_keywords = extract_keywords(job_tokens)

    resume_phrases = extract_phrases(resume_tokens)
    job_phrases = extract_phrases(job_tokens)

    results = analyze_match(
        resume_keywords,
        job_keywords,
        resume_phrases,
        job_phrases,
    )

    report = build_report(results)
    print(report)


if __name__ == "__main__":
    main()
