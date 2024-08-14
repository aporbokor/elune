import os
import sys
import tempfile
import re
import subprocess
import datetime
import yaml
from . import rc


def escape_filename(value: str) -> str:
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def get_rawtext(template="", extension: str = ".tmp"):
    with tempfile.NamedTemporaryFile(suffix=extension) as tf:
        tf.write(template.encode("utf-8"))
        tf.flush()
        subprocess.call([rc.EDITOR, tf.name])
        tf.seek(0)
        edited_message = tf.read()
    return edited_message


def get_problem_bodies(tpl=rc.PS_HINTS, ext: str = ".typ") -> list[str]:
    template = tpl + rc.NSEPARATOR
    return get_rawtext(template, ext).decode("utf-8").split(rc.SEPARATOR)


def get_yaml_tags(src: str):
    template = rc.YAML_HINTS.format(
        src=src,
        path=os.path.join(rc.ELUNE_PATH, escape_filename(src)),
        date=datetime.datetime.now(),
        hint=rc.TAG_HINTS,
    )
    rawtext = get_rawtext(template, ".yaml")
    d = yaml.load(rawtext, Loader=yaml.Loader)
    if os.path.isdir(d["path"]):
        print("Directory already exists!")
        return
    if os.path.isfile(d["path"]):
        print("File already exists!")
        return
    return d["path"], rawtext


def add(source: str):
    bodies = get_problem_bodies()
    target, rt = get_yaml_tags(source)
    try:
        os.mkdir(target)
        with open(os.path.join(target, escape_filename(source) + ".typ"), "w") as f:
            # f.write("/*")
            # f.write(rt)
            # f.write("*/")
            for b in bodies:
                f.write(b + "\n")
    except:
        print("oops")
