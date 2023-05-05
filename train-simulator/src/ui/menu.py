from ui.run_ui import animate_single_simulations
from ui.run_ui import run_many_simulations
import pygame_menu
from pygame_menu.examples import create_example_window
from pygame import font
def start_many_simulation() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """

    result = run_many_simulations( int(n_trains.get_value()), int(n_sim.get_value()))
    results(result)

def start_animated_simulation():
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    value = int(n_trains.get_value())
    animate_single_simulations(value)
    results()




def mainmenu():
    surface = create_example_window('Example - Simple', (1200, 800))
    menu = pygame_menu.Menu(
        height=800,
        theme=pygame_menu.themes.THEME_BLUE,
        title='Welcome',
        width=1200
    )
    selected = 0
    global n_trains
    global n_sim
    n_trains = menu.add.range_slider \
        (default=1, title='Number of trains', increment=1, range_values=(1, 5), value_format=lambda x: str(int(x)))
    menu.add.button('Animate single simulation', start_animated_simulation)
    n_sim = menu.add.range_slider \
        (default=1, title='Number of simulations', increment=1, range_values=(1, 5), value_format=lambda x: str(int(x)))

    menu.add.button('Run multiple simulations', start_many_simulation)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)

def results(result):
    surface = create_example_window('Train Simulator', (1200, 800))
    menu = pygame_menu.Menu(
        height=800,
        theme=pygame_menu.themes.THEME_BLUE,
        title='Welcome',
        width=1200
    )
    selected = 0
    global n_trains
    global n_sim
    menu.add.label(f'previous simulation: Trains{}, avg. waiting time{}')
    menu.add.label(f'resuls: {result}')
    menu.add.button('save results', print("saving or not :D"))
    n_trains = menu.add.range_slider \
        (default=1, title='Number of trains', increment=1, range_values=(1, 5), value_format=lambda x: str(int(x)))
    menu.add.button('Animate single simulation', start_animated_simulation)
    n_sim = menu.add.range_slider \
        (default=1, title='Number of simulations', increment=1, range_values=(1, 5), value_format=lambda x: str(int(x)))

    menu.add.button('Run multiple simulations', start_many_simulation)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
