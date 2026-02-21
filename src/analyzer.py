from src.aliases import build_term_to_concept_map
from src.config import DEFAULT_FUZZY_THRESHOLD, DEFAULT_INCLUDE_FUZZY_IN_SCORE
from src.explain import build_explanations
from src.keywords import extract_keywords
from src.loader import load_text
from src.phrases import extract_phrases
from src.preprocess import preprocess_text
from src.scorer import analyze_match
from src.sections import split_into_sections


def extract_terms_from_text(text: str) -> tuple[set[str], set[str], set[str], dict[str, str]]:
    tokens = preprocess_text(text)
    keywords = extract_keywords(tokens)
    phrases = extract_phrases(text)
    raw_terms = keywords | phrases
    term_map = build_term_to_concept_map(raw_terms)

    return keywords, phrases, raw_terms, term_map


def build_section_concept_map(sections: dict[str, str]) -> dict[str, set[str]]:
    section_concepts = {}

    for section_name, section_text in sections.items():
        _, _, _, term_map = extract_terms_from_text(section_text)
        section_concepts[section_name] = set(term_map.values())

    return section_concepts


def run_analysis(
    resume_path: str,
    job_path: str,
    fuzzy_threshold: int = DEFAULT_FUZZY_THRESHOLD,
    include_fuzzy_in_score: bool = DEFAULT_INCLUDE_FUZZY_IN_SCORE,
) -> dict:
    resume_text = load_text(resume_path)
    job_text = load_text(job_path)

    resume_sections = split_into_sections(resume_text)
    job_sections = split_into_sections(job_text)

    resume_keywords, resume_phrases, resume_raw_terms, resume_term_map = extract_terms_from_text(resume_text)
    job_keywords, job_phrases, job_raw_terms, job_term_map = extract_terms_from_text(job_text)

    resume_section_concepts = build_section_concept_map(resume_sections)

    results = analyze_match(
        resume_raw_terms,
        job_raw_terms,
        resume_term_map,
        job_term_map,
        resume_section_concepts,
        fuzzy_threshold=fuzzy_threshold,
        include_fuzzy_in_score=include_fuzzy_in_score,
    )

    results["resume_keywords"] = sorted(resume_keywords)
    results["job_keywords"] = sorted(job_keywords)
    results["resume_phrases"] = sorted(resume_phrases)
    results["job_phrases"] = sorted(job_phrases)
    results["resume_raw_terms"] = sorted(resume_raw_terms)
    results["job_raw_terms"] = sorted(job_raw_terms)
    results["resume_term_map"] = resume_term_map
    results["job_term_map"] = job_term_map
    results["resume_sections"] = resume_sections
    results["job_sections"] = job_sections
    results["resume_section_concepts"] = {
        key: sorted(value) for key, value in resume_section_concepts.items()
    }
    results["explanations"] = build_explanations(results)

    return results
