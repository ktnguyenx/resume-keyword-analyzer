from src.keywords import extract_keyword_counts, extract_keywords
from src.loader import load_text
from src.phrases import extract_phrase_counts, extract_phrases
from src.preprocess import preprocess_text
from src.scorer import analyze_match


def run_analysis(resume_path: str, job_path: str) -> dict:
    resume_text = load_text(resume_path)
    job_text = load_text(job_path)

    resume_tokens = preprocess_text(resume_text)
    job_tokens = preprocess_text(job_text)

    resume_keywords = extract_keywords(resume_tokens)
    job_keywords = extract_keywords(job_tokens)

    resume_phrases = extract_phrases(resume_tokens)
    job_phrases = extract_phrases(job_tokens)

    job_keyword_counts = extract_keyword_counts(job_tokens)
    job_phrase_counts = extract_phrase_counts(job_tokens)

    results = analyze_match(
        resume_keywords,
        job_keywords,
        resume_phrases,
        job_phrases,
        job_keyword_counts,
        job_phrase_counts,
    )

    results["resume_tokens"] = resume_tokens
    results["job_tokens"] = job_tokens
    results["resume_keywords"] = sorted(resume_keywords)
    results["job_keywords"] = sorted(job_keywords)
    results["resume_phrases"] = sorted(resume_phrases)
    results["job_phrases"] = sorted(job_phrases)

    return results
