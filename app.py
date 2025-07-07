import json
import tempfile
from pathlib import Path

import streamlit as st

from src.analyzer import run_analysis


st.set_page_config(page_title="Resume Keyword Analyzer", layout="wide")

st.title("Resume Keyword Analyzer")
st.write("Upload a resume and a job description to compare their alignment.")

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

        st.subheader("Match Results")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Overall Match Score", f"{results['match_score']}%")
        with col2:
            st.metric("Keyword Score", f"{results['keyword_score']}%")
        with col3:
            st.metric("Phrase Score", f"{results['phrase_score']}%")

        left, right = st.columns(2)

        with left:
            st.markdown("### Matched Standalone Keywords")
            st.write(results["matched_keywords"] or ["None"])

            st.markdown("### Matched Phrases")
            st.write(results["matched_phrases"] or ["None"])

        with right:
            st.markdown("### Missing Standalone Keywords")
            st.write(results["ranked_missing_keywords"][:5] or ["None"])

            st.markdown("### Missing Phrases")
            st.write(results["ranked_missing_phrases"][:5] or ["None"])

        st.markdown("### Full Analysis JSON")
        json_str = json.dumps(results, indent=2)
        st.download_button(
            label="Download JSON Results",
            data=json_str,
            file_name="analysis_results.json",
            mime="application/json",
        )

        with st.expander("Show extracted terms"):
            st.write("Resume Keywords:", results.get("resume_keywords", []))
            st.write("Job Keywords:", results.get("job_keywords", []))
            st.write("Resume Phrases:", results.get("resume_phrases", []))
            st.write("Job Phrases:", results.get("job_phrases", []))

    except Exception as error:
        st.error(f"Error: {error}")
else:
    st.info("Upload both files to begin analysis.")
