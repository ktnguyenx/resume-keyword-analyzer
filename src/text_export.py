from src.report import build_report


def export_results_to_text(results: dict) -> str:
    return build_report(results)
