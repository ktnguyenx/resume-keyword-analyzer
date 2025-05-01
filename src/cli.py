import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze how well a resume matches a job description."
    )
    parser.add_argument("resume_path", help="Path to the resume file (.txt, .pdf, .docx)")
    parser.add_argument("job_path", help="Path to the job description file (.txt, .pdf, .docx)")
    parser.add_argument(
        "--json",
        dest="json_path",
        default=None,
        help="Optional path to save analysis results as JSON",
    )
    return parser.parse_args()
