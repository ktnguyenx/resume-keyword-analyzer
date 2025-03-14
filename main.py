from src.loader import load_text
from src.preprocess import preprocess_text
from src.keywords import extract_keywords
from src.scorer import compute_keyword_overlap
from src.report import build_report


def main():
    resume_path = "sample_data/sample_resume.txt"
    jd_path = "sample_data/sample_job_description.txt"

    resume_text = load_text(resume_path)
    jd_text = load_text(jd_path)

    clean_resume = preprocess_text(resume_text)
    clean_jd = preprocess_text(jd_text)

    resume_keywords = extract_keywords(clean_resume)
    jd_keywords = extract_keywords(clean_jd)

    results = compute_keyword_overlap(resume_keywords, jd_keywords)
    report = build_report(results)

    print(report)


if __name__ == "__main__":
    main()
