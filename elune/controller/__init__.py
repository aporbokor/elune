import shlex
from tabulate import tabulate
from . import (
    add,
    delete,
    find,
    edit,
    view,
)


class EluneController:
    def __init__(self):
        self.last_find_results = []

    def do_add(self, f: str) -> None:
        if not f.strip():
            print("give argument plz")
            return
        return add.add(f.strip())

    def do_delete(self, f: str) -> None:
        if not f.strip():
            print("give argument plz")
            return
        return delete.delete(f.strip())

    def do_find(self, arg: str) -> None:
        """find [--tag TAG] [--source SOURCE]"""
        args = shlex.split(arg)
        tag = None
        source = None

        i = 0
        while i < len(args):
            if args[i] == "--tag":
                i += 1
                tag = args[i]
            elif args[i] == "--source":
                i += 1
                source = args[i]
            i += 1

        matches = find.find_problems(source=source, tag=tag)
        if not matches:
            print("No matching problems found.")
            return

        self.last_find_results = [fname[:-5] for fname, _, _ in matches]

        table_data = []
        for idx, (fname, src, tags) in enumerate(matches, 1):
            table_data.append([idx, fname[:-5], src, ", ".join(tags)])

        print(
            tabulate(
                table_data,
                headers=["id", "fname", "src", "tags"],
                tablefmt="fancy_grid",
            )
        )

    def do_edit(self, f: str) -> None:
        if not f.strip():
            print("give argument plz")
            return
        return edit.edit(f.strip())

    def do_view(self, f: str) -> None:
        if not f.strip():
            print("give argument plz")
            return

        f = f.strip()

        if f.isdigit():
            idx = int(f) - 1
            if not (0 <= idx < len(self.last_find_results)):
                print("Invalid selection index.")
                return
            f = self.last_find_results[idx]

        return view.view(f)
