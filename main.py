from src.cli import parse_args
from src.export import export_results_to_json
from src.keywords import extract_keyword_counts, extract_keywords
from src.loader import load_text
from src.phrases import extract_phrase_counts, extract_phrases
from src.preprocess import preprocess_text
from src.report import build_report
from src.scorer import analyze_match


def main():
    args = parse_args()

    try:
        resume_text = load_text(args.resume_path)
        job_text = load_text(args.job_path)

        resume_tokens = preprocess_text(resume_text)
        job_tokens = preprocess_text(job_text)

        resume_keywords = extract_keywords(resume_tokens)
        job_keywords = extract_keywords(job_tokens)

        resume_phrases = extract_phrases(resume_tokens)
        job_phrases = extract_phrases(job_tokens)

        job_keyword_counts = extract_keyword_counts(job_tokens)
        job_phrase_counts = extract_phrase_counts(job_tokens)

        results = analyze_match(
            resume_keywords,
            job_keywords,
            resume_phrases,
            job_phrases,
            job_keyword_counts,
            job_phrase_counts,
        )

        print(build_report(results))

        if args.json_path:
            export_results_to_json(results, args.json_path)
            print(f"\nSaved JSON results to: {args.json_path}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
