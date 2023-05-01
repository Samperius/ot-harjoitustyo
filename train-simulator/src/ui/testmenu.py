from ui.run_ui import run_simulation_window

import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (1200, 800))


def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')


def start_the_simulation() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    #global user_name
    print(f'{user_name.get_value()}, Do the job here!')
    value = n_trains.get_value()
    print(value)
    run_simulation_window(value)


menu = pygame_menu.Menu(
    height=800,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=1200
)
selected = 0
user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)
Tracks = menu.add.selector('Tracks: ', [('1', 1), ('2', 2)], onchange=set_difficulty)
n_trains = menu.add.range_slider(default=1, title='Number of trains', increment=1, range_values= (1,10),value_format=lambda x: str(int(x)))
menu.add.button('Play', start_the_simulation)
menu.add.button('Quit', pygame_menu.events.EXIT)

def main():
    menu.mainloop(surface)
