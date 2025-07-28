import os
from pathlib import Path


# PS_HINTS = """#import "@local/evan:1.0.0":*
# #show: evan.with(maketitle:false)
# /*Input the problem and solution below.*/"""
PS_HINTS = """\\documentclass[12pt]{scrartcl}
\\usepackage{apor}
\\aporsetup
\\begin{document}
%%input the problem and solution below.
\\begin{prb*}[%s]
\\end{prb*}\n
\\end{document}"""
SEPARATOR = "\n---\n"
NSEPARATOR = "\n" + SEPARATOR + "\n"
EDITOR = os.environ.get("EDITOR")
ELUNE_PATH = str(Path.home().joinpath("Dropbox", "ELUNE"))
YAML_HINTS = """#input the problem metadata below.
source: {src} #must be specified
desc: <+> #must be specified
path: {path}
date: {date}
tags: <+> #@analysis, @calc, @linalg
{hint}"""
TAG_HINTS = """#Some hints for tags:
#
# Source: @imo @putnam @schweitzer @elmo @cmo
# Shape: @eval @findall @isthere
# Tactics: @invariant @symmetry @pigeonhole @extreme
# NT tags: @modular @p-adic @diophantine @powersum @pell
# Algebra tags: @funct-anal @polynomial @trig @roots @calculus
# Ineq tags: @amgm @cauchy @trivial @holder @schur @jensen @powermean @tangentline @muirhead
# Geo tags: @collinearity @concurrency @projection @inversion @homothecy @anglechase @simtri
# Combi tags: @pascals @blockwalk @binom @genfunc @partition @process"""
