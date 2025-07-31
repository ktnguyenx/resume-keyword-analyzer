import json
import tempfile
from pathlib import Path

import streamlit as st

from src.analyzer import run_analysis


st.set_page_config(page_title="Resume Keyword Analyzer", layout="wide")

st.title("Resume Keyword Analyzer")
st.write("Upload a resume and a job description to compare concept-level alignment.")

resume_file = st.file_uploader(
    "Upload Resume",
    type=["txt", "pdf", "docx"],
    key="resume_uploader",
)

job_file = st.file_uploader(
    "Upload Job Description",
    type=["txt", "pdf", "docx"],
    key="job_uploader",
)


def save_uploaded_file(uploaded_file) -> str:
    suffix = Path(uploaded_file.name).suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        return tmp.name


if resume_file and job_file:
    try:
        resume_path = save_uploaded_file(resume_file)
        job_path = save_uploaded_file(job_file)

        results = run_analysis(resume_path, job_path)

        st.metric("Overall Match Score", f"{results['match_score']}%")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Summary", "Matched Concepts", "Missing Concepts", "Debug"]
        )

        with tab1:
            st.subheader("Summary")
            for explanation in results.get("explanations", []):
                st.write(f"- {explanation}")

        with tab2:
            st.subheader("Matched Concepts")
            st.write(results["matched_terms"] or ["None"])

        with tab3:
            st.subheader("Missing Concepts")
            st.write(results["missing_terms"] or ["None"])

        with tab4:
            st.subheader("Alias Normalization")
            st.write("Resume alias mappings:", results["matched_aliases"]["resume"])
            st.write("Job alias mappings:", results["matched_aliases"]["job"])

            st.subheader("Extracted Raw Terms")
            st.write("Resume Keywords:", results.get("resume_keywords", []))
            st.write("Job Keywords:", results.get("job_keywords", []))
            st.write("Resume Phrases:", results.get("resume_phrases", []))
            st.write("Job Phrases:", results.get("job_phrases", []))

        json_str = json.dumps(results, indent=2)
        st.download_button(
            label="Download JSON Results",
            data=json_str,
            file_name="analysis_results.json",
            mime="application/json",
        )

    except Exception as error:
        st.error(f"Error: {error}")
else:
    st.info("Upload both files to begin analysis.")
