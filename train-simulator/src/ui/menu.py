from ui.run_ui import run_simulation_window

import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (1200, 800))
def start_the_simulation() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    #global user_name
    value = int(n_trains.get_value())
    run_simulation_window(value)


menu = pygame_menu.Menu(
    height=800,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=1200
)
selected = 0
n_trains = menu.add.range_slider(default=1, title='Number of trains', increment=1, range_values= (1,5),value_format=lambda x: str(int(x)))
menu.add.button('Play', start_the_simulation)
menu.add.button('Quit', pygame_menu.events.EXIT)

def main():
    menu.mainloop(surface)
