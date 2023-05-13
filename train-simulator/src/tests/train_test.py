import unittest
import simpy
import numpy as np
import pygame
import pytest

from entities.train import Train
from entities.track import Track
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection
from ui.ui import Ui
from ui.game_loop import GameLoop, EventQueue, Renderer, Clock


width = 200
height = 50
MAP = np.zeros((height,width))
MAP[height//2,:] = np.ones(width)
MAP[height//2,0] = 2
MAP[height//2,width-1] = 2
MAP[height//2,width//2] = 2
MAP[height//2,width//3] = 3
CELL_SIZE = 1
DEFAULT_IMAGE_SIZE = np.array((CELL_SIZE, CELL_SIZE))


class TestTrack(unittest.TestCase):
    def setUp(self):
        print('debug')
        display_height = height * CELL_SIZE
        display_width = width * CELL_SIZE
        display = pygame.display.set_mode((display_width, display_height))
        ui = Ui(MAP, CELL_SIZE, display)
        connection = get_database_connection()
        track_repository = TrackRepository(connection)
        clock = Clock()
        renderer = Renderer(display, ui)
        event_queue = EventQueue()
        game_loop = GameLoop(renderer, event_queue, clock, CELL_SIZE)

        self.track = Track("Helsinki-P", "Tampere-P", track_repository)
        env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=1.0, strict=False)
        bottleneck = simpy.PreemptiveResource(env, capacity=1)
        self.train = Train(env, "Train", bottleneck, self.track, ui, game_loop, False)

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_move_x_train(self):
        before_move = self.train.rect.x
        self.train.move_train(11,5)
        print(self.train.move_train(11,0))
        after_move = self.train.rect.x
        self.assertEqual(before_move + 11, 110)
        print("done")

    def test_move_y_train(self):
        before_move = self.train.rect.y
        self.train.move_train(11,5)
        after_move = self.train.rect.y
        self.assertEqual(before_move + 11, 410)

    def test_print_next_stop(self):
        self.train.user_message('next_stop', True)
        out, err = self.capsys.readouterr()
        print(out)
        self.assertEqual("starting to drive to" in out, True)

    def test_print_station_reached(self):
        self.train.user_message('station_reached', True)
        out, err = self.capsys.readouterr()
        print(out)
        self.assertEqual("reached" in out, True)

    def test_print_bottleneck_passed(self):
        self.train.user_message('bottleneck_passed', True)
        out, err = self.capsys.readouterr()
        print(out)
        self.assertEqual("bottleneck passed" in out, True)

    def test_print_trip_complete(self):
        self.train.user_message('trip_complete', True)
        out, err = self.capsys.readouterr()
        print(out)
        self.assertEqual("trip complete" in out, True)
        