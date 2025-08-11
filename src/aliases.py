ALIAS_MAP = {
    "git": "version control",
    "github": "version control",
    "gitlab": "version control",
    "version control": "version control",

    "nlp": "natural language processing",
    "natural language processing": "natural language processing",

    "ml": "machine learning",
    "machine learning": "machine learning",

    "api": "application programming interface",
    "apis": "application programming interface",
    "rest api": "application programming interface",
    "application programming interface": "application programming interface",

    "oop": "object oriented programming",
    "object oriented programming": "object oriented programming",

    "ci/cd": "continuous integration",
    "ci cd": "continuous integration",
    "continuous integration": "continuous integration",

    "js": "javascript",
    "py": "python",

    "data analytics": "data analysis",
    "data analysis": "data analysis",
}


def normalize_term(term: str) -> str:
    return ALIAS_MAP.get(term, term)


def normalize_terms(terms: set[str]) -> set[str]:
    return {normalize_term(term) for term in terms}


def build_term_to_concept_map(terms: set[str]) -> dict[str, str]:
    return {term: normalize_term(term) for term in terms}
