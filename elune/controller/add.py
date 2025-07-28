import os
import tempfile
import subprocess
import datetime
import yaml
from . import rc
from .utils import escape_filename


def get_rawtext(template: str = "", extension: str = ".tmp") -> bytes:
    with tempfile.NamedTemporaryFile(suffix=extension) as tf:
        tf.write(template.encode("utf-8"))
        tf.flush()
        subprocess.call([rc.EDITOR, tf.name])
        tf.seek(0)
        return tf.read()


def get_problem_bodies(src: str, ext: str = ".tex") -> list[str]:
    template = rc.PS_HINTS % src
    return get_rawtext(template, ext).decode("utf-8").split(rc.SEPARATOR)


def get_yaml_tags(src: str):
    template = rc.YAML_HINTS.format(
        src=src,
        path=os.path.join(rc.ELUNE_PATH, escape_filename(src)),
        date=datetime.datetime.now(),
        hint=rc.TAG_HINTS,
    )
    rawtext = get_rawtext(template, ".yaml")

    try:
        data = yaml.safe_load(rawtext)
    except yaml.YAMLError as e:
        print(f"Error parsing yaml: {e}")
        return None

    path = data.get("path")
    if os.path.isdir(path):
        print("Directory already exists!")
        return
    if os.path.isfile(path):
        print("File already exists!")
        return
    return path, rawtext


def add(source: str):
    try:
        bodies = get_problem_bodies(source)
        target, rt = get_yaml_tags(source)
        # create yaml file
        with open(
            os.path.join(rc.ELUNE_PATH, escape_filename(source) + ".yaml"), "w"
        ) as f:
            f.write(rt.decode("utf-8"))
        os.mkdir(target)
        with open(os.path.join(target, escape_filename(source) + ".tex"), "w") as f:
            # f.write("/*")
            # f.write(rt)
            # f.write("*/")
            for b in bodies:
                f.write(b + "\n")
    except Exception as e:
        print("Failed to add problem: ", e)
