import yaml
from . import rc


class Problem(yaml.YAMLObject):
    bodies = []
    source = ""
    tags = []
    date_added = None

    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, key, kwargs[key])


# def read_problem(text):
