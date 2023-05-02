import unittest
import simpy
import numpy as np
import pygame

from entities.train import Train
from entities.track import Track
from repositories.track_repository import TrackRepository
from ui.ui import Ui


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
        stops = ["Helsinki", "Pasila", "Tikkurila", "Hämeenlinna",
                 "Tampere"]  # this data should be imported from database - to be modified later
        speed_limit = {"Pasila": 60, "Tikkurila": 70, "Hämeenlinna": 120,
                       "Tampere": 100}  # this data should be imported from database - to be modified later
        distances = {"Pasila": 5, "Tikkurila": 15, "Hämeenlinna": 100,
                     "Tampere": 100}  # this data should be imported from database - to be modified later

        display_height = height * CELL_SIZE
        display_width = width * CELL_SIZE
        display = pygame.display.set_mode((display_width, display_height))
        ui = Ui(MAP, CELL_SIZE, display)
        track_repo = TrackRepository()
        self.track = Track("Helsinki", "Tampere", stops,
                           speed_limit, distances, track_repo)
        env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=1.0, strict=False)
        bottleneck = simpy.PreemptiveResource(env, capacity=1)
        self.train = Train(env, "Train", bottleneck, self.track, ui)

    def test_move_x_train(self):
        before_move = self.train.rect.x
        self.train.move_train(11,0)
        after_move = self.train.rect.x
        self.assertEqual(before_move + 11, after_move)
        print("done")

    def test_move_y_train(self):
        before_move = self.train.rect.x
        self.train.move_train(11,0)
        after_move = self.train.rect.x
        self.assertEqual(before_move + 11, after_move)