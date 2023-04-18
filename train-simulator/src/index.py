import os
from ui.level import Level
from ui.run_ui import run_ui


def main():
    print(os.getcwd())
    run_ui(Level)


if __name__ == "__main__":
    main()
