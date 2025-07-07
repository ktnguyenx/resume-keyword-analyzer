# Resume Keyword Analyzer

A Python application that analyzes how well a resume aligns with a job description using standalone keyword matching, multi-word phrase detection, weighted scoring, and interactive reporting.

## Features

- Compare a resume against a job description
- Extract standalone keywords and multi-word skill phrases
- Compute alignment scores based on matched and missing terms
- Support `.txt`, `.pdf`, and `.docx` inputs
- Run analysis from the command line
- Launch a Streamlit web app for file upload and interactive results
- Export analysis results to JSON

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
- Improve concept and alias matching (for example, relating Git to version control) 
- Make phrase and keyword extraction more robust 
- Improve scoring quality for real-world job descriptions 
- Add better handling for noisy PDF formatting 
- Expand test coverage Explore deployment options for a public demo
