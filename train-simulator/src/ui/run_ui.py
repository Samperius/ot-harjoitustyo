import numpy as np
import pygame
from simulator.simulator import Simulator
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection
from ui.ui import Ui
from ui.game_loop import GameLoop, EventQueue, Renderer, Clock


width = 200
height = 400
MAP = np.zeros((height,width))
MAP[height//2,:] = np.ones(width)
MAP[height//2,0] = 2

MAP[height//2,width-1] = 2
MAP[height//2,width//2] = 2
MAP[height//2,width//3] = 3
CELL_SIZE = 3


def initialize_map():
    """
        Simulaatiokäyttöliitymän pohjan alustamiseen tarkoitettu funktio.
        :return: palauttaa pohjan, jota simulaatiokäyttöliittymä tarvitsee
        """
    MAP = np.zeros((height, width))
    connection = get_database_connection()
    track_repository = TrackRepository(connection)
    stops = track_repository.return_all_start_stops()
    bottlenecks = track_repository.return_all_bottlenecks()

    for stop in stops:
        direction = stop.split("-")[1]
        stop_coordinate = track_repository.station_xy_coordinates(stop)
        if direction == "P" or direction == "E":
            MAP[:, stop_coordinate[0]-1] = np.ones(height)

        if direction == "L" or direction == "I":
            MAP[stop_coordinate[1]-1, :] = np.ones(width)
    for stop in stops:
        stop_coordinate = track_repository.station_xy_coordinates(stop)
        MAP[stop_coordinate[1]-1, stop_coordinate[0]-1] = 2

    for bottleneck in bottlenecks:
        bottleneck_coordinate = track_repository.station_xy_coordinates(bottleneck)
        MAP[bottleneck_coordinate[1] - 1, bottleneck_coordinate[0] - 1] = 3
    return MAP

def run_many_simulations(n_trains, n_simulations):
    """
        Funktio, joka huolehtii käyttöliittymän käynnistyksestä luoden Simulaatio-luokan usean simulaation suorittamiseksi.
        :param n_trains: Junien lukumäärä
        :param n_simulations: Simulaatioiden lukumäärä
        :return: palauttaa tulokset tallennusta ja esittämistä varten
        """
    MAP = initialize_map()
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Train simulator")
    user_interface = Ui(MAP, CELL_SIZE, display)
    clock = Clock()
    renderer = Renderer(display, user_interface)
    event_queue = EventQueue()
    game_loop = GameLoop(renderer, event_queue, clock, CELL_SIZE)
    pygame.init()
    simulation = Simulator(user_interface, n_trains, game_loop)
    result = simulation.simulate_many(n_simulations)
    game_loop.start()
    return result


def animate_single_simulations(n_trains):
    """
        Funktio, joka huolehtii käyttöliittymän käynnistyksestä luoden Simulaatio-luokan animoidun simulaation suorittamiseksi.
        :param n_trains: Junien lukumäärä
        :return: palauttaa tulokset tallennusta ja esittämistä varten
        """
    MAP = initialize_map()
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Train simulator")
    user_interface = Ui(MAP, CELL_SIZE, display)
    clock = Clock()
    renderer = Renderer(display, user_interface)
    event_queue = EventQueue()
    game_loop = GameLoop(renderer, event_queue, clock, CELL_SIZE)
    pygame.init()
    simulation = Simulator(user_interface, n_trains, game_loop)
    result = simulation.simulate_animated()
    game_loop.start()
    return result

