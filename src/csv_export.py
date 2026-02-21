import io
import pandas as pd


def export_results_to_csv(results: dict) -> str:
    rows = []

    for concept in results.get("matched_concepts", []):
        rows.append({
            "concept": concept,
            "status": "matched",
            "locations": ", ".join(results.get("concept_locations", {}).get(concept, [])),
        })

    for concept in results.get("missing_concepts", []):
        rows.append({
            "concept": concept,
            "status": "missing",
            "locations": "",
        })

    df = pd.DataFrame(rows)
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue()
