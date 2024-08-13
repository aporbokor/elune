import os

PS_HINTS = b"""/*Input the problem and solution below.*/"""
SEPARATOR = "\n---\n"
NSEPARATOR = "\n" + SEPARATOR + "\n"
EDITOR = os.environ.get("EDITOR")
ELUNE_PATH = "$HOME/Dropbox/elune/"
YAML_HINTS = b"""#Input the problem metadata below.\n
#source: %b #must be specified\n
#bodies: %b\n 
#tags: %b #\n
#date: %b"""
