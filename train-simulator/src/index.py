import os
from ui.ui import Ui
from ui.run_ui import run_menu
from ui.run_ui import run_ui



def main():
    print(os.getcwd())
    run_ui(Ui)


if __name__ == "__main__":
    main()
