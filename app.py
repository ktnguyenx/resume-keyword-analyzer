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
            ["Summary", "Matches", "Missing", "Debug"]
        )

        with tab1:
            st.subheader("Summary")
            for explanation in results.get("explanations", []):
                st.write(f"- {explanation}")

        with tab2:
            st.subheader("Matched Concepts")
            st.write(results["matched_concepts"] or ["None"])

            st.subheader("Exact Matches")
            st.write(results["exact_matches"] or ["None"])

            st.subheader("Alias-Inferred Matches")
            if results["alias_inferred_matches"]:
                for item in results["alias_inferred_matches"]:
                    st.write(
                        f"- Job term **{item['job_term']}** matched concept **{item['concept']}** via resume term(s): {', '.join(item['matched_by'])}"
                    )
            else:
                st.write("None")

        with tab3:
            st.subheader("Missing Concepts")
            st.write(results["missing_concepts"] or ["None"])

        with tab4:
            st.subheader("Term Normalization")
            st.write("Resume term map:", results["resume_term_map"])
            st.write("Job term map:", results["job_term_map"])

            st.subheader("Extracted Raw Terms")
            st.write("Resume raw terms:", results["resume_raw_terms"])
            st.write("Job raw terms:", results["job_raw_terms"])

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
