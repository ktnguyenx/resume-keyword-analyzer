from src.analyzer import run_analysis
from src.cli import parse_args
from src.export import export_results_to_json
from src.report import build_report


def main():
    args = parse_args()

    try:
        results = run_analysis(args.resume_path, args.job_path)
        print(build_report(results))

        if args.json_path:
            export_results_to_json(results, args.json_path)
            print(f"\nSaved JSON results to: {args.json_path}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
