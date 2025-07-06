import os
import shutil
from .rc import ELUNE_PATH
from .utils import escape_filename


def delete(name: str):
    slug = escape_filename(name)
    yaml_path = os.path.join(ELUNE_PATH, f"{slug}.yaml")
    folder_path = os.path.join(ELUNE_PATH, slug)

    if not os.path.exists(yaml_path):
        print(f"YAML file not found: {yaml_path}")
    else:
        os.remove(yaml_path)
        print(f"Deleted YAML: {yaml_path}")

    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
    else:
        shutil.rmtree(folder_path)
        print(f"Deleted folder: {folder_path}")
