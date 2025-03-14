# Resume Keyword Analyzer

A Python project for analyzing how well a resume aligns with a job description using keyword overlap, basic NLP preprocessing, and similarity scoring.

## Goals
- Extract keywords from resumes and job descriptions
- Compare overlap between the two
- Compute a simple alignment score
- Generate a readable report highlighting matched and missing terms

## Features
- Text cleaning and normalization
- Stopword removal and lemmatization
- Keyword extraction
- Resume-to-job-description similarity scoring
- CSV/JSON export of analysis results
- Optional UI or web interface in a later version

## Tech Stack
- Python
- Pandas
- spaCy / NLTK
- scikit-learn
- Git

## Project Status
In active development.

## Example Use Case
Given:
- a resume text file
- a job description text file

The program returns:
- matched keywords
- missing keywords
- keyword overlap percentage
- a simple similarity score

## Next Steps
- Improve keyword weighting
- Handle multi-word skills like "machine learning" and "data analysis"
- Add better scoring logic
- Support PDF/DOCX input
