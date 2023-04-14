from simulator.simulate import simulate
from ui.level import Level
from ui.run_ui import run_ui
import os

def main():
    print(os.getcwd())
    run_ui(Level)


if __name__ == "__main__":
    main()
