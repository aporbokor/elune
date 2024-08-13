import cmd2
from . import controller


class EluneTerminal(cmd2.Cmd, controller.EluneController):
    prompt = "elune) "
    file = None
