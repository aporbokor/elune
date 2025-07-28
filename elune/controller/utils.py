import re


def escape_filename(value: str) -> str:
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def truncate(s, w):
    return s if len(s) <= w else s[: w - 1] + "…"
