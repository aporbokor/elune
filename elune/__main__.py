from . import term


def main():
    t = term.EluneTerminal()
    t.debug = True
    t.cmdloop()


if __name__ == "__main__":
    main()
