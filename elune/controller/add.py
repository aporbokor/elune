import os
import sys
import tempfile
import re
import subprocess
import datetime
from . import rc


def escape_filename(value: str) -> str:
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def get_rawtext(skeleton=b"", extension: str = ".tmp"):
    with tempfile.NamedTemporaryFile(suffix=extension) as tf:
        print(tf.name)
        print(rc.EDITOR)
        tf.write(skeleton)
        tf.flush()
        subprocess.call([rc.EDITOR, tf.name])

        tf.seek(0)
        edited_message = tf.read()
        print(edited_message.decode("utf-8"))
        # print(edited_message.decode("utf-8"))
    return edited_message


def get_problem_bodies(sk=rc.PS_HINTS, ext: str = ".typ") -> list[str]:
    skeleton = sk + rc.NSEPARATOR.encode("utf-8")
    f = get_rawtext(skeleton, ext)
    f = f.decode("utf-8")
    print(f.split(rc.SEPARATOR))
    return f.split(rc.SEPARATOR)


def get_yaml_tags(src):
    get_rawtext(rc.YAML_HINTS, ".yaml")


def add(source: str):
    fname = escape_filename(source) + ".yaml"
    if os.path.isfile(fname):
        print("File already exists!")
        return

    return [
        get_problem_bodies(),
        source,
        # TODO: tags
        datetime.datetime.now(),
    ]
