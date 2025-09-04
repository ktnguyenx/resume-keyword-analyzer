# Resume Keyword Analyzer

A Python and Streamlit application that analyzes resume-to-job-description alignment using keyword extraction, phrase detection, concept normalization, and interactive reporting.

## Features

- Normalize related terms into shared concepts (for example, `Git` and `version control`)
- Distinguish between exact matches and alias-inferred matches
- Detect common resume sections such as Skills, Experience, Projects, and Education
- Support `.txt`, `.pdf`, and `.docx` inputs
- Run analysis from the command line or through a Streamlit web app
- Provide human-readable explanations for match results

## Tech Stack

- Python
- Streamlit
- PyPDF
- python-docx
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
```

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
