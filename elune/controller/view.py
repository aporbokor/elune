import os
import subprocess
import yaml
from .rc import ELUNE_PATH
from .utils import escape_filename


def view(problem_name: str):
    slug = escape_filename(problem_name)
    yaml_path = os.path.join(ELUNE_PATH, slug + ".yaml")

    if not os.path.isfile(yaml_path):
        print(f"No YAML found for: {problem_name}")
        return

    try:
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)

        target_dir = data["path"]
        pdf = os.path.join(target_dir, slug + ".pdf")

        if not os.path.isfile(pdf):
            print(f"No PDF found at: {pdf}")
            return

        subprocess.Popen(["xdg-open", pdf])
    except Exception as e:
        print(f"Error opening pdf: {e}")
