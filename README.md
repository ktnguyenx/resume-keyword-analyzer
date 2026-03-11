# Resume Keyword Analyzer

A Python and Streamlit application that analyzes resume-to-job-description alignment using keyword extraction, phrase detection, concept normalization, and interactive reporting.

## Features

- Use spaCy-based preprocessing for tokenization, stopword filtering, and lemmatization
- Identify exact, alias-based, and fuzzy concept matches to reduce brittle wording dependence
- Extract multi-word skill phrases with NLP-assisted phrase detection
- Normalize related terms into shared concepts
- Weight matched concepts based on where they appear in the resume
- Run analysis through both a CLI and a Streamlit web app
- Download results as JSON, plain text, or CSV

## Tech Stack

- Python
- Streamlit
- PyPDF
- python-docx
- spaCy
- pandas
- rapidfuzz
- Git

## Project Status

In active development.

## How It Works

Given:
- a resume file
- a job description file

The analyzer returns:
- matched standalone keywords
- matched skill phrases
- missing standalone keywords
- missing skill phrases
- weighted match scores
- optional JSON output

## Installation

```bash
python3 -m pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
python -m pip install rapidfuzz
```

### Recommended Python Version
Python 3.11 or 3.12 is recommended for compatibility with the current NLP stack.

## Usage

### Run the CLI
```bash
python3 main.py sample_data/sample_resume.txt sample_data/sample_job_description.txt
```

### Run the CLI with JSON export
```bash
python3 main.py sample_data/sample_resume.txt sample_data/sample_job_description.txt --json output/results.json
```

### Run the Streamlit app
```bash
streamlit run app.py
```
## Supported File Types 

- .txt
- .pdf
- .docx

## Example Use Case

This project can help users:

- Compare a resume against a target role
- Identify missing technical skills or phrases
- Improve resume targeting for specific job descriptions

## Future Improvements

- Expand the current rule-based alias mappings to cover a broader range of equivalent concepts.
- Improve section-aware weighting so skills found in Experience or Projects can count differently from those listed only in Skills.
- Refine scoring with stronger NLP methods and more robust concept matching.
- Improve parsing reliability for real-world PDF and DOCX inputs.
- Expand test coverage and prepare the app for public deployment.
