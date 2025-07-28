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

            tags = data.get("tags", [])
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",")]
            if not isinstance(tags, list):
                raise ValueError(f"'tags' must be a list in {fname}")

            src = data.get("source", "")
            desc = data.get("desc", "[no description]")
            if source and source.lower() not in src.lower():
                continue
            if tag and tag.lower() not in [t.lower() for t in tags]:
                continue

            results.append((fname, src, desc, tags))
        except Exception as e:
            print(f"Failed to read {fname}: {e}")

    return results
