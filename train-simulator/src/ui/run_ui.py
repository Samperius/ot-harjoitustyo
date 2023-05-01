import numpy as np
import pygame
import pygame_menu
from pygame_menu import themes
from simulator.simulate import simulate
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection
from ui.ui import Ui



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



def run_simulation_window(n_trains):
    MAP = initialize_map()
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Train simulator")

    user_interface = Ui(MAP, CELL_SIZE, display)

    pygame.init()
    user_interface.all_sprites.draw(display)
    pygame.display.update()
    simulate(user_interface, n_trains)
    user_interface.all_sprites.draw(display)


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
