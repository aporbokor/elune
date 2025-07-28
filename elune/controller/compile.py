import os
import subprocess
from . import rc


def compile(slug: str):
    dir_path = os.path.join(rc.ELUNE_PATH, slug)
    tex_file = os.path.join(dir_path, slug + ".tex")

    if not os.path.isfile(tex_file):
        print(f"No .tex file found for: {slug}")
        return

    try:
        subprocess.run(
            ["latexmk", "-xelatex", "-interaction=nonstopmode", tex_file],
            cwd=dir_path,
            check=True,
        )
        print(f"Compiled {tex_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed: {e}")
