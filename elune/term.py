import cmd2
from . import controller
from datetime import datetime
import os


class EluneTerminal(cmd2.Cmd, controller.EluneController):
    intro = f"\033[0;93mElune 0.1.0 ({datetime.now().strftime('%h')} {datetime.now().day} {datetime.now().year}) on {os.name}"
    prompt = "\033[1;33melune) \033[0;0m"
    file = None
