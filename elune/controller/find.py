import os
import yaml
from .rc import ELUNE_PATH


def find_problems(source=None, tag=None):
    results = []

    for fname in os.listdir(ELUNE_PATH):
        if not fname.endswith(".yaml"):
            continue

        path = os.path.join(ELUNE_PATH, fname)
        try:
            with open(path, "r") as f:
                data = yaml.safe_load(f)

            if source and source.lower() not in data.get("source", "").lower():
                continue
            if tag:
                tags = data.get("tags", [])
                if isinstance(tags, str):
                    tags = [t.strip() for t in tags.split(",")]
                if tag.lower() not in [t.lower() for t in tags]:
                    continue

            results.append((fname, data.get("source", ""), tags))
        except Exception as e:
            print(f"Failed to read {fname}: {e}")

    return results
