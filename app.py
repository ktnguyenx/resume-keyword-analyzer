import json
import tempfile
from pathlib import Path

import streamlit as st

from src.analyzer import run_analysis
from src.config import DEFAULT_FUZZY_THRESHOLD, DEFAULT_INCLUDE_FUZZY_IN_SCORE
from src.csv_export import export_results_to_csv
from src.text_export import export_results_to_text


st.set_page_config(page_title="Resume Keyword Analyzer", layout="wide")

st.title("Resume Keyword Analyzer")
st.write("Upload a resume and a job description to compare concept-level alignment using NLP-powered extraction.")

st.sidebar.header("Analysis Settings")
fuzzy_threshold = st.sidebar.slider(
    "Fuzzy Match Threshold",
    min_value=70,
    max_value=95,
    value=DEFAULT_FUZZY_THRESHOLD,
)
include_fuzzy_in_score = st.sidebar.checkbox(
    "Include Fuzzy Matches in Score",
    value=DEFAULT_INCLUDE_FUZZY_IN_SCORE,
)
show_debug = st.sidebar.checkbox(
    "Show Debug Info",
    value=False,
)

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

        results = run_analysis(
            resume_path,
            job_path,
            fuzzy_threshold=fuzzy_threshold,
            include_fuzzy_in_score=include_fuzzy_in_score,
        )

        score = results["match_score"]
        if score >= 75:
            status = "Strong"
        elif score >= 50:
            status = "Moderate"
        else:
            status = "Weak"

        st.metric("Overall Match Score", f"{score}%")
        st.caption(f"Match Strength: {status}")

        if not results["matched_concepts"] and not results["missing_concepts"]:
            st.warning("No meaningful concepts were extracted from one or both files.")
        elif not results["matched_concepts"]:
            st.warning("No matched concepts were found between the uploaded files.")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Summary", "Matches", "Missing", "Exports / Debug"]
        )

        with tab1:
            st.subheader("Summary")
            for explanation in results.get("explanations", []):
                st.write(f"- {explanation}")

        with tab2:
            st.subheader("Matched Concepts")
            if results["matched_concepts"]:
                for concept in results["matched_concepts"]:
                    locations = results["concept_locations"].get(concept, [])
                    st.write(f"- **{concept}** — found in: {', '.join(locations) if locations else 'unknown'}")
            else:
                st.write("None")

            st.subheader("Alias-Inferred Matches")
            if results["alias_inferred_matches"]:
                for item in results["alias_inferred_matches"]:
                    st.write(
                        f"- Job term **{item['job_term']}** matched concept **{item['concept']}** via resume term(s): {', '.join(item['matched_by'])}"
                    )
            else:
                st.write("None")

            st.subheader("Fuzzy Matches")
            if results["fuzzy_matches"]:
                for item in results["fuzzy_matches"]:
                    st.write(
                        f"- Job concept **{item['job_concept']}** loosely matched resume concept **{item['resume_concept']}** (score: {item['score']})"
                    )
            else:
                st.write("None")

        with tab3:
            st.subheader("Missing Concepts")
            st.write(results["missing_concepts"] or ["None"])

        with tab4:
            st.subheader("Downloads")

            json_str = json.dumps(results, indent=2)
            st.download_button(
                label="Download JSON Results",
                data=json_str,
                file_name="analysis_results.json",
                mime="application/json",
            )

            report_text = export_results_to_text(results)
            st.download_button(
                label="Download Text Report",
                data=report_text,
                file_name="analysis_report.txt",
                mime="text/plain",
            )

            csv_data = export_results_to_csv(results)
            st.download_button(
                label="Download CSV Summary",
                data=csv_data,
                file_name="analysis_summary.csv",
                mime="text/csv",
            )

            if show_debug:
                st.subheader("Resume Section Concepts")
                st.write(results["resume_section_concepts"])

                st.subheader("Term Normalization")
                st.write("Resume term map:", results["resume_term_map"])
                st.write("Job term map:", results["job_term_map"])

                st.subheader("Raw Terms")
                st.write("Resume raw terms:", results["resume_raw_terms"])
                st.write("Job raw terms:", results["job_raw_terms"])

    except Exception as error:
        st.error(f"Error: {error}")
else:
    st.info("Upload both files to begin analysis.")
