import os
import subprocess
import yaml
from .rc import ELUNE_PATH, EDITOR
from .utils import escape_filename


def edit_problem(problem_name: str):
    slug = escape_filename(problem_name)
    yaml_path = os.path.join(ELUNE_PATH, slug + ".yaml")

    if not os.path.isfile(yaml_path):
        print(f"No YAML found for: {problem_name}")
        return
    try:
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        target_dir = data["path"]
        tex_file = os.path.join(target_dir, slug + ".tex")

        if not os.path.isfile(tex_file):
            print(f"No .tex file found at: {tex_file}")
            return

        subprocess.call([EDITOR, tex_file])
    except Exception as e:
        print(f"Error editing {problem_name}: {e}")


def edit_yaml(problem_name: str):
    slug = escape_filename(problem_name)
    yaml_path = os.path.join(ELUNE_PATH, slug + ".yaml")

    if not os.path.isfile(yaml_path):
        print(f"No YAML file found for: {problem_name}")
        return

    try:
        subprocess.call([EDITOR, yaml_path])
    except Exception as e:
        print(f"Error opening YAML file: {e}")
