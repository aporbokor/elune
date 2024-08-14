import os
from pathlib import Path


PS_HINTS = """/*Input the problem and solution below.*/"""
SEPARATOR = "\n---\n"
NSEPARATOR = "\n" + SEPARATOR + "\n"
EDITOR = os.environ.get("EDITOR")
ELUNE_PATH = str(Path.home().joinpath("Dropbox", "ELUNE"))
YAML_HINTS = """#Input the problem metadata below.
source: {src} #must be specified
desc: <+> #must be specified
path: {path}
date: {date}
tags: <+> #@analysis, @calc, @linalg
{hint}"""
TAG_HINTS = """#Some hints for tags:
#
# Source: @uni @mine
# Shape: @eval @findall @isthere
# NT tags: @modular @p-adic @diophantine @powersum @pell
# Algebra tags: @funct-anal @polynomial @trig @roots @calculus
# Ineq tags: @amgm @cauchy @trivial
# Geo tags: @collinearity @concurrency @projection @inversion @homothecy @anglechase @simtri
# Combo tags: @pascals @blockwalk @binom @genfunc @partition"""
