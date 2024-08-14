import cmd2
from . import controller


class EluneTerminal(cmd2.Cmd, controller.EluneController):
    prompt = "\033[0;36melune) \033[0;0m"
    file = None
