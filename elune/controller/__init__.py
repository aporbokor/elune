from . import (
    add,
)


class EluneController:
    prompt = "elune) "
    file = None

    def do_add(self, f: str) -> None:
        return add.add(f)
