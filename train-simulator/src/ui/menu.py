from ui.run_ui import animate_single_simulations
from ui.run_ui import run_many_simulations
import pygame_menu
import numpy as np
from pygame_menu.examples import create_example_window
from repositories.saving import Saving

def start_many_simulation():
    global n_trains
    global n_sim
    global waiting_time
    waiting_time = run_many_simulations( int(n_trains.get_value()), int(n_sim.get_value()))
    waiting_time = np.asarray(waiting_time)
    results(False)
def start_animated_simulation():
    global n_trains
    global waiting_time
    value = int(n_trains.get_value())
    waiting_time = animate_single_simulations(value)
    waiting_time = np.asarray(waiting_time)
    results(False)

def save_results():
    global n_trains
    global n_sim
    global waiting_time
    if type(n_trains) != int:
        n_trains = n_trains.get_value()
        n_sim = n_sim.get_value()
    data = {'number_of_simulations': [n_sim],
            'number_of_trains': [n_trains],
            'average_waiting_time': [np.mean(waiting_time)]}
    saving = Saving()
    saving.save_dataframe(data)
    print("results saved")
    mainmenu()

def mainmenu():
    global n_trains
    global n_sim
    global waiting_time
    surface = create_example_window('Train Simulator', (1200, 800))
    menu = pygame_menu.Menu(
        height=800,
        theme=pygame_menu.themes.THEME_BLUE,
        title='Welcome',
        width=1200
    )
    n_trains = menu.add.range_slider \
        (default=1, title='Number of trains', increment=1, range_values=(1, 5), value_format=lambda x: str(int(x)))
    menu.add.button('Animate single simulation', start_animated_simulation)
    n_sim = menu.add.range_slider \
        (default=1, title='Number of simulations', increment=1, range_values=(1, 5), value_format=lambda x: str(int(x)))

    menu.add.button('Run multiple simulations', start_many_simulation)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)

def results(saved):
    global n_trains
    global n_sim
    global waiting_time
    surface = create_example_window('Train Simulator', (1200, 800))
    menu = pygame_menu.Menu(
        height=800,
        theme=pygame_menu.themes.THEME_BLUE,
        title='Welcome',
        width=1200
    )
    menu.add.label(f'Previous simulation:')
    menu.add.label(f'Number of Trains: {int(n_trains.get_value())}, Number of simulations: {int(n_sim.get_value())}')
    menu.add.label(f'Average waiting time per simulation: {np.mean(waiting_time):.2f}')
    if not saved:
        menu.add.button('save results', save_results)
    menu.add.label(f'')
    n_trains = menu.add.range_slider \
        (default=int(n_trains.get_value()), title='Number of trains', increment=1, range_values=(1, 5), value_format=lambda x: str(int(x)))
    menu.add.button('Animate single simulation', start_animated_simulation)
    n_sim = menu.add.range_slider \
        (default=int(n_sim.get_value()), title='Number of simulations', increment=1, range_values=(1, 5), value_format=lambda x: str(int(x)))

    menu.add.button('Run multiple simulations', start_many_simulation)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)