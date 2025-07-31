from src.aliases import build_alias_matches, normalize_terms
from src.explain import build_explanations
from src.keywords import extract_keywords
from src.loader import load_text
from src.phrases import extract_phrases
from src.preprocess import preprocess_text
from src.scorer import analyze_match
from src.sections import split_into_sections


def run_analysis(resume_path: str, job_path: str) -> dict:
    resume_text = load_text(resume_path)
    job_text = load_text(job_path)

    resume_sections = split_into_sections(resume_text)
    job_sections = split_into_sections(job_text)

    resume_tokens = preprocess_text(resume_text)
    job_tokens = preprocess_text(job_text)

    resume_keywords = extract_keywords(resume_tokens)
    job_keywords = extract_keywords(job_tokens)

    resume_phrases = extract_phrases(resume_tokens)
    job_phrases = extract_phrases(job_tokens)

    resume_raw_terms = resume_keywords | resume_phrases
    job_raw_terms = job_keywords | job_phrases

    matched_aliases = {
        "resume": build_alias_matches(resume_raw_terms),
        "job": build_alias_matches(job_raw_terms),
    }

    resume_terms = normalize_terms(resume_raw_terms)
    job_terms = normalize_terms(job_raw_terms)

    results = analyze_match(resume_terms, job_terms)

    results["resume_keywords"] = sorted(resume_keywords)
    results["job_keywords"] = sorted(job_keywords)
    results["resume_phrases"] = sorted(resume_phrases)
    results["job_phrases"] = sorted(job_phrases)
    results["resume_terms"] = sorted(resume_terms)
    results["job_terms"] = sorted(job_terms)
    results["resume_sections"] = resume_sections
    results["job_sections"] = job_sections
    results["matched_aliases"] = matched_aliases
    results["explanations"] = build_explanations(results)

    return results
