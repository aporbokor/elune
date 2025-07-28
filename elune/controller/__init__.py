import shlex
from tabulate import tabulate
from . import (
    add,
    delete,
    find,
    edit,
    view,
    compile,
)
from .utils import truncate


def with_resolved_filename(usage: str):
    def decorator(func):
        def wrapper(self, f: str):
            fname = self.resolve_filename(f)
            if not fname:
                print(f"Usage: {usage}")
                return
            return func(self, fname)

        return wrapper

    return decorator


class EluneController:
    def __init__(self):
        self.last_find_results = []

    def resolve_filename(self, arg: str) -> str | None:
        arg = arg.strip()

        if arg.isdigit():
            idx = int(arg) - 1
            if 0 <= idx < len(self.last_find_results):
                return self.last_find_results[idx]
            else:
                print(f"Invalid id: {arg} (out of range)")
                return None
        else:
            return arg if arg else None

    @with_resolved_filename("add $PROBLEM")
    def do_add(self, f: str) -> None:
        return add.add(f)

    @with_resolved_filename("delete $PROBLEM")
    def do_delete(self, f: str) -> None:
        return delete.delete(f)

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

        self.last_find_results = [fname[:-5] for fname, _, _, _ in matches]

        table_data = []
        for idx, (_, src, desc, tags) in enumerate(matches, 1):
            tag_str = ", ".join(tags)
            table_data.append([idx, src, truncate(desc, 40), truncate(tag_str, 15)])

        print(
            tabulate(
                table_data,
                headers=["id", "src", "desc", "tags"],
                tablefmt="github",
            )
        )

    @with_resolved_filename("ep $PROBLEM")
    def do_ep(self, f: str) -> None:
        return edit.edit_problem(f)

    @with_resolved_filename("ey $PROBLEM")
    def do_ey(self, f: str) -> None:
        return edit.edit_yaml(f)

    @with_resolved_filename("view $PROBLEM")
    def do_view(self, f: str) -> None:
        return view.view(f)

    @with_resolved_filename("compile $PROBLEM")
    def do_compile(self, f: str) -> None:
        return compile.compile(f)
